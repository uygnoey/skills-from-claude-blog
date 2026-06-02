---
name: dynamic-workflows-harness
description: Patterns and reusable prompt templates for creating “dynamic workflows” in Claude Code to orchestrate multi-agent harnesses for complex, high-value tasks.
---

## Instructions
Use this skill to help you design, prompt, and package Claude Code dynamic workflows.

### What dynamic workflows are
- Dynamic workflows let Claude Code “write and orchestrate its own multi-agent harness on the fly” by executing a JavaScript workflow file that can spawn and coordinate subagents.
- Workflows can decide which model each agent uses and whether subagents run in their own worktree.
- If a workflow is interrupted, resuming the session can allow the workflow to pick up where it left off.

### When to use dynamic workflows
Use dynamic workflows for complex, high-value tasks where orchestration materially improves outcomes, even if it costs extra tokens.

### Core workflow patterns
Use (and compose) these patterns when designing a workflow:

1) Classify-and-act
- Add a classifier step that routes to different behaviors/agents based on task type, or use classification at the end to determine output.

2) Fan-out-and-synthesize
- Split a task into smaller steps, run an agent per step, then synthesize.
- The synthesize step acts as a barrier: it waits for all agents and merges their structured outputs.

3) Adversarial verification
- For each produced output, spawn a verifier/reviewer agent to check it against a rubric or criteria.

4) Generate-and-filter
- Generate many ideas, then filter by rubric/verification, dedupe, and return only the highest-quality results.

5) Tournament selection
- Spawn N agents that attempt the same task using different approaches.
- Use a judging agent to run pairwise comparisons until a winner (or top-k) remains.

6) Loop until done
- For tasks with unknown work size, loop spawning agents until a stop condition is met (e.g., no new findings or no more errors).

### Packaging and distribution
- You can save workflows from the workflow menu and store them under `~/.claude/workflows`.
- You can distribute workflows via a skill by placing JavaScript workflow files inside the skill folder and referencing them from this SKILL.md.
- If you want flexibility, treat the workflow as a template rather than a script that must be run verbatim.

### Bundled templates
- Prompt templates live in `templates/`:
  - `templates/reproduce-flaky-test.md`
  - `templates/mine-sessions-into-claude-md-rules.md`
  - `templates/slack-incidents-root-cause-mining.md`
  - `templates/multi-perspective-teardown.md`
  - `templates/resume-ranking-with-rubric.md`
  - `templates/name-ideas-tournament.md`
  - `templates/rename-model-everywhere.md`
  - `templates/verify-blog-claims.md`

For a longer narrative guide and examples, see `guides/dynamic-workflows.en.md`.

## Examples
### Example: use the "ultracode" trigger
Ask Claude Code:
- See `templates/ultracode-trigger.md`

### Example: build a triage workflow with quarantine
Ask Claude Code to propose a workflow that classifies items, dedupes against existing tracking, quarantines uncertain items, and then acts.

### Example: run adversarial verification
Ask Claude Code to create a workflow where each proposed fix is reviewed against an explicit rubric, and only merged if it passes.
