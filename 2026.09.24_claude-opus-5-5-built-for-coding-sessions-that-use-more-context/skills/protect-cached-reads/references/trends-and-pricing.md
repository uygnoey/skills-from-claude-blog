# Claude Code usage trends and Opus 5.5 economics

Figures as stated in the source post (published 2026-09-24).

## Usage trends, March → September 2026 (aggregate Claude Code data)

Prompts per session stayed steady, but:

| Metric | Change |
|---|---|
| Time Claude works per prompt | 3.3× longer |
| Model calls per prompt | more than 40% more |
| Interruptions | 68% fewer |
| Tool server connected or skill used | about 2× as likely |
| Pasting text into a prompt | about a third less likely |
| Context per request | 2.6× larger |
| Input : output token ratio | 189:1 → 324:1 |

Interpretation from the post: developers aim a harder-working, better-informed Claude at bigger,
more open-ended tasks, so the economic impact of context engineering compounds.

## Why Opus 5.5 is cheaper for long, context-heavy sessions

Estimated about **40% cheaper to run than Opus 5** for typical token-billed workloads, with the
largest difference on longer, higher-context sessions. Three contributing changes:

### 1. Pricing
- Input and output tokens: **−20%**.
- Cached-token reads: **−60%**. Cache reads make up the majority of agentic and coding costs, and
  because context per request keeps growing, the same price cut saves more on today's traffic than
  it would have six months earlier.
- At publication, a cached token on Opus 5.5 cost a fifth of competing models' price.

### 2. Claude Code uses the cache better
- Despite longer sessions, input that misses the cache **fell by more than 50%**.
- Harder to break the cache accidentally (e.g., refreshing a login) or with larger actions (adding
  instructions mid-conversation, loading tools on demand).
- Effort level can change mid-session without resetting cache on newer models (Opus 5.5, Fable 5.1).
- One-hour cache lifetime available to API-key and cloud-provider users.
- Forked subagents start from the parent's cache.

### 3. Fewer turns
- Opus 5.5 can need fewer turns for the same task. Zeta Labs reported fewer turns and tool calls per
  task than Opus 5, at nearly half the cost, with twice as many of their hardest tasks completed.
- The gap is biggest on open-ended tasks and negligible on well-scoped ones; measure on your own
  codebase.
- Output generation is more than 30% faster than Opus 5 — no token savings, but less waiting on long
  runs.
