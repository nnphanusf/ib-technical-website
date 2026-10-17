# Merger Model & M&A + LBO & Private Equity — full accuracy audit

**Scope: all 225 cards across the two topics (116 Merger Model & M&A, 109 LBO & Private Equity),
read in full.** Same method as the earlier tranches.

Composition: 70 concept/method, 66 model answers, 50 M&I guide transcriptions, 21 dated-research,
16 missing-input, 2 open framework.

## Result

| | Cards |
| --- | ---: |
| Read in full | 225 |
| **Errors in these two topics** | **4** |
| Defensible but incomplete or mismatched | 38 |
| Verified correct | 183 |

Every numerical card recomputes correctly. That includes all five paper-LBO math cards
(F2101–F2105), the IRR reference points, the option-pool splits, the dividend recaps and the
EBITDA-growth solve — this is the most arithmetic-dense pair of topics in the deck and none of it
is wrong.

All four errors are the familiar wrong-template failure. Two of them are a sharper version of it:
**a question the M&I guide answers with a full worked solution had that solution replaced by an
unrelated definition template.** Chasing that pattern deck-wide found four more cards, in three
other topics — see below.

---

## Errors in these two topics

### 1 & 2. F2088 and F2089 — worked guide solutions replaced by an EBITDA definition

**F2088:** *"An Acquirer with an Equity Value of $500 million and an Enterprise Value of $600
million has a Net Income of $50 million and an EBITDA of $100 million. The Target, with a Purchase
Equity Value of $100 million and a Purchase Enterprise Value of $150 million, has a Net Income of
$10 million and an EBITDA of $15 million. What are the Combined P / E and TEV / EBITDA multiples
in a 100% Stock deal? Assume 25% tax rates."*

**F2089** is the follow-up: *"How do the multiples change if this is a 100% Debt deal funded with
an 8% interest rate issuance?"*

Both cards answer with the EBITDA bridge template — *"EBITDA = net income + income taxes + net
interest expense + depreciation and amortization... EBITDA omits taxes, CapEx, working-capital
investment and debt service, so it is not free cash flow."*

**Why it is wrong.** Every input needed is supplied and the questions ask for four specific
numbers. The cards compute nothing. The template is accurate in itself and entirely beside the
point. Worse, the guide these questions come from contains the full worked answers on page 118; I
verified my own computation against it before restoring it, and the two agree.

**Corrected wording, F2088** (the guide's own answer):

> The Combined Equity Value in a 100% Stock deal is $500 + $100 = $600 million, and the Combined
> Enterprise Value is $600 + $150 = $750 million. The Combined EBITDA is $115 million, and the
> Combined Net Income, assuming the same tax rates and no interest effects since it's a 100% Stock
> deal, is $50 + $10 = $60 million. Therefore, the Combined P / E multiple is $600 million / $60
> million = 10x, and the Combined TEV / EBITDA multiple is $750 million / $115 million = ~6.5x.

**Corrected wording, F2089:**

> The Combined EBITDA and Enterprise Value stay the same because they do not depend on the deal
> financing, so the Combined TEV / EBITDA is still ~6.5x. The Combined Equity Value is now just
> the Acquirer's Equity Value of $500 million. The Combined Net Income equals $50 + $10 - $100 *
> 8% * (1 - 25%) = $50 + $10 - $6 = $54. Therefore, the Combined P / E multiple is now $500
> million / $54 million = ~9.3x, which you can estimate as "between 9x and 10x" (since $500 / $50
> = 10x and $500 / ~$56 = 9x).

Both results are consistent with the deck's own F2090, which says combined EV multiples sit
between the buyer's standalone and the seller's purchase multiples: 6.5x falls between 6.0x and
10.0x.

### 3. F0626 — a computable waterfall refused on a misreading of its own prompt

Question: *"HoldCo owns 75% of OpCo 1 and all of OpCo 2. OpCo 1 has EBITDA of $60 million, an 8x
multiple and $300 million debt. OpCo 2 has EBITDA of $40 million, a 10x multiple and $500 million
debt. **OpCo 1 guarantees OpCo 2's debt.** Compare buying HoldCo stock at $0.50 per share with 100
shares outstanding versus OpCo 2 debt at 90 cents on the dollar with a 10% coupon and one-year
maturity."*

The card declines to answer, on the grounds that *"the wording does not establish whether the
stated recoveries already incorporate guarantees or **which entity guarantees which
obligation**."*

**Why it is wrong.** The question states the guarantee direction explicitly. The card refuses a
determinate problem by asserting the prompt is missing something it contains, so a student is told
this cannot be worked when in fact it is the whole point of the question — and the answer is
interesting, because the junior-looking debt turns out to be the better buy.

**Corrected wording:**

> Work each borrower's own assets first, then add the guarantee claim. OpCo 1: EBITDA 60 at 8x
> gives an enterprise value of 480 against 300 of debt, so its debt is covered in full and 180 of
> residual equity is left. OpCo 2: EBITDA 40 at 10x gives 400 against 500 of debt, so it is short
> 100 and its equity is worthless. Because OpCo 1 guarantees OpCo 2's debt, that 100 deficiency
> becomes a claim at OpCo 1, where it ranks alongside OpCo 1's other unsecured creditors and is
> paid out of the 180 of residual value. OpCo 2's lenders therefore recover in full: 400 from their
> own borrower and 100 under the guarantee. OpCo 1's residual equity falls to 80, and HoldCo's 75%
> of that is 60, with nothing from OpCo 2, so HoldCo's equity is worth 60. On the two investments:
> the stock costs 100 shares times $0.50, and taking the share count in millions to match the
> EBITDA figures, that is 50 against 60 of value, roughly 1.2x. The OpCo 2 debt costs 90 and pays
> 100 of principal plus the 10% coupon at maturity in one year, so 110 against 90, about 1.22x. The
> debt is the better risk-adjusted purchase: a similar multiple earned over a known one-year
> horizon rather than an unspecified equity holding period, and a contractual claim that sits ahead
> of both HoldCo's equity and the guarantee. Confirm the guarantee's ranking at OpCo 1, whether it
> is secured or structurally subordinated, and the HoldCo share-count units before relying on these
> figures.

### 4. F1403 — a sources and uses schedule answered with a comps template

Question: *"Create a sources and uses schedule from valuation multiples, debt funding and
financing assumptions."*

The card answers with the comparable-companies template — *"Choose companies with similar business
model, geography, growth, margins, risk and capital intensity... EV/Revenue divided by EV/EBITDA
equals EBITDA margin..."* — which has nothing to do with sources and uses.

**Why it is wrong.** The schedule's structure is determinate even without amounts, and the deck
states it correctly on F0007 ("Build sources and uses: purchase of equity, debt refinancing and
fees are funded by new debt, sponsor equity and any permitted target cash"). The card instead
teaches peer selection.

**Corrected wording:**

> A sources and uses schedule lists what the deal must pay for and where the money comes from, and
> the two sides must equal. Uses typically include the purchase of the target's equity (the equity
> purchase price, or the enterprise value when the deal is cash-free and debt-free), repayment or
> refinancing of existing target debt that will not be assumed, cash needed to fund the target's
> minimum operating cash, and transaction and financing fees. Sources typically include each new
> debt tranche (revolver draw, term loans, secured and unsecured notes, mezzanine or PIK), sponsor
> equity, any target balance-sheet cash permitted to fund the deal, rollover equity from management
> or the existing owner, and seller notes or earnouts where used. Size the debt from the leverage
> assumption on entry EBITDA and the lenders' coverage tests, then let sponsor equity be the plug
> that balances the schedule: sponsor equity = total uses less all other sources. That equity
> figure is the denominator for MOIC and IRR, so a change in fees, minimum cash or refinanced debt
> changes returns even when the purchase multiple does not. The source records no amounts, so build
> the schedule as line items and keep it symbolic.

---

## The deck-wide scan, and four corrections outside these topics

F2088 and F2089 suggested a general defect: a guide-sourced question whose worked answer was
swapped for a shared template. I searched all 2,049 technical cards for guide-sourced questions
whose answer text is shared by three or more cards. Ten cards matched. Six are benign, where the
shared template genuinely answers the question (F0113, F1408, F2093, F2151, plus F2088/F2089 now
fixed). **Four had lost a worked guide answer, in three topics outside this tranche.** All four
are restored from the guide, verified page by page:

### F2140 (Deal & Process) — the worst of the set

*"Can you explain Primary vs. Secondary Shares in an IPO or Follow-On Offering?"* was answered
with the **private equity fund** primary/secondary template: *"A primary investor commits to a new
fund before most assets are known and funds capital calls as investments are made. A secondary
investor buys an existing fund interest or portfolio/continuation-vehicle stake..."*

Two completely different meanings of the same word pair. In an equity offering, primary shares are
newly issued by the company and the company receives the cash; secondary shares are existing
shares sold by existing holders, who receive the cash instead. A student revising ECM from this
card would answer an IPO question with fund-secondaries content and be plainly wrong. Restored
from guide page 147.

### F2154 (FIG & Specialty Valuation)

A commercial bank increasing its loan-loss estimates by $100, and the effect on the CET 1 ratio,
was answered with the **debt-issuance** template: *"If debt is issued and proceeds stay as excess
cash, debt and cash rise equally and operating EV is unchanged..."* Entirely unrelated. Restored
from guide page 154; the restored answer's arithmetic checks (provision +100, net income −75 at
25%, cash +25, net loans −100, both sides down 75, and RWAs unchanged because they key off gross
rather than net loans).

### F2003 and F2007 (Enterprise & Equity Value) — a correction to my own earlier audit

Both are factory-purchase questions that the guide answers in two lines, and both had the generic
debt-issuance template instead. **`ev_accretion_audit.md` listed these two as "incomplete, not
errors."** That was under-called: I did not know then that the guide contained worked answers, so
I treated a lost solution as mere vagueness. With that evidence they belong in the error column,
which takes the Enterprise & Equity Value tranche from 2 errors to 4.

- **F2003** restored (guide p.78): equity value unchanged because debt, not equity, funds it;
  net operating assets up $100, so enterprise value up $100.
- **F2007** restored (guide p.78): "No" — the funding method is irrelevant to how enterprise value
  moves; the likely explanation is that the factory's book value is $50 but its market value is
  $100.

---

## Not errors: incomplete, mismatched or ambiguous

**A cluster worth fixing together: the IRR-levers cards.** Five cards ask, in different words, how
to raise returns, and none receives the enumeration:

- **F0787** "Give me 5 or more ways to boost IRR on an LBO" → the general LBO walkthrough
- **F1187** "How do you maximize IRR?" → the MOIC/IRR definitions
- **F1324** "Who uses LBO analysis, and how can they increase IRR?" → the general walkthrough
- **F1663** "What are some drivers of IRR?" → the definitions
- **F0444** "How to increase returns in an LBO?" → the general walkthrough

Meanwhile **F0445**, which asks something else entirely (what happens when the equity contribution
rises with debt constant), *has* the enumeration: "pay a lower entry price, grow sustainable
EBITDA/cash flow, improve working capital and CapEx efficiency, repay debt, or exit at a defensible
higher multiple." And **F2096** states the three canonical drivers cleanly. The templates are
simply pointed at the wrong questions; F0445 and F0787 look like a straight swap.

**"Solve for X" questions given a definition template.** Each has a one-line determinate method
the deck already contains:

- **F0591** break-even interest rate for EPS neutrality (method: the target's earnings yield at
  the purchase price, grossed up by 1/(1−t) — the deck does exactly this on F2082)
- **F0742** revenue synergies needed for accretion (the deck does this on F2083)
- **F1929** additional shares created (new shares = stock consideration / buyer share price, on
  F0371, F1545 and F2068)

**Direct questions the template never answers:** F0064 (the three value-creation levers), F0065
("walk me through a *paper* LBO" → full-model description rather than the mental-math shortcut),
F0247, F0530, F0589 (forms of consideration — never lists cash, stock, debt, earnouts), F0672 (why
the LBO is a valuation floor — and F0648's template actively disputes the premise), F1073, F1504,
F1802 (market conditions conducive to M&A), F1777, F1867.

**Specific prompt, generic template:** F0423 (diligence questions for an aerospace engine
manufacturer → the sell-side process steps), F0445, F0677, F0709, F0913, F1185, F1349, F1423,
F1473, F1569, F1913, F0216, F0455, F0832, F0293 (asks how the secondaries market has grown over
ten years, which is empirical, and gives definitions without saying it cannot answer), F0333
(multi-part, only the DCF part answered), F1070 (asset vs equity acquisition difference never
addressed), F1819 (three synergy types, no example for the third).

**Wording worth a glance:** F0843 ("levered vs unlevered dividend recap" — the template covers the
debt-funded case but never names the distinction), F1522 (SaaS metrics on a question about a
software *acquisition*).

## Verified correct — the calculation-heavy cards

- **F2101–F2105** — the five paper-LBO solves. 2.5x and ~20% IRR; the 13x exit multiple needed for
  a 25% IRR; 11.1x once 75% of debt is repaid; $100 of debt repayment implied by a 20% IRR; and the
  10x exit that equals the entry multiple. Every one recomputes, and the mental-math shortcuts the
  guide gives alongside them are sound.
- **F1090** — the EBITDA CAGR needed for a 25% IRR at 9x entry and exit with half the debt repaid:
  13.91%. I rebuilt it from scratch (exit equity 15.2588, exit EV 17.2588, exit EBITDA 1.91764).
- **F1625 / F1952** — IRR reference points: 2x over five years 14.9%, 2x over three years 26.0%,
  3x over five years 24.6%, and the guide's $1,000-to-$2,000 example at 14.9%.
- **F2100** — 50% IRR over six months is only ~1.25x, and 3x over ten years is only ~12%.
- **F1744** — the 10% option pool: 1.8x to the sponsor on a share of total exit equity, 1.9x on a
  share of the gain above entry.
- **F0070** — the equity proportion for a 3x return, including the debt-repayment variant
  E = (600+P)/2, which I derived independently.
- **F0364 / F1695** — the dividend recap: 4.0x gross leverage, and the correct observation that the
  dividend consumes the proceeds so net leverage is not offset.
- **F0534** — purchase accounting with $300 of goodwill; both sides move $700.
- **F0710** — 2.0x MOIC and a 14.87% IRR from a $400 equity cheque.
- **F1428** — gain on an asset sale: cash up P − Gt, equity up G(1−t).
- **F2006** — $150 debt plus $50 stock into $175 of PP&E and $25 of investments: EV up $175.
- **F1043** — the Gordon-growth rearrangement g = (T·WACC − FCF_N)/(T + FCF_N), and the variant
  when the supplied figure is already next period's cash flow. Both algebraically correct.
- **F1953** — that the discount rate does not affect IRR, and that the asking price affects IRR but
  not the present value of the future cash flows. Subtle and correctly stated.
- **F2094** — cash available for optional repayment = beginning cash + FCF − minimum cash −
  mandatory repayments.
- **F2163** — TVPI, DPI and RVPI, with TVPI correctly splitting into the other two.

## What this audit does not cover

Only factual accuracy of answer text for these two topics, plus the four cross-topic restorations
above. Remaining unaudited: Industry & Company Analysis (590), Stock Pitch & Investing (101),
Markets & Economy (69), Deal & Process (31 of 32), Options & Derivatives (14), Quant &
Brainteasers (8), FIG & Specialty Valuation (6 of 7).

Running total across six tranches (five of mine plus the Valuation & Comps pass in
`valuation_audit.md`): **1,228 of 2,049 technical cards audited, 36 errors found and corrected**
— 23 in this session's five tranches and 13 in the valuation pass.
