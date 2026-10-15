# IB Interview Prep

Source question bank and the flashcard app built from it.

| Path | What it is |
| --- | --- |
| `flashcards/` | The flashcard web app — open `flashcards/index.html`, or see [flashcards/README.md](flashcards/README.md) |
| `Technical_Questions_and_Answers.json` | 2,049 technical Q&A with firm sources, answer status and merged IDs — the app's input |
| `Technical_Questions_and_Answers.txt` | The same material as a readable document |
| `Investment_Banking_Questions.txt` | 3,440 consolidated questions (1,185 behavioral, 2,255 finance) with source labels |
| `M&I 2025 400 IB Questions-2.pdf` | Guide used as source material |

Rebuild the deck after editing the sources or the tagging rules:

```bash
cd flashcards && python3 build_data.py
```

Keep this repository private. The question bank is derived from a paid guide and from
private interview notes; publishing it would redistribute someone else's material.
