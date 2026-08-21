---
name: model-and-effort-selection
description: Decide which model and which effort level to use in Claude Code, and diagnose which of the two to change when a result misses the mark. Use when a session produced a wrong or shallow answer and the instinct is to reach for a dial, when setting a team default for a kind of work, or when deciding whether a routine stretch of work can drop to a smaller model. The core diagnostic is "did it not know enough, or did it not try hard enough?" — not knowing enough points at the model, not trying hard enough points at effort, and both point upstream at context first.
---

# Choosing a model and an effort level

Claude Code gives you two settings that appear to "make the answer better": the **model** and the
**effort level**. They do different things.

- **Model** selects which set of frozen weights handles your request — the overall capability
  range, and what each output token costs.
- **Effort** controls how much work Claude does on your request overall: how long it thinks, how
  many files it reads, how much it verifies, and how far it pushes through a multi-step task
  before checking in with you.

Effort is not just "thinking time." At higher effort Claude takes more of those actions — read
files, run tests, double-check — before coming back to you. At lower effort it would rather ask
you for more context than spend tokens figuring something out on its own.

## Instructions

### 1. Start with the defaults

For most tasks, use the model's **default effort level**. The default is the level where Claude
scales its token usage according to what most people would want to spend on a task.

Treat effort as a **manual override** to scale how hard and long Claude works. Choose it
deliberately when you have a strong preference for thoroughness or speed based on your domain or
the type of work you do — as a **general preference**, not a task-by-task decision.

### 2. When a result misses the mark, check context before touching a dial

Your first instinct should not be to adjust a knob. Examine the context you provided:

- Is the prompt too vague?
- Is Claude connected to the right tools?
- Is it equipped with the right skills?

If you find yourself raising effort on a task that shouldn't need it, the fix is usually
upstream — in your context, your `CLAUDE.md`, or how the task is scoped.

### 3. Then ask the diagnostic question

Assuming context was clear and Claude still got it wrong:

> **Did it not try hard enough, or did it not know enough?**

| Symptom | Cause | Change |
|---|---|---|
| Skipped a file, didn't run the tests, bailed on a refactor partway through | Didn't try hard enough | **Raise effort** — most relevant if you had set effort below the model's default |
| Had all the pertinent context, clearly tried, and was still confidently wrong | Didn't know enough | **Pick a larger model** |

Use this to pick a starting point, not as a hard rule.

### 4. Pick the model by the shape of the work

**Larger model** when the problem is genuinely hard: subtle bugs, unfamiliar domains,
architecture decisions — situations where a smaller model is confidently wrong no matter how much
context you give it. Larger models are also better at handling **ambiguity**.

**Smaller model** when the work is routine: edits you can describe precisely, mechanical changes,
questions about code already in context. There's no reason to pay for capability the task doesn't
need. Specific instructions directing execution are a better recipe for success on smaller models.

If you're on the larger model and the work has been routine for a while, dropping down increases
speed and typically reduces cost without affecting output quality.

### 5. Use the specialist / expert / generalist framing

See [references/model-tiers.md](references/model-tiers.md) for the full analogy.

- **Fable** is a specialist who's seen problems almost no one else has.
- **Opus** is the expert.
- **Sonnet** is a really good generalist.

The effort level decides how much time any of them spends on your task. *Opus at low effort* is
five minutes with an expert who brings knowledge that isn't anywhere in your codebase — but only
a quick read of your code. *Sonnet at high effort* is a really good generalist with the whole
afternoon: reads everything, runs things, double-checks, ends up understanding your specific code
thoroughly, with less of the "I've seen exactly this before" recognition.

None is universally better. **Model is roughly how capable; effort is roughly how thorough.** Most
real tasks need some of both.

### 6. Reason about cost by task shape, not per-token price

Full treatment: [references/cost-and-tokens.md](references/cost-and-tokens.md).

- **Routine work, same effort:** both models generally get it right. The larger model consumes
  more tokens on extra verification at a higher per-token price — so dropping to the smaller model
  for routine stretches saves real money at no quality cost.
- **Harder, multi-step work:** the smaller model grinds toward the limit of its ability, burning
  iterations, while the larger model reaches the same quality bar in fewer steps. Total cost per
  task can come out *lower* on the larger model — and more importantly, the larger model can
  accomplish tasks the smaller one cannot at any effort setting.
- **Effort shapes token consumption but does not limit it.** The only hard cap is `max_tokens`,
  which truncates a response mid-stream — a blunt instrument, mostly relevant to API developers.
  Softer controls (task budgets, asking Claude to keep it brief) are guidance the model is trained
  to follow: it will look to conclude its task as it nears the limit, rather than hitting a wall.

### 7. Know what is actually happening underneath

Two references explain the mechanics, so the settings stop feeling like magic:

- [references/how-inference-works.md](references/how-inference-works.md) — tokenization, frozen
  weights, and the one-token-at-a-time generation loop. Why steering with context is not teaching,
  and why a hallucination is the weights producing a plausible-looking sequence, not a failed
  lookup.
- [references/effort-mechanics.md](references/effort-mechanics.md) — how the effort level is sent
  with the request, why thinking tokens are ordinary output tokens, and why Claude revises its
  plan mid-run instead of executing every planned step.

## Examples

Worked scenarios, each mapping a symptom to the setting to change:
[examples/choosing-in-practice.md](examples/choosing-in-practice.md).

### Claude skipped the tests

It made the change but never ran the suite, and the change was wrong in a way the suite would have
caught. That's "didn't try hard enough" — **raise effort**, especially if you had lowered it below
the model's default.

### Claude was confidently wrong about an unfamiliar framework

It had the files, it clearly worked the problem, and it still produced an API call that doesn't
exist. First check whether the docs were actually in context; putting real docs in front of Claude
is steering and it works well. If the context was there and it still failed, that's "didn't know
enough" — **pick a larger model**.

### A long mechanical rename across a package

Precisely describable, no ambiguity, all the relevant code already in context. **Drop to a smaller
model.** There's no reason to pay for capability the task doesn't need.

### A multi-day refactor nothing else has finished

Long, multi-step work is where Fable pulls furthest ahead — in Anthropic's testing it finished
jobs Opus and Sonnet couldn't reach at any effort level. It also costs the most per token, which
is the other reason to save it for the work that needs it.

## Source

["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
by Lydia Hallie, member of technical staff on the Claude Code team — published July 7, 2026.
