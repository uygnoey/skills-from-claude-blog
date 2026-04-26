---
name: api-integration-resilience-playbook
description: Plan and implement resilient third-party API integrations with Claude. Use Claude.ai to enumerate failure modes, authentication risks, and rate-limit strategies before coding, then use Claude Code to generate typed clients, OAuth/JWT/key-rotation flows, and contract/refresh tests across the codebase. Apply when onboarding a new API, hardening a flaky integration, or standardizing how a team splits planning vs implementation work for integrations.
---

## Instructions

This Skill operationalizes the workflow described in "How to integrate APIs seamlessly" (Claude blog, 2025-10-27). The post argues most teams discover failure modes only after production incidents and proposes a two-tool split: Claude.ai for upfront analysis, Claude Code for codebase-wide implementation.

Follow the steps below when integrating a new API or hardening an existing one. Do not invent vendor-specific behavior — when uncertain, ask the user to share the API docs or open them with web search.

### Phase 1 — Plan in Claude.ai (before writing code)

1. **Risk discovery.** Use the [risk-discovery-prompt template](./templates/risk-discovery-prompt.md). Paste the API specification or doc URL and ask for "integration risks ranked by likelihood." Capture concrete items only: rate-limit thresholds, counting method (per user / per IP / per API key), required headers, field nullability, idempotency keys, webhook delivery guarantees.
2. **Failure-mode walkthrough.** Ask Claude to identify scenarios that trigger each error class — timeouts, rate limiting, authentication failures, schema drift. Cross-check against the [failure-mode-catalog](./references/failure-mode-catalog.md). Output: a focused list of issues to prevent rather than discover in production.
3. **Auth strategy decision.** Ask plain-language questions about OAuth2 flows, token refresh cycles, header requirements. Decide where credentials live (env vars vs secret manager) before any code is written.
4. **Webhook vs polling decision.** Use latency requirements, data volume, and infrastructure constraints to pick. Hybrid (webhook for real-time, polling for reconciliation) is valid. Record the decision and the constraints that drove it.
5. **Versioning plan.** If the vendor publishes multiple API versions, plan a versioned client + adapter layer so a future schema change does not require rewriting callers.

### Phase 2 — Implement with Claude Code

Install once per machine, then run from your project root:

```
npm install -g @anthropic-ai/claude-code
claude
```

Use the [auth-implementation-prompt template](./templates/auth-implementation-prompt.md) and ask Claude Code to:

- Generate a typed client matching existing project patterns (HTTP layer, logging, retry utilities).
- Implement the chosen auth flow: OAuth2 with automatic token refresh, JWT validation for service-to-service, or API-key rotation with monitoring.
- Add rate-limit handling: exponential backoff with jitter for `429`, request queuing for per-key limits, circuit breaker where appropriate.
- Wire schema validation at the response boundary and an adapter layer that translates between API versions.

### Phase 3 — Validate

Ask Claude Code to generate and run tests verifying that the integration handles edge cases properly:

- Reproduce a rate-limit scenario and confirm backoff behavior.
- Generate contract tests against the response schema; fail fast on breaking changes.
- Exercise authentication refresh during a long-running operation.

### Phase 4 — Ship

After tests pass, run inside the Claude Code prompt:

```
> Commit these API changes and open a PR
```

Claude Code generates a descriptive commit message and a PR description that links the implementation to the test coverage.

### When to use Claude.ai vs Claude Code

- **Claude.ai**: evaluating new APIs, understanding auth requirements, planning error-handling strategies, sharing approaches with the team, vendor research via web search. Browser-only, no codebase access.
- **Claude Code**: generating boilerplate clients, implementing complex auth flows across multiple files, creating comprehensive test suites, touching configuration files, environment variables, and CI/CD pipelines.

## Examples

See [examples/example-prompts.md](./examples/example-prompts.md) for the verbatim Claude.ai and Claude Code prompts cited in the original post — covering Stripe webhook signature debugging, OAuth tokens during multi-step checkouts, webhook vs polling for inventory updates, OAuth2 for Google Calendar with refresh, rotating Twilio API keys with monitoring, JWT validation for microservices, rate-limit reproduction tests, contract tests, and the commit-and-PR command.

## Source

Distilled from [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (published 2025-10-27).
