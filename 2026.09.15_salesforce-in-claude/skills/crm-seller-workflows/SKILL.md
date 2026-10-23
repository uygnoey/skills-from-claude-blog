---
name: crm-seller-workflows
description: Run an account executive's daily work in Claude with the Salesforce in Claude plugin (beta, September 2026) - morning brief, call prep, deal review and close plan, post-meeting CRM updates, and pipeline/forecast dashboards - pulling context from Salesforce, email, call recordings, and Slack and writing changes back to Salesforce only after the seller approves. Covers admin rollout (Salesforce MCP, AgentExchange access, org-wide connection, group targeting) and the permission model. Use when a seller or sales leader wants Claude to assemble account context or keep Salesforce updated, or when an admin is planning the rollout.
---

## Purpose
The source announces Salesforce in Claude, a beta plugin built with Salesforce that brings a seller's
accounts, opportunities, and pipeline into Claude under their existing Salesforce permissions. It ships 37
skills for daily AE work. Claude does the administrative assembly of information; the seller approves
every write. This skill turns the described workflows into a repeatable routine.

## When to use
- Preparing the day, a call, or a deal review from scattered CRM, email, call, and Slack context.
- Turning meeting notes or transcripts into follow-ups and opportunity updates.
- Reviewing pipeline or drafting a forecast narrative for leadership.
- An admin planning access, connection, and rollout.

## Instructions

1. **Confirm setup.** The Salesforce connector (read and act on Salesforce data) and the Slack connector
   (read/write deal-channel summaries and account-team threads) should be connected. On first use, run
   the setup skill: it identifies the seller's tools and connectors and creates a Claude Artifact tailored
   to their role and book of business. Admin steps are in
   [references/setup-and-permissions.md](references/setup-and-permissions.md).
2. **Morning brief.** Schedule a brief covering the day's meetings, deals closing soon, at-risk
   opportunities, and unread threads needing replies. From it, push a close date, change a stage, or add a
   follow-up task. On Fridays, summarize the week and draft a manager update.
3. **Call prep.** Pull open opportunities, recent account-team discussion, unanswered threads, and open
   questions from prior calls across Salesforce, Slack, and email. Propose adding stakeholders who appear
   in threads but are missing from Salesforce as contacts.
4. **Deal review and close plan.** Score the deal against the team's methodology, flagging qualification
   gaps, unmet stakeholders, and close-date risks. Then draft a business case and a dated mutual close plan,
   fill qualification fields, and add missing contact roles.
5. **After every meeting.** From the transcript or notes, draft a follow-up email, a Slack deal-channel
   summary, and opportunity updates (next steps, stage, close date) for review.
6. **Pipeline and forecast.** Build an interactive dashboard: coverage by stage, deals likely to slip and
   why, drill-downs by account. Allow close-date and stage changes from it; share it if needed. Draft the
   forecast narrative in leadership's format. Leaders can run the same views across their teams.
7. **Always gate writes.** Present every proposed Salesforce change and wait for approval before saving
   (the default behavior). Salesforce stays the system of record.

Workflow-by-workflow checklists: [references/workflows.md](references/workflows.md). Output skeletons:
[templates/close-plan.md](templates/close-plan.md) and
[templates/post-meeting-update.md](templates/post-meeting-update.md).

## Examples

**Morning**
> The scheduled brief lists three meetings, two deals closing this month, one opportunity flagged at risk
> because the champion went quiet, and four unanswered threads. The seller approves moving one close date
> and adding a follow-up task.

**Deal review**
> Claude scores an opportunity against the team's methodology, flags that the economic buyer has not been
> met and the close date is risky, drafts a dated mutual close plan, and proposes two new contact roles.
> The seller edits the plan and approves saving it to the opportunity.

**After a call**
> From the call transcript, Claude drafts the follow-up email, a deal-channel summary for Slack, and new
> next steps and stage for the opportunity, all held for review.
