---
name: governance-via-compliance-api
description: Plan Claude governance using the Claude Compliance API and the 28 launch integrations Anthropic announced on May 21, 2026. Use when an IT or security team is wiring Claude Enterprise and the Claude Platform into existing DLP, SASE, data-security, SIEM/SecOps, identity, eDiscovery, AI-SPM, or AI observability/telemetry stacks — or when a security/compliance platform vendor is deciding whether to apply to the integration network.
---

# Claude governance via the Compliance API

This skill packages "Claude now works with more security and compliance tools" so a team can map an existing stack to the right integration and decide what governance Claude needs. It does not invent capabilities beyond the source; for anything past it, route to the [Compliance API docs](https://claude.com/blog/compliance-api-security-partners) referenced from the post and to the partner's own documentation.

## Instructions

When the user is scoping Claude governance with the Compliance API:

1. **Confirm scope.** The Compliance API exposes two data types — **conversation content from Claude Enterprise** (chats, uploaded files, projects) and **activity events across both Claude Enterprise and the Claude Platform** (user logins, admin actions, configuration changes). Plan against these two surfaces, not against assumed APIs the post does not mention.

2. **Walk the 8 integration categories the post names**, in this order:
   - DLP
   - SASE
   - Data security
   - SIEM and security operations
   - Identity
   - eDiscovery
   - AI security posture management (AI-SPM)
   - AI observability and telemetry infrastructure
   For each, ask the user which incumbent vendor they run today. The verbatim partner list bucketed by category is in [`references/launch-partners-by-category.md`](./references/launch-partners-by-category.md).

3. **Map incumbents to launch partners.** The post lists 28 launch partners: Cloudflare, Cribl, CrowdStrike, Cyera, Datadog, Forcepoint, Fortinet, Geordie AI, IBM Guardium, Microsoft Purview, Mimecast, Netskope, Okta, Palo Alto Networks, Proofpoint, Relativity, ReliaQuest, Rubrik, SailPoint, Smarsh, Snyk, Sumo Logic, Tenable, Theta Lake, Trellix, Varonis, Wiz (now part of Google Cloud), and Zscaler. If the user's incumbent is on the list, recommend turning on the partner's Claude integration before building anything custom — the post explicitly frames this as the fast path.

4. **Default policy alignment.** The post's framing line is: "apply the same security, monitoring and DLP policies to Claude that they already use for other workplace applications." Recommend not creating a separate Claude policy regime — extend the existing policy library and label Claude as another covered application.

5. **Pick the integration before the deployment shape.** The post says enabling coverage is "connect and configure your Claude instance, and the data flows into the same dashboards and alerting workflows you use for everything else." That means downstream operations (incident response, eDiscovery workflow, identity provisioning) should stay where they live today; the integration is the bridge, not the new home.

6. **For platform vendors deciding whether to join.** The post invites security/compliance/IT platforms that have built a Compliance API integration to apply to join the network. Direct vendors to the [source post](https://claude.com/blog/compliance-api-security-partners) for the application link.

7. **Decline to invent.** The post does **not** publish:
   - Webhook payload shapes.
   - Retention windows, region availability, residency guarantees.
   - The minimum Claude tier required for a given integration.
   - SLAs.
   - Pricing.
   When the user asks any of those, route them to the Anthropic Help Center / Compliance API documentation referenced in the post and to the partner's own docs. Do not estimate.

## Examples

### Example 1 — mapping an incumbent stack

> "We use Netskope, Splunk for SIEM (we are migrating to Sumo Logic), Okta, and Microsoft Purview. What lights up for Claude?"

Walk through:
- **SASE / DLP** — Netskope is a launch partner; turn on the Netskope Claude integration to extend their existing DLP and SASE coverage to Claude Enterprise conversation content.
- **SIEM** — Sumo Logic is on the launch list; once the migration lands, point Claude Enterprise and Claude Platform activity events at Sumo Logic via its Compliance API integration. (Splunk is not on the launch list per the source post; do not invent it.)
- **Identity** — Okta is on the list; use the Okta integration to bring login and admin-action events into the firm's existing identity-event flow.
- **Data security / DLP overlay** — Microsoft Purview is on the list; use its integration so Claude conversation content carries the same labels/policies as M365 content.

### Example 2 — picking a SIEM destination when there is none

> "We don't have a SIEM yet; we're starting from scratch."

The post names six SIEM/SecOps-adjacent options (Datadog, Sumo Logic, ReliaQuest, Trellix, Cribl, Fortinet — note that Cribl is a routing layer, not a SIEM). Recommend matching the destination to the team's operational shape (ops-led vs. detection-engineering-led vs. managed) rather than to the model. Route the user to each vendor's docs for the live SIEM/SecOps capabilities; the post does not differentiate them.

### Example 3 — declining to invent

> "What's the per-event volume cap on the activity events stream?"

Reply that the source post does not publish event-volume caps; route to the Anthropic Help Center and the Compliance API documentation referenced from the post, plus the partner's docs for any rate limits on their side.

## Bundled resources

- [`references/launch-partners-by-category.md`](./references/launch-partners-by-category.md) — verbatim partner list bucketed by the eight integration categories named in the post.
- [`examples/dlp-and-siem-wiring.md`](./examples/dlp-and-siem-wiring.md) — worked example wiring DLP and SIEM coverage for Claude via the Compliance API.

## Source

- [Claude now works with more security and compliance tools](https://claude.com/blog/compliance-api-security-partners) (Anthropic blog, May 21, 2026)
