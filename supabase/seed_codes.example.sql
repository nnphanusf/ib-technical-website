-- Registration codes — COPY THIS FILE, do not edit it in place.
--
--   cp seed_codes.example.sql seed_codes.local.sql
--
-- seed_codes.local.sql is ignored by git. Put your real codes there and run it
-- in the SQL editor after 03_access.sql and 04_scopes.sql. Anyone holding a
-- code can register, so it does not belong in a public repository.

insert into public.access_codes (code, tag, role, note, admin_scope, is_owner) values
  -- a student cohort: tag only, no rights over anyone
  ('STUDENT_CODE_A', 'Cohort A', 'student', 'Example', '{}', false),

  -- an editor for that cohort: sees and tags Cohort A and its editors
  ('EDITOR_CODE_A',  'Cohort A Editor', 'teacher', 'Editing rights',
   array['Cohort A', 'Cohort A Editor'], false),

  -- the owner: sees every cohort, every editor and every code
  ('OWNER_CODE',     'Owner', 'teacher', 'Full rights', '{}', true)
on conflict (code) do update
  set tag = excluded.tag, role = excluded.role, note = excluded.note,
      admin_scope = excluded.admin_scope, is_owner = excluded.is_owner, active = true;

-- Name the owner. An account made before tags existed has none, so the owner
-- flag has to be set by address.
update public.profiles
   set is_owner = true, role = 'teacher', tags = array['Owner']
 where email = 'you@example.com';
