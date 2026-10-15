# Debt, Credit & Restructuring — full accuracy audit

**Scope: all 261 cards with topic "Debt, Credit & Restructuring" in `flashcards/data.json`, read
in full.** Same method as the three previous tranches.

Composition: 96 concept/method, 82 model answers, 32 M&I guide transcriptions, 25 missing-input,
15 dated-research, 11 open framework.

## Result

| | Cards |
| --- | ---: |
| Read in full | 261 |
| **Errors** | **4** (3 of them one shared defect) |
| Defensible but incomplete or mismatched | 26 |
| Verified correct | 231 |

`answer_review.md` nominated this tranche for "waterfall and recovery logic." That logic is
sound: every waterfall, every recovery percentage, every bond price and yield recomputes
correctly. Among the cards verified here are two YTM solutions that required solving a quadratic
and a five-period annuity, and both are right to the basis point.

All four errors are the same failure mode as the previous three tranches — a shared template
attached to a question it does not fit. There are no finance errors in this topic.

---

## Errors

### 1. Bond-price mechanics answered with the "identical companies" template — F0599, F0600, F0601

Three cards ask a bond-mechanics question and receive a template about business quality:

> Identical current statements do not guarantee identical future cash flows or risk. One may have
> stronger customer retention, better products, patents, management, governance, backlog... If all
> future cash flows, risk, rights and information are truly identical, intrinsic value should be
> identical; a price difference would then reflect **market mispricing** or omitted assumptions.

**Why it is wrong.** These questions have clean mechanical answers that have nothing to do with
customer retention or patents, and the template's conclusion — that any remaining difference is
mispricing — is the wrong explanation.

- **F0599 / F0600** — *"Why could two companies with identical financial profiles have bonds with
  the same yield to maturity and par value but different prices?"* Price is determined by coupon,
  maturity and yield. Hold yield and par constant and a price difference means the coupons or the
  maturities differ: a higher-coupon bond trades at a higher price for the same YTM. This is not
  mispricing, it is arithmetic.
- **F0601** — *"Two companies, same coupon, both trading at par, what has the higher YTM?"*
  Neither. A bond priced at par has a YTM equal to its coupon rate, so two par bonds with the same
  coupon have the same YTM. The question is a trap testing whether the candidate knows the
  par/coupon/yield identity, and the card answers with business-quality factors instead.

**The deck already contains the correct answer.** F0627 asks essentially the same thing as
F0599/F0600 and answers it properly: *"Bonds can have identical quoted YTM but different coupons,
maturity, call terms or cash-flow schedules, producing different prices."* As with the ASC 842
lease sentence and the CapEx card in earlier tranches, the deck currently contradicts itself.

**Corrected wording, F0599 and F0600:**

> Price, coupon, maturity and yield are linked by one equation, so fixing the yield and the par
> value forces the difference into the other two. A bond's price is the present value of its
> coupons and principal discounted at its YTM, so two bonds with the same YTM and the same par
> value trade at different prices when their coupon rates differ, their maturities differ, or
> their payment frequency or day-count conventions differ. The higher-coupon bond trades at the
> higher price, because the same yield is being delivered through larger interim payments. A bond
> priced above par has a coupon above its YTM; one priced below par has a coupon below its YTM.
> Quoted price conventions matter too: clean versus dirty price differ by accrued interest, and a
> total market value also depends on the face amount outstanding. Only after those mechanical
> explanations are excluded should you reach for issuer-level differences such as liquidity,
> covenants, call features or credit, and those would normally show up in the yield rather than
> leaving it unchanged.

**Corrected wording, F0601:**

> Neither — they have the same YTM. A bond trading exactly at par has a yield to maturity equal to
> its coupon rate, because the price equals the redemption amount and there is no amortized gain
> or loss to add to or subtract from the coupon income. Two bonds with the same coupon, both at
> par, therefore have the same YTM regardless of the issuers' differing business quality, and the
> market is telling you it requires the same yield from both. The question tests whether you know
> that identity rather than inviting a comparison of the two companies. Qualifications: the bonds
> must have the same payment frequency and day-count convention, "par" must mean a clean price of
> 100 rather than a dirty price including accrued interest, and if either bond is callable the
> relevant comparison becomes yield to worst, which can differ even when both trade at par. A
> credit difference between the issuers would show up as a price difference away from par, not as
> different yields at the same price.

### 2. F0608 — Chapter 7 liquidation answered with bank valuation

Question: *"Value post chapter 7 bankruptcy liquidation?"*

The card answers with the commercial-bank valuation template: *"Banks are usually valued with
equity-based methods such as dividend discount, FCFE or residual income, plus P/E and
price/tangible book cross-checks. Deposits and debt are operating funding... Forecast net interest
income, fees, credit losses, expenses, regulatory capital and distributable earnings."*

**Why it is wrong.** Nothing in the question concerns a bank, and none of the methods listed apply
to a liquidation. A Chapter 7 liquidation valuation is an asset-by-asset recovery exercise, not a
going-concern earnings model — dividend discount and residual income models assume exactly the
continuing operations that Chapter 7 ends. The deck has the right machinery on its waterfall
cards (F0501, F1365, F1876) but points this question at the wrong template.

**Corrected wording:**

> A Chapter 7 liquidation is valued asset by asset, not as a going concern, so the earnings-based
> methods used for an operating company do not apply. Start from the balance sheet and estimate
> gross recoveries on each asset class under a forced or orderly sale, applying recovery rates
> that reflect how saleable each one is: cash at or near 100%, receivables at a discount for
> collectability and aging, inventory well below book depending on whether it is finished goods or
> work in process, PP&E at market or scrap value rather than book, and intangibles and goodwill at
> little or nothing, since brand and going-concern value largely evaporate when operations stop.
> Then subtract the costs of the process itself — trustee and professional fees, wind-down and
> severance costs, lease rejection and contract breakage — because these are administrative claims
> paid ahead of creditors. Distribute what remains down the statutory priority: secured creditors
> against their collateral first, then superpriority and administrative claims, then priority
> unsecured claims such as certain employee and tax obligations, then general unsecured creditors
> pro rata, with equity last and almost always receiving nothing. Compare the result with the
> going-concern or reorganization value, because liquidation value is normally the floor that
> makes a Chapter 11 plan worth pursuing instead.

**Scope note:** F0601 sits in the "Industry & Company Analysis" topic rather than this one. I
corrected it anyway because it is the same defect, on the same instrument, as its two siblings
here, and the answer is determinate. Flagging it so the scope change is visible.

---

## Cross-topic finding, not corrected

The scan that found F0601 also showed the "identical companies" template on two
**Valuation & Comps** cards where it is a poor fit, each of which has a definite mechanical
answer:

- **F0697** — "Why might two companies have identical EV/EBITDA multiples but different P/E
  multiples?" (answer: differing leverage, tax rates, D&A and non-operating items — the two
  multiples sit on opposite sides of the capital structure)
- **F0735** — "You have two companies with the same P/E ratio. What makes their EV/EBITDA
  different?" (the same mechanics in reverse)

I left these alone. Unlike F0601, rewriting them needs real judgment inside a topic I have not
read, and they belong in the Valuation & Comps tranche. **Start that tranche with these two.**

The same template also sits on five Industry & Company Analysis cards (F1368, F1529, F1797,
F1798, and F0601 before correction) where it genuinely fits — those questions really are asking
why similar-looking businesses are valued differently.

---

## Not errors: incomplete, mismatched or ambiguous

**Direct questions the template never answers**

- **F1176** — "What is the order of repayment during a bankruptcy?" gets the restructuring-process
  template (13-week cash flow, Chapter 11 vs 7, prepacks, 363 sales) and never states the
  priority order, which the deck's own waterfall template gives.
- **F1263** — "Explain how credit ratings work" gets the credit-versus-equity investing template;
  no rating scales, agencies, investment grade versus high yield, or rating process.
- **F0966** — "What is the yield curve?" gets the macro template, which discusses inversion
  without ever defining the curve.
- **F1265** — "What does a flat yield curve mean for a fixed income investor?" — same template,
  and the investor implications (little term premium, weak roll-down and carry) are never drawn.
- **F1295** — "Explain debt covenants and give examples" gets the credit template, which names
  maintenance versus incurrence but gives no examples; F1291 has them.
- **F0125** — "What are the key credit-related KPIs?" gets the generic business framework, while
  the credit template sitting next to it lists exactly the KPIs asked for.
- **F2117** — asks the difference between coupon rate, current yield and YTM; defines the last two
  but never the coupon rate.

**Generic or wrong-flavour template on a specific prompt**

F0045 (credit analysis by industry), F0087 (three-statement effects of issuing a bond → the
debt-versus-equity choice template), F0226 (calculate a pro forma leverage ratio), F0488, F0493,
F0889, F1147 (wind-farm credit risk → generic credit rather than the project-finance template
the deck has), F1356 (creditor incentives by type), F1361 ("debt trading at 50c, buy or sell?" →
unit economics, while F1370 answers exactly this), F1366 (how distressed companies select
restructuring bankers → the restructuring-process template, unrelated), F1392, F1449, F1617,
F1882, F0467, F0618, F1363, F1212.

**"Explain it simply" answered technically**

- **F0725** — "explain the difference between bank debt and high yield debt to your grandmother"
  returns lien priority, intercreditor documents and call protection. Third instance of this
  pattern after F0551 and F1202 in the DCF tranche.

**Internal inconsistency worth a decision**

- **The three Cs of credit.** The credit template, on 27 cards, says the three Cs are "character,
  capacity and capital, with collateral and conditions added in a five-C framework." **F0052** —
  the one card actually asked *"What are the 3 C's of credit?"* — says "Character, Capacity and
  Collateral," with the five-C framework adding "Capital and Conditions." Both splits appear in
  the literature and both cards hedge with "commonly," so neither is wrong and I changed nothing.
  But the deck gives two different answers to the same question, and the outlier is on the card a
  student would actually look up. If you want them aligned, character/capacity/capital is the more
  common three-C subset and matches the other 27 cards.

**Guide text left as written**

- **F2121** — "Duration is the first derivative of the bond's price with respect to its YTM, and
  Convexity is the second derivative." Loose: modified duration is the negative of the first
  derivative divided by price, and convexity the second derivative divided by price. The deck's
  own concept template (F0185, F0259, F0814) states both correctly, and the guide's version
  conveys the right intuition, so I left it.
- **F2130** — describes DIP financing as having "repayment priority over all other existing
  secured/unsecured debt." In practice DIP loans get superpriority administrative status, and
  priming existing liens requires court approval and adequate protection under §364(d). The
  simplification is the standard interview answer; left as written.

## Verified correct — the calculation-heavy cards

- **F0883** — bond at 80, 12% coupon, 5 years: YTM 18.46%. I solved the annuity equation
  independently and it ties to within a cent. The card also gives the rough approximation (17.78%)
  and correctly labels it as one.
- **F1382** — bond at 65, 10% coupon, 2 years: sets up 65x² − 10x − 110 = 0 and gets 38.01%. The
  quadratic solves exactly.
- **F2119** — the approximate-YTM formula applied to a 5% discount bond: 9/97.5 = 9.2%.
- **F0058** — the three-year Apple factory sequence, including the year-3 write-down and debt
  repayment: cash −84, PP&E −80, debt −100, retained earnings −64, and the balance sheet balances.
- **F0628** — $100m of bonds repurchased at 106: a $6m extinguishment loss, net cash −104.02.
- **F1362** — $100M loan, half cash and half PIK, repaid in year 1: principal accretes to 102.5
  and the year-1 cash change of −105 + 5t reconciles.
- **F0705** — the debt-funded buyback: accretive if and only if original EPS exceeds $0.60. I
  derived the threshold independently and it is right.
- **F0874** — ROE of 15% from an unlevered 10% asset return, plus the correct alternative answer
  of 20% under the accounting (net income) definition of ROA. Flagging both definitions is the
  right call.
- **F1254** — the swap hedge directions. Pay fixed / receive floating against a floating-rate
  loan; pay fixed / receive floating against a fixed-rate bond asset. Both right, and this is the
  kind of card that is usually backwards.
- **F1854** — 8% cash coupon versus 10% compounding PIK over two years: $16 against $21.
- **F0597, F0619, F1027, F1828, F1173** — entity-level waterfalls and EV bridges, all correct,
  with F1828 flagging the units ambiguity rather than silently guessing.
- **F1979, F1980, F1983, F1984, F1985** — the five M&I debt walkthroughs. All balance, including
  the final one where the $190 debt repayment exceeds the $180 PP&E reduction, leaving cash up
  $20 rather than $30.
- **F2123** — yield to worst: YTW equals YTM for a discount bond and is at most YTM for a premium
  bond, with the right intuition for both.
- **F2158, F2218** — LCR and NSFR both correctly defined at a 100% minimum; DSCR and LLCR formulas
  and the CFADS build all correct.

## What this audit does not cover

Only factual accuracy of answer text for this topic. Remaining unaudited: Valuation & Comps (153),
Merger Model & M&A (116), LBO & Private Equity (109), and the non-technical topics. Running total
across four tranches: **850 cards audited, 15 errors found and corrected.**
