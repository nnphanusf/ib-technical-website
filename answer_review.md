# Accuracy review of the AI-written answers

**Status: sampled, not certified.** 27 answers read in full and checked line by line.
No errors found. That is 1.5% of the 1,746 prepared answers, so it supports "the core looks
sound", not "the deck is correct".

## What was checked

Each answer was verified against standard US GAAP / banking convention: the arithmetic
recomputed, the direction of every balance-sheet and cash-flow effect checked, and the stated
assumptions tested for internal consistency.

### Accounting and enterprise value (10)

`F0024` `F0400` `F0587` `F0668` `F0901` `F1088` `F0201` `F0222` `F1542` `F1154`

Worth singling out: **F0901**, the 200m inventory purchase financed with 5% cash / 5% PIK debt
amortising 20%. Ending debt of 170 (200 + 10 PIK − 40 amortisation), CFO of 190 − 180t and
ending cash of 350 − 180t all reconcile, and the full-year working-capital treatment is right.
That is the kind of question where a wrong answer is usually wrong.

**F0201** goes further and corrects its own source: the interview note said a $5 EBITDA increase
beat a one-turn multiple increase, and the answer says plainly that it does not (at 5x on $100
EBITDA, one turn is +$100 against +$25).

### Numeric cases (10)

`F0910` `F1173` `F2000` `F1007` `F1093` `F1290` `F0616` `F0615` `F2005` `F1011`

**F0616** is the strongest of these: $100m secured against $50m collateral, $150m unsecured,
$200m of value. The deficiency claim is correctly ranked alongside the unsecured debt, giving
75% on the $200m unsecured pool, 87.5c to the secured lender and 75c to the original unsecured
holders.

**F1093**: EPS 7 at a 30% tax rate implies pre-tax EPS of 10; at 15% that is 8.50, and 15x gives
127.50 against 105. Correct.

### Advanced valuation, accretion and options (9)

`F1089` `F0432` `F1348` `F1241` `F0792` `F1110` `F1482` (plus two re-reads)

Hamada unlevering and relevering are stated correctly. **F1241** reasons through earnings yields
rather than asserting the rule: a 10x buyer gives up a 10% yield to buy a 5% yield, so all-stock
is dilutive. **F0792** refuses to invent a convertible coupon from a cost of debt and cost of
equity, and says explicitly that averaging the two is wrong.

## What this does not cover

- **1,719 prepared answers were not read.** Zero errors in 27 is consistent with a true error
  rate as high as roughly 11% at 95% confidence. Absence of evidence over a 1.5% sample is weak
  evidence of absence.
- **303 guide-derived answers** come from the M&I guide rather than being written here; they
  have different provenance and were not sampled.
- **216 open-ended and 197 date-dependent answers** have no fixed answer to check against.
- **Sector-specific answers** (biotech, SaaS, real estate, FIG) are the thinnest ice: fewer
  conventions are universal, and they were only lightly sampled.

## If you want this done properly

Work topic by topic, highest traffic first, checking every card rather than a sample:

| Tranche | Cards | Why first |
| --- | ---: | --- |
| Accounting & 3 Statements | 209 | Asked in every interview; errors are unambiguous |
| DCF & Intrinsic Value | 222 | Formula-heavy, easy to state subtly wrong |
| Enterprise & Equity Value + Accretion | 158 | Sign conventions are where answers slip |
| Merger Model, LBO | 225 | Numeric, checkable |
| Debt, Credit & Restructuring | 261 | Waterfall and recovery logic |

Anything flagged as wrong should be corrected in the source JSON, not patched in the page, so a
rebuild keeps the fix.
