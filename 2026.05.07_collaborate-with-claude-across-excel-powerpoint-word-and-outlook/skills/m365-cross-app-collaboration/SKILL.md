---
name: m365-cross-app-collaboration
description: Collaborate with Claude across Microsoft 365 apps (Excel, PowerPoint, Word, Outlook) while keeping one continuous conversation context and updating related artifacts.
---

# M365 cross-app collaboration

Use this skill to coordinate work across Excel, PowerPoint, Word, and Outlook within a single, continuous conversation context, so changes in one artifact can be reflected consistently in others.

## Instructions

### 1) Establish the cross-app objective
- Ask what outcome the user wants (e.g., “an exec-ready deck + a memo + the supporting spreadsheet + a draft email”).
- Confirm which files are open (or should be opened) in Excel/PowerPoint/Word/Outlook.

### 2) Keep a shared set of assumptions
- Maintain a short list of key assumptions (inputs, definitions, constraints).
- When an assumption changes in Excel, re-check dependent content in the deck and memo.

### 3) Treat each app as the right tool for the job
- Excel: calculations, scenario inputs, coverage/financial models, tables.
- PowerPoint: charts and narrative slides.
- Word: narrative memo, structured write-up.
- Outlook: inbox triage, reply drafting, calendar invites.

### 4) Outlook-focused safety checks
- Create replies and invites as drafts.
- Require human review before sending.

### 5) Admin/ops awareness (enterprise)
- If the user asks about rollout and governance, point them to:
  - Admin deployment via Microsoft admin tooling / AppSource listings.
  - Optional observability via OpenTelemetry.
  - Usage reporting via an Analytics API.
  - Optional routing via an LLM gateway (e.g., cloud providers).

## Examples

### Example 1: Spreadsheet → memo → deck
**User:** I have an Excel model and need a one-page memo and a 6-slide deck summarizing the key drivers.

**Assistant:**
1. In Excel: identify the main drivers, confirm assumptions, and generate the chart(s) needed for slides.
2. In Word: draft the memo using the same assumptions and numbers as the spreadsheet.
3. In PowerPoint: build slides and insert charts; ensure titles and callouts match the memo.
4. If any assumption changes in Excel, update the memo and deck references to keep them consistent.

### Example 2: Outlook triage + attachment workflow
**User:** I got an email asking for an updated model and a short update. Please help.

**Assistant:**
1. In Outlook: triage the email and create a draft reply.
2. Open the attachment in Excel or Word; confirm what the sender requested.
3. Update the model in Excel; summarize changes.
4. Draft a short Word update or slide, then finalize the Outlook draft with the right attachment(s).
5. Ask the user to review before sending.

## Source
- https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
