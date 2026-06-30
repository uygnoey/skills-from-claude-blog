---
name: loops-playbook
description: Choose the simplest loop primitive (turn-based, /goal, /loop, /schedule) and make success criteria explicit and verifiable.
---

# Loops playbook

This skill summarizes practical guidance for progressing from one-off, turn-based work to goal-based, time-based, and proactive loops, with a focus on clear stop conditions and verifiable success criteria.

## Instructions

### 1) Start with the simplest loop
- Prefer a one-off, turn-based interaction for short tasks that aren’t part of a regular process.
- Escalate to more structured loops only when it materially improves reliability or automation.

### 2) Make stop conditions explicit
- For goal-based work, define **success criteria** and an explicit **turn cap** (e.g., “stop after 5 tries”).
- Avoid subjective success criteria; prefer deterministic checks (tests, scores, thresholds).

### 3) Improve reliability with verification
- Give Claude a way to verify results end-to-end (tools/connectors, measurable checks).
- When possible, encode manual verification as reusable skills (see `references/related-skill-verify-frontend-change.md`).

### 4) Use the right primitive
- **Turn-based**: user-triggered, stops when the task is done or more context is needed.
- **/goal**: user-triggered; stops when the goal is achieved or the turn cap is reached.
- **/loop**: time-triggered; runs on your computer and stops if you turn it off.
- **/schedule**: time-triggered in the cloud; suitable for recurring routines.

### 5) Manage tokens intentionally
- Choose the right primitive/model for the job.
- Pilot before large runs.
- Use scripts for deterministic work.
- Don’t run routines more often than needed.

## Examples
See `examples/commands.md` for command examples from the source post.

## References
See `references/notes.md` for additional notes captured from the source.

## Source
- https://claude.com/blog/getting-started-with-loops
