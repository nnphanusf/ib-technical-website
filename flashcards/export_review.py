"""Export the technical bank in two human-readable shapes for proofreading.

Reads the source of truth, Technical_Questions_and_Answers.json, and writes:

  - Technical_Questions_and_Answers.txt  every question with its answer, to read
                                         straight through. Regenerated in place.
  - review/all_questions.csv             the same content one row per card, with
                                         the page's flags, to sort and filter.

Run it after build_data.py, because the CSV's flag columns come from the built
data.json. Nothing reads either output; they exist to be read by a person.
"""

import csv
import datetime
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
TECH_JSON = os.path.join(SRC, "Technical_Questions_and_Answers.json")
DATA_JSON = os.path.join(HERE, "data.json")
TXT = os.path.join(SRC, "Technical_Questions_and_Answers.txt")
REVIEW = os.path.join(SRC, "review")
CSV_OUT = os.path.join(REVIEW, "all_questions.csv")

RULE = "-" * 88
BANNER = "=" * 88

# The .txt spells out each answer_status. Keep these exact: the file has been read
# in this wording, and a silent relabel would look like a change of substance.
STATUS_LABEL = {
    "concept_and_method": "Concept explanation / method",
    "model_answer": "Prepared model answer",
    "guide_answer": "Guide answer",
    "open_ended_framework": "Open-ended answer framework",
    "requires_dated_research": "Framework — dated research required",
    "requires_missing_inputs": "Method / conditional answer — source details needed",
}

# Where the regenerated entries start, and where the preserved tail begins. Both the
# header prose and the scope appendix are written by hand and live only in the .txt,
# so they are carried across verbatim rather than rebuilt.
ENTRIES_HEADING = "QUESTIONS AND ANSWERS"
APPENDIX_HEADING = "SCOPE APPENDIX"


def load_questions():
    with open(TECH_JSON) as fh:
        return json.load(fh)["questions"]


def load_flags():
    """Card flags as the page computes them, keyed by id. Absent is not an error:
    the CSV simply leaves those columns empty if data.json has not been built."""
    if not os.path.exists(DATA_JSON):
        return {}
    with open(DATA_JSON) as fh:
        return {c["id"]: c for c in json.load(fh)["cards"]}


def split_header_and_appendix():
    """The .txt's hand-written head and tail, so a regeneration keeps both."""
    with open(TXT) as fh:
        lines = fh.read().split("\n")
    head, tail = [], []
    for i, line in enumerate(lines):
        if line.startswith(ENTRIES_HEADING):
            head = lines[: i + 1]
            break
    else:
        raise SystemExit("cannot find the '%s' heading in %s" % (ENTRIES_HEADING, TXT))
    for i, line in enumerate(lines):
        if line.startswith(APPENDIX_HEADING):
            tail = lines[i:]
            break
    return head, tail


def refresh_counts(head, questions):
    """Rewrite the two places in the header that state a count, and the date."""
    text = "\n".join(head)
    today = datetime.date.today().strftime("%d %B %Y").lstrip("0")
    text = re.sub(r"^Prepared: .*$", "Prepared: " + today, text, flags=re.M)

    originals = sum(len(q.get("original_question_ids") or [q["question_id"]]) for q in questions)
    text = re.sub(
        r"^[\d,]+ entries covering [\d,]+ original finance-question IDs\.$",
        "{:,} entries covering {:,} original finance-question IDs.".format(
            len(questions), originals),
        text, flags=re.M)

    counts = {}
    for q in questions:
        counts[q.get("answer_status", "")] = counts.get(q.get("answer_status", ""), 0) + 1
    coverage = "\n".join("- %s: %d" % (k.replace("_", " "), counts[k])
                         for k in sorted(counts, key=lambda k: -counts[k]))
    text = re.sub(r"(?<=^ANSWER COVERAGE\n)(?:- .*\n)+", coverage + "\n",
                  text, flags=re.M)
    return text


def entry_block(q):
    """One question in the .txt's layout."""
    out = []
    # a question with author paragraph breaks keeps them, on their own lines
    paras = [p.strip() for p in q["question"].split("\n\n") if p.strip()]
    out.append("[%s] %s" % (q["question_id"], paras[0]))
    out.extend(paras[1:])

    sources = q.get("question_sources") or []
    if sources:
        out.append("Asked by / question source: " + "; ".join(sources))

    also = [i for i in (q.get("original_question_ids") or []) if i != q["question_id"]]
    if also:
        out.append("Also covers: " + ", ".join(also))

    status = q.get("answer_status", "")
    out.append("Answer status: " + STATUS_LABEL.get(status, status))
    if q.get("answer_origin"):
        out.append("Answer origin: " + q["answer_origin"])

    out.append("")
    out.append("ANSWER:")
    out.append(q.get("answer", "").strip())
    for url in q.get("supporting_reference_urls") or []:
        out.append("Supporting reference: " + url)
    return "\n".join(out)


def write_txt(questions):
    head, tail = split_header_and_appendix()
    parts = [refresh_counts(head, questions), BANNER, ""]
    for q in questions:
        parts.append(entry_block(q))
        parts.append("")
        parts.append(RULE)
        parts.append("")
    parts.extend(tail)
    with open(TXT, "w") as fh:
        # the tail keeps its own trailing blank line, so join as-is
        fh.write("\n".join(parts) + "\n")
    return len(questions)


def write_csv(questions, flags):
    if not os.path.isdir(REVIEW):
        os.makedirs(REVIEW)
    cols = ["id", "topic", "difficulty", "answer_status", "answer_origin", "verified",
            "flags", "also_covers", "firms", "question", "answer", "notes", "references"]
    with open(CSV_OUT, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for q in questions:
            card = flags.get(q["question_id"], {})
            also = [i for i in (q.get("original_question_ids") or []) if i != q["question_id"]]
            w.writerow([
                q["question_id"],
                card.get("tp", q.get("topic", "")),
                card.get("d", ""),
                q.get("answer_status", ""),
                "guide" if "guide" in (q.get("answer_origin") or "").lower() else "prepared",
                card.get("vf", ""),
                "; ".join(card.get("iss", [])),
                ", ".join(also),
                "; ".join(q.get("question_sources") or []),
                # the CSV is one row per card, so paragraph breaks flatten to spaces
                " ".join(q["question"].split()),
                " ".join((q.get("answer") or "").split()),
                " ".join("; ".join(q.get("notes") or []).split()),
                "; ".join(q.get("supporting_reference_urls") or []),
            ])
    return len(questions)


def main():
    questions = load_questions()
    flags = load_flags()
    n_txt = write_txt(questions)
    n_csv = write_csv(questions, flags)
    print("Technical_Questions_and_Answers.txt  %d entries" % n_txt)
    print("review/all_questions.csv             %d rows" % n_csv)
    if not flags:
        print("note: data.json not found, so the flag columns are empty")


if __name__ == "__main__":
    main()
