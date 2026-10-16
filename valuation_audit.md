# Valuation & Comps — 153-card answer audit

Audited October 15, 2026. Starting repository revision: `4d062bb`. Scope: the 153 technical cards whose generated topic was exactly **Valuation & Comps** at that revision.

## Results

All 153 question–answer pairs were read in eight sequential batches (seven of 20, one of 13). The review checked question/answer fit, assumptions, multiple conventions, accounting effects, and stated numerical results. Guide answers were compared with the supplied PDF.

| Initial finding | Cards | Action |
| --- | ---: | --- |
| Incorrect answer for the question | 13 | Corrected |
| Incomplete or ambiguous answer | 56 | Two wording clarifications applied; 54 left unchanged and documented below |
| No issue found within this review | 84 | Unchanged |
| Total reviewed | 153 | 15 source answer fields edited |

Of the 13 corrected entries, **12 address the wrong task, omit its central mechanical answer, or violate its premise; one contains a substantive conceptual claim from the guide (F2019)**. This is not a claim that 13 numerical calculations were wrong. No arithmetic error was found in the existing worked numerical answers reviewed. F2038 had no solution because an unrelated template had replaced it; the replacement restores the correct result.

Two ambiguities are counted separately rather than added to the error total. The remaining 54 incomplete or qualified answers have not been made interview-ready by this audit. A “no issue found” result is a scoped review conclusion, not a guarantee that an answer covers every possible follow-up.

Only `answer` fields changed in the source JSON. Question wording, IDs, firm/guide source labels, references, answer-status metadata and topic rules were retained. The two generated data files were rebuilt with the existing builder. Existing structural “Verified” flags are not finance-audit certifications. This audit does not re-audit prior topics or verify current market prices, named-company peer sets, or a candidate’s personal deal experience.

## Corrected answers

### F0382

**Question:** Walk through multiple years of the three statements after buying $200 of PP&E, financed half with debt and half with cash. [Other assumptions not recorded.]

**Source labels:** Citi Technology SF

**Original problem:** A corporate comparable-companies template was supplied for a multi-year equipment-purchase accounting case.

**Why:** Valuation-comps template is unrelated to a $200 equipment three-statement case; initial PP&E/cash/debt effects are determinable.

**Replacement answer:** At purchase, capitalize $200 of PP&E. A $100 debt draw creates a $100 financing inflow; the equipment purchase creates a $200 investing outflow, so cash falls $100, PP&E rises $200 and debt rises $100. There is no immediate income-statement effect, ignoring fees. For each later year, let d be depreciation, I cash interest on the outstanding debt, P principal repaid and t the tax rate. With no other operating changes and an immediately usable tax deduction, net income and retained earnings fall (d+I)*(1-t). Add back d in indirect CFO: CFO changes by -I+(d+I)*t. Principal repayment is a financing outflow P, so cash changes by -I+(d+I)*t-P; net PP&E falls d and debt falls P. These incremental balance-sheet changes balance. Roll debt and asset balances forward each year; straight-line d=(200-residual value)/useful life. Useful life, rates, timing and repayments are missing, so later years must remain symbolic. If tax deductions are not currently usable, model cash taxes and deferred taxes separately.

### F0466

**Question:** How would you value different asset classes?

**Source labels:** Dodge & Cox

**Original problem:** An asset-allocation framework was supplied instead of methods for valuing asset classes.

**Why:** Portfolio-allocation template answers what to own, not how to value different asset classes; none of the requested valuation methods given.

**Replacement answer:** Value each asset using the cash flows or economic rights its owner receives. For equities, use equity cash flow/dividend or operating-company DCF with the appropriate EV-to-equity bridge, and cross-check suitable trading multiples. For bonds and loans, discount expected coupons, principal and recoveries consistently for rates, credit, timing and embedded options. For income-producing property, discount net property cash flow or capitalize stabilized NOI, then account for financing to reach equity value. For private equity, value the underlying businesses and deduct fund-level claims, fees and expenses rather than treating commitments as assets. Commodities usually require spot/forward market evidence and analysis of supply, demand, storage and convenience yield; they do not generally have an issuer-like earnings stream. Derivatives require contract-specific payoff models. Match risk, currency, liquidity and the legal claim; an asset-allocation decision is separate from estimating value.

### F0664

**Question:** How to value a company with negative net income and negative Ebitda?

**Source labels:** Financial Technology Partners SF

**Original problem:** A net-income-to-EBITDA definition was supplied instead of a method for valuing a loss-making company.

**Why:** NI-to-EBITDA definition template never values a negative-NI/negative-EBITDA business or handles unusable negative earnings multiples.

**Replacement answer:** Negative net income and EBITDA make historical P/E and EV/EBITDA unsuitable as straightforward valuation anchors; they do not automatically make the business worthless. Identify whether losses are temporary, growth-related or structural. Forecast revenue, sustainable margins, taxes, reinvestment and funding in base, upside and downside scenarios, then discount the resulting cash flows. Include cash burn before profitability and the risk the business fails to reach that stage. Use EV/revenue or forward positive-earnings multiples only with genuinely comparable economics and a credible profitability path. Add excess cash and subtract debt/other claims to reach equity consistently, accounting for financing needs without double counting them. If no viable going concern remains, examine realizable asset value and the claim waterfall instead.

### F0678

**Question:** Estimate a valuation multiple for an unfamiliar business using qualitative questions about unit economics, total addressable market and penetration, without asking for comparable-company multiples. [Business description not recorded.]

**Source labels:** GTCR

**Original problem:** The answer instructed the candidate to use peer multiples even though the question specifically disallows asking for them.

**Why:** Answer explicitly proposes comparable-company multiples despite the question forbidding that input; use fundamentals/implied multiples instead.

**Replacement answer:** Derive an implied multiple from fundamentals instead of asking for comparable-company multiples. Ask about market size and penetration, growth runway, customer retention, pricing, contribution margins, fixed costs, required CapEx/working capital and business risk. Convert these into forecast cash flows and discount them. Then divide the resulting enterprise value by the matching revenue or EBITDA measure to obtain an implied multiple. As a simplified sustainable-growth illustration, EV/EBITDA_1 = (FCFF_1/EBITDA_1)/(WACC-g), where both flow measures refer to next year and WACC exceeds g. Cash conversion must include taxes and the reinvestment required to support g. A changing-growth business needs an explicit forecast before its terminal period. No unique multiple can be calculated without the omitted business inputs, but the method does not require peer multiples.

**Formula check:** Start from EV = FCFF₁/(WACC − g) and divide by EBITDA₁. This is a sustainable-growth special case, not a universal multiple. Taxes and reinvestment drive conversion of EBITDA into FCFF; see [Damodaran’s Value/EBITDA notes](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/vebitnote.html).

### F0697

**Question:** Why might two companies have identical EV/EBITDA multiples but different P/E multiples?

**Source labels:** Goldman Sachs LA

**Original problem:** An identical-company template replaced the required relationship between operating multiples and equity multiples.

**Why:** Identical-company template omits the mechanical EV/EBITDA-to-P/E bridge; equal operating multiples do not mean identical financial statements.

**Replacement answer:** EV/EBITDA compares operating value with earnings before financing, tax and D&A; P/E compares common equity value with net income available to common shareholders. Therefore equal EV/EBITDA can coexist with different leverage, cash, interest costs, D&A, tax rates and non-operating items, producing different P/E ratios. Define B as debt + preferred stock + NCI - excess cash - other non-operating assets. Then equity value = EV-B, so P/E = [(EV/EBITDA) - B/EBITDA]/(common net income/EBITDA). For example, two unlevered, cash-free companies can each have EV=1,000 and EBITDA=100, hence EV/EBITDA=10x. With no D&A or other items, tax rates of 20% and 40% give net income of 80 and 60, and P/E of 12.5x and 16.67x. This is a mechanical example holding EV fixed, not a claim that taxes have no effect on intrinsic EV.

### F0735

**Question:** You have two companies with the same P/E ratio. What makes their EV/EBITDA different?

**Source labels:** Goldman Sachs NY

**Original problem:** An identical-company template replaced the mechanical bridge from P/E to EV/EBITDA.

**Why:** Equal P/E is not identical financial statements; answer omits mechanical bridge through NI/EBITDA and net debt/other claims.

**Replacement answer:** The same P/E does not imply the same operating valuation multiple. Let B = debt + preferred stock + NCI - excess cash - other non-operating assets. Since EV = common equity value + B and common equity value = (P/E)*common net income, EV/EBITDA = (P/E)*(common net income/EBITDA) + B/EBITDA. D&A, interest, taxes and non-operating items change net income relative to EBITDA; leverage, cash and other claims change the bridge. For example, at 15x P/E, common net income of 100 implies equity value of 1,500. If EBITDA is 200, net debt of zero gives EV/EBITDA=7.5x, while net debt of 500 gives 10x, with no other bridge items. The example takes those net-income figures as given; it does not assume identical interest expense or other earnings inputs.

### F0835

**Question:** How would you value a company with negative EBITDA?

**Source labels:** Guggenheim Partners NY; UBS NY

**Original problem:** An EBITDA definition replaced the negative-EBITDA valuation answer. Its cash-expense shorthand also obscured non-D&A noncash costs.

**Why:** EBITDA-definition template does not answer negative-EBITDA valuation. Its cash-operating-expenses shorthand also misses non-D&A noncash costs in unadjusted EBITDA.

**Replacement answer:** A negative EBITDA denominator makes a conventional EV/EBITDA comparison economically unhelpful. Determine why EBITDA is negative and whether the business can generate sustainable positive cash flow. Use a scenario DCF that includes losses, CapEx, working capital, funding requirements and failure risk before reaching normalized profitability. A revenue multiple or a forward positive-EBITDA multiple may provide a cross-check if peers have comparable growth, margins, capital needs and risk; do not assume all revenue deserves the same multiple. If the business cannot remain a going concern, use asset/recovery analysis instead. When reconciling earnings, unadjusted EBITDA adds back interest, taxes and D&A, not every non-cash expense; SBC and other adjustments require separate identification.

**Definition check:** Standard EBITDA is not earnings before every noncash charge. Additional adjustments must be distinguished from EBITDA; see the [SEC’s non-GAAP guidance, questions 103.01–103.02](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures).

### F0876

**Question:** Walk through multiple years of inventory, debt, PIK interest and debt amortization. [Inputs not recorded.]

**Source labels:** Houlihan Lokey Restructuring LA

**Original problem:** A comparable-companies template was supplied instead of the inventory, debt, PIK and principal-repayment roll-forwards.

**Why:** Comps template unrelated to inventory, PIK, interest and amortization accounting, even though missing inputs justify only a symbolic solution.

**Replacement answer:** Build an inventory, debt and cash-flow roll-forward for each year. Buying inventory increases inventory and reduces cash, or increases accounts payable if unpaid; borrowing to fund it is a separate financing inflow and debt increase. Recognize revenue when earned and inventory cost as COGS when sold, distinguishing cash sales from receivables. For opening debt D, cash interest c and PIK interest p for the period, both c and p reduce pre-tax income, but only c is paid currently. Add p back in indirect CFO; it increases debt without a cash financing inflow. Ending debt = opening debt + new cash borrowing + capitalized PIK - principal repaid, using the actual interest-accrual convention. Under the usual US GAAP interview convention, cash interest is operating and principal repayment is financing. Reconcile net income to CFO using non-cash charges and changes in receivables, inventory and payables; then update cash and retained earnings and check assets=liabilities+equity. Amounts, sales/collection timing, tax use and amortization terms are absent, so no unique multi-year numbers can be supplied.

### F1137

**Question:** How would you value an EBITDA negative tech company?

**Source labels:** LionTree

**Original problem:** An EBITDA definition replaced the requested loss-making technology-company valuation answer.

**Why:** Same EBITDA-definition template as F0835; no valuation of a loss-making technology business or path to sustainable margins.

**Replacement answer:** For a technology company with negative EBITDA, first test whether losses reflect scalable growth investment or poor underlying economics. Build a scenario DCF from customers/users, monetization, retention and gross margins through sales/R&D costs, reinvestment and cash burn to sustainable cash flow. Include funding and survival risks. EV/revenue or, for recurring software, EV/ARR can be cross-checks when adjusted for growth, retention, achievable margins and capital requirements. A forward EBITDA multiple is useful only once a credible positive denominator exists. Historical negative EV/EBITDA is not a meaningful cheapness ranking. Keep SBC and other economic costs explicit rather than assuming every non-cash expense disappears.

### F1277

**Question:** If all else equal, company A has a larger PE than company B, which one would you invest in?

**Source labels:** Nomura NY

**Original problem:** The answer explained multiple differences using unequal growth or risk, although the question holds everything else equal.

**Why:** Question holds everything else equal, but generic template justifies different prices with different growth/risk; should choose lower positive P/E B under the premise, then explain real-world qualifications.

**Replacement answer:** If everything relevant truly is equal, including positive, consistently measured earnings, future growth, cash conversion, leverage and risk, choose company B: its lower P/E means paying less per dollar of the same earnings stream and receiving a higher earnings yield. That is the answer under the stated premise. In real investing, check that equality actually holds: a low P/E can reflect peak or non-recurring earnings, weaker prospects or greater risk. A zero/negative earnings denominator makes the simple comparison unsuitable. Do not explain away the question by assuming different growth or risk after it explicitly holds those factors equal.

### F1357

**Question:** Walk me through a deal, multiple follow-up questions asking for the motivations for certain actions.

**Source labels:** PJT Partners RSSG NY

**Original problem:** The answer interpreted “multiple follow-up questions” as valuation multiples and never walked through a deal.

**Why:** Multiple follow-up questions refers to interview follow-ups, not valuation multiples. Comps template does not walk through a deal or its motivations.

**Replacement answer:** Choose an actual deal you worked on or studied and make that distinction explicit. Explain the buyer and target, their businesses, the transaction objective, price and valuation basis, consideration/funding, strategic rationale and verified status. Then explain the reasons for the important decisions: why this target or buyer, why that price and financing mix, what alternatives were considered, and which risks or synergies mattered. If discussing your own experience, state your actual contribution and respect confidentiality. Prepare follow-up support from the deal announcement, filings and your analysis. Here, "multiple follow-up questions" means several interview questions; it is not a request only for valuation multiples.

### F2019

**Question:** Why do you look at BOTH historical and projected metrics in comparable public company and precedent transaction analyses?

**Source labels:** M&I 400 Questions Guide (2025), p. 84

**Original problem:** The guide-derived answer asserted that projected metrics necessarily assume steady-state operations without acquisitions, divestitures or non-recurring items.

**Why:** Faithful guide pp84-85 says forecasts assume steady state and no acquisitions/divestitures/nonrecurring items. That is not a property of projected metrics; forecast basis and normalization must be checked.

**Replacement answer:** Historical metrics are based on reported results and provide an observable baseline, but acquisitions, divestitures, cyclicality and non-recurring items may distort comparability. Projected metrics reflect expected future performance and can better capture growth, operating changes and a path toward normalized profitability, but they depend on uncertain assumptions. A forecast does not automatically assume a steady state or exclude acquisitions, divestitures or one-time items; read what each estimate actually includes. Compare historical and forward multiples to understand the change in expected earnings, and align financial periods, transaction scope and normalization policies across companies. For precedent transactions, use forecasts available at the relevant deal date rather than later hindsight.

**Evidence:** The original wording is present in the supplied guide on printed pp. 84–85; this is a guide generalization, not a transcription error. Forecasts can explicitly contain a high-growth period before stable growth, as explained in [Damodaran’s valuation notes](https://pages.stern.nyu.edu/adamodar/New_Home_Page/valquestions/highgrowthperiod.htm). The correction requires checking what each forecast includes rather than assuming normalization.

### F2038

**Question:** Company A has a P / E multiple of 15x, with a Net Income of $120 and a TEV / EBITDA multiple of 15x. Its EBITDA is $150. Company B has the same 15x P / E multiple but a Net Income of $100, a TEV / EBITDA of 10x, and an EBITDA of $200. Which one has a higher Net Debt balance?

**Source labels:** M&I 400 Questions Guide (2025), p. 92

**Original problem:** A net-income-to-EBITDA definition replaced a fully specified net-debt calculation.

**Why:** NI-to-EBITDA template replaces a fully specified net-debt exercise. Guide p92 gives the correct result: A450 versus B500, so B by50.

**Replacement answer:** Assuming net debt is the only EV-to-equity bridge item, company A has equity value = 15*120 = 1,800 and EV = 15*150 = 2,250, so net debt = 2,250-1,800 = 450. Company B has equity value = 15*100 = 1,500 and EV = 10*200 = 2,000, so net debt = 2,000-1,500 = 500. Company B therefore has the higher net debt balance, by 50. If preferred stock, NCI or other non-operating assets are present, EV minus equity is the combined bridge amount rather than net debt alone.

**Evidence:** The supplied guide’s printed p. 92 gives A net debt of 450 and B of 500. The source JSON’s template had displaced that correct solution.

## Wording clarifications — not additional error findings

### F0513

**Question:** How would you value that (pointing out the window) office building?

**Finding:** Core NOI/cap-rate approach is correct. Wording AFFO adds recurring capital ... adjustments is ambiguous: recurring CapEx is normally deducted from FFO, not added. Clarify sign; not an explicit false formula.

**Replacement answer:** Estimate stabilized net operating income from rents/occupancy and operating expenses, excluding financing and depreciation. A simple unlevered property value is NOI/capitalization rate; reconcile it to DCF and comparable sales. Account for tenant credit, location, lease duration, vacancy, tenant improvements, leasing commissions and maintenance CapEx. Equity value subtracts debt and other claims. For REITs, FFO adjusts net income for specified real-estate depreciation and disposition items; AFFO generally deducts recurring maintenance capital expenditures from FFO and adjusts non-cash rent and other items; definitions vary by issuer. Hotels often have higher operational volatility than long-lease residential assets, but cap rates depend on quality, market and growth rather than a universal ranking.

The original phrase about adding capital “adjustments” did not unambiguously state a false formula, but it could teach the wrong sign. [Nareit’s AFFO definition](https://www.reit.com/glossary/adjusted-funds-operations-affo) deducts normalized recurring capital spending and explains that issuer definitions vary.

### F0537

**Question:** $100 in debt is issued, how does it impact your P/E and EV/EBITDA?

**Finding:** First sentence correctly keeps initial EV, EBITDA and equity unchanged. Later NI changes by expense less income reverses the signed expression; next clause correctly says earnings fall. Clarify as cash interest income minus debt interest expense, after tax; count as wording clarification, not an independent directional error.

**Replacement answer:** If the $100 debt proceeds remain as cash, EV and EBITDA are initially unchanged, so EV/EBITDA is unchanged. Equity value is also initially unchanged. Later, assuming the same usable tax rate t, the incremental net-income effect is (interest income on the new cash - interest expense on the new debt)*(1-t); P/E may rise if earnings fall and equity value stays constant. Interest rates and how cash is used are needed for a numerical P/E effect.

## Incomplete or qualified answers left unchanged (54)

These findings concern missing explanations, examples, assumptions or overgeneralized heuristics. They are not included in the 13-error count. Missing numerical inputs are not treated as an error when the conditional method is otherwise appropriate. F1015 is specifically a defensible bank answer that omits the other two company types; it is not counted as a false bank-valuation claim.

| Card | Question | Missing content or qualification |
| --- | --- | --- |
| F0039 | Value an office building in New York. Explain the relevant multiples, forecast its profit and loss, assess growth opportunities and risks, and evaluate debt leverage. [Property inputs not recorded.] | Generic corporate comps answer omits property NOI/cap rate, lease roll, growth risks and DSCR/LTV; missing case data prevents a numerical value but not the property method. |
| F0171 | If using comparable companies or precedent transactions, what relevant metrics would you look at for a negative cash flow company? | Distinguish cash burn from negative earnings: profitable EBITDA can support EV/EBITDA despite negative FCF; cash-burn cause and forward metrics are not addressed. |
| F0215 | How would you go about spreading comps for ‹given company› Stock pitch? | Stock-pitch framework covers the pitch but omits selecting peers, spreading financials and calendarized/normalized valuation multiples. |
| F0225 | Value a private company assuming there is one comparable public company. | General comps method is valid; does not address single-peer fragility, private financial adjustments and evidence-based marketability/control differences. |
| F0228 | Tell me about three apps on your phone, how would you value these companies? | Valid general valuation framework but no app examples or ad/subscription/transaction revenue economics. |
| F0232 | What multiples you would use for companies of different stages. | Mentions negative EBITDA and revenue multiples but does not compare pre-revenue, growth and mature-stage metrics explicitly. |
| F0240 | How would you value a semiconductor company over a business cycle? | Generic operating-driver template never normalizes semiconductor earnings across a cycle or distinguishes fabless/foundry capital intensity. |
| F0246 | How would you value an energy Company and what financial metrics would you use apart from the average ones. | Generic corporate methods omit upstream reserves/production, midstream throughput/contracts or energy-specific metrics. |
| F0313 | Discuss a business you follow. How would you value it, and which multiples would you use? | Pitch framework does not name a valuation method or select multiples for an example business. |
| F0318 | Give at least five reasons a company's valuation multiple could be below those of its direct competitors. | Correct growth/return/risk drivers but does not give the requested five concrete discount reasons. |
| F0367 | What kind of multiple would you use for a tech company? | Accurate general comps template but does not distinguish mature software, loss-making platforms and hardware/semiconductors. |
| F0368 | How do you value a company like Lyft, pre-IPO, using public company comparisons? | Omits pre-IPO mobility peer selection, revenue versus gross bookings and unit-economics comparability. |
| F0379 | Which of the main valuation methods is most appropriate for a public company, and why? | No universal best method, but the answer should explicitly connect public trading prices/comps and DCF to the objective. |
| F0389 | Give examples of valuation multiples, where to find their inputs and when each is useful. | Multiples are provided, but where to obtain share price, diluted shares, claims and financial inputs is omitted. |
| F0394 | If only one valuation method is available, how would you check for errors? | Lists several methods when the question allows one; no formula, unit, timing, bridge or assumption-validation procedure. |
| F0440 | What's the difference between EV/EBIT, EV/EBITDA, and EV/Revenue and what kind of companies would use each one? | Does not discuss EV/EBIT or D&A/capital-intensity implications, despite the explicit comparison. |
| F0453 | Why would you use these versus the traditional multiples such as ev/ebita. | The antecedent for these is missing; cannot justify a specific alternative to EV/EBITA. Generic template should flag this. |
| F0539 | How does a dividend impact your P/E, EV/EBITDA, and P/B ratio? | Correct dividend/EV mechanics but never derives P/E decline or conditional P/B direction, nor expressly states unchanged EV/EBITDA. |
| F0585 | How would you value a recently restructured third division in a sum-of-the-parts valuation? | SOTP framework is correct but omits normalized post-restructuring earnings, remaining cash costs and turnaround scenarios for the third division. |
| F0685 | How would you value a consumer company in Asia? | Valid general methods but omits market/currency, regulation, country exposure and consumer-demand considerations specific to the stated setting. |
| F0727 | What are the advantages and disadvantages of the main valuation methods? | Names methods and pricing bases but does not explicitly give each method's strengths and limitations. |
| F0728 | How would you value a manufacturing company? | General valuation methods are valid but manufacturing-specific capacity, maintenance CapEx, cyclicality and inventory economics are absent. |
| F0749 | How would you value a pre-revenue tech company? | Business-diligence framework does not translate pre-revenue scenarios, funding and failure risk into a valuation or discuss unusable historical multiples. |
| F0755 | How would you value a newly established mobile social-media app that allows photo and music sharing? | No app monetization, user/cohort economics, funding or scenario path to cash flow; generic corporate framework only. |
| F0825 | How do you value a company with negative earnings? | General methods do not explicitly explain why negative P/E is unhelpful or distinguish temporarily negative NI from structural losses. |
| F0829 | How would you value a company with negative revenue growth? | Diligence template does not value declining cash flows, turnaround versus runoff, or use a non-growing terminal assumption. |
| F0846 | Calculate an exit valuation multiple after changes in revenue and EBITDA margins. [Inputs incomplete in source.] | Given no numerical inputs, should state exit EV/(exit revenue*exit EBITDA margin); generic comps paragraph never produces the requested formula. |
| F0963 | Identify comparable companies for Netflix. | Date dependence is valid for current peers/prices, but no streaming/content peer candidates or comparability method is given. |
| F0964 | Choose a comparable company for Jamba Juice and explain similarities and differences. | No comparable candidate or business-model similarities/differences; current data caveat alone does not answer the qualitative comparison. |
| F0991 | If you had to find comps for a business that was very niche or specialized without very clear cut public competitors, how would you go about compiling a list together? | Standard peer-screen advice does not explain broadening to adjacent business models, segment data, economic drivers or de-emphasizing poor comps. |
| F0992 | How would you value a healthcare startup? | Drug-pipeline valuation is a valid conditional subset, but healthcare startups can instead be services, devices or software; those are not addressed. |
| F1015 | Compare valuation methods for startups, banks and large public companies. | Bank section is defensible, but startups and large public companies are entirely omitted. Partial fit, not a false bank-valuation claim. |
| F1050 | Would you use EV/EBITDA or P/E to value a biotechnology company, and why? | Pre-revenue rNPV is valid but does not explicitly compare EV/EBITDA with P/E or state when mature biotech supports either. |
| F1051 | How would you value a Healthcare Company? | Generic methods omit the key distinction among drugs, devices, providers and payers and their different unit economics. |
| F1061 | You had to apply all the concepts learned through the guides through paper DCFs, Comparable Comps analysis, and a few other calculations. | Source is an interview-description fragment, not a complete case; only comps addressed and no DCF/case inputs exist. |
| F1086 | What kinds of multiples would you expect to use in the Aerospace and Defense Industry? | Generic comps answer gives no A&D-specific metric rationale, backlog/program mix, aftermarket or pension normalization. |
| F1109 | How do you which company between two pays dividends if they have the same everything except one has a higher PE multiple. | Dividend/EV mechanics are correct but does not say lower ex-dividend P/E under fixed positive earnings or explain why P/E alone does not identify a payer. |
| F1125 | Calculate EV/EBITDA from P/E and financial information including revenue, EBITDA margin, capital structure, D&A and COGS. Identify which inputs are relevant. [Numerical inputs not recorded.] | Missing numbers prevent a numeric answer, not the bridge: EBITDA=Sales*margin, derive NI, E=P/E*NI, EV=E+net debt+other claims. The answer omits this and relevant versus redundant inputs. |
| F1230 | How would you value a company with no revenue or profit? | Diligence framework lacks probability-weighted future cash flow, funding/dilution, milestones and lack of usable historical earnings multiples. |
| F1337 | Compare EBIT and EBITDA multiples. | No comparison of EBIT versus EBITDA denominator/D&A or capital intensity; generic comps template. |
| F1450 | If l pay out a dividend, what happens to the EV/EBITDA multiple for a private company? | Correctly keeps EV unchanged but does not explicitly keep EBITDA and the multiple unchanged; expected conclusion only implied. |
| F1481 | Why could comparable companies yield higher valuation than precedent transactions? | Does not explain timing/market moves, distress or selection differences that can put public comps above precedents. |
| F1513 | How would you value two companies in the same industry with positive revenue growth when one has negative profits? | No explicit comparison between positive-earnings multiples and forward/revenue/scenario methods for the unprofitable company. |
| F1562 | Which of the three valuation methodologies would you use to value a piece of real estate? | Corporate methods template never selects property-income DCF, cap rate or comparable-property sales for the asset. |
| F1606 | Calculate enterprise value and share price from valuation multiples, revenue, margins, debt and shares outstanding. [Numerical inputs not recorded.] | Omits the requested EBITDA=Sales*margin, EV=multiple*metric, equity=EV-net debt-other claims and per-share bridge despite missing numeric inputs. |
| F1685 | Rank the three main valuation methods by reliability. | Discusses relative implied values instead of conditional reliability based on peer quality, data availability and forecastability. |
| F1786 | How much would it cost for you to start a sports team at JPM? How would you value it? | Generic operating template does not price league/equipment/venue costs or clarify recreational versus commercial team and revenue rights. |
| F1811 | How would you value a basketball team that JPM put together? | No clarification of employee recreational team versus transferable commercial franchise; generic operating template does not establish its economic rights or cash flows. |
| F1832 | What are some industry specific multiples? | Requested industry-specific examples absent; give e.g. bank P/TBV, REIT P/FFO, software EV/ARR with claimant and denominator caveats. |
| F1833 | Why do you think a subscription company shouldn't use EV/EBITDA? | Does not reject the blanket premise: mature profitable subscriptions can use EV/EBITDA; growth spending, deferred revenue and SBC/cash conversion affect usefulness. |
| F1883 | How would you value a bicycle company compared with a flower shop? | Generic unit economics never compares bicycle inventory/capacity with flowers' perishability, seasonality and spoilage. |
| F2027 | You're valuing a mid-sized manufacturing company. This company's TEV / EBITDA multiple is 15x, but the median TEV / EBITDA for the comparable companies is 10x. What's the most likely explanation? | Guide pp88-89 growth explanation is plausible, but similar industry/size alone do not ensure similar risk, reinvestment or cash conversion; treat as heuristic rather than established most-likely cause. |
| F2184 | You're comparing two sets of comparable companies: Pure-play gold miners and pure-play copper miners. How would you expect their valuation multiples to differ? Why? | Guide p170 heuristic gold/copper P/NAV ordering is not universal. High dollar metal price is not by itself a fundamental reason for a higher valuation multiple; demand/risk and NAV price-deck assumptions require evidence. Flag original guide generalization, not a measured current market fact. |
| F2250 | How would you value an unprofitable tech startup that is years away from positive Net Income and cash flow? | Guide p205 methods are possible, but no explicit survival, cash-burn/funding, dilution or user monetization checks; a long forecast or user multiple alone does not establish value. |

## Numerical and accounting verification

Existing numerical results were independently recomputed. A separate check run passed **67 numerical assertions**, plus the explicit square-door simulation and the recovery-offer comparison. These checks support the arithmetic and formulas; they do not substitute for the qualitative card-by-card review.

| Cards | Recomputed result / check |
| --- | --- |
| F0201 | 21% × 18 = 3.78; starting EV 500; one turn adds 100 versus 25 from five additional EBITDA at 5x |
| F0203, F0540, F0800 | EBITDA margins 50%, 20% in both F0540 periods, and 40% |
| F0475 | Earnings yield 1/9 = 11.111%; not a promised cash return |
| F0528, F1862 | NI 10; debt 400; EV 600; EBITDA 60; EBIT 40; EBT 20; effective tax 50%, conditional on the stated bridge |
| F0620 | Junior capacity 150 million if cash is 100 million; 50.0001 million if cash is literally 100 dollars; face amount remains indeterminate |
| F0887 | Junior recovery 400/600 = 66.67 cents; 500 exceeds recovery 400; depreciation balance-sheet identity verified at several tax rates |
| F0920 | Revenue grows 33.333% at fixed EV; margin changes from 8/12 to 6/12 while EBITDA stays constant |
| F0944 | Ten square-number doors remain open after 100 passes, assuming initially closed doors |
| F1240 | EBIT 30; NI 25.5; P/E 11.7647 if intended EV/EBIT is 10; 0.117647 under literal EBIT/EV of 10, assuming no net debt |
| F1495 | Unit EBITDA is 10 million × 10% = 1 million |
| F1705 | Pretax EPS 10; new EPS 8.50; price 105 to 127.50; increase 21.4286% |
| F1754 | Doubling both consistent EV-based multiples leaves their ratio, EBITDA margin, unchanged |
| F2016 | 100 million EBITDA × 7 = 700 million EV |
| F2038 replacement | Net debt A 450, B 500; B exceeds A by 50, assuming no other bridge items |
| F0697 / F0735 replacements | 12.5x versus 16.6667x P/E with equal 10x operating multiples; 7.5x versus 10x operating multiples with equal 15x P/E |
| F0382 replacement | Initial assets +100 = debt +100; later Δcash − d = −P − (d+I)(1−t); tested with four combinations of depreciation, interest, repayments and tax |
| F0876 replacement | Inventory 100 funded with debt; sale 150 cash; cash interest 5; PIK 10; repayment 20; 25% usable tax: NI 26.25, CFO 36.25, ending cash 116.25 = debt 90 + equity 26.25 |
| F0537 clarification | Cash interest income 2 less debt interest 5 at 25% tax gives ΔNI −2.25; matched yields give zero |
| F0678 replacement | EV/forward EBITDA identity reconciles to FCFF₁/(WACC−g), with sustainable reinvestment and WACC > g |

The F0382 and F0876 check scenarios are independent illustrations, not invented facts added to incomplete interview prompts. Cash-interest classification follows the usual US GAAP interview convention. The replacements retain symbolic answers where useful life, interest rates, repayment schedules or timing are missing. Current tax benefits require usable deductions; otherwise cash and deferred taxes must be modeled separately.

## Guide comparison

All 15 cards marked `guide_answer` in this topic were checked against the supplied PDF: F2013 (printed p. 82), F2016 (83–84), F2017–F2018 (84), F2019 (84–85), F2020–F2021 (85), F2027 (88–89), F2040 (93), F2170 (163), F2177 (166–167), F2184 (170), F2195 (175–176), F2197 (176), and F2250 (205). The guide-origin numerical question F2038 was additionally checked on p. 92 despite its current model-answer status. Page references here are printed guide pages.

F2019 warranted overriding the guide’s blanket claim. F2027’s growth explanation and F2184’s gold/copper P/NAV ranking remain qualified heuristics, flagged separately. In particular, a metal’s nominal dollar price alone does not establish a higher company valuation multiple. F2250 lists possible technology valuation methods but omits survival and financing considerations. These three guide entries remain unchanged. No assertion is made about present gold/copper market multiples.

## Shared-template scan and leads outside this topic

When repeated templates caused answer mismatches, all occurrences of those templates in the 2,049-entry source were searched and their question fit inspected. This is a limited routing scan, not a full audit of other topics; no out-of-topic answers were edited. Counts describe the pre-edit source.

| Template signature | Occurrences | Follow-up |
| --- | ---: | --- |
| Identical current statements | 10 | F0697 and F0735 corrected here; F1529 merits explicit share-count comparison |
| Choose companies with similar business | 53 | Includes a missing-inputs prefix on some entries; F1403 sources-and-uses question is a next-topic mismatch lead |
| EBITDA = net income + | 5 | F0664 and F2038 corrected here; F2088/F2089 contain numeric combined-company multiples and need an M&A review |
| EBITDA = revenue − cash operating expenses | 11 | F0835/F1137 corrected here; assess the cash-expense shorthand and question fit on remaining occurrences |
| Begin with objective, horizon | 17 | F0466 corrected here; F0054 business model, F0719 credit spread, F0973 return/variance are follow-up leads |
| Historical metrics are useful because | 1 | F2019 only; corrected |
| Estimate stabilized net operating income | 6 | F0513 clarified here; review AFFO wording on other occurrences and F0988 apartment-probability mismatch |

Other IDs for reproducibility: identical-statements F0115/F0669/F0786/F1368/F1529/F1688/F1797/F1798; NI-to-EBITDA F1686/F2088/F2089; revenue-minus-cash-expenses F0016/F0622/F0665/F0821/F1018/F1174/F1421/F1438/F1484; NOI F0310/F0493/F0988/F1354/F1355. Treat these as leads, not additional error counts or previously completed audits.

## Build and scope checks

The unmodified builder produced 3,234 cards: 2,049 technical and 1,185 behavioral. Exactly 15 source answers changed. All other source fields were preserved; all 3,219 other generated cards remained identical. The topic still contains 153 cards, with the same question IDs, wording, sources and topic assignments. Both generated formats contain the same payload.

The builder automatically derives some group/difficulty tags from answer text; consequently F0466 and F0664 have regenerated group tags and F0697 a regenerated difficulty tag. These follow directly from the existing rules, which were not changed. Verification flags and answer-status fields were not manually promoted.

Files delivered in the repository: `Technical_Questions_and_Answers.json`, `flashcards/data.json`, `flashcards/data.js`, and this report (`valuation_audit.md`). The existing untracked `AUDIT_HANDOFF.md` was left untouched. No website UI or backend change was made. The changes are intended for a local commit without a push.

## Complete review ledger (153 cards)

Each entry below records its initial classification and final action. “No issue found” is scoped to the stated assumptions and supplied answer; “incomplete” includes qualified guide heuristics. This ledger accounts for every card rather than sampling representative answers.

| Batch | Card | Initial finding | Action | Review note |
| ---: | --- | --- | --- | --- |
| 1 | F0039 | Incomplete / ambiguous | Unchanged | Generic corporate comps answer omits property NOI/cap rate, lease roll, growth risks and DSCR/LTV; missing case data prevents a numerical value but not the property method. |
| 1 | F0077 | No issue found | Unchanged | Appropriately requires a dated index level and P/E; no live quotation is asserted. Trailing/forward convention would improve it. |
| 1 | F0091 | No issue found | Unchanged | Methods and conditional selection are correct; sector-specific approaches distinguished. |
| 1 | F0103 | No issue found | Unchanged | Correctly rejects a universal ranking while explaining typical precedent/control and sponsor effects. |
| 1 | F0126 | No issue found | Unchanged | Historical peer/date constraints and no-look-ahead convention are correct; no unsupported 2012 numbers. |
| 1 | F0171 | Incomplete / ambiguous | Unchanged | Distinguish cash burn from negative earnings: profitable EBITDA can support EV/EBITDA despite negative FCF; cash-burn cause and forward metrics are not addressed. |
| 1 | F0174 | No issue found | Unchanged | Risk-adjusted pipeline cash flows, reinvestment, expiry and no double counting of clinical risk are appropriate. |
| 1 | F0175 | No issue found | Unchanged | Expiry/runoff framework is appropriate under the specified remaining patent life; no invented perpetual monopoly. |
| 1 | F0188 | No issue found | Unchanged | No deal is specified; conditional method-selection framework is defensible. |
| 1 | F0201 | No issue found | Unchanged | Recomputed 18*0.21=3.78; EV 500; one turn +100 versus EBITDA +5 at 5x adds 25; bridge signs correct. |
| 1 | F0203 | No issue found | Unchanged | Derived (EV/Sales)/(EV/EBITDA)=EBITDA/Sales; 5/10=50%. |
| 1 | F0215 | Incomplete / ambiguous | Unchanged | Stock-pitch framework covers the pitch but omits selecting peers, spreading financials and calendarized/normalized valuation multiples. |
| 1 | F0225 | Incomplete / ambiguous | Unchanged | General comps method is valid; does not address single-peer fragility, private financial adjustments and evidence-based marketability/control differences. |
| 1 | F0228 | Incomplete / ambiguous | Unchanged | Valid general valuation framework but no app examples or ad/subscription/transaction revenue economics. |
| 1 | F0232 | Incomplete / ambiguous | Unchanged | Mentions negative EBITDA and revenue multiples but does not compare pre-revenue, growth and mature-stage metrics explicitly. |
| 1 | F0240 | Incomplete / ambiguous | Unchanged | Generic operating-driver template never normalizes semiconductor earnings across a cycle or distinguishes fabless/foundry capital intensity. |
| 1 | F0246 | Incomplete / ambiguous | Unchanged | Generic corporate methods omit upstream reserves/production, midstream throughput/contracts or energy-specific metrics. |
| 1 | F0291 | No issue found | Unchanged | Provides consistent EV/revenue, EV/EBITDA and P/E examples and denominator limitations. |
| 1 | F0301 | No issue found | Unchanged | Peer selection, calendarization, normalization and applying a multiple range are correctly described. |
| 1 | F0313 | Incomplete / ambiguous | Unchanged | Pitch framework does not name a valuation method or select multiples for an example business. |
| 2 | F0318 | Incomplete / ambiguous | Unchanged | Correct growth/return/risk drivers but does not give the requested five concrete discount reasons. |
| 2 | F0343 | No issue found | Unchanged | Company and meaning of too large are absent; conditional method framework appropriately avoids a fabricated case answer. |
| 2 | F0367 | Incomplete / ambiguous | Unchanged | Accurate general comps template but does not distinguish mature software, loss-making platforms and hardware/semiconductors. |
| 2 | F0368 | Incomplete / ambiguous | Unchanged | Omits pre-IPO mobility peer selection, revenue versus gross bookings and unit-economics comparability. |
| 2 | F0378 | No issue found | Unchanged | Both requested multiples defined; no company financial inputs supplied to recompute. |
| 2 | F0379 | Incomplete / ambiguous | Unchanged | No universal best method, but the answer should explicitly connect public trading prices/comps and DCF to the objective. |
| 2 | F0382 | Incorrect answer | Corrected | Valuation-comps template is unrelated to a $200 equipment three-statement case; initial PP&E/cash/debt effects are determinable. |
| 2 | F0389 | Incomplete / ambiguous | Unchanged | Multiples are provided, but where to obtain share price, diluted shares, claims and financial inputs is omitted. |
| 2 | F0394 | Incomplete / ambiguous | Unchanged | Lists several methods when the question allows one; no formula, unit, timing, bridge or assumption-validation procedure. |
| 2 | F0434 | No issue found | Unchanged | Relevant peer/earnings principles apply; a differentiated product alone does not dictate a unique multiple. |
| 2 | F0440 | Incomplete / ambiguous | Unchanged | Does not discuss EV/EBIT or D&A/capital-intensity implications, despite the explicit comparison. |
| 2 | F0442 | No issue found | Unchanged | Gives negative EBITDA as a reason its multiple is unhelpful; broad question permits this example. |
| 2 | F0447 | No issue found | Unchanged | SOTP aggregation, central costs, consolidated bridge and example are appropriate. |
| 2 | F0453 | Incomplete / ambiguous | Unchanged | The antecedent for these is missing; cannot justify a specific alternative to EV/EBITA. Generic template should flag this. |
| 2 | F0466 | Incorrect answer | Corrected | Portfolio-allocation template answers what to own, not how to value different asset classes; none of the requested valuation methods given. |
| 2 | F0475 | No issue found | Unchanged | 1/9=11.111%; distinguishes earnings yield from cash return and price from value. |
| 2 | F0478 | No issue found | Unchanged | Identical present income statements need not imply equal future growth, risk, cash conversion or capital needs; answer's comparison factors support this. |
| 2 | F0481 | No issue found | Unchanged | Mature software EV measures and separate excess cash treatment are appropriate; SBC and recurring cash conversion considered. |
| 2 | F0513 | Incomplete / ambiguous | Clarified | Core NOI/cap-rate approach is correct. Wording AFFO adds recurring capital ... adjustments is ambiguous: recurring CapEx is normally deducted from FFO, not added. Clarify sign; not an explicit false formula. |
| 2 | F0528 | No issue found | Unchanged | Recomputed NI10, debt400, EV600, EBITDA60, EBIT40, EBT20, tax10 and 50%, under disclosed no-cash assumption. |
| 3 | F0529 | No issue found | Unchanged | Correctly pairs EV with pre-interest EBITDA and common equity with NI; explains tax/financing differences. |
| 3 | F0537 | Incomplete / ambiguous | Clarified | First sentence correctly keeps initial EV, EBITDA and equity unchanged. Later NI changes by expense less income reverses the signed expression; next clause correctly says earnings fall. Clarify as cash interest income minus debt interest expense, after tax; count as wording clarification, not an independent directional error. |
| 3 | F0539 | Incomplete / ambiguous | Unchanged | Correct dividend/EV mechanics but never derives P/E decline or conditional P/B direction, nor expressly states unchanged EV/EBITDA. |
| 3 | F0540 | No issue found | Unchanged | Recomputed 2/10=4/20=20%; cannot infer whether numerator or denominator moved. |
| 3 | F0546 | No issue found | Unchanged | Conditional pre-revenue pipeline approach is appropriate; risks and expiry addressed. |
| 3 | F0548 | No issue found | Unchanged | rNPV plus carefully limited comparable revenue checks is defensible; no invalid negative-earnings multiple proposed. |
| 3 | F0573 | No issue found | Unchanged | Correctly rejects mechanical cheapness ranking of 5x and 10x and tests risk/cash conversion. |
| 3 | F0574 | No issue found | Unchanged | Accurately distinguishes US operating-lease EBITDA from depreciation and requires consistent lease EV treatment. |
| 3 | F0581 | No issue found | Unchanged | SOTP uses division-specific economics and net-debt bridge; neither growth pattern alone fixes value. |
| 3 | F0585 | Incomplete / ambiguous | Unchanged | SOTP framework is correct but omits normalized post-restructuring earnings, remaining cash costs and turnaround scenarios for the third division. |
| 3 | F0593 | No issue found | Unchanged | Operating-unit forecast, costs, cash flows and peer cross-check suit an unspecified local business. |
| 3 | F0620 | No issue found | Unchanged | Recomputed EV300 plus cash100 less senior250=150 residual; literal $100 alternative and inability to infer junior face amount correctly flagged. |
| 3 | F0629 | No issue found | Unchanged | Inputs absent; conditional valuation framework is appropriate. |
| 3 | F0645 | No issue found | Unchanged | Correct identity links revenue multiple, EBITDA multiple and margin; negative-profit caveat included. |
| 3 | F0664 | Incorrect answer | Corrected | NI-to-EBITDA definition template never values a negative-NI/negative-EBITDA business or handles unusable negative earnings multiples. |
| 3 | F0678 | Incorrect answer | Corrected | Answer explicitly proposes comparable-company multiples despite the question forbidding that input; use fundamentals/implied multiples instead. |
| 3 | F0685 | Incomplete / ambiguous | Unchanged | Valid general methods but omits market/currency, regulation, country exposure and consumer-demand considerations specific to the stated setting. |
| 3 | F0697 | Incorrect answer | Corrected | Identical-company template omits the mechanical EV/EBITDA-to-P/E bridge; equal operating multiples do not mean identical financial statements. |
| 3 | F0720 | No issue found | Unchanged | Correctly values manager-owned fee/carry economics rather than client AUM; specific fund-manager inputs are absent. |
| 3 | F0727 | Incomplete / ambiguous | Unchanged | Names methods and pricing bases but does not explicitly give each method's strengths and limitations. |
| 4 | F0728 | Incomplete / ambiguous | Unchanged | General valuation methods are valid but manufacturing-specific capacity, maintenance CapEx, cyclicality and inventory economics are absent. |
| 4 | F0729 | No issue found | Unchanged | Growth, margins, returns, capital intensity and risk correctly explain cross-industry multiple differences. |
| 4 | F0735 | Incorrect answer | Corrected | Equal P/E is not identical financial statements; answer omits mechanical bridge through NI/EBITDA and net debt/other claims. |
| 4 | F0736 | No issue found | Unchanged | Correctly avoids automatic choice of 8x over 10x; identifies fundamental reasons for differing valuation. |
| 4 | F0746 | No issue found | Unchanged | P/E correctly defined as equity value/NI with relative-pricing context, though more concise answer would help. |
| 4 | F0749 | Incomplete / ambiguous | Unchanged | Business-diligence framework does not translate pre-revenue scenarios, funding and failure risk into a valuation or discuss unusable historical multiples. |
| 4 | F0754 | No issue found | Unchanged | Appropriate framework for explaining selected peers, periods and business-risk differences in an unspecified actual deal. |
| 4 | F0755 | Incomplete / ambiguous | Unchanged | No app monetization, user/cohort economics, funding or scenario path to cash flow; generic corporate framework only. |
| 4 | F0800 | No issue found | Unchanged | 2/5=40%; consistent EV and period assumed. |
| 4 | F0824 | No issue found | Unchanged | Requested multiples and relevant profit/negative-EBITDA limitations covered; no EBIT comparison asked here. |
| 4 | F0825 | Incomplete / ambiguous | Unchanged | General methods do not explicitly explain why negative P/E is unhelpful or distinguish temporarily negative NI from structural losses. |
| 4 | F0829 | Incomplete / ambiguous | Unchanged | Diligence template does not value declining cash flows, turnaround versus runoff, or use a non-growing terminal assumption. |
| 4 | F0835 | Incorrect answer | Corrected | EBITDA-definition template does not answer negative-EBITDA valuation. Its cash-operating-expenses shorthand also misses non-D&A noncash costs in unadjusted EBITDA. |
| 4 | F0846 | Incomplete / ambiguous | Unchanged | Given no numerical inputs, should state exit EV/(exit revenue*exit EBITDA margin); generic comps paragraph never produces the requested formula. |
| 4 | F0851 | No issue found | Unchanged | Correctly explains revenue multiples can help with negative EBITDA only with a credible margin path; high expenses alone do not guarantee low value. |
| 4 | F0876 | Incorrect answer | Corrected | Comps template unrelated to inventory, PIK, interest and amortization accounting, even though missing inputs justify only a symbolic solution. |
| 4 | F0887 | No issue found | Unchanged | Recomputed EV700, senior300, junior400/600=66.6667c; offer500 exceeds400 under stated assumptions. Depreciation balance: cash+10t, PPE-10, RE-10(1-t). |
| 4 | F0920 | No issue found | Unchanged | Constant EV: revenue grows (8/6)-1=33.3333%; EBITDA unchanged; margins 8/12 to6/12. |
| 4 | F0944 | No issue found | Unchanged | Under stated initial-closed/toggling assumptions, only ten square-number doors have odd divisor counts. Topic misclassification is outside answer-accuracy scope. |
| 4 | F0963 | Incomplete / ambiguous | Unchanged | Date dependence is valid for current peers/prices, but no streaming/content peer candidates or comparability method is given. |
| 5 | F0964 | Incomplete / ambiguous | Unchanged | No comparable candidate or business-model similarities/differences; current data caveat alone does not answer the qualitative comparison. |
| 5 | F0991 | Incomplete / ambiguous | Unchanged | Standard peer-screen advice does not explain broadening to adjacent business models, segment data, economic drivers or de-emphasizing poor comps. |
| 5 | F0992 | Incomplete / ambiguous | Unchanged | Drug-pipeline valuation is a valid conditional subset, but healthcare startups can instead be services, devices or software; those are not addressed. |
| 5 | F0999 | No issue found | Unchanged | Relevant selection framework; candidate must supply their real case-comp peers/deals rather than an invented history. |
| 5 | F1009 | No issue found | Unchanged | Hospital cash-flow drivers and real-estate/nonprofit distinctions are appropriate. |
| 5 | F1015 | Incomplete / ambiguous | Unchanged | Bank section is defensible, but startups and large public companies are entirely omitted. Partial fit, not a false bank-valuation claim. |
| 5 | F1016 | No issue found | Unchanged | Current numerator versus LTM/forward denominator and transaction-date convention are correctly distinguished. |
| 5 | F1050 | Incomplete / ambiguous | Unchanged | Pre-revenue rNPV is valid but does not explicitly compare EV/EBITDA with P/E or state when mature biotech supports either. |
| 5 | F1051 | Incomplete / ambiguous | Unchanged | Generic methods omit the key distinction among drugs, devices, providers and payers and their different unit economics. |
| 5 | F1061 | Incomplete / ambiguous | Unchanged | Source is an interview-description fragment, not a complete case; only comps addressed and no DCF/case inputs exist. |
| 5 | F1079 | No issue found | Unchanged | With positive EV and EBIT, EBITDA>=EBIT implies EV/EBITDA<=EV/EBIT; zero/negative denominator caveats included. |
| 5 | F1086 | Incomplete / ambiguous | Unchanged | Generic comps answer gives no A&D-specific metric rationale, backlog/program mix, aftermarket or pension normalization. |
| 5 | F1108 | No issue found | Unchanged | Football-field ranges, common valuation basis and interpretation correctly described. |
| 5 | F1109 | Incomplete / ambiguous | Unchanged | Dividend/EV mechanics are correct but does not say lower ex-dividend P/E under fixed positive earnings or explain why P/E alone does not identify a payer. |
| 5 | F1112 | No issue found | Unchanged | Supplies more than three methods and appropriately rejects a universal ranking. |
| 5 | F1119 | No issue found | Unchanged | Private-company financial reliability and comparable/intrinsic range framework are appropriate; actual internship facts must come from candidate. |
| 5 | F1120 | No issue found | Unchanged | Rent/NOI/DCF framework correctly conditions on transferable property rights rather than equating a student's use right with ownership. |
| 5 | F1125 | Incomplete / ambiguous | Unchanged | Missing numbers prevent a numeric answer, not the bridge: EBITDA=Sales*margin, derive NI, E=P/E*NI, EV=E+net debt+other claims. The answer omits this and relevant versus redundant inputs. |
| 5 | F1137 | Incorrect answer | Corrected | Same EBITDA-definition template as F0835; no valuation of a loss-making technology business or path to sustainable margins. |
| 5 | F1230 | Incomplete / ambiguous | Unchanged | Diligence framework lacks probability-weighted future cash flow, funding/dilution, milestones and lack of usable historical earnings multiples. |
| 6 | F1239 | No issue found | Unchanged | Valid methodology framework; candidate must supply their actual e-commerce deal and chosen valuation rather than invented experience. |
| 6 | F1240 | No issue found | Unchanged | Recomputed EBIT30, NI25.5; EV/EBIT10 gives EV300 and P/E11.7647, literal EBIT/EV10 gives EV3 and P/E0.117647. Explicit net-debt assumption and irrelevant D&A identified. |
| 6 | F1277 | Incorrect answer | Corrected | Question holds everything else equal, but generic template justifies different prices with different growth/risk; should choose lower positive P/E B under the premise, then explain real-world qualifications. |
| 6 | F1337 | Incomplete / ambiguous | Unchanged | No comparison of EBIT versus EBITDA denominator/D&A or capital intensity; generic comps template. |
| 6 | F1357 | Incorrect answer | Corrected | Multiple follow-up questions refers to interview follow-ups, not valuation multiples. Comps template does not walk through a deal or its motivations. |
| 6 | F1414 | No issue found | Unchanged | SaaS-specific conditional framework links recurring economics to DCF and suitable EV metrics; Rule of 40 properly described as heuristic. |
| 6 | F1427 | No issue found | Unchanged | Consistent claimant/denominator examples and loss-making limitation cover the broad method-selection question. |
| 6 | F1450 | Incomplete / ambiguous | Unchanged | Correctly keeps EV unchanged but does not explicitly keep EBITDA and the multiple unchanged; expected conclusion only implied. |
| 6 | F1457 | No issue found | Unchanged | Appropriately an open-ended pitch framework requiring actual company inputs; no fabricated portfolio holding or valuation. |
| 6 | F1467 | No issue found | Unchanged | Correct P/E definition plus growth, risk and financing explanations for changes; no deterministic direction misstated. |
| 6 | F1474 | No issue found | Unchanged | Slower growth alone not a short; conditional expectation/catalyst framework appropriate and explicitly dated research needed. |
| 6 | F1476 | No issue found | Unchanged | DCF and revenue/ARR with retention, margins and unit economics address loss-making B2B SaaS; profitable-only EBITDA condition correct. |
| 6 | F1481 | Incomplete / ambiguous | Unchanged | Does not explain timing/market moves, distress or selection differences that can put public comps above precedents. |
| 6 | F1495 | No issue found | Unchanged | Unit EBITDA10*10%=1m, not3m; standalone incremental value, shared costs and after-tax separation alternative are correct. |
| 6 | F1513 | Incomplete / ambiguous | Unchanged | No explicit comparison between positive-earnings multiples and forward/revenue/scenario methods for the unprofitable company. |
| 6 | F1517 | No issue found | Unchanged | No companies identified; general EV/revenue, EV/EBITDA and P/E examples appropriately conditional. |
| 6 | F1562 | Incomplete / ambiguous | Unchanged | Corporate methods template never selects property-income DCF, cap rate or comparable-property sales for the asset. |
| 6 | F1575 | No issue found | Unchanged | Growth, risk, returns, earnings basis and financing are defensible P/E drivers. |
| 6 | F1593 | No issue found | Unchanged | Missing company figures preclude a numerical result; peer selection, normalization and applying range are correct. |
| 6 | F1594 | No issue found | Unchanged | No actual values retained; general comps procedure is valid and makes no invented calculation. |
| 7 | F1598 | No issue found | Unchanged | Case inputs absent; applying consistent precedent multiples to matching financial metrics is a valid conditional approach, although deal timing/terms could be more explicit. |
| 7 | F1599 | No issue found | Unchanged | Missing private-company inputs correctly acknowledged; comps method and period normalization are appropriate. |
| 7 | F1603 | No issue found | Unchanged | No values available for mental arithmetic; method and multiple identity are valid. |
| 7 | F1604 | No issue found | Unchanged | Peer selection uses operating model, geography, growth, margins, capital intensity and risk rather than sector labels alone. |
| 7 | F1606 | Incomplete / ambiguous | Unchanged | Omits the requested EBITDA=Sales*margin, EV=multiple*metric, equity=EV-net debt-other claims and per-share bridge despite missing numeric inputs. |
| 7 | F1685 | Incomplete / ambiguous | Unchanged | Discusses relative implied values instead of conditional reliability based on peer quality, data availability and forecastability. |
| 7 | F1705 | No issue found | Unchanged | Pretax EPS10, new EPS8.5, price105 to127.5, increase22.5/105=21.4286%; assumptions explicit. |
| 7 | F1754 | No issue found | Unchanged | Derived unchanged EBITDA margin when both consistent EV ratios double. |
| 7 | F1772 | No issue found | Unchanged | Unit-based revenue, variable/fixed costs, cash flow and local risk framework is defensible for an unspecified local laundromat; could add machine cycles/utilities. |
| 7 | F1786 | Incomplete / ambiguous | Unchanged | Generic operating template does not price league/equipment/venue costs or clarify recreational versus commercial team and revenue rights. |
| 7 | F1795 | No issue found | Unchanged | Food-outlet volume/ticket/days, reinvestment, concentration and cash flow support a food-truck comparison. |
| 7 | F1811 | Incomplete / ambiguous | Unchanged | No clarification of employee recreational team versus transferable commercial franchise; generic operating template does not establish its economic rights or cash flows. |
| 7 | F1832 | Incomplete / ambiguous | Unchanged | Requested industry-specific examples absent; give e.g. bank P/TBV, REIT P/FFO, software EV/ARR with claimant and denominator caveats. |
| 7 | F1833 | Incomplete / ambiguous | Unchanged | Does not reject the blanket premise: mature profitable subscriptions can use EV/EBITDA; growth spending, deferred revenue and SBC/cash conversion affect usefulness. |
| 7 | F1838 | No issue found | Unchanged | Negative EBITDA is a valid example of unsuitability; not an exhaustive list, but broad question does not require one. |
| 7 | F1862 | No issue found | Unchanged | Recomputed NI10, debt400, EV600, EBITDA60, EBIT40, EBT20, tax10; 50% under simplified bridge. |
| 7 | F1883 | Incomplete / ambiguous | Unchanged | Generic unit economics never compares bicycle inventory/capacity with flowers' perishability, seasonality and spoilage. |
| 7 | F2013 | No issue found | Unchanged | Original guide p82 confirmed; method tradeoffs defensible, with most correct understood as theory-based rather than guaranteed accuracy. Prior opening restoration is present. |
| 7 | F2016 | No issue found | Unchanged | Guide pp83-84 confirmed; 100m EBITDA*7=700m EV; peer/deal selection, percentiles and matched periods correct. |
| 7 | F2017 | No issue found | Unchanged | Guide p84 screens are illustrative and correctly vary size, geography and historical deal window; no actual market facts asserted. |
| 8 | F2018 | No issue found | Unchanged | Guide p84 financial metric and claimant pairing is correct; selection depends on earnings/cash flow relevance. |
| 8 | F2019 | Incorrect answer | Corrected | Faithful guide pp84-85 says forecasts assume steady state and no acquisitions/divestitures/nonrecurring items. That is not a property of projected metrics; forecast basis and normalization must be checked. |
| 8 | F2020 | No issue found | Unchanged | Guide p85 standard forward-comps convention is current valuation numerator over forecast denominator; not a prohibition on terminal valuation in other contexts. |
| 8 | F2021 | No issue found | Unchanged | Guide p85 uses could indicate mispricing, not an automatic undervaluation claim; matching growth/margins is illustrative and other risk/return differences still matter. |
| 8 | F2027 | Incomplete / ambiguous | Unchanged | Guide pp88-89 growth explanation is plausible, but similar industry/size alone do not ensure similar risk, reinvestment or cash conversion; treat as heuristic rather than established most-likely cause. |
| 8 | F2038 | Incorrect answer | Corrected | NI-to-EBITDA template replaces a fully specified net-debt exercise. Guide p92 gives the correct result: A450 versus B500, so B by50. |
| 8 | F2040 | No issue found | Unchanged | Guide p93: include lease claims and remove US operating-rent earnings effect for lease-adjusted EV/EBITDAR; consistent broad interview convention, not complete comparability of every business/lease term. |
| 8 | F2170 | No issue found | Unchanged | Guide p163 identifies explicitly forecast peak/L+5 revenue multiples, with clinical-stage/forecast-reliability qualifications; not a current-revenue multiple for a zero-revenue drug. |
| 8 | F2177 | No issue found | Unchanged | Guide pp166-167 SOTP fit follows heterogeneous segments/assets versus a homogeneous pure play; examples conditional. |
| 8 | F2184 | Incomplete / ambiguous | Unchanged | Guide p170 heuristic gold/copper P/NAV ordering is not universal. High dollar metal price is not by itself a fundamental reason for a higher valuation multiple; demand/risk and NAV price-deck assumptions require evidence. Flag original guide generalization, not a measured current market fact. |
| 8 | F2195 | No issue found | Unchanged | Guide pp175-176 throughput/utilization/fees, maintenance/growth CapEx, enterprise versus equity distribution metrics are defensible; MLP-specific DDM is conditional. |
| 8 | F2197 | No issue found | Unchanged | Guide p176 refinery capacity/utilization/margins with normal DCF/multiples is correct; cyclical normalization would be a useful elaboration. |
| 8 | F2250 | Incomplete / ambiguous | Unchanged | Guide p205 methods are possible, but no explicit survival, cash-burn/funding, dilution or user monetization checks; a long forecast or user multiple alone does not establish value. |
