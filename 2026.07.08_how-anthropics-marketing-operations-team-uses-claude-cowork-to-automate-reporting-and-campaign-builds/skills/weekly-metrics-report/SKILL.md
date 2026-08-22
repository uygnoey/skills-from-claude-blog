---
name: weekly-metrics-report
description: Assemble a weekly marketing metrics review when the numbers are scattered across a dashboard, a data warehouse, Slack, and call transcripts. Use to run the Sunday-night data hunt, produce metrics tables with suggested headlines, expand a confirmed headline into narrative with supporting detail, generate the leadership slide from the same data, and turn follow-ups into tasks. Also use at the quarter turn, when quarterly plans lead instead of weekly movement. Flags mismatches between sources rather than reconciling them silently.
---

# Weekly marketing metrics report

In a perfect world every metric would already be in a dashboard and the job would be
writing the narrative. In practice some metrics are in the dashboard, some have not
made it there from the warehouse, some have not been piped into the warehouse yet,
and new ones exist only in a Slack message or a call transcript. This skill does the
hunt, then hands a human the narrative decision.

Target shape: a process that used to take one to two days a week takes up to two
hours, with the human time spent on judgment rather than retrieval.

## Instructions

### 1. Run the data hunt on a schedule, before the session

Set this to run every Sunday evening (see
[references/scheduled-run.md](references/scheduled-run.md)). The scheduled run:

1. Reads the previous week's review, so continuity and prior focus areas carry over.
2. Reads the latest meeting transcript.
3. Checks Slack for what the sales team is focused on.
4. Queries the data warehouse for the metrics that live there.
5. Leaves a folder containing the numbers and a few suggested focus areas.

Nothing in this step decides the story. It gathers, and it proposes.

### 2. Open with the initial report

Monday morning, the initial report is already assembled: the metrics tables plus
suggested headlines, i.e. candidate areas of focus. Use
[templates/weekly-report.md](templates/weekly-report.md) for the shape.

Present the suggested headlines as choices, not conclusions. The human confirms one
or redirects to another.

### 3. Expand only what was confirmed

Once the human has confirmed or decided where to focus the narrative, expand those
headlines with supporting details and examples. Do not expand a headline that was
not chosen — an unchosen headline stays a one-line candidate.

The right focus varies by week:

- A sales priority the team is responding to.
- A product launch.
- At the quarter turn: lead with quarterly plans, and take the quarterly review doc
  as input.

### 4. Flag mismatches instead of guessing

When numbers do not line up, say so and ask how to handle it. Do not pick the source
that looks more plausible, and do not silently average or reconcile.

The worked case: after a reorg on the sales team, marketing's reporting no longer
matched theirs. The correct behaviour was to flag the gap and ask, because the answer
was a definitional decision a person had to make — not a data error to fix.

Definitions, regional structures, and segment boundaries are the usual sources of
mismatch. Record each resolution back into this skill so the same question is not
re-asked next week.

### 5. Proofread before anything leaves the draft

Every number in the draft is checked against a verified source by the separate
proofreading skill bundled with this post. Numbers that cannot be traced do not ship;
they become an open question in the report.

### 6. Generate the leadership slide from the same data and narrative

The slide answers three things: what changed, why, and what the teams are doing about
it. It is generated from the same data and narrative as the report, not written
separately — that is what keeps them from drifting apart.

### 7. Turn follow-ups into tasks

Any follow-up raised in the session becomes a task in the team's tracker, with the
context needed to act on it without rereading the report.

### 8. Close the session by updating this skill

At the end of every weekly session, ask what came up that should go back into the
skills. Typical entries:

- A structural change, such as a sales reorg, that redefines a metric's grouping.
- A correction the human made to a number, a label, or a framing.
- A new way they wanted the headlines framed.

Write those into this skill immediately. A correction you make twice belongs in a
skill; the second time is already too late to be efficient.

## Examples

**A normal week.** Sunday's run leaves a folder with the metric tables and three
suggested focus areas: pipeline from a webinar series, a dip in organic signups, and
a lift in enterprise trials. Monday, the human says the dip is the story because
sales is asking about it. The skill expands that headline with the weekly series,
the segment breakdown, and two example accounts, leaves the other two as one-liners,
generates the leadership slide, and files three follow-ups as tasks.

**A mismatch.** Marketing's regional pipeline totals do not match the sales team's
after their reorg. The skill reports both figures side by side, names the
grouping that differs, and asks which definition the report should use. The answer
goes into the skill so next week's run applies it.

**The quarter turn.** The human feeds in the quarterly review doc. The report leads
with quarterly plans, and the weekly movement becomes supporting material rather than
the headline.

**A metric with no source of truth.** A number appears only in a Slack thread. It is
included with its provenance stated as the Slack thread, flagged as unverified by
proofreading, and logged as a candidate for the warehouse.

## Source

[How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) — Ian Chan and Annabel Custer, July 8, 2026
