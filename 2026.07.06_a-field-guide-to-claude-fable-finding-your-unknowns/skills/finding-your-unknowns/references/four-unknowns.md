# The four unknowns

Everything you have not told Claude falls into one of four categories. They are not equally
hard to close, and they do not respond to the same technique.

| | **You know it** | **You do not know it** |
|---|---|---|
| **You are aware of it** | Known knowns | Known unknowns |
| **You are not aware of it** | Unknown knowns | Unknown unknowns |

## Known knowns

Information you have and know you have — it is explicitly in the prompt, the skill, or the
context file. This is the part of the map you drew on purpose.

**How to close it:** just say it. This quadrant is a writing problem, not a discovery
problem.

## Known unknowns

Gaps you can name. You know there is a caching layer, you know you do not know how it
invalidates, and you know that matters.

**How to close it:** ask. Point Claude at the code, ask it to explain the part you know you
are missing, or ask it to research the domain before it starts.

## Unknown knowns

Details that are obvious to you and therefore never get written down. The team convention
nobody documents. The reason a module is structured oddly. The performance constraint
everyone internalized two years ago.

This is the quadrant that quietly ruins otherwise good prompts: you get a technically
correct result that is wrong for your codebase, and you cannot say why you expected
different.

**How to close it:**
- **References** — point at existing source code that already does it the right way. The
  reference carries the convention you could not articulate, even across languages.
- **Interviews** — being asked one question at a time surfaces answers you would never
  have volunteered.

## Unknown unknowns

Blind spots. Factors you have not considered and would not know to ask about.

**How to close it:**
- **Blind spot pass** — ask outright for what you have not considered, and state your level
  of expertise so the answer is calibrated.
- **Brainstorms and prototypes** — exploring several approaches makes the criteria you were
  implicitly judging by become visible.
- **Implementation notes** — the ones the territory only reveals mid-implementation get
  recorded when they happen instead of being rediscovered at review.

## Why the quadrants matter

The moves in `SKILL.md` are ordered by which quadrant they attack. Running them in order is
what makes each later one cheaper: a blind spot pass narrows unknown unknowns into known
unknowns, an interview converts unknown knowns into known knowns, and a plan turns the
remaining known unknowns into explicit decision points you can answer before any code moves.
