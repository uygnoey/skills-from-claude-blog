---
name: enterprise-unified-rollout
description: Plan and run an organization-wide rollout of the unified chat + Cowork experience on Claude Enterprise (generally available October 23, 2026) - confirm eligibility, review the security posture, and set cost controls (efficient mode, model entitlements, spend limits, pooled group budgets) before enabling it in Organization settings. Use when an Enterprise admin, IT, security, or finance owner must decide how and for whom to turn on the unified experience, or must explain how cloud task work is secured and paid for.
---

## Purpose
In September 2026 chat and Cowork became one Claude for Pro and Max. On October 23, 2026 the unified
experience became generally available for Claude Enterprise. Conversations start as chats; when a task
needs code or file work, Claude continues in the cloud and returns a finished document, analysis, or deck.
This skill turns the announcement into an admin rollout procedure. Facts come from the post; anything
organization-specific is yours to decide.

## When to use
- You administer a Claude Enterprise organization and are about to enable the unified experience.
- Security asks how cloud sessions, connectors, and data are protected.
- Finance asks how agentic (cloud) work affects usage-based spend and how to cap it.
- You need to explain to end users what changes and what carries over.

## Instructions
1. **Check eligibility first.** Organizations using zero data retention for Claude Code, a HIPAA-ready
   configuration, or customer-managed encryption keys stay on their current configuration. Confirm which
   applies to you before planning.
2. **Explain what changes for users.**
   - One Claude across web, desktop, and mobile.
   - Simple questions get quick chat answers; code or file tasks continue in the cloud and come back as
     finished outputs.
   - Cloud work keeps running after a laptop is closed and can be resumed on any platform.
   - Chats, projects, connectors, skills, and plugins carry over.
3. **Review the security posture** with your security team using
   [references/security-posture.md](references/security-posture.md) (SSO and Compliance API, encryption,
   no training by default, one isolated VM per cloud session, network egress off by default, connector
   credentials outside the sandbox, central visibility). Point them to the security best practices guide
   on the Anthropic Trust Center.
4. **Set cost controls before broad enablement.** Pricing stays usage-based, and agentic work can use more
   tokens than quick chats. Choose a setting for each of the four admin controls in
   [references/cost-controls.md](references/cost-controls.md):
   efficient mode, model entitlements per role, spend limits (organization / group / member), and pooled
   group budgets.
5. **Fill in the rollout plan** with [templates/rollout-checklist.md](templates/rollout-checklist.md):
   pilot groups, entitlements, limits, comms, and review dates.
6. **Enable it in Organization settings**, where admins manage the rollout. Follow the admin setup guide
   linked from the post (support.claude.com, article 17444462). Existing Enterprise customers also receive a
   rollout email.
7. **Review spend and usage after launch** and adjust entitlements, limits, or efficient mode by group.

## Examples
**Example 1 - cost-conscious first wave**
- Pilot: one analytics group with a pooled monthly group budget.
- Everyone else: efficient mode on (Sonnet and Haiku), member spend limits set.
- Model entitlements: Opus 5.5 only for roles that need heavy analysis.
- After a month, widen entitlements where the pilot showed value.

**Example 2 - security briefing answer**
"Each cloud session runs in its own isolated virtual machine, network egress is off by default on
Enterprise, connector credentials are stored outside the sandbox, data is encrypted in transit and at
rest and not used for training by default, and our SSO and Compliance API controls still apply."

**Example 3 - not eligible yet**
An organization with customer-managed encryption keys keeps its current configuration; the admin records
this in the checklist and does not plan an enablement date.

## Notes
- Model efficiency figures quoted in the post: Opus 5.5 costs 40% less than Opus 5 on typical workloads;
  Sonnet 5.5 costs up to 30% less than Sonnet 5 for most work.
- The post includes customer stories (DXC, LifeMoves, Quantium, Carvana); see the original for details.
- Source: https://claude.com/resources/articles/unified-claude-enterprise
