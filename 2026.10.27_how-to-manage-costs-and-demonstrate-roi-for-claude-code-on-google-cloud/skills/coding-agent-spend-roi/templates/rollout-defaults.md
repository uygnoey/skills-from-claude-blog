# Rollout defaults checklist

Start with reasonable defaults, then refine by role and team as usage data comes in.

## Google Cloud project and billing
- [ ] Dedicated Google Cloud project for Claude Code (per-project billing)
- [ ] Billing budget with alert thresholds for admins: ______
- [ ] Service-level spend cap (Preview), if you want a hard ceiling: ______
- [ ] Cloud Billing export to BigQuery enabled
- [ ] Quotas reviewed per model family and endpoint location
- [ ] Provisioned throughput considered instead of pay-as-you-go? (yes / no)

## Claude apps gateway
- [ ] Gateway deployed in the project; developers sign in through the IdP (e.g. Google Workspace)
- [ ] Org-wide spend cap (per-developer default): ______ per day / week / month
- [ ] Group caps where roles differ (IdP group -> cap): ______
- [ ] Default model: ______
- [ ] Model allowlist per IdP group: ______
- [ ] Developers know about the 75% / 95% in-CLI warnings and the 429 at the cap
- [ ] Cap-increase request flow (ticket -> gateway admin API): ______

## Telemetry
- [ ] Telemetry destination set on the gateway (or OTel collector configured)
- [ ] `OTEL_RESOURCE_ATTRIBUTES` for department / cost center
- [ ] Cloud Monitoring "Claude Code Monitoring" dashboard copied
- [ ] Blocked-request (cap hit) metric wired to ticketing
- [ ] Prompt logging decision recorded (opt-in only; sensitive content): ______

## Review cadence
- [ ] First review date: ______ (look for routine work on expensive models, stale scheduled tasks)
- [ ] Refine caps and model policy by role/team
- [ ] Do not cap power users by reflex - check the value of their sessions first
