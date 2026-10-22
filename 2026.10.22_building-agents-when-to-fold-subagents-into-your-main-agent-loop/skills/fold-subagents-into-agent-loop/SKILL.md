---
name: fold-subagents-into-agent-loop
description: Decide whether each subagent in an existing multi-agent system (orchestrator plus specialists, routers, planners, domain agents) should be folded into a single main agent loop that uses progressively disclosed skills and tool search, and migrate one subagent at a time behind a task-completion eval. Keeps a subagent only when the single loop shows measurable context-bloat degradation, when work needs parallel throwaway context windows, or when one agent cannot pick tools or holds conflicting instructions. Covers failure modes of org-chart architectures (context loss, subagent sprawl, the Frankenprompt, localized evals, latency), the target single-loop design, merging coupled specialists, calling subagents as tools as an interim step, and how teams contribute skills, MCP tools, and knowledge bases under one central owner. Use when reviewing or simplifying an agent architecture, planning a subagent migration, or when a multi-agent agent is slow, inconsistent, or hard to own.
---

## Purpose
Many enterprise agents mirror the org chart: every team ships its own subagent and a central team puts
an orchestrator on top. Anthropic's Applied AI team found that a single agent with skills often beat
both a one-prompt-for-everything design and a subagent design on quality, frequently at lower cost and
latency. This skill walks through deciding, per subagent, whether to fold it into the main loop, and
doing so safely.

## When to use
- An agent has routers, planners, intent classifiers, or many domain subagents.
- Responses are inconsistent in voice, or latency from nested model loops hurts users.
- Teams each add rules to the system prompt or ship their own narrowly scoped evals.
- A model upgrade is planned and the multi-agent structure blocks the new model from doing more.

## Instructions

1. **Inventory the system.** List every subagent, router, and planner with its prompt owner, tools,
   evals, and how often production traffic chains it with another agent. Use
   [templates/migration-plan.md](templates/migration-plan.md).
2. **Apply the keep criteria** in [references/decision-criteria.md](references/decision-criteria.md).
   Keep a subagent only if at least one holds:
   - the single loop shows *measurable* degradation from context bloat;
   - tasks must run in parallel in fresh context windows that are discarded afterwards;
   - one agent struggles to pick the right tools, or its system prompt holds conflicting instructions.
   Everything else is a fold candidate. Flag splits that follow team boundaries (Conway's law).
3. **Build a task-completion eval first.** One shared end-to-end set owned by a central team, plus
   small sets each skill team ships. Ten golden examples is enough to start. See
   [templates/eval-plan.md](templates/eval-plan.md). Grade final messages against a rubric; while an
   orchestrator exists also track routing accuracy, and after folding track whether the right skill
   was loaded or the right tool called. Include a task for every agent chain that runs together in
   production and every rule the agent must not break; run each task more than once.
4. **Choose a path per subagent** (in order of disruption):
   - *Merge domain agents* that chain on each other's output, touch the same data, or are called
     together (e.g. a large share of traffic is specialist A then B). Start with the most-used ones.
   - *Call as a tool* when you keep a subagent: the main agent keeps the conversation, uses a shared
     response schema, verifies conclusions against real data, and trims input to the final synthesis.
     Full handoff only when the subagent must talk to the user directly. This gives a baseline without
     rewriting subagents, but summaries stay lossy and every call is a nested loop.
   - *Fold into skills and tools*: prompts become skills, API calls become MCP tools.
5. **Fold one subagent at a time.** Compare eval results with and without it. Look at which tasks
   *flipped*, not just the total score. Keep it as a subagent only if the folded version scores worse.
6. **Shape the target loop** as described in
   [references/single-loop-design.md](references/single-loop-design.md): one model, one context
   window, parallel tool batches, harness budgets and write gates, plan written and revised in context,
   procedure in skills, hard limits in tools.
7. **Set ownership.** One small central team owns the system prompt, end-to-end quality, and vets every
   new skill, tool, and eval. Teams move from owning agents to owning skills (with a DRI each), MCP
   tools grouped by user intent, and knowledge-base content.
8. **Use the Claude API skills where available**: `/claude-api build-eval`, `/claude-api prompt-audit`,
   `/claude-api hillclimb` (folded vs kept comparison), `/claude-api cost-optimize`; `/skill-creator`
   and `/skill-doctor` for the skill library. The post's migration kit chains these into one guided
   workflow with a demo on a mock system.
9. **Repeat**: measure, change one thing at a time, keep what holds up.

## Examples

**Example 1 - tightly coupled pair**
Input: "Our support agent routes to an order-lookup specialist and then a shipping specialist on most
tickets."
Output: Flag the pair as a merge candidate (chained output, shared data). Add eval tasks for the full
chain, merge into one domain agent, then consider folding into a skill plus order/shipping tools.

**Example 2 - a fold that broke a process**
In the post's sample support agent, folding one subagent cut latency but broke a passing task: the main
agent answered with the order lookup tool alone and never asked the shipping specialist for the delivery
date. It showed up in only one of two runs - hence a task per production chain and multiple runs.

**Example 3 - keep a subagent**
Independent research paths that run in parallel and only return a compact result meet the "parallel,
discardable context" criterion. Keep them as subagents called as tools, divided by context rather than
by problem type to avoid the "telephone game".

## Source
- https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
