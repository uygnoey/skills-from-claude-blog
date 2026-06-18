---
name: configure-wif-service-accounts
description: Plan and review a Workload Identity Federation (WIF) setup for Claude Platform workloads, using service accounts, federation rules, and least-privilege scopes.
---

## Instructions

Use this skill to turn a Claude Platform Workload Identity Federation (WIF) announcement into an actionable implementation and review checklist.

1) Identify the workload and execution environment
- Describe what the workload is (CI job, Kubernetes workload, cloud function, etc.).
- Identify the identity provider (IdP) that will issue signed OIDC tokens (e.g., cloud IAM, Kubernetes, GitHub Actions, Okta).

2) Choose a Claude Platform service account per workload
- Prefer a dedicated service account per workload (avoid shared identities) so roles and audit logs are attributable.
- Record which Claude Platform roles/scopes the workload needs.

3) Define federation rules
- Specify which OIDC token claims must match for the workload to assume the service account.
- Keep the rule as narrow as possible to reduce blast radius.

4) Validate authentication and auditability
- Use the guided setup flow in the Claude Console when available and run the provided test command.
- Confirm that the resulting access tokens are short-lived and bounded by the service account’s roles.
- Confirm audit logs attribute exchanges and requests to the intended service account.

5) Plan incremental migration from API keys
- If you currently rely on static API keys, migrate one workload at a time.
- Keep API keys enabled for workloads not yet migrated.

## Examples

### Example: turn a WIF announcement into a rollout plan
Input:
- Workloads: GitHub Actions (repo A), Kubernetes cronjob (cluster B)
- Desired principle: least privilege

Output:
- Create a dedicated Claude service account for each workload.
- Define one federation rule per workload that matches only the expected OIDC claims.
- Assign only required roles/scopes to each service account.
- Use the Claude Console setup flow and the test command to verify auth.
- Roll out WIF workload-by-workload while leaving remaining API-key workloads untouched.

## Source
- https://claude.com/blog/workload-identity-federation
