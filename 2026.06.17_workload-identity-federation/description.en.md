**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces general availability of Workload Identity Federation (WIF) on the Claude Platform.

## When is it useful?
Use this when you want workloads (CI, cloud services, Kubernetes jobs, etc.) to call Claude APIs without managing long-lived, static API keys.

## Key points
- WIF replaces static API keys with short-lived, scoped credentials issued at request time.
- WIF works with any OIDC-compliant identity provider and can be used across all Claude API endpoints (including first-party SDKs and Claude Code).
- Claude Platform introduces service accounts so each workload can have its own identity, roles, and audit trail.
- Federation rules bind external identities (via OIDC token claims) to Claude service accounts.
- API keys can coexist with WIF, enabling incremental migration.

## Bundled resources
- Agent Skill: Configure WIF service accounts and federation rules (conceptual checklist).

## Source
- https://claude.com/blog/workload-identity-federation
