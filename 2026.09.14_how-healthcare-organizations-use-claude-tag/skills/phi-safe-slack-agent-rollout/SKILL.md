---
name: phi-safe-slack-agent-rollout
description: Plan and run a rollout of Claude Tag (beta, Claude in Slack) inside a healthcare organization so it never touches protected health information (PHI) - modeled on the September 2026 article "How healthcare organizations use Claude Tag" with examples from Insight Health, Tennr, and Medallion. Covers admin controls (off by default, channel allowlist, DMs disabled, per-channel connector scoping, access bundles that exclude the EHR and clinical systems), pairing with a separate BAA-covered agent that masks PHI, choosing PHI-free workstreams (incident response, internal tooling, payer-rule expertise), per-channel autonomy levels, and a start-small two-week pilot. Use when a healthcare or other regulated team wants an AI teammate in Slack but must keep regulated data out of it.
---

## Purpose
Claude Tag brings Claude into Slack as a teammate. The source notes that Claude Tag is **not yet covered
by Anthropic's Business Associate Agreement (BAA)**, so healthcare organizations use it only in channels
and with connectors that never touch PHI. This skill turns the article's admin controls, customer
patterns, and getting-started advice into a rollout procedure.

## When to use
- A healthcare (or similarly regulated) organization wants Claude in Slack for engineering, ops,
  support, or recruiting work.
- You must prove to security/compliance that the agent cannot reach PHI.
- You are deciding which channels get which connectors and how much autonomy.

## Instructions

1. **Pick PHI-free workstreams first.** The article's three patterns (details in
   [references/customer-patterns.md](references/customer-patterns.md)):
   - Incident response: investigate alerts, find root cause, open a draft PR, monitor tests; an engineer
     reviews and merges.
   - Internal tooling: non-technical staff request changes in plain language; Claude ships, deploys,
     and reports back in a dedicated channel.
   - Domain expertise: answer policy-level questions (e.g. payer rules) from past expert answers and
     internal resources; tag in a human expert when not confident.
2. **Lock down the workspace with admin controls** (checklist in
   [templates/rollout-checklist.md](templates/rollout-checklist.md)):
   - Keep Claude Tag off by default; enable it only in approved channels.
   - Disable DMs; prefer open threads.
   - Scope connectors per channel.
   - Remember Claude Tag only sees what the invoking member can see; it can read and search public
     channels but not private channels it was not invited to.
   - Use access bundles to connect sources such as the codebase and issue tracker while leaving the EHR,
     clinical systems, and patient communications inaccessible.
3. **If production data is needed, put a BAA-covered agent in between.** Insight Health pairs Claude Tag
   (codebase + Linear) with a second agent built on the Claude Agent SDK, running on a BAA-covered
   Claude API organization, which queries production data and masks PHI before anything reaches Slack.
4. **Set autonomy per channel.** Tennr gave full autonomy in its offer-tool channel while keeping Product
   and Eng channels more limited.
5. **Keep humans in the loop where it matters.** Engineers review and merge PRs; experts answer when
   Claude is unsure, and those answers become the basis for future ones; add automated downstream
   validation (Medallion's rationale).
6. **Let the team teach conventions in-channel** (e.g. Tennr's emoji status legend and numbered ticket
   format) so Claude follows them.
7. **Pilot small, then widen.** Start in one engineering, product, ops, or recruiting channel with one or
   two connectors and open threads. Read Anthropic's healthcare best-practices guide, enable Claude Tag
   in an alert or support-engineering channel, connect GitHub, and let the team use it for two weeks
   before widening the allowlist.

## Examples

**Alert channel pilot**
> Enable Claude Tag only in `#alerts-critical` and `#support-eng`, connectors: GitHub + issue tracker.
> DMs off. EHR and patient-messaging systems excluded from the access bundle. Claude investigates each
> alert, files or de-duplicates a ticket, and opens a draft PR; an on-call engineer reviews and merges.
> Review after two weeks before adding channels. (Insight Health reports 97% of alerts in its critical
> channel closed without an engineer stepping in since go-live.)

**Policy-level knowledge channel**
> In an engineering Q&A channel, Claude answers payer-rule questions from prior expert answers and
> internal docs. When not confident it tags the payer expert; the expert's reply is reused next time.
> No individual patient or provider data is involved.

## Notes
- Credits mentioned in the article (Enterprise orgs that activate and link GitHub: $25,000; Team orgs
  with 10+ seats: $2,500) expired on October 1, 2026.
- For security and data-handling details, see the official docs referenced by the article (original
  article).
