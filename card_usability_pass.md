# Card usability pass — tax assumptions, answer structure, welded questions

Three changes requested together, all applied to `Technical_Questions_and_Answers.json` and rebuilt.
The deck goes from 3,234 to 3,239 cards.

---

## 1. A 20% tax rate instead of a symbolic `t`

Of the 209 Accounting & 3 Statements cards, **60 answers carried a symbolic tax rate** and only one
of those questions stated a rate. A student reading "net income falls d(1-t)" has to do algebra
before they can rehearse an answer out loud, which is the opposite of what a flashcard is for.

**54 answers now use concrete numbers at 20%**, and **45 questions gained the sentence "Assume a
20% tax rate."** Only 8 accounting cards still carry a symbolic rate, and all 8 are the formula
questions listed below. The questions that already state their own rate keep it — F0102 at 40%,
F1714 at
20%, F0919 at 60%, F0781's illustrative 20% — because overriding a rate the question gives would
break the question.

**Formulas were deliberately left alone where the question asks for one**, as instructed:

| Card | Why it keeps the formula |
| --- | --- |
| F0112 | asks "with x tax rate" explicitly |
| F0193, F0797, F1168, F1326, F1452 | ask for the FCFF / FCFE formulas themselves |
| F1278 | asks *why* you multiply EBIT by (1-t) |
| F1480 | asks about depreciation policy, not a worked case |

F0845 is the exception that proves the rule: it asks you to *calculate* a company's tax rate, so
assuming one would defeat the question. It now derives the effective rate as Income Tax Expense /
Pre-Tax Income and distinguishes the statutory, effective and cash tax rates, which also closes a
gap flagged in `accounting_audit.md`.

## 2. Answer structure follows the 400 guide

Measuring first was worth it, because the diagnosis was not the obvious one:

| | cards | median length | p90 |
| --- | ---: | ---: | ---: |
| M&I 400 guide answers | 309 | 714 chars | 1,107 |
| prepared answers | 1,172 | 613 chars | 804 |

**The prepared answers were already shorter than the guide's.** Length was never the problem. What
the guide does and the prepared answers did not is *structure*: 29 guide answers use
`• Income Statement: / • Cash Flow Statement: / • Balance Sheet: / • Intuition:` and **zero of
1,172 prepared answers used any labelled structure at all.** A 600-character wall of prose is
harder to follow than a 700-character answer in four labelled steps, which is exactly what you were
seeing.

So the 54 rewritten answers follow the guide's pattern: one line of setup, a labelled bullet per
statement, and a closing `• Intuition:` line that says what actually happened in cash. For example
F0038 now reads:

> A $10 increase in depreciation, with the deduction usable now and a 20% tax rate.
> • Income Statement: depreciation is an operating expense, so EBIT and Pre-Tax Income fall $10 and
> Net Income falls $8.
> • Cash Flow Statement: Net Income is down $8, but you add back the $10 of non-cash depreciation,
> so cash rises $2.
> • Balance Sheet: Cash +$2 and Net PP&E -$10, so assets fall $8; Retained Earnings falls $8, so
> both sides fall $8 and balance.
> • Intuition: the only cash effect is the $2 tax saving, because the asset was paid for earlier.

**One fix to the page was needed to make this work.** `paragraphs()` in `flashcards/index.html`
only started a new paragraph after `. ` followed by a capital letter or quote mark, so a `•` never
triggered a break — every bulleted answer rendered as one unbroken block. That was already
happening to the 29 guide answers. The renderer now treats a bullet as the start of its own
paragraph, so each step gets its own line. This improves the guide cards as much as the new ones.

Every rewritten answer's arithmetic was checked to balance: assets equal liabilities plus equity in
all 54, and the cash-flow line reconciles to the balance-sheet cash movement. That includes the
multi-step worked cases, which are the ones worth re-checking if you change a rate later: F0901
(inventory bought with PIK debt, sold at double), F0833 (book depreciation against MACRS, which
throws off a $20 deferred tax liability), F0900, F0782, F1515 and F0621.

The answers were written once per template family and applied across the cards sharing that family,
which is how the deck already worked — deferred revenue (14 cards), depreciation (10), accounts
payable (3), accounts receivable (3), PIK interest (7), inventory (3), write-downs and asset sales
(2), plus 12 individually worked multi-step cases.

---

## 3. Welded questions: flagged and split

Detection found cards carrying three or more separate interrogative prompts, excluding the guide's
`Context: ... Follow-up: ...` cards, which are deliberate two-step questions and were left alone.
The first detection pass missed cards whose prompts were separated by full stops rather than
question marks — F0933 is the clearest, three unrelated prompts and only one question mark — so the
rule was rewritten to split on sentence boundaries too.

### Split: 16 cards had genuinely unrelated prompts

The important discovery is that **the deck already has a standalone card for almost every welded
sub-prompt.** Creating a new card for each part would have produced about 35 duplicates of
questions the deck already answers. So each welded card was **narrowed to its one distinctive
prompt**, with the other parts pointed at the card that already owns them. The original welded
wording is preserved in each card's `question_variants`, and each card now carries a note telling a
student where the other parts went.

| Card | Narrowed to | Parts that already had a home |
| --- | --- | --- |
| **F0390** | what beta you would expect for a given stock | 9 prompts, 8 of them covered: F0091, F0702, F0274, F0238, F0038, F0043, F0775, F0037, F0854 |
| **F1696** | how companies relieve financial distress | DCF (F0037), other methods (F0091), a recent deal (F1170) |
| **F0201** | one turn of multiple vs $5 of EBITDA | mental arithmetic; the EV-to-equity bridge (F1128) |
| **F0698** | is debt always cheaper than equity | the balls puzzle → **new card F2501** |
| **F0887** | the senior/subordinated waterfall and the 500 offer | $10 depreciation (F0038) |
| **F0933** | what is on JPMorgan's balance sheet | bat and ball → **F2502**; moral dilemma → **F2503** |
| **F1007** | depreciation falling $20 | stock pitch (F0089/F0570), valuation (F0091), CAPM (F0274) |
| **F1154** | depreciation rising $5 | DCF (F0037), macro event (F0186), unlever beta (F1408), statements (F0043) |
| **F1292** | the Chicago–New York flight estimate | $5 depreciation (F1154); why credit investing |
| **F1089** | US vs China cost of equity | story, why Lazard, why IB, why LA — all behavioral |
| **F1290** | which bond moves more when yields fall | mental arithmetic; covenants → **new card F2504** |
| **F1093** | EPS at 15x when the tax rate falls | F0828, F1704, F0029 |
| **F0212** | written down TO vs BY $80 | EV calc (F0342), EV on new debt (F1535), asset sale (F0796) |
| **F0327** | $100 more cash and enterprise value | revolver vs TL (F0051), multiples (F1577), beta (F0238), rev to FCF (F0113) |
| **F0844** | all-debt accretion at a 15x purchase multiple | the separate EV calculation (F0342/F1828) |
| **F1321** | Black-Scholes and the out-of-the-money call puzzle | Panama Canal → **new card F2505** |

### Five parts had no home, so they became cards

- **F2501** — the 50 blue / 50 red balls puzzle. 74/99, about 74.7%.
- **F2502** — bat and ball. $0.25 and $1.25.
- **F2504** — which three covenants to focus on in an indenture.
- **F2505** — what you would pay for exclusive rights to the Panama Canal.
- **F2503** — the moral-dilemma question. This one is behavioral, not technical. It stays in the
  technical file because that is where its source note lives, and its own note says so; move it to
  the behavioral deck if you would rather it sat with the other ethics questions.

### Left alone: 9 cards whose follow-ups are logical

These ask several things, but each follows from the last, which is how a real interview proceeds.
Splitting them would destroy the point:

- **F1091** three multiples on the same deal · **F1092** accretion, new shares and EPS for the same
  two companies · **F1799** cost of equity against market return, then the risk-free rate, then
  beta · **F2170** a question with "if so" and "if not" branches · **F0623** the coin game, then
  whether you would pay to play it · **F1939** your view on a deal, then whether you would have
  done it · **F1805** three facts about the same firm · **F0177** convertible debt for biotech, then
  its trade-offs against equity · **F0411** a $10 rise in AR, then a $10 cash sale.

All the guide's `Context: ... Follow-up:` cards are the same case and were not split. They were
later reformatted - see section 5.

Three behavioral cards (B0542, B0596, B1049) also carry multiple prompts. They are in the
behavioral file and outside this pass.

---

## 4. The same structure outside the accounting topic

The topic router files a card by its question wording, so plenty of three-statement walkthroughs sit
in other topics — Apple's factories in Debt & Restructuring, the chemical plant in Quant &
Brainteasers, the laptop purchase in Industry & Company Analysis. Thirty-eight such answers existed
outside Accounting & 3 Statements, and **23 of them were genuine worked transactions** and now use
the same labelled structure and the same 20% assumption.

The other 15 were deliberately left in prose, because they are not transactions: "walk me through
the three statements" (F0043), "how are they linked" (F0775), "walk me through building a
three-statement model" (F0307, F1223), the IFRS differences (F1956), and the missing-input cards
that describe the bridge as a method rather than working a case (F0111, F0322, F0370, F0463, F1591,
F0120, F1116, F0861, F1585, F1586). Bulleting a description of how the statements connect would add
structure without adding clarity.

**108 cards now carry the labelled structure**, across Accounting (58), Debt & Restructuring (20),
Industry & Company Analysis (12), Merger Model (5), Valuation & Comps (3), DCF (2), LBO (2) and FIG
(2).

Where a card already stated its own tax rate, that rate was kept and the structure written around
it: F0628 at 33%, F1757 at 40%, F1745 and F2154 at the guide's 25%. **Every structured card was then
cross-checked so that the rate in the question matches the rate used in the answer** — that
check caught four cards whose only percentage was an interest rate, so the tax assumption had been
skipped, one card where a 20% tag had been added to an answer that uses the guide's 25%, one
question that ended up claiming both "assume 20%" and "tax assumptions are not recorded", and six
answers carrying a leaked `{M}` placeholder from the rewrite script. All are fixed; the check now
reports zero mismatches and zero placeholders.

Twelve M&I guide cards that state 25% only in the answer now say so in the question too, so a
student reading the prompt alone knows what to assume.

---

## What to check

The accounting answers are the ones students will hit most, so spot-check a few on the page:
F0038 and F1771 for depreciation, F0023 for deferred revenue, F1709 for receivables, F0613 for PIK.
Outside accounting, F0058 (Apple's factories over three years) and F1404 (a part-debt factory with a
principal repayment) are the most involved.
Each should show four or five short labelled lines rather than a block of prose. If the bullets run
together instead of breaking onto their own lines, the `index.html` change did not deploy.

---

## 5. Release of reviewed tags, and the Context cards

Five changes requested together. The deck goes from 3,239 to 3,238 cards.

**23 cards cleared by hand.** The structural heuristics had flagged them; you read them and judged
them askable as written. Rather than weaken the heuristics - which would let genuinely broken cards
through - `build_data.py` now carries a `CLEARED_ISSUES` set that overrides the flags for a named
id. All 29 ids in it now read Verified with no tags.

**F1941** now reads *"Tell me about an M&A deal. What were the main risk factors in this deal?"*
It is in the cleared set too, which is one more than the 23 you named: the rewrite supplies the
context its dangling-reference flag was complaining about, so the flag no longer describes the card.

**18 `Context:` cards now break into paragraphs.** The word is gone and each `Follow-up:` starts its
own paragraph. Two fixes were needed to make this hold:

- `tidy_punctuation()` collapsed all whitespace runs, destroying the breaks on every rebuild. It now
  protects a deliberate blank line through the collapse with a sentinel.
- The question rendered as a single escaped `<h2>`, which never ran through the paragraph splitter,
  so newlines did nothing on the page. `index.html` now splits the question on blank lines.

F2085 had a doubled `Context: Context:` and now reads as three parts. You named five cards; the
other 13 carry the identical format, so they got the same formatting for consistency. **Their tags
were left alone** - clearing a tag is a judgment about content, and you only reviewed the five.

**"Needs the missing context" is now "Input Required"**, on 76 cards. No card carries the old label.

**F1945 is deleted.**

