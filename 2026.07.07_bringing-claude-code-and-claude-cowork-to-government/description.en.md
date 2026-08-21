**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic announced that Claude Code and Claude Cowork are available in public beta through Claude for Government Desktop, delivered via a FedRAMP High authorized environment. Agencies get capabilities on the same release schedule as commercial customers.

The announcement covers four areas: where data lives (inference inside the authorized environment, conversation history stored locally on the agency-managed device), how spend is bounded (standard seats or custom tiers, usage bought in fixed increments with a hard not-to-exceed cap), how administration is delegated (department-level seat allocation, SCIM group mappings for rate limits, dollar caps and allowed models, layered configuration defaults for sub-agencies), and how oversight works (hash-chained audit log reviewable in-product, two-person approval for sensitive Anthropic-side operations, metering-only usage exports). Supporting documents: a public FedRAMP Secure Configuration Guide and formal change notification, plus a penetration-test summary under NDA through Anthropic's trust center. The desktop app deploys through standard agency MDM platforms.

## When is it useful?
- When preparing an ATO package or security review and you need to state where processing happens and where data rests.
- When a department has to allocate seats and different limits across sub-agencies under a single authorization.
- When finance needs consumption-based pricing reconciled with appropriated funds.
- When an inspector general or auditor asks for usage figures and sensitive material cannot leave the boundary.
- When planning MDM distribution and endpoint policy for a tool whose transcripts live on the laptop.

## Key points
- **FedRAMP High, with inference inside the boundary.** Delivered through Claude for Government Desktop, currently public beta.
- **Conversation history is local.** It sits on the agency-managed device, which puts the endpoint in scope — disk encryption, backup, retention, and device-loss procedures are agency endpoint policy, not vendor retention.
- **Spend is bounded by a hard cap.** Usage is purchased in fixed increments with a not-to-exceed cap, tracked per user and per model in the admin console, with automatic burndown alerts before the balance runs low.
- **Limits ride on identity.** SCIM group mappings set rate limits, dollar caps, and allowed models per group; layered configuration sets sub-agency defaults for what Claude can connect to and which features are available.
- **Oversight is built in.** A hash-chained audit log is reviewable directly in the product by organization administrators, and sensitive operations on Anthropic's side require two-person approval.
- **Usage exports are metering data only,** so ATO and IG questions can be answered without moving sensitive material.
- **Documentation at two levels.** FedRAMP Secure Configuration Guide and formal change notification are public; the penetration-test summary is available under NDA through the trust center.
- **Same release schedule as commercial customers** — a benefit and a change-management obligation at once.
- **Anthropic is the contracted billing party;** no separate cloud provider relationship is required. New customers request access at claude.com/solutions/government.

## Bundled resources
- `skills/government-deployment-planning/SKILL.md` — the rollout as a seven-step procedure, from authorization boundary to risk register.
- `skills/government-deployment-planning/references/controls-inventory.md` — the full control surface as announced, grouped by the question a reviewer will ask.
- `skills/government-deployment-planning/templates/rollout-checklist.md` — a working checklist across authorization, evidence, identity, cost, oversight, endpoint, contracting, and users.
- `skills/government-deployment-planning/templates/evidence-map.md` — a one-page reviewer-question-to-artifact table for an ATO package.
- `guides/agency-rollout.{en,ko,es,ja}.md` — what the announcement means in practice for the people who authorize, fund, administer, and distribute it.

## Source
[Bringing Claude Code and Claude Cowork to government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government) — published 2026-07-07.
