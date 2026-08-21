# Template: root `CLAUDE.md` — what can't change

The guide's rule for the repo-root context file: **put what can't change in
`CLAUDE.md` at the root of your repo.** Claude reads it at the start of every
session, so your architecture rules, security boundaries, and non-negotiables
travel with every session.

This is deliberately not a project-overview template. Overview material belongs
in the codebase and in per-subdirectory `CLAUDE.md` files, which the guide
recommends for coding conventions specific to that subdirectory that apply every
time. On-demand procedural workflows belong in skills.

Zingage's version of this file ran to 567 lines: "How we frame problems. What has
to be true no matter what. How to prove something works instead of trusting a
confident answer." Length is not the goal — completeness on the invariants is.

Copy the scaffold below into `CLAUDE.md` at the repo root and fill it in. Delete
any heading you cannot state a real, checkable rule under; an empty section
teaches nothing.

---

```markdown
# <repo name>

## Invariants — true no matter what

<!-- Statements that a change is wrong if it violates. Not preferences. -->
- 
- 

## Architecture rules

<!-- Boundaries between layers/services; what may depend on what; what may not
     be introduced without a design discussion. -->
- 
- 

## Security boundaries

<!-- Where secrets may and may not go. What leaves the sandbox. What must never
     be logged. Which surfaces are untrusted input. -->
- 
- 

## How we frame problems

<!-- The house method: how a change gets scoped, what gets written down before
     code, what "done" means here. -->
- 
- 

## How to prove something works

<!-- The verification standard. Which command is authoritative for tests. What
     evidence counts, so a confident answer alone never does. -->
- 
- 

## Non-negotiables

<!-- Compliance, regulatory, or contractual constraints that override velocity. -->
- 
- 
```

---

## Writing rules that hold

- **State the invariant, not the example.** "Fix the principle, not the example"
  applies to context files as much as to agent instructions. If you find yourself
  adding a line per incident, you are accumulating patches.
- **Cap the specifics.** Cainex explicitly caps how many specifics can enter a
  change to their instruction set, after a first version that overfitted.
- **Make it checkable.** Prefer "every PR that touches `billing/` must include a
  test that fails without the change" over "be careful with billing."
- **Let it drift a little.** Emergent's stance on shared context: it is fine to
  live with slightly outdated context files as long as the agent can quickly
  verify and course correct. Perfection here is not worth blocking on.

## Related mechanisms from the guide

- **Hooks** for the parts that must be deterministic — they fire at fixed points
  in the lifecycle and execute regardless of what the model decides.
- **Skills** for on-demand procedural workflows, shared through a directory or a
  company plugin marketplace.
- **Subdirectory `CLAUDE.md`** for conventions local to one part of the repo.

## Source

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) (published 2026-08-20).
