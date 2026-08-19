# Inline DLP rollout plan — <organization>

Fill this in before enabling anything. The decision log at the bottom is the part that has to survive the rollout.

## 1. Scope

| Field | Value |
|---|---|
| Surfaces in scope | <chat / coding agent / agentic workspace / tool calls> |
| Surfaces explicitly out of scope | <...and why> |
| Policy server | <vendor platform or in-house service> |
| Owner (security) | <name / team> |
| Owner (platform) | <name / team> |
| Target start date | <YYYY-MM-DD> |
| Target full-enforcement date | <YYYY-MM-DD> |

## 2. Enforcement settings

| Setting | Value | Rationale |
|---|---|---|
| Failure policy | fail open / fail closed | |
| Timeout | <ms> | |
| Role-based exclusions | <roles> | |
| Shadow mode | on / off | |
| Enforcement percentage | <n>% | |

## 3. Shadow-mode measurements

Record one row per observation window. Do not begin enforcement until the would-be denial rate is dominated by hits you would actually want blocked.

| Window | Requests | Would-be denials | Denial rate | Top matching rules | p95 added latency | Server errors/timeouts |
|---|---|---|---|---|---|---|
| | | | | | | |

**Rules tuned as a result:**

- <rule> — <change> — <why>

## 4. Ramp plan

| Step | Population | Start | Exit condition | Result |
|---|---|---|---|---|
| 0 | Everyone, shadow mode | | Rules tuned, latency acceptable, server stable | |
| 1 | Security team, enforcing | | No unexplained denials | |
| 2 | <n>% of org | | Denial rate at or below <x>%, no unresolved escalations | |
| 3 | <n>% of org | | Denial rate holds as usage broadens | |
| 4 | 100% | | Steady state | |

**Rollback:** to return to shadow mode, <who> does <what>. On-call runbook: <link or location>.

## 5. User-facing path on denial

- What the user sees: <...>
- Where to report a false positive: <channel / queue>
- Exception process: requested by <...>, approved by <...>, expires after <...>

## 6. Decision log

| Date | Change | Made by | Reason |
|---|---|---|---|
| | | | |

## Source

- https://claude.com/blog/claude-enterprise-inference-hooks
