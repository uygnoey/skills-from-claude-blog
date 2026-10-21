**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A customer story about Cresta, a customer experience (CX) AI company, and Conductor — a
natural-language agent builder for production-ready CX agents, built on the Claude Agent SDK. Users
describe what they want, and Conductor guides them through blueprint, implementation, evaluation,
and optimization.

## When is it useful?
- When a team with domain expertise wants to turn it into an agent-building product.
- When deciding what to build in-house versus rely on the Claude Agent SDK.
- When setting up an evaluation loop to catch improvements and regressions on model upgrades.

## Key points
- The Claude Agent SDK is the general-purpose execution harness (context gathering, tool calls,
  writing and running code); Cresta's CX workflows, tools, and domain context sit on top. Cresta
  evaluated it for data privacy, tenant architecture, org-level key distribution, controls, and
  observability.
- Historical conversations show where a human should stay in the loop and where the model can
  adapt. Enterprise-critical workflows, especially in regulated industries, are hardened with
  explicit rules that are tested and revised.
- Build tasks (create an agent, write a test case, change an agent, root cause analysis) are scored
  on outcome, execution path, quality vs. a curated reference, and resource use — and rerun on every
  new model or framework change.
- Early use reportedly cut initial deployment time roughly in half. Builders share proven patterns
  as skills.
- Lessons: dogfood until output matches an expert engineer; invest only in unique advantages; decide
  what must be deterministic; the first build is ~20% of the effort, iteration is ~80%.

## Bundled resources
- Skill: `domain-agent-builder` — plan for building a domain agent builder on the Claude Agent SDK,
  with a build-task scorecard template.

## Source
- https://claude.com/resources/articles/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk
