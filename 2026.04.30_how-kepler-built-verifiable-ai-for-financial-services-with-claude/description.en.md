**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A case study on Kepler Finance, a financial-services research platform that combines Claude for interpretation and reasoning with deterministic infrastructure that verifies every number back to the exact source document, page, and line item.

## When is it useful?
When you need patterns for building auditable, regulated AI systems (especially for finance) that must be verifiable and accountable, and for designing architectures that separate probabilistic reasoning from provably-correct computation and provenance.

## Key points
- Kepler pairs Claude’s reasoning with a deterministic trust/verification layer (retrieval, computation, and assembly) to make answers traceable and auditable.
- The system decomposes work into multi-stage pipelines and matches models to stages (complex reasoning vs. high-throughput constrained tasks).
- Strong content engineering (structured domain knowledge, definitions, boundaries) plus automated evaluation pipelines help maintain reliability across prompt, model, and context changes.
- Building for provenance, audit logging, and security from day one is emphasized.

## Bundled resources
- None (the post describes architecture and practices; it does not include full prompts, scripts, or hook JSON).

## Source
- https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude
