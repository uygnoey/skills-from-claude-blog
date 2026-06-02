**English** · [한국어](./dynamic-workflows.ko.md) · [Español](./dynamic-workflows.es.md) · [日本語](./dynamic-workflows.ja.md)

# Dynamic workflows in Claude Code (guide)

## What it is
Dynamic workflows let Claude Code write and run a custom multi-agent harness “on the fly” by executing a JavaScript workflow file that can spawn and coordinate subagents.

## How it works (high level)
- A workflow executes a JavaScript file with special helper functions for spawning/coordinating subagents.
- Workflows can use standard JavaScript utilities (e.g., JSON, Math, Array) to process data.
- Workflows can decide which model an agent uses and whether subagents run in their own worktree.
- If interrupted, resuming the session can allow the workflow to continue.

## When to use it
Dynamic workflows are best for complex, high-value tasks where you want isolated contexts, specialized roles, and structured synthesis/verification.

## Common patterns
- Classify-and-act
- Fan-out-and-synthesize (barrier + merge)
- Adversarial verification (review against a rubric)
- Generate-and-filter (generate many → dedupe → keep best)
- Tournament (pairwise judging to a winner/top-k)
- Loop until done (stop condition, not fixed passes)

## Example use cases
- Engineering: break work by failing tests/modules/callsites; fix in parallel worktrees; adversarial review and merge.
- Triage: classify items, dedupe against existing tracking, quarantine uncertain cases, then act.
- Lightweight evals: run candidate solutions in worktrees, then compare/grade against a rubric.
- Non-technical: multi-perspective critique, resume ranking with a rubric, naming tournaments.

## Saving and sharing
- Save from the workflow menu (press `s`) and store under `~/.claude/workflows`.
- To distribute via a skill, place workflow JavaScript files in the skill folder and reference them from `SKILL.md`.
- Consider treating workflows as templates for flexibility.

## Source
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
