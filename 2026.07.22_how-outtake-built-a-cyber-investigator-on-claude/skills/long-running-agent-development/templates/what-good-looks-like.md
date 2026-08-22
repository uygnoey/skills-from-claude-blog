# "What does good look like?" — the definition that gates every iteration

Fill this in **before** writing agent code, and keep it fixed across iterations so
every change is measured against the same standard.

> "The most important thing about building long running agents is that you really
> have to understand *what does good look like? What is the agent supposed to be
> doing?*" — Jack Hayford, engineering lead, Outtake

---

## 0. Did you run the task yourself?

- [ ] I have personally completed this task end to end, at least once
- [ ] I have extracted domain expertise from customers and/or design partners
- Date completed: `<date>`
- What surprised me about doing it manually: `<note>`

If both boxes are unchecked, stop here. Everything below will be a guess.

---

## 1. What is the agent supposed to be doing?

One paragraph, in the language a practitioner would use. Not the implementation —
the job.

```
<job description>
```

---

## 2. What does a good result look like?

| Dimension | Good | Not good | How it is observed |
| --- | --- | --- | --- |
| `<e.g. completeness>` | | | |
| `<e.g. accuracy>` | | | |
| `<e.g. the artifact produced>` | | | |

"How it is observed" is the column that becomes an eval. If you cannot fill it,
that dimension is not gradeable yet and you will end up reviewing transcripts by
hand.

---

## 3. What must always happen?

These become **hardcoded guardrails at the orchestration layer**, not prompt
lines. Sorting rule: if you would file a bug when the agent violates it, it
belongs here.

| Requirement | Enforced by | Failure mode if it drifts |
| --- | --- | --- |
| `<always X>` | `<harness / orchestration step>` | |

---

## 4. Where does the agent need improvisation space?

The judgment calls. Do not constrain these — improvisation space is where the
best results come from.

| Decision point | Why it needs judgment |
| --- | --- |
| `<decision>` | |

---

## 5. What is the simplest version that works?

Complexity must be earned. Name the smallest thing that produces a good result,
and what evidence would justify each addition.

- Simplest working version: `<description>`
- First complexity to add, and the result that would justify it: `<description>`

---

## 6. Session profile

| Measure | Expected |
| --- | --- |
| Median runtime | |
| Routine upper range | |
| Worst case | |

If the worst case is long enough that context will be compacted mid-task, assume
prompts will be ignored and plan the guardrails in section 3 accordingly.

---

## 7. First evals

Imperfect and early beats rigorous and later.

| Check | Grades which dimension from §2 | Pass criterion |
| --- | --- | --- |
| `<check>` | | |

## Source

[How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) — Michael Segner, July 22, 2026
