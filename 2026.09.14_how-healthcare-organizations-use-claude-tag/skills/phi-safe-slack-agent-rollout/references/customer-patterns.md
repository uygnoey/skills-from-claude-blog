# Customer patterns from the source article

## Insight Health — incident response
- Builds MagicDocs, an AI referral coordinator used by 1,100+ specialty practices across 56 specialties.
- Claude Tag runs in PHI-free engineering and support channels: investigating alerts, filing and
  de-duplicating tickets, reviewing PRs, carrying context across threads.
- Two-agent setup:
  - **Claude Tag**: access to the codebase and Linear.
  - **Zeus**: built on the Claude Agent SDK, runs on a BAA-covered Claude API organization, queries
    production data and masks PHI before it reaches Slack.
- Flow: investigate → root cause → draft PR → monitor tests → engineer reviews and merges.
- Result: since go-live, 97% of alerts in the critical alert channel closed without an engineer stepping in.
- Also used for hiring, vendor-negotiation prep, contract review against call transcripts, business ops.
- The CTO noted that everyone sees both agents' reasoning, which builds trust.

## Tennr — internal tooling
- Patient orchestration platform. In July 2026 launched an internal offer-presentation portal built in
  Claude Code, with Claude Tag as primary maintainer through a dedicated Slack channel.
- Recruiters, People team, hiring managers, and RevOps request changes in plain language; Claude ships,
  deploys, and reports back.
- About a month: 15+ tickets shipped (benefits section built from a PDF, a "Sign your offer here" banner,
  target bonus fields, admin controls).
- Claude locked down a publicly exposed copy API the same day it was flagged, fixed an import bug that
  reset equity on live offers, and posted a channel-wide notice about a variable-comp display bug.
- Team taught conventions: emoji status legend, numbered ticket format.
- Per-channel scoping: full autonomy in the offer-tool channel; Product and Eng channels more limited.

## Medallion — payer expertise
- Automates provider credentialing, licensing, and payer enrollment.
- Claude Tag answers engineers' payer-rule questions from past expert responses, historical data, and
  internal resources, so knowledge accumulates in the channel instead of with one person.
- When not confident, it tags the right expert; that answer becomes the basis for future answers.
- Rollout rationale: PHI-free workstreams, expert review, automated downstream validation. Works at the
  policy level, not on individual patients or providers.
