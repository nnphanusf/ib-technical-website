-- Scoped editors: who an editor may see and change (one tag per person)
-- Run after 03_access.sql. Safe to re-run.
--
-- The code marked is_owner creates the owner: sees everyone, every code,
-- every editor. A code carrying an admin_scope creates a scoped editor, who
-- sees only the cohorts in that scope and can only hand out tags from it.
-- All of it is enforced by row level security, not by hiding buttons.

-- --------------------------------------------------------- the columns --
alter table public.profiles add column if not exists admin_scope text[] not null default '{}';
alter table public.profiles add column if not exists is_owner    boolean not null default false;

-- An earlier version let a person hold several tags. Collapse any such list
-- back into the single tag before the column goes.
do $$
begin
  if exists (select 1 from information_schema.columns
              where table_schema = 'public' and table_name = 'profiles' and column_name = 'tags') then
    execute 'update public.profiles set tag = coalesce(tag, tags[1]) where tag is null';
  end if;
end $$;

-- The view, the policies and the helper all read the old array column, so they
-- have to go before it does. Everything here is recreated further down.
drop view if exists public.class_summary;

drop policy if exists "profiles visible" on public.profiles;
drop policy if exists "profiles editable" on public.profiles;
drop policy if exists "profiles readable by owner or teacher" on public.profiles;
drop policy if exists "read own profile" on public.profiles;
drop policy if exists "profiles updatable by owner" on public.profiles;
drop policy if exists "update own profile" on public.profiles;
drop policy if exists "teachers update profiles" on public.profiles;
drop policy if exists "progress readable" on public.progress;
drop policy if exists "progress readable by owner or teacher" on public.progress;
drop function if exists public.can_see(text[]);

alter table public.profiles drop column if exists tags;

alter table public.access_codes add column if not exists admin_scope text[] not null default '{}';
alter table public.access_codes add column if not exists is_owner    boolean not null default false;

-- Which code grants which scope, and which one is the owner, is set in
-- seed_codes.local.sql rather than here.

-- Whoever registered with the owner code keeps the rights.
update public.profiles p set is_owner = true
  from public.access_codes c
 where c.is_owner and p.role = 'teacher' and p.tag = c.tag;

-- Naming the owner is also in seed_codes.local.sql: it needs a real address.

-- Editors who were promoted before scopes existed get one from their tag.
update public.profiles p
   set admin_scope = sub.scope
  from (
    select pr.id,
           coalesce(array_agg(distinct sc), '{}') as scope
      from public.profiles pr
      left join public.access_codes c on c.tag = pr.tag
      left join lateral unnest(c.admin_scope) sc on true
     where pr.role = 'teacher'
     group by pr.id
  ) sub
 where p.id = sub.id
   and p.is_owner = false
   and coalesce(array_length(p.admin_scope, 1), 0) = 0;

-- --------------------------------------------------------------- helpers --
create or replace function public.is_owner()
returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and is_owner);
$$;

create or replace function public.my_scope()
returns text[] language sql stable security definer set search_path = public as $$
  select coalesce(admin_scope, '{}') from public.profiles where id = auth.uid();
$$;

-- An editor may see a person when that person's tag is in their scope.
drop function if exists public.can_see(text[]);
create or replace function public.can_see(target_tag text)
returns boolean language sql stable security definer set search_path = public as $$
  select public.is_owner()
      or (public.is_teacher() and target_tag is not null and target_tag = any (public.my_scope()));
$$;

-- ------------------------------------------------------- profile policies --
drop policy if exists "profiles readable by owner or teacher" on public.profiles;
drop policy if exists "read own profile" on public.profiles;
drop policy if exists "profiles visible" on public.profiles;
create policy "profiles visible" on public.profiles
  for select using (id = auth.uid() or public.can_see(tag));

drop policy if exists "profiles updatable by owner" on public.profiles;
drop policy if exists "update own profile" on public.profiles;
drop policy if exists "teachers update profiles" on public.profiles;
drop policy if exists "profiles editable" on public.profiles;
create policy "profiles editable" on public.profiles
  for update using (id = auth.uid() or public.can_see(tag));

-- The policy decides who may touch a row; this decides what they may change.
create or replace function public.guard_profile_update()
returns trigger language plpgsql security definer set search_path = public as $$
declare
  scope text[];
begin
  -- Promoting someone to editor has to give them a scope, or they would sign
  -- in able to see nobody: take it from the code that grants their tag.
  if new.role = 'teacher' and coalesce(array_length(new.admin_scope, 1), 0) = 0 then
    select coalesce(array_agg(distinct sc), '{}')
      into new.admin_scope
      from public.access_codes c, unnest(c.admin_scope) sc
     where c.tag = new.tag;
  elsif new.role <> 'teacher' then
    new.admin_scope := '{}';
  end if;

  if public.is_owner() then
    return new;                                   -- the owner may set anything
  end if;

  scope := public.my_scope();

  if public.is_teacher() and old.tag = any (scope) then
    -- An editor may move someone between their own cohorts, not out of them.
    if new.tag is null or not (new.tag = any (scope)) then
      new.tag := old.tag;
    end if;
    new.is_owner    := old.is_owner;              -- nobody promotes themselves
    new.admin_scope := case when new.role = 'teacher' then scope else '{}' end;
    return new;
  end if;

  -- anyone else, including a student editing their own row
  new.role        := old.role;
  new.tag         := old.tag;
  new.admin_scope := old.admin_scope;
  new.is_owner    := old.is_owner;
  return new;
end;
$$;

drop trigger if exists profiles_guarded on public.profiles;
create trigger profiles_guarded
  before update on public.profiles
  for each row execute function public.guard_profile_update();

-- --------------------------------------------------- progress and codes --
drop policy if exists "progress readable by owner or teacher" on public.progress;
drop policy if exists "progress readable" on public.progress;
create policy "progress readable" on public.progress
  for select using (
    user_id = auth.uid()
    or public.can_see((select p.tag from public.profiles p where p.id = progress.user_id))
  );

-- Only the owner sees or changes the access codes.
drop policy if exists "teachers manage codes" on public.access_codes;
drop policy if exists "owner manages codes" on public.access_codes;
create policy "owner manages codes" on public.access_codes
  for all using (public.is_owner()) with check (public.is_owner());

-- ------------------------------------------------------- signup, updated --
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
declare
  supplied text := coalesce(new.raw_user_meta_data ->> 'code', '');
  rec      public.access_codes%rowtype;
begin
  select * into rec from public.access_codes where code = supplied and active;
  if not found then
    raise exception 'invalid registration code';
  end if;

  insert into public.profiles (id, name, email, role, tag, admin_scope, is_owner)
  values (new.id,
          coalesce(new.raw_user_meta_data ->> 'name', ''),
          new.email,
          rec.role,
          rec.tag,
          rec.admin_scope,
          rec.is_owner);
  return new;
end;
$$;

-- ---------------------------------------------------- class view, updated --
drop view if exists public.class_summary;
create view public.class_summary with (security_invoker = on) as
select
  p.id,
  p.name,
  p.email,
  p.role,
  p.tag,
  p.is_owner,
  count(*) filter (where pr.mastered)                           as mastered,
  count(*) filter (where pr.seen)                               as seen,
  count(*) filter (where pr.flagged)                            as flagged,
  count(*) filter (where pr.note is not null and pr.note <> '') as notes,
  max(pr.updated_at)                                            as last_studied
from public.profiles p
left join public.progress pr on pr.user_id = p.id
group by p.id, p.name, p.email, p.role, p.tag, p.is_owner;

grant select on public.class_summary to authenticated;
