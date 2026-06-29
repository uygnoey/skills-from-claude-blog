# Apps gateway deployment & rollout overview

This reference mirrors the deployment and rollout model described in the source post.

## Architecture (as described)

- **Gateway**: single stateless Linux container backed by **PostgreSQL**.
- **Identity**: OIDC relying party against your IdP; short-lived sessions; no long-lived secrets on developer machines.
- **Policy**: managed settings defined once on the server; delivered at client sign-in; enforced on every request.
- **Telemetry**: client stamps a usage metric for every request; gateway relays it via **OTLP** to your collector.
- **Routing**: holds upstream credential; routes to Claude API / Amazon Bedrock / Google Cloud; optional provider failover.
- **Spend caps**: daily/weekly/monthly limits per org/group/user.

## Rollout steps (as described)

1. Deploy the gateway (CLI binary + `gateway.yaml` + IdP OIDC app).
2. Roll out managed settings (`managed-settings.json` with `forceLoginMethod` and `forceLoginGatewayUrl`).
3. Operate centrally (models/defaults, telemetry, spend limits).

## Source

- https://claude.com/blog/introducing-the-claude-apps-gateway
