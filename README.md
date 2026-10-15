# Banking Interview Prep Website

Source question bank and the flashcard app built from it.

**Live site:** https://nnphanusf.github.io/new-folder/flashcards/ (the repo root redirects there)

| Path | What it is |
| --- | --- |
| `flashcards/` | The flashcard web app — open `flashcards/index.html`, or see [flashcards/README.md](flashcards/README.md) |
| `Technical_Questions_and_Answers.json` | 2,049 technical Q&A with firm sources, answer status and merged IDs — the app's input |
| `Technical_Questions_and_Answers.txt` | The same material as a readable document |
| `IB_Behavioral_Questions.txt` | 3,440 consolidated questions (1,185 behavioral, 2,255 finance) with source labels |
| `M&I 2025 400 IB Questions-2.pdf` | Guide used as source material |

Rebuild the deck after editing the sources or the tagging rules:

```bash
cd flashcards && python3 build_data.py
```

This repository is public so GitHub Pages can serve the deck. That also makes the question
bank and the source PDF publicly readable — both are derived from a paid guide and from private
interview notes. Making the repo private stops that, at the cost of the Pages site.
