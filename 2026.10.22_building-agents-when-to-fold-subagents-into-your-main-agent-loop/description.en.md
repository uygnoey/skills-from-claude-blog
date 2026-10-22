**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A best-practices article (October 22, 2026, Diane Sarkis) on when to fold routers, planners, and domain
subagents into a single main agent loop that uses progressively disclosed skills and tool search, and
how to migrate there step by step on Claude Platform.

## When is it useful?
- When an agent architecture has grown into a copy of the org chart (one subagent per team).
- When a multi-agent agent is slow, inconsistent in voice, or hard to evaluate end to end.
- When planning which subagents to keep, call as tools, merge, or fold into skills and tools.

## Key points
- In comparisons across enterprise deployments, a single agent with skills often beat both a
  one-prompt design and a subagent design on quality, often at lower cost and latency.
- Keep subagents when there is measurable context-bloat degradation, parallel work needing discardable
  context, or tool-selection trouble / conflicting instructions.
- Failure modes: context management, subagent sprawl, the Frankenprompt, localized evals, latency
  (one customer saw roughly 2x faster runtime with a single loop).
- Target design: one model, one context window, parallel tool batches, harness budgets and write gates,
  plan written and revised in context; procedure in skills, hard limits in tools.
- Migrate behind a task-completion eval (10 golden examples to start), one subagent at a time, checking
  which tasks flipped and running each task more than once.
- Teams own skills, MCP tools (grouped by user intent; choice degrades past 30-50 definitions), and
  knowledge bases; one small central team owns the system prompt and end-to-end quality.
- Helpers: `/claude-api build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`, `/skill-creator`,
  `/skill-doctor`, and a migration kit with a demo.

## Bundled resources
- Skill: `fold-subagents-into-agent-loop` (`references/decision-criteria.md`,
  `references/single-loop-design.md`, `templates/migration-plan.md`, `templates/eval-plan.md`).
- Guide: `guides/subagent-to-single-loop-migration.{en,ko,es,ja}.md`.

## Source
- https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
