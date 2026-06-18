**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces enterprise-managed authorization for MCP connectors in Claude, starting with Okta-based provisioning.

## When is it useful?
Use this approach when you need centralized, IT-managed connector access for a team or enterprise, with automatic end-user access on first login and IdP-governed revocation.

## Key points
- Admins authorize a connector once; users inherit access via existing IdP groups and roles.
- End users get “zero-touch” connector setup (no per-user OAuth authorization step).
- Access is consistent across Claude chat, Claude Code, and Cowork.
- It is based on an open Enterprise-Managed Authorization extension to the Model Context Protocol, so custom connectors can support it.
- Central management enables shorter token lifetimes and faster deprovisioning outcomes.

## Bundled resources
- Skill: enterprise-managed-connector-auth (implementation checklist + rollout steps)
- Guide: enterprise-managed-connector-auth-rollout (practical deployment guide)

## Source
- https://claude.com/blog/enterprise-managed-auth
