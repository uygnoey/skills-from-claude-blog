---
name: background-task-delegation
description: Hand Claude Cowork a job that outlives one sitting — write the delegation brief, schedule it, and set the approval gates — so the work continues while you are away and only the decisions reach you. Use when a task accumulates over days rather than finishing in one session, when work should run overnight or before you arrive, when you will be moving between desk, phone, and web mid-task, or when the output must not ship until you have reviewed it. Built around the pattern of pointing Claude at the folder, thread, or half-finished deck and describing what done looks like.
---

# Delegating work that runs in the background

Asking an assistant for an answer and **handing it the work** are different things. Answers fit in a
sitting; handed-over work does not. It accumulates overnight, between meetings, on the train.

Cowork is where you hand Claude a task and it works across your files, calendar, email, messaging
app, the web, and the other tools you connect until the job is done. This skill is about writing that
handoff well: what to include in the brief, when to schedule it, and where the approval gates go.

Three properties of the delegation shape everything below:

- **The work follows you.** Start at your desk, check from your phone, pick up the finished output
  anywhere.
- **The work continues in the background.** Close the laptop; Claude keeps going. Scheduled tasks run
  with no device online.
- **The decisions still come to you.** When Claude reaches a call only you can make, it asks, and the
  question reaches your phone. Nothing ships until you have reviewed and approved it.

## Instructions

### 1. Pick a job that is actually a job

The best candidates are the work around the work — rarely in anyone's job description, but a large
share of everyone's week. In observed Cowork usage, more than 90% was not software development; the
largest categories were business operations and content creation, together roughly half of all usage.

Start with something already on your plate rather than inventing a demo task. Good shapes:

- Reconciling the quarter's spend and drafting the variance memo.
- Turning a folder of contracts into a renewals tracker with the risks flagged.
- Building tomorrow's client deck from call transcripts and pipeline data.

See [examples/delegation-briefs.md](examples/delegation-briefs.md) for these written out as briefs.

### 2. Point at the material, then describe what done looks like

The delegation has two halves, and briefs usually fail on the second one.

**Point at the material.** Name the folder, the thread, the half-finished deck, the calendar range,
the connected tool. Be specific about which one — "the contracts folder" is a pointer only if there
is exactly one.

**Describe what done looks like.** Not the steps — the finished state. "A renewals tracker with one
row per contract and the risks flagged" is a description of done. "Go through the contracts" is not.

Use [templates/delegation-brief.md](templates/delegation-brief.md) as the shape.

### 3. Decide when it runs

Two modes:

- **Now, and keep going.** Start it at your desk and walk away. Close the laptop and head to your
  meeting; Claude keeps going.
- **Scheduled.** Scheduled tasks run with no device online. Set Monday's client prep for 6 am: Claude
  works through the email threads, transcripts, and recent news, builds the briefing doc, and leaves
  the follow-up email drafted but unsent. Review it over coffee.

Schedule backwards from when *you* need to act on the output, not forwards from when you wrote the
brief.

### 4. Place the approval gates

State explicitly, in the brief, which actions require you and which do not. The default is that
nothing ships until you have reviewed and approved it — say what "ships" means for this task so the
line is unambiguous:

- Anything that sends, posts, or publishes.
- Anything that changes a system of record.
- Anything a third party would see.

Leave everything up to that line unblocked, so the work does not stall waiting on a decision that was
never yours to make. The pattern to aim for is the scheduled-prep example: the briefing doc is built,
and the follow-up email is **drafted but unsent**.

### 5. Expect to steer mid-flight, from wherever you are

When Claude reaches a call only you can make, it asks, and the question reaches your phone. You can
redirect a draft mid-meeting and Claude keeps going, on the right path.

So write the brief knowing you will be able to correct it. Do not try to pre-answer every possible
branch; state the outcome and the constraints you are sure about, and leave the genuinely open calls
to arrive as questions.

### 6. Pick the surface for the phase you are in

Desktop remains the place for deep work, and it is the full Cowork experience, where Claude can also
use your local files and browser. Web and mobile are where you check in and decide. See
[references/surfaces.md](references/surfaces.md).

## Examples

Full briefs in [examples/delegation-briefs.md](examples/delegation-briefs.md). In outline:

**Quarterly spend reconciliation.** Point at the finance exports and the ledger; done is a
reconciliation plus a drafted variance memo. Gate: the memo is not sent.

**Contracts folder to renewals tracker.** Point at the folder; done is one row per contract with
renewal date, owner, and flagged risks. Gate: nothing leaves the tracker.

**Client deck from transcripts and pipeline data.** Point at the call transcripts and the pipeline
view; done is tomorrow's deck. Gate: it stays a draft until you have reviewed it.

**Monday client prep, scheduled for 6 am.** Point at the email threads, transcripts, and recent news;
done is a briefing doc plus a follow-up email drafted but unsent. Runs with no device online.

## Source

["Claude Cowork is coming to mobile and web"](https://claude.com/blog/cowork-web-mobile) — published
July 7, 2026.
