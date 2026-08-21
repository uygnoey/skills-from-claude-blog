# Worked example — editing the Fable launch video

The author's own account of how the moves in this skill come together on a real project,
in a domain they did not know.

## The setup

The task was editing the Claude Fable launch video, using Claude Code. The relevant fact is
not that it was a video — it is that the author was working across **video transcription,
color grading, and video manipulation**, none of which they knew going in.

That makes every quadrant hostile at once:

- Almost nothing is a *known known* — there is no domain vocabulary to put in the prompt.
- The *known unknowns* are unhelpfully large ("I don't know how color grading works").
- There are no *unknown knowns* to extract by interview, because there is no prior expertise
  to draw out.
- The *unknown unknowns* dominate. In an unfamiliar domain, you cannot even tell a good
  result from a bad one yet.

## What it looked like in practice

Unknowns were discovered **iteratively**, not planned away up front. In a domain this
unfamiliar, a long planning pass is not cheaper than a prototype — it is worse, because the
plan encodes assumptions you have no basis for.

The loop that worked:

1. **Attempt something concrete** in one sub-domain (transcribe, cut, grade).
2. **Look at the result and react.** Reacting to an artifact recovers criteria that
   introspection does not: you cannot state what "correct color grading" means, but you can
   tell that a shot looks wrong.
3. **Ask what you did not know to ask** about the thing you just reacted to — a blind spot
   pass narrowed to the one sub-domain rather than the whole project.
4. **Repeat** in the next sub-domain, carrying forward the vocabulary you just acquired.

Each pass converts unknown unknowns into known unknowns, and known unknowns into vocabulary
you can put in the next prompt. The map catches up to the territory in increments.

## What transfers

- **In an unfamiliar domain, prototype before you plan.** Planning is for when you can judge
  the plan. Prototyping is for when you cannot.
- **Narrow the blind spot pass to the sub-domain you just touched.** "What are my blind spots
  in this project" is too broad to be useful in a domain you do not know; "what am I missing
  about this transcription output" is answerable.
- **Expect the criteria to arrive late.** You will know what you were judging by only after
  you have something to judge. Budget iterations for that instead of trying to specify it up
  front.
- **The unfamiliar-domain case is the general case, compressed.** Every project has some
  corner you do not know. This one just has no corner you do.

## Closing

> Every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out
> what you didn't know before it gets expensive to fix. So start your next project by asking
> Claude to help you find your unknowns.
