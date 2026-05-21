**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude now works with more security and compliance tools

## What is this post?

Anthropic's May 21, 2026 announcement of 28 new security and compliance integrations built on the **Claude Compliance API**, so IT and security teams can govern Claude across the Claude Enterprise and Claude Platform products the same way they govern any other application in their stack. The post explains what the API exposes, lists every launch partner, and points customers and partners to the next step.

## When is it useful?

- When an IT/security team is scoping how to wire Claude into existing DLP, SASE, SIEM, identity, eDiscovery, AI-SPM, or AI observability stacks.
- When deciding whether to extend a current security/compliance vendor for Claude coverage instead of building a custom integration.
- When a security/compliance platform vendor is deciding whether to apply to the integration network.
- When packaging the governance story for a CISO/CRO sign-off on Claude Enterprise or Claude Platform rollout.

## Key points

- The Claude Compliance API is the substrate behind all 28 integrations.
- **Two data types** the API exposes to enterprise security and compliance teams programmatically:
  - **Conversation content from Claude Enterprise** — chats, uploaded files, and projects — so admins can apply the same security, monitoring, and DLP policies to Claude that they already use for other workplace applications.
  - **Activity events across both Claude Enterprise and the Claude Platform** — user logins, admin actions, and configuration changes — for a unified view of usage.
- **Coverage categories** for the 28 launch integrations: DLP, SASE, data security, SIEM and security operations, identity, eDiscovery, AI security posture management, and AI observability and telemetry infrastructure.
- **28 launch partners** (alphabetical from the post): Cloudflare, Cribl, CrowdStrike, Cyera, Datadog, Forcepoint, Fortinet, Geordie AI, IBM Guardium, Microsoft Purview, Mimecast, Netskope, Okta, Palo Alto Networks, Proofpoint, Relativity, ReliaQuest, Rubrik, SailPoint, Smarsh, Snyk, Sumo Logic, Tenable, Theta Lake, Trellix, Varonis, Wiz (now part of Google Cloud), and Zscaler.
- **Customer onboarding** — connect and configure the Claude instance; data then flows into the same dashboards and alerting workflows the customer already runs.
- **Partner onboarding** — security/compliance/IT platforms that have built a Compliance API integration can apply to join the network.

## Bundled resources

- `skills/governance-via-compliance-api/SKILL.md` — playbook for picking which Compliance API integration matches an existing stack, and how to scope Claude governance with it.
- `skills/governance-via-compliance-api/references/launch-partners-by-category.md` — verbatim partner list bucketed by the integration categories the post names.
- `skills/governance-via-compliance-api/examples/dlp-and-siem-wiring.md` — worked example wiring DLP and SIEM coverage across Claude Enterprise and the Claude Platform via the Compliance API.

## Source

- [Claude now works with more security and compliance tools](https://claude.com/blog/compliance-api-security-partners) (Anthropic blog, May 21, 2026)
