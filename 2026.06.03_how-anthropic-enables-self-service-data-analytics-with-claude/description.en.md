**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Anthropic enables self-service data analytics with Claude

## What is this post?
This post explains how Anthropic uses Claude to automate the majority of internal business analytics requests, and why accuracy in analytics is mainly a context, retrieval, and verification problem (not just SQL generation).

## When is it useful?
Use this when you are building an agentic analytics workflow (or “analytics copilot”) that must answer questions from a data warehouse reliably, with safeguards against ambiguous entities, stale data, and missing retrieval context.

## Key points
- Analytics differs from software development: there is often a single correct answer tied to a specific, up-to-date entity in the data model.
- Three dominant failure modes are (1) concept–entity ambiguity, (2) data staleness, and (3) retrieval failure.
- Anthropic’s stack focuses on strong data foundations, explicit sources of truth, skill-based procedural guidance, and validation (offline evals + online monitoring).
- The appendix includes a concrete “warehouse skill” skeleton and a reference-doc skeleton for domain tables.

## Bundled resources
- A reusable “warehouse skill” skeleton (suitable for `skills/<skill-name>/SKILL.md`).
- A reusable reference-document skeleton (suitable for `skills/<skill-name>/references/*.md`).

## Source
- https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
