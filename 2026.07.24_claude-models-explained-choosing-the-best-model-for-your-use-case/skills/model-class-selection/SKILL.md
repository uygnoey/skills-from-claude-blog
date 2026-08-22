---
name: model-class-selection
description: Choose which Claude model class — Mythos/Fable, Opus, Sonnet, or Haiku — to run a workload on, and use effort level to dial in the quality/speed/cost balance. Use when picking a model for a new production workload, when revisiting a model choice after evals show a gap, when a workload is latency- or cost-sensitive enough that a lower class is worth testing, or when deciding whether to pair a cheaper worker model with a more capable advisor. Default recommendation is to start with the most intelligent generally available model and tune down, because cost-per-task is often lower on more capable models even when price-per-token is higher.
---

# Choosing a Claude model class for a workload

Claude model classes do not specialize by domain. There is no finance model and no science model —
every Claude model is trained to excel at coding, agentic tasks, and knowledge work. The difference
between classes is **how hard a problem the class can reliably carry, and what that capability costs
in price and speed**.

So model selection is not "which model is good at my field." It is "how hard is my task, and what
am I willing to pay in latency and dollars to have it reliably done."

## Instructions

### 1. Start with the most intelligent generally available model

The default recommendation is to **start smart**: begin on the most intelligent model class you can
access, then use **effort level** to dial in performance and cost.

Two reasons this beats starting small:

- **Cost-per-task is often lower on more capable models**, especially at lower effort levels, even
  though price-per-token is higher. More capable models tend to take fewer turns and less thinking
  time to get a task right.
- **Starting on a smaller model blurs your diagnostics.** When something fails, you cannot easily
  tell a model failure from a setup failure.

Then, as latency- or cost-sensitive use cases arise, test lower classes until you find the fit.

The opposite direction is also legitimate: some organizations start with the most cost-effective
model and move **up** classes until the quality bar is met. Both directional approaches are
supported. Pick one and be consistent, so the results of your tests are comparable.

### 2. Know what each class is for

See [references/model-classes.md](references/model-classes.md) for the full descriptions, including
the Mythos vs. Fable packaging distinction and the rule of thumb for Opus vs. Fable.

Short form:

| Class | What it is for |
|---|---|
| **Mythos / Fable** | Most capable class, frontier across domains. Coding, long-running agent tasks, and problems AI has not reliably handled before. |
| **Opus** | Powerful class for reasoning-intensive enterprise tasks. Leading on GDPval-AA (knowledge work) and Terminal-Bench 2.1 (agentic coding). |
| **Sonnet** | Versatile class for everyday tasks. Best balance of performance, cost, and speed for the widest set of general-purpose use cases, including high-volume sub-agents in multi-agent orchestration. |
| **Haiku** | Lowest cost, fastest class. Built for high-frequency workloads where latency and cost matter. |

### 3. Ask the four selection questions

Work through these in order for the specific workload. Full treatment with follow-up prompts in
[references/selection-questions.md](references/selection-questions.md).

1. **How hard is this task?** If it typically takes a lot of time, involves multiple steps, or is
   previously unsolved, a more capable model class is appropriate.
2. **What are the latency needs?** If the model sits in a high-frequency, customer-facing workload,
   Sonnet is often the best choice.
3. **What are the access constraints?** Mythos is only available to organizations under Project
   Glasswing, and not all organizations make all model classes available to all roles.
4. **What are the unit economics?** Higher production volumes may suit lower model classes,
   particularly where evaluations show those tasks are completed satisfactorily. Models are priced
   differently per token and have different price-per-task costs depending on capability and effort.

### 4. Use effort level as the second dial

Effort level also shifts the balance of quality, speed, and cost. Two facts to hold together:

- Higher-class models at **higher** efforts give the best possible performance.
- Higher-class models at **lower** efforts can sometimes be **more efficient than smaller models**.

That second point is why "start smart and dial down effort" is often cheaper than "start small."
Do not treat class and effort as one axis — search the grid.

### 5. Consider the advisor strategy before settling for a single model

You do not have to run the whole task on one class. In the **advisor strategy**, a faster,
lower-cost worker model calls a more intelligent model to check its plan and evaluate its work.
The executor is coached only when needed.

The reported result: on SWE-bench Pro, **Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5's
score at 63% of the price** of using Fable 5 for the whole task.

Details and the two roles in [references/advisor-strategy.md](references/advisor-strategy.md); the
role definitions are also shipped as subagents in this post's `agents/` folder.

### 6. Decide with evals, not with vibes

Standard benchmarks are useful **directional** guides across classes and providers, but they
saturate: powerful models such as Opus and Fable solve nearly everything on the test, so the
benchmark stops discriminating.

When that happens, run the models on real workloads or on your own evaluations — a curated set of
problems drawn from production, including difficult tasks where your current tools fall short, with
success criteria your team defines. That is where the capability and creativity of frontier models
separate from the pack and from one another.

See [references/evals-and-benchmarks.md](references/evals-and-benchmarks.md).

### 7. Re-run the choice when conditions change

There is no one-size-fits-all model choice, which is why multiple classes exist. Selecting well
means understanding the basics of each class and understanding your use case in depth — which in
practice means building, maintaining, and deploying strong evaluations, then revisiting the choice
when the workload, the volume, or the model lineup moves.

## Examples

Worked scenarios in [examples/selection-scenarios.md](examples/selection-scenarios.md). Summary:

**A previously unsolved research-style task, low volume.**
Question 1 dominates: multi-step, long-running, not reliably solved before. Start on the most
capable class available. Volume is low, so unit economics barely bind. Tune effort down only if
evals hold.

**A customer-facing support assistant answering thousands of sessions an hour.**
Question 2 dominates: high-frequency and customer-facing, so Sonnet is often the best choice.
Validate with a custom eval built from real production tickets before committing.

**A high-volume classification or extraction step inside a larger pipeline.**
Questions 2 and 4 dominate: latency and cost matter, the task is narrow. Haiku is the class built
for this shape. Confirm with an eval that the task is completed satisfactorily at that class.

**Sub-agents inside a multi-agent orchestration.**
Sonnet is explicitly called out for high-volume sub-agents. Keep the orchestrator on a higher class
if the planning is the hard part.

**Opus clears the bar but you are tempted by Fable.**
Rule of thumb: if evals or internal testing show Opus struggling on some tasks, Fable is the answer.
If Opus already clears the quality bar, its speed and price profile may make it the better choice.

**Cost pressure on a workload that currently runs entirely on the top class.**
Before dropping a class outright, test the advisor strategy: worker on the cheaper class, advisor on
the top class, invoked only to check plans and evaluate work.

## Source

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
by Michael Segner — published July 24, 2026.
