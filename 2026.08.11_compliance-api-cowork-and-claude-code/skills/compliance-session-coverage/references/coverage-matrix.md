# Compliance API coverage matrix — Cowork and Claude Code (beta)

Everything below is taken from the announcement. Anything not listed here is not
established by the source; check the Compliance API documentation or your account team.

## Availability

| Item | Value |
| --- | --- |
| Status | Beta |
| Plan | Claude Enterprise |
| Entitlement | Included with the Compliance API |
| Credential | Your **existing Compliance Access Key** |
| Interface | The same Compliance API interface for both products |

## Surfaces in scope

| Product | Surfaces covered |
| --- | --- |
| Claude Cowork | Desktop, web, mobile |
| Claude Code | CLI, desktop app |

## Surfaces excluded from this beta

- Claude Code on the web
- Claude Code via Claude Platform
- Sessions on Amazon Bedrock
- Sessions on Google Cloud Vertex AI
- Sessions on Microsoft Foundry

## Session content captured

- Prompts and responses
- Tool-call content — web and Model Context Protocol
- Skills and artifacts, captured as transcript text

## Session metadata captured

- Verified user ID
- Verified email address
- Organization ID
- Session ID
- Per-message IDs
- Timestamps

## Relationship to OpenTelemetry

Organizations already exporting OpenTelemetry data can continue running both systems
simultaneously, with no additional infrastructure requirements. The announcement does not
present the Compliance API as a replacement for an existing OTel export.

## Source

- https://claude.com/blog/compliance-api-cowork-and-claude-code
