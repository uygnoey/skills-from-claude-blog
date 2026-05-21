# Worked example — DLP and SIEM wiring for Claude

This example shows how a team would extend two specific governance surfaces — DLP and SIEM — over Claude using the Compliance API and the launch partners named in the post. It does not extend the post's claims; it only composes what the source says.

## Starting state (representative)

A team runs:

- **DLP** — Microsoft Purview policies covering M365 content.
- **SASE / secure web** — Netskope.
- **SIEM** — Sumo Logic.
- **Identity** — Okta SSO + lifecycle.
- **Claude footprint** — Claude Enterprise (chat + projects) and Claude Platform (custom apps).

## Wiring DLP and content monitoring

Goal: every chat, uploaded file, and project on Claude Enterprise should fall under the same DLP and labeling regime as M365 content.

Steps the post supports:

1. Enable the **Microsoft Purview** Claude integration via the Compliance API so that Claude Enterprise conversation content is visible to the existing Purview policy engine. The post's framing line is: *"so admin teams can apply the same security, monitoring and DLP policies to Claude that they already use for other workplace applications."*
2. Enable the **Netskope** Claude integration so that the team's existing SASE/DLP inline policies extend to Claude usage where Netskope already sits in the path.
3. Do not author a separate Claude policy regime. Extend the existing M365 policy library to include Claude as a covered application; tag and label rules carry over.

The post does not specify how the two DLP integrations are reconciled when both fire on the same content — route the user to each vendor's documentation.

## Wiring SIEM and activity-event visibility

Goal: every Claude Enterprise and Claude Platform activity event — user login, admin action, configuration change — should land in the same SIEM workflow the team already uses.

Steps the post supports:

1. Enable the **Sumo Logic** Compliance API integration so Claude Enterprise and Claude Platform activity events flow into existing dashboards and alerting workflows.
2. If telemetry routing is desired (for example, also forwarding to a data lake or cold storage), the post lists **Cribl** as a launch partner; route through Cribl before fan-out.
3. Tie identity context to events via the **Okta** integration so login/admin-action events join the firm's existing identity-event flow.

## What this example does not invent

- It does not assume an event payload schema or a delivery mode (the post does not publish either).
- It does not assume a region/residency constraint.
- It does not assume a minimum Claude tier required for any of the integrations.
- It does not assume a polling vs. push semantic.
- It does not name vendors not in the post's list of 28 launch partners.

## Source

- [Claude now works with more security and compliance tools](https://claude.com/blog/compliance-api-security-partners)
