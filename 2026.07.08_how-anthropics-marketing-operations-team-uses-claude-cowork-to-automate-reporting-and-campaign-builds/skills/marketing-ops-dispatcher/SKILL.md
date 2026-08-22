---
name: marketing-ops-dispatcher
description: Hourly intake triage for a marketing operations request queue. Reads the intake channel, picks the most urgent request, stamps the ticket so the work is not duplicated, and hands off to the right specialist skill — event build, data import, apply-to-attend, or approval support. Does no setup work itself. Use when requests arrive in a shared channel through an intake form and several specialist workflows exist behind them.
---

# Marketing ops dispatcher

The dispatcher decides what runs next. It does not do the work.

Keeping routing separate from doing is the point: each specialist skill can be
refined on its own, as edge cases surface, without touching the routing logic. A
dispatcher that also builds events becomes the file everyone is afraid to edit.

Runs once an hour on a scheduled task.

## Instructions

### 1. Read the intake channel

Requests arrive through an intake form where the requester specifies the type of help
they need. The four types are:

- **Event build** — the most complex request type.
- **Data import**
- **Apply-to-attend**
- **Approval support**

Read the channel for new, unstamped requests since the last run.

### 2. Pick the most urgent request

One request per run. Ranking criteria are in
[references/triage-rules.md](references/triage-rules.md) — event date proximity comes
first, because an event build that starts too late cannot be recovered by working
faster.

### 3. Stamp the ticket before doing anything else

Stamping is what stops the work from being duplicated — by the next hourly run, by
another agent, or by a person who saw the request in the channel. Stamp first, hand
off second. A run that stamps after handing off has a window where two workers can
pick up the same ticket.

The stamp records: which run picked it up, when, and which specialist it was routed
to.

### 4. Route to exactly one specialist

| Request type | Specialist |
| --- | --- |
| Event build | The event-build skill — full sequence across CRM, marketing automation, event platform, email, landing page, and the integrations between them |
| Webinar landing page | The webinar landing page creation skill |
| Apply-to-attend | The apply-to-attend skill — in-flight changes to the registration flow |
| Approval support | The approval-support skill — event approvals and the appropriate emails on a scheduled cadence |
| Data import | The data-import skill — scrubs lists and processes attendee data |

Each specialist is described in
[references/specialist-skills.md](references/specialist-skills.md). Only the
event-build skill is bundled in full alongside this one; the others are described as
the post describes them.

### 5. Do no setup work

If a request is ambiguous, ask the requester in the channel — do not resolve it by
starting the work and seeing what happens. If a request spans two types, route it to
the primary one and note the secondary in the stamp.

### 6. Hand off and stop

After handing off, the run is finished. Do not follow the specialist's progress, and
do not pick up a second request in the same run. The next hourly run picks up the
next one.

## Examples

**A normal hour.** Three new requests: a data import for a list of 400 attendees, an
event build for a field dinner in three weeks, and an approval-support request. The
dispatcher ranks the event build first on date proximity, stamps it, routes to the
event-build skill, and stops. The other two wait for the next runs.

**A duplicate.** A requester posts the same event twice. The second request is already
covered by the first stamp; the dispatcher notes it in the channel as a duplicate of
the stamped ticket rather than routing it again.

**An ambiguous request.** "Can you help with the webinar next month?" — no type
selected. The dispatcher asks in the channel which of the four types it is, and leaves
the ticket unstamped so it can be picked up once answered.

**A spanning request.** An event build that also needs a list scrubbed. Routed to the
event-build skill as primary, with the data import noted in the stamp so it is not
forgotten.

## Source

[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan and Annabel Custer, July 8, 2026
