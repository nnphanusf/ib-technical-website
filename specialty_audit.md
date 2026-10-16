# Options, FIG, Quant, Deal Process, Markets and Stock Pitch — full accuracy audit

**Scope: all 231 cards in the six remaining small topics, read in full.** Grouped into one tranche
because each is well under 200 cards on its own. Same method as the earlier passes.

| Topic | Cards |
| --- | ---: |
| Stock Pitch & Investing | 101 |
| Markets & Economy | 69 |
| Deal & Process | 32 |
| Options & Derivatives | 14 |
| Quant & Brainteasers | 8 |
| FIG & Specialty Valuation | 7 |

Composition: 86 open framework, 57 dated-research, 28 model answers, 25 concept/method, 19 M&I
guide transcriptions, 16 missing-input. **143 of the 231 are cards with no fixed answer** — the
highest proportion of any tranche — so the checkable surface here is much smaller than the card
count suggests.

## Result

| | Cards |
| --- | ---: |
| Read in full | 231 |
| **Errors** | **8** |
| Defensible but incomplete or mismatched | 24 |
| Verified correct | 199 |

Every numerical card recomputes: the Black-Scholes formula where it appears, the risk-neutral
probability, delta hedging, the chemical-plant impairment, the insurance premium walkthrough, the
combined ratio, the portfolio harmonic-mean P/E, the constrained allocation and the debt-for-equity
swap. No finance errors.

All eight errors are wrong-template failures, and this tranche shows the keyword-collision pattern
at its clearest — three of them pull in a template from a completely different discipline.

---

## Errors

### 1 & 2. F0695 and F0856 — Black-Scholes answered with the binomial model

- **F0695:** *"What is the Black-Scholes option pricing model and describe the mechanism?"*
- **F0856:** *"Explain the Black-Scholes model and how stock prices affect option values."*

Both receive the general options template, which presents the **one-period binomial model** —
`q = [(1+r)S0-Sdown]/(Sup-Sdown)` — and never mentions Black-Scholes at all.

**Why it is wrong.** The questions name a specific model and ask for its mechanism. A candidate who
answers "Black-Scholes" with a two-state binomial tree has answered a different question. The deck
already carries the correct formula on **F1321**, so the content exists and is simply pointed at the
wrong cards.

Both are corrected with the formula, the inputs, the replication/no-arbitrage mechanism, the
risk-neutral reading of N(d1) and N(d2), put-call parity, and the model's known limitations.

### 3. F0075 — market sizing answered with unit economics

Question: *"Estimate the pizza market in a local town using two different methods."*

The card returns the unit-economics template ("Start with the decision and define the relevant unit
economics: volume/customer demand, price, contribution margin, fixed costs, reinvestment and
funding").

**Why it is wrong.** The question asks for two *methods*, which names the standard answer: a
top-down estimate and a bottom-up cross-check. The deck states exactly that on **F0148** ("Use both
top-down and bottom-up estimates... estimate addressable customers * penetration * usage frequency
* spend, and cross-check against capacity * utilization * price"). The template supplied instead
describes how to evaluate a business, not how to size a market, so it does not produce either
method.

Corrected with both methods worked through on illustrative numbers that reconcile to the same
~$4.3 million, plus the reconciliation and double-counting cautions.

### 4. F0988 — a probability question answered with real-estate cap rates

Question: *"What is the probability that at least one of ten randomly selected Manhattan apartments
is in the top ten by price?"*

The card returns the **real-estate valuation** template: *"Estimate stabilized net operating income
from rents/occupancy and operating expenses... A simple unlevered property value is
NOI/capitalization
rate... For REITs, FFO adjusts net income for specified real-estate depreciation..."*

**Why it is wrong.** "Manhattan apartments" pulled in the property template, but nothing in the
question concerns valuation. It is a hypergeometric sampling problem with a clean closed form.
Corrected with `1 - C(N-10,10)/C(N,10)`, the sequential-product equivalent, the `100/N` large-N
shortcut (about 0.012%, or one in 8,500, at roughly 850,000 apartments) and the with-replacement
variant.

### 5 & 6. F0199 and F1172 — macro-impact questions answered with process mechanics

- **F0199:** *"How would a recession affect investment banking?"* → the **sell-side M&A process**
  template (teasers, buyer lists, management presentations, greenshoes).
- **F1172:** *"How would rising Federal Reserve rates affect the restructuring market?"* → the
  **restructuring process** template (13-week cash flows, Chapter 11 versus 7, prepacks, 363 sales).

**Why they are wrong.** Both ask how a macro condition changes activity in a business, and both
receive a description of how that business's process works mechanically. The two have no overlap: a
candidate reciting the steps of a sell-side auction has not answered what a recession does to fee
pools, and one reciting the stages of a Chapter 11 has not answered what higher rates do to coverage
ratios and refinancing walls. Both questions have determinate, teachable answers.

F0199 is corrected to cover the split across products — M&A and ECM contract hardest, DCM depends on
why rates moved, restructuring and liability management are counter-cyclical, trading often benefits
from volatility — plus the consequences for the bank itself. F1172 is corrected to the three
channels: floating-rate debt service compressing coverage, refinancing walls that can no longer be
cleared, and lower enterprise values moving the fulcrum security up the stack.

### 7. F0054 — a portfolio company's business model answered with personal asset allocation

Question: *"Explain the business model of one of this firm's portfolio companies."*

The card returns the **retail asset-allocation** template: *"Begin with objective, horizon,
liquidity
needs, risk tolerance, constraints, taxes and currency. An illustrative long-horizon growth
allocation could combine diversified global equities with high-quality bonds and a liquidity
reserve..."*

**Why it is wrong.** The question is about how a company makes money. The answer is about how an
individual should split a savings pot between stocks and bonds. Nothing transfers. Corrected to a
business-model framework — what is sold and to whom, the charging model, customer acquisition cost
against lifetime value, incremental gross margin, recurrence, defensibility — closing with how to
connect it to the firm's own strategy, since this is a question you prepare per firm rather than
answer generically.

### 8. F0719 — a securitization spread answered with personal asset allocation

Question: *"What spread would you bid for a portfolio of these phones?"*

The same asset-allocation template as F0054.

**Why it is wrong.** This is the asset-backed pricing question from a cluster the deck handles
correctly elsewhere: **F0716**, **F0717** and **F0718** all receive the securitization template,
whose closing line is exactly the right answer — *"A quoted spread must compensate for expected
losses, duration/option risk, liquidity and model uncertainty."* F0719 is the one card in that
cluster that got the wrong template, and the one that actually asks for the spread.

Corrected to expected loss (PD × LGD × exposure driven by used-phone resale value net of collection
and refurbishment), plus premia for obsolescence concentration, correlation with a falling
secondhand
market, short uncertain duration, servicing practicality and illiquidity, benchmarked against
comparable consumer ABS, and conditioned on where in the structure the bid sits.

---

## A documented cluster, deliberately not corrected here

**Plain-language questions answered technically.** I scanned all 2,049 cards for questions that ask
for an explanation to a child, a grandmother, an eighth grader, or "as simply as possible." There
are
seven, and **only one delivers it**:

| Card | Topic | Register |
| --- | --- | --- |
| F0450 | Accounting & 3 Statements | **plain** — the lemonade stand, and it is excellent |
| F0460 | Deal & Process | technical |
| F0725 | Debt, Credit & Restructuring | technical |
| F1202 | DCF & Intrinsic Value | technical |
| F1266 | Markets & Economy | technical |
| F1309 | Markets & Economy | technical |
| F1432 | Stock Pitch & Investing | technical |

F1202 answers "explain DCF to a 10 year old" with summation notation; F0725 answers "explain bank
debt versus high yield to your grandmother" with lien priority and intercreditor documents; F1266
answers "as simply as possible" with core PCE.

Nothing in these six is false, so they are not in the error count. But the register *is* the
question
in every one of them, and the deck proves it can do this — F0450 shows the house style. Fixing them
means writing six new plain-language answers, which is composition rather than accuracy correction,
so I have left them for a decision rather than quietly rewriting them in an accuracy pass.

---

## Not errors: incomplete, mismatched or ambiguous

**Definitional questions the template never defines:** **F1413** ("What is quantitative easing?" →
the macro template, which never says what QE is), **F0431** ("What is a 'Derivative'?" → the options
template, which never gives the general definition). F1413 is the cleanest miss of this kind in the
deck and pairs with F0966 ("What is the yield curve?") from the restructuring tranche.

**Macro condition, wrong flavour of template:** **F0737** (valuation when rates are rising → the
choose-a-method template, which never mentions rates), **F0943** (a Fed move's effect on gold, the
yen and oil → the general macro template, none of the three addressed), **F0967** (yield-curve
curvature), **F0413** (oil and equities), **F1012** (analyse a market event → business-diligence
framework).

**Solve-for-X given a definition:** **F0973** (compute a portfolio's return and the effect of
changing constituent returns and standard deviations → the allocation template, which gives neither
`Σw·r` nor the variance formula). This joins F0591, F0742 and F1929 from the merger tranche as the
same family.

**Pitch questions pointed at the equity template for non-equity products:** **F1390** (agency MBS
trade idea) and **F0965** (non-equity trade idea) both get the equity-pitch framework, whose listed
factors — revenue quality, margins, management capital allocation — do not apply to a rates product.
The template's skeleton (thesis, catalysts, downside, what would invalidate it) does transfer, which
is why these are notes rather than errors, but the MBS-specific content the deck holds on F0954 and
F0986 would serve better.

**Generic where the question is specific:** **F1055** (healthcare investment banking), **F1650**
(sell now or wait), **F0272** (BlackRock's asset classes), **F0479** (an idea in your personal
portfolio → allocation rather than pitch template), **F1908**, **F1387** (estimate the cost of
expanding a school → business-diligence framework rather than the estimation template), **F1030**,
**F0254**.

**Guide wording worth knowing about, left as written:** **F2137** writes the approximate-YTM formula
as `($10 + ($100 – $50) / 5) / ($100 + $50) / 2`, whose parentheses as literally written do not
produce the stated result; the intended calculation and the stated ~27% are both right, and this is
the guide's own typo.

## Verified correct — the checkable cards

- **F1321** — the Black-Scholes formula, both `d1` and `d2`, plus a genuinely good answer to why an
  out-of-the-money call can collapse while the stock rises 10% (volatility crush near expiry), and
  the correct observation that with all else fixed a call cannot fall as the spot rises.
- **F0516** — the risk-neutral probability derived correctly for the 120/50 two-state case, and the
  right warning that a stated real-world 50% is not `q`.
- **F0959** — delta hedging: hold about `-N*d*m` of the underlying against a long option position.
- **F1745** — the chemical plant: $12.5m annual depreciation, $275m impairment to salvage, net
  income
  down $206.25m, CFO up $68.75m, and the balance sheet balances. The alternative nine-year reading
is
  carried correctly too.
- **F2155** — the insurance premium walkthrough: $10 of cash commissions against $4 expensed, the
  unearned premium reserve up $60, the DAC asset up $6, cash up $81, both sides up $87.
- **F2154** — the loan-loss provision and CET 1 (restored from the guide in the previous tranche;
  re-verified here).
- **F2156** — the combined ratio, including the guide's correct note that adding two fractions with
  different denominators is a long-standing industry inconsistency.
- **F2137** — the debt-for-equity swap: ~27% approximate YTM, a 3.0x multiple for a 25% five-year
  IRR, and 10% of a $1,500 equity value.
- **F0485** — portfolio P/E as the weighted harmonic mean `1/Σ(w_i/PE_i)`. I derived it
  independently;
  the warning that an arithmetic average of P/Es misleads is right.
- **F1843** — the constrained allocation: 40% Z, 40% X, 20% Y for a 10.4% expected return, and the
  correct point that the standard deviations are irrelevant to that objective and that risk needs
  correlations.
- **F1422** — `sqrt(0.9) ≈ 0.94868`, and the fee-gap-times-10,000 method for the breakeven basis
  points.
- **F1552** — a perpetuity of $1 a day as `1/rd`, with the annual-to-daily conversion.
- **F1976** — the two-step inventory purchase and sale; both steps balance and combine correctly.
- **F2141** — the greenshoe: 11.5 million shares and $115 million on a 15% overallotment.
- **F2138** — the IPO model, including the offering-price and primary-share formulas and the
  $2bn / $50 worked example.
- **F0172** — the expenditure approach to GDP, with transfer payments correctly excluded.
- **F1531 / F1818 / F1532 / F1946** — Fed increments in 25bp multiples with exceptions noted, PCE as
  the target basis with core PCE watched, why the Fed raises rates, and time value distinguished
from
  inflation.
- **F0255 / F1322** — ETF NAV, indicative value and the authorised-participant arbitrage, with the
  correct caution that a premium is not riskless profit.
- **F2160 / F2148 / F2150 / F2152** — embedded value, and why banks are valued on equity rather than
  enterprise value.
- **F0282 / F1571 / F1649 / F0088 / F0515** — all sound, and F1649's point that banks do not
  uniformly benefit from higher rates is the kind of nuance that is usually missing.

## What this audit does not cover

Only factual accuracy of answer text for these six topics. **Industry & Company Analysis (590 cards)
is now the only unaudited technical topic.**

Running total across seven tranches: **1,459 of 2,049 technical cards audited, 44 errors found and
corrected** — 31 in my six tranches and 13 in the Valuation & Comps pass.
