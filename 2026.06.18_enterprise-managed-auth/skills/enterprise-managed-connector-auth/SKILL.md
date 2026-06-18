---
name: enterprise-managed-connector-auth
description: Centralize authorization for MCP connectors via an identity provider so admins provision once and users inherit access via IdP groups and roles.
---

## Instructions
You are helping an IT/admin team plan and roll out enterprise-managed authorization for MCP connectors (starting with Okta), based strictly on the source post.

1. Confirm scope
   - Identify which Claude plan and environment is in scope (Team or Enterprise; beta availability).
   - List which connectors need to be centrally authorized.

2. Choose the governance model
   - Prefer centralized authorization through the identity provider.
   - Map connector access to existing IdP groups and roles.

3. Provision connector access (org-level)
   - Have an admin authorize the connector once for the organization.
   - Ensure end users inherit access automatically on first login (zero-touch setup).

4. Operationalize lifecycle management
   - Manage revocation through the IdP.
   - Consider shortening token lifetimes to reduce long-lived access, while keeping user productivity intact.
   - Ensure deprovisioned users lose access quickly (avoid lingering tokens).

5. Enforce separation (work vs personal)
   - If needed, require that the connector only ever connects through the IdP to reduce accidental linking of personal accounts.

6. Verify consistency across surfaces
   - Confirm the intended connector access works consistently across Claude chat, Claude Code, and Cowork.

7. Document what is (and is not) covered by the source
   - The source post does not provide step-by-step IdP configuration, SAML/OIDC settings, or SCIM examples; note any gaps and refer readers to official documentation as needed.

## Examples
### Example: rollout checklist (high-level)
- Admin enables and authorizes the connector once.
- Access is assigned using IdP groups/roles.
- A pilot group confirms the connector is available on first login.
- Revocation and offboarding behavior is tested.
- Token lifetime policy is reviewed.

### Example: explaining the benefit to end users
“Connectors will appear automatically the first time you open Claude. You won’t need to authorize each connector yourself.”

## Source
- https://claude.com/blog/enterprise-managed-auth
