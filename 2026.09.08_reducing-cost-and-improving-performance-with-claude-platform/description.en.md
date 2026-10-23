**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A best-practices article (September 8, 2026, later updated with Opus 5.5 benchmarks) arguing that cost and
performance on the Claude Platform need not be traded off. Three levers usually improve both: maximizing
prompt cache hits, removing prompting anti-patterns when moving to frontier models, and calibrating effort
to the task. The guidance is packaged into the `claude-api` skill.

## When is it useful?
- When API spend is high or cache hit rates are low.
- After migrating to a newer model while keeping old prompts, skills, or tool descriptions.
- When choosing a model and effort level against an eval.

## Key points
- Prompt cache: pinned to a model, needs a byte-exact prefix, 5-minute default TTL. Keep volatile values
  and reordering tools out of the prefix, use `defer_loading`, send system prompt updates as messages,
  pre-warm with `max_tokens: 0`, consider a 1-hour TTL for long waits.
- Anti-patterns: verification rituals, thoroughness boosters, scratchpad scaffolds, stale examples,
  contradictory rules, dated config. `/claude-api prompt-audit` finds them; in a case study it cut cost a
  further ~9% and raised accuracy ~2 points.
- Effort: too high overthinks, too low skips evidence. Sweep effort; try stronger models at lower effort.
  `/claude-api hillclimb` automates the search with a held-out test set.
- `/claude-api cost-optimize` ranks levers (caching, trimming, output bounds, Batch API); public
  benchmarks showed ~24-73% lower cost with little or no quality change.

## Bundled resources
- Skill: `api-cost-performance-tuning` (`references/prompt-cache-checklist.md`,
  `references/prompt-anti-patterns.md`, `references/benchmark-results.md`,
  `templates/cost-audit-report.md`).

## Source
- https://claude.com/resources/articles/reducing-cost-and-improving-performance-with-claude-platform
