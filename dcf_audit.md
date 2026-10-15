# DCF & Intrinsic Value — full accuracy audit

**Scope: all 222 cards with topic "DCF & Intrinsic Value" in `flashcards/data.json`, read in full.**
Same method as the Accounting pass (`accounting_audit.md`): every number recomputed, every formula
checked against convention, every stated assumption tested against the conclusion drawn from it.

Composition: 113 concept/method, 65 model answers, 30 M&I guide transcriptions, 7 missing-input,
6 dated-research, 1 open framework.

## Result

| | Cards |
| --- | ---: |
| Read in full | 222 |
| **Errors** | **5** |
| Defensible but incomplete, mismatched or ambiguous | 48 |
| Verified correct | 169 |

Every formula and every computed number in this topic is correct. I recomputed the Hamada
unlevering and relevering, the CAPM partial derivatives, the Gordon Growth and mid-year
conventions, both M&I lease walkthroughs, the utility rate case, three perpetuity problems
including an arithmetic-gradient perpetuity, and the bond-duration comparison — all right.

The errors are all one failure mode, the same one the Accounting pass found: **a shared answer
template attached to a question it does not fit.** None is a miscalculation.

The incomplete count is high (48) and that is the real finding in this topic — see
"The template problem" below. It is a usability problem, not an accuracy problem.

---

## Errors

### 1. F0862 — a convention question tagged as needing dated research

Question: *"How does an increase in current liabilities affect FCFF."*

The card answers with the dated-research template: *"This is date-dependent and has no permanent
numerical answer. Before the interview, retrieve the relevant dated data from a primary source:
... Federal Reserve releases for policy, Treasury for government yields ..."*

**Why it is wrong.** Nothing about this question is date-dependent and it is not numerical. It has
a fixed, permanent answer. The card sends a student to look up Treasury yields and LIBOR history
to answer a question about working capital.

**Corrected wording:**

> An increase in operating current liabilities (accounts payable, accrued expenses, deferred
> revenue) reduces operating net working capital, which releases cash and therefore increases
> FCFF, because FCFF subtracts the increase in operating NWC. A decrease does the reverse. Two
> cautions: the item must be an operating, non-debt liability — an increase in short-term
> borrowings or the current portion of long-term debt is financing, so it does not affect FCFF at
> all — and if the liability rose because an expense was accrued rather than paid, record the
> expense effect on EBIT first and then the offsetting working-capital change, rather than
> counting the cash benefit alone.

### 2. F2061 — the ECB and the Bank of England do not issue government bonds

Question: *"If a company operates in the EU, U.S., and U.K., what should you use for its Risk-Free
Rate?"*

The card says to use *"the yield on 10-year bonds issued by the European Central Bank or the Bank
of England."*

**Why it is wrong.** Neither institution issues sovereign debt. They are monetary authorities.
EUR-denominated risk-free rates come from a euro-area sovereign benchmark, in practice 10-year
German Bunds; GBP comes from 10-year UK gilts, issued by the UK Debt Management Office on behalf
of HM Treasury. A candidate who says "bonds issued by the European Central Bank" in an interview
will be corrected on the spot.

**This is the guide's own error, transcribed faithfully.** I verified it against page 105 of
`M&I 2025 400 IB Questions-2.pdf`, which contains the sentence verbatim. The card's note says to
retain the guide's stated assumptions, so this correction deliberately departs from verbatim guide
text. I read that note as covering illustrative assumptions, not misstatements of fact — but it is
your deck, so this is the one correction in this audit you might want to reverse on principle.
The guide's substance (use the government bond yield in the currency of the cash flows) is kept
and is correct.

**Corrected wording:**

> You should use the appropriate yield on the government bonds denominated in the currency of the
> company's cash flows. So, if the company reports its financials in USD, you might use the yield
> on 10-year U.S. Treasuries; if it reports in EUR, the standard euro-area benchmark is the
> 10-year German Bund; if it reports in GBP, the 10-year UK gilt. Note that the European Central
> Bank and the Bank of England are monetary authorities and do not issue government bonds —
> euro-area and UK sovereign debt is issued by national treasuries and debt management offices.

### 3. F1671 — a capex difference answered by denying that there is a difference

Question: *"2 companies are exactly the same (same revenue, growth, margins, etc...), but one of
them has higher capex than the other, and the other one pays out a higher dividend... how are
these two companies valued differently from a DCF perspective?"*

The card answers with the "identical companies" template: *"Identical current statements do not
guarantee identical future cash flows or risk... If all future cash flows, risk, rights and
information are truly identical, intrinsic value should be identical."*

**Why it is wrong.** The question states that the companies differ, and names both differences.
The answer never addresses either, and its conditional ("if truly identical, value is identical")
reads as a denial of the question's premise. The actual answer is specific and testable: higher
CapEx directly reduces FCFF and so reduces DCF value, while dividends do not appear in an
unlevered DCF at all — they are a distribution below FCFF, not an operating cash flow. A student
who gave this answer would be marked wrong on a standard question.

The deck already has the correct answer one card away: **F1689** ("Higher CapEx reduces FCFF and
DCF value if all other cash flows are unchanged..."). As with the lease sentence in the accounting
pass, the deck currently contradicts itself.

**Corrected wording:**

> Take the two differences separately. Higher CapEx reduces unlevered free cash flow directly,
> because FCFF = EBIT(1-t) + D&A - CapEx - increase in operating NWC, so the higher-CapEx company
> has a lower DCF value if nothing else changes. That is only the mechanical answer: distinguish
> maintenance from growth CapEx, since productive investment can raise future revenue, margins or
> asset life by more than its cost, and the associated tax depreciation partly offsets the outlay.
> The dividend difference does not affect an unlevered DCF at all. Dividends are a distribution to
> shareholders, paid out of cash flow that FCFF has already measured; they are not an operating
> cash flow and do not enter FCFF or enterprise value. A higher payout can matter indirectly — it
> leaves less cash on the balance sheet, which changes the EV-to-equity bridge, and it signals
> management's view of reinvestment opportunities — but it is not a DCF value driver on its own.

### 4. F2236 — a REIT methodology comparison answered with dividend mechanics

Question: *"How would you compare a Dividend Discount Model (DDM), Unlevered DCF, and Levered DCF
for valuing a REIT?"*

The card answers with the cash-dividend-and-enterprise-value template: *"For a cash dividend D
with no change in the operating business, cash and common equity value each fall D; EV is
unchanged..."*

**Why it is wrong.** The answer compares none of the three methods, never mentions REITs, and
answers a different question (what a dividend does to EV). It shares this template with F1659 in
the Accounting topic, where it is also a poor fit. Nothing in it is false; it is simply not an
answer, and a student reading it learns nothing about the question asked.

**Corrected wording:**

> All three can be built, but they suit a REIT differently. A DDM fits REIT economics most
> directly: a REIT must distribute most of its taxable income to keep its tax status, so dividends
> are close to the cash flow actually available to shareholders, and the payout is both large and
> relatively predictable. Discount dividends at the cost of equity. A levered DCF is the next most
> natural, because property-level debt is central to how REITs are financed and because the
> sector's own metrics (FFO and AFFO) are after-interest equity measures; discount levered cash
> flow at the cost of equity and you reach equity value directly, with no bridge. An unlevered DCF
> is the weakest fit: it values the whole property portfolio before financing, which cuts against
> both the sector's leverage profile and its standard metrics, and it requires a terminal value
> for assets usually valued on a cap rate or NAV basis instead. In practice NAV — appraised or
> cap-rate-derived property value less net debt — plus P/FFO and P/AFFO multiples carry more weight
> than any of the three, with a DDM or levered DCF as the cash-flow cross-check.

### 5. F2035 — truncated first sentence

The answer begins mid-phrase: *"equals Net Operating Profit After Taxes (NOPAT) + D&A and
sometimes other non-cash adjustments..."* The subject of the sentence is missing, so the card
never says what equals NOPAT + D&A.

Page 91 of the guide reads "Unlevered Free Cash Flow equals Net Operating Profit After Taxes
(NOPAT) + D&A...", so this is a transcription truncation, not a guide error. The content that
follows is correct. **Fix: restore the three dropped words.**

---

## One change outside the source JSON

F0862's wrong template had a traceable cause, and it is a one-line bug in the build script.
`TIME_PAT` in `flashcards/build_data.py` flags a card as "Needs fresh research" when the question
contains the word "current" — which matched the accounting term **"current liabilities"**. That is
what classified a pure-convention question as time-sensitive and attached the dated-research
template to it.

I added a negative lookahead so "current" no longer matches when it is followed by `assets`,
`liabilit`, `portion`, `ratio` or `maturit`. I checked the whole 2,049-card source first: F0862 is
the **only** card the change affects (verified cards 2,540 to 2,541; "Needs fresh research" 233 to
232), so there is no collateral effect on the other topics' flags.

This is the one edit in this audit outside the source JSON's `answer` fields, so flagging it
explicitly: if you would rather keep `build_data.py` untouched, revert that hunk and F0862 will
simply carry a stale "Needs fresh research" badge while its corrected answer stands.

## The template problem

This is the main finding and it is not an accuracy problem, so it is not counted above.

Of 222 cards, 113 are "concept_and_method" and they draw on about ten shared templates. A handful
of templates carry a very large share of the topic: the WACC-formula paragraph alone answers
roughly 30 cards. That keeps the deck internally consistent — and the templates themselves are
accurate, which is why this topic has no formula errors — but it means a specific question often
gets a correct paragraph that does not answer it.

The clearest pattern: **a direct question with a definite answer, answered by a template that
states the general principle but never draws the conclusion.** The student is left to infer it.

- Direction questions that are never answered: **F0870** (does increasing or decreasing WACC raise
  a DCF value), **F1446** (if beta increases, what happens to EV), **F1500 / F1501 / F1502** (what
  a recession, or a broad move, does to WACC), **F1538** (startup vs industrial WACC), **F0206**
  (industrials vs consulting WACC), **F0194** (cost of equity rising from zero), **F0703** (a
  cash-burning company's WACC), **F1214** (which is higher, cost of debt or cost of equity).
- "Give an example" questions with no example: **F0018** (an industry with negative beta),
  **F0596** (an asset with beta of zero), **F1211** (a company whose cost of debt exceeds its cost
  of equity), **F1775** (a low-beta and a high-beta company). The deck has the content for these:
  F0351 covers negative and zero beta well, F0698 covers cost of debt exceeding cost of equity.
  The templates were simply assigned in the wrong direction.
- "Explain it simply" questions answered technically: **F0551** (explain WACC to someone without a
  finance background) and **F1202** (explain DCF to a 10-year-old) both return the full technical
  paragraph, F1202 including summation notation. The deck proves it can do this register —
  F0450 explains working capital with a lemonade stand — so these two are fixable by reassignment.
- Standard questions left generic: **F1299** (disadvantages of a DCF), **F1338** (when a DCF is
  not useful), **F1340** (how to choose the projection period), **F0210** (which companies suit a
  DCF), **F0747** (when a DCF gives the highest value), **F1544** (time value of money and its
  formulas), **F1498** (PV of a year-three cash flow — the formula is only implicit in a
  summation).
- Question-specific content dropped for a generic template: **F1220** (the discount rate for an
  apple tree, answered with a customer/addressable-market framework), **F0168** (two most
  important macro indicators), **F0399** (Ireland vs US then Russia vs US, where country risk is
  the whole point), **F1041** (inflation and rate hikes), **F1164** (debt seniority), **F1372**
  (distressed WACC), **F1796** (a food truck's WACC), **F1826** (a country's cost of debt),
  **F1560** (how each component of cost of equity is derived — given the WACC template rather than
  the CAPM one), **F1421** and **F1044** (multi-part questions where only one part is answered),
  **F1126**, **F1568**, **F1848**, **F0110**, **F0208**, **F0869** (sensitivity template on
  questions about something else).
- Dated-research template on questions that are only partly dated: **F1339** (asks about forecast
  period, mid-year convention and terminal value method — all pure convention — about a dated
  company), **F1118** (how to calculate AT&T's beta — the method is not dated), **F1217**
  (describe beta, then rank three companies). Defensible for the numbers, unhelpful for the
  method. F0207 ("What is Apple's WACC?") is the one card where this template genuinely fits.
- Ambiguous but defensible: **F2159** (bank DDM) describes backing into dividends as CET1 plus
  intangibles less beginning equity less net income, which yields the dividend with a negative
  sign; correct as a negative line in an equity roll-forward, confusing out of context. **F2060**
  calls dividends "a real cash expense" — a distribution, not an expense, though the cash meaning
  is clear. Both are guide text; left unchanged.
- **F1688** (same profile, different retained earnings) gets the "identical companies" template and
  here it is actually a reasonable fit, since retained earnings is a historical equity account that
  does not change future cash flows. Noted only to show why F1671 is different: there the stated
  difference does change cash flows.

**Suggested follow-up, not done here:** none of these needs new finance, only reassignment —
pointing each question at a template the deck already contains, and adding a one-line conclusion
to the direction questions. That is a mechanical pass over the `answer_status: concept_and_method`
cards, and it would improve this topic more than any further accuracy work.

## Verified correct — the cases most likely to be wrong

- **F0576 / F0740 / F0891** — arithmetic-gradient perpetuities (100, 200, 300, … forever).
  PV = 100(1+r)/r² is right; I confirmed it independently as a sum of stacked level perpetuities,
  giving 11,000 at r = 10%.
- **F1799** — CAPM partials. Ke rises by β·ΔRm when Rm moves; one-for-one with Rf when the ERP is
  held constant; and by (1-β)·ΔRf when Rm is held fixed instead. That third case is the one people
  get wrong, and it is right.
- **F1981 / F1982** — the M&I operating-lease and IFRS/finance-lease walkthroughs. Both balance
  (+980 and +965 respectively), and the IFRS intuition check (-160 + 180 × 25% = -115) ties.
- **F2057** — a corporate tax cut raises the after-tax cost of debt and, through relevering, the
  cost of equity, so WACC rises slightly while FCF rises more. The no-debt edge case is also right.
- **F0432 / F0594 / F1570 / F1408** — Hamada unlevering and relevering, consistently stated with
  the zero-debt-beta assumption made explicit each time.
- **F0459 / F0838 / F2052 / F2053** — mid-year convention and stub periods, including the subtle
  point in F0838 that whether the terminal-value share of total PV changes depends on whether the
  terminal value moves with the explicit period.
- **F1863** — $20 of depreciation at 25% tax and 10% WACC: $5 of FCFF, $4.55 discounted one year,
  $50 as a perpetuity.
- **F2056** — 10% vs 5% growth over ten years leaves Year 10 revenue ~37% lower; the guide's "~35%"
  is fair.
- **F2120** — the 5% coupon bond is more rate-sensitive than the 10% bond. Right conclusion.
- **F1093 / F1290** — EPS 7 at 30% tax → 8.50 at 15% → 127.50 at 15x; and 103 × 17 = 1,751 with the
  "1/15%" ambiguity flagged rather than guessed.

## What this audit does not cover

Only factual accuracy of answer text for this one topic. The 27-card sample in `answer_review.md`
included 9 advanced-valuation cards; those were re-read here as part of the full pass and remain
correct. Remaining unaudited topics: Enterprise & Equity Value (100), Accretion / Dilution (58),
Merger Model & M&A (116), LBO & Private Equity (109), Debt/Credit & Restructuring (261),
Valuation & Comps (153), and the non-technical topics.
