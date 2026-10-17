# Accounting & 3 Statements — full accuracy audit

**Scope: all 209 cards with topic "Accounting & 3 Statements" in `flashcards/data.json`, read in
full.** Not a sample. Each answer was checked against US GAAP convention: every stated figure
recomputed, every income statement / balance sheet / cash flow direction verified, every balance
sheet forced to balance, and the stated assumptions tested against the conclusion drawn from them.

Of the 209: 177 are prepared model answers and 32 are transcribed from the supplied M&I 2025 guide.

## Result

| | Cards |
| --- | ---: |
| Read in full | 209 |
| **Factual errors** | **4** (3 of them one shared sentence) |
| Defensible but incomplete or mismatched | 20 |
| Verified correct | 185 |

Two distinct defects, both correctable in the source JSON. Neither is an arithmetic slip — every
number in every worked card recomputes correctly, including the cases most likely to go wrong
(PIK accretion, MACRS vs book depreciation with the resulting DTL, debt extinguishment gains,
asset sales at a loss, recovery waterfalls). The errors are a wrong convention statement and a
wrong template applied to a question.

---

## Errors

### 1. Lease principal classification — F0882, F1626, F1896

Three cards share one answer template containing this sentence:

> Lease principal is financing cash flow; interest classification follows the applicable reporting rules.

**Why it is wrong.** Stated without qualification, this is false under US GAAP and it contradicts
the same answer two sentences earlier, which correctly says operating leases produce "operating
cash payments" while finance leases put "principal in financing cash flow." Under ASC 842 an
operating lease has no principal/interest split on the cash flow statement at all — the entire
lease payment is an operating outflow. Only finance-lease principal is a financing outflow.

A student who reads the blanket sentence will move operating-lease payments out of CFO, which
inflates CFO and inflates any CFO-based cash conversion or coverage figure. The deck's own M&I
guide card F1963 states the rule correctly, so the deck currently contradicts itself.

**Corrected wording** (replaces that sentence in all three cards):

> Finance-lease principal repayments are a financing outflow, while operating-lease payments under
> ASC 842 sit entirely in operating cash flow; interest classification follows the applicable
> reporting rules.

Affected cards: **F0882** (operating vs capital lease accounting), **F1626** (lease vs buy case),
**F1896** (Vici/Blackstone lease revenue — this card is also a topic mismatch, see notes below).

### 2. F1536 — an equipment purchase answered as a depreciation charge

Question: *"Walk through the three-statement effects of purchasing $100 of equipment, immediately
and one year later."*

The card currently answers with the symbolic depreciation template:

> For this 100 increase in depreciation: EBIT changes by -100; net income changes by -100*(1-t);
> the non-cash add-back changes by 100; cash changes by 100*t. PP&E changes by -100 ...

**Why it is wrong.** Buying $100 of equipment is not a $100 expense. A capitalized purchase has
**no** income statement effect at acquisition: PP&E rises 100, cash falls 100 (or debt/equity
rises), and the 100 is an investing outflow. The depreciation charge one year later is 100 divided
by the useful life, not 100. As written the card asserts that a $100 purchase cuts EBIT by 100 and
*reduces* PP&E by 100 — both the opposite of what happens, on exactly the capitalize-vs-expense
distinction interviewers use this question to test.

This is the only one of the five cards using this template that is misapplied; F0038, F0218,
F0406 and F1771 are genuine depreciation questions and are correct.

**Corrected wording:**

> Capitalize the purchase. At acquisition, PP&E rises 100 and cash falls 100 (if financed, show the
> financing inflow and the debt or equity increase instead of the cash decline); the 100 is an
> investing outflow and there is no income-statement effect, so net income is unchanged. One year
> later, straight-line depreciation is (100 - residual value) / useful life; call it d. EBIT and
> pre-tax income fall d, net income falls d*(1-t), d is added back in indirect CFO so cash rises
> d*t, net PP&E falls d and retained earnings fall d*(1-t); the balance sheet balances. Neither the
> useful life, the financing nor the tax rate is supplied, so keep both steps symbolic. Do not
> expense a capitalized purchase in the year of acquisition.

---

## Not errors: incomplete, ambiguous or mismatched

These are defensible as far as they go — nothing in them is factually wrong — but the answer does
not reach what the question asked, usually because a generic template was attached to a specific
prompt. Listed separately so they are not counted as errors.

**Answer never addresses part of the question**

- **F0193** — asks "which value is more useful for a lender to look at?" The answer defines FCFF,
  FCFE and EBITDA correctly but never names the lender's preference or says why.
- **F0660** — asks about accounts receivable *and* accounts payable. Only AR is covered.
- **F0654** — asks what types of companies carry deferred revenue. No company type is named.
- **F1493** — asks to compare balance-sheet lenders with advisory-only banks. Explains bank balance
  sheets; never discusses advisory-only economics.
- **F1857** — asks when a reorganized company can use NOLs after bankruptcy. Gives the general
  deferred-tax answer with a correct Section 382 caution, but not the bankruptcy-specific rules
  (the 382(l)(5)/(l)(6) exceptions, attribute reduction for cancellation-of-debt income).
- **F1234** — coffee machine bought by a dental clinic: covers the depreciation but skips the
  initial capitalization and cash outflow.
- **F1919** — gift card deferred revenue: correct, but omits breakage, which is the point of the
  gift-card version of the question.

**Generic template attached to a specific question**

- **F0010** — build a cash flow statement and ratios → generic business-diligence framework; never
  mentions the indirect method, CFO/CFI/CFF or a single ratio.
- **F0027** — multi-year inventory purchase financed with debt → depreciation-only boilerplate.
- **F0252** — SaaS debt capacity on cash EBITDA → deferred-revenue boilerplate.
- **F0622** — calculate cash burn starting from EBIT → EBITDA-definition boilerplate.
- **F0845** — calculate the tax rate from the supplied figures → depreciation boilerplate; never
  states taxes / pre-tax income.
- **F1345** — "$5 increase in revenue" → generic three-statement bridge. This is a standard
  question with a standard answer (NI +5(1-t), CFO +5(1-t), cash and retained earnings +5(1-t)
  assuming no associated cost and cash collection); the card declines to give it.
- **F1489** — activist stake in another company → unit-economics boilerplate; never mentions how
  the stake is carried (fair value, equity method, consolidation).
- **F1497** — statement effects of selling a business unit → investment-pitch boilerplate.
- **F1600** — depreciation *and* deferred revenue → depreciation boilerplate only.
- **F1896** — Vici vs Blackstone lease revenue → lease-accounting boilerplate, unrelated to the
  question. (Also carries error 1.)
- **F0900** — gives $100 inventory, 10% interest split 5% cash / 5% PIK, 20% amortization and a
  $200 sale; only the tax rate is missing. F0901 works an almost identical case symbolically in t,
  so this one could be worked rather than deferred to boilerplate.

**Wording worth tightening**

- **F1957** (M&I guide) — "Preferred Dividends appear on the Income Statement." They are not an
  expense in arriving at net income; they are deducted below net income to reach income available
  to common. Defensible as written since that deduction is presented on the face of the statement,
  and it is transcribed guide text, so left unchanged.
- **F1659** — the prompt is a statement of the retained-earnings roll-forward (which is correct);
  the answer discusses cash dividends and enterprise value. Adjacent, not responsive.

---

## Spot-checks worth recording

These are the cards where a wrong answer would have been easiest to produce, and all reconcile:

- **F0833** — $1,000 PP&E, $500 at 10% cash interest, $500 at 5% PIK, book depreciation 100 against
  MACRS 200. Book EBT -175, taxable income -275, CFO -50 + 275t, debt +25, **DTL +100t**. Assets
  -150 + 275t against liabilities and equity -150 + 275t. The deferred-tax direction is right.
- **F0919** — 60% tax rate, PIK accretion and 20% amortization: CFO 70.5 by two independent routes
  (100 - 2.5 - 27, and NI 18 + inventory 50 + PIK 2.5), debt ends 42.5, balance sheet balances.
- **F1758** — $400 of debt repurchased at 60: gain 160, NI +96, gain reversed out of CFO at -64,
  financing -240, cash -304 against debt -400 and equity +96.
- **F1746** — asset sold at a loss: CFO +8, investing +80, cash +88, PP&E -100, equity -12.
- **F1215** — gift card plus cash: cash +50 - 70t, inventory -30, deferred revenue -50, balances.
- **F2199** — utility rate case: equity 1,000, allowed NI 120, pre-tax 160, revenue requirement 300,
  and the GWh-to-kWh unit conversion to $0.20/kWh is right.
- **F0894 / F1162 / F1856 / F2134 / F2136** — recovery waterfalls, all correctly ranked and divided.

## What this audit does not cover

Only the factual accuracy of the answer text for this one topic. It does not re-check the
structural verification flags in `question_flags.md`, and it says nothing about the other 2,000
technical cards. The 27-card sample in `answer_review.md` covered 10 accounting and enterprise
value cards; those were re-read here as part of the full pass and remain correct.
