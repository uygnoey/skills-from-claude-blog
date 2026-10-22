---
name: agent-scale-ci-test-selection
description: Design or rescue a CI test impact analysis (test selection) service for agent-driven development, based on Anthropic's experience after CI jobs grew ~25x in six months. Covers the listener/selector architecture, why listener lag means stale selection, recognizing when quick fixes (bigger machine, per-package sharding, restarts) are buying less time each round, the stateless redesign (listener workers append to a journal in an in-memory store, a small consumer rolls it up into per-test history every few seconds, the selector reads that history), and the planning rules - assume 25x load within two quarters, design v0 for 10-20x perceived scale if budget allows, keep state out of the process, avoid single-instance critical services, and instrument services so Claude can diagnose and tune them (jobs in must equal jobs out). Use when CI is straining under agent-generated PRs, when a test selection service lags or hits memory limits, or when designing CI infrastructure for exponential growth.
---

## Purpose
Agents write and review more code, in smaller PRs, around the clock. That multiplies CI jobs. A test
impact analysis service that was fine for human-paced development becomes the next bottleneck. This
skill captures how Anthropic's service broke, which patches bought less and less time, the redesign
that held, and the planning rules the author would apply from day one.

## When to use
- CI job volume is climbing faster than headcount because of agent-authored PRs.
- A test selection / test impact analysis service is lagging, paging, or hitting memory limits.
- You are deciding between another patch and a redesign.
- You are designing a v0 CI service and need to size for agent-era growth.

## Instructions

1. **Prefer test selection over run-everything.** Running every test on every change does not scale:
   gates get long, expensive, and untrustworthy. Agents also need a specific set of valid tests to
   self-verify and iterate; humans can ignore irrelevant failures, agents need more context.

2. **Model the service as listener + selector.**
   - Listener: records test results from every CI run.
   - Selector: reads result history and decides which tests run on each opened PR (based on past
     performance and package relevance).
   They must stay in sync. Measure **listener lag** as a first-class signal.

3. **Know what lag costs.** At agent-era volume, small lag is large: 20 minutes of lag can mean tens
   of thousands of test updates not applied. Consequences:
   - A bad change merges and a test starts failing for everyone, causing redundant investigations.
   - A flaky dependency's reds start blocking merges.
   - A fixed or newly added test does not run until the listener catches up, risking regressions.
   A listener that falls behind does not mean untested code shipped; it means selection runs on stale
   data.

4. **Watch the half-life of patches.** Common fixes still work, but each buys a fraction of the time
   it used to. Anthropic's sequence: double the cores (~70 days), shard state per package with a
   worker each (29 days), daily restarts after hitting memory limits (<1 day, and restarts made the
   service drift further behind). See [references/scaling-timeline.md](references/scaling-timeline.md).
   When the window shrinks like this, stop patching.

5. **Redesign so workers are stateless.** The fix that held:
   - Move state into an in-memory data store.
   - Any listener worker processes any result, appends it to a **journal**, and moves on, holding
     nothing in memory, so workers scale horizontally.
   - A small separate **consumer** rolls the journal up into per-test history every few seconds.
   - The **selector** looks up that history quickly.
   This costs more to run, but it is easier to scale and memory-profile than a singleton. Expect to
   tune journal size and worker count; Claude did much of this autonomously.

6. **Use an agent as a long-running monitor.** A dedicated long-running Claude Tag session pinged the
   engineer when listener lag passed 50,000 jobs and resumed the conversation with context of past
   efforts. If Claude keeps arguing for an overhaul, take it seriously.

7. **Plan for the exponential** (the author's "do differently" list):
   - Assume 25x load within two quarters, whether you build or buy.
   - If budget allows, design v0 for 10-20x the perceived scale.
   - Keep state out of the process from the start.
   - Avoid running any critical service as a single instance unless you can measure it and any
     canary changes.
   - Instrument services as Claude's eyes and ears so it can hill-climb fixes; in particular, ensure
     CI jobs in equals CI jobs out.
   - Expect more, smaller PRs from agents, a higher overnight/weekend activity floor, and bursts
     still driven by human approvals.

Run the review in [templates/ci-scaling-review.md](templates/ci-scaling-review.md) before choosing
another patch.

## Examples

**Example 1 — Patch or redesign?**
A team's selector service was scaled up 3 months ago and sharded 1 month ago; now it OOMs every
afternoon. Using step 4, the shrinking patch window says redesign: move per-test history into an
in-memory store with journal + roll-up consumer, and make listener workers stateless.

**Example 2 — Sizing a v0**
A new CI results service is expected to see 2,000 jobs/day. Following step 7, design so the same
architecture can absorb 25x within two quarters (stateless workers, external state, in/out job
counters exposed as metrics) rather than a single-process writer.

**Example 3 — Agent monitoring**
Set up a long-running agent session that watches listener lag and job in/out counts, alerts above a
threshold (Anthropic used 50,000 jobs), and keeps the history of what has been tried.

## Source
- https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
