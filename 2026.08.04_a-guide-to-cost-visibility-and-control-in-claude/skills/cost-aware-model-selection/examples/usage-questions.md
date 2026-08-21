# Usage questions and which tool answers them

Three observation tools, each suited to a different kind of question.

## Analytics Chat — when you want an answer, not a report

Natural-language questions about usage, without generating a full report. Two examples given in
the source:

> Who are our top spenders this month?

> Which team's usage grew fastest this quarter?

This is the right tool for the questions that come up in the middle of something else — a budget
conversation, a rollout decision, a spike you noticed. The value is the absence of a reporting
cycle between the question and the answer.

Other questions in the same shape:

- Which model is most of our spend going to?
- Is any individual approaching their cap?
- Did usage change after we widened access to a new department?

## Usage analytics — when you need the breakdown

Spend broken down by **person, team, and model**. Data exports **align with invoices**, which
makes this the tool for billing reconciliation specifically — the numbers are meant to tie out.

Use it for:

- Reconciling a month's spend against the invoice.
- Finding which team or which model a change in total spend came from.
- Establishing the baseline before a rollout widens.

## Analytics API — when the answer belongs somewhere else

The same data, delivered to existing business systems: **business intelligence tools, finance
systems, and internal dashboards**.

Use it when the recurring consumer of the number is a system rather than a person — a finance
close process, a chargeback model, a dashboard a team already watches. Anything you find
yourself exporting on a schedule belongs here instead.

## What to watch during a phased rollout

While access gating is still holding most of the organization back, the observation window is
what tells you where to set caps. Worth watching:

- **Per-person spread within an enabled group.** A wide spread usually means the workload split
  is uneven, not that someone is misusing it — set caps against the shape you see, not the mean.
- **Model mix against the defaults you set.** If people are routinely overriding the default to
  a more capable model, either the default is wrong for that team or the work is harder than
  assumed.
- **Rapidly changing usage patterns.** Administrators can track these directly. A sharp move is
  worth understanding in either direction — a sudden drop is as informative as a spike.
- **Users approaching limits.** Identify them before the cap interrupts work, and use automated
  spend-limit increase requests so the admin is not a bottleneck for legitimate work.
