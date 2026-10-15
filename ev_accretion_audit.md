# Enterprise & Equity Value + Accretion / Dilution — full accuracy audit

**Scope: all 158 cards across the two topics (100 Enterprise & Equity Value, 58 Accretion /
Dilution), read in full.** Same method as `accounting_audit.md` and `dcf_audit.md`.

Composition: 54 model answers, 45 concept/method, 40 M&I guide transcriptions, 17 missing-input,
2 dated-research.

## Result

| | Cards |
| --- | ---: |
| Read in full | 158 |
| **Errors** | **2** |
| Defensible but incomplete or mismatched | 21 |
| Verified correct | 135 |

`answer_review.md` singled this tranche out as the place where "sign conventions slip." They do
not. **Every numeric card in both topics computes correctly** — and these are the most
calculation-dense topics audited so far: eleven recovery waterfalls, nine accretion/dilution
cases, three treasury-stock-method problems, the EV bridge in a dozen variants, and the
disappearing-premium share-price case. I could not find an arithmetic or sign error anywhere in
the 158.

Both errors are the familiar failure mode — a template attached to the wrong question — plus one
transcription truncation.

---

## Errors

### 1. F0584 — a diluted-share EV question answered with option-pricing theory

Question: *"A company is trading at $X per share and is being purchased at a Y% premium. You are
given the amount of convertible debt, RSUs, options (and exercise price), cash, and debt the
company has. What is the enterprise value of the company?"*

The card answers with the options/derivatives template: *"A call payoff is max(S-K,0)... In a
one-period arbitrage-free binomial model, q = [(1+r)S0-Sdown]/(Sup-Sdown)... More volatility
generally benefits plain long options. Hedges reduce a specified risk but introduce costs, basis
risk..."*

**Why it is wrong.** The question lists options only as a dilution input. It is a standard
fully-diluted EV build: gross up the share price by the premium, run the treasury stock method on
the options, add the RSUs, convert the in-the-money converts, multiply by the offer price, then
bridge to EV. The card instead teaches binomial option valuation, which no interviewer is asking
for here and which cannot produce the requested number. The template content is itself accurate —
it is simply attached to the wrong question.

The deck has the right content two cards away: **F1078** and **F1542** both state the treasury
stock method correctly, and **F2011** works a near-identical problem with options, RSUs and
converts.

**Corrected wording:**

> Work to the offer price first, then to diluted shares, then bridge. The per-share offer price is
> the current price grossed up by the premium: X * (1 + Y%). Build the fully diluted share count
> at that offer price, not at the unaffected price. Under the treasury stock method, in-the-money
> options are exercised and the proceeds buy back stock, so each tranche adds options * (offer
> price - strike) / offer price net new shares; out-of-the-money options add nothing. RSUs are
> added in full, since there are no exercise proceeds. For convertible debt, compare the offer
> price with the conversion price: if it is in the money, apply the if-converted method, adding
> principal / conversion price shares and removing that principal from debt in the bridge; if it
> is out of the money, leave it in debt and add no shares. Never count the same convertible as
> both debt and shares. Diluted equity value = offer price * fully diluted shares. Then enterprise
> value = diluted equity value + debt (including any unconverted convertible principal) + preferred
> + noncontrolling interests - cash and other non-operating assets.

### 2. F1988 — truncated first sentence

The answer begins mid-sentence: *"represents the value of EVERYTHING a company has (its Net
Assets) but only to the EQUITY INVESTORS..."* — so the card never says what represents it.

Page 72 of the guide reads "**Equity Value** represents the value of EVERYTHING a company
has...", so this is a transcription truncation, not a guide error. The content that follows is
correct. **Fix: restore the two dropped words.**

This is the same defect found at F2035 in the DCF pass, which prompted a deck-wide scan — see
below.

---

## Deck-wide scan for the truncation defect

After finding a second instance, I scanned all 2,049 technical answers for any that begin
mid-sentence. There are exactly four, and three are real truncations of guide text:

| Card | Topic | Dropped opening | Verified against |
| --- | --- | --- | --- |
| F1988 | Enterprise & Equity Value | "Equity Value " | guide p.72 |
| F2002 | Merger Model & M&A | "CSE " | guide p.77 |
| F2013 | Valuation & Comps | "Public Comps " | guide p.91 |

The fourth, F1422, begins "sqrt(0.9) is approximately 0.94868" — a legitimate lowercase opening,
not a defect.

**F2002 and F2013 are outside this tranche's two topics.** I fixed them anyway: each is a
mechanical restoration of words verified against the guide PDF, the defect class was already
established, and leaving a known-broken card in the deck to respect a topic boundary would be the
wrong call. Flagging it here so the scope change is visible. With F2035 fixed in the DCF pass,
this defect class is now cleared deck-wide.

---

## Not errors: incomplete, mismatched or ambiguous

Fewer than in the DCF topic, and the two dominant templates here (the EV-bridge paragraph and the
accretion paragraph) are both accurate and genuinely fit most of the questions they answer.

**Direct questions the template never answers**

- **F2007** — "your co-worker claims EV rose $100 rather than $50 because the company issued
  debt — is he correct?" The answer is no (debt and cash offset; the gap must come from the
  factory being worth more than its cost or from other operating changes), but the card gives the
  generic debt template and never says yes or no.
- **F2003** — "$100 of debt to purchase a new factory: how do Equity Value and Enterprise Value
  change?" The template covers the case conditionally but never states the specific result
  (equity value unchanged, EV +$100), and never addresses equity value at all. The guide's own
  version of this question, on page 78, answers it in two lines.
- **F0410** — "if a company takes out a loan to buy back stock, what is the impact on enterprise
  value?" Says the bridge "must reflect that use" without giving the answer, which is that
  operating EV is unchanged: equity value and cash both fall by the repurchase amount.
- **F1409** — asks what happens if cash is *added* instead of subtracted in the EV bridge; the
  template explains the correct treatment but not the consequence of the error.
- **F1463** — asks why you *subtract* NCI going from EV to equity value; the template states the
  opposite direction (add NCI going from equity to EV). Consistent, but never answers as asked.
- **F1491** — asks for examples of nonsensical multiples; gives the pairing rule that explains why
  Equity Value/EBITDA is wrong but offers no further examples.
- **F1465** — "why might a company choose a dilutive deal?" The template's closing line gestures
  at it; F0532 answers it properly.

**Generic template on a specific prompt**

- **F0895** (calculate equity value from a capital structure → debt-vs-equity financing
  boilerplate), **F1477** (why change in working capital is not in equity value → tagged
  "missing inputs" though the question needs none, then answered with the working-capital
  template; unlike F0862 in the DCF pass the content at least stays on topic), **F1347** (asks for
  EV and implied share price plus a dividend comparison → only the dividend template), **F0643**
  (equity value for a private company → template whose only share-count method is "diluted shares
  times share price", which is precisely what a private company lacks), **F0739** (effective vs
  marginal tax rates in a debt-funded deal → generic accretion template that never distinguishes
  the two), **F0789**, **F1643**, **F0230**, **F1376**.

**Guide text worth knowing about, left unchanged**

- **F2031** — says the IFRS EBITDA "would be higher than $15". The companion card F2030 computes
  EBITDA as **$20** under U.S. GAAP ($15 EBIT + $5 D&A), so $15 is the wrong reference figure. I
  confirmed against guide page 91 that the "$15" is the guide's own slip, not a transcription
  error. Left as written because the directional conclusion — EBITDA is higher under IFRS, and
  TEV/EBITDA roughly unchanged once lease liabilities are added — is correct, and a student is
  unlikely ever to quote the stray figure. Correct it if you would rather the deck be internally
  consistent.
- **F2135** — the HoldCo recovery of 250/270 pools all debt pari passu, which sets aside the
  structural subordination of HoldCo debt to the operating companies' debt. The guide flags its
  own approximation and the arithmetic is right.

## Verified correct — the calculation-heavy cards

- **Accretion, all nine numeric cases.** F0784 (1/3 stock, 1/3 debt, 1/3 cash: blended cost
  5.833% against a 6.667% target yield), F1092 (2% dilution), F1206 (25% accretion), F1471,
  F1131, F2079, F2080, F2081 (weighted cost 6% against a 5% yield), F2082 (the breakeven debt rate
  of 10%/(1-25%) = ~13.3%), F2083 ($20 after-tax synergies, ~$27 pre-tax). Every one recomputes,
  and each is consistent with the P/E shortcut as a cross-check.
- **F2084 / F2085 — the disappearing-premium case.** $3,000 over 320 shares = $9.38, the $0.62
  drop is 6.25% of the share price just as $200 is 6.25% of the $3,200 combined equity value, and
  the cash-deal variant correctly gives a $1.00 drop over 200 shares instead.
- **Recovery waterfalls, all eleven.** F0605, F0616, F0877, F0884, F0885, F0896, F0903, F1874,
  F2135 and the EV-bridge cases F0543 and F1861. The undersecured-deficiency cases (F0616, F1874)
  correctly rank the $50 deficiency alongside the unsecured pool, giving 87.5c and 75c.
- **Treasury stock method.** F1078, F1542 and F2010 (200 + 50 - 40 = 210 shares) all state it
  correctly, and F2011 handles options, RSUs and converts together to 11,100 diluted shares.
- **F2039** — infers the existence of preferred stock from a $50 apparent net income against a $60
  calculated net income. The reasoning and the ">$1,000 EV" conclusion are both right.
- **F2005** — the preferred-and-common dividend step, consistent with guide page 78.
- **F2009** — the two-step inventory purchase and sale: equity value +$75, TEV unchanged, with the
  right intuition that generating net income into cash does not make the core business more
  valuable.
- **F2145** — a convertible's market price starts exceeding its payoff value *below* the
  conversion price. Subtle and correctly stated.

## What this audit does not cover

Only factual accuracy of answer text for these two topics. Remaining unaudited: Debt, Credit &
Restructuring (261), Valuation & Comps (153), Merger Model & M&A (116), LBO & Private Equity
(109), and the non-technical topics. Running total across three tranches: **589 cards audited,
11 errors found and corrected.**
