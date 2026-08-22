# The Sunday-night scheduled run

The report does not start on Monday. A scheduled task runs every Sunday evening and
leaves the work already done, so the Monday session starts from numbers rather than
from a search.

## What the scheduled run does

| Step | Source | Why it is in the list |
| --- | --- | --- |
| Read the previous week's review | Last week's output | Continuity: prior focus areas, open questions, and framing carry over |
| Read the latest meeting transcript | Meeting recording / transcript | New metrics sometimes exist only here |
| Check Slack for sales focus | Slack channels | What the sales team is focused on shapes which movement matters this week |
| Query the data warehouse | Warehouse | The metrics that have made it into the pipeline |
| Leave a folder | Output location | The numbers plus a few suggested focus areas |

## Why the sources are mixed

The reporting stack is never complete, and waiting for it to be complete is how a
weekly report becomes a two-day job. In practice:

- Some metrics are already in the dashboard.
- Some have not made it to the dashboard from the warehouse.
- Some have not been piped into the warehouse yet.
- New ones might exist only in a Slack message or a call transcript.

The business moves faster than a traditional reporting pipeline can keep up with. The
scheduled run is what absorbs that gap.

## What it must not do

- It must not decide the narrative. It proposes focus areas; the human picks.
- It must not reconcile conflicting numbers. It reports the conflict.
- It must not drop a metric because the source is informal. A number from a Slack
  thread is included with its provenance stated.

## Setting it up

Create a scheduled task that runs Sunday evening with the prompt shaped as:

```
Read last week's review and the latest meeting transcript. Check the sales channels
in Slack for what the sales team is focused on this week. Query the warehouse for
the standard weekly metric set. Leave a folder containing: the metrics tables, any
numbers whose sources disagree (with both figures and where each came from), and
three to five suggested focus areas with a one-line reason each. Do not write the
narrative.
```

Work that runs on its own every Sunday night is work no one has to remember to do.
The same principle applies to any recurring step in this workflow — if it has a fixed
cadence, schedule it rather than depending on a person to trigger it.
