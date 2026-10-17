# Industry & Company Analysis — full accuracy audit

**Scope: all 590 cards with topic "Industry & Company Analysis" in `flashcards/data.json`, read in
full.** Audited in three groups of roughly 200 as requested, with cards ordered so the checkable
statuses came first: guide answers, then model answers, then concept/method, missing-input,
open-framework and dated-research last.

Composition: 154 model answers, 112 concept/method, 105 open framework, 93 dated-research, 87 M&I
guide transcriptions, 39 missing-input. **198 of the 590 are open-framework or dated-research**
cards with no fixed answer, and a further 39 lack inputs, so the checkable surface is about 350.

## Result

| | Cards |
| --- | ---: |
| Read in full | 590 |
| **Errors** | **5** |
| Defensible but incomplete or mismatched | 29 |
| Verified correct | 556 |

This is the lowest error rate of any tranche (0.8%), which is what the composition predicts: most
of the topic is firm-specific or judgment questions where a generic framework is the honest answer.

Every numerical card recomputes. The 87 guide transcriptions are the strongest material in the
topic and are uniformly correct, including the sector-specific metrics — gold equivalents, reserve
life ratios, cap rates, airline ASK/load factor/yield, book-to-bill, CET 1 and RWAs, insurance
combined ratios and the FFO build.

Four of the five errors are the wrong-template failure. One, F0448, is a genuine factual error.

---

## Errors

### 1. F0448 — calendarization runs in the wrong direction

Question: *"Explain calendarization of financial statements."*

The card says:

> For a company whose fiscal year ends in September, approximate calendar-year revenue using 9/12
> of the fiscal year ending the next September and **3/12 of the prior fiscal year**.

**Why it is wrong.** The weights are right but the second period is the wrong one. Calendar 2024
consists of January–September 2024, which sits in the fiscal year ending September 2024, plus
October–December 2024, which sits in the **following** fiscal year, the one ending September 2025.
The prior fiscal year (ending September 2023) covers October 2022 to September 2023 and contains
none of calendar 2024. Taking 3/12 of it pulls in October–December **2022**.

A student calendarizing a comps set this way would blend a quarter from two years earlier into
every peer, which is exactly the error calendarization exists to prevent. This is the only
arithmetic or convention error found in the 590.

**Corrected wording:**

> Calendarization aligns companies' results to the same fiscal or calendar period so that multiples
> are comparable. Take the calendar year you want and add up the fiscal periods that actually fall
> inside it. For a company whose fiscal year ends 30 September, calendar 2024 is January to
> September 2024 plus October to December 2024: the first nine months come from the fiscal year
> ending September 2024, and the last three come from the following fiscal year, the one ending
> September 2025. So calendar-year revenue is approximately 9/12 of the fiscal year ending in that
> calendar year plus 3/12 of the next fiscal year - never the prior one, which contains no part of
> the calendar year you are building. Where quarterly data is reported, sum the actual quarters
> rather than pro-rating, because month weights assume revenue is spread evenly and most businesses
> are seasonal. Apply the same month weights to every company and to forecasts as well as
> historicals, and state the convention you used. The same logic applies to any target period: a
> June year-end company contributes 6/12 and 6/12, and a stub or 53-week year needs its actual
> days.

### 2. F0564 — market sizing answered with SaaS performance metrics

Question: *"Walk me through how you would calculate the market size of [software product]?"*

The card returns the SaaS metrics template — ARR, net and gross retention, churn, CAC payback, the
Rule of 40, EV/ARR.

**Why it is wrong.** Those metrics describe how good an existing business is, not how large its
market is. Market sizing needs a top-down and a bottom-up estimate, which the deck states
correctly on **F0028**, **F0137** and **F1845** ("Use both top-down and bottom-up estimates...
addressable customers * penetration * usage frequency * spend"). This is the same defect as F0075
in the previous tranche, where a pizza-market question got the unit-economics template.

**Corrected wording** sizes it both ways — bottom-up from target organisations, seats per
organisation and price per seat; top-down from total IT or software spend narrowed by category
share — and separates TAM from serviceable and obtainable market.

### 3 & 4. F0160 and F0273 — permanent questions tagged as needing dated research

- **F0160:** *"What makes a stock price move?"*
- **F0273:** *"Calculate the return of the stock if the price of 2014 is \*\* and the price of 2015
  is \*\*."*

Both receive the dated-research template: *"This is date-dependent and has no permanent numerical
answer. Before the interview, retrieve the relevant dated data from a primary source... Federal
Reserve releases for policy, Treasury for government yields... do not invent a current LIBOR
quotation after cessation."*

**Why they are wrong.** Neither is date-dependent. F0160 is a conceptual question with a stable
answer: price moves when expected cash flows change, when the discount rate changes, or when
expectations and flows shift relative to what was priced in. F0273 is a one-line formula — the
return is the ending price over the beginning price minus one, plus dividends for total return.
The two prices are missing from the transcription, which makes it a missing-input card, not a
go-and-check-the-Fed card. This is the same defect as F0862 in the credit tranche, where
"how does an increase in current liabilities affect FCFF" got this template.

Both are corrected: F0160 to the three drivers with the distinction between a price move and a
value change; F0273 to the simple and total-return formulas with the annualisation and the
dividend/split cautions.

### 5. F0661 — a cash-flow bridge question answered with a business-model framework

Question: *"A company's revenue is stagnant but it has a positive ending cash-flow balance. Explain
where the cash may be coming from or going."*

The card returns the business-analysis template: *"Describe the customer problem, revenue model,
unit economics, competitive advantage and addressable market..."*

**Why it is wrong.** The question asks where cash came from when revenue did not grow, which is a
cash-flow-statement question with a short list of answers: non-cash charges added back, working
capital released, asset sales, borrowing or equity issued, reduced capex, or cash collected in
advance. Customer problems and addressable markets do not answer it. The deck has the right
machinery on its three-statement bridge and EBITDA-versus-cash-flow templates.

**Corrected wording** walks the three sections of the cash flow statement in turn and notes which
sources are repeatable and which are one-off.

---

## Not errors: incomplete, mismatched or ambiguous

**Definitional or list questions the template does not deliver:** **F0028** (which databases to
consult for market sizing — no source is ever named), **F0541** ("give examples of companies with
betas of -1, 0 and 1" — the template gives a fair casino game and protective puts but no company
and no example of beta 1, joining the example-less cluster from the DCF tranche), **F1418** (how to
value a negative-FCF business — the FCFF formula without the negative-FCF approach).

**Wrong flavour of template, question still partly served:** **F0699** (costing a new stadium
including financing → the revenue-driver template rather than project finance), **F1665** (explain
the interest tax shield → the five-uses-of-cash template, which happens to define it correctly in
its closing line), **F0229** (which form of capital raising → unit economics rather than the
debt-versus-equity template), **F1194** (rank semis, software and internet → the SaaS template,
which never compares the three), **F1511**, **F1608**, **F0644**, **F1040**, **F0200**, **F0848**,
**F1468** (two-part question, one part answered), **F0650**, **F0420**, **F0731**.

**Dated template where the question is partly permanent:** **F1807** (why a client's stock price is
down), **F0523** (what ECM services the firm offers), **F0937** and **F0938** (how the firm makes
money, its main lines of business), **F0271** (how to grow a business in Asia), **F1774** (compare
Exxon and Tesla's financial profiles), **F0166** (how a tax law changed valuation). In each of
these the firm-specific or dated half genuinely needs current sources, so pointing at filings is
defensible even though the conceptual half is stable. F0160 and F0273 above are different: nothing
in them is dated at all.

**Guide wording worth knowing about, left as written:** **F2231** says REITs must distribute 90% of
"Net Income"; the U.S. requirement is 90% of taxable income, which can differ materially from net
income because of depreciation. The 75% gross income and asset tests are stated correctly.

## Verified correct — a selection

- **The 87 guide transcriptions**, which carry most of the sector-specific content: **F2185** (gold
  equivalent: 1,000 + 10,000 × $4 / $2,000 = 1,020 oz), **F2193** (reserve life ratio of 11.1 using
  the 6:1 gas conversion), **F2224** (a 5% cap rate as the reciprocal of 20x), **F2174** (ASK, load
  factor, RPK and passenger yield), **F2176** (book-to-bill), **F2153** (CET 1 and risk-weighted
  assets, 4.5% rising to 9.5% with buffers), **F2155** (the insurance premium walkthrough, which
  balances at +$87), **F2156** (the combined ratio and its acknowledged denominator inconsistency),
  **F2235** (the FFO build), **F2192** (successful efforts versus full cost), **F2251** (SaaS
  bookings, billings and revenue), **F2253** (an LTV of about $110K).
- **F1970 / F1973 / F1974 / F1975 / F1978** — the guide's employee-cost, receivable, payable and
  share-issuance walkthroughs. All five balance, including the dividend paid on the post-issuance
  share count.
- **F0006** — $10 to $50 in four years is a 49.53% CAGR, with the 1.5^4 = 5.0625 mental check.
- **F0242** — five up-and-down 50% pairs leave 23.73% of the starting value; five alternating single
  moves starting up leave 84.375%. Both right.
- **F0304 / F0295** — 18.92% for a doubling over four years, and 41.4% to double in two.
- **F1433** — the missing-dollar hotel puzzle, correctly resolved as double counting.
- **F0623** — the St. Petersburg paradox, with each term contributing $1 and the right observation
  that divergent expectation does not justify a $10,000 entry fee.
- **F1235** — $10m for 50% implies a $20m post-money and $10m pre-money valuation.
- **F0050** — degree of operating leverage as contribution margin over EBIT, financial leverage as
  EBIT over EBIT less interest.
- **F1310** — FIFO versus LIFO under rising costs.
- **F0157 / F1257 / F1258** — VaR, expected shortfall, RAROC, CAR and key-rate duration.
- **F0374 / F0107 / F1825** — the buyback EPS formula and the condition for accretion.
- **F0448's companion cards** on multiples and comps selection are unaffected by its error.
- **F0610 / F1751** — one-year YTMs of 37.5%.
- **F0655 / F1209** — gross and net revenue retention, correctly excluding new customers.
- **F0377** — acquisition accounting, with goodwill not amortised but impairment-tested.

## What this audit does not cover

Only factual accuracy of answer text. **With this tranche the technical deck is fully audited: all
2,049 cards across all topics.** The 1,185 behavioral cards are out of scope — they are preparation
frameworks rather than answers with a right and wrong.

Final total: **2,049 of 2,049 technical cards audited, 49 errors found and corrected** — 36 across
my seven tranches and 13 in the Valuation & Comps pass.
