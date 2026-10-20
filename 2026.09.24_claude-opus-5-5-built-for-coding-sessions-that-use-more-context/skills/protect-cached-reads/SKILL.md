---
name: protect-cached-reads
description: Keep long, context-heavy Claude Code sessions cost-efficient by protecting prompt-cache hits — check how much usage is cached reads with /usage, pick the model at session start, compact before stepping away, and set the one-hour cache lifetime on API keys or cloud providers. Use when token-billed Claude Code costs are rising, when sessions run long or unattended, or when deciding which work to point Claude Opus 5.5 at.
---

## Purpose
Claude Code sessions have become longer and read far more context per request, so most of the bill
is now re-read context. Cached reads are much cheaper than uncached input, and a reduced turn is
cheaper still. This skill turns the post's guidance into habits that keep as much context as
possible coming from cache, and points Opus 5.5 at the work where those habits compound.

## When to use
- Token-billed (API key or cloud provider) Claude Code spend is growing.
- Sessions run long, unattended, or with delegated/forked subagents.
- You are choosing which tasks to give Opus 5.5 versus other models.
- You want to explain why long sessions cost what they do (see
  [references/trends-and-pricing.md](./references/trends-and-pricing.md)).

## Instructions

1. **Measure first.** Run `/usage` in Claude Code to see how much of your usage is cached reads.
   That share is the number to protect.

2. **Make sure the context is necessary.** Claude reads more tokens per request than it used to;
   every piece of context you provide should earn its place, and as much of it as possible should be
   read from cache.

3. **Pick your model at the start of a session** rather than switching midway.

4. **Compact before you step away, not after.**

5. **On an API key or cloud provider, set the one-hour cache lifetime for long sessions.**
   (Subscribers already had it.)

6. **Lean on harness behaviors that preserve cache.** Recent Claude Code changes make the cache
   harder to break:
   - Small papercuts such as refreshing a login no longer break it, nor do larger actions such as
     adding instructions mid-conversation or loading tools on demand.
   - On newer models (Opus 5.5, Fable 5.1) you can change effort level mid-session without resetting
     the cache.
   - Forked subagents start from the parent's cache instead of paying for the same context again.

7. **Point Opus 5.5 at open-ended, context-heavy work.** On well-scoped, mechanical tasks models
   finish in about the same number of turns and the price cut is the only saving. On open-ended
   tasks Opus 5.5 can avoid spending many turns on the wrong idea, and a saved turn is worth more
   than a cached token. No single number holds for every codebase — measure on your own tasks.

## Examples

**Example 1 — Long refactor session on an API key.**
Start the session on Opus 5.5 and stay on it. Set the one-hour cache lifetime. Raise effort for a
hard section mid-session instead of switching models. Before a lunch break, run compaction, then
leave. Afterward, check `/usage` to confirm cached reads remain the bulk of input.

**Example 2 — Choosing what to delegate.**
A batch of mechanical renames: either model takes similar turns, so savings come only from price.
An open-ended "find why this flaky integration test fails" investigation: give it to Opus 5.5, where
fewer wasted turns compound with cheap cached reads.

**Example 3 — Fan-out with subagents.**
Use forked subagents for parallel investigation so each starts from the parent's cache rather than
re-reading the same context at full price.

## Source
- https://claude.com/resources/articles/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
