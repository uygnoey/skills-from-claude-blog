**English** · [한국어](./enterprise-managed-connector-auth-rollout.ko.md) · [Español](./enterprise-managed-connector-auth-rollout.es.md) · [日本語](./enterprise-managed-connector-auth-rollout.ja.md)

# Enterprise-managed connector authorization rollout (Okta)

## Goal
Roll out centrally managed authorization for MCP connectors so users inherit access via IdP groups and roles and can use connectors on first login.

## Recommended rollout phases
1. Define scope: connectors, pilot group, and success criteria.
2. Provision centrally: admin authorizes once, scope by IdP group/role.
3. Pilot validation: verify zero-touch access and revocation behavior.
4. Production rollout: expand group assignment; document support playbooks.

## Operational considerations
- Treat connector access like the rest of your access stack: provision, audit, revoke through the IdP.
- Consider shorter token lifetimes to reduce lingering access after deprovisioning.
- If required, enforce IdP-only connections to reduce personal/work account mix-ups.

## Source
- https://claude.com/blog/enterprise-managed-auth
