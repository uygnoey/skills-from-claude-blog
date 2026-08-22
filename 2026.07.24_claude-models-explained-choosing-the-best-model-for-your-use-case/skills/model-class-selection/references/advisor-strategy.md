# The advisor strategy

> The advisor strategy allows faster, lower-cost worker models to call more intelligent models to
> check their plan and evaluate their work, leading to improved performance.

Instead of choosing one class for the whole task, you split the work across two:

| Role | Model class | Responsibility |
|---|---|---|
| **Worker (executor)** | Faster, lower-cost class | Carries out the task end to end: plans, executes, produces the result. |
| **Advisor** | More intelligent class | Reviews the worker's plan before execution and evaluates the worker's output afterwards. |

The defining property is that **the executor model is coached only when needed**. The advisor is not
in the loop for every token — it is consulted at the decision points where a better judgment call
changes the outcome.

## Reported result

On **SWE-bench Pro**, **Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5's score at 63% of
the price** of using Fable 5 for the whole task.

Read that as: most of the top class's quality, at roughly two-thirds of the cost — because the
expensive model is only paying for review, not for every step of execution.

## When to reach for it

- A workload currently runs entirely on the top class and is under cost pressure — try the advisor
  split before dropping a class outright.
- A workload runs on a cheaper class and evals show it failing on planning quality or on
  self-assessment, rather than on raw execution.
- The task has clear checkpoints — a plan to approve, an output to grade — where a second opinion
  can be inserted cheaply.

## What to measure

Compare three configurations on the same eval set:

1. Worker class alone.
2. Advisor class alone (the quality ceiling and the cost ceiling).
3. Worker + advisor.

Report both the score and the price for each, the way the SWE-bench Pro figure above does. The
advisor strategy is worth it when configuration 3 lands close to configuration 2's score at
meaningfully less than configuration 2's price.

## Shipped as subagents

The two roles in this post's `agents/` folder implement this split:

- `agents/task-executor.md` — the worker.
- `agents/plan-advisor.md` — the advisor.

## Source

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
by Michael Segner — published July 24, 2026.
