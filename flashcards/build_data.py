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

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
TECH_JSON = os.path.join(SRC, "Technical_Questions_and_Answers.json")
BEHAV_TXT = os.path.join(SRC, "IB_Behavioral_Questions.txt")
OUT = os.path.join(HERE, "data.json")

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
    ("Deal & Process", r"pitch book|cim\b|teaser|nda\b|data room|lbo model|build a model|model(ing)? (a|the)|process|timeline|roadshow|ipo\b|follow-?on|bookbuild"),
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


DROP_NOTES = (
    "Transcribed from the supplied guide; retain its stated assumptions.",
)


def clean_notes(notes):
    """Drop boilerplate notes that only repeat provenance."""
    return [n for n in (notes or [])
            if not any(n.startswith(d) for d in DROP_NOTES)]


def classify(text, rules, default):
    low = text.lower()
    for name, pat in rules:
        if re.search(pat, low):
            return name
    return default


def groups_for(sources, text):
    out = []
    for s in sources:
        low = s.lower()
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
        text = q["question"] + " " + (q.get("answer") or "")
        topic = classify(q["question"] + " " + q.get("topic", ""),
                         TECH_TOPIC_RULES, "Industry & Company Analysis")
        ans = q.get("answer") or ""
        collections = []
        if is_guide:
            collections.append("IB Fundamentals (M&I 400)")
        if firm_srcs:
            collections.append("Firm Interview Insights")
        if not collections:
            collections.append("IB Fundamentals (M&I 400)")
        cards.append({
            "id": q["question_id"],
            "t": "Technical",
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
        question = " ".join(question.split())
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
        cards.append({
            "id": bid,
            "t": "Behavioral",
            "q": question,
            "a": BEHAV_FRAMEWORKS[topic],
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
        },
    }

    payload = {"meta": meta, "cards": cards}
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    with open(OUT, "w") as fh:
        fh.write(blob)
    # data.js lets index.html open straight from the filesystem (no server, no CORS)
    with open(os.path.join(HERE, "data.js"), "w") as fh:
        fh.write("window.DECK=" + blob + ";\n")

    print(f"wrote {OUT}  {os.path.getsize(OUT)/1e6:.2f} MB  {len(cards)} cards")
    for k, v in meta["facets"].items():
        print(f"\n{k}: {len(v)}")
        print("  " + ", ".join(f"{n}({c})" for n, c in v[:14]))


if __name__ == "__main__":
    main()
