**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Anthropic's cybersecurity team built a threat detection platform with Claude Code

## What is this post?

A May 11, 2026 case study by Jackie Bow, Technical Lead of Anthropic's Detection Platform Engineering team, on how her team built **CLUE (Claude Looks Up Evidence)** — a detection-and-response platform with two surfaces (CLUE Triage and CLUE Investigate) that uses Claude as a natural-language interface over Anthropic's internal systems. The post details what they shipped, how they measured impact (false-positive rate, query/tool-call volume, time saved), and how their philosophy shifted from SOAR-style scripted playbooks toward giving Claude boundaries and letting it choose its own investigation paths.

## When is it useful?

- When a defensive security team is deciding whether to build a Claude-powered triage/investigation surface on top of their SIEM and internal systems.
- When designing the boundary between deterministic playbooks and agent-driven investigation, and the data-governance scope that an agent can read.
- When packaging a business case for an internal detection platform: alert volume, false-positive reduction, hours saved, coverage of low-confidence signals.
- When framing how organizational context (Slack, internal docs, data warehouse, code repos) plugs into a security agent through tools.

## Key points

- CLUE Triage performs first-pass triage on every incoming alert and enriches it with Slack, internal docs, code, and data warehouse context; analysts get a disposition plus confidence score.
- CLUE Investigate exposes a natural-language query interface; Claude runs an agentic loop where an orchestrator dispatches sub-agents that issue queries in parallel and synthesize findings.
- Reported impact: false-positive rate dropped from ~1 in 3 to **7%**; over 30 days CLUE automated ~**12,000 queries and 27,000 tool calls**, ~**1,870 hours / 234 person-days** of manual work, for **5–10× time savings**; CLUE averages ~25 tool calls and ~11 queries per investigation.
- Built with Claude Code as a "design partner and collaborator": proof of concept in a day, design and implementation within a week.
- Philosophy: encode boundaries (what tools and data Claude can access) but leave strategy open — Claude often finds investigation paths a human would not have prescribed.
- Forward-looking: move from reactive alerting to continuous proactive hunting, treat the investigation transcript corpus as organizational memory, and embrace non-determinism by running multiple investigation strategies in parallel.

## Bundled resources

- `skills/clue-style-detection-platform-playbook/SKILL.md` — how to plan a CLUE-style detection platform: surfaces, agentic loop shape, context sources, metrics, and governance.
- `skills/clue-style-detection-platform-playbook/references/clue-architecture-from-post.md` — verbatim catalog of components, metrics, and quotes from the source post.
- `skills/clue-style-detection-platform-playbook/examples/data-governance-investigation.md` — worked example mirroring the post's contractor data-governance scenario.

## Source

- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity) (Anthropic blog, May 11, 2026)
