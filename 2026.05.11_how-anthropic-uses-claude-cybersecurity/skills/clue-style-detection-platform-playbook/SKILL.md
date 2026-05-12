---
name: clue-style-detection-platform-playbook
description: Plan a Claude-powered detection and response platform in the style of CLUE (Claude Looks Up Evidence), the internal platform Anthropic's Detection Platform Engineering team built with Claude Code. Use when a defensive security team is deciding whether to wrap their SIEM and internal systems with a triage surface and a natural-language investigation surface, where to set the deterministic-vs-agentic boundary, what context sources to plug in via tools, and how to measure impact (false-positive rate, query and tool-call volume, hours saved, coverage of low-confidence signals).
---

# CLUE-style detection platform playbook

This skill packages the architecture and operating philosophy described in Anthropic's "How Anthropic's cybersecurity team built a threat detection platform with Claude Code" post. It does not invent product details beyond what the post states; when a question goes past the source surface, route the user to the post or the [Anthropic Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) the post references.

## Instructions

When the user is scoping a Claude-powered detection-and-response platform, work through these steps in order:

1. **Confirm the team's posture is defensive.** The source platform is for detecting threats and responding to potential breaches — not for probing vulnerabilities. Recommend keeping that scope explicit in the platform's charter, the way Anthropic's team does.

2. **Plan two surfaces, not one.** The post describes two complementary components — design both, or be explicit about which you are skipping.
   - **Triage surface (CLUE Triage analogue).** Auto-enriches every incoming alert with organizational context and assigns a disposition (`false positive`, `true positive`, `malicious`, `expected behavior`) plus a confidence score. Analysts read the enriched alert, not the raw one.
   - **Investigate surface (CLUE Investigate analogue).** Natural-language query interface. The analyst asks questions; Claude runs an orchestrator/sub-agent loop that issues parallel queries against internal systems and synthesizes a written investigation.

3. **Wire the right context sources as tools, not as scraped exports.** The source post explicitly lists what mattered:
   - Slack messages (planned-maintenance context, team discussion).
   - Internal documentation.
   - Code repositories (what a service actually does).
   - Data warehouse / security-critical logs (baseline behavior).
   The point of internal context is exactly what an external security platform cannot see. Surface this as the deciding factor when the user asks "why build this instead of buy."

4. **Encode boundaries, leave strategy open.** This is the philosophical core of the post. Codify what tools Claude can call and what data it can read; do not encode the order in which it must investigate. The source explicitly contrasts this with the SOAR instinct to "build playbooks, define every step, make the process deterministic."

5. **Use a published metric set from day one.** The source quantifies impact with a specific small set — use the same set so a business case is comparable:
   - False-positive rate before/after (the post: ~1 in 3 → 7%).
   - Total queries automated and total tool calls over a window (the post: ~12,000 queries and 27,000 tool calls in 30 days).
   - Hours / person-days of manual work avoided (the post: ~1,870 hours, ~234 person-days, 5–10× time savings).
   - Average tool calls and queries per investigation (the post: ~25 tool calls, ~11 queries).
   - Coverage of low-confidence signals that previously went unexamined.
   - Note that accuracy is **harder** to measure than speed: the source post explicitly says the team is still building feedback loops to know when Claude caught something analysts would have missed and vice versa.

6. **Use transcripts as auditable evidence and as a learning corpus.** Every investigation should produce an auditable transcript: the queries Claude ran, the tools it called, the conclusions it drew. Use those transcripts for two purposes:
   - **Audit** — analysts and reviewers can replay reasoning.
   - **Organizational memory** — the corpus is something Claude itself can later query for patterns in how past investigations unfolded.

7. **Plan the roadmap explicitly along three lines named in the post:**
   - **Reactive → proactive.** Move from "an alert fires, Claude investigates" to continuous hunting agents that look for behaviors that don't match any written rule.
   - **Learning from itself.** Treat the transcript corpus as a knowledge base.
   - **Embracing non-determinism.** Run multiple investigation strategies in parallel and compare; treat divergent results as a signal rather than a bug.

8. **Hand off cleanly when out of scope.** Do not invent Anthropic-internal architecture details, exact tool integrations, model selection rules, or governance policies that the post does not state. The post says results were generated using Claude Sonnet and Opus models — do not extrapolate which model handles which task. For anything outside the source, point the user to the post and the [Anthropic Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy).

## Examples

### Example 1 — picking the boundary

> "Should we write a playbook that tells Claude what queries to run for a failed-login alert?"

Recommend the source's posture: do not script the queries. Instead, give Claude:
- The alert payload.
- A tool to query the relevant log store.
- A tool to read the user's recent Slack mentions and on-call docs.
- A tool to look up the user's baseline behavior in the data warehouse.
Let Claude pick its own sequence. Audit via the transcript. The post explicitly notes Claude often surfaces context a human analyst would have missed when given latitude.

### Example 2 — making the business case

> "We need a one-pager for leadership."

Use the post's metric structure:
- False-positive rate before/after (target: bring 1-in-3 toward single digits).
- Hours of manual triage avoided per month.
- Coverage of low-confidence signals previously dropped.
- Speed of complex investigations (the post says investigations that took hours now run in 3–4 minutes).
Frame transcripts as the audit story for compliance.

### Example 3 — declining to invent

> "Which model does CLUE use for what?"

Reply that the post only states results were generated using Claude Sonnet and Opus models, without per-component assignment, and point the user to the [source post](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity).

## Bundled resources

- [`references/clue-architecture-from-post.md`](./references/clue-architecture-from-post.md) — verbatim catalog of CLUE components, metrics, and quotes from the source.
- [`examples/data-governance-investigation.md`](./examples/data-governance-investigation.md) — worked example following the contractor data-governance scenario described in the post.

## Source

- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity) (Anthropic blog, May 11, 2026)
- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)
