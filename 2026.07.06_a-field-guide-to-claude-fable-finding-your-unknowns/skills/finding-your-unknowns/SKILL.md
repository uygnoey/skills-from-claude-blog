---
name: finding-your-unknowns
description: Surface what you did not know you needed to say before, during, and after an implementation. Use when starting work in an unfamiliar codebase or domain, when writing a plan or spec, when you want to find architectural decision points before any code is edited, when a change deviated from its plan, or when handing a finished change to reviewers. Provides a blind spot pass, brainstorm and prototype loops, one-question-at-a-time interviews, reference-code pointers, decision-point implementation plans, running implementation notes, shareable pitches and explainers, and self-assessment quizzes.
---

# Finding Your Unknowns

The prompt, the skills, and the context you supply are **the map**. The codebase and its
real constraints are **the territory**. Work goes wrong where the two disagree — and the
disagreement is almost never in what you said, it is in what you never thought to say.

Treat every project as a search for the gap. The moves below are cheap ways to find that
gap early, while it is still cheap to fix.

See [references/four-unknowns.md](references/four-unknowns.md) for the four-quadrant model
that names the different kinds of gap and how each one gets closed.

## Instructions

### Phase 1 — Before implementation

Do these before any file is edited. Each one is cheap; a wrong architecture is not.

1. **Blind spot pass.** Ask directly for what you have not considered, and state your own
   level of expertise so the answer is calibrated to it. A senior engineer in their own
   subsystem and a newcomer to it need different blind spot lists.
   Use [templates/blind-spot-pass.md](templates/blind-spot-pass.md).

2. **Brainstorms and prototypes.** Before committing to one approach, explore several.
   Prototypes are not throwaway work — they are how unclear success criteria become
   visible. If you cannot yet tell a good result from a bad one, build two and compare.
   Use [templates/brainstorm-and-prototype.md](templates/brainstorm-and-prototype.md).

3. **Interviews.** Ask to be interviewed **one question at a time** about anything
   ambiguous, and explicitly prioritize the questions whose answers would change the
   architecture. One-at-a-time matters: a batch of twenty questions gets skimmed and
   answered shallowly; a single question gets thought about.
   Use [templates/interview.md](templates/interview.md).

4. **References.** Point at existing source code that already implements the behavior you
   want. This works across programming languages — the value is in the shape of the
   solution and the edge cases it handles, not the syntax. A reference implementation
   transfers *unknown knowns* you could never have articulated.
   Use [templates/references.md](templates/references.md).

5. **Implementation plans.** Ask for a plan that explicitly calls out where decisions will
   have to be made, not just what will be done. Review the decision points, not the steps.
   Use [templates/implementation-plan.md](templates/implementation-plan.md).

### Phase 2 — During implementation

6. **Implementation notes.** Keep a temporary `implementation-notes.md`. Whenever an edge
   case forces a deviation from the plan, it gets written down there with the reason. The
   file is the record of every unknown the territory revealed while the work was happening,
   and it is the raw material for Phase 3.
   Use [templates/implementation-notes.md](templates/implementation-notes.md).

### Phase 3 — After implementation

7. **Pitches and explainers.** Package the prototype, the spec, and the implementation
   notes into a single document you can drop into a chat channel. People who were not in
   the loop cannot review a diff, but they can review a story about why it looks like this.
   Use [templates/pitch-and-explainer.md](templates/pitch-and-explainer.md).

8. **Quizzes.** Ask for a report on the changes with enough context to actually read them,
   plus a self-assessment quiz. Failing your own quiz on your own change is the cheapest
   possible way to discover you did not understand what shipped.
   Use [templates/quiz.md](templates/quiz.md).

### How to sequence it

Run Phase 1 in order until the answers stop surprising you. That is the signal that the map
has caught up with the territory for now. Then implement, keeping notes. Then close the
loop with Phase 3 before you consider the work done.

Not every project needs all eight moves. A one-line fix in code you wrote last week needs
none of them. A new subsystem in code you have never opened needs all of them.

## Examples

### Adding an auth provider to an unfamiliar module

> I'm working on adding a new auth provider but I know nothing about the auth modules in
> this codebase. Can you do a blind spot pass — what are the unknown unknowns here, the
> things I would not even know to ask about?

The answer names the session-invalidation path, the token-refresh race, and a migration
concern for existing sessions. None of the three were in the original ticket.

Follow with an interview to resolve the ambiguities the blind spot pass exposed:

> Interview me one question at a time about anything ambiguous, prioritize questions where
> my answer would change the architecture.

### Working in a domain you do not know

The author edited the Claude Fable launch video with Claude Code, working across video
transcription, color grading, and video manipulation — none of which they knew going in.
The unknowns were discovered iteratively rather than planned away up front. See
[examples/launching-fable.md](examples/launching-fable.md) for the full walkthrough.

### Catching a mid-flight deviation

> Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate
> from the plan, write down what you hit, what you did instead, and why.

Later, at review time, the notes file explains why the retry logic looks nothing like the
plan — an upstream API returns 200 with an error body. That was an unknown unknown at
planning time, and it is now documented instead of rediscovered.

### Verifying your own understanding

> Give me a HTML report on the changes for me to read and understand with context, then
> quiz me on it so I can check whether I actually followed what happened.

Every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out
what you did not know before it gets expensive to fix.

## Source

- [A Field Guide to Claude Fable 5: Finding Your Unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns), Thariq Shihipar, 2026-07-06
