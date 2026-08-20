# Evaluation dimensions

The dimensions worth scoring separately when comparing a new frontier model against the
model you currently default to. Each one answers a different deployment question, so
collapsing them into a single score throws away the routing decision.

## 1. Pass rate, per language

**What it is.** Share of eval tasks the model completes such that the repository's own
tests pass.

**How to compute.** Run the full private eval set per language and report each language
separately. A model that leads decisively on one ecosystem may only tie on another.

**Why it matters.** This is the headline number, but on its own it tells you nothing
about *where* the gain came from or what it cost.

**Reference point.** In JetBrains' private-repo suite, Claude Fable 5 passed 44.3% of
Python tasks against 28.2% for Opus 4.8 — a roughly 16-point gap.

## 2. Head-to-head win/loss split

**What it is.** Of the tasks where the two models disagree, how many does the new model
solve that the incumbent missed, and how many does it lose that the incumbent solved.

**How to compute.** Pair the runs task-by-task rather than comparing aggregates. Report
`won: N, lost: M` alongside the pass rates.

**Why it matters.** A uniform lift and a lopsided trade produce the same average but very
different risk. If the new model loses tasks the old one reliably solved, those task
types are candidates to keep routing to the incumbent.

**Reference point.** Fable 5 solved 18 Python tasks Opus 4.8 missed while losing 2.

## 3. Runs-but-wrong rate

**What it is.** Among attempts whose code actually executed, the share that produced the
wrong answer.

**How to compute.** Separate three outcomes rather than two: *failed to run*, *ran and
was wrong*, *ran and was right*. The middle bucket is the one to track.

**Why it matters.** Code that crashes announces itself. Code that runs and quietly
produces a wrong answer is the most expensive kind of failure to catch — it consumes
reviewer attention and can reach production. Weight this above raw pass rate when
choosing a model for autonomous or long-running work.

## 4. Steps to solution

**What it is.** Number of turns / tool calls the model consumed before arriving at a
working answer.

**How to compute.** Log turn counts per task and compare medians, not means — a few
runaway runs will distort the average.

**Why it matters.** Two things at once. It is a direct cost multiplier on agentic work,
and it is a proxy for engineering judgment: a model that stops trying to pull an external
resource it does not need is displaying better habits, not just being lucky.

**Reference point.** Fable 5 reached solutions in roughly 22% fewer steps than Opus 4.8.

## 5. Cost per task

**What it is.** Total spend to complete a task end-to-end, including retries.

**How to compute.** `tokens_consumed × price` summed across every turn of every attempt,
divided by tasks completed successfully. Compute it per workload class, since long-running
agentic work and short routine edits behave differently.

**Why it matters.** Per-token price is the wrong unit. A model can be more expensive per
token and still cheaper per task on complex, long-running work because it takes fewer
steps and retries less. This is exactly the case that a single "cheapest model"
leaderboard would hide.

## 6. Latency / throughput

**What it is.** Wall-clock time to completion.

**Why it matters.** It is the deciding dimension for interactive, in-editor use even when
it loses on quality. Keep it as its own leaderboard rather than folding it into a
composite score.

## Scoring discipline

- Re-run the **same** eval set on each release so comparisons stay apples-to-apples.
- Verify that a model's real-world behaviour matches its public benchmark scores before
  trusting the scores; treat a gap between the two as a signal about the model's tuning.
- Record every round — see `templates/leaderboard-record.md` in this skill folder.

## Source

- https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5 (August 13, 2026)
