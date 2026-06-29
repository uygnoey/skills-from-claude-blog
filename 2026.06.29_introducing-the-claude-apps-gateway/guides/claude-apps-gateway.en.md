**English** · [한국어](./claude-apps-gateway.ko.md) · [Español](./claude-apps-gateway.es.md) · [日本語](./claude-apps-gateway.ja.md)

# Claude apps gateway: deployment & rollout overview

## What is this guide?
This guide summarizes the deployment and rollout model described in the post, focusing on what the gateway does (SSO, policy, telemetry, routing) and how clients are configured to use it.

## When is it useful?
Use this as a quick reference when planning an organization-wide Claude Code rollout on Amazon Bedrock or Google Cloud and you want centralized login, policy enforcement, and per-user usage attribution.

## Architecture (as described)
- **Gateway**: a single stateless Linux container backed by **PostgreSQL**.
- **Identity**: the gateway is an **OIDC relying party** against your IdP (e.g., Google Workspace, Microsoft Entra ID, Okta), issuing short-lived sessions.
- **Policy**: managed settings are defined once on the server; clients receive them at sign-in; the gateway enforces them on every request.
- **Telemetry**: the client stamps a usage metric for every request; the gateway relays it via **OTLP** to a collector you configure.
- **Routing**: the gateway holds the upstream credential and routes inference to the **Claude API**, **Amazon Bedrock**, or **Google Cloud**, with optional provider failover.

## Rollout steps (as described)
1. **Deploy the gateway**
   - Download the Claude Code CLI binary.
   - Configure `gateway.yaml` to point to your OIDC issuer and upstream credential.
   - Register one OIDC application in your IdP.
2. **Force gateway login on clients**
   - Distribute `managed-settings.json` to developer machines.
   - Set `forceLoginMethod` and `forceLoginGatewayUrl` so clients connect to your gateway on first boot.
3. **Operate and adjust centrally**
   - Manage allowed models and default settings centrally.
   - Use telemetry relayed to your collector for per-user attribution.
   - Apply daily/weekly/monthly spend limits per org/group/user.

## Source
- https://claude.com/blog/introducing-the-claude-apps-gateway
