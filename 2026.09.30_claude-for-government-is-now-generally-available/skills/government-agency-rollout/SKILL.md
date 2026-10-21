---
name: government-agency-rollout
description: Plan the rollout of Claude for Government (generally available to US federal and state agencies in a FedRAMP High authorized environment) — usage-based billing with a hard not-to-exceed cap, department and sub-agency administration, SSO and SCIM seat tiers, layered configuration defaults, audit logs and ATO documentation, MDM deployment, and the early-access Claude Code CLI and Claude for Microsoft 365. Use when an agency administrator, security team, authorizing official, or procurement officer is preparing to adopt or configure Claude for Government.
---

## Purpose
Claude for Government delivers Claude's coding and agentic work capabilities through a FedRAMP High
authorized environment, with capabilities comparable to commercial customers and new features
generally on the commercial release cadence. This skill turns the post's controls into an ordered
rollout plan for the people involved: administrators, security teams and authorizing officials, and
procurement officers.

## When to use
- An agency is evaluating or onboarding Claude for Government.
- Administrators need to split prepaid usage across departments and sub-agencies.
- Security teams are assembling evidence for the agency ATO process or an IG request.
- An existing customer is moving staff to the desktop application.
- A team wants the early-access Claude Code CLI or Claude for Microsoft 365.

## Instructions

1. **Confirm eligibility and contracting.** The platform is generally available to federal and state
   agencies. No separate cloud-provider relationship is needed. Procurement officers can contract
   with Anthropic directly and award on general-availability terms. New agencies request access at
   claude.com/solutions/government.

2. **Size the spend envelope.** There are no seat fees. Usage is bought in fixed increments with a
   hard not-to-exceed cap, so spend cannot exceed what the agency has obligated. Decide the
   obligated amount and who receives burndown alerts before a balance runs low.

3. **Mirror the org chart.** Department-level administrators allocate prepaid usage to sub-agencies;
   each sub-agency manages its own users. Write down the department → sub-agency tree and the admin
   for each node.

4. **Connect identity.** Connect the agency's own identity provider for single sign-on (self-serve in
   the admin portal). Use SCIM group mappings to set, per seat tier, the rate limits, dollar caps,
   and allowed models.

5. **Define user tiers.** For each group set spend and model limits. Plan to track usage by user and
   by model.

6. **Set layered configuration defaults.** Set defaults for sub-agencies, including what Claude can
   connect to and which features are available.

7. **Prepare oversight evidence.** Administrative actions are recorded in an audit log that
   organization admins can review. Sensitive operations on Anthropic's side require two-person
   approval. Usage exports contain metering data only, so ATO and IG requests can be answered without
   moving sensitive material. Conversation history stays local on the agency-managed device. Get the
   FedRAMP Secure Configuration Guide from Anthropic's trust center.

8. **Deploy the desktop application** through the agency's standard MDM platform. Existing customers
   can bring their conversation history with them through the in-app import.

9. **Enable work patterns.** Staff can work with files on the desktop and use skills, plugins, and
   projects for memo creation, RFP reviews, casework, and other tasks. Engineering teams can use
   Claude Code to build and modernize the software behind public services.

10. **Optional early access.** The Claude Code CLI and Claude for Microsoft 365 are rolling out in
    early access in the same environment with the same administrative controls. Contact the public
    sector team to join.

11. Record decisions in [templates/admin-rollout-checklist.md](./templates/admin-rollout-checklist.md).

## Examples

**State agency with three sub-agencies**
- Department admin obligates a fixed usage amount with a hard cap and sets burndown alerts.
- Prepaid usage is allocated to each sub-agency; each manages its own users.
- SCIM groups map to two tiers: "general staff" (lower dollar cap, a limited model list) and
  "engineering" (higher cap, Claude Code access).
- Layered defaults restrict which connectors sub-agencies can use.

**Answering an ATO evidence request**
- Provide the admin audit log, the FedRAMP Secure Configuration Guide, and a metering-only usage
  export — no conversation content leaves the agency-managed devices.

## Notes
- Details not in the post (exact admin console fields, tier names, procurement vehicles): see the
  Claude for Government documentation.
