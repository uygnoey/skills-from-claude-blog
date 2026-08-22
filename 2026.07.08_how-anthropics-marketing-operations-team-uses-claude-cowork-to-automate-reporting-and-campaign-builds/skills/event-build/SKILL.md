---
name: event-build
description: Set up an event, webinar, or integrated campaign end to end across the CRM, the marketing automation platform, the event platform, and email — including the integrations between them, which are rarely complete out of the box. Use when a build request has been routed from the intake queue. Posts two Slack updates (on pickup, and when the landing page is ready for review), then hands off to a fresh audit agent rather than marking its own work complete.
---

# Event build

Setting up the infrastructure behind a marketing campaign has traditionally been one
of the most manual processes in marketing. Every event, webinar, or integrated
campaign needs to be set up in the CRM, in the marketing automation platform that
runs the email sequences, and in the event management platform that hosts
registration and the event landing page. Each is typically a different vendor, and
the integrations between them are rarely complete.

This skill runs that whole sequence. It does not verify its own output.

The reason to automate it is consistency, not only speed: at scale, marketers cloning
event pages from whatever template happens to be nearby produce bugs — confirmation
emails surfacing the wrong city name, broken landing pages.

## Instructions

### 1. Post the pickup update to Slack

Before starting, post the first of two scripted Slack updates: Claude has picked up
this request. Use the wording in
[templates/slack-updates.md](templates/slack-updates.md).

This is not a courtesy. The requester and the rest of the team need to know the work
started, and the update timestamps the start of the build.

### 2. Read the request and resolve every variable before building

Pull from the intake form and the request thread: event name, type, date and time,
time zone, location (including city, exactly as it should appear in every asset),
audience, capacity, approval requirements, and owner.

Resolve unknowns by asking in the channel now. A variable guessed at step 2 becomes a
wrong city name in a confirmation email at step 5.

The full sequence and its per-step checks are in
[references/build-sequence.md](references/build-sequence.md).

### 3. Run the sequence

1. **CRM campaign creation** — the campaign record everything else attaches to.
2. **Marketing automation campaign** — with its workflows and lists.
3. **Event platform setup** — registration and the event landing page.
4. **Email drafting** — invitation, confirmation, reminders.
5. **Landing page generation.**
6. **Integrations between them** — the step that is rarely complete out of the box,
   and the step where builds break.

Do not skip ahead when a platform is slow to respond. A half-created campaign in the
CRM that later gets a second attempt is worse than a delayed build.

### 4. Post the review update to Slack

When the landing page is ready for the requester's review and the audit takes over,
post the second scripted update.

### 5. Hand off to the audit — do not mark the task complete

The build is not done when the sequence finishes. It is done when a fresh agent has
verified it end to end: submitted a test registration on the live landing page,
opened the confirmation email, and confirmed everything looks right.

Hand off to that audit agent. It starts with no prior context, which is exactly the
property that makes its check worth having. Do not summarize your build for it, and
do not tell it what to look at — a briefed auditor inherits your assumptions.

The requester reviews the audited result before it ships.

### 6. Feed edge cases back into this skill

Every new edge case found in a build belongs in this skill. Cities with names that
differ between platforms, a venue that needs a different confirmation template, an
integration that silently drops a field — write them in rather than remembering them.

## Examples

**A field dinner.** Request routed from the queue with a date three weeks out. The
skill posts the pickup update, resolves the city and capacity from the intake form,
creates the CRM campaign, builds the automation campaign with its workflow and list,
sets up registration on the event platform, drafts the invitation and confirmation
emails, generates the landing page, wires the integrations, posts the review update,
and hands to the audit agent.

**A missing variable.** The intake form has no time zone for a virtual event with a
global audience. The skill asks in the channel before building rather than defaulting
to the requester's local zone — a defaulted time zone appears in every calendar
invite that goes out.

**An integration that half-worked.** Registrations land in the event platform but do
not flow to the CRM campaign. The skill catches this at step 6 rather than leaving it
for the audit, because verifying the integration is part of building it.

**A build the audit rejects.** The confirmation email surfaces the wrong city. The
audit agent finds it by opening the actual email after a test registration, and the
task is not marked complete. The fix goes into the build, and the cause goes into
this skill.

## Source

[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan and Annabel Custer, July 8, 2026
