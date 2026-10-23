# Cost audit: <application name>

## Usage source
- [ ] Organization usage and cost reports (Admin API key)
- [ ] Logged usage objects from API responses
- [ ] Estimated from request-building code

## Current state
| Metric | Value |
|---|---|
| Model / effort | |
| Cache hit rate | |
| Avg input / cache-read / output tokens per request | |
| Cost per task | |
| Eval score (if available) | |

## Levers (ranked)
| # | Lever | Finding | Change | Expected effect |
|---|---|---|---|---|
| 1 | Prompt caching | | | |
| 2 | Trim request content / prompt-audit | | | |
| 3 | Bound output | | | |
| 4 | Batch API for unattended work | | | |
| 5 | Model / effort trade-off (needs eval) | | | |

## Result
| Config | Cost per task | Score (held-out) |
|---|---|---|
| Baseline | | |
| Final | | |
