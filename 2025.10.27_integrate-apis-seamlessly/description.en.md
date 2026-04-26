**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How to integrate APIs seamlessly

## What is this post?

A field guide for shifting API integration work from reactive debugging to upfront, systematic design. The original post argues that most teams discover failure modes (rate limits, token expiry, schema drift, webhook ordering) only after they hit production, then retrofit error handling. It shows how to use Claude.ai for upfront analysis of authentication, rate limits, and edge cases, and Claude Code for generating typed clients, OAuth/JWT/key-rotation flows, and contract/refresh tests across your codebase.

## When useful

- Onboarding a new third-party API and you want a checklist of failure modes before writing a line of code.
- Your existing integration is firefighting 401/429/timeout incidents and you need a systematic remediation plan.
- Choosing between webhooks vs polling, or planning a versioned client that survives schema changes.
- Standardizing how your team uses Claude.ai (planning) and Claude Code (implementation/tests/PRs) for integration work.

## Key points

- Claude.ai for planning: paste API docs, ask for "integration risks ranked by likelihood", get specific items (rate-limit thresholds, required headers, field nullability, idempotency, jitter for 429s).
- Claude Code for implementation: install via `npm install -g @anthropic-ai/claude-code`, run `claude`, then ask for OAuth2 with refresh, JWT validation, rotating API keys with monitoring, and contract/refresh tests.
- Build adapter layers and versioned clients to absorb schema changes; use schema validation to detect breaking changes early.
- Choose webhooks vs polling per use case (latency, volume, infra); hybrid strategies are valid.
- Ship via Claude Code: `> Commit these API changes and open a PR` produces commit messages and PR descriptions linking changes and tests.

## Bundled resources

- [skills/api-integration-resilience-playbook/SKILL.md](./skills/api-integration-resilience-playbook/SKILL.md): planning + implementation playbook with prompts.
- [templates/risk-discovery-prompt.md](./skills/api-integration-resilience-playbook/templates/risk-discovery-prompt.md): reusable prompt for ranked failure-mode lists.
- [templates/auth-implementation-prompt.md](./skills/api-integration-resilience-playbook/templates/auth-implementation-prompt.md): OAuth2 / JWT / key-rotation prompt.
- [references/failure-mode-catalog.md](./skills/api-integration-resilience-playbook/references/failure-mode-catalog.md): catalog of named failure modes from the post.
- [examples/example-prompts.md](./skills/api-integration-resilience-playbook/examples/example-prompts.md): verbatim Claude.ai/Claude Code prompts from the post.
- [guides/integration-planning-workflow.en.md](./guides/integration-planning-workflow.en.md) (+ ko/es/ja): step-by-step planning workflow.

## Source

Distilled from [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (published 2025-10-27).
