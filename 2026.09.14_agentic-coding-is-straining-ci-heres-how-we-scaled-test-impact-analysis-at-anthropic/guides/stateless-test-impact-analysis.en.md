**English** · [한국어](./stateless-test-impact-analysis.ko.md) · [Español](./stateless-test-impact-analysis.es.md) · [日本語](./stateless-test-impact-analysis.ja.md)

# Stateless test impact analysis for agent-scale CI

An architecture guide based on how Anthropic redesigned its test selection service after CI jobs
grew about 25x in six months.

## Why CI strains under agents
- Engineers ship ~8x more code per quarter than in 2021-2025; Claude writes ~80% of it and helps
  review and approve PRs. Once review speeds up, CI takes the pressure.
- Tests grew ~10x; CI jobs grew ~25x in six months.
- Agents favor smaller, more granular PRs and push overnight and on weekends, raising the activity
  floor, while human approvals keep traffic bursty.

## The listener/selector model
| Component | Role |
|---|---|
| Listener | Records test results from every CI run |
| Selector | Reads result history and picks tests for each PR (past performance, package relevance) |

If the listener lags, selection runs on stale data: bad changes fail tests for everyone, flaky
dependencies block merges, and new or fixed tests do not run. 20 minutes of lag can mean tens of
thousands of unapplied updates.

## Why v0 stopped scaling
A single process held per-test history and needed a single writer, so it could not shard
horizontally. Patches bought less time each round: bigger machine (~70 days), per-package sharding
(29 days), daily restarts (< 1 day).

## The redesign
```
CI runs ──▶ stateless listener workers ──append──▶ journal (in-memory store)
                                                      │ every few seconds
                                                      ▼
                                        consumer rolls up per-test history
                                                      │
PR opened ──▶ selector ──────── reads history ◀───────┘
```
- Any worker can process any result and holds nothing in memory, so workers scale horizontally.
- More expensive to run than the singleton, but easier to scale and memory-profile.
- One engineer, three weeks; Claude tuned journal size and worker count largely autonomously.
- After cutover and tuning, the hourly max of queued unprocessed events stayed flat.

## Planning rules
1. Assume 25x load within two quarters, whether you build or buy.
2. If budget allows, design v0 for 10-20x perceived scale.
3. Keep state out of the process from the start.
4. Avoid single-instance critical services unless you can measure them and canary changes.
5. Instrument services as Claude's eyes and ears; make sure CI jobs in equal jobs out.
6. Use a long-running agent session to monitor lag (Anthropic alerted at 50,000 jobs) and keep
   context across incidents.

## Source
- https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
