**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces the Claude apps gateway, a self-hosted gateway that lets organizations run Claude Code with Amazon Bedrock and Google Cloud while keeping authentication, policy, and cost controls centralized.

## When is it useful?
Use it when you want to deploy Claude Code at scale without provisioning a separate cloud credential per developer, while enforcing consistent org policies (models, defaults) and enabling per-user cost attribution and spend caps.

## Key points
- The gateway is deployed by you as a single stateless container on Linux, backed by a PostgreSQL database.
- It holds the upstream provider credential and authenticates developers via your identity provider (OIDC).
- Managed settings (policy) are defined once on the server, applied at client sign-in, and enforced on every request.
- The client stamps usage metrics per request; the gateway relays them to your collector via OTLP.
- It can route to the Claude API, Amazon Bedrock, or Google Cloud, with optional provider failover.
- Spend limits (daily/weekly/monthly) can be applied per organization, group, or user.

## Bundled resources
- Example configuration files mentioned in the post: `gateway.yaml` and `managed-settings.json` (parameters include `forceLoginMethod` and `forceLoginGatewayUrl`).
- The gateway is shipped inside the same `claude` CLI binary developers already install.

## Source
- https://claude.com/blog/introducing-the-claude-apps-gateway
