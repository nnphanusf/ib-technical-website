-- Run this entire file in the existing project's Supabase SQL Editor.
-- Preserves existing registration codes and adds another student code.
begin;

insert into public.app_config (key, value)
values ('join_code_usf', 'USFFTP2026')
on conflict (key) do update set value = excluded.value;

create or replace function public.handle_new_user()
returns trigger
language plpgsql security definer set search_path = public as $$
declare
  supplied text := coalesce(new.raw_user_meta_data ->> 'code', '');
  join_code text;
  teacher_code text;
  assigned text;
begin
  select value into join_code from public.app_config where key = 'join_code';
  select value into teacher_code from public.app_config where key = 'teacher_code';

  if supplied = teacher_code then
    assigned := 'teacher';
  elsif supplied = join_code or exists (
    select 1 from public.app_config where key = 'join_code_usf' and value = supplied
  ) then
    assigned := 'student';
  else
    raise exception 'invalid registration code';
  end if;

  insert into public.profiles (id, name, email, role)
  values (new.id, coalesce(new.raw_user_meta_data ->> 'name', ''), new.email, assigned);
  return new;
end;
$$;

commit;
