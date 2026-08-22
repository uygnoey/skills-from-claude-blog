# How evals and benchmarks help with model choice

There are two common ways to see whether model capabilities are sufficient for your needs:
**standard benchmarks** and **custom evaluations**.

## Standard benchmarks

Benchmarks are a set of pre-determined tasks or scenarios, often for a specific domain, with known
solutions. They are helpful **directional** guides for evaluating capabilities across model classes
and across providers.

Named in the post:

| Benchmark | Domain |
|---|---|
| **GDPval-AA** | Knowledge work |
| **Terminal-Bench 2.1** | Agentic coding |
| **SWE-bench Pro** | Software engineering (used to report the advisor-strategy result) |

### The saturation problem

The challenge arises when evaluating powerful models, such as Opus and Fable, which can solve almost
all of the questions on the test — often referred to as **saturation**. A saturated benchmark stops
discriminating between the models you are actually choosing between, so a near-tie on the scoreboard
tells you nothing about which one will do better on your work.

## Custom evaluations

When benchmarks saturate, the recommendation is to use the models on **real workloads**, or test
them with **your own evaluations**.

A custom evaluation is typically:

- a **curated set of problems drawn from production**,
- **including difficult tasks where your current tools fall short**,
- with **success criteria your team defines**.

That last clause matters as much as the first: a custom eval without an explicit, team-owned
definition of success is a demo, not an evaluation.

This is where the capability and creativity of frontier models start to separate from the pack and
from one another.

## Why this is the load-bearing step

There is no one-size-fits-all approach to AI model selection, which is why multiple model classes
are available. The best way to select a model is to understand the basics of each model class and to
understand your use case in depth — which means **building, maintaining, and deploying strong
evaluations**.

Maintaining matters: a model choice made against an eval set that no longer reflects production is a
stale choice.

## Source

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
by Michael Segner — published July 24, 2026.
