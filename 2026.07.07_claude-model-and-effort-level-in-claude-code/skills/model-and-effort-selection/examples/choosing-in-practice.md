# Choosing in practice

Each scenario maps a symptom to the setting to change. The underlying question is always the same:

> Did Claude not know enough, or did it not try hard enough?

And before either: **was the context right?**

---

## Before you touch a dial

| Check | If the answer is no |
|---|---|
| Is the prompt specific enough about what "done" looks like? | Fix the prompt, not the dial |
| Is Claude connected to the right tools? | Connect them |
| Is it equipped with the right skills? | Add the skill |
| Does `CLAUDE.md` say what this repo expects? | Write it down there |

If you're increasing effort on a task that shouldn't need it, the fix is often upstream.

---

## Scenario 1 — It edited the code but never ran the tests

**Symptom.** The change looks reasonable; the test suite would have caught that it isn't. Claude
came back without running it.

**Diagnosis.** Didn't try hard enough.

**Move.** Raise the effort level. This is most relevant if you had set effort *below* the model's
default — at lower effort Claude would rather come back to you than spend tokens verifying on its
own.

---

## Scenario 2 — It bailed on a refactor partway through

**Symptom.** Half the call sites updated, then a summary asking how you'd like to proceed.

**Diagnosis.** Didn't try hard enough. How far Claude pushes through a multi-step task before
checking in with you is exactly what effort controls.

**Move.** Raise effort.

---

## Scenario 3 — It called an API that doesn't exist

**Symptom.** Confident, idiomatic-looking code against a library, and the method isn't real.

**Diagnosis.** First, check whether the docs were actually in context. If the library didn't exist
when the model was trained, it isn't in the weights — but putting the real docs in front of Claude
is steering, and steering works well.

If the docs *were* there and it still produced the wrong call, that's the weights producing a
plausible-looking sequence: didn't know enough.

**Move.** Pick a larger model.

---

## Scenario 4 — A subtle bug in an unfamiliar domain

**Symptom.** Every explanation Claude offers is coherent and wrong, across several attempts, with
all the relevant code in context.

**Diagnosis.** Didn't know enough. A larger model is helpful exactly where the smaller model is
confidently wrong no matter how much context you give it.

**Move.** Pick a larger model. If the problem is one nothing else has cracked, this is the case
for Fable — long, multi-step work is where it pulls furthest ahead.

---

## Scenario 5 — A precisely describable mechanical change

**Symptom.** Nothing is wrong. You're renaming a symbol across a package, and the relevant code is
already in context.

**Diagnosis.** Routine work. There's no reason to pay for capability the task doesn't need, and
specific instructions directing execution are a better recipe for success on smaller models
anyway.

**Move.** Drop to a smaller model. Speed goes up, cost typically goes down, quality doesn't move.

---

## Scenario 6 — An ambiguous request

**Symptom.** "Make the settings page less confusing." There is no single right answer, and the
shape of the solution is part of the work.

**Diagnosis.** Larger models are better at handling ambiguity; smaller models do better when given
specific instructions directing execution.

**Move.** Either move up, or resolve the ambiguity yourself and stay where you are.

---

## Scenario 7 — Responses are longer than you want

**Symptom.** The work is correct but verbose, and you'd rather it wrapped up sooner.

**Diagnosis.** Effort shapes token consumption but doesn't limit it. `max_tokens` is the only hard
cap, and it truncates mid-stream — a blunt instrument, mostly relevant to API developers.

**Move.** Use softer controls: a task budget, or asking Claude to keep it brief in your prompt.
These are guidance the model is trained to follow; it will look to conclude its task as it nears
the limit rather than running into a wall.

---

## Setting a standing preference

Effort is best chosen as a **general preference** based on your domain or the type of work you do,
not task by task. Most of the time you shouldn't be thinking about either setting: start with the
model's default effort, and reach for the dials only when a result misses the mark.

## Source

["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
