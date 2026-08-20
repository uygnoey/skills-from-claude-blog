# The two lighter monitors

Alongside the hourly inbox skill, the post describes two "lighter skills that
help with my administrative workload." Both are small, scheduled, and end in a
notification or a draft — never an autonomous send.

## 1. No-show and gone-dark watcher

> "Every BDR knows the pain of meeting no-shows and prospects going dark. To
> address this, I built a skill that watches Gmail and Google Calendar to notify
> me when that happens, so I can follow up quickly."

**Watches:** Gmail and Google Calendar.

**Looks for:**
- meetings that did not happen,
- threads that have gone quiet.

**Produces:** a notification to the rep, in time for the follow-up to still be
timely.

**Why it is separate from the inbox skill:** the inbox skill reacts to threads
that need an answer. This one reacts to the *absence* of a thread — silence is
the signal, and nothing arrives in the inbox to trigger on.

**Worth deciding when you build it:**
- how long quiet counts as dark, per stage of the conversation,
- whether the notification carries a suggested follow-up or just the alert,
- how to avoid re-notifying about the same silence every run.

## 2. New-lead first touch

> "The other skill uses our CRM connector to scan for all new leads and draft a
> personalized first touch. It runs on a schedule throughout the day to ensure
> we don't leave leads waiting."

**Reads:** the CRM, through its connector.

**Looks for:** new leads not yet contacted.

**Produces:** a drafted, personalized first touch for the rep to review.

**Cadence:** multiple times a day rather than nightly — the stated reason is that
leads should not be left waiting.

**Worth deciding when you build it:**
- what "personalized" draws on for a lead with almost no history,
- which leads are worth a draft at all,
- how a drafted-but-unsent first touch is tracked so it does not get drafted
  twice.

## The shared shape

Both monitors follow the same pattern as the inbox skill:

| | Trigger | Output | Who acts |
| --- | --- | --- | --- |
| Inbox skill | hourly scan | draft reply | rep sends |
| No-show watcher | event absence | notification | rep follows up |
| New-lead first touch | scheduled CRM scan | drafted first touch | rep sends |

Scheduled work, reviewable output, a person on every send.

## Source

- https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale (August 7, 2026)
