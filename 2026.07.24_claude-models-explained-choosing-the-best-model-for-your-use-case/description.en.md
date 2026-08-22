**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Michael Segner answers the question Anthropic hears most often — "what model should I choose for this workload?" — with a default recommendation and a procedure. The default: start with the most intelligent generally available model and use effort level to dial in performance and cost, because cost-per-task is often lower on more capable models even when price-per-token is higher, and because starting small makes it hard to tell a model failure from a setup failure.

The procedure is four questions (how hard, how fast, what can you access, what does volume cost), a walk through the four model classes and what each is actually for, the advisor strategy for splitting a task across two classes, and the reason evals rather than benchmarks have to make the final call. The framing throughout: model classes don't specialize by domain — there is no finance model and no science model — so selection is about how hard a problem a class can reliably carry, and what that capability costs in price and speed.

## When is it useful?
- When picking a model class for a new production workload and wanting a defensible starting point rather than a guess.
- When a workload is under cost pressure and someone proposes dropping a class.
- When choosing between Opus and Fable, whose benchmark scores look close.
- When a latency-sensitive, customer-facing feature needs a class chosen for it.
- When a benchmark says two models are tied and you need something better to decide with.
- When a workload fails intermittently and nobody can say whether the model or the setup is at fault.

## Key points
- **Start smart, then dial down.** The default is the most intelligent generally available model plus effort level tuning. Starting on a smaller class blurs the diagnosis between model failure and setup failure.
- **Price-per-token is not price-per-task.** More capable models often take fewer turns and less thinking time, so cost-per-task can be lower despite a higher token price — especially at lower effort levels.
- **No domain specialists.** Every Claude model is trained to excel at coding, agentic tasks, and knowledge work. Classes differ in how hard a problem they carry reliably, not in what field they know.
- **Mythos and Fable are one model in two packages.** Mythos for trusted organizations handling dual-use cybersecurity and biology work; Fable with additional safeguards for general public use. Both require limited data retention.
- **The Opus/Fable rule of thumb.** If evals show Opus struggling on some tasks, Fable is the answer. If Opus already clears the bar, its speed and price profile may make it better. Larger models tend to have more wisdom, creativity, and writing skill at similar benchmark scores.
- **Sonnet's two homes.** High-frequency customer-facing workloads, and high-volume sub-agents in multi-agent orchestration.
- **Effort is a second axis, not a redundant one.** Higher class at higher effort is the performance ceiling; higher class at *lower* effort is sometimes more efficient than a smaller class outright.
- **The advisor strategy.** A faster worker model calls a more intelligent model to check its plan and evaluate its work — coached only when needed. On SWE-bench Pro, Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5's score at 63% of the price.
- **Benchmarks saturate.** Opus and Fable solve nearly everything on standard tests, so the benchmark stops discriminating exactly where you need it to. Directional guidance only.
- **Custom evals are the deciding instrument.** A curated set of production problems, including the hard ones your current tools fail, with success criteria your team defines. Building, maintaining, and deploying them is the actual work of model selection.

## Bundled resources
- `skills/model-class-selection/SKILL.md` — the selection procedure: start smart, the four questions, the effort dial, the advisor option, decide with evals.
- `skills/model-class-selection/references/model-classes.md` — the four classes in full, the Mythos/Fable packaging split, and the Opus-vs-Fable rule of thumb.
- `skills/model-class-selection/references/selection-questions.md` — the four questions with follow-ups, and why price-per-token and price-per-task can point opposite ways.
- `skills/model-class-selection/references/advisor-strategy.md` — the worker/advisor split, the SWE-bench Pro result, and what to measure before adopting it.
- `skills/model-class-selection/references/evals-and-benchmarks.md` — benchmark saturation, the named benchmarks, and what a custom eval must contain.
- `skills/model-class-selection/examples/selection-scenarios.md` — seven worked scenarios from research tasks to high-volume extraction.
- `agents/task-executor.md` — the worker role: plan, get the plan checked, execute, get the work evaluated.
- `agents/plan-advisor.md` — the advisor role: review plans for ordering and unverified assumptions, review outputs against stated criteria, and stay out of execution.
- `guides/choosing-a-claude-model.{en,ko,es,ja}.md` — the full guide in four languages.

## Source
["Claude models explained: choosing the best model for your use case"](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case) by Michael Segner — published July 24, 2026.
