**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An interview with Philip Martin, Uber's CISO, on why AI agents need the same kind of insider threat
program companies already run for employees, how frontier models change security work, and how
Uber's open-source AI Detection and Response (ADR) tooling works alongside Anthropic's Enterprise
Frontier Safeguards.

## When is it useful?
- When designing monitoring, detection, and response for AI agents inside a company.
- When combining your own agent telemetry with a model provider's safeguard signals.
- When deciding where defenders should focus next in securing AI systems.
- When making the case to leadership for monitoring frontier-model deployments.

## Key points
- Frontier models can take in much more context over long horizons (code, design docs, Jira issues,
  service history), producing very specific threat models and security reviews. Martin expects
  per-service agents that exchange threat models with each other.
- Enterprise Frontier Safeguards: Uber keeps control of its data (not accessible to Anthropic without
  permission) and of what happens after a safeguard triggers.
- Uber's AI security architecture: an LLM gateway as perimeter, open-sourced ADR for real-time
  telemetry and action in agent harnesses, and provider classifier output integrated into the
  detection environment.
- Priority 1: real-time detection and intervention, as close as possible to a person entering a
  prompt or a model calling a tool.
- Priority 2: understand emerging patterns — discover new behaviors, build safeguards, repeat
  (constraints create new behaviors).
- Every company runs an insider threat program for people; models introduce the same risk, so they
  need the equivalent.

## Bundled resources
- Skill: `ai-insider-threat-program` — layered architecture, real-time intervention, behavior-discovery
  loop (`references/ai-security-architecture.md`).
- Guide: "Securing AI agents like insiders" (4 languages).

## Source
- https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
