---
name: onboarding-cc
description: Treat Claude Code onboarding like developer onboarding by maintaining durable, versioned project context (e.g., a root CLAUDE.md plus a small skill library and references to deeper documentation).
---

## Instructions

Use this skill to make Claude Code productive in a large, long-lived repository by turning “context” into maintained project artifacts.

1) Create a durable context home
- Maintain a dedicated, versioned place for AI context that can improve over time (the post’s example is a separate repository). 
- Keep it stable across branch churn and long-running release lines.

2) Add a repo-root onboarding entrypoint
- Add a `CLAUDE.md` at the repository root.
- Include:
  - Environment setup steps
  - The “lay of the land” (where key code lives)
  - Links to deeper documentation (“reference, don’t embed”)

3) Build a small skill library for recurring work patterns
- Create reusable skills that encode your team’s expectations.
- Keep skills short and point to canonical docs rather than duplicating them.
- Examples mentioned in the post include skills for:
  - Project orientation
  - Version control conventions
  - Debugging (load when investigating bugs/failures)

4) Use integrations to reduce manual context-passing
- Where appropriate, add integrations that can expose project signals to Claude Code (e.g., tests, exceptions, support threads, release tags).
- Prefer automation that produces summaries and diffs over raw dumps.

## Examples

### Example: Minimal onboarding checklist for a new repo
- Create or update `CLAUDE.md` with environment setup and links to docs.
- Add/update small skills for debugging and version control.
- Add integrations for the project’s “health signals” (tests, exceptions, support).

### Example: “Reference, don’t embed” documentation pattern
Instead of copying a long internal document into an instruction, add a short pointer:
- “See `docs/architecture.md` for module boundaries.”
- “See `docs/testing.md` for how to run and interpret nightly tests.”

## Source
- https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development
