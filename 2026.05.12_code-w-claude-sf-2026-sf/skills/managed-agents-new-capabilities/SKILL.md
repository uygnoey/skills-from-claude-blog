---
name: managed-agents-new-capabilities
description: Adopt the four capabilities Anthropic shipped to Claude Managed Agents at Code w/ Claude SF 2026 — Dreaming (scheduled memory curation from past sessions), Multiagent orchestration (a lead agent delegating to parallel specialist subagents on a shared filesystem), Outcomes (a separate grader scoring each result against a developer-defined rubric until the bar is met), and Webhooks (async completion notification). Use when a team building on Claude Managed Agents needs to decide which of these to turn on, in what order, and how they fit a production pipeline.
---

# Managed Agents — new capabilities playbook (Code w/ Claude SF 2026)

This skill packages the four Claude Managed Agents capabilities announced at Code w/ Claude SF 2026 — Dreaming, Multiagent orchestration, Outcomes, and Webhooks — plus the rate-limit changes called out in the same post (doubled Claude Code rate limits, raised Claude Opus API limits). It does not invent product behavior beyond what is in the source post; for anything outside that surface (pricing, SLAs, configuration details), point the user to the Claude Console and the source blog.

## Instructions

When the user is planning or revisiting a Claude Managed Agents deployment in light of this announcement:

1. **Confirm scope.** This skill applies to **Claude Managed Agents on the Claude Platform**. If the user is on Claude Code or Cowork without Managed Agents, the new memory/orchestration/grader/webhook features described here are not the same thing — refer them to the source post and the Claude Console docs.

2. **Pick which of the four to turn on first.** Use this default ordering when the user is starting from scratch:
   1. **Outcomes** — gives every other capability a quality bar to grade against. Anthropic reports up to a 10-point lift on the hardest internal benchmarks when outcomes are wired in.
   2. **Multiagent orchestration** — once an outcome exists, splitting the work across a lead agent plus parallel specialist subagents (each with its own model, prompt, tools) becomes safer because each branch can be graded.
   3. **Webhooks** — once outcomes drive the run to completion, webhooks replace polling for downstream systems.
   4. **Dreaming** — turn on after you have run sessions worth learning from; Dreaming reviews past sessions, surfaces patterns, and curates memory so subsequent runs improve.
   See [`references/announcements-from-post.md`](./references/announcements-from-post.md) for the verbatim feature descriptions.

3. **Use the rubric → grader → revision loop for Outcomes.**
   - Developer defines the rubric for what a "good" output looks like.
   - A separate grader evaluates each result **in its own context window**.
   - The agent revises until the grader's bar is met.
   - Recommend keeping the grader rubric short and explicit (acceptance criteria, hard constraints, format requirements) so the grader's judgment is reproducible.

4. **Design multiagent flows around a shared filesystem.**
   - There is one lead agent that delegates.
   - Specialist subagents run **in parallel** on a **shared filesystem**, each free to pick its own model, prompt, and tools.
   - Treat the filesystem as the contract between agents — every subagent reads inputs and writes outputs as files rather than passing state through prompts.
   - The full flow is traceable in the **Claude Console**; route the user there for debugging instead of reconstructing traces by hand.

5. **Wire webhooks instead of polling.** Once an outcome is defined and the agent can run to completion on its own, replace any polling loop in the user's system with a webhook handler. The post does not specify webhook payload shape — direct the user to the Claude Console docs for the schema.

6. **Stage Dreaming carefully.**
   - Dreaming is a **scheduled** process — it runs between agent sessions, not inside them.
   - It curates memory based on patterns it sees in **past sessions**.
   - Recommend turning it on only after the team has accumulated session history they would actually want reflected in memory; turning it on too early risks fossilizing early mistakes into long-term memory.

7. **Capacity check.** Remind the user of the rate-limit changes in the same announcement:
   - Claude Code rate limits **doubled**.
   - Claude Opus **API limits raised**.
   - Both live as of May 12, 2026.
   These reduce friction for scaled multiagent flows but the post does not state the exact new numerical limits — direct the user to the Claude Console.

8. **Hand off cleanly.** When asked anything outside the four capabilities and the rate-limit changes — for example, pricing, region availability, security artifacts, exact webhook schemas, or specific customer numbers — say so and point at the [source post](https://claude.com/blog/code-w-claude-sf-2026-sf) and the recorded sessions linked from it.

## Examples

### Example 1 — sequencing the four features

> "We just got access to all four. What do we turn on first?"

Walk through the default ordering above: Outcomes → Multiagent orchestration → Webhooks → Dreaming. Explain that Outcomes goes first because everything downstream benefits from having a graded quality bar, and Dreaming goes last because it learns from history you have not yet accumulated.

### Example 2 — designing a research-and-write agent

> "We want a lead agent that researches a market and writes a brief."

Decompose into:
- **Lead agent** — orchestrates and assembles the final brief.
- **Specialist subagents** running in parallel on a shared filesystem:
  - One pulls source material and writes `notes/sources.md`.
  - One drafts each section into `draft/<section>.md`.
  - One runs a style/factual pass and writes `review/<section>.md`.
- **Outcome rubric** for the lead agent: structure, citation count, factual consistency, length, format.
- **Webhook** fires when the lead agent's output satisfies the outcome grader.
- **Console** is where to debug if a branch stalls.

See [`examples/outcomes-and-multiagent-patterns.md`](./examples/outcomes-and-multiagent-patterns.md) for the worked version.

### Example 3 — declining to invent

> "What's the exact request-per-minute limit on Claude Opus now?"

Reply that the post says Claude Opus API limits were raised but does not state the exact numbers; direct the user to the Claude Console for the live limits.

## Bundled resources

- [`references/announcements-from-post.md`](./references/announcements-from-post.md) — verbatim list of announcements and customer references from the post.
- [`examples/outcomes-and-multiagent-patterns.md`](./examples/outcomes-and-multiagent-patterns.md) — worked patterns combining Outcomes, Multiagent orchestration, and Webhooks.

## Source

- [Code w/ Claude SF 2026: Building on the AI exponential](https://claude.com/blog/code-w-claude-sf-2026-sf) (Anthropic blog, May 12, 2026)
