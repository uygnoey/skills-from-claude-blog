**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A post explaining why Claude Opus 5.5 — estimated to cost about 40% less than Opus 5 for typical
token-billed workloads — saves the most on long, context-heavy Claude Code sessions. It shares
aggregate Claude Code usage trends from March to September 2026, then breaks the savings into
pricing, better cache use in the Claude Code harness, and fewer turns, and closes with habits that
protect cached reads.

## When is it useful?
- When token-billed Claude Code spend is growing and you want to know where it goes.
- When sessions run long or unattended and you want to keep cache hits high.
- When deciding which tasks are worth giving to Opus 5.5.

## Key points
- Trends (Mar→Sep 2026): Claude works 3.3× longer per prompt with 40%+ more model calls and 68%
  fewer interruptions; tool servers and skills are about twice as common; context per request grew
  2.6×; the input:output ratio went from 189:1 to 324:1.
- Pricing: input and output tokens −20%, cached reads −60%. Cache reads are most of agentic coding
  cost, so the cut matters more as context grows.
- Claude Code harness: cache-missing input fell by more than 50%; the cache is harder to break
  (login refresh, mid-conversation instructions, on-demand tool loading); effort can change
  mid-session without a cache reset on Opus 5.5 and Fable 5.1; one-hour cache lifetime for API and
  cloud users; forked subagents reuse the parent's cache.
- Fewer turns: Zeta Labs saw fewer turns and tool calls at nearly half the cost and twice as many
  hardest tasks completed. Gains are largest on open-ended tasks; measure on your own codebase.
- Output generation is more than 30% faster than Opus 5.
- Habits: run `/usage` to see your cached-read share; pick the model at session start; compact
  before stepping away; set the one-hour cache lifetime on API keys/cloud providers.

## Bundled resources
- Skill: `protect-cached-reads` — habits for keeping long Claude Code sessions cache-efficient and
  choosing work for Opus 5.5, with a reference of the usage trends and pricing figures.

## Source
- https://claude.com/resources/articles/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
