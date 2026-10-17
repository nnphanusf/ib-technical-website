# Brainteasers moved from the behavioral deck to the technical deck

Every behavioral card was checked for quantitative content. **100 were brainteasers or maths
questions and are now technical cards with worked solutions.** The deck total is unchanged at
3,318: technical goes from 2,067 to 2,167, behavioral from 1,251 to 1,151.

| | |
| --- | ---: |
| Candidates examined | 119 |
| **Moved with a worked solution** | **100** |
| — exact answers (arithmetic, logic, probability) | 62 |
| — estimation, worked with stated assumptions | 38 |
| Left in the behavioral deck | 19 |
| Quant & Brainteasers topic | 110 cards (was 10) |

The two you named are in: the lily pad is F2546 and the 15:15 clock angle is F2587.

## What moved

**Mental arithmetic (27).** 7 cubed, 9^3, 432 x 63, the square roots, 3% of 113, the sum of 1 to
100. Each answer gives the number *and the route*, because the route is what an interviewer is
listening for: 21 x 19 is the difference of two squares, 400 - 1 = 399; 25 cubed is "times 100,
divided by 4"; 49 x 63 is 50 x 63 less 63. Every value was computed and checked before it was
written.

**Logic and probability (35).** The pirates, the balance-scale weighings, the burning ropes, the
jugs, the light bulbs, the lily pads, the clock angles, three aces from a deck, the correlated
coins, the two-jar marble problem, the knights at the doors.

Three of these are worth flagging because the obvious answer is wrong:

- **The 15:15 clock angle is 7.5 degrees, not zero.** Both hands look like they are on the 3, but
  the hour hand has drifted a quarter of the way to the 4.
- **1.5 chickens laying 1.5 eggs in 1.5 days gives 6 eggs** from 3 chickens in 3 days, not 3.
  Doubling both inputs quadruples the chicken-days.
- **The three-hands-on-a-clock question is twice a day, not 22.** The hour and minute hands meet 22
  times, but only the two meetings at 12 o'clock fall on an exact whole minute where the second hand
  can join them.

**Estimation (38).** Market sizing and packing problems — ATMs, barbers, gas stations, golf balls in
a 737, pennies in a city, potholes in New York. These are filed as *concept and method* rather than
model answers, because the number is not the point. Each gives a worked chain, a cross-check where
one exists, and a line saying which assumption the answer is most sensitive to. The Oreo estimate
checks itself against retail revenue; the pregnancy estimate works from the birth rate rather than
the population, because that anchors on a number you can actually reason about.

Technical already held estimation cards under Quant & Brainteasers — the pizza market, the biotech
addressable market, the Chicago-New York flights — so this follows the existing precedent rather
than inventing a home.

## Two cards needed restructuring

- **B0979 and B0980** were one puzzle split across two cards: the marble-jar setup had no question
  and the question had no setup. They are merged into a single technical card.
- **B0718** welded a behavioral prompt to an estimation question ("Tell me about a passion that is
  not on your resume. How many cups of water does the coffee stand across the street use in a
  week?"). The behavioral half stays; the estimation half moved.

## The 19 left behind, and why

**Eleven cannot be solved as written** because the source lost the inputs: "Find the next number in
a mathematical sequence. [Sequence not recorded.]", "Multiply two numbers mentally. [Numbers not
recorded.]", the Rubik's cube with no dimensions, the ten-machine weighing with no measurement
limit. Moving these to the technical deck would put unanswerable cards in front of a student.

**Five more were unanswerable but carried no flag** — the 100 coins on a table with no question
attached, the closets puzzle whose process is missing, "How many degrees between the hour and minute
hands?" with no time given, "How many days will it take you to crawl out of the hole?" with no depth
or rate. These now carry **Incomplete prompt**, so they can be filtered out.

**Three are not brainteasers.** B0891 is three puzzles crammed into one card. B0733 asks for a view
on Bitcoin, which is a markets opinion. B1048 asks what YTM, YTC and YTW are — a genuine technical
question, but a bond question rather than a brainteaser, and part of the larger group of finance
technicals sitting in the behavioral file that is still open.

## Two routing bugs found on the way

**"Quant & Brainteasers" contains the substring "teaser".** The topic router matched it against the
deal-teaser keyword and filed 98 of the moved cards under *Deal & Process*. The keyword now requires
a word boundary, which it should always have done — any question mentioning a brainteaser would have
been mis-filed the same way.

**A stored topic was being treated as a hint rather than an instruction.** `classify()` concatenated
the stored topic onto the question text and ran keyword rules over the result, so an explicit topic
could lose to an accidental keyword match. A stored topic that names a real topic now wins outright,
and the keyword rules handle only the cards that say nothing. This moved three cards besides the
hundred, all of them added earlier in this session.

**"How many hours will you work?"** was being treated as a market-sizing question because it starts
with "how many". It is a question about the job, and now routes to the pressure and hours guidance.
