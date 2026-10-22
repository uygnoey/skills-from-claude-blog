**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement (October 22, 2026) that Claude Models on Google Cloud (Anthropic managed) is generally
available: Google Cloud customers get the full Claude Platform feature set with Google Cloud IAM,
billing, and commitment retirement. Claude also stays available via the Google managed offering.

## When is it useful?
- When a Google Cloud customer must choose between the Anthropic managed and Google managed offerings.
- When a team wants new Claude features and betas on day one without leaving Google Cloud.
- When planning billing, IAM, and discount handling before onboarding.

## Key points
- Anthropic managed: full Claude API features, with new features and betas shipping the same day as on
  the native Claude Platform. Anthropic operates the service and is the data processor.
- Works with existing Google Cloud IAM credentials; billed on one Google Cloud invoice; draws down the
  Google Cloud commitment. Currently US and Global endpoints.
- Included: Managed Agents (beta), code execution, computer use, agent skills, advisor strategy (beta),
  Files API, citations, web search and web fetch, MCP connector (beta), prompt caching, batch processing.
- Fast Mode on Claude Opus 5.5 is GA here: up to 2.5x faster output, $8 / $40 per million input /
  output tokens.
- Claude Console access for prompts, agent configuration and hosted runs, usage/cost monitoring, and
  per-workspace access control. Models: Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5.
- Google managed remains the choice when Google must be the data processor, strict regional residency
  applies, or native integrations like Model Armor or Agent Engine are needed.
- Existing discounts: contact your account executive first; discounts are not applied retroactively.

## Bundled resources
- Skill: `google-cloud-offering-selector` (`references/feature-matrix.md`,
  `templates/offering-decision.md`).

## Source
- https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
