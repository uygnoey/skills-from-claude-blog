# Auth implementation prompt (Claude Code)

Run inside `claude` (Claude Code) at your project root. Replace the placeholder block before sending.

---

I need to implement authentication for an integration with <vendor / API name>. Here is the context Claude Code should use:

- Existing secret-management approach: <env vars / Vault / AWS Secrets Manager / etc.>
- Existing HTTP client utilities and retry helpers: <file paths or "search the codebase">
- Auth flow required by this API: <OAuth2 with refresh / JWT validation / rotating API key / mTLS>
- Constraints: no hardcoded credentials, must match existing logging/tracing patterns.

Please:

1. Generate a typed client that matches our project's patterns (search the codebase first to confirm conventions).
2. Implement the auth flow above. For OAuth2, include automatic token refresh; for JWTs, include validation for incoming requests; for API keys, include a rotation path and monitoring hooks.
3. Add rate-limit handling appropriate to this vendor: exponential backoff with jitter for 429, request queuing if the API limits per-key, and a circuit breaker if outage cascades are a risk.
4. Wire schema validation at the response boundary and add an adapter layer if the vendor publishes multiple API versions.

After generating the code, list the new and modified files and summarize the assumptions you made. I will review before tests are added.

---

Source: [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27).
