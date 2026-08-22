# Worked model-selection scenarios

Each scenario runs the four questions from
[../references/selection-questions.md](../references/selection-questions.md), then names the class
and the next step. Every choice is provisional until an eval confirms it.

---

## 1. A previously unsolved research-style task, low volume

**Shape.** Long-running, many steps, no reliable existing tool handles it today. A handful of runs
per week.

| Question | Answer |
|---|---|
| How hard? | Very — multi-step, long-running, previously unsolved. |
| Latency? | No human waiting in real time. |
| Access? | Check whether Mythos is in scope (Project Glasswing) or whether Fable is the ceiling. |
| Unit economics? | Volume is low, so per-task price barely binds. |

**Choice.** The most capable class available — the Mythos/Fable class is described as especially
capable at exactly this shape: coding, long-running agent tasks, and problems AI has not reliably
handled before.

**Next step.** Start at the default effort, then dial effort *down* while an eval holds the quality
bar. Do not drop a class first.

---

## 2. A customer-facing support assistant, thousands of sessions an hour

**Shape.** High-frequency, customer-facing, a person is waiting on every response.

| Question | Answer |
|---|---|
| How hard? | Individually moderate; the difficulty is in volume and consistency, not depth. |
| Latency? | Binding. This is the canonical high-frequency customer-facing workload. |
| Access? | Widely available classes only — this must be deployable to every role that touches support. |
| Unit economics? | Binding. Per-task price multiplies by a very large number. |

**Choice.** Sonnet — "if the model is involved in high-frequency customer facing workloads, then
Sonnet is often the best choice."

**Next step.** Build a custom eval from real production tickets, including the ones your current
tooling handles badly, before committing.

---

## 3. A high-volume classification or extraction step inside a pipeline

**Shape.** Narrow, precisely describable, repeated identically at very high volume.

| Question | Answer |
|---|---|
| How hard? | Low — single-step, well-specified. |
| Latency? | Binding — it sits in the hot path of a larger pipeline. |
| Access? | No constraint. |
| Unit economics? | Strongly binding — the volume is the whole cost story. |

**Choice.** Haiku — the lowest cost and fastest class, designed for high-frequency workloads where
latency and cost matter.

**Next step.** Confirm with an evaluation that the task is "completed satisfactorily" at that class.
Higher volumes suit lower classes *particularly if evaluations show that*, so the eval is the
condition, not a formality.

---

## 4. Sub-agents inside a multi-agent orchestration

**Shape.** One orchestrator decomposes work; many sub-agents execute pieces in parallel.

**Choice.** Sonnet is explicitly called out as suited to **high-volume sub-agents in multi-agent
orchestration setups**. Keep the orchestrator on a higher class when the planning and decomposition
is the genuinely hard part of the system.

**Next step.** This is structurally adjacent to the advisor strategy — see
[../references/advisor-strategy.md](../references/advisor-strategy.md). If the sub-agents are
producing plans that go wrong, add an advisor rather than upgrading every sub-agent.

---

## 5. Opus clears the bar, but Fable is tempting

**Shape.** Reasoning-intensive enterprise work. Opus benchmarks close to Fable. Someone wants to
"just use the best."

**Choice.** Apply the rule of thumb directly:

- Evals or internal testing show Opus **struggling** on some tasks → **Fable**.
- Opus **already clears** the quality bar → its speed and price profile may make it the better
  choice.

**Why the benchmarks do not settle it.** Similar benchmark scores hide a real difference: larger
models such as Fable tend to have more wisdom, creativity, and writing skills in real-world
situations. If your work leans on those qualities, benchmark parity is not parity — and if the
benchmark is saturated, it was never discriminating in the first place.

---

## 6. Cost pressure on a workload running entirely on the top class

**Shape.** Quality is good, finance wants the bill down.

**Do not** drop a class as the first move. Two cheaper options come first:

1. **Lower the effort level on the same class.** Higher-class models at lower efforts can sometimes
   be more efficient than smaller models outright.
2. **Split into worker + advisor.** On SWE-bench Pro, Sonnet 5 with a Fable 5 advisor is within 10%
   of Fable 5's score at 63% of the price of using Fable 5 for the whole task.

**Next step.** Measure all three configurations — worker alone, advisor class alone, worker +
advisor — on the same eval set, reporting score *and* price for each.

---

## 7. You genuinely cannot tell whether it is the model or your setup

**Shape.** A workload fails intermittently and nobody can say why.

**Choice.** Move *up*, temporarily. Starting with a smaller model makes it harder to distinguish
between model failures and setup failures. Run on the most intelligent class available; if the
failures persist there, they are setup failures — prompt, tools, context, task scoping — and no
model change will fix them.

**Next step.** Once the setup is clean, walk the class back down under eval until you find the fit.

## Source

["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)
by Michael Segner — published July 24, 2026.
