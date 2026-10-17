# Interview Banking

A flashcard site for investment banking interview preparation, with student
accounts, cohort tags and an editor workflow.

**Live:** https://interviewbanking.tech

```
flashcards/   the site itself — this folder is what gets deployed
build/        turns the question bank into the deck the site loads
data/         the question bank: questions, answers, sources
docs/         audits, quality reports and review material
supabase/     database schema, applied in numbered order
```

## The three moving parts

**The deck is a file.** `build/build_data.py` reads `data/` and writes
`flashcards/data.json`, tagging every card by topic, difficulty, firm, cohort
and known issues. Nothing is computed in the browser.

```bash
cd build && python3 build_data.py
```

**The site is one page.** `flashcards/index.html` holds the layout, styles and
logic with no build step and no framework. It loads `data.json`, and
`flashcards/config.js` points it at Supabase.

**The database holds people, not questions.** Accounts, progress, cohort tags,
problem reports and teacher edits live in Supabase. Teacher edits are stored as
overrides and laid over the deck at load, so correcting a card takes effect for
everyone without rebuilding or redeploying.

## Setting up the database

Run these in the Supabase SQL editor, in order:

| File | What it adds |
| --- | --- |
| `supabase/01_core.sql` | Profiles, progress, row level security, the class view |
| `supabase/02_collab.sql` | Problem reports, teacher edits with history |
| `supabase/03_access.sql` | Access codes, cohort tags, hiding a card |
| `supabase/04_scopes.sql` | Scoped editors: who an editor may see and change |
| `supabase/seed_codes.local.sql` | **Your codes — not in this repository** |

The codes are deliberately absent. Copy `seed_codes.example.sql` to
`seed_codes.local.sql`, put your real codes in it, and run it last; git ignores
that filename. `supabase/SETUP.md` has the full walkthrough.

## Who can do what

- **Students** study, mark progress, keep private notes, and report a problem
  on any card.
- **Editors** (a teacher code) handle reports, edit or hide cards for everyone,
  and manage the cohorts in their scope — only those.
- **The owner** (one code) sees every cohort and editor, and manages the codes.

Scope is enforced by row level security, not by hiding buttons: an editor
calling the API directly still cannot read or tag anyone outside their cohorts.

## What is not here

The M&I guide PDF the question bank was compiled from is not in this
repository, and should not be: it is a paid product. The bank itself is a
rewritten, consolidated set of prompts with prepared answers.

Answers are study answers, not model answers from the firms named on each card.
Firm labels record where a question was reported in the source material.
`docs/audits/` records which topics have been checked for accuracy and what was
found; `docs/quality/question_flags.md` records which cards are incomplete,
time-sensitive or open-ended.
