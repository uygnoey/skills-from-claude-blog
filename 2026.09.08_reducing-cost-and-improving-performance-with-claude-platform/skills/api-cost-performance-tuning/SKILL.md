---
name: api-cost-performance-tuning
description: Cut Claude API cost while holding or improving quality using the three levers from the Claude Platform best-practices article (September 2026) - maximize prompt cache hits, remove legacy prompting anti-patterns when moving to frontier models, and calibrate effort to the task - plus the claude-api skill commands that automate them (/claude-api prompt-audit, /claude-api cost-optimize, /claude-api hillclimb). Use when an API application's spend is high, cache hit rates are low, a prompt was written for an older model, or you need to choose model and effort level against an eval.
---

## Purpose
The source argues that cost and performance do not have to be traded off. Most applications improve on
both by (1) hitting the prompt cache more, (2) deleting instructions that patched older model weaknesses,
and (3) setting effort to what the task actually needs. Anthropic packaged this guidance into the
`claude-api` skill; this skill is the manual procedure plus pointers to those commands.

## When to use
- API spend is rising, or cache reads are a small share of input tokens.
- You upgraded the model ID but kept prompts, skills, or tool descriptions written for an older model.
- You need to pick a model and effort level and have (or can build) an eval.
- Unattended workloads run synchronously at full price.

## Instructions

### 1. Prompt cache
1. Measure first: check hit rates in Claude Console cache diagnostics, which explain misses; the cache
   diagnostics API shows where two requests diverged.
2. Order every request static-first: tools, then system prompt, then the growing conversation.
3. Keep the prefix byte-exact. Remove timestamps, IDs, and other volatile values; make tool definitions
   render in a stable order (tools render at the top, so any change breaks the cache).
4. Defer rarely used tools with `defer_loading` so they stay out of the cached prefix until tool search
   finds them.
5. Send mid-conversation system prompt changes as messages instead of editing the system prompt.
6. Don't change effort or thinking settings mid-conversation (they are part of the prefix). The source
   notes Opus 5 and Fable 5.1 allow mid-conversation effort updates without breaking the cache.
7. Fork carefully: subagents and branches share the parent's cache only with a byte-identical prefix, the
   same model, and the same effort.
8. Respect the TTL (5 minutes by default). For long tool or subagent waits, consider a 1-hour TTL on the
   prefix. A cache rewrite costs 1.25x input price (2x for a 1-hour cache).
9. Move the cache breakpoint as the conversation grows, or use automatic caching on the last cacheable
   block. Pre-warm at session start with a `max_tokens: 0` request carrying an explicit breakpoint.
10. Change model or effort only when the cache is already broken anyway (for example at compaction).

Full checklist: [references/prompt-cache-checklist.md](references/prompt-cache-checklist.md).

### 2. Instructions (prompt audit)
1. Scan prompts, skills, tool descriptions, and Claude Code config (CLAUDE.md, skills) for the anti-patterns
   in [references/prompt-anti-patterns.md](references/prompt-anti-patterns.md).
2. Remove or rewrite each hit; delete dated configuration such as manual thinking budgets that the
   platform may reject after an upgrade.
3. Or run `/claude-api prompt-audit` to do this automatically.

### 3. Effort
1. Sweep effort levels on your eval to learn the task's shape. A flat cost-performance curve on a
   non-saturated eval means thinking compute is not the bottleneck; more effort won't help.
2. Test a stronger model at lower effort; it can beat a weaker model at high effort.
3. Watch both failure modes: too high overthinks (cost, latency, sometimes lower quality); too low stops
   before gathering enough evidence (fewer tool calls, skipped checks).
4. `/claude-api hillclimb` automates the search: it splits the eval into train/test, proposes config
   changes, and reads failing train examples to fix them.

### 4. Holistic audit
Run `/claude-api cost-optimize`. It finds token usage from organization usage and cost reports (with an
Admin API key), logged usage objects, or by reading request-building code, then ranks levers: prompt
caching, trimming request content (including prompt-audit), bounding output, and batching unattended work
with the Batch API. Record findings with [templates/cost-audit-report.md](templates/cost-audit-report.md).

Benchmark numbers quoted in the source are in
[references/benchmark-results.md](references/benchmark-results.md).

## Examples

**Low cache hit rate in an agent**
> Diagnostics show the request diverges at the tool list. Tools are built from a dict whose order varies.
> Sort tool definitions deterministically, move a per-request timestamp from the system prompt into the
> latest user message, and defer three rarely used tools with `defer_loading`.

**Model migration**
> After switching from an older Opus to Opus 5.5, run `/claude-api prompt-audit`. It flags "double-check
> your work", "Be maximally thorough", a manual scratchpad section, and a retired thinking-budget setting.
> Remove them, then rerun the eval.

**Choosing a configuration**
> Run `/claude-api hillclimb` with the support eval. Compare a stronger model at low effort against a
> cheaper model at low effort plus added routing rules, and keep whichever wins on the held-out test set.
