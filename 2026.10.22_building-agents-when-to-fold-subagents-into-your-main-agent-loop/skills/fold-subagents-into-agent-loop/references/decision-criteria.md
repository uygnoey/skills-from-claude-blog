# Decision criteria: keep, call as tool, merge, or fold

Source: "Building agents: When to fold subagents into your main agent loop" (Claude, 2026-10-22).

## Keep a subagent when at least one is true
1. A single agent loop hits **measurable** performance degradation from context bloat.
2. Multiple tasks must run **in parallel** with fresh context windows that can be discarded afterwards.
3. A single agent **struggles to select appropriate tools**, or the system prompt contains
   **conflicting instructions**.

Subagents remain effective for verification, parallel work, and modular permissioning.

## Warning signs of an org-chart architecture
| Failure mode | What it looks like |
|---|---|
| Context management | Deciding what context moves between agents; details lost in the back and forth |
| Subagent sprawl | Hundreds of overlapping subagents, no enforced standards, no specific owner |
| The Frankenprompt | Every team adds a sentence to the system prompt: conflicting rules, no consistent voice |
| Unvetted, overly localized evals | Evals optimized for subtasks; nobody owns the whole set; leadership reads watered-down scores |
| Latency | Nested loops add latency; one customer saw roughly 2x faster runtime with a single loop |

Other common over-structure: intent classifier, fixed multi-step reasoning pipeline, user-segment
buckets, separate recommendation branches, multi-agent orchestrator on top. Often one clear system
prompt, 4-5 thin data tools, and firm output guardrails cover most of the use case.

## Why a single loop with progressive disclosure can win
- **Shared context** - the agent that saw each earlier step can connect them; fewer lossy handoffs.
- **Progressive disclosure prevents bloat** - short skill and tool descriptions, full content loaded
  only when needed (Claude Code's system prompt for advanced models was cut by over 80%, partly this way).
- **Models are more capable** - since Opus 4.5 models manage far more in one loop; recent models narrate
  progress and check their work, making some harness elements redundant. Simpler loops also move to the
  next model more easily.

## If you do go multi-agent
- Start with the simplest pattern that could work (generator-verifier, orchestrator-subagent, ...).
- Divide **by context**, not by problem type: each subagent gets work that needs little from the rest of
  the system and returns a compact result (independent research paths, components with clean
  interfaces, black-box verification).

## Where team knowledge should live
| Kind | Use when | Notes |
|---|---|---|
| MCP tools | Take an action, read live data, return a fixed shape | Group by user intent, not one per API; choice degrades past ~30-50 definitions; use tool search with deferred loading; put preconditions and per-user permission checks inside tools, returning instructions or plain refusals the model can read |
| Skills | How a team does the work: steps, rules, judgment calls | DRI per team; well crafted, distinct, shipped with evals; `/skill-creator`, `/skill-doctor` |
| Knowledge bases | Reference material needed some of the time | Behind a search/lookup tool or as skill reference files; avoid code that pastes it into prompts |
