# Behavioral deck — guidance rewrite

All 1,185 behavioral cards were read in full. The finding is not that the guidance was wrong;
it is that there was almost none of it, and that what existed was attached to the wrong thing.

## What was there before

| | Before | After |
| --- | ---: | ---: |
| Behavioral cards | 1,185 | 1,185 |
| **Distinct guidance texts** | **12** | **58** |
| Cards sharing one generic STAR block | 549 | 0 |
| Cards with guidance for their own question type | 0 | 854 (72%) |
| Median guidance length | 410 chars | 652 chars |

Every behavioral answer was `BEHAV_FRAMEWORKS[topic]` — a single block of text keyed only to the
card's topic. With twelve topics, 1,185 distinct questions shared twelve answers. A student
working through the deck met the same paragraph 549 times.

Worse than the repetition, the fallback was often **wrong for the question**. The 549 cards on the
generic STAR block included "What's your greatest weakness?", "Do you have any questions for me?",
"Who is the CEO of BlackRock?" and "What is 7 cubed?" — none of which is a STAR story. The deck was
telling students to answer a mental-arithmetic question with Situation, Task, Action, Result.

The clearest single failure: roughly 25 **defensive** questions — "Why is your college GPA low?",
"Why did you quit after you were promoted twice?", "Why didn't you win an offer last year?",
"Why should we pick a candidate from a non-target?" — were routed to the *Why Banking / Why Firm*
framework, which opens "Three parts, 45–60 seconds. The path: what in your background pulled you
toward this work." That is confident, cheerful advice for the questions where a student is most
exposed and most likely to ramble.

## What replaced it

**46 question-level families**, matched on the question's own wording and ordered narrow to broad,
with the twelve topic frameworks kept as the floor. Each family follows the same shape as the
technical deck's rewritten answers — a line of framing, then labelled bullets — so the two halves
of the app now read alike and the bullets render as separate paragraphs.

Each family says what the question is actually testing, the structure to use, what makes an answer
strong, and the specific trap. For example, the GPA family now tells a student to state the number
plainly, give one reason in a sentence, and spend the rest on evidence — an upward trend, a higher
major GPA, a job carried alongside the course load — and warns against blaming a professor or
volunteering a number nobody asked for.

The families, by what they serve:

- **Questions that put you on the back foot** (7): low or missing GPA, a resume gap, why you left
  or did not return, non-target school, switching careers, doubts about commitment, "give us a
  reason not to hire you."
- **The why family** (6): why this firm, this city, this group, why not the other path, why your
  school or major, and why banking itself.
- **Fit and self-assessment** (7): tell me about yourself, weakness, strengths, three words, career
  goals, proudest achievement, what motivates you.
- **Story questions by what the story must prove** (8): failure, conflict, leadership, teamwork,
  pressure and prioritisation, an ethical dilemma, learning fast, plus a general "tell me about a
  time."
- **Hypothetical judgement** (1), kept deliberately separate from the story families: there is no
  past story to tell, so the answer is a principle, a first action, and who you tell.
- **Research and role** (3): what you know about the firm, what the job actually involves, and
  questions for them.
- **Markets, deals and sectors** (5): your own deal, a deal the firm advised, a market view, a
  sector you follow, current events, plus a stock pitch.
- **Quantitative** (3): mental arithmetic, market sizing, logic puzzles — each with worked technique
  rather than encouragement.
- **The rest** (6): playful hypotheticals, hobbies, classes and your major, Excel and tools,
  logistics, and technical questions that were filed with the behavioral set.

331 cards still fall back to a topic framework. These are mostly one-off questions with no family to
join, and a correct general framework is better than a specific wrong one — which is why the GPA
family was narrowed after it was caught claiming "Tell me about a difficult class you have taken"
as a grade question.

## Three defects found while reading

**1. "TMT" was expanded as if it were "TMAAT".** Six questions had the sector name replaced with the
shorthand for *tell me about a time*, which left nonsense on the card:

> Which two Tell me about a time companies should merge?
> How does one amortize Tell me about a time subscriptions?
> Where is the Tell me about a time industry heading, and what catalysts affect major companies?

Fixed in `IB_Behavioral_Questions.txt`: B0110, B0645, B0646, B0652, B0838, B0982 now read TMT.

**2. Nineteen cards are not questions.** The source captured a candidate's commentary about their
own interview, or half of a prompt whose other half is on a different card, and the deck presented
each one as a question with a STAR framework attached:

> If anything, 1 was surprised by the lack of technicals.
> Who can read English will be able to understand it.
> If you take the outside shell of, it becomes an 8x8x8 cube.

These now carry a **Not a question** flag and read as Not verified, so a student can filter them
out. The list is hand-checked, in `NOT_A_QUESTION` in `build_data.py`; add an id only after reading
it.

**3. Technical questions are filed in the behavioral set.** "Walk me through the BS Equation",
"What is YTM, YTC and YTW?", "What is a mid-period adjustment?", "What is a capped call?" and about
twenty more sit in the behavioral file. They are not errors — fit interviews do turn technical
without warning — but they were getting a STAR framework. They now get a family that says so,
tells the student to answer it as a technical question and to search the technical deck for the
term, and makes the point that the switch of register is itself part of what is being tested.

## What this does not cover

The guidance is preparation framework, not model answers, and the card footer still says so: a
behavioral answer has to be the student's own. Nothing here invents an experience for them.

Two things were deliberately left alone. The topic router still files about 300 cards under
*General Fit*, which is a filtering problem rather than a guidance one now that those cards get
question-level guidance regardless of topic. And a cluster of questions carries dangling references
— "How do you incorporate these actions into your daily routine?", "What steps were taken to manage
the situation?" — where the antecedent was lost in transcription. The existing *Input Required*
flag catches some but not all of them; a pass over those is a separate job.
