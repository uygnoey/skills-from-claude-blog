# The specialist skills behind the dispatcher

The dispatcher routes to one of five specialists. Each is a separate skill so it can
be refined on its own as edge cases surface, without touching the routing.

Only the event-build skill is bundled in full alongside this one. The others are
described here as the post describes them — enough to build from, without inventing
detail the post does not give.

---

## Event build

**Scope.** The most complex request type. Handles the full sequence end to end:

1. CRM campaign creation.
2. Marketing automation campaign, with workflows and lists.
3. Event platform setup.
4. Email drafting.
5. Landing page generation.
6. All of the integrations between them.

**Slack updates.** Two, scripted into the skill: when Claude picks up the request, and
when the landing page is ready for the requester's review and the audit takes over.

**Handoff.** When the build is done, it hands off to a fresh agent for audit.

See the bundled `event-build` skill for the full version.

---

## Webinar landing page creation

**Scope.** Spins up landing pages for webinars.

**Why it is separate from the event build.** A webinar landing page is a smaller,
higher-frequency request than a full event build, and separating it keeps the
event-build sequence from being edited every time a webinar page needs a tweak.

---

## Audit

**Scope.** Verifies the event-build skill's output before the task is marked complete.

**Key property.** Run by a separate, fresh Claude instance with no prior context. The
agent that did the build is not the agent that checks it.

See the bundled `build-auditor` agent for the full version.

---

## Apply-to-attend

**Scope.** Handles in-flight changes to the registration flow.

**Note.** These changes land on a flow that is already live and that people may be
using right now, which is why they rank above ordinary queued work in triage.

---

## Approval support

**Scope.** Handles event approvals and sends the appropriate emails at a scheduled
cadence.

**Note.** The cadence is scheduled, so this specialist is partly self-triggering
rather than purely dispatcher-driven.

---

## Data import

**Scope.** Scrubs lists and processes attendee data.

---

## Keeping them current

Each specialist is updated as new edge cases are found. When a run misfires, the
manager agent diagnoses it and proposes the adjustment; anything worth keeping goes
back into the relevant specialist skill — not into the dispatcher, unless the misfire
was a routing decision.
