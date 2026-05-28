**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
CodeRabbit describes how it built a planning-orchestration layer (powered by Claude) that runs before code generation, producing a structured plan/PRD the team can review to reduce “correct-looking but wrong” code outcomes.

## When is it useful?
Use this approach when AI-generated code can compile and pass tests yet still misses intent, or when requirements and assumptions are not written down explicitly before implementation.

## Key points
- Insert a structured planning phase before implementation to make assumptions explicit and align stakeholders.
- Treat the plan as a shared artifact and quality gate before code generation.
- Match model tiers to task complexity (Opus for orchestration, Sonnet for structured planning steps, Haiku for narrow tasks like context distillation).
- Evaluate plan quality with an evaluation harness (including judge-style scoring and downstream code outcomes such as extra scope and tokens to completion).

## Bundled resources
- A reusable “planning layer” prompt template for extracting outcomes, assumptions, edge cases, and validation checks.
- An example “collaborative PRD” outline teams can review before implementation.

## Source
- https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system
