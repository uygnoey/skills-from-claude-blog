**English** · [한국어](./choosing-a-claude-model.ko.md) · [Español](./choosing-a-claude-model.es.md) · [日本語](./choosing-a-claude-model.ja.md)

# Choosing the right Claude model for your use case

"What model should I choose for this workload?" is one of the most frequent questions Anthropic
hears. As more model classes and versions have shipped, the answer has become more nuanced. This
guide walks the model family, the questions to ask, and the practices that make the answer stick.

## The default recommendation: start smart

Set the nuance aside for a moment. The default recommendation is to **start with the most intelligent
generally available model and use effort level to dial in performance and cost.**

Two reasons:

- **Cost-per-task is often lower for more intelligent models**, especially at lower effort levels,
  even when price-per-token is higher. More capable models often take fewer turns and less thinking
  time to get most tasks right.
- **Starting with a smaller model makes diagnosis harder.** When something fails, you cannot easily
  tell a model failure from a setup failure.

As use cases arise that are more latency- or cost-sensitive, test lower-tier models until you find
your fit.

Some organizations prefer the opposite direction — start with the most cost-effective model and move
up classes until the quality bar is met. Both directional approaches appear in Anthropic's model
selection documentation. Either works; consistency is what makes the results comparable.

## The Claude model family

The family — Fable, Opus, Sonnet, Haiku — balances intelligence, speed, and cost differently at each
class. Model classes do **not** specialize by domain: there is no finance model and no science model.
Every Claude model is trained to excel at coding, agentic tasks, and knowledge work. The difference
is how hard a problem a class can reliably carry, and what that costs in price and speed.

### Mythos / Fable

The most capable class, with frontier capabilities across domains — especially strong at coding,
long-running agent tasks, and solving problems AI has not reliably handled before.

The class ships in two packages of the same underlying model. **Claude Mythos** is for trusted
organizations handling dual-use cybersecurity and biology work. **Claude Fable** is packaged with
additional safeguards that make the model safe for use by the general public. Both require limited
data retention so they can be used safely.

### Opus

The powerful class for reasoning-intensive enterprise tasks. Opus models consistently rank among
leading models on benchmarks such as **GDPval-AA** for knowledge work and **Terminal-Bench 2.1** for
agentic coding.

Opus vs. Fable is the genuinely hard call, since both excel at coding, long-running agents, and
knowledge work. In real-world situations, larger models such as Fable tend to have more wisdom,
creativity, and writing skills despite similar benchmark scores. The rule of thumb: **if your evals
or internal testing show Opus struggling on some tasks, Fable is the answer. If Opus already clears
the quality bar, its speed and price profile may make it the better choice.**

### Sonnet

The versatile class for everyday tasks — a balance of performance, cost, and speed across the widest
set of general-purpose use cases, including **high-volume sub-agents in multi-agent orchestration
setups**.

### Haiku

The lowest-cost, fastest class, designed for **high-frequency workloads where latency and cost
matter**.

## Four questions for choosing a class

1. **How hard is this task?** If it typically takes a lot of time, involves multiple steps, or is
   previously unsolved, a more capable class is appropriate.
2. **What are the latency needs?** If the model is involved in high-frequency customer-facing
   workloads, Sonnet is often the best choice.
3. **What are the access constraints?** Mythos is only available to organizations under Project
   Glasswing, and not all organizations make all classes available to all roles.
4. **What are the unit economics?** Higher production volumes may suit lower classes, particularly
   where evaluations show those tasks are completed satisfactorily. Models are priced differently
   per token and carry different price-per-task costs depending on capability and effort level.

### Effort is the second dial

Effort level also shifts the quality/speed/cost balance. Higher-class models at higher efforts offer
the best possible performance — and **higher-class models at lower efforts can sometimes be more
efficient than smaller models**. That is why "start smart, then lower effort" often beats "start
small." Search the grid of class × effort rather than a single axis.

## Combining strengths: the advisor strategy

You do not have to run the whole task on one class. The **advisor strategy** lets faster, lower-cost
worker models call more intelligent models to check their plan and evaluate their work.

Because the executor is **coached only when needed**, the improvement is substantial relative to the
cost. On **SWE-bench Pro, Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5's score at 63% of
the price** of using Fable 5 for the whole task.

## How evals and benchmarks help

Two common ways to check whether capabilities are sufficient:

**Standard benchmarks** are pre-determined tasks with known solutions, often domain-specific. They
are useful directional guides across classes and providers. The problem is **saturation**: powerful
models such as Opus and Fable solve almost all the questions, so the benchmark stops discriminating
between the models you are actually deciding between.

**Custom evaluations** are the answer when that happens. Use the models on real workloads, or test
them with your own evaluations — typically a curated set of problems drawn from production,
including difficult tasks where your current tools fall short, with success criteria your team
defines. This is where the capability and creativity of frontier models start to separate from the
pack and from one another.

## Making the smart choice

There is no one-size-fits-all approach to model selection, which is why multiple classes exist.
Ultimately, the best way to select a model is to understand the basics of each class and to
understand your use case in depth — which means building, maintaining, and deploying strong
evaluations, and revisiting the choice when the workload, the volume, or the lineup moves.

## Source

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
by Michael Segner — published July 24, 2026.
