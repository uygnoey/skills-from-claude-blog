# Template — the two scripted Slack updates

The event-build skill scripts exactly two Slack updates. They are written into the
skill rather than left to judgment, so every build reports at the same two points and
the channel reads consistently.

## 1. On pickup

Posted before any platform work starts.

```
:inbox_tray: Picked up: *<event name>* (<event type>, <date>)
Requested by: <requester>
Ticket: <link or id>

Starting the build now — CRM campaign, automation campaign, event platform,
emails, landing page, integrations. I'll post again when the landing page is
ready for your review.
```

## 2. When the landing page is ready for review

Posted when the sequence is complete and the audit takes over.

```
:white_check_mark: Landing page ready for review: *<event name>*
Landing page: <url>
Registration: <url>

Built: CRM campaign · automation campaign (workflows + lists) · event platform ·
emails (<which>) · landing page · integrations

Now handing off to the audit — a fresh session will submit a test registration,
open the confirmation email, and check the result before the task is marked
complete. <requester>, please review the page in the meantime.
```

## Why exactly two

- **Pickup** tells the requester and the channel that the request is being worked, and
  pairs with the dispatcher's ticket stamp so nothing is picked up twice.
- **Ready for review** is the point where a human has something to look at and the
  audit begins.

Intermediate progress updates are not posted. A channel that receives an update per
platform stops being read, and the useful signal — "this needs your eyes now" — gets
lost in it.
