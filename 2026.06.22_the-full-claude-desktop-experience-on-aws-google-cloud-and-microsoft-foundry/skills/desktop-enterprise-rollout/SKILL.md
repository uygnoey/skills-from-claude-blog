---
name: desktop-enterprise-rollout
description: Roll out Claude Desktop across an organization with cloud-hosted inference and enterprise controls, based on a provider-backed deployment (AWS, Google Cloud, or Microsoft Foundry).
---

## Instructions
Use this skill as an admin-runbook helper for planning and executing an organization-wide Claude Desktop deployment through a supported cloud provider.

1) Decide which surfaces to enable first
- Claude Desktop can include Chat, Claude Cowork, and Claude Code.
- Treat each surface as separately controllable using its own policy key.

2) Configure enterprise sign-in
- Prefer existing enterprise identity (e.g., IAM Identity Center, Microsoft Entra ID, or other OIDC providers) so end users do not need shared keys.

3) Prepare deployment policies
- Export policy templates from the Claude Desktop setup UI.
- Distribute those policies using your existing endpoint-management tools (e.g., Intune, GPO, Jamf).
- If you have air-gapped environments, plan for an offline installer workflow.

4) Validate before broad rollout
- Test each connector you intend to allow.
- Confirm which Claude models your provider serves.
- Verify connectivity and routing behavior before end users see the app.

5) Expand iteratively
- Start with a small pilot, then broaden access as teams adopt each surface.
- Keep hard-deny rules consistent across every surface/tab.

6) Connect to where work lives (Microsoft 365)
- If enabling Microsoft 365 access, use a connector backed by your own Entra app with tenant allowlisting.
- If you need strict residency, consider the local connector option described in the post.

## Examples
### Example: Staged rollout plan
- Phase 1: IT pilot users get Chat only.
- Phase 2: Broader knowledge-worker groups get Chat + Claude Cowork.
- Phase 3: Engineering gets Claude Code.
- Phase 4: Expand surfaces based on adoption and policy readiness.

### Example: Pre-rollout validation checklist
- [ ] Confirm identity provider sign-in works as expected.
- [ ] Verify connector allow/deny rules behave correctly.
- [ ] Confirm available Claude models from your provider.
- [ ] Validate Microsoft 365 connector endpoints and tenant allowlisting (if applicable).
- [ ] Confirm offline installer path for air-gapped devices (if applicable).

