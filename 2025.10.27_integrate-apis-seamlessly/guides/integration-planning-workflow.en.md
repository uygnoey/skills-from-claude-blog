**English** · [한국어](./integration-planning-workflow.ko.md) · [Español](./integration-planning-workflow.es.md) · [日本語](./integration-planning-workflow.ja.md)

# Integration planning workflow

A step-by-step workflow distilled from [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27). Use it to standardize how your team plans, implements, validates, and ships third-party API integrations using Claude.ai and Claude Code.

## 1. Triage the API in Claude.ai

- Open Claude.ai. Paste the doc URL, OpenAPI spec, or relevant excerpts.
- Ask: "Integration risks ranked by likelihood." Demand vendor-specific items only — rate-limit thresholds, counting method (per user / IP / API key), required headers, idempotency keys, webhook delivery guarantees, field nullability.
- Ask follow-up debugging questions for any unclear failure mode (e.g. "Why might OAuth tokens expire during multi-step checkout flows?", "Here's a Stripe webhook signature error. What validation steps am I missing?").
- Output: a concrete failure-mode list and an authentication-strategy decision (where credentials live, refresh cadence, rotation plan).

## 2. Decide webhook vs polling

- Compare options for the specific use case (e.g. "webhook vs polling for real-time inventory updates").
- Pick based on latency, volume, and infra constraints. Hybrid (webhook for real-time, polling for reconciliation) is acceptable.
- Record the decision and the constraints that drove it.

## 3. Implement with Claude Code

- Install: `npm install -g @anthropic-ai/claude-code`. Launch from project root: `claude`.
- Ask Claude Code to generate a typed client matching existing project conventions.
- Implement the chosen auth flow:
  - "Build OAuth2 flow for Google Calendar with automatic token refresh"
  - "Create rotating API key system for Twilio with monitoring"
  - "Implement JWT validation for microservices"
- Add rate-limit handling: exponential backoff with jitter for 429, request queuing if applicable, circuit breaker for cascade-prone calls.
- Wire schema validation at the response boundary; add an adapter layer for versioned clients.

## 4. Validate

Ask Claude Code to generate and run tests:

- "Create tests that reproduce this rate limit scenario"
- "Generate contract tests for schema validation"
- "Run tests for authentication refresh during long operations"

Iterate until tests confirm the integration handles the failure modes captured in step 1.

## 5. Ship

Run inside Claude Code:

```
> Commit these API changes and open a PR
```

Claude Code generates a descriptive commit message and a PR description that links the implementation to test coverage.

## Source

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (published 2025-10-27).
