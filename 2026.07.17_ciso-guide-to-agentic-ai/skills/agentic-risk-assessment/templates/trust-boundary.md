# Trust boundary statement

> Decide your trust boundary and write it down. Every future agent decision gets easier once
> that line exists.

## What counts as untrusted content in this environment

Untrusted means anything an attacker could plausibly write or alter.

| Source | Trusted / Untrusted | Notes |
|---|---|---|
| Internal Slack / chat | | |
| Internal wiki and docs | | |
| Production logs | | PII present? |
| Source repositories (internal) | | |
| Source repositories (public / third-party) | | |
| Inbound email from outside the org | | |
| The open web / web search results | | |
| Third-party documents and attachments | | |
| Vendor portals and questionnaires | | |
| Customer-submitted content | | |

## The corporate / production data boundary

- **Corporate side:**
- **Production side:**
- **Connectors permitted on each side:**

## Crossing rules

- Data that must cross the boundary goes through: (DLP / DSPM control name)
- Connectors that access untrusted sources require human review for any **destructive or
  one-way** decision. Specifically:
  - Email: draft only, never automatic external send.
  - (add per-connector rules here)

## Off-switch layers, in the order they get pulled

1. Per-connector write disable on: 
2. RBAC removal for group(s): 
3. Org-wide connector off switch.

## Review

- **Owner:**
- **Last reviewed:**
- **Next review:**

---

Source: ["Zero risk isn't the job: a CISO's guide to agentic AI"](https://claude.com/blog/ciso-guide-to-agentic-ai)
