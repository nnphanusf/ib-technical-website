-- Access codes, cohort tags, and hiding a card
-- Run after schema.sql and schema_collab.sql. Safe to re-run.

-- --------------------------------------------------------- cohort tags --
alter table public.profiles add column if not exists tag text;

-- Each registration code carries the cohort tag it grants and whether it
-- creates a teacher. Editing a row here changes what the code does next time
-- it is used; it does not touch people who already registered.
create table if not exists public.access_codes (
  code       text primary key,
  tag        text not null,
  role       text not null default 'student' check (role in ('student', 'teacher')),
  note       text,
  active     boolean not null default true,
  created_at timestamptz not null default now()
);
alter table public.access_codes enable row level security;

drop policy if exists "teachers manage codes" on public.access_codes;
create policy "teachers manage codes" on public.access_codes
  for all using (public.is_teacher()) with check (public.is_teacher());

insert into public.access_codes (code, tag, role, note) values
  ('USFFTP2026', 'USF Finance Talent Pathway', 'student', 'Cohort 2026'),
  ('USFFTP',     'USF Finance Talent Pathway', 'student', null),
  ('WEditorFTP', 'FTP Teacher',                'teacher', 'Editing rights'),
  ('JLA2026',    'My Love',                    'student', null),
  ('JLA2026@',   'My Love',                    'teacher', 'The original teacher code'),
  ('BTNFF_ST',   'BTNFF Fellow',               'student', null),
  ('BTNFF_TCH',  'BTNFF Mentor/Editor',        'teacher', 'Editing rights'),
  ('INV_ONLY',   'By Personal Invitation',     'student', null)
on conflict (code) do update
  set tag = excluded.tag, role = excluded.role, note = excluded.note, active = true;

-- The signup gate now reads that table instead of two fixed codes.
create or replace function public.handle_new_user()
returns trigger
language plpgsql security definer set search_path = public as $$
declare
  supplied text := coalesce(new.raw_user_meta_data ->> 'code', '');
  rec      public.access_codes%rowtype;
begin
  select * into rec from public.access_codes where code = supplied and active;
  if not found then
    raise exception 'invalid registration code';
  end if;

  insert into public.profiles (id, name, email, role, tag)
  values (new.id, coalesce(new.raw_user_meta_data ->> 'name', ''), new.email, rec.role, rec.tag);
  return new;
end;
$$;

-- A teacher can change someone's cohort or make them an editor later on.
drop policy if exists "teachers update profiles" on public.profiles;
create policy "teachers update profiles" on public.profiles
  for update using (public.is_teacher()) with check (public.is_teacher());

-- The class view carries the tag, so the teacher can group by cohort.
create or replace view public.class_summary with (security_invoker = on) as
select
  p.id,
  p.name,
  p.email,
  p.role,
  p.tag,
  count(*) filter (where pr.mastered)                           as mastered,
  count(*) filter (where pr.seen)                               as seen,
  count(*) filter (where pr.flagged)                            as flagged,
  count(*) filter (where pr.note is not null and pr.note <> '') as notes,
  max(pr.updated_at)                                            as last_studied
from public.profiles p
left join public.progress pr on pr.user_id = p.id
group by p.id, p.name, p.email, p.role, p.tag;

-- ------------------------------------------------------- hiding a card --
-- A hidden card stays in the deck file but disappears from every learner's
-- deck. Clearing the flag brings it back, so nothing is destroyed.
alter table public.card_overrides add column if not exists hidden boolean not null default false;

-- ---------------------------------------------------------------- grants --
grant select, insert, update, delete on public.access_codes to authenticated;
grant select                         on public.class_summary to authenticated;
