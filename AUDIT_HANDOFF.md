# Flashcard accuracy audit — handoff

Paste the block below into a fresh session to continue the audit.

---

## Context

Repo: `/Users/jimphan/Downloads/new folder` — an investment banking interview flashcard web app.
`flashcards/index.html` is a static page built from a question bank by `flashcards/build_data.py`.
3,234 cards: 2,049 technical with prepared answers, 1,185 behavioral. Live at
nnphanusf.github.io/ib-technical-website/flashcards/. The Supabase backend doesn't matter here.

The technical answers were written by an AI, not a banker. A student is handing this deck to
classmates, so a wrong answer gets repeated in real interviews. **Accuracy matters more than
speed, and overstating what was verified is worse than reporting a small number of findings
honestly.**

An earlier structural pass checked card shape only (`question_flags.md`, the `vf`/`iss` fields).
This is the finance check, running topic by topic.

## Task

Audit every card in the next topic for factual accuracy of the answer text.

For each card: recompute any arithmetic, check the direction and magnitude of every income
statement / balance sheet / cash flow effect against US GAAP convention, and check that the
answer's stated assumptions are consistent with what it concludes. Work in batches of roughly
20 cards so the review stays careful; do not skim.

Record findings in a new `<topic>_audit.md` at the repo root: card id, the wrong claim, why it is
wrong, and the corrected wording. **Where an answer is defensible but incomplete or ambiguous,
note it separately from outright errors — do not inflate the error count.**

Corrections go in the source file `Technical_Questions_and_Answers.json` (the `answer` field),
**not** in `flashcards/data.json` or the page. Then `cd flashcards && python3 build_data.py` to
rebuild, and commit. **Do not push** — the user pushes from VS Code. Commit messages end with:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

## Progress: 1,459 of 2,049 technical cards audited, 44 errors found and corrected

| Topic | Cards | Errors | Audit file | Commit |
| --- | ---: | ---: | --- | --- |
| Accounting & 3 Statements | 209 | 4 | `accounting_audit.md` | `615df46` |
| DCF & Intrinsic Value | 222 | 5 | `dcf_audit.md` | `4b4f671` |
| Enterprise & Equity Value + Accretion / Dilution | 158 | 4 | `ev_accretion_audit.md` | `b512c56` |
| Debt, Credit & Restructuring | 261 | 4 | `restructuring_audit.md` | `4d062bb` |
| Valuation & Comps | 153 | 13 | `valuation_audit.md` | `d949203` |
| Merger Model & M&A + LBO & Private Equity | 225 | 4 | `merger_lbo_audit.md` | `e2c9092` |
| Options, FIG, Quant, Deal Process, Markets, Stock Pitch | 231 | 8 | `specialty_audit.md` | see log |

Two of the Enterprise & Equity Value errors were reclassified from "incomplete" during the Merger
Model pass, which also restored four lost guide answers in other topics; `merger_lbo_audit.md`
explains both. The Valuation & Comps tranche was done by a separate session.

`answer_review.md` is the original 27-card sample that started this. Read the audit files before
beginning — they record the method, the error bar used, and the leads below.

## Remaining: 590 technical cards, in one topic

| Topic | Cards | Priority |
| --- | ---: | --- |
| Industry & Company Analysis | 590 | the only one left |

Expect a low error yield: this topic is mostly qualitative and firm-specific, and the
checkable surface is small. Audit it in three groups of roughly 200.


To pull one topic's cards:

```python
import json
cards = json.load(open('flashcards/data.json'))['cards']
src = {q['question_id']: q for q in
       json.load(open('Technical_Questions_and_Answers.json'))['questions']}
ids = [c['id'] for c in cards if c['tp'] == 'Valuation & Comps']
```

Card fields: `id`, `tp` (topic), `q`, `a`. Source fields: `question_id`, `question`, `answer`,
`answer_status`, `answer_type`, `notes`.

## Known leads, not yet acted on

No specific defect is sitting unfixed. What is left is one cluster worth a mechanical pass, and
two scans already run that need no repeating.

**The IRR-levers cluster (LBO & Private Equity, worth fixing, needs no new finance).** Five cards
ask how to raise LBO returns and none gets the enumeration: F0787, F1187, F1324, F1663, F0444.
Meanwhile F0445 — which asks something else — carries exactly that list, and F2096 states the three
canonical drivers cleanly. F0445 and F0787 look like a straight swap. `merger_lbo_audit.md` has the
detail.

**Already scanned deck-wide; do not repeat.** Guide answers truncated at the start (three found and
fixed); guide-sourced questions whose worked answer was replaced by a shared template (four found
and fixed); and plain-language questions answered technically (seven found, six still open — see
below). All three classes are now mapped.

**The plain-language cluster, open by choice.** Six cards ask for an explanation to a child, a
grandmother or "as simply as possible" and return a technical paragraph: F0460, F0725, F1202, F1266,
F1309, F1432. Nothing in them is false, so they are not errors, but the register *is* the question.
F0450 (working capital as a lemonade stand) shows the house style to match. Fixing them is six short
pieces of writing, not an accuracy correction, which is why an accuracy pass left them alone.

## What the first 1,459 cards taught — read this before starting

**The finance is strong; the routing is what breaks.** Of the 23 errors found in these
tranches, only 3 were finance errors
(a blanket "lease principal is financing cash flow" that is false for operating leases under
ASC 842; a claim that the ECB and Bank of England issue government bonds; and a $100 equipment
purchase answered as a $100 depreciation charge). **Every arithmetic card in all five tranches
recomputed correctly**, including PIK accretion, MACRS-vs-book deferred tax, debt extinguishment,
recovery waterfalls, accretion/dilution, and two YTMs needing a quadratic and a five-period
annuity. Budget attention accordingly: **check template-to-question fit first, recompute second.**

**The dominant defect is template misassignment.** Roughly half the cards share about a dozen
answer templates. The templates are accurate; they are often attached to questions they don't
answer. The signature is stable: a keyword in the question pulls in the template about that
keyword's usual topic.

- "options" → option-pricing template (F0584, an enterprise value question)
- "current" → dated-research template (F0862, "current liabilities")
- "liquidation" → bank-valuation template (F0608, Chapter 7)
- "two companies with the same X" → identical-companies template (F0599/F0600/F0601)

**Method that works: when you find one, grep the template's first sentence across the whole
source and check every card it lands on.** That found F0601 and the two Valuation & Comps cards
above, and in an earlier tranche it found three truncated guide cards in topics nobody had
audited. Same rule for any mechanical defect: on the second instance, stop and scan deck-wide.

**Sub-patterns worth grepping for, none needing finance knowledge to spot:**
- direction questions ("what happens to X if Y rises") answered with a definition template that
  never states the direction
- "give an example of..." answered with a template containing no example — the deck usually HAS
  the example on a sibling card
- "explain it simply / to a 10-year-old" answered with the full technical paragraph

## Practical gotchas

- **Reading the M&I guide PDF.** 30-40 cards per topic are transcriptions from
  `M&I 2025 400 IB Questions-2.pdf`. No pdftotext or poppler on this machine, but
  `pip install --target <scratchdir> pypdf` works offline and `extract_text()` is clean enough to
  grep. **Do this for any `guide_answer` card before editing it** — distinguishing a transcription
  slip from the guide's own error changes the right fix. A deck-wide truncation scan has already
  been run and cleared, so don't repeat it.
- **Overriding guide text.** The bar used so far: correct it only when reciting it would be
  plainly wrong out loud. That bar was met once (the ECB/BoE claim). Two guide slips were
  deliberately left alone and documented instead.
- **`build_data.py` has heuristics that misfire.** `TIME_PAT`, `INCOMPLETE_PAT` and
  `DANGLING_PAT` derive the user-facing verification flags from question text. One bug was
  already fixed (`TIME_PAT` matched "current" inside "current liabilities", mis-tagging a card as
  needing fresh research). If a card shows an odd template assignment, check these regexes before
  assuming the answer was written badly.
- **The user commits to this repo while you work.** Stage only your own files; never `git stash`,
  `reset` or switch branches.
- Hand-over notes from the four completed tranches are in
  `/Users/jimphan/Library/Application
Support/Claude/side-session-notes/local_3780a44e-8b11-4c98-8b60-567305df354d/`

## Done looks like

Every card in the topic read, `<topic>_audit.md` listing errors with corrections and incomplete
cards noted separately, source corrections applied, rebuilt, committed (not pushed), and a
summary of how many cards were wrong.
