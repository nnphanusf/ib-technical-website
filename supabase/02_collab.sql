-- Reporting, teacher edits and highlights
-- Run after 01_core.sql, in the project's SQL editor. Safe to re-run.

-- ------------------------------------------------------------- reports --
-- A student flags a card; teachers see the queue.
create table if not exists public.card_reports (
  id          uuid primary key default gen_random_uuid(),
  card_id     text not null,
  reported_by uuid not null references auth.users on delete cascade,
  reason      text not null default '',
  status      text not null default 'open' check (status in ('open', 'resolved', 'dismissed')),
  created_at  timestamptz not null default now(),
  resolved_by uuid references auth.users,
  resolved_at timestamptz
);
alter table public.card_reports enable row level security;
create index if not exists card_reports_open_idx on public.card_reports (status, created_at desc);

drop policy if exists "report own" on public.card_reports;
create policy "report own" on public.card_reports
  for insert with check (reported_by = auth.uid());

drop policy if exists "read own reports or teacher" on public.card_reports;
create policy "read own reports or teacher" on public.card_reports
  for select using (reported_by = auth.uid() or public.is_teacher());

drop policy if exists "teachers resolve reports" on public.card_reports;
create policy "teachers resolve reports" on public.card_reports
  for update using (public.is_teacher());

-- ----------------------------------------------------------- overrides --
-- The teacher-maintained layer that sits on top of the shipped deck. The page
-- loads data.json, then applies any row here, so an edit reaches every learner
-- on their next load without rebuilding the deck.
create table if not exists public.card_overrides (
  card_id    text primary key,
  question   text,
  answer     text,
  sources    text,                    -- the "reported by" line
  origin     text,                    -- where the answer came from
  edited_by  uuid references auth.users,
  updated_at timestamptz not null default now()
);
alter table public.card_overrides enable row level security;

drop policy if exists "overrides readable by all signed in" on public.card_overrides;
create policy "overrides readable by all signed in" on public.card_overrides
  for select using (auth.uid() is not null);

drop policy if exists "teachers write overrides" on public.card_overrides;
create policy "teachers write overrides" on public.card_overrides
  for all using (public.is_teacher()) with check (public.is_teacher());

-- Every save keeps the previous text, so a bad edit can be read back.
create table if not exists public.card_override_history (
  id        bigint generated always as identity primary key,
  card_id   text not null,
  question  text,
  answer    text,
  sources   text,
  origin    text,
  edited_by uuid,
  saved_at  timestamptz not null default now()
);
alter table public.card_override_history enable row level security;

drop policy if exists "teachers read history" on public.card_override_history;
create policy "teachers read history" on public.card_override_history
  for select using (public.is_teacher());

create or replace function public.log_card_override()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  -- On an update, file the version being replaced. On the first edit there is
  -- nothing to file: the original wording is still in the deck file.
  if TG_OP = 'UPDATE' then
    insert into public.card_override_history (card_id, question, answer, sources, origin, edited_by)
    values (old.card_id, old.question, old.answer, old.sources, old.origin, old.edited_by);
  end if;
  new.updated_at := now();
  new.edited_by := auth.uid();
  return new;
end;
$$;

drop trigger if exists card_overrides_logged on public.card_overrides;
create trigger card_overrides_logged
  before insert or update on public.card_overrides
  for each row execute function public.log_card_override();

-- ---------------------------------------------------------- highlights --
-- Per learner, per card. Ranges are character offsets into the plain text of
-- that field: [{"s": 12, "e": 48, "c": "yellow"}]
create table if not exists public.highlights (
  user_id    uuid not null references auth.users on delete cascade,
  card_id    text not null,
  field      text not null check (field in ('question', 'answer')),
  ranges     jsonb not null default '[]'::jsonb,
  updated_at timestamptz not null default now(),
  primary key (user_id, card_id, field)
);
alter table public.highlights enable row level security;
create index if not exists highlights_user_idx on public.highlights (user_id);

drop policy if exists "own highlights" on public.highlights;
create policy "own highlights" on public.highlights
  for all using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists "teachers clear reports" on public.card_reports;
create policy "teachers clear reports" on public.card_reports
  for delete using (public.is_teacher());

-- --------------------------------------------------------------- grants --
-- Without these every request comes back 42501, whatever the policies say.
grant select, insert                 on public.card_reports          to authenticated;
grant update, delete                 on public.card_reports          to authenticated;
grant select, insert, update, delete on public.card_overrides        to authenticated;
grant select                         on public.card_override_history to authenticated;
grant select, insert, update, delete on public.highlights            to authenticated;
