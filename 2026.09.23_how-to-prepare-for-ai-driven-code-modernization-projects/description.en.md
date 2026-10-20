**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
A Notes from the Field article by Anthropic forward deployed engineers on preparing critical systems
and regulated enterprises for agent-driven code modernization. Agents now write changes faster than
organizations can review them, so the post lays out six steps of organizational work: define the
target, create the certificate, set the promotion policy, put prerequisites in place, build and
refine the agentic workflow, and run the modernization — plus a note on token cost.

## When is it useful?
- When scoping a legacy version upgrade, cross-stack rewrite, or rebuild of a system that goes
  through change management, audit, or regulators.
- When stakeholders disagree on whether behavior may change during the modernization.
- When review and approval, not code writing, has become the bottleneck.
- When leadership needs a business case or token-cost estimate before committing.

## Key points
- Three modernization types: **uplift** (same-stack version bump), **transform** (cross-stack
  rewrite with fixed behavior), **reimagine** (rebuild with changed behavior and a written spec).
  Settle the choice early.
- Map the codebase (the code modernization plugin's `assess`, `map`, `extract-rules`), fill gaps
  with interviews, and justify the project mainly through **risk reduction**.
- The **certificate** is a set of human-free, automatically checkable conditions every change must
  meet — tests, coverage, performance bounds, fresh-context adversarial Claude reviews, output parity,
  staging soak, security scans. Write it with the reviewers; have Claude build missing evidence.
- The **promotion policy** tiers human review by blast radius and agent confidence, fixes recurring
  flags at the source, and spends SME time on the riskiest changes. Leadership should issue it in
  advance so accountability is shared.
- Prerequisites span environment, CI/CD, reviewer capacity, and security (least privilege, scrubbed
  secrets/PII, PR-to-transcript traceability).
- Build the workflow from the code modernization plugin; when issues surface, fix the workflow, not
  each change. Pilot one partition end to end, then scale. Uplifts can modernize in place partition
  by partition.
- Cost: measure tokens in the pilot to estimate a floor, gate expensive checks behind cheap ones,
  and use models like Sonnet for mechanical work.

## Bundled resources
- Skill: `code-modernization-readiness` — the six-step procedure with references (modernization
  types, certificate conditions, promotion policy, prerequisites checklist, cost estimation) and a
  modernization charter template.
- Guide: `preparing-ai-code-modernization` (en/ko/es/ja) — the methodology end to end.

## Source
- https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects
