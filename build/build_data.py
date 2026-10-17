#!/usr/bin/env python3
"""Build flashcard data.json from the question bank files in the parent folder.

Inputs (parent directory):
  - Technical_Questions_and_Answers.json   (2,049 technical Q&A with firm sources)
  - IB_Behavioral_Questions.txt       (behavioral question list with sources)

Output:
  - data.json  consumed by index.html

Firm / group / topic / difficulty tags on each card are DERIVED here by rule,
not supplied by the source files. Re-run after editing the rules below.
"""

import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))     # build/
ROOT = os.path.dirname(HERE)                          # the repository
SRC = os.path.join(ROOT, "data")                      # the question bank
SITE = os.path.join(ROOT, "flashcards")               # what gets served
TECH_JSON = os.path.join(SRC, "Technical_Questions_and_Answers.json")
BEHAV_TXT = os.path.join(SRC, "IB_Behavioral_Questions.txt")
OUT = os.path.join(SITE, "data.json")

# ---------------------------------------------------------------- firms ----

FIRMS = [
    "Adams Street", "Advent International", "Aeris Partners", "Alpine Investors",
    "Apollo Global Management", "Ardian", "Ares Management", "Audax Group",
    "BMO Capital Markets", "BNP Paribas", "Bain Capital", "Balyasny Asset Management",
    "Bank of America", "Barclays", "BlackRock", "Blackstone", "Cain Brothers",
    "Canaccord Genuity", "Centerview Partners", "Citadel", "Citizens Bank", "Citi",
    "D.E. Shaw", "DC Advisory", "Deloitte Corporate Finance", "Deutsche Bank",
    "Dodge & Cox", "Ducera Partners", "Eastdil Secured", "Ernst & Young", "Evercore",
    "Financial Technology Partners", "GCM Grosvenor", "GTCR", "General Atlantic",
    "Goldman Sachs", "Greenhill", "Guggenheim Partners", "Houlihan Lokey",
    "ICONIQ Capital", "Insight Partners", "Intrepid", "J.P. Morgan", "Jane Street",
    "Jefferies", "KKR", "KeyBanc", "Lazard", "Leerink Partners", "LionTree", "MUFG",
    "Macquarie Group", "Miller Buckfire", "Moelis & Co.", "Morgan Stanley", "Nomura",
    "Oak Hill", "PIMCO", "PJT Partners", "PNC Capital Markets",
    "Perella Weinberg Partners", "Piper Sandler", "Point72",
    "Prudential Global Investment Management", "RBC Capital Markets", "Raine Group",
    "Raymond James", "Rothschild & Co.", "Shea & Co", "Sixth Street",
    "Société Générale", "Stephens", "Summit Partners", "TD Securities", "Tesla",
    "The Sage Group", "UBS", "Union Square Advisors", "Vista Equity Partners",
    "Warburg Pincus", "Weiss Asset Management", "Wells Fargo", "William Blair",
    # firms that appear only in the USF interview workbooks
    "Accenture", "Alliance Bernstein", "Amgen", "BNY Mellon", "Crosstree", "Delta Air Lines",
    "Diamond Hill Capital", "Dubin Clark", "FTI Consulting", "Fidelity", "First Citizens Bank",
    "Freddie Mac", "Huron Consulting", "Mariner Wealth Management", "PEI Global", "PGIM",
    "Walmart",
]
FIRMS_BY_LEN = sorted(FIRMS, key=len, reverse=True)

GUIDE_SOURCE = "M&I 400 Questions Guide"


def parent_firm(source):
    """Map 'Goldman Sachs TMT SF' -> 'Goldman Sachs'. None for the guide."""
    s = source.strip()
    if s.startswith(GUIDE_SOURCE):
        return None
    for f in FIRMS_BY_LEN:
        if s == f or s.startswith(f + " ") or s.startswith(f + " ("):
            return f
    return s


# -------------------------------------------------- groups / industries ----
# Matched against the raw source label first, then against question text.

GROUP_BY_LABEL = [
    ("Restructuring", ("restructuring", "rssg", "ducera", "miller buckfire", "pfa")),
    ("Healthcare", ("healthcare", "leerink", "cain brothers")),
    ("Technology & Media", ("technology", "tmt", "financial technology partners",
                            "union square advisors", "shea & co", "liontree",
                            "raine group", "aeris partners", "insight partners",
                            "vista equity", "iconiq", "canaccord genuity ny technology")),
    ("Industrials", ("industrials",)),
    ("FIG", ("fig", "raymond james fig")),
    ("Real Estate", ("real estate", "eastdil")),
    ("Credit & Leveraged Finance", ("credit", "direct lending", "leveraged finance",
                                    "fixed income", "financing", "debt advisory",
                                    "sixth street", "ares management", "bain capital credit")),
    ("Markets & Trading", ("global markets", "equities", "citadel", "jane street",
                           "balyasny", "point72", "d.e. shaw", "weiss asset management")),
    ("Asset & Wealth Management", ("asset management", "wealth management", "blackrock",
                                   "pimco", "dodge & cox", "prudential global",
                                   "investment management", "private wealth",
                                   "gcm grosvenor", "adams street", "strategic partners",
                                   "secondaries", "park hill")),
    ("Equity Capital Markets", ("ecm", "capital markets & debt", "public finance")),
    ("Private Equity & Growth", ("private equity", "advent international", "alpine investors",
                                 "apollo global management", "ardian", "audax group",
                                 "bain capital", "blackstone", "gtcr", "general atlantic",
                                 "kkr", "oak hill", "summit partners", "warburg pincus")),
    ("Research", ("research",)),
]

GROUP_BY_TEXT = [
    ("Healthcare", r"\b(biotech|pharma|drug|clinical|fda|medical device|payer|provider|hospital)\b"),
    ("Technology & Media", r"\b(saas|arr|software|subscription|churn|streaming|semiconductor|cloud|internet)\b"),
    ("Real Estate", r"\b(reit|cap rate|noi|real estate|property)\b"),
    ("Restructuring", r"\b(chapter 11|distressed|bankrupt|dip |restructur|liquidation|waterfall|covenant breach)\b"),
    ("Energy & Power", r"\b(oil|gas|upstream|midstream|refin(er|ing)|renewable|solar|utility|power plant)\b"),
    ("Consumer & Retail", r"\b(retail|consumer|restaurant|grocery|apparel|same-store)\b"),
    ("FIG", r"\b(bank's|net interest margin|tangible book value|insurance|deposits|loan loss)\b"),
]

GENERALIST = "M&A / Generalist"

# ------------------------------------------------------------- topics -----
# First rule that matches wins, so order is deliberate.

TECH_TOPIC_RULES = [
    ("Accretion / Dilution", r"accretiv|dilutiv|accretion|dilution|eps impact|pro forma eps"),
    ("Merger Model & M&A", r"merger model|purchase accounting|goodwill|synerg|acquir|acquisition|takeover|hostile|tender offer|earnout|\bm&a\b|sell-?side|buy-?side|due diligence|deal process|stock vs\.? cash|cvr\b|breakup fee|fairness opinion|asset (sale|deal)|stock (sale|deal)|338"),
    ("LBO & Private Equity", r"\blbo\b|leveraged buyout|sponsor|\birr\b|\bmoic\b|dividend recap|management rollover|paydown|exit multiple|sources and uses|cash sweep|private equity"),
    ("Options & Derivatives", r"black-?scholes|option (pric|value|premium)|price an option|call option|put option|strike price|futures contract|swap\b|derivative|volatility surface|delta hedg|implied vol"),
    ("DCF & Intrinsic Value", r"\bdcf\b|discounted cash flow|terminal value|gordon growth|\bwacc\b|cost of equity|cost of capital|capm|unlevered free cash flow|levered free cash flow|\bfcff\b|\bfcfe\b|mid-?year|perpetuity|discount rate|lever(ed|ing) beta|unlever|\bbeta\b|risk-?free rate|equity risk premium|\bddm\b|dividend discount|revenue to ufcf"),
    ("Valuation & Comps", r"comparable compan|trading comps|precedent transaction|\bcomps\b|valuation method|football field|sum of the parts|sotp|control premium|liquidity discount|which (valuation|method)|ev/ebitda|p/?e multiple|multiple(s)? (of|expansion)|how would you value|value a (company|business)"),
    ("Enterprise & Equity Value", r"enterprise value|equity value|ev bridge|market cap|noncontrolling|minority interest|net debt|treasury stock method|fully diluted|convertible (bond|note)|options? (outstanding|exercis)"),
    ("Accounting & 3 Statements", r"three statements|income statement|balance sheet|cash flow statement|cash flow from|depreciation|amortization|deferred (tax|revenue)|\bdta\b|\bdtl\b|working capital|accounts (receivable|payable)|inventory|accrual|revenue recognition|write-?(down|off)|capitaliz|lease|stock-based compensation|net income|ebitda|ebit\b|gaap|ifrs|link the (three|3)|balance(s)? out|goodwill impairment|book value|prepaid|deferred"),
    ("Debt, Credit & Restructuring", r"\bdebt\b|bond|credit|leverage ratio|coverage ratio|covenant|interest expense|\bpik\b|tranche|senior|mezzanine|revolver|securitiz|default|recovery|duration|yield|bankrupt|chapter 11|distressed|waterfall|refinanc|capital structure|rating"),
    ("Markets & Economy", r"interest rate|interest-rate|fed\b|federal reserve|inflation|yield curve|macro|recession|gdp|tariff|currency|fx\b|commodity|market outlook|s&p 500|bond market|monetary|fiscal|unemployment|financial crisis|the economy|economic|stock market|global markets|market event|geopolit"),
    ("Stock Pitch & Investing", r"stock pitch|pitch me|pitch a|would you pitch|invest in|where would you invest|allocate .{0,20}(\$|million|capital)|would you (buy|short)|long or short|portfolio|thesis|catalyst|undervalued|overvalued|hedge fund|etf\b|asset allocation|investment horizon|stock (pick|you)"),
    ("Industry & Company Analysis", r"industry|sector|competitive|moat|business model|unit economics|market size|trend|how does .* make money|what drives"),
    ("FIG & Specialty Valuation", r"regulatory capital|commercial bank|insurance (company|firm)|specialty finance|net interest margin|tangible book|loan loss|basel|bank's balance sheet|value a bank"),
    ("Deal & Process", r"pitch book|cim\b|\bteasers?\b|nda\b|data room|lbo model|build a model|model(ing)? (a|the)|process|timeline|roadshow|ipo\b|follow-?on|bookbuild"),
    ("Quant & Brainteasers", r"how many|estimate the|probability|dice|coin|expected value|mental math|percent of|what is \d|\d+ ?% of"),
]

BEHAV_TOPIC_RULES = [
    ("Why Banking / Why Firm", r"^why\b|why (do|did|are|would|should) you|\bwhy (this|our|us\b|not |a |an |the )|interested in (banking|finance|this|our|the (role|group|firm|industry|sector)|energy|healthcare|tech|software|renewables)|how did you (get interested|find out|hear about)|what (attracts|interests) you|why (not )?(consult|pe|private equity|trading|accounting)|what do you know about (us|our|the firm)|why should we hire"),
    ("Resume & Experience Walkthrough", r"walk me through your (resume|cv|background)|tell me about yourself|your (internship|experience|background)|describe your responsibilit|typical work day|what did you (do|learn)"),
    ("Leadership & Teamwork", r"leader|team|collaborat|mentor|manage(d|ment of)? (a|people|others)|influence|persuade|delegate|conflict with a (team|colleague)"),
    ("Conflict, Failure & Pressure", r"fail|mistake|conflict|disagree|difficult|criticism|stress|pressure|tight (deadline|timeline|project)|setback|weakness|challenge|workload|burnout|long hours|prioriti|multitask|juggl|ethical|integrity|handle the|under pressure"),
    ("Strengths, Goals & Self-Assessment", r"strength|weakness|greatest|proud|five years|long-?term goal|career|describe yourself|three words|what motivates|biggest critic"),
    ("Markets & Deal Interest", r"deal (you|that)|recent (deal|transaction|ipo|merger)|follow the market|stock you|company you (like|admire)|news|current event"),
    ("Brainteasers & Estimation", r"how many|estimate|probability|coin|dice|guess|weigh|golf balls|puzzle|mental math|calculate|mentally|square root|next number|sequence|multiplied by|divided by|what(?:'s| is) \d|\d+ ?x ?\d|doubles? (in size )?every|\^\d|% of \d|percent of \d"),
    ("Personality & Interests", r"hobb|outside (of )?(work|the office|academics)|favou?rite (book|website|movie|app|class|stock|place)|if you were an? |read (recently|lately)|book you|fun fact|remember you|describe yourself in|three words|what do you do for|passion|sport|music|travel"),
    ("Technical Skills & Tools", r"\bexcel\b|bloomberg|shortcut|capiq|capital iq|factset|powerpoint|\bvba\b|how comfortable are you (with|at)|modell?ing (skill|experience|comfort)|what (software|tools)"),
    ("Behavioral Stories (STAR)", r"tell me about a time|tell us about a time|describe a (time|situation|experience|project)|give (me |us )?an example|an experience where|name (that|a) \d? ?time|a time (when|where|you)|walk me through a situation"),
    ("Logistics & Recruiting", r"other (firms|offers)|recruiting|interview process|relocat|start date|visa|gpa|grades|questions for me|anything else"),
]

ADV_PAT = re.compile(
    r"\blbo\b|accretiv|dilutiv|deferred tax|\bdta\b|\bdtl\b|securitiz|waterfall|\bpik\b|"
    r"purchase accounting|338|noncontrolling|minority interest|unlever|relever|mid-?year|"
    r"convertible|option pricing|black-?scholes|duration|convexity|tranche|synthetic|"
    r"circular|iterat|sensitivity|three-?statement|walk me through (the|a) (full|entire)|"
    r"what happens to (all )?(three|3) statements|net operating loss|\bnol\b|earnout|cvr\b|"
    r"stub period|dividend recap|pro forma", re.I)

BASIC_PAT = re.compile(
    r"^(what is|what are|define|what does .{0,40} (stand for|mean)|how do you calculate|"
    r"what's the difference between|why (do|does|would) .{0,60}\?$)", re.I)

NUM_PAT = re.compile(r"\$?\d[\d,.]*\s*(m|mm|bn|billion|million|%|x)\b", re.I)

BEHAV_FRAMEWORKS = {
    "Why Banking / Why Firm": (
        "Three parts, 45–60 seconds. (1) The path: what in your background pulled you toward this "
        "work — a class, a project, an internship task you actually enjoyed. (2) The role: what an "
        "analyst does day to day (valuation and modelling, diligence, marketing materials, running a "
        "process) and which part of that you want reps in. (3) The firm: two specifics you could not "
        "say about any other bank — a group's deal flow, a sector focus, the deal team structure, "
        "people you spoke with and what they said. Close by connecting your evidence to their platform. "
        "Avoid generic praise ('great culture', 'prestige') with nothing behind it."),
    "Resume & Experience Walkthrough": (
        "Chronological and short: where you started, each move and *why* you made it, ending at this "
        "interview. Two minutes maximum. Spend the most time on the one or two experiences most "
        "relevant to the role, and for each give the task, what you specifically did, and the outcome "
        "with a number if you have one. Plant hooks you want to be asked about; be ready to go three "
        "layers deeper on anything on the page, including every technical claim and deal you list."),
    "Leadership & Teamwork": (
        "STAR: Situation, Task, Action, Result. Pick a story where you had no formal authority — that "
        "shows more. Be explicit about what *you* did versus what the group did, name the trade-off "
        "you had to manage, and finish with a measurable result and one thing you would do differently. "
        "Have three distinct stories prepared so you are not reusing the same one all interview."),
    "Conflict, Failure & Pressure": (
        "Choose a real failure with real stakes, not a disguised strength. Structure: what went wrong, "
        "your share of the responsibility (own it plainly), the concrete steps you took to contain it, "
        "the outcome, and the specific habit or process you changed afterwards — with evidence that the "
        "change stuck. Keep the blame off other people. For pressure and deadline questions, show "
        "prioritisation and communication: what you cut, what you escalated, and when."),
    "Strengths, Goals & Self-Assessment": (
        "Give a strength that maps to the job (attention to detail, speed on repetitive work, clear "
        "written communication) and prove it with one short example. For weaknesses, name a genuine one "
        "that is not disqualifying, then the mechanism you use to manage it and evidence it is "
        "improving. For goals, show commitment to the analyst role first and a plausible, honest "
        "direction after it; do not announce that you plan to leave for a buy-side seat in two years."),
    "Markets & Deal Interest": (
        "Pick a deal in the group's sector announced in the last 6–12 months. Cover: buyer, target, size "
        "and multiple, the strategic rationale, how it was financed, what the market reaction was, and "
        "your own view on whether it was a good price. Know the comparable multiples and one risk to the "
        "deal. Refresh your example and the numbers the week of the interview — dated facts are the "
        "fastest way to lose credibility here."),
    "Brainteasers & Estimation": (
        "Think out loud and structure before you compute. State your assumptions, break the problem into "
        "population × penetration × frequency (or an equivalent decomposition), use round numbers, then "
        "sanity-check the magnitude against something you know. The interviewer is testing structure and "
        "composure, not the exact answer — say your logic as you go and flag which assumption your answer "
        "is most sensitive to."),
    "Logistics & Recruiting": (
        "Answer briefly, honestly and without over-explaining. On other processes: be truthful without "
        "naming leverage you do not have, and reaffirm interest in this firm with a specific reason. On "
        "timing and availability: be concrete. Always bring two or three real questions of your own — "
        "about the group's deal mix, how analysts are staffed, or what separates a strong first-year — "
        "and never ask something answered on the firm's website."),
    "Personality & Interests": (
        "These are culture and memorability checks, not trick questions. Give a real, specific answer "
        "you can talk about for a minute — a book you actually read, a hobby you actually do — and "
        "say why it holds your interest. Specific beats impressive. Keep it clean and uncontroversial, "
        "tie it back to a trait that matters on the job (curiosity, discipline, competitiveness) "
        "without forcing the connection, and leave the interviewer an easy follow-up."),
    "Technical Skills & Tools": (
        "Answer concretely and modestly, then prove it. Name the tools you have actually used and what "
        "you built with them — a three-statement model, a comps set, a screen — rather than claiming "
        "fluency in the abstract. Be ready to name specific shortcuts or functions if asked, and to say "
        "honestly where your limits are plus how you are closing the gap. Overstating here is costly: "
        "the follow-up question is usually a live test."),
    "Behavioral Stories (STAR)": (
        "STAR: Situation (two sentences of context), Task (what you were responsible for), Action (the "
        "bulk of the answer — what *you* did, step by step, including the judgement calls), Result "
        "(quantified if possible, plus what you learned). Keep it to 90 seconds and stop; let them ask "
        "follow-ups. Prepare four or five versatile stories — leadership, failure, conflict, analytical "
        "work, going beyond the brief — and adapt them rather than searching for a new story each time."),
    "General Fit": (
        "STAR: Situation, Task, Action, Result, with the Action doing most of the work. Keep it under "
        "90 seconds, use a real example you can defend under follow-ups, quantify the result where you "
        "can, and end with what you took from it. Prepare a small set of versatile stories — a "
        "leadership one, a failure one, a conflict one, an analytical one — and map them onto whatever "
        "is asked rather than inventing on the spot."),
}


# A behavioral question gets guidance for its own kind of question, not just its topic.
# The twelve topic frameworks below are the floor; these are matched first, in order, so
# a defensive question about a low GPA stops reading like a cheerful "why banking" pitch.
# Order matters: the narrow patterns come before the broad ones that would also match.
# Lines the source captured as questions that are not questions: a candidate's commentary
# on their own interview, or half of a prompt whose other half landed on another card.
# Hand-checked one by one; add an id only after reading it.
# Quantitative questions the source recorded without the numbers, the rules or the
# question itself, so no solution exists for them as written. Hand-checked while the
# solvable brainteasers were moved to the technical deck.
UNSOLVABLE = {
    "B0096", "B0230", "B0564", "B0768", "B0943",
}

NOT_A_QUESTION = {
    "B0137", "B0187", "B0226", "B0286", "B0289", "B0302", "B0315", "B0347",
    "B0444", "B0498", "B0540", "B0546", "B0678", "B0682", "B0771", "B0909",
    "B0954", "B0966", "B0973",
}

BEHAV_GUIDES = [

    # ---- questions that put you on the back foot -------------------------------------
    ("Explaining a low or missing GPA",
     r"\bgpa\b|failed a class|what grade did you (receive|get)",
     "A number on the page is already known, so this is a composure test, not a maths test. "
     "They want to see whether you own a weakness without unravelling. "
     "• Structure: state the number plainly, give one real reason in a single sentence, then "
     "spend the rest of the answer on evidence that it does not predict your work. "
     "• Evidence that works: an upward trend by year, a higher major or quantitative GPA, a "
     "heavy course load carried alongside a job, a specific hard class you did well in. "
     "• Say it like this: \"It's a 3.2. I worked twenty hours a week through sophomore year and "
     "my grades showed it. It's 3.6 since, and 3.8 in my finance classes.\" "
     "• Traps: do not blame a professor, do not call the curve unfair, do not volunteer a number "
     "nobody asked for, and never round up — they may have your transcript."),

    ("Explaining a gap in your resume",
     r"gap (in|between) (your )?(employment|resume|work)|why was there a gap|"
     r"work experience gaps|weren't working for",
     "The silence is what worries them, not the gap. An unexplained gap invites the worst guess. "
     "• Structure: name the period, say what you were doing in one sentence, and show it was "
     "purposeful or at least handled — study, caring for family, visa processing, a failed "
     "venture, a deliberate search for the right role. "
     "• Then close it: say what you did to stay sharp, and bring the answer back to the present. "
     "• Traps: vagueness reads as concealment. Do not pad the dates on your resume to hide it, "
     "because the background check will find the real ones."),

    ("Why you left, or did not return",
     r"why did you (leave|quit)|why are you leaving|why did you (choose )?not to return|"
     r"didn't you (win|get) an offer|fail to get a return offer|(don't|do not|do you not) want to (go back|return)|"
     r"do not want to return|why do you want to lateral|why associate lateral|"
     r"why.{0,30}leave (your current|investment banking)",
     "They are checking whether you were pushed or whether you chose. Both can be fine; only one "
     "of them survives a bad telling. "
     "• Structure: a forward-looking reason first — the work you want to do and cannot do there — "
     "then the honest constraint, briefly, without a villain. "
     "• If there was no return offer, say so before they ask twice. A candidate who names it "
     "calmly and says what they learned reads far better than one who is caught. "
     "• Traps: never criticise the old firm, your old team or your old boss. The industry is "
     "small, the interviewer may know them, and bitterness is the actual disqualifier."),

    ("Coming from a non-target school",
     r"non-?target|from a non-traditional background|over an applicant from|"
     r"why should we (pick|select) a candidate from",
     "This is asked to see whether you are defensive about it. Being defensive is the only wrong "
     "answer. "
     "• Structure: do not argue that your school is underrated. Move straight to evidence — the "
     "modelling you have actually done, the deals you can discuss, the number of bankers you have "
     "spoken to, the preparation you did without a campus pipeline. "
     "• The strongest version shows initiative that a target-school student would not have needed: "
     "you found the material and the people yourself. "
     "• Traps: comparing yourself unfavourably to anyone, and naming another candidate or school."),

    ("Switching careers or fields",
     r"why (are you )?(moving|switching|changing) (from|careers)|why did you switch|"
     r"move from (pharmaceuticals|medicine|technology|operations)|from medicine and science|"
     r"pursuing a finance career when you did not major|why pursue a career with.{0,40}in your thirties|"
     r"why finance.{0,20}(when|despite)|never worked in investment banking before|"
     r"haven't you taken any accounting",
     "A switch is only a risk if it looks like an escape. Make it look like a decision. "
     "• Structure: what you learned in the old field that transfers (client work, modelling, "
     "technical depth, a sector you now know better than most bankers), what the old field could "
     "not give you, and what you did to prove the switch is real. "
     "• Proof matters more than enthusiasm here: a course finished, a model built, a deal you can "
     "walk through, twenty bankers spoken to. Name it. "
     "• Traps: \"I wanted more money\" and anything that reads as running away rather than toward."),

    ("Doubts about your commitment",
     r"how do (i|we) know you (will|won't|will not)|won't just leave|would you move again|"
     r"stay in banking for two years|how committed are you|leave in a year|"
     r"why.{0,25}not leave|long-term career pursuit or are you doing this as a launchpad",
     "They are pricing the risk that they train you and you walk. You cannot promise forever and "
     "they would not believe you. "
     "• Structure: be honest about the horizon you can commit to, give a concrete reason tied to "
     "this seat rather than to banking generally, and show you know what you are signing up for. "
     "• What convinces: specifics about the group's work that you could not get elsewhere, and "
     "evidence you have stuck with something hard before. "
     "• Traps: announcing a buy-side plan, over-promising a decade, or sounding as if the job is a "
     "stepping stone you have already stepped off."),

    ("Give us a reason not to hire you",
     r"why should we not hire|why shouldn't we hire|wary of hiring|"
     r"one problem that we will have with you|what would worry you most if you got the job|"
     r"reservation you have about working|one question you wish we would not ask",
     "A trap dressed as humility. They want self-awareness without self-sabotage. "
     "• Structure: give one real, non-disqualifying gap, stated plainly, then the mechanism you "
     "use to manage it, then evidence that it is closing. "
     "• Safe ground: inexperience with something specific and learnable. Dangerous ground: "
     "anything about attention to detail, reliability, or handling hours — those are the job. "
     "• Traps: a disguised strength (\"I care too much\") insults them, and a genuine "
     "disqualifier ends the interview. Pick the narrow middle and move on quickly."),

    # ---- the why family --------------------------------------------------------------
    ("Why this firm",
     r"^why (this firm|us\b|our)|want to be part of this firm|see yourself contributing|"
     r"why do you want to work (at|for) (this|our|us)|"
     r"why (goldman|evercore|moelis|lionTree|ubs|blair|nomura|lazard|jpmorgan|jp morgan)|"
     r"why.{0,20}specifically (do you want to work|interested in working) for|"
     r"what interests you in our firm|why us ver|why .{0,15} and why not other|"
     r"why a (boutique|big bank|bulge|rotational program)|why middle.?market|"
     r"what specifically about .{0,20} attracts you|original reason why you want to work",
     "The answer that fails is the one that would survive a find-and-replace of the firm's name. "
     "• Structure: two or three reasons that are specifically true of this firm — its deal mix, "
     "its sector strength, its structure (lean deal teams, no staffer, early client contact), a "
     "named transaction — and then the people you have actually spoken to there. "
     "• Names and deals are the proof. \"I spoke with two analysts in your industrials group and "
     "both described the same staffing model\" beats any adjective. "
     "• Traps: prestige, culture and \"the people\" with nothing behind them. Every candidate says "
     "those. Do not praise a league-table rank the firm does not hold."),

    ("Why this city or office",
     r"why (do you want to work in |would you want to move to |)?(new york|nyc|chicago|boston|"
     r"san francisco|los angeles|la\b|charlotte|raleigh|singapore|london|west coast|usa)\b|"
     r"why this (office|location)|why this location as opposed|which office location|"
     r"why.{0,20}(east|west) coast|rather than (staying in|your hometown)",
     "A short question with a real purpose: they are testing whether you will still be there in a "
     "year, and whether your interest is in the city or just in the offer. "
     "• Structure: one genuine tie to the place — family, your school, a sector that is "
     "concentrated there — plus the professional reason, which is usually the client base. "
     "• Say where you will live and that you have thought about the move. Logistics reassure. "
     "• Traps: \"I'll go anywhere\" sounds like you have applied everywhere, and weather or "
     "nightlife sounds like you are not thinking about the work."),

    ("Why this group or product",
     r"why (this|x|\[x\]|that)? ?(group|coverage|industry group|product group)|"
     r"why (financial planning|private credit)|"
     r"why (m&a|leveraged finance|lev fin|restructuring|ecm|dcm|capital markets|credit|"
     r"fixed income|equity research|secondaries|growth equity|public finance|industrials|"
     r"healthcare|technology|software|saas|fintech|renewables|energy|retail|beauty)\b|"
     r"which group|what areas of investment banking|why are you interested in (m&a|credit|"
     r"capital markets|dcm|secondaries|growth equity|equity markets|fixed income|energy)|"
     r"why.{0,20}rather than (m&a|capital markets|an industry group)",
     "Groups are chosen for the work they do, not the brand on the door. Show you know what the "
     "day actually looks like in this one. "
     "• Structure: the characteristic of the work that suits you — the modelling intensity of "
     "lev fin, the legal and creditor dynamics of restructuring, the long client relationships of "
     "a coverage group — then the evidence in your background, then a deal in that space. "
     "• Name the product's own vocabulary correctly. Confusing ECM with DCM, or a coverage group "
     "with a product group, ends the conversation quickly. "
     "• Traps: reasons that would apply to any group, and claiming to have wanted this since "
     "childhood."),

    ("Why not the other path",
     r"would you rather pursue|have you considered a (bigger|different)|"
     r"why not (consulting|pe\b|private equity|buy.?side|buyside|s&t|sales and trading|hf\b|"
     r"hedge fund|vc\b|venture capital|ib\b|investment banking|a bulge|a major american bank|"
     r"a different group|accounting|trading)|why.{0,25}rather than (consulting|private equity|"
     r"investment banking|sales and trading|equity research|fixed income|engineering|m&a)|"
     r"why.{0,10}(vs\.?|versus) (ib|pe|am|s&t)|why would i want to join a big 4",
     "They want to know you chose this deliberately, having understood the alternative. "
     "• Structure: say something genuinely true and positive about the other path, then the "
     "specific difference that made you choose this one — pace, ownership of the model, the kind "
     "of problem, the length of the engagement. "
     "• Knowing the alternative well is the point. A candidate who cannot describe what "
     "consultants actually do has not chosen between them. "
     "• Traps: dismissing the other path, or giving a reason that applies equally to both."),

    ("Why your school, major or degree",
     r"why did you (choose|attend|major|pursue|study)|why your (university|school|degree)|"
     r"why (ucla|usc|northeastern|an mba|pursue an mba)|why did you change your field|"
     r"why are you studying|why did you decide to take those classes|why.{0,15}/ ?economics|"
     r"why finance and philosophy|why did you choose your (business school|mba program|"
     r"undergraduate university|graduate school)",
     "A low-stakes opener that is really a test of whether you make decisions for reasons. "
     "• Structure: the reason you chose it at the time, something concrete you got from it, and "
     "the bridge to this job. The bridge matters most for a non-finance major. "
     "• A non-finance degree is an asset if you can name the transferable skill — writing, "
     "statistics, the discipline of a lab — rather than apologising for it. "
     "• Traps: \"it was the best school I got into\" and treating the major as an accident."),

    ("Why banking, finance or this field",
     r"career in the financial|financial (career )?industry\b|"
     r"^why (banking|investment banking|finance|ib\b|asset management|private equity|"
     r"equity research|wealth management|investing|consulting)|"
     r"why do you want to (work in|do|be)|why are you interested in (banking|finance|"
     r"investment banking|private equity|asset management|wealth management|investing|this role|"
     r"a fund of funds|working)|what (attracts|interests) you|how did you get interested|"
     r"what sparked your interest|what makes you interested|why did you get into|"
     r"why.{0,20}interested in working (at|for)|why do you want a role",
     "The most asked question in the process, and the one most often answered with adjectives. "
     "Three parts, 45 to 60 seconds. "
     "• The path: the specific moment that pulled you here — a class, a model you built, a task "
     "in an internship you actually enjoyed. One moment, told concretely, not a life story. "
     "• The role: what an analyst actually does, said in a way that proves you know — the "
     "modelling, the diligence, the volume of it, the hours — and why that suits you. "
     "• The fit: why this firm and this group, with a name or a deal attached. "
     "• Traps: \"fast-paced and dynamic,\" \"I like finance,\" and anything about compensation or "
     "exit opportunities. Every one of those is a filler phrase they have heard all week."),

    # ---- fit and self-assessment ------------------------------------------------------
    ("Tell me about yourself",
     r"tell me about yourself|tell me everything about yourself|tell us your story|"
     r"overview of your educational|walk me through your "
     r"(resume|cv|background)|personal elevator pitch|tell me about your background",
     "The opener, and the only answer you can fully script. Ninety seconds, chronological, "
     "ending where you are sitting. "
     "• Structure: where you started, each move and the reason you made it, and what that chain "
     "of choices leads to — this role. The reasons are what makes it an argument rather than a "
     "recitation of your resume. "
     "• Plant hooks. Mention the deal, the club or the project you want them to ask about, and be "
     "ready for the follow-up on each. "
     "• Practise it aloud until it is 90 seconds. Written answers always run long. "
     "• Traps: starting at birth, listing every job, or reading your resume back to someone who "
     "is holding it."),

    ("Walk me through something on your resume",
     r"(?<!not )(?<!listed )on your resume|resume experience|explain each item|"
     r"discuss (your |an |a )?(achievement|project|internship|experience|previous experiences|"
     r"previous internships|previous work|university|research|part-?time|projects)|"
     r"tell me about (your time at|\(internship\)|this company that you worked for)|"
     r"what was your role on the|case competition|explain your responsibilities in previous|"
     r"what did you learn in your most recent internship|discuss the (leadership activities|"
     r"interests listed)|explain how you approached a project|describe your investment club|"
     r"tell me about your experience in",
     "Everything on the page is fair game, so the rule is simple: if you cannot talk about a line "
     "for two minutes, take it off. "
     "\u2022 Structure: what the organisation or project was in one sentence, what you were "
     "responsible for, the hardest part, and the outcome with a number where one exists. "
     "\u2022 Be precise about scope. Saying you 'worked on' something invites the follow-up that "
     "finds out you did not. Naming the narrow thing you actually owned is more impressive and "
     "survives questioning. "
     "\u2022 Have a reason ready for why you did it, not just what it was. Choices are what the "
     "interviewer is reading. "
     "\u2022 Traps: inflating a title, claiming a team result as your own, and a bullet you wrote "
     "a year ago and can no longer explain."),
    ("Your greatest weakness",
     r"weakness|three weaknesses|what are you not good at|biggest critic|"
     r"shortcomings|what are three things your former manager would like you to improve|"
     r"what do other people think about you that isn't true|misconception do people have",
     "Not a confession and not a humblebrag. They want evidence you can take feedback. "
     "• Structure: one real weakness that is not central to the job, the specific mechanism you "
     "now use to manage it, and a concrete sign it is improving. "
     "• Good ground: public speaking, delegating, over-editing your own work, saying no to too "
     "many commitments. Bad ground: attention to detail, meeting deadlines, working under "
     "pressure, teamwork — you are applying for a job made of those. "
     "• If asked for three, give three real ones and keep each short. Reaching for a fourth "
     "filler is worse than a brief answer. "
     "• Traps: \"perfectionist,\" \"I work too hard,\" and any weakness you cannot show you are "
     "actually working on."),

    ("Your strengths and what sets you apart",
     r"strength|what sets you apart|what can you offer us|unique viewpoints|what represents you|specific skillset|why someone from your university|"
     r"why should we hire you|two reasons we should hire|what makes you the best candidate|"
     r"most qualified candidate|best fit for this position|why are you the|"
     r"which skills distinguish you|skill you have that your peers do not|"
     r"what experience do you bring|why would you be a strong",
     "Pick strengths the job actually needs, then prove them. An unproved strength is an opinion. "
     "• Structure: name two or three, each with a one-sentence piece of evidence attached. "
     "Attention to detail, speed on repetitive work without errors, clear writing, staying "
     "organised across several workstreams — these are the analyst's real currency. "
     "• The evidence is the answer. \"I check my own work twice\" is nothing; \"I built the "
     "operating model for a 40-page CIM and the VP found no errors in the final version\" is "
     "something. "
     "• Traps: abstract nouns with no example, and strengths that have nothing to do with the "
     "seat you are interviewing for."),

    ("Describe yourself in three words",
     r"three words|describe yourself in|how would your (friends|roommate|teammates|manager|"
     r"colleagues) describe|what would your (roommate|teammates|friends|manager) say|"
     r"if i spoke with your friends|name one thing your colleagues would describe",
     "A memory test for the interviewer: they will remember the words, so choose ones that help. "
     "• Structure: three words that are different from one another, each with a half-sentence of "
     "proof. Two work words and one human one is a good mix. "
     "• If the question routes through a friend or roommate, keep the register honest — the words "
     "a friend would use are warmer than the ones you would pick for a resume, and the interviewer "
     "can tell when you have ignored that. "
     "• If asked for positives and negatives, give both honestly; the negative is a weakness "
     "question wearing a hat. "
     "• Traps: three synonyms, and words so generic they describe everyone ('hardworking')."),

    ("Career goals and where you see yourself",
     r"five years|ten years|long-?term (career )?goal|where do you see yourself|"
     r"what would you like to be doing in ten|after a two-year analyst program|"
     r"what would (a successful|a failure of) 5 years look like|what do you want from this job|"
     r"what do you (hope|want) to (gain|learn|get)|what would you get out of our program|"
     r"what are you looking for in an ideal opportunity|what motivated you to apply",
     "They are testing commitment to this seat, not the accuracy of your five-year forecast. "
     "• Structure: commit clearly to the analyst role and what you want to be good at by the end "
     "of it, then give an honest and plausible direction after it. "
     "• Direction beats precision. \"I want to be the analyst the VPs trust with the model, and "
     "then keep building sector depth\" is safe, specific and true. "
     "• Traps: announcing a private equity exit in two years, naming business school as the plan, "
     "or claiming you will still be at this firm in twenty years. One is disloyal, one is worse, "
     "and one is not believed."),

    ("Your proudest achievement",
     r"proudest|most proud|most significant achievement|accomplishment you are most proud|key accomplishments|"
     r"greatest achievement|what is something that you are doing right now that you are proud",
     "Choose on the strength of the story, not the size of the trophy. "
     "• Structure: brief context, what made it hard, what you specifically did, and the outcome "
     "with a number if one exists. The difficulty is what makes it an achievement. "
     "• Something modest that you drove yourself beats something impressive you were adjacent to. "
     "Be clear about which parts were yours. "
     "• Traps: an achievement with no obstacle in it, and a team result where your own "
     "contribution never becomes clear."),

    ("What motivates you",
     r"what motivates you|what drives you|your values|what is your purpose in life|"
     r"drive for excellence|how do you define success",
     "A soft question that rewards specificity as much as a hard one. "
     "• Structure: name the thing honestly — solving a problem nobody has cracked, being trusted "
     "with real responsibility early, getting measurably better at a craft — and attach one "
     "example of it operating in your life. "
     "• Tie it to the job without forcing it. If what drives you is mastery, banking's "
     "apprenticeship is a genuine answer. "
     "• Traps: money, prestige, and abstractions so broad they could belong to anyone."),
    # ---- story questions, by what the story has to prove -----------------------------
    ("A hypothetical judgement call",
     r"what would you do if|what would be your thought process|completely swamped|"
     r"how would you handle (the situation|it)|you find an error|"
     r"sends the wrong document|accidentally emails you confidential|"
     r"not completely accurate|close enough|printed something out for a presentation|"
     r"realize you made a large error|conflicting work priorities|two mds|five mds|"
     r"half your team takes leave|where is that thing i asked you for|"
     r"last resort to ensure a client presentation|client demanded lower fees|"
     r"client tells you to do x",
     "These are not STAR questions — there is no past story to tell. They are testing judgement "
     "under a specific banking constraint, so answer the scenario as posed. "
     "• Structure: state the principle you are applying, say what you do first, say who you tell "
     "and how quickly, then handle the complication the question has built in. "
     "• On an error in work about to go out: flag it immediately, to the most senior person "
     "available, with the fix or an estimate of how long the fix takes. Speed and candour are the "
     "whole answer. An error that reaches a client is far worse than an awkward conversation. "
     "• On conflicting instructions from two seniors: you do not adjudicate between them. Get the "
     "deadlines and the scope, tell each what else is in the queue, and let them re-prioritise. "
     "• Traps: quietly fixing it and saying nothing, going over someone's head as the first move, "
     "and refusing to commit to an answer because \"it depends.\""),
    ("A time you failed or made a mistake",
     r"fail|mistake|went wrong|didn't go as planned|hasn't gone the way you expected|"
     r"missed a deadline|slipped through the cracks|something did not go as expected|"
     r"biggest mistake|a regret|something you did which you regret|unhappy with an outcome|"
     r"setback|were wrong\b|felt wronged",
     "The most revealing story question. They are testing accountability, and a sanitised answer "
     "tells them you have none. "
     "• Structure: what you were responsible for, what went wrong and your part in it, what you "
     "did the moment you knew, and the specific change you made afterwards. "
     "• Spend the most time on the last two. The recovery and the lesson are the answer; the "
     "failure is only the setup. "
     "• Pick something with real stakes that was genuinely your fault. A failure caused entirely "
     "by someone else is not a failure story, and they will notice. "
     "• Say what you told the person affected and how fast. In banking an error flagged in ten "
     "minutes is a nuisance and the same error found by a client is a crisis — show you know "
     "which one you created. "
     "• Traps: a disguised strength, blaming a teammate, and a failure so trivial it insults the "
     "question."),

    ("A time you handled conflict or disagreement",
     r"conflict|disagree|difficult (colleague|team member|person|people|manager|client|customer)|"
     r"someone whose style was very different|worked with someone difficult|"
     r"disagreements with another team member|stood up for your beliefs|"
     r"told someone in authority that they were wrong|had an issue with another co worker",
     "They are not looking for someone who wins arguments. They are looking for someone who stays "
     "professional when a deal team is tired. "
     "• Structure: the substance of the disagreement (not the personalities), what you did to "
     "understand the other position, the specific step you took, and the working relationship "
     "afterwards. "
     "• Be generous about the other person. The candidate who describes a colleague as lazy or "
     "difficult has told the interviewer how they will describe this team one day. "
     "• A disagreement you lost, handled well, is a strong answer — it shows you can commit to a "
     "decision that was not yours. "
     "• Traps: a conflict with no resolution, anything that escalated to a manager as the first "
     "move, and making yourself the only reasonable person in the story."),

    ("A time you led, and your leadership style",
     r"leader|leadership|led people|how do you lead|manage a team|managing people|"
     r"mentor|delegat|took initiative|stepped up|organize a team|"
     r"convince(d)? (a group|someone|people)|persuade|influence|"
     r"rose above your peers|took charge",
     "The strongest leadership stories are the ones where you had no authority, because that is "
     "the analyst's actual position. "
     "• Structure: STAR, with most of the time on the Action. Pick a case where you had to bring "
     "people with you rather than instruct them. "
     "• Show the mechanism: how you worked out what each person wanted, what you changed in your "
     "own approach, how you handled the person who would not move. "
     "• If asked for your style, name it and then prove it with the same story rather than "
     "describing it in the abstract. "
     "• Traps: a title with no decision attached, and claiming credit for a group's work without "
     "ever saying what you personally did."),

    ("A time you worked in a team",
     r"\bteam\b|group project|worked in a group|collaborat|team player|teamwork|"
     r"group dynamics|put your team before|contributed uniquely",
     "Banking work is done in deal teams of three or four, so this is a direct test of what you "
     "would be like at 1am on a Tuesday. "
     "• Structure: STAR, and be precise about your own role — \"I owned the model and the two "
     "appendix exhibits\" rather than \"we worked together well.\" "
     "• Show awareness of the others: how the work was divided, what you did when someone was "
     "behind, how you handled being the junior person in the room. "
     "• A story where you covered for a struggling teammate without making it a complaint is "
     "unusually strong. "
     "• Traps: a story in which you did everything yourself, which answers a different question, "
     "and one in which your own contribution never becomes visible."),

    ("Pressure, deadlines and competing priorities",
     r"pressure|stress|difficult times|how many hours will you work|"
     r"tight (deadline|timeline|project)|long hours|workload|burnout|"
     r"priorit|multitask|juggl|competing (tasks|deadlines|priorities|work)|"
     r"demanding hours|80 hours|can you work|handle the (hours|demands)|"
     r"high quality output under tight|the hardest you've ever worked",
     "Half a test of your method, half a test of whether you know what you are signing up for. "
     "• For the story version: STAR, with the triage made explicit — what you did first, what you "
     "let slip deliberately, and who you told. Communicating a slipping deadline early is the "
     "behaviour they are actually screening for. "
     "• For the hours version: do not perform enthusiasm for suffering. Say you understand the "
     "hours concretely (the weeks are long and unpredictable, weekends get taken), give evidence "
     "you have sustained something demanding before, and say how you stay functional. "
     "• Traps: claiming you never feel stress, claiming you love 100-hour weeks, and any method "
     "that sounds like working harder rather than prioritising better."),

    ("An ethical dilemma you faced",
     r"ethical|integrity|morally ambiguous|unethical behavio|compromise your values|"
     r"saw somebody doing something wrong|saw something wrong",
     "A values question with one right shape: you noticed, you did something, and you did it "
     "through the proper channel. "
     "• Structure: the situation and precisely what made it wrong, what you considered, what you "
     "did, and the outcome — including the cost to you if there was one. "
     "• Escalating appropriately is a good answer, not a weak one. Juniors are not expected to "
     "resolve these alone; they are expected not to stay silent. "
     "• Keep the stakes real but proportionate. A genuine small dilemma handled well beats an "
     "implausible large one. "
     "• Traps: a story where you did nothing, one where you went around everyone to a regulator "
     "as a first step, and any answer that treats the rule as negotiable under deadline."),

    ("A time you learned something fast or worked without information",
     r"quickly learn|learned something new|limited information|lacked sufficient data|"
     r"very little information|unfamiliar problem|haven't done before|"
     r"gap in your skills|change your (usual workflow|approach)|demonstrate flexibility|"
     r"stepped outside your comfort zone|tried something new|adapt",
     "A direct proxy for the first month of the job, when you will be handed something you have "
     "never done and a deadline. "
     "• Structure: what you did not know, how you closed the gap and how fast, what you did about "
     "the parts you still could not resolve, and the result. "
     "• The sophisticated move is showing how you worked while still uncertain — the assumption "
     "you flagged, the question you asked early rather than guessing. "
     "• Traps: a story where the learning was easy, and one where you went quiet for three days "
     "before admitting you were stuck."),

    ("How you work: process, time and method",
     r"do you prefer|how do you (manage your time|structure|approach|solve problems|teach|work in|organi[sz]e)|"
     r"how would you approach a project|describe a typical research process|"
     r"how do you (think about|define success)|what is your approach to analy|"
     r"how would you (research an idea|go about convincing)|how do you structure an unfamiliar|"
     r"approach a project from start to finish|how do you (communicate|persuade someone)|"
     r"are you detail-oriented|how do you manage|what is important in teamwork",
     "A question about method. The answer should sound like something you actually do, which "
     "means it needs mechanics, not adjectives. "
     "\u2022 Structure: name the method in one sentence, then walk one real example through it. "
     "The example is what makes it credible. "
     "\u2022 For prioritisation and time: say how you decide what is urgent, what you do when two "
     "seniors both want something, and how you communicate a slipping deadline. Flagging early is "
     "the behaviour banks screen for. "
     "\u2022 For analysis: scope the question, find the data, sanity-check it, and say what you do "
     "when the data is incomplete. "
     "\u2022 Traps: a method with no example, and 'I'm very organised' with nothing behind it."),
    ("Tell me about a time (any story question)",
     r"describe an analysis|tell me about a time|tell us about a time|tell me a time|describe a (time|situation|"
     r"experience|project|problem|setback)|give (me |us )?an example|name a time|"
     r"talk about a time|a time (when|where|you)|when (did|have) you|"
     r"provide an example|describe an experience|an experience where|"
     r"can you (describe|tell me about) a (situation|time)|what(?:'s| is) a time",
     "The general story question. Whatever it asks for, the shape is the same and the Action is "
     "where the marks are. "
     "\u2022 STAR: Situation in two sentences, Task in one, Action in five or six, Result in one "
     "with a number if you have it. Most candidates over-build the Situation and rush the Action, "
     "which is exactly backwards. "
     "\u2022 Keep it under 90 seconds and end with what you took from it. "
     "\u2022 Prepare four versatile stories rather than one per question: a leadership story, a "
     "failure story, a conflict story and an analytical story. Almost any prompt can be served by "
     "one of them if you choose the angle deliberately. "
     "\u2022 Use a real example you can defend. Every story invites follow-ups about what you "
     "specifically did, what you would change, and what the other people thought. "
     "\u2022 Traps: a story with no obstacle, 'we' throughout so your own role never lands, and a "
     "result you cannot describe."),

    # ---- what they expect you to have researched --------------------------------------
    ("What you know about the firm",
     r"summarize your understanding of|hardest issue this firm|know of its history|"
     r"what do you know about (this firm|this bank|us|our|the firm|blackrock|blackstone|jpmorgan|"
     r"jp ?morgan|goldman|evercore|stephens|this (role|industry))|"
     r"who (is|are) (the firm's|our)? ?(ceo|cfo|founder|competitors)|who founded|"
     r"what differentiates this firm|who do you think our competitors|"
     r"this firm's values|what are evercore's values|what do you know about (this firm's culture|"
     r"our office|our group|the structure)|how is .{0,15} different from others|"
     r"what does (an analyst at the firm|the cb role|our team) do|"
     r"what makes .{0,10} special compared|what role does technology play at",
     "A preparation check with a binary outcome. There is no technique that substitutes for "
     "having looked. "
     "• What to know before any interview: the firm's size and structure, two or three recent "
     "deals it advised (parties, size, your view of the rationale), the groups it is strong in, "
     "the names of people you have spoken to, and the leadership of the group you are joining. "
     "• Where to get it: the firm's own tombstones and press releases, recent deal coverage, and "
     "conversations with people there. The last of these is what makes an answer specific. "
     "• If asked something you genuinely do not know — a CFO's name, a number — say so briefly "
     "and offer what you do know. Guessing is worse. "
     "• Traps: facts anyone could recite from the homepage, and praising a strength the firm does "
     "not actually have."),

    ("What the job actually involves",
     r"what does an (analyst|investment banker|investment banking analyst|rx banker|associate) do|"
     r"what do bankers work on|what do you think (an analyst does|you will be doing|your job "
     r"would look like)|typical day|day to day|average day on the job|"
     r"what makes a (good|successful) (analyst|associate|banker)|"
     r"qualities that make an analyst successful|three qualities necessary|"
     r"what will be the hardest and easiest|what do you expect to do",
     "They are checking that you want this job rather than an idea of it. The students who answer "
     "badly here have usually never asked anyone. "
     "• What the work is: building and maintaining models, producing pitch books and CIMs, "
     "comparable company and precedent analysis, diligence request lists and data room "
     "management, taking notes on calls, and a great deal of formatting and checking. "
     "• What makes an analyst good at it: accuracy under time pressure, turning comments fast, "
     "clear written communication, and being the person whose work does not need re-checking. "
     "• Say the unglamorous parts out loud. A candidate who names the formatting and the version "
     "control is more convincing than one who only mentions the modelling. "
     "• Traps: describing a VP's job, mentioning client dinners, and saying you will be 'advising "
     "clients on strategy' in your first year."),

    ("Do you have any questions for us",
     r"questions for (me|us)|anything else you.{0,10}like (us )?to know|"
     r"two minutes to add anything|anything you would like us to know",
     "Never decline. Saying you have no questions reads as no interest, and it is the one part of "
     "the interview you fully control. "
     "• Have four or five ready, because two may get answered during the conversation. "
     "• What works: their own experience (what surprised them in their first year, what makes an "
     "analyst stand out here), the group's work (how deal teams are staffed, what the mix of "
     "sell-side and buy-side looks like), and anything that follows naturally from what they just "
     "told you. The last kind is the most impressive, because it proves you were listening. "
     "• Closing move: ask what the next step is and when you should expect to hear. "
     "• Traps: compensation, hours, vacation, exit opportunities, and anything answered on the "
     "firm's website. Do not ask a question designed to show off."),

    # ---- markets, deals and sectors ---------------------------------------------------
    ("Walk me through a deal you worked on",
     r"walk me through a deal|deal you worked on|your (role|contribution|involvement) in the deal|"
     r"your unique contributions to this deal|walk through a deal|"
     r"discuss (a deal|your transaction|recent transactions|your deal)|"
     r"explain your (work and contribution|involvement)|how was the deal.{0,10}financed|"
     r"strategic rationale for the deal you worked|walk me through one of your transactions|"
     r"a deal's rationale",
     "The follow-ups are the real test here, so choose a deal you can defend rather than the "
     "largest one you touched. "
     "• Structure: the parties and the size, why the client was doing it, what the process looked "
     "like, what you personally built, and how it ended or where it stands. "
     "• Be exact about your own contribution. \"I built the operating model and ran the comps\" is "
     "credible; implying you ran the process is not, and one follow-up will expose it. "
     "• Prepare for: what multiple it went at, how it was financed, what the key diligence issue "
     "was, and what you would have done differently. "
     "• Respect confidentiality. If the deal is unannounced, describe it generically — sector, "
     "rough size, structure — and say that is why. Interviewers respect the instinct. "
     "• Traps: a deal you only read about presented as one you worked on, and numbers you cannot "
     "reproduce under questioning."),

    ("A deal our firm advised, or a recent deal you followed",
     r"deal that (this firm|intrepid|evercore|jp ?morgan|sixth street|ft partners) has done|"
     r"recent (deal|transaction|ipo|merger)|a deal you (recently have |)followed|"
     r"one of our recent transactions|discuss a recent|name a deal|"
     r"deal that .{0,20} has (done|worked on)|two companies that .{0,15} should merge|"
     r"tell me two companies that you think should merge|deal you thought went badly",
     "Pick a deal in the group's own sector, announced in the last six to twelve months, and know "
     "it properly rather than knowing three deals vaguely. "
     "• Cover: buyer, target, size and multiple, the strategic rationale, how it was financed, the "
     "market reaction, and your own view on whether the price made sense. "
     "• The view is what distinguishes the answer. Have one specific reason the deal was a good or "
     "bad idea, and one risk to it. "
     "• Refresh the facts the week of the interview. A stale number is the fastest way to lose "
     "credibility on a question you chose to answer. "
     "• Traps: a deal so large everyone will cite it, a deal outside the group's sector, and "
     "reciting the press release without a judgement."),

    ("A market view or forecast",
     r"where (will|is) the (s&p|market|nasdaq|dow)|s&p 500 be in|up or down|"
     r"where do you see us equities|what do you think will happen to oil prices|"
     r"view on (bitcoin|sustainability|cryptocurrency)|where do you see the .{0,20} industry in five|"
     r"major world event|geopolitical threats|macroeconomic trends|"
     r"what is the current|where is the s&p at",
     "Two different questions wear this shape, and you must tell them apart. "
     "• If it asks for a level — where the S&P, the 10-year or SOFR is right now — it is a "
     "preparation check with a correct answer, and it expires. Look the numbers up the morning of "
     "the interview and know roughly where they were a year ago. "
     "• If it asks for a forecast, nobody expects you to be right. Give a base case with two or "
     "three drivers, name the indicator that would change your mind, and size your conviction "
     "honestly. "
     "• Say what you actually read and how often. The habit is more persuasive than the opinion. "
     "• Traps: a confident forecast with no mechanism behind it, a stale number stated as current, "
     "and inventing a figure you are not sure of."),

    ("An industry or sector you follow",
     r"thoughts on ai\b|private credit investments|"
     r"industry (you follow|you've been following|do you think has the largest potential)|"
     r"what do you think (of|about) the|sector|vertical|trend|headwind|tailwind|"
     r"competitive landscape|disruptive force|driving forces of innovation|"
     r"what's the next new|which (technology|fintech) company interests you|"
     r"sub-verticals|what are the moats|key performance indicators for the company|"
     r"startups|what are the main drivers of",
     "The point is depth in one area, not coverage of everything. One sector you genuinely follow "
     "beats opinions on five. "
     "• Structure: how the industry makes money, the two or three forces currently reshaping it, "
     "who is winning and why, and the metric that matters most in it — same-store sales, net "
     "revenue retention, book-to-bill, reserve life, whatever the sector actually uses. "
     "• Have one company you can discuss in detail and one recent transaction in the space. "
     "• Match the sector to the group where you can. Discussing semis with a healthcare team is a "
     "missed opportunity even when the analysis is good. "
     "• Traps: headlines with no mechanism underneath, and a 'trend' that has been true for a "
     "decade."),

    ("Current events and what you read",
     r"current event|recent (piece of )?news|in the news|news sources|podcasts|"
     r"which (websites|newspapers)|what articles do you read|keep up with current events|"
     r"tell me about an? (domestic current event|article|recent news)|"
     r"recent events that could affect",
     "A habit check. They want evidence you follow markets routinely, not that you crammed "
     "yesterday. "
     "• Structure: name what you actually read and how often, then take one story and say what it "
     "means — for a sector, for rates, for deal activity, ideally for this firm's business. "
     "• The second half is the answer. Summarising a headline proves nothing; the implication "
     "proves you think about it. "
     "• Have one story ready that connects to the group you are interviewing with. "
     "• Traps: naming a publication you do not read, and a story you cannot answer one follow-up "
     "question about."),

    ("Pitch me a stock or an investment",
     r"stock you|pitch|best idea|long or short|would you short|compelling investment opportunity|"
     r"what do you look for when investing|why are you long|investment (idea|thesis)|"
     r"which parts of the capital structures|would you invest|one portco|"
     r"company you (like|admire)|how would you allocate|if i gave you a million|"
     r"you have \$?1 million|how would you spend the money|how would you research an idea|"
     r"fundamental analysis|compare two investments",
     "Structure matters more than the pick. A defensible thesis on a dull company beats "
     "enthusiasm about a famous one. "
     "• Structure: what the company does and how it makes money, your thesis in one sentence, two "
     "or three supporting drivers, the valuation and why it is mispriced, the catalyst and its "
     "timing, and the main risk with your answer to it. "
     "• Know the numbers you quote — multiple, growth, margins — and where they came from. "
     "• Naming the risk yourself is what makes it a pitch rather than an advertisement. "
     "• Traps: a mega-cap everyone covers, a thesis that is only 'it is a good company,' and no "
     "view on valuation."),

    # ---- quantitative and puzzle --------------------------------------------------------
    ("Mental arithmetic",
     r"what(?:'s| is) \d|calculate \d|\d+ ?x ?\d|multiplied by|divided by|square root|"
     r"cubed|express .{0,12} as a percentage|what is the sum of|sum of 1 to|"
     r"% of \d|percent of \d|weighted average of",
     "Speed matters less than method and composure. Say the method out loud as you go. "
     "• Technique: round to something easy and correct afterwards. 19 × 23 is 20 × 23 less 23, so "
     "460 − 23 = 437. 49 × 63 is 50 × 63 less 63, so 3,150 − 63 = 3,087. Squares near a round "
     "number work the same way: 21² = 441 from 400 + 2(20) + 1. "
     "• Square roots: bracket it. √4,800 sits between 69² = 4,761 and 70² = 4,900, so about 69.3. "
     "• Percentages: 3% of 113 is 1% (1.13) times three, so 3.39. "
     "• Always sanity-check the magnitude before you answer, and never correct yourself silently "
     "— say that you are checking. "
     "• Traps: guessing to seem fast, and going quiet while you compute."),

    ("Market sizing and estimation",
     r"how many|estimate|approximately how large|how much would you charge|"
     r"market size|how much water does|what would it cost",
     "They are testing structure, not the answer. Two candidates with the same number can score "
     "very differently. "
     "• Method: decompose before you compute. Population, then the fraction that applies, then "
     "frequency, then amount — and keep the units straight at every step. "
     "• Worked shape: US coffee cups a day ≈ 330m people × 60% who drink coffee × 1.5 cups ≈ 300m. "
     "Round aggressively; 330m becomes 300m and the arithmetic stays in your head. "
     "• State each assumption as you make it, then say which one your answer is most sensitive to "
     "and roughly what range it implies. That sentence is what separates a strong answer. "
     "• Sanity-check at the end against something you know. "
     "• Traps: starting to calculate before structuring, false precision, and defending an "
     "assumption the interviewer pushes back on instead of adjusting it."),

    ("Logic puzzles and brainteasers",
     r"balance scale|weighing|light bulb|switches|ropes|jug|gallon|marble|knight|"
     r"pirates|lily pad|doubles? (in size )?every|coins that look identical|"
     r"faulty machine|broken machine|cut a cake|rubik|next number|sequence|"
     r"probability that|biased coin|deck of 52|how many degrees|hands of a clock|"
     r"angle of the hands|chickens lay",
     "The answer is usually a trick you either know or derive. Deriving it out loud is worth more "
     "than recalling it silently. "
     "• Method: restate the problem and the constraint in your own words first — most wrong "
     "answers come from misreading the constraint, not from bad logic. Then work a smaller version "
     "of the problem and generalise. "
     "• Common families worth knowing cold: doubling problems (if it covers the pond on day 60 it "
     "was half covered on day 59), weighing problems (each weighing splits the candidates in "
     "three, so three weighings cover 27), clock angles (the hour hand moves 0.5° a minute, which "
     "is why 3:15 is 7.5° and not 0°), and labelled-coin problems where you take a different "
     "number of coins from each source so the total weight identifies the odd one. "
     "• If you are stuck, say what you have established and what you are trying next. Silence is "
     "the only failing answer. "
     "• Traps: blurting a remembered answer without the reasoning, and refusing to start."),

    # ---- personality, logistics and tools ---------------------------------------------
    ("A playful hypothetical about you",
     r"if you (were|could be) (an?|one)|were to sponsor|which (animal|fruit|key|superhero)|"
     r"if you could (have dinner|bring one|choose 2|only save|be named)|"
     r"stranded on an island|three items|your life was a book|book about your life|"
     r"autobiography|headline|dinner with one person|guest speaker|"
     r"which three people, dead or alive|invite to dinner|if you die today|"
     r"to your grave|if you are a dictator|perfect day|personal beta|"
     r"8 ways to use a pencil|seven different ways|if you could be doing anything",
     "There is no right answer and they know it. They are testing whether you can be relaxed, "
     "quick and memorable under a question you cannot prepare precisely. "
     "• Structure: commit to a specific answer, give the reason in one or two sentences, and stop. "
     "The reason is the whole substance; the choice is just the hook. "
     "• Specific and slightly unexpected beats safe and generic. The interviewer is deciding "
     "whether they would mind sitting next to you at 2am. "
     "• Have two or three of these loosely prepared — they recur in a hundred variations. "
     "• Traps: refusing to answer, taking too long, anything political or divisive, and an answer "
     "engineered so transparently to flatter the firm that it stops being human."),

    ("Contributing to diversity and inclusion",
     r"foster(ing)? (an )?inclusi|contributions you have made to foster|diversity and inclusion|"
     r"what does diversity mean|commit to diversity|fostering dei|promoting these values|"
     r"worked with a diverse (group|team)|inclusive environment",
     "Several firms ask this one almost word for word, and it is scored on evidence, not on "
     "sentiment. "
     "\u2022 Structure: one concrete thing you did, who it affected and what changed. A specific "
     "small action beats a statement of belief every time. "
     "\u2022 What counts: recruitment outreach to a group that was not showing up, rewriting how "
     "a club picked its officers, mentoring a first-year student, making sure the quiet person in "
     "a group project was heard and their idea used. You do not need to have run a campaign. "
     "\u2022 If asked what diversity means to you, answer in terms of what it does for the work "
     "\u2014 different backgrounds catching assumptions a uniform team would miss \u2014 and "
     "then give the example anyway. "
     "\u2022 If the firm names it as a core value and asks how you would continue it here, name "
     "something an analyst could actually do: the campus pipeline you would keep, the network you "
     "would join. "
     "\u2022 Traps: abstractions with no action attached, claiming credit for a programme you "
     "merely attended, and treating the question as a box to tick."),
    ("A class, subject or your major",
     r"(difficult|toughest|hardest|favou?rite|least favou?rite) class|which class|"
     r"classes are you taking|academic subjects|what are you studying|"
     r"advantages and disadvantages of your major|what skills would you say your major|"
     r"what advantage does your major|explain the major|how does your major apply|"
     r"most interesting things you have learned in your classes|"
     r"tell me about one of your favou?rite classes|how do you like your school|"
     r"low and high points in high school|what are you exceptional at outside of academics",
     "Academic questions are rapport and reasoning questions, not a transcript review. "
     "\u2022 Structure: name the class, say in one sentence what made it hard or interesting, and "
     "spend the rest on how you handled it or what you took from it. The approach is the answer. "
     "\u2022 For a hard class: show method rather than suffering \u2014 how you worked out you "
     "were behind, what you changed, who you asked. That is the same skill they need in month one. "
     "\u2022 For a major outside finance: name the transferable skill concretely \u2014 writing "
     "under deadline, statistics, the discipline of a lab \u2014 rather than apologising for it. "
     "\u2022 Traps: calling a class useless or a professor bad, and naming a favourite class you "
     "cannot say anything specific about."),
    ("Hobbies and life outside work",
     r"hobb|passions and interests|something that interests you|balance your academics|"
     r"outside (of )?(work|the office|academics)|favou?rite (book|website|movie|app|class|"
     r"food|state)|what do you do for fun|fun fact|something personal about yourself|"
     r"not (listed |)on your resume|tell me something that will make me remember|"
     r"what sort of clubs|where do you like to (hang out|go hiking)|"
     r"balance your social life|what are you doing this (upcoming )?weekend|"
     r"geek out about|read (recently|lately)|book you",
     "These are rapport questions, and they are also a check that you are a person who will be "
     "bearable on a long night. "
     "• Structure: a real interest, one specific detail that proves it is real, and an opening for "
     "them to respond. Depth beats breadth — one genuine hobby discussed well is better than a "
     "list. "
     "• Anything on your resume under interests is fair game and will be asked about. Do not list "
     "something you cannot talk about for two minutes. "
     "• Traps: inventing a prestigious-sounding interest, answering 'work,' and giving a one-word "
     "answer that kills the conversation."),

    ("Excel, modelling and tools",
     r"\bexcel\b|bloomberg|shortcut|capiq|capital iq|factset|powerpoint|\bvba\b|macro|"
     r"vlookup|pivot table|how comfortable are you (with|at)|modell?ing (skill|experience)|"
     r"what (software|tools)|technical skills have you learned|how advanced are your|"
     r"math and technical skills",
     "Claim only what you can demonstrate, because the next question is often a live test. "
     "• Structure: name the tools, say what you built with them, then offer the detail. \"I built "
     "a three-statement model with a debt schedule in Excel; I work without a mouse and use "
     "INDEX/MATCH rather than VLOOKUP\" answers the question and the follow-up at once. "
     "• Worth knowing cold: F2 to edit, F4 for absolute references, Alt+= to sum, Ctrl+arrows to "
     "navigate, paste-special values, and why INDEX/MATCH beats VLOOKUP (it looks left and "
     "survives inserted columns). Know what #REF!, #N/A and #VALUE! each mean. "
     "• If you are weak, say what you are doing about it and by when. That answer is survivable; "
     "an inflated claim is not. "
     "• Traps: 'advanced' with nothing behind it, and listing a tool you last used once."),

    ("A technical question filed with the behavioral set",
     r"\bytm\b|ytc|ywt|bs equation|sources and uses|capped call|martingale|"
     r"mid-period adjustment|dividend recap|unrestricted subsidiary|non-guarantor|"
     r"\bpipe\b|general partner and a limited partner|strategic buyer or a financial sponsor|"
     r"how do public companies raise money|federal reserve's mandate|expense model|"
     r"purchase accounting|rule of 72|what adjustments|types of adjustments|"
     r"identical buildings in the same location|usd appreciation|waccs in general|"
     r"explain r square|eigenvalues|linear model|machine learning|how ai models work",
     "This is a technical question that arrived in the behavioral set, usually because the "
     "interview mixed the two. Answer it as a technical question, not with a story. "
     "\u2022 Expect this. Fit interviews routinely turn technical without warning, and the "
     "switch itself is part of the test \u2014 they want to see whether you can change register "
     "cleanly. "
     "\u2022 The technical deck in this app covers the underlying concepts; search it for the term "
     "in the question rather than improvising. "
     "\u2022 If you do not know it, say so in one sentence, then reason out loud from what you do "
     "know. A structured attempt scores; a confident wrong answer does not, because the follow-up "
     "will find it. "
     "\u2022 Traps: bluffing a definition, and answering a technical question with a behavioral "
     "story because that is what you prepared."),
    ("Logistics and process questions",
     r"willing to relocate|when can you start|what times are you free|available to meet|"
     r"where are you in (your other|the interview)|other (firms|offers)|received (any )?offers|"
     r"where else are you interviewing|which other (investment banks|jobs)|"
     r"are you just looking at|how did you (prepare for|find out about) (this|the) interview|"
     r"who have you spoken to|where did you get your technical answers",
     "Short, factual questions. The only way to lose points is to over-explain or to be caught "
     "out. "
     "• On other processes: be truthful without giving a full list. \"I'm in final rounds at two "
     "other banks, both in similar groups\" is honest and keeps the focus here. Saying you have no "
     "other processes is fine too. "
     "• On start dates, relocation and availability: be precise and say yes if it is true. "
     "Hedging on logistics creates a doubt that is expensive to remove. "
     "• On who you have spoken to: name them, and make sure the conversation actually happened. "
     "They will check. "
     "• Traps: inventing a competing offer to create leverage, and treating a scheduling question "
     "as an opportunity to pitch yourself again."),
]


BEHAV_GUIDE_PATTERNS = [(name, re.compile(pat, re.I), text) for name, pat, text in BEHAV_GUIDES]


def _breaks(text):
    """Put a real paragraph break before each bullet.

    The page splits on authored blank lines when it finds them and falls back to a
    sentence heuristic when it does not. The heuristic gives a bullet exactly one
    sentence, which breaks the guidance bullets that run to two or three. Authoring
    the breaks removes the guesswork for this text without touching the technical
    answers, where the heuristic still does the right thing.
    """
    return text.replace(" \u2022 ", "\n\n\u2022 ")


BARE_WHY = re.compile(r"^\s*why\s+([A-Za-z][\w&.'\- ]{1,30})\s*\??\s*$", re.I)


def behav_guidance(question, topic):
    """Guidance for this kind of question, falling back to the topic framework.

    First match wins, so BEHAV_GUIDES is ordered narrow to broad.
    """
    # "Why Walmart?" names a firm, so it is a why-this-firm question even though nothing
    # in the wording says so. Checked against the firm list rather than guessed at.
    m = BARE_WHY.match(question)
    if m and m.group(1).strip().lower() in {f.lower() for f in FIRMS}:
        for name, pat, text in BEHAV_GUIDE_PATTERNS:
            if name == "Why this firm":
                return name, text
    for name, pat, text in BEHAV_GUIDE_PATTERNS:
        if pat.search(question):
            return name, _breaks(text)
    return None, _breaks(BEHAV_FRAMEWORKS[topic])



DROP_NOTES = (
    "Transcribed from the supplied guide; retain its stated assumptions.",
)


def clean_notes(notes):
    """Drop boilerplate notes that only repeat provenance."""
    return [n for n in (notes or [])
            if not any(n.startswith(d) for d in DROP_NOTES)]


# ------------------------------------------------------ sentence case ----
# The source questions are transcriptions, so a few carry a bare "i", a
# lower-cased word after a full stop, or a finance term in lower case. These
# fix presentation only; the source files are never rewritten.

ACRONYMS = {
    "ebitda": "EBITDA", "ebit": "EBIT", "ebiat": "EBIAT", "dcf": "DCF", "lbo": "LBO",
    "wacc": "WACC", "irr": "IRR", "moic": "MOIC", "ipo": "IPO", "capex": "CapEx",
    "cogs": "COGS", "roe": "ROE", "roic": "ROIC", "roa": "ROA", "gaap": "GAAP",
    "ifrs": "IFRS", "reit": "REIT", "saas": "SaaS", "nwc": "NWC", "fcf": "FCF",
    "fcff": "FCFF", "fcfe": "FCFE", "pik": "PIK", "nol": "NOL", "dta": "DTA",
    "dtl": "DTL", "ddm": "DDM", "tev": "TEV", "arr": "ARR", "cagr": "CAGR",
    "ceo": "CEO", "cfo": "CFO", "ipos": "IPOs",
}
ABBREV = re.compile(
    r"\b(?:vs|e\.g|i\.e|etc|approx|no|fig|est|ex|mr|ms|dr|inc|co|corp|ltd|u\.s|u\.k|jr|sr)$",
    re.I)


PARA = "\x00PARA\x00"


def tidy_punctuation(text):
    """Repair transcription artefacts: stray spacing and welded-together questions.

    A deliberate blank line between paragraphs survives; runs of ordinary
    whitespace do not.
    """
    if not text:
        return text
    # protect author-intended paragraph breaks from the whitespace collapse below
    text = re.sub(r"\n[ \t]*\n\s*", PARA, text)
    # "pitchbook., Which is higher" - two questions joined by a stray comma
    text = re.sub(r"([a-z])([.?!]),\s+([A-Z])", r"\1\2 \3", text)
    # "private company ?" / "Fintech ?"
    text = re.sub(r"\s+([,?!;:]|\.(?!\d))", r"\1", text)
    # "5x....what" - keep the ellipsis, drop the extra stops
    text = re.sub(r"\.{4,}", "...", text)
    text = re.sub(r"\s{2,}", " ", text).strip()
    return text.replace(PARA, "\n\n").strip()


def tidy_case(text, firms=FIRMS):
    """Capitalise sentence starts, the pronoun I, finance acronyms and firm names."""
    if not text:
        return text

    # the pronoun, but never the "i" of "i.e."
    text = re.sub(r"(?<![\w.])i(?=[\s,])", "I", text)

    # a lower-case word straight after a full stop, question mark or exclamation
    def after_stop(m):
        before = text[:m.start()]
        if ABBREV.search(before):
            return m.group(0)
        return m.group(1) + m.group(2).upper()
    text = re.sub(r"([.?!]\s+)([a-z])", after_stop, text)

    # finance terms written in lower case (an already-capitalised one is left alone)
    text = re.sub(
        r"\b(" + "|".join(sorted(ACRONYMS, key=len, reverse=True)) + r")\b",
        lambda m: ACRONYMS[m.group(0).lower()] if m.group(0).islower() else m.group(0),
        text)

    # firm names as the source spells them
    for f in firms:
        if len(f) < 5 or " " in f:
            continue
        text = re.sub(r"\b" + re.escape(f) + r"\b",
                      lambda m, f=f: f if m.group(0) != f else m.group(0), text, flags=re.I)

    # "a EBITDA multiple" reads wrong once the acronym is capitalised: these are
    # the ones said with a leading vowel sound.
    text = re.sub(r"\b([Aa])\s+(EBITDA|EBIT|EBIAT|IPO|IRR|LBO|NOL|ROE|ROA|ROIC|ARR|FCFF|FCFE|FCF|NWC|IFRS|EV)\b",
                  lambda m: ("An " if m.group(1) == "A" else "an ") + m.group(2), text)

    # and the opening letter, only when the question actually starts with one
    # ("$150 par value" and "1st round" must stay as they are)
    if text[:1].isalpha() and text[:1].islower():
        text = text[0].upper() + text[1:]
    return text


# ---------------------------------------------------- card integrity ----
# These check the SHAPE of a card: is the prompt self-contained, and does the
# card carry a specific answer? They do not check whether the finance in the
# answer is correct.

INCOMPLETE_PAT = re.compile(
    r"\[[^\]]*(not recorded|not identified|not specified|not given|missing|unclear|unknown)[^\]]*\]", re.I)

DANGLING_PAT = re.compile(
    r"\b(this|that) (company|firm|stock|trend|deal|business|article|case|transaction|fund|industry|product)\b"
    r"|\bthe (deal|stock|company|case|trend|article) (you|we|just|above|mentioned|discussed|pitched)"
    r"|\byou (just )?(mentioned|discussed|pitched)\b"
    r"|\bthe supplied (case|company|data)\b"
    r"|\bin the case\b|\bthe case study\b", re.I)

INSTRUCTION_VERBS = re.compile(
    r"\b(calculat|comput|find|determin|walk|explain|value|rank|estimat|forecast|discuss|describ|"
    r"assess|evaluat|build|deriv|solv|prove|compar|list|name|pitch|tell|show|analy[sz]|"
    r"work out|go through)", re.I)

TIME_PAT = re.compile(
    r"\b(current(?! (assets?|liabilit|portion|ratio|maturit))|currently|today|right now|"
    r"this (year|quarter|week)|latest|recent(ly)?|"
    r"at the moment|these days)\b|\boutlook\b|where (do you see|are) .*(rates|markets|economy)", re.I)


def looks_like_question_set(text):
    """A list of separate interview prompts crammed into one card (e.g. F0942)."""
    if "?" in text or INSTRUCTION_VERBS.search(text):
        return False
    parts = [p.strip() for p in re.split(r"[,;]", text) if p.strip()]
    if len(parts) < 3:
        return False
    # a worked case states numbers in several of its clauses; an interview list does not
    if sum(1 for p in parts if re.search(r"\d", p)) >= 2:
        return False
    bare = sum(1 for p in parts
               if not re.search(r"\b(is|are|was|were|do|does|did|would|should|can|will|have|has)\b", p, re.I))
    return bare >= 3


def card_issues(question, answer, status, is_behavioral):
    """Structural defects, most serious first. An empty list means usable as written."""
    issues = []
    if INCOMPLETE_PAT.search(question):
        issues.append("Incomplete prompt")
    if looks_like_question_set(question):
        issues.append("Question set")
    if DANGLING_PAT.search(question):
        issues.append("Input Required")
    if is_behavioral:
        return issues
    if status == "requires_missing_inputs" and "Incomplete prompt" not in issues:
        issues.append("Missing inputs")
    if status == "requires_dated_research" or TIME_PAT.search(question):
        issues.append("Needs fresh research")
    if status == "open_ended_framework":
        issues.append("No single right answer")
    return issues


SERIOUS = {"Incomplete prompt", "Question set", "Input Required", "Missing inputs",
           "Not a question"}

# Cards reviewed by hand and cleared: the structural heuristics flagged them, a human
# read them and judged them askable as written. An id here gets no issues and reads as
# Verified. Keep it sorted and only add an id you have actually read.
CLEARED_ISSUES = {
    "F0021", "F1939", "F1941", "F1946", "F1950", "F1962",
    "F1967", "F1991", "F2010", "F2011", "F2020", "F2021",
    "F2027", "F2031", "F2033", "F2034", "F2039", "F2043",
    "F2080", "F2082", "F2084", "F2085", "F2117", "F2122",
    "F2136", "F2137", "F2169", "F2179", "F2191", "F2253",
}


TECH_TOPIC_NAMES = {name for name, _ in TECH_TOPIC_RULES}


def classify(text, rules, default):
    low = text.lower()
    for name, pat in rules:
        if re.search(pat, low):
            return name
    return default


# The USF interview workbooks record a "General Area" per firm. A source label carrying
# the USF tag maps straight from that area to a group, rather than being guessed from
# keywords in the label - "BMO Capital Markets" is a firm name, not a capital-markets desk.
USF_TAG = "(usf 24-25)"
USF_AREA_GROUP = {
    "investment banking": "M&A / Generalist",
    "equity research": "Research",
    "private equity": "Private Equity & Growth",
    "asset management": "Asset & Wealth Management",
    "wealth management": "Asset & Wealth Management",
    "private banking": "Asset & Wealth Management",
    "financial planning": "Asset & Wealth Management",
    "sales & trading": "Markets & Trading",
    "capital markets": "Equity Capital Markets",
    "commercial banking": "Credit & Leveraged Finance",
    "consulting": "Consulting",
    "operations & risk": "Operations & Risk",
    "corporate finance": "Corporate Finance",
}

def groups_for(sources, text):
    out = []
    for s in sources:
        low = s.lower()
        if USF_TAG in low:
            m = re.search(r"\u2014\s*(.+?)\s*\(usf", low)
            g = USF_AREA_GROUP.get(m.group(1).strip()) if m else None
            if g and g not in out:
                out.append(g)
            continue
        for name, keys in GROUP_BY_LABEL:
            if any(k in low for k in keys) and name not in out:
                out.append(name)
    low_t = text.lower()
    for name, pat in GROUP_BY_TEXT:
        if name not in out and re.search(pat, low_t):
            out.append(name)
    if not out:
        out = [GENERALIST]
    return out


def difficulty(question, answer, topic, is_guide):
    q = question
    score = 0
    if ADV_PAT.search(q) or ADV_PAT.search(answer[:600]):
        score += 2
    if NUM_PAT.search(q):
        score += 1
    if len(q) > 150:
        score += 1
    if len(answer) > 1100:
        score += 1
    if topic in ("LBO & Private Equity", "Accretion / Dilution", "Merger Model & M&A"):
        score += 1
    if BASIC_PAT.match(q.strip()):
        score -= 2
    if is_guide and len(q) < 110:
        score -= 1
    return "Advanced" if score >= 2 else "Basic"


def main():
    with open(TECH_JSON) as fh:
        tech = json.load(fh)

    cards = []
    for q in tech["questions"]:
        sources = q.get("question_sources") or []
        firm_srcs = [s for s in sources if not s.startswith(GUIDE_SOURCE)]
        is_guide = any(s.startswith(GUIDE_SOURCE) for s in sources) or \
            q.get("answer_status") == "guide_answer"
        firms = sorted({f for f in (parent_firm(s) for s in firm_srcs) if f})
        q["question"] = tidy_case(tidy_punctuation(q["question"]))
        text = q["question"] + " " + (q.get("answer") or "")
        # A stored topic that names a real topic is a deliberate choice by whoever
        # wrote the card, so it wins. The keyword rules are for the cards that say
        # nothing, and they cannot tell a brainteaser from a deal teaser.
        stored = q.get("topic", "")
        topic = stored if stored in TECH_TOPIC_NAMES else classify(
            q["question"] + " " + stored, TECH_TOPIC_RULES, "Industry & Company Analysis")
        ans = q.get("answer") or ""
        collections = []
        if is_guide:
            collections.append("IB Fundamentals (M&I 400)")
        if firm_srcs:
            collections.append("Firm Interview Insights")
        if not collections:
            collections.append("IB Fundamentals (M&I 400)")
        issues = ([] if q["question_id"] in CLEARED_ISSUES
                  else card_issues(q["question"], ans, q.get("answer_status", ""), False))
        verified = not issues
        cards.append({
            "id": q["question_id"],
            "t": "Technical",
            "vf": "Verified" if verified else "Not verified",
            "iss": issues,
            "ser": bool(SERIOUS & set(issues)),
            "q": q["question"],
            "a": ans,
            "tp": topic,
            "d": difficulty(q["question"], ans, topic, is_guide),
            "f": firms,
            "g": groups_for(sources, text),
            "c": collections,
            "st": q.get("answer_status", ""),
            "ao": q.get("answer_origin", ""),
            "sr": sources,
            "nt": clean_notes(q.get("notes")),
            "ur": q.get("supporting_reference_urls") or [],
        })

    # ---- behavioral ----
    with open(BEHAV_TXT) as fh:
        btxt = fh.read()
    blocks = re.findall(r"^(B\d{4})\.\s+(.+?)\nSources:\s*(.+?)\s*$",
                        btxt, re.M | re.S)
    for bid, question, src in blocks:
        question = tidy_case(tidy_punctuation(" ".join(question.split())))
        sources = [s.strip() for s in src.split(";") if s.strip()]
        firm_srcs = [s for s in sources if not s.startswith(GUIDE_SOURCE)]
        is_guide = any(s.startswith(GUIDE_SOURCE) for s in sources)
        firms = sorted({f for f in (parent_firm(s) for s in firm_srcs) if f})
        topic = classify(question, BEHAV_TOPIC_RULES, "General Fit")
        collections = []
        if is_guide:
            collections.append("IB Fundamentals (M&I 400)")
        if firm_srcs:
            collections.append("Firm Interview Insights")
        bissues = card_issues(question, "", "", True)
        if bid in NOT_A_QUESTION:
            bissues = ["Not a question"]
        elif bid in UNSOLVABLE and "Incomplete prompt" not in bissues:
            bissues = bissues + ["Incomplete prompt"]
        guide_name, guidance = behav_guidance(question, topic)
        cards.append({
            "id": bid,
            "t": "Behavioral",
            "vf": "Verified" if not bissues else "Not verified",
            "iss": bissues,
            "ser": bool(SERIOUS & set(bissues)),
            "q": question,
            "a": guidance,
            "tp": topic,
            "d": "Advanced" if len(question) > 110 else "Basic",
            "f": firms,
            "g": groups_for(sources, question),
            "c": collections or ["Firm Interview Insights"],
            "st": "preparation_framework",
            "ao": "Preparation framework written for this app — not a model answer, "
                  "and not supplied by the named firms. Your answer must be your own.",
            "sr": sources,
            "nt": [],
            "ur": [],
            "gd": guide_name or "",
        })

    def facet(key):
        c = Counter()
        for card in cards:
            v = card[key]
            for x in (v if isinstance(v, list) else [v]):
                c[x] += 1
        return c

    meta = {
        "built": tech["metadata"].get("prepared_on"),
        "total": len(cards),
        "technical": sum(1 for c in cards if c["t"] == "Technical"),
        "behavioral": sum(1 for c in cards if c["t"] == "Behavioral"),
        "sourceMaterial": tech["metadata"].get("source_material", []),
        "attribution": tech["metadata"].get("attribution_note", ""),
        "facets": {
            "firms": facet("f").most_common(),
            "groups": facet("g").most_common(),
            "topics": facet("tp").most_common(),
            "collections": facet("c").most_common(),
            "difficulty": facet("d").most_common(),
            "verification": facet("vf").most_common(),
            "issues": facet("iss").most_common(),
        },
    }

    payload = {"meta": meta, "cards": cards}
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    with open(OUT, "w") as fh:
        fh.write(blob)
    # data.js lets index.html open straight from the filesystem (no server, no CORS)
    with open(os.path.join(SITE, "data.js"), "w") as fh:
        fh.write("window.DECK=" + blob + ";\n")

    print(f"wrote {OUT}  {os.path.getsize(OUT)/1e6:.2f} MB  {len(cards)} cards")
    for k, v in meta["facets"].items():
        print(f"\n{k}: {len(v)}")
        print("  " + ", ".join(f"{n}({c})" for n, c in v[:14]))


if __name__ == "__main__":
    main()
