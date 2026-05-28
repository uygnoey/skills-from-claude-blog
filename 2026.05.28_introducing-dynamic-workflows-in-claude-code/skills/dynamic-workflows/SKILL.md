---
name: dynamic-workflows
description: Decide when to use Claude Code dynamic workflows and structure requests so Claude can coordinate parallel subagents, resume long runs, and verify work before presenting results.
---

## Instructions

Use this skill when you want Claude Code to tackle a task that is too large for a single focused pass.

1. **Check that the task fits the workflow shape.** Dynamic workflows are suited for large-surface-area work (many files/modules/unknowns), broad discovery/review, migrations touching many files, or plans you want stress-tested.
2. **Prefer auto mode.** For the best experience, turn on auto mode before starting.
3. **Choose how to start.**
   - Ask Claude directly to “create a workflow” for your task.
   - Or enable **ultracode** (effort level xhigh) so Claude can decide when to use a workflow automatically.
4. **Expect a confirmation gate.** The first time a workflow triggers, Claude Code will show what it’s about to run and ask you to confirm.
5. **Plan for longer runs and higher cost.** Workflows can run for hours or days, can resume if interrupted, and may consume substantially more tokens than typical sessions.

## Examples

### Example 1: Service-wide bug hunt
User: Hunt for the root cause of intermittent 500s across the entire service. Use a dynamic workflow to search logs/config, trace code paths, propose candidate fixes, and verify by running the relevant tests.

### Example 2: Large migration
User: Migrate the codebase from X to Y across all packages. Use a workflow that (1) inventories impacted modules, (2) applies changes in parallel with reviews, and (3) runs build/tests in a fix loop until clean.

### Example 3: Stress-test a plan
User: I have a proposal to refactor subsystem Z. Use a dynamic workflow to challenge assumptions, identify risks, and produce a revised plan with milestones.

## Source
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
