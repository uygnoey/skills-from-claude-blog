**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An Anthropic engineer explains how agentic coding pushed CI jobs up about 25x in six months, how the
team's test impact analysis (test selection) service nearly became the bottleneck, and why they
replaced three shrinking patches with a stateless redesign. The core lesson: always plan for the
exponential.

## When is it useful?
- When agent-authored PRs are driving CI volume faster than headcount.
- When a test selection service lags, pages, or hits memory limits.
- When deciding between another quick fix and a redesign, or sizing a new CI service.

## Key points
- Engineers ship ~8x more code per quarter than in 2021-2025, Claude writes ~80% of it; tests grew
  ~10x and CI jobs ~25x in six months.
- The service has a listener (records results) and a selector (picks tests per PR). Listener lag
  means stale selection: shared failures, flaky blockers, new or fixed tests not running.
- v0 was a single-writer process. Patches bought less time each round: bigger machine (~70 days),
  per-package sharding (29 days), daily restarts (< 1 day).
- A long-running Claude Tag session monitored lag (alert at 50,000 jobs) and kept arguing for an
  overhaul.
- Redesign: state in an in-memory store, stateless listener workers append to a journal, a consumer
  rolls it into per-test history every few seconds. One engineer, three weeks; Claude tuned it
  largely autonomously; backlog stayed flat.
- Advice: assume 25x load within two quarters, design v0 for 10-20x if budget allows, keep state out
  of the process, avoid single-instance critical services, instrument so jobs in equal jobs out.

## Bundled resources
- Skill: `agent-scale-ci-test-selection` — listener/selector model, lag costs, patch half-life,
  stateless redesign, planning rules (`references/scaling-timeline.md`,
  `templates/ci-scaling-review.md`).
- Guide: `stateless-test-impact-analysis` (en/ko/es/ja) — architecture and planning rules.

## Source
- https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
