-- Banking Interview Deck — Supabase schema
-- Run once, whole file, in the project's SQL editor (New query → paste → Run).
-- Safe to re-run: every statement is idempotent.

-- ---------------------------------------------------------------- codes --
-- Registration codes live here, not in the page. RLS is on and there are no
-- policies, so nothing on the client can read this table; only the signup
-- trigger below (security definer) can.
create table if not exists public.app_config (
  key   text primary key,
  value text not null
);
alter table public.app_config enable row level security;

insert into public.app_config (key, value) values
  ('join_code',    'JLA2026'),
  ('teacher_code', 'JLA2026@')
on conflict (key) do update set value = excluded.value;

-- ------------------------------------------------------------- profiles --
create table if not exists public.profiles (
  id         uuid primary key references auth.users on delete cascade,
  name       text not null default '',
  email      text not null default '',
  role       text not null default 'student' check (role in ('student', 'teacher')),
  created_at timestamptz not null default now()
);
alter table public.profiles enable row level security;

create or replace function public.is_teacher()
returns boolean
language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from public.profiles
    where id = auth.uid() and role = 'teacher'
  );
$$;

drop policy if exists "profiles readable by owner or teacher" on public.profiles;
create policy "profiles readable by owner or teacher" on public.profiles
  for select using (id = auth.uid() or public.is_teacher());

drop policy if exists "profiles updatable by owner" on public.profiles;
create policy "profiles updatable by owner" on public.profiles
  for update using (id = auth.uid());

-- --------------------------------------------------- registration gate ---
-- Runs on every signup. The code travels in the signup metadata; an unknown
-- code aborts the signup, so the page cannot hand itself a teacher role.
create or replace function public.handle_new_user()
returns trigger
language plpgsql security definer set search_path = public as $$
declare
  supplied     text := coalesce(new.raw_user_meta_data ->> 'code', '');
  join_code    text;
  teacher_code text;
  assigned     text;
begin
  select value into join_code    from public.app_config where key = 'join_code';
  select value into teacher_code from public.app_config where key = 'teacher_code';

  if supplied = teacher_code then
    assigned := 'teacher';
  elsif supplied = join_code then
    assigned := 'student';
  else
    raise exception 'invalid registration code';
  end if;

  insert into public.profiles (id, name, email, role)
  values (new.id, coalesce(new.raw_user_meta_data ->> 'name', ''), new.email, assigned);
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ------------------------------------------------------------- progress --
create table if not exists public.progress (
  user_id    uuid not null references auth.users on delete cascade,
  card_id    text not null,
  mastered   boolean not null default false,
  bookmarked boolean not null default false,
  flagged    boolean not null default false,
  seen       boolean not null default false,
  note       text,
  updated_at timestamptz not null default now(),
  primary key (user_id, card_id)
);
alter table public.progress enable row level security;
create index if not exists progress_user_idx on public.progress (user_id);

drop policy if exists "progress readable by owner or teacher" on public.progress;
create policy "progress readable by owner or teacher" on public.progress
  for select using (user_id = auth.uid() or public.is_teacher());

drop policy if exists "progress insert own" on public.progress;
create policy "progress insert own" on public.progress
  for insert with check (user_id = auth.uid());

drop policy if exists "progress update own" on public.progress;
create policy "progress update own" on public.progress
  for update using (user_id = auth.uid());

drop policy if exists "progress delete own" on public.progress;
create policy "progress delete own" on public.progress
  for delete using (user_id = auth.uid());

-- -------------------------------------------------------- class summary --
-- security_invoker keeps the policies above in force: a student selecting
-- from this view sees one row, a teacher sees the class. Needs Postgres 15+,
-- which every current Supabase project runs.
create or replace view public.class_summary with (security_invoker = on) as
select
  p.id,
  p.name,
  p.email,
  p.role,
  count(*) filter (where pr.mastered)                             as mastered,
  count(*) filter (where pr.seen)                                 as seen,
  count(*) filter (where pr.flagged)                              as flagged,
  count(*) filter (where pr.note is not null and pr.note <> '')   as notes,
  max(pr.updated_at)                                              as last_studied
from public.profiles p
left join public.progress pr on pr.user_id = p.id
group by p.id, p.name, p.email, p.role;
