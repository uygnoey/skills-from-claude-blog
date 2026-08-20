# Analytical skills the agent needs beyond data access

Knowing which tables to query is necessary but not sufficient. The source lists five analytical skill areas to write down. In every case these are **documentation of practices your analysts already follow**, not new methodology — the point is consistency between what the agent produces and what a human analyst would have produced.

## Forecasting
Cover trend fitting and how seasonality is assumed. An agent that fits a trend differently from your analysts will produce numbers that disagree with the team's own forecasts for reasons nobody can locate.

## Cohort and retention analysis
Cover the standard cohort definitions and how retention curves are constructed. Retention is one of the metrics most prone to silently divergent definitions, so the canonical version has to be written down.

## Funnel analysis
Cover the canonical stage definitions. If the funnel stages in the agent's answers do not match the funnel stages in the team's dashboards, every answer becomes a reconciliation exercise.

## Charting
Cover the visualization conventions the team uses — what gets charted which way, and how.

## Analytical writing
Cover structure, hedging, and confidence levels. This is what turns a correct number into a usable answer: the reader needs to know how much to trust it and what the caveats are, in the form the organization already recognizes.

## How to source these
Write them from what analysts on the team already do. Where practice is inconsistent, this exercise surfaces the inconsistency — resolve it once, then encode the resolution.

Sequence note: the source recommends creating these analytics skills **last**, informed by the questions users actually asked, rather than guessing the set up front. See [rollout-sequence.md](rollout-sequence.md).

## Source
- https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
