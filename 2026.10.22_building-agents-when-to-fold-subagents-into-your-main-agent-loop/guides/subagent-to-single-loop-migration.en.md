**English** · [한국어](./subagent-to-single-loop-migration.ko.md) · [Español](./subagent-to-single-loop-migration.es.md) · [日本語](./subagent-to-single-loop-migration.ja.md)

# From subagents to a single agent loop

A methodology summary of Anthropic's guidance on folding subagents into the main agent loop.

## 1. Why it matters
Large organizations often let each team build its own agent and add a central orchestrator. That
creates context loss between agents, subagent sprawl, a "Frankenprompt" of conflicting rules, localized
evals nobody owns, and extra latency. A single loop with progressively disclosed skills and tools keeps
shared context, avoids bloat, and leans on more capable models.

## 2. When subagents still belong
- Measurable degradation from context bloat in a single loop.
- Parallel tasks that need fresh, discardable context windows.
- Tool-selection trouble or conflicting instructions in one system prompt.
If you go multi-agent, start with the simplest pattern and divide by context, not by problem type.

## 3. Target architecture
One model and context window; an open-ended tool loop with turn/cost budgets and write gates; parallel
tool batches with raw results returned to the same model; a plan written in context and revised as
results arrive; procedure in skills, hard limits and mid-conversation lookups in tools; code only for
cheap, almost-always-relevant loading and mechanical work inside tools.

## 4. Migration stages
1. **Task-completion evals** - shared end-to-end set (central team) plus per-skill sets; 10 golden
   examples to start; rubric grading, routing accuracy, then skill/tool selection.
2. **Merge domain agents** that chain, share data, or are called together - most-used first.
3. **Call kept subagents as tools** - shared response schema, main agent verifies and keeps the
   conversation; full handoff only when the subagent must talk to the user.
4. **Fold one subagent at a time** - prompts to skills, API calls to MCP tools; compare flipped tasks;
   run each task more than once; keep the subagent only if the folded version scores worse.

## 5. Ownership model
| Asset | Owner | Rule of thumb |
|---|---|---|
| System prompt, end-to-end evals | Small central team | Vets every new skill, tool, eval |
| Skills | Team DRI | Distinct, well crafted, shipped with evals |
| MCP tools | Domain teams | Grouped by user intent; under ~30-50 definitions; tool search with deferred loading |
| Knowledge bases | Domain teams | Behind a lookup tool or skill reference files |

## 6. Tooling
`/claude-api build-eval`, `/claude-api prompt-audit`, `/claude-api hillclimb`,
`/claude-api cost-optimize`, `/skill-creator`, `/skill-doctor`, and the migration kit (with a demo on a
mock system).

## 7. Principle
Measure, change one thing at a time, and keep what holds up.

Source: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
