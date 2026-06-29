---
name: apps-gateway-rollout
description: Plan and roll out Claude Code via a self-hosted apps gateway, using centralized SSO login, managed settings enforcement, and per-user usage attribution when running on Amazon Bedrock or Google Cloud.
---

## Instructions

Use this skill when you need to deploy and operate the apps gateway described in the source post to enable organization-wide Claude Code usage on Amazon Bedrock or Google Cloud.

### What the gateway does (as described)

- **Centralized identity**: The gateway authenticates developers against your identity provider (OIDC) and issues a short-lived session; no long-lived secrets sit on developer machines.
- **Centralized policy**: Managed settings are defined once on the server, delivered to clients at sign-in, and enforced by the gateway on every request.
- **Usage attribution**: The client stamps a usage metric on every request; the gateway relays these metrics via OTLP to a collector you operate.
- **Provider routing**: The gateway holds the upstream credential and routes inference to the Claude API, Amazon Bedrock, or Google Cloud, with optional provider failover.
- **Spend caps**: Supports daily/weekly/monthly spend limits per organization, group, or user.

### Deployment and rollout (as described)

1. **Deploy the gateway**
   - Download the Claude Code CLI binary.
   - Configure `gateway.yaml` to point to your OIDC issuer and upstream credential.
   - Register one OIDC app in your IdP.
2. **Roll out to developers**
   - Distribute `managed-settings.json` to developer machines.
   - Set `forceLoginMethod` and `forceLoginGatewayUrl` so clients connect to your gateway on first boot.
3. **Operate centrally**
   - Adjust allowed models and default settings on the server.
   - Monitor per-user usage from your OTLP collector.
   - Apply spend limits (org/group/user).

### Bundled resources

- Guide: [Apps gateway deployment & rollout overview](./references/apps-gateway-rollout-guide.en.md)
- Reference templates (based on config files mentioned in the post):
  - [`templates/gateway.yaml`](./templates/gateway.yaml)
  - [`templates/managed-settings.json`](./templates/managed-settings.json)

## Examples

### Create a rollout checklist

1. Confirm you can deploy a Linux container and provision PostgreSQL.
2. Confirm your IdP supports OIDC and create/register an OIDC application.
3. Configure the gateway (`templates/gateway.yaml`) with your OIDC issuer and upstream provider credential.
4. Publish managed settings (`templates/managed-settings.json`) and set `forceLoginMethod` and `forceLoginGatewayUrl`.
5. Validate that clients receive managed settings at sign-in and that policy is enforced consistently.
6. Connect an OTLP collector and verify per-user metrics are received.
7. Configure spend limits at the org/group/user level.

### Explain the security posture to stakeholders

- The gateway authenticates users via your IdP and issues short-lived sessions.
- No long-lived secrets are stored on developer laptops.
- The gateway is self-hosted and does not send inference traffic or usage data to Anthropic unless you choose to route to the Claude API.

## Source

- https://claude.com/blog/introducing-the-claude-apps-gateway
