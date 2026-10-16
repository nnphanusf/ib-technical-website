# USF interview workbooks — import

Two workbooks were read in full and merged into the deck: the USF Interview + Offers Database
24-25 and the internship tracking sheet. The deck goes from 3,238 to 3,318 cards.

| | |
| --- | ---: |
| Question-bearing rows read | 236 |
| Distinct questions extracted | 174 |
| Kept after curation | 82 |
| **Added as new cards** | **80** (66 behavioral, 14 technical) |
| Existing cards given a new firm source | 14 |
| Firms in the deck | 100 (was 83) |
| Industry groups | 18 (was 15) |

## Where the questions came from

The two files hold different things, and treating them the same would have produced junk.

- **The tracking sheet** is the gold seam: 27 rows, each a numbered list of the questions actually
  asked, verbatim, with the firm and the round. Almost everything in it is usable.
- **The USF database** is mostly a description of the *process* — "3 rounds: HR screener,
  behavioral, superday" — with questions quoted only occasionally. Its real value is the
  **Findings** sheet, which assigns every firm a General Area (IB, PE, ER, AM, S&T, WM, CM, CB, CT,
  OP, FP). That is the industry map the import is built on.

## What was dropped, and why

92 of the 174 extracted lines were not added. They fall into three groups, and every one was read
before being dropped:

- **Process description** — "Pymetrics", "Superday (not invited)", "Completed 2 rounds, no Super
  day", "Traditionally 4-5 rounds, depends on candidate." These describe the format, not a
  question.
- **Interview commentary** — "N/A - don't remember", "They don't touch non-target for NY",
  "*networked into the firm, no official application." This is the same class of noise that the
  behavioral deck already carries 19 cards of, and the point of this pass was not to add more.
- **Fragments** — half-questions whose other half was in a different cell, and reconstructions that
  would have required inventing the question. Where a note said only "asked about EBITDA,
  financial statements", nothing was added, because guessing the wording would put words in an
  interviewer's mouth.

Where a note did contain a real question inside prose, it was lifted out: "What are your thoughts
about AI?" from an Ares superday note, "Gross and net revenue retention without a calculator" from
an Alpine Software Group round.

## How firm and industry were attached

Each new card carries a source of the form `Morgan Stanley — Equity Research (USF 24-25)`. Two
things read that label:

- `parent_firm()` takes the firm, so the card appears under Morgan Stanley. This needed **17 new
  firms** added to the firm list — Freddie Mac, Walmart, Delta Air Lines, Amgen, Accenture, PGIM,
  BNY Mellon, Fidelity, First Citizens Bank, Mariner Wealth Management, Diamond Hill Capital,
  Alliance Bernstein, Crosstree, PEI Global, Dubin Clark, Huron Consulting and FTI Consulting —
  without which the whole label would have been treated as the firm name.
- `groups_for()` now maps the USF area straight to a group instead of guessing from keywords. This
  matters: the existing router matches substrings, and "BMO Capital Markets" is a firm name, not a
  capital-markets desk. The USF tag short-circuits that and uses the area the workbook recorded.

Three groups were added to hold work the deck had no home for: **Corporate Finance** (Freddie Mac,
Walmart, Delta, Amgen), **Consulting** (Accenture, Huron, FTI, RSM) and **Operations & Risk**
(Goldman's Controllers, Internal Audit and Risk divisions). They are reachable only through the USF
tag, so no existing card moved.

A late catch worth recording: three of the new technical cards were being tagged with the wrong
industry because the *answers* mentioned a trigger word — the airline break-even answer listed
"insurance" among fixed costs and was filed under FIG. The group router reads question and answer
together. The answers were reworded ("hull and liability cover"), which is both accurate and
untagged.

## The 14 technical cards

These needed written answers, since the technical deck stores a real answer per card rather than a
framework. Each was written for this import and checked:

Bond prices against yields in plain language (Freddie Mac) · risk versus control (Goldman Sachs
Internal Audit) · how much to lend against a million in cash (Goldman Sachs) · what each financial
statement tells a reader (Delta) · a regional-airline break-even, which works out to 125 passengers
on $80 of contribution against $10,000 of fixed cost (Delta) · valuing a machinery company
(Morgan Stanley) · what moves paper and packaging prices (Morgan Stanley) · good business with bad
management or the reverse (BNY Mellon) · how to find a business's multiple (Crosstree) · why two
companies with identical statements are valued differently (PEI Global) · hedging a two-stock
position, what a sales and trading desk does, futures, and derivatives (all Nomura).

## Firm credit on questions the deck already had

Fourteen of the harvested questions were already in the deck — a DCF walkthrough, the three
statements, the $10 depreciation question, CAPM, why private equity, questions for the interviewer.
Adding them again would have made duplicates, so instead the firm was added as a source on the
existing card. F0037 now credits BNP Paribas and PEI Global, F0043 credits Nomura and Amgen, and
B0020 credits First Citizens Bank and Goldman Sachs.

One correction made during this pass: Goldman's plain "walk through resume" prompt was first
attached to B0192, which asks about deals at your current shop. That is a different question, so it
was moved to B0020.

## Behavioral guidance

All 66 new behavioral cards route to a question-level guidance family. Reaching that took widening
sixteen existing patterns and adding one new family — **contributing to diversity and inclusion**,
which Blackstone, Morgan Stanley and Piper Sandler each ask almost word for word and which the deck
had no guidance for at all. A bare "Why Walmart?" is now recognised as a why-this-firm question by
checking the name against the firm list rather than by keyword.

Deck-wide behavioral coverage rose from 71% to 74% as a side effect.

## What this import does not do

The USF database's RESPONSES sheet carries offer outcomes, difficulty ratings, GPA bands and
sponsorship status per interview. None of that was imported — it is applicant data rather than
question data, and some of it is personal. Only the question text, the firm and the area were taken.
