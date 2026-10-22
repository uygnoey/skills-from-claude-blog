# Subagent migration plan

System: ______  Central owner team: ______  Date: ______

## 1. Inventory
| Subagent / router / planner | Owner team | Prompt size | Tools | Own evals? | Often chained with | Share of traffic |
|---|---|---|---|---|---|---|
| | | | | | | |

## 2. Keep criteria (mark each that applies, with evidence)
| Subagent | Measured context-bloat degradation | Parallel, discardable context | Tool selection / conflicting instructions | Decision |
|---|---|---|---|---|
| | | | | keep as tool / merge / fold |

## 3. Order of work
1. Build the end-to-end eval (see eval-plan.md) and record the baseline.
2. (Optional) Switch kept subagents to "called as tools" with a shared response schema.
3. Merge tightly coupled pairs, most-used first.
4. Fold one subagent: prompt -> skill, API calls -> MCP tools (grouped by user intent).
5. Re-run the eval; list tasks that flipped; keep the subagent only if the folded version scores worse.
6. Repeat step 4-5 for the next subagent.

## 4. Change log
| Change | Eval before | Eval after | Flipped tasks | Latency / cost delta | Kept? |
|---|---|---|---|---|---|
| | | | | | |
