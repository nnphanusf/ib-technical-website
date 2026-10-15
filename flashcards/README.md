# Banking Interview Deck

Flashcard app built from the question bank in the parent folder.

**Online:** https://claude.ai/artifact/9EGd9DfFSLCzVnyUTKBHea (private to your Claude account)

**Offline:** double-click `index.html` — it loads `data.js` directly from disk, no server needed.
To serve it instead:

```bash
cd "/Users/jimphan/Downloads/new folder/flashcards" && python3 -m http.server 8777
```

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app — layout, styles, logic. No build step, no dependencies. |
| `build_data.py` | Turns the two source files into the deck. Re-run after editing the rules. |
| `data.json` | The deck, fetched by the hosted version. |
| `data.js` | The same deck as a script, used when the page is opened from the filesystem. |

Sources read by the build script (parent folder):
`Technical_Questions_and_Answers.json` and `Investment_Banking_Questions.txt`.

## What's in the deck

3,234 cards: 2,049 technical questions with prepared answers, 1,185 behavioral questions
with a preparation framework per category (behavioral answers have to be your own stories —
the frameworks say how to structure them).

Every card carries five filterable tags:

- **Collection** — IB Fundamentals (M&I 400) or Firm Interview Insights
- **Firm** — 83 firms, normalised from the office/group labels in the source ("Goldman Sachs TMT SF" → Goldman Sachs)
- **Industry / group** — Healthcare, Technology & Media, Restructuring, FIG, Real Estate, Credit & Leveraged Finance, Private Equity, Markets & Trading and others, inferred from the source label and the question text
- **Topic** — 27 topics: Accounting & 3 Statements, DCF, Valuation & Comps, Merger Model & M&A, LBO, Accretion / Dilution, Enterprise & Equity Value, Options & Derivatives, plus the behavioral topics
- **Difficulty** — Basic or Advanced

Tags are derived by rule in `build_data.py`, not taken from the source files. They are good for
filtering, not an official taxonomy — to retag, edit the keyword rules near the top of the script
and re-run it.

Firm labels record where a question was reported in your source material. The answers are
prepared study answers; they were not supplied or endorsed by those firms.

## Signing in

The page opens on a sign-in card. Each student creates a profile with a name and their own
password; creating one also needs the class password (set in `index.html` — share it with the
class, not in this repo). Profiles keep students on a shared computer out of each other's
progress, bookmarks and notes.

This is browser-side only: there is no server, so a profile lives in the browser it was made in
and the check can be bypassed by anyone who reads the page source. Treat it as a doorlatch
between classmates, not as security.

## Using it

Space reveals the answer and moves on, arrow keys navigate, `M` marks mastered, `B` bookmarks,
`F` flags for review, `S` reshuffles, `E` jumps to your notes, `?` lists every shortcut.
Progress, bookmarks and your own notes are saved per profile in the browser you study in — they
do not follow you to another device, so use **Copy progress** on the Mastery tab before switching.
`T` switches the light and dark themes, and **Always show answers** in the filter rail reveals
every card without pressing space, for revision runs.
