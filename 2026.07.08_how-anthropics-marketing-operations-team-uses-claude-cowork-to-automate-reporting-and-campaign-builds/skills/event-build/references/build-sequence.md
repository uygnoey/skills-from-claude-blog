# The build sequence

Six steps, in order, across four vendor platforms. The order matters: each step
attaches to something the previous one created.

---

## 0. Resolve variables (before step 1)

| Variable | Why it matters |
| --- | --- |
| Event name | Appears in the CRM record, every email, and the page title; renaming later means editing four platforms |
| Event type | Determines which specialist path and which email set applies |
| Date, time, time zone | A defaulted time zone reaches every calendar invite |
| City / location, exactly as it should appear | This is the field that produces the classic bug — a confirmation email with the wrong city name |
| Audience and list criteria | Determines the automation list |
| Capacity | Determines registration behaviour when full |
| Approval requirements | Determines whether approval support is also involved |
| Owner | Who reviews the audited result |

Anything unresolved is asked in the channel before building starts.

---

## 1. CRM campaign creation

The campaign record everything else attaches to. Create it first so the automation
campaign and the event platform both have something to reference.

**Check before moving on:** the campaign exists, is named per convention, and has the
event date and owner set.

---

## 2. Marketing automation campaign

The campaign that runs the email sequences and the automation behind them, including
its workflows and lists.

**Check before moving on:** the workflow is attached to the right list, the list
criteria match the intended audience, and the campaign is linked to the CRM record
rather than standing alone.

---

## 3. Event platform setup

Registration and the event landing page live here.

**Check before moving on:** registration is open (or scheduled to open), capacity is
set, and the event details — date, time zone, location — match what was resolved at
step 0 rather than a template's defaults.

---

## 4. Email drafting

Invitation, confirmation, and reminders as the event type requires.

**Check before moving on:** every merge field resolves. Cloning from a nearby template
is exactly how a confirmation email ends up surfacing the wrong city name, so verify
the rendered output rather than the template.

---

## 5. Landing page generation

**Check before moving on:** the page renders, the registration form submits, and links
resolve. A broken landing page is the other classic clone-from-template bug.

---

## 6. Integrations between them

The step that is rarely complete out of the box and the one where builds break.

**Check before moving on:**

- A registration on the event platform creates or updates the CRM record.
- The CRM record is associated with the campaign from step 1.
- The automation workflow fires on registration.
- The confirmation email actually sends, with correct content.

Verifying an integration is part of building it. Do not leave this for the audit — the
audit is a second, independent check, not the first one.

---

## Handoff

When the sequence is complete, post the review update and hand off to the audit agent,
which starts with no prior context. Do not mark the task complete yourself.
