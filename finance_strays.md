# Finance technicals moved out of the behavioral deck

The behavioral file holds a group of genuine finance questions that arrived with the fit
questions, usually because the interview mixed the two. The brainteaser pass left them because they
are not quantitative puzzles. **Thirty behavioral entries have now been dealt with: 29 are
technical cards with written answers, and two more were folded into technical cards that already
asked the same question.**

| | |
| --- | ---: |
| Behavioral entries read for this pass | 1,151 |
| Candidates examined | about 50 |
| **Moved, with a written answer** | **29 cards** |
| — from the known guidance family | 19 entries → 18 cards (two merged) |
| — found by reading, outside that family | 9 |
| — split out of a card that welded two questions together | 2 |
| Folded into an existing technical card | 2 |
| Left in the behavioral deck | 15 |
| Deck total | 3,317 (was 3,318) |

Technical goes from 2,167 to 2,196 and behavioral from 1,151 to 1,121. The total falls by one,
which is the arithmetic of the merges: two entries folded into existing cards and two merged into a
single new card (−3), against two cards split out of welded entries (+2). Nothing was dropped.

## How the strays were found

The 25 cards carrying the *A technical question filed with the behavioral set* guidance family were
the starting point, but that list was neither complete nor all finance: six of its members are
statistics and machine-learning questions. All 561 General Fit cards were read, plus a keyword
sweep over the whole behavioral deck for finance vocabulary and a sweep for definitional question
stems ("what is a", "walk me through the", "what is the difference between"). That turned up nine
more, including the two named in the brief that were not in the family — the SaaS metrics question,
filed under General Fit, and the Google/Nest question, which the topic router had put under *Why
Banking* because it starts with "Why".

Each one was checked against the existing technical deck before being written, which changed the
treatment of four cards (below) and supplied the factual anchors for the rest: the mid-year
convention cards for the mid-period adjustment, the dividend recap and sponsor-versus-strategic
cards, the SaaS retention definitions, the credit underwriting template, the structural
subordination card and the renewables guide answers.

## What moved

**Source context decided several of these.** The behavioral entries carry a firm label, and the
neighbouring entries come from the same interview, which is often the only thing that fixes what a
short question means:

- **B0369, the two identical buildings** (now F2625) was flagged in the brief as possibly
  unanswerable. The source is **Eastdil Secured**, a real-estate investment bank, which makes it an
  ordinary property-valuation question: the rent roll, tenant credit, occupancy, condition,
  encumbrances and the buyer's own tax position. It is answerable and it is now answered.
- **B0372 and B1018** ("What types of adjustments do you expect to encounter?", "What adjustments
  are you familiar with?") are both from **Ernst & Young M&A**, and B1018's neighbours are "Why
  Transaction Services?" and "Why TS industries?". That fixes "adjustments" as quality-of-earnings
  adjustments in financial due diligence. The two ask the same thing, so they are **one card**
  (F2639), which also says to clarify the word, because in a merger model it means purchase
  accounting and in comps it means comparability.
- **B0987** ("How do public companies raise money and how do governments raise money?") is from
  **Wells Fargo Public Finance**, so the government half is answered on municipal bonds — general
  obligation against revenue, the tax exemption, the note products — rather than on Treasury
  auctions alone.
- **B0108** ("the underwriting process of a fake transaction") is from **BNP Paribas Leveraged
  Finance**, so it is answered as a leveraged financing: commitment letter, flex, syndication and
  the hung-deal risk. "Fake" was read as hypothetical and the wording adjusted to say so, with the
  original recorded in the card's notes.
- **B0731** ("Walk me through the BS Equation") is from **Nomura Global Markets**, where BS can also
  mean Black-Scholes. The card answers the balance sheet reading and says to ask.

The 29 new cards, by topic:

- **Debt, Credit & Restructuring (5):** YTM/YTC/YTW with worked numbers (F2620), how public
  companies and governments raise money (F2627), unrestricted versus non-guarantor subsidiary
  (F2633), what to examine before lending (F2643), the underwriting process (F2645).
- **Accounting & 3 Statements (5):** the balance sheet equation (F2621), building an expense model
  (F2622), diligence adjustments (F2639), amortising subscriptions (F2642), three items in a 10-K
  (F2644).
- **Merger Model & M&A (4):** why Google paid about $3.2bn for Nest (F2626), strategic buyer versus
  financial sponsor (F2628), what companies are trying to achieve when they merge (F2640), purchase
  accounting (F2648).
- **DCF & Intrinsic Value (3):** WACCs falling across the board (F2624), the mid-period adjustment
  (F2632), valuing a solar project (F2647).
- **LBO & Private Equity (3):** when a dividend recap does not help (F2623), the sources and uses
  table (F2634), general partner versus limited partner (F2635).
- **Options & Derivatives (2):** the capped call (F2630) and the martingale (F2631).
- **Markets & Economy (2):** the Fed's mandate (F2636) and USD appreciation on the sale of a
  European subsidiary (F2638).
- **Deal & Process (2):** PIPEs (F2637) and the routes to going public (F2641).
- **Valuation & Comps (1):** the two identical buildings (F2625).
- **Industry & Company Analysis (2):** SaaS metrics (F2629) and the payments chain behind a Square
  transaction (F2646).

Each answer follows the house shape — a line of framing, then labelled bullets — and the stored
`topic` field names the destination topic exactly, which the build now honours. Firm sources are
carried across unchanged, and each card's notes record the behavioral id it came from.

Two numbers in the answers were computed rather than asserted. The bond in F2620 yields 15.96%
semi-annual and 16.13% annual to maturity at a price of 80, 26.3% to a 105 call in two years, and
the same bond at 108 yields 8.0% to maturity against 7.0% to a 103 call — which is what makes the
discount-bond and premium-bond cases in the yield-to-worst bullet concrete rather than asserted. The
WACC example in F2624 (7.8% falling to 6.4% on 150bp) was worked through.

## Two cards were split, two folded

- **B0625** welded a fit question to a technical one: "Why are you interested in renewables? How
  would you value a solar project?" The fit half stays; the valuation half is F2647.
- **B0698** did the same: "Tell me about a time you stepped outside your comfort zone. Separately,
  explain purchase accounting and the accounting adjustments in an M&A transaction." The story half
  stays; the technical half is F2648.
- **B0983** ("If you could choose 2 statements what would they be?") is the standard
  two-of-the-three-statements question, which the technical deck already asks properly as **F0732**.
  Rather than add a near-duplicate with a truncated prompt, the entry is folded into F0732 as a
  variant and its Wells Fargo source carried across.
- **B1134** ("Compare financing methods for a deal and their advantages and disadvantages") is
  already **F1789**, which answers cash, debt and stock from both sides. Folded in the same way.

One move does overlap an existing card deliberately. **F2640** ("What are companies trying to
achieve when they merge?") duplicates the subject of F0106, but F0106's answer is a
deal-assessment template shared across 27 cards and never names the motives, so the new card
answers the question directly. F0106 was left alone, since editing it would change 27 cards.

## The 15 left behind, and why

**Six are statistics, machine learning or quant, not finance** — B0189 (where eigenvalues come into
play), B0213 (the assumptions of a linear model), B0529 (R squared, time series, Fama-French),
B0188 (solving a problem "in the linear case"), B0517 (how AI models work "at a detailed level") and
B1148 ("Explain machine learning"). These are the whole of what is left in the guidance family,
which is now a clean quant group. Three of them have lost their context and the other three are
openers for a conversation rather than questions with an answer; none belongs in a finance deck.
They keep the guidance that tells a student to answer them as technical questions.

**Six cannot be answered because the transcription lost the context:**

- **B0911** — "Could you go into more detail on what makes it different than the other statements?"
  No statement is named.
- **B1019 / B1020 / B1021** — "What documents would you request from the CFO?", "What questions
  would you ask the CFO?", "What information do you need before starting work on the case?" These
  are case questions whose case is not recorded.
- **B0732** — "What are the problems and limitations of this formula?" The formula is not
  identified.
- **B0499** — "How much would you pay for an asset that pays a fixed amount?" The amount, the
  timing and the discount rate are all missing; it already carries **Incomplete prompt**.

**B0478** is left because its premise cannot be read reliably: "2 companies, same profiles, GM 0%,
one with 15% and one with 20% growth, what metric would you use to differentiate between them?" The
question it is reaching for — use a growth-adjusted multiple when everything else matches — is
answerable, but "GM 0%" could be a zero gross margin or a zero difference in margin, and those are
different questions. Guessing it would put a confident answer on a prompt nobody can verify.

**B0973** — "You have to use the rule of 72 to figure this out" — is a fragment with no question
attached. It already carries the **Not a question** flag from the earlier pass.

**One is a dated market opinion**: B0547, "Why did oil prices fall and the yuan depreciate?", which
needs the interview's own date to answer and belongs with the market-view questions rather than the
technicals.

**B0862 did move**, although the brief flagged it as possibly unanswerable, because the mechanism
behind an economy-wide fall in WACC is a DCF question with a definite answer. The card gives the
mechanism, a worked example and the episodes rather than pretending to recall a specific
conversation.

## Three things noticed in passing

**Group tags are keyword-derived from the question and the answer together**, so a long answer picks
up sector tags from incidental words. Writing these cards surfaced it clearly: the capped call card
was tagged *Consumer & Retail* because the answer mentioned retail products, the lending card
*Energy & Power* for a passing "utility", the payments card *Healthcare* for "software provider".
The wording of the new answers was tightened where it produced a plainly wrong tag; the mechanism
itself is unchanged, and the same noise exists on older cards. Narrowing the group rules to the
question would re-tag much of the deck and is a separate job.

**The technical metadata was stale.** `entry_count` and `answer_status_counts` still described 2,049
entries, from before the brainteaser move and the earlier additions. Both are now recomputed from
the file.

**The behavioral file's header counts disagreed with themselves.** The brainteaser pass updated the
behavioral line to 1,151 but left the finance line at 2,255, so the two no longer summed to the
stated 3,506. Both lines are now consistent again: 1,121 behavioral and 2,385 finance.

**`Technical_Questions_and_Answers.txt` is stale** — it predates the brainteaser move as well as
this one. Nothing reads it (the build reads the JSON), so it was left alone, but it should either be
regenerated or deleted.
