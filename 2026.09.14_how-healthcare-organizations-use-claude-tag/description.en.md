**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A best-practices article (September 14, 2026) by Camy Pearson, Maria Howe, and Araba Koomson on how
healthcare organizations use Claude Tag (beta, Claude in Slack) in workstreams that never touch protected
health information (PHI), with examples from Insight Health, Tennr, and Medallion.

## When is it useful?
- When a healthcare or regulated team wants an AI teammate in Slack but must keep PHI out of it.
- When choosing channels, connectors, and autonomy levels for a Claude Tag pilot.
- When looking for proven PHI-free use cases: incident response, internal tooling, payer-rule expertise.

## Key points
- Claude Tag is not yet covered by Anthropic's BAA, so it is used only in PHI-free channels and connectors.
- Admin controls: off by default, approved-channel allowlist, DMs disabled, per-channel connector scoping,
  access bundles that exclude the EHR, clinical systems, and patient communications. It sees only what
  the invoking member can see.
- Insight Health pairs Claude Tag with Zeus, a BAA-covered Agent SDK agent that masks PHI; 97% of
  critical-channel alerts closed without an engineer stepping in.
- Tennr uses Claude Tag as the main maintainer of an internal offer portal (15+ tickets in about a month).
- Medallion builds up payer-rule knowledge in a channel, tagging experts when Claude is unsure.
- Start with one channel and one or two connectors, connect GitHub, and pilot for two weeks.
- Credits ($25,000 Enterprise / $2,500 Team 10+ seats) expired October 1, 2026.

## Bundled resources
- Skill: `phi-safe-slack-agent-rollout` (`references/customer-patterns.md`,
  `templates/rollout-checklist.md`).

## Source
- https://claude.com/resources/articles/how-healthcare-organizations-use-claude-tag
