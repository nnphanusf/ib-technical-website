-- Scoped editors: who an editor may see and change
-- Run after schema_access.sql. Safe to re-run.
--
-- JLA2026@ creates the owner: sees everyone, every code, every editor.
-- WEditorFTP and BTNFF_TCH create scoped editors: each sees only the cohorts
-- in their scope, and can only hand out tags from that scope.
-- All of it is enforced by row level security, not by hiding buttons.

-- ------------------------------------------------- people carry several tags --
alter table public.profiles add column if not exists tags        text[] not null default '{}';
alter table public.profiles add column if not exists admin_scope text[] not null default '{}';
alter table public.profiles add column if not exists is_owner    boolean not null default false;

update public.profiles
   set tags = array[tag]
 where tag is not null and cardinality(tags) = 0;

alter table public.access_codes add column if not exists admin_scope text[] not null default '{}';
alter table public.access_codes add column if not exists is_owner    boolean not null default false;

update public.access_codes set admin_scope = array['USF Finance Talent Pathway', 'FTP Teacher']
 where code = 'WEditorFTP';
update public.access_codes set admin_scope = array['BTNFF Fellow', 'BTNFF Mentor/Editor']
 where code = 'BTNFF_TCH';
update public.access_codes set is_owner = true, admin_scope = '{}'
 where code = 'JLA2026@';

-- whoever already holds the owner code keeps the rights
update public.profiles p set is_owner = true
 where p.role = 'teacher' and 'My Love' = any (p.tags);

-- --------------------------------------------------------------- helpers --
create or replace function public.is_owner()
returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and is_owner);
$$;

create or replace function public.my_scope()
returns text[] language sql stable security definer set search_path = public as $$
  select coalesce(admin_scope, '{}') from public.profiles where id = auth.uid();
$$;

-- An editor may see a person when any of that person's tags is in their scope.
create or replace function public.can_see(target_tags text[])
returns boolean language sql stable security definer set search_path = public as $$
  select public.is_owner()
      or (public.is_teacher() and coalesce(target_tags, '{}') && public.my_scope());
$$;

-- ------------------------------------------------------- profile policies --
drop policy if exists "profiles readable by owner or teacher" on public.profiles;
drop policy if exists "read own profile" on public.profiles;
drop policy if exists "profiles visible" on public.profiles;
create policy "profiles visible" on public.profiles
  for select using (id = auth.uid() or public.can_see(tags));

drop policy if exists "profiles updatable by owner" on public.profiles;
drop policy if exists "update own profile" on public.profiles;
drop policy if exists "teachers update profiles" on public.profiles;
drop policy if exists "profiles editable" on public.profiles;
create policy "profiles editable" on public.profiles
  for update using (id = auth.uid() or public.can_see(tags));

-- The policy decides who may touch a row; this decides what they may change.
create or replace function public.guard_profile_update()
returns trigger language plpgsql security definer set search_path = public as $$
declare
  scope    text[];
  untouched text[];
  chosen   text[];
begin
  if public.is_owner() then
    return new;                                   -- the owner may set anything
  end if;

  if public.is_teacher() and old.tags && public.my_scope() then
    scope := public.my_scope();
    -- Tags outside this editor's scope are invisible to them, so they are
    -- carried across untouched; only the in-scope part of the list is theirs
    -- to change.
    untouched := array(select unnest(old.tags) except select unnest(scope));
    chosen    := array(select unnest(coalesce(new.tags, '{}')) intersect select unnest(scope));
    new.tags        := array(select distinct unnest(untouched || chosen));
    new.is_owner    := old.is_owner;              -- nobody promotes themselves
    new.admin_scope := case when new.role = 'teacher' then scope else '{}' end;
    return new;
  end if;

  -- anyone else, including a student editing their own row
  new.role        := old.role;
  new.tags        := old.tags;
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
    or public.can_see((select p.tags from public.profiles p where p.id = progress.user_id))
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

  insert into public.profiles (id, name, email, role, tag, tags, admin_scope, is_owner)
  values (new.id,
          coalesce(new.raw_user_meta_data ->> 'name', ''),
          new.email,
          rec.role,
          rec.tag,
          array[rec.tag],
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
  p.tags,
  p.is_owner,
  count(*) filter (where pr.mastered)                           as mastered,
  count(*) filter (where pr.seen)                               as seen,
  count(*) filter (where pr.flagged)                            as flagged,
  count(*) filter (where pr.note is not null and pr.note <> '') as notes,
  max(pr.updated_at)                                            as last_studied
from public.profiles p
left join public.progress pr on pr.user_id = p.id
group by p.id, p.name, p.email, p.role, p.tags, p.is_owner;

grant select on public.class_summary to authenticated;
