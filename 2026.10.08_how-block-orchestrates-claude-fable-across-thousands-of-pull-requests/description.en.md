**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An interview with Bradley Axen, Head of AI Capabilities at Block (Square, Cash App), on how Block
evaluates models, how Claude Fable 5 orchestrates company-wide code migrations across thousands of
pull requests, how Block steers employees toward efficient model use, and which safeguards it relies
on when every technical employee has access to frontier models.

## When is it useful?
- When planning a migration that spans hundreds or thousands of PRs across many repos.
- When deciding which model and effort level to use for a given kind of agent task.
- When designing guardrails for agents that write code in a large organization.

## Key points
- Tiered orchestration: a human steers; Fable does the upfront design (data models, API specs,
  algorithms) and directs up to dozens of smaller models (Opus, Sonnet) that edit files and run tests.
  Early results show more tokens shifting to worker models without a drop in quality; one migration
  might merge a thousand Fable-orchestrated PRs.
- Block runs this in Buzz, its open-source workspace where humans and agents share channels and threads.
- Agents make daily or weekly passes over a roughly million-line codebase to find tech debt to clean
  up and consolidate.
- Efficiency: full frontier access for technical roles, plus an auto-selector for choosing models.
  Every use case is benchmarked across every model and every effort level — a grid, not a slider.
- Safeguards: merges to main, production deploys, and feature flags stay with humans; agent changes
  pass security checks and need two human approvals. Remote workstations, network allow lists, and
  cheap checks outside the model loop (regexes, small classifiers). Opening PRs, code review, and
  querying logs and analytical databases are deliberately allowed. Claude refuses requests to bypass
  the dual approval, and Block benchmarks that.
- Organizational maturity means keeping learned context at the system level, not the individual level.

## Bundled resources
- Skill: `orchestrated-code-migrations` — tiered orchestrator/worker migrations, model × effort
  selection (`templates/model-effort-grid.md`), and safeguards (`references/safeguards.md`).
- Agents: `migration-orchestrator` and `migration-worker`, the two roles described in the post.
- Guide: "Operating frontier models efficiently and safely at scale" in four languages.

## Source
- https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
