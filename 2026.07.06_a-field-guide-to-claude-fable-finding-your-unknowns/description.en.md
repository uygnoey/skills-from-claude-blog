**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# A Field Guide to Claude Fable 5: Finding Your Unknowns

## What is this post?

A field guide by Thariq Shihipar (member of technical staff, Anthropic) on how to work with Claude Fable 5 by treating the gap between **the map** (your prompts, skills, and context) and **the territory** (the actual codebase and its constraints) as the thing to close. The argument is that as models get stronger, the quality of the work stops being limited by how well you plan and starts being limited by how well you surface what you did not know you needed to say.

The post sorts what you have not said into four kinds — known knowns, known unknowns, unknown knowns, and unknown unknowns — and then gives concrete moves for each phase of a project: before implementation, during implementation, and after implementation.

## When is it useful?

- Starting work in a part of the codebase you do not know well.
- Writing a plan or spec and wanting to find the decision points before Claude starts editing.
- Working in an unfamiliar domain where you cannot tell a good result from a bad one yet.
- Handing off a finished change to reviewers or stakeholders who were not in the loop.
- Wanting to verify that you actually understand a change Claude made for you.

## Key points

- **Four unknowns.** *Known knowns* are what you put in the prompt. *Known unknowns* are gaps you can name. *Unknown knowns* are obvious-to-you details you never think to write down. *Unknown unknowns* are blind spots you have not considered.
- **Blind spot pass.** Ask Claude directly for your blind spots, and tell it your level of expertise so it can calibrate.
- **Brainstorms and prototypes.** Explore several approaches before committing, so unclear criteria show up early and cheaply.
- **Interviews.** Ask Claude to interview you one question at a time, prioritizing questions whose answers would change the architecture.
- **References.** Point Claude at existing source code that already implements the behavior you want — even in a different programming language.
- **Implementation plans.** Ask for a plan that calls out the likely decision points before work begins.
- **Implementation notes.** Keep a scratch `implementation-notes.md` where Claude records every deviation from the plan forced by an edge case.
- **Pitches and explainers.** Package the prototype, spec, and notes into one shareable doc for buy-in.
- **Quizzes.** Ask for a contextual report plus a self-assessment quiz to check that you actually understand the change.
- **Worked example.** The author edited the Fable launch video with Claude Code, iteratively discovering unknowns across transcription, color grading, and video manipulation — domains they did not know going in.

## Bundled resources

- `skills/finding-your-unknowns/SKILL.md` — the full workflow as an Agent Skill, with prompt templates for each move.
- `skills/finding-your-unknowns/references/four-unknowns.md` — the four-quadrant model and how to attack each quadrant.
- `skills/finding-your-unknowns/templates/` — ready-to-paste prompts for blind spot passes, interviews, implementation notes, pitches, and quizzes.
- `skills/finding-your-unknowns/examples/launching-fable.md` — the launch-video case study.
- `guides/knowing-your-unknowns.en.md` — the same material as a narrative guide, in four languages.

## Source

- [A Field Guide to Claude Fable 5: Finding Your Unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns) — published 2026-07-06
