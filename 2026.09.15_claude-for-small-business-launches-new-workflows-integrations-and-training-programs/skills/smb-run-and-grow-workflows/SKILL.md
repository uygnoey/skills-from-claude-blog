---
name: smb-run-and-grow-workflows
description: Run a small business owner's week with Claude using the Claude for Small Business workflow pattern - onboarding (/smb-onboard), a Monday brief of cash, sales, pipeline, and overdue invoices (/monday-brief), after-hours lead response (/speed-to-lead), proposals from voice memos priced from past jobs (/proposal-builder), marketing content and review replies (/social-content-engine, /marketing-monday), month-end close with a packet for the accountant (/close-month), and gap fillers for missing connectors or steps (/build-connector, /build-agent). Every workflow starts in approval mode, some stop before the final step (payroll staged in Gusto), existing software permissions hold, and each workflow has a no-connector fallback from uploaded files. Use when an owner wants a weekly brief, lead replies, a proposal, a content calendar, or a month-end close.
---

## Purpose
Claude for Small Business (launched May 2026, expanded September 2026 to 43 workflows and 27 new
integrations) runs in Claude Cowork and puts Claude inside the tools an owner already uses. The
September release moves it from back-office work toward growing the business: leads, inbound
inquiries, proposals, and day-to-day reporting — the requests owners raised most on the spring
Claude SMB Tour.

Companion files:
- [references/weekly-workflows.md](references/weekly-workflows.md) — each workflow: trigger
  phrase, command, output, eligible connectors, and no-connector fallback.
- [references/controls-and-enablement.md](references/controls-and-enablement.md) — approval and
  permission rules, plan advice, training programs, and partners.
- [references/owner-stories.md](references/owner-stories.md) — the owner examples and figures
  cited in the post.

## When to use
- An owner is setting up and wants to connect tools and pick a first task.
- Monday morning: one page on cash, sales vs. last week, pipeline movement, overdue invoices, and
  the three things that need the owner.
- Inbound inquiries arrive after hours and need qualifying, a reply, and a CRM log.
- A job-site memo, photos, or an RFP need to become a priced, branded proposal.
- Next week's posts and this week's review replies need drafting.
- Month end: reconcile, flag mismatches, write a plain-English P&L, prepare an accountant packet.

## Instructions

1. **Onboard first.** On "help me get set up" or `/smb-onboard`, ask which tools the owner uses,
   connect them, and agree on a first task. Offer to put recurring workflows on a schedule
   (for example the Monday brief weekly).

2. **Map the request to a workflow** using
   [references/weekly-workflows.md](references/weekly-workflows.md). Prefer the named workflow's
   output shape over an ad-hoc answer.

3. **Use connected tools; fall back to files.** If the needed connector is missing, follow the
   workflow's fallback (uploaded spreadsheet, forwarded inquiry, statements, past proposal as a
   template). If a recurring step has no connector, offer `/build-connector` (or reach the tool
   through Zapier) and `/build-agent` to save a manual step for next time.

4. **Stay in approval mode by default.** Draft and stage; wait for the owner's OK before anything
   sends, posts, or pays. Only run a workflow unattended if the owner has switched that specific
   workflow to run on its own, and switch back on request.

5. **Stop short where the post says to.** For payroll, confirm cash, pull hours, flag anomalies,
   and stage the run in Gusto for the owner to submit. Proposals go out for signature only after
   approval.

6. **Respect existing permissions.** Do not surface data a user cannot already see in the source
   tool (for example QuickBooks or Google Drive).

## Examples

**Monday brief**
- Input: "give me my Monday brief"
- Output: one page with cash position, last week's sales vs. the week before, pipeline changes,
  overdue invoices, and the three items that need the owner this week.

**After-hours lead**
- Input: a catering inquiry received at 9:40pm.
- Output: lead qualified, reply drafted with two real openings from the calendar, entry logged in
  the CRM; the reply waits for approval unless the owner set this workflow to run on its own.

**Proposal**
- Input: a two-minute voice memo from a job site.
- Output: a branded proposal priced from past jobs, waiting for edits; sent for signature after
  approval.

**Month-end close**
- Input: "close September"
- Output: reconciliation across sales settlements, card spend, and payroll; transaction-level
  mismatch flags; a plain-English P&L; a close packet for the accountant.

## Source
- https://claude.com/resources/articles/claude-for-small-business-launches-new-workflows-integrations-and-training-programs (2026-09-15)
