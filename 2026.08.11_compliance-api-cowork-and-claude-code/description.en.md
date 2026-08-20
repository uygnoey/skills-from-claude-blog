**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement that the **Compliance API now covers Claude Cowork and Claude Code**, in beta, for Claude Enterprise customers. Cowork is covered on desktop, web, and mobile; Claude Code is covered in the CLI and the desktop app. Both products are read through the same Compliance API interface, so compliance and security teams pull session content and metadata from one place instead of two.

The post lists what a session record contains — prompts and responses, tool-call content (web and Model Context Protocol), and skills and artifacts captured as transcript text — plus the metadata that accompanies it: verified user ID and email address, organization ID, session and per-message IDs, and timestamps. It also states what the beta does not cover, and confirms that no new infrastructure is required: coverage is included with the Compliance API under your existing Compliance Access Key, and organizations already exporting OpenTelemetry data can keep running both systems side by side.

## When is it useful?
- When a compliance or security team needs Cowork and Claude Code sessions in the same audit feed they already use for the Compliance API.
- When you are scoping a retention, eDiscovery, or investigation program and need to know exactly which surfaces are in scope today.
- When you have to explain to auditors or reviewers which fields are captured per session and per message.
- When you are deciding whether to keep an OpenTelemetry export running alongside the Compliance API.

## Key points
- **Beta, Claude Enterprise only.** Coverage is available today and is included with the Compliance API — no separate entitlement, and it uses your existing Compliance Access Key.
- **Unified interface.** Cowork and Claude Code session content and metadata are pulled through the same Compliance API interface.
- **Covered surfaces.** Cowork on desktop, web, and mobile; Claude Code in the CLI and the desktop app.
- **Session content captured.** Prompts and responses; tool-call content (web and Model Context Protocol); skills and artifacts, captured as transcript text.
- **Session metadata captured.** Verified user ID and email address, organization ID, session ID and per-message IDs, and timestamps.
- **Excluded from the beta.** Claude Code on the web; Claude Code via Claude Platform; sessions on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry.
- **Coexists with OpenTelemetry.** Organizations already exporting OTel data can continue running both systems at once, with no additional infrastructure requirements.

## Bundled resources
- `skills/compliance-session-coverage/SKILL.md` — scope a Compliance API pull across Cowork and Claude Code, and check coverage before relying on it.
- `skills/compliance-session-coverage/references/coverage-matrix.md` — covered surfaces, excluded surfaces, and every captured field named in the post.
- `skills/compliance-session-coverage/templates/coverage-verification-checklist.md` — a fill-in checklist for confirming scope before an audit or investigation.

## Source
- https://claude.com/blog/compliance-api-cowork-and-claude-code
