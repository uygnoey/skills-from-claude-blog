**English** · [한국어](./knowing-your-unknowns.ko.md) · [Español](./knowing-your-unknowns.es.md) · [日本語](./knowing-your-unknowns.ja.md)

# Knowing your unknowns: matching the map and the territory

## The shift

The prompt, the skills, and the context you hand to Claude are **the map**. The codebase,
its constraints, and everything true about it that nobody wrote down are **the territory**.

Work goes wrong where the two disagree. As models get stronger, the binding constraint on
quality moves: it stops being how well you plan and becomes how well you surface what you did
not know you needed to say. Planning improves the map. It does nothing about the parts of the
territory you have never seen.

## Four kinds of gap

Everything you have not said falls into one of four kinds, and they do not respond to the
same treatment.

- **Known knowns** — what you deliberately put in the prompt. A writing problem, not a
  discovery problem.
- **Known unknowns** — gaps you can name. You know there is a caching layer; you know you do
  not know how it invalidates. These you can simply ask about.
- **Unknown knowns** — details so obvious to you that you never think to write them down. The
  undocumented team convention. The reason a module is shaped oddly. This quadrant quietly
  ruins good prompts: the result is technically correct and wrong for your codebase.
- **Unknown unknowns** — blind spots. Factors you have not considered and would not know to
  ask about.

The last two are the expensive ones, and neither is closed by trying harder at the prompt.

## Before implementation

**Blind spot pass.** Ask outright what you have not considered, and say how much you actually
know about the area. A senior engineer new to the auth module and a newcomer to the codebase
need different lists, and the answer is only useful if it is calibrated to you.

> I'm working on adding a new auth provider but I know nothing about the auth modules in this
> codebase. Can you do a blind spot pass...

**Brainstorms and prototypes.** Explore several approaches before committing to one. This is
not a hedge — it is how you discover the criteria you were implicitly judging by. If you
cannot yet tell a good result from a bad one, build two and react to them.

**Interviews.** Ask to be interviewed one question at a time, prioritizing questions whose
answers would change the architecture.

> Interview me one question at a time about anything ambiguous, prioritize questions where my
> answer would change the architecture.

One-at-a-time is the whole technique. A batch of twenty questions gets skimmed; a single
question gets thought about, and the answer redirects the next one. This is the main way
unknown knowns get out of your head.

**References.** Point at source code that already implements the behavior you want — even in
a different programming language. What transfers is the shape of the solution and the set of
edge cases the original author hit and handled. That set is a free inventory of your unknown
unknowns for this problem.

**Implementation plans.** Ask for a plan that highlights the likely decision points, not just
the steps. Review the decisions. Steps tell you whether the work will get done; decisions tell
you whether it will get done right, and that is the part a plan can still change cheaply.

## During implementation

**Implementation notes.** Keep a temporary `implementation-notes.md`. When an edge case forces
a deviation from the plan, it gets recorded there with the reason.

> Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate
> from the plan...

The territory reveals unknowns while the work is happening, and the reason is the field that
matters. Retry logic that does not match the plan looks like sloppiness unexplained and like
diligence when the note says an upstream API returns 200 with an error body.

## After implementation

**Pitches and explainers.** Package the prototype, the spec, and the implementation notes into
one shareable document.

> Package the prototype, the spec, and the implementation notes into a single doc I can drop
> in Slack...

People who were not in the loop cannot review a diff. They can review the story of why the
change looks like this — including the approach that was tried and rejected, which is usually
the most persuasive part.

**Quizzes.** Ask for a report on the changes with enough context to read them, plus a
self-assessment quiz.

> Give me a HTML report on the changes for me to read and understand with context...

Failing your own quiz on your own change is the cheapest possible way to find out you did not
understand what shipped. Do it before review, not after.

## How it comes together

The author edited the Claude Fable launch video with Claude Code, working across video
transcription, color grading, and video manipulation — none of which they knew going in. In a
domain that unfamiliar, planning is not cheaper than prototyping; it is worse, because the
plan encodes assumptions you have no basis for. The unknowns were found iteratively: attempt
something concrete, react to the result, ask what you did not know to ask about the thing you
just reacted to, repeat with the vocabulary you just acquired.

That is the general case compressed. Every project has a corner you do not know. This one just
had no corner the author did.

## The point

Every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out
what you didn't know before it gets expensive to fix. So start your next project by asking
Claude to help you find your unknowns.

## Source

- [A Field Guide to Claude Fable 5: Finding Your Unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns), Thariq Shihipar, 2026-07-06
