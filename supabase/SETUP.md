# Turning on cross-device accounts

The deck works without any of this — profiles and progress live in the browser.
Follow these steps and the same accounts work on every device instead, with a
teacher view that reads the whole class.

Roughly 15 minutes, no cost: the Supabase free tier covers a class comfortably.

## 1. Create the project

1. Sign up at [supabase.com](https://supabase.com) (GitHub login works)
2. **New project** → name it (e.g. `ib-deck`), pick the region closest to you,
   set a database password and save it in your password manager
3. Wait about two minutes for it to provision

## 2. Create the tables

1. Open **SQL Editor** → **New query**
2. Paste the whole of [`schema.sql`](schema.sql) and press **Run**

That creates the profiles and progress tables, the row-level-security policies,
the class summary view, and the signup trigger that checks registration codes.

## 3. Switch off email confirmation

**Authentication** → **Sign In / Providers** → **Email** → turn **Confirm email**
off, and Save.

Do this before students register. With it on, everyone has to click a link in an
email first, and Supabase's built-in mailer is rate-limited to a handful of
messages per hour — fine for you testing, not for a class signing up at once.

## 4. Copy the two values into the site

**Project Settings** → **API Keys**: copy the **Project URL** and the
**publishable** key into `flashcards/config.js`:

```js
window.SUPA_URL = "https://xxxxxxxxxxxx.supabase.co";
window.SUPA_KEY = "sb_publishable_xxxxxxxxxxxxxxxx";
```

Supabase is retiring the old `anon` key (the long `eyJ...` string) by the end of
2026. A new project gives you a publishable key instead — take that one. If your
project only shows a legacy anon key, it still works.

Commit, push, and the host redeploys. The page detects the config and switches
from browser storage to Supabase on its own.

That key belongs in the page — it is designed to be public, and carries no more
privilege than an anonymous visitor. The row-level security policies in
`schema.sql` are what protect the data, not the key.

## 5. Check it

1. Open the site, **Register**, use the student code
2. Sign in with the same email on your phone — the progress should be there
3. Register a second account with the teacher code and open the **Class** tab

## Running it

**Changing the codes** — in the SQL editor:

```sql
update public.app_config set value = 'NEWCODE' where key = 'join_code';
```

**Removing a student** — Authentication → Users → delete. Their progress rows go
with them.

**Resetting a password** — Authentication → Users → the row's menu.

**Free tier pauses** after about a week with no activity; the dashboard restores
it in one click. Term-time use keeps it awake.

## What this does and does not do

- Accounts and progress follow a student to any device they sign in on
- Passwords are hashed by Supabase; the registration codes live in a table the
  page cannot read, and the signup trigger refuses any other code
- A teacher profile can read every student's progress — keep that code to yourself
- The deck contents (`data.json`) stay public to anyone with the site URL. This
  protects accounts, not the questions
- The artifact copy on claude.ai cannot reach Supabase (its sandbox blocks
  outside connections), so that one stays browser-only
