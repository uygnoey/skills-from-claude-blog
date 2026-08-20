---
name: compliance-session-coverage
description: Scope and verify a Compliance API pull that spans Cowork and Claude Code sessions — confirm which surfaces are in scope for the beta, which session content and metadata fields are captured, and whether an existing OpenTelemetry export still needs to run alongside it.
---

## Instructions
You are helping a compliance or security team at a Claude Enterprise organization retrieve session records for Cowork and Claude Code through the Compliance API. Coverage for these two products is in beta.

1) Confirm eligibility and access.
- The organization must be on Claude Enterprise; this coverage is a beta feature for Enterprise customers.
- No new entitlement or key is needed. Coverage for Cowork and Claude Code is included with the Compliance API and uses the organization's **existing Compliance Access Key**.
- If the team does not yet have a Compliance Access Key, route them through their normal Compliance API enablement path before going further.

2) Pin down which surfaces the request actually needs.
- In scope today: **Cowork** on desktop, web, and mobile; **Claude Code** in the CLI and the desktop app.
- Out of scope in this beta: Claude Code on the web, Claude Code via Claude Platform, and sessions on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry.
- See [references/coverage-matrix.md](references/coverage-matrix.md) for the full in/out list and the captured fields.
- If any surface the requester named is out of scope, say so explicitly and up front. Do not let an audit, retention, or eDiscovery scope silently assume a surface that the beta does not cover.

3) Decide what has to come back per session.
- Session content: prompts and responses; tool-call content (web and Model Context Protocol); skills and artifacts, captured as transcript text.
- Session metadata: verified user ID and email address, organization ID, session ID and per-message IDs, and timestamps.
- Map each of the requester's questions to a specific field above. If a question cannot be answered by any captured field, flag it instead of inferring one.

4) Pull both products through the one interface.
- Cowork and Claude Code session content and metadata are retrieved through the **same Compliance API interface** — build one query path, not two.
- Use session IDs to group a conversation and per-message IDs to order or cite individual turns.

5) Settle the OpenTelemetry question.
- If the organization already exports OpenTelemetry data, it can keep running both systems at the same time, with no additional infrastructure requirements.
- Recommend keeping the OTel export in place while the coverage is in beta, especially where it observes a surface the beta excludes.

6) Record the scope before acting on the data.
- Fill in [templates/coverage-verification-checklist.md](templates/coverage-verification-checklist.md) and keep it with the audit record, so the coverage boundary in force at pull time is documented.

For anything not stated in the source announcement — endpoint paths, parameters, retention windows, rate limits — direct the user to the Compliance API documentation or their account team rather than guessing.

## Examples

### Example: scoping an investigation across two products
User: Legal needs every Claude session for one employee over the last quarter.
Assistant:
- Confirm Enterprise plan and that a Compliance Access Key already exists — no new key is required for this coverage.
- Covered for that employee: Cowork on desktop, web, and mobile, and Claude Code in the CLI and the desktop app, pulled through the same Compliance API interface.
- Filter on the verified user ID / email address and the timestamp range; group by session ID.
- Flag the gap explicitly: if the employee used Claude Code on the web or via Claude Platform, or worked on Bedrock, Vertex AI, or Foundry, those sessions are outside this beta and will not appear.
- Record the scope in the coverage verification checklist and attach it to the matter file.

### Example: answering "do we still need our OTel pipeline?"
User: We already ship OpenTelemetry data to our SIEM. Can we turn it off now?
Assistant:
- Not on the strength of this change alone. The two systems can run simultaneously with no additional infrastructure requirements.
- The Compliance API coverage for Cowork and Claude Code is in beta and excludes Claude Code on the web, Claude Code via Claude Platform, and Bedrock, Vertex AI, and Foundry sessions.
- Keep the OTel export running for anything in those gaps, and re-evaluate when the coverage leaves beta.

### Example: an auditor asks what is actually captured
User: The auditor wants to know exactly what a session record contains.
Assistant:
- Content: prompts and responses, tool-call content (web and Model Context Protocol), and skills and artifacts captured as transcript text.
- Metadata: verified user ID and email address, organization ID, session ID and per-message IDs, and timestamps.
- Hand over `references/coverage-matrix.md` as the field-level answer, and note that anything beyond this list is not established by the announcement.

## Source
- https://claude.com/blog/compliance-api-cowork-and-claude-code
