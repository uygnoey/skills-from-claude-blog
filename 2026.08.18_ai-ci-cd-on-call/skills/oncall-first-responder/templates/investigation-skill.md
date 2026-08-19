# Investigation skill skeleton — `<bug-class>`

One of these per bug class. It encodes the steps a human actually takes for that class of failure, so orchestrator and executor agents are guided rather than searching blind.

## How to build it — do not write this from memory

1. Wait for a real incident of this class.
2. Troubleshoot it turn-by-turn with the agent, narrating what you check and why.
3. At the end, have the agent write this file from that session.
4. Correct it during the next incident of the same class.

A thorough investigation skill for a single bug class can run to several hundred lines. That length is a feature: it captures the steps an experienced engineer performs without noticing, which are exactly the ones an agent otherwise skips.

---

## Skeleton

```markdown
---
name: investigate-<bug-class>
description: Investigate <bug class> incidents in <system>. Use when <symptom pattern> appears in <channel or dashboard>.
---

# Investigating <bug class>

## Recognising this class

- Signature symptoms: <...>
- Signals that look similar but are a different class: <..., and which skill to use instead>

## Step 0 — read the lessons log

Start from what has happened recently. Note any entry from the last <N> weeks whose bug class matches.

## Step 1 — establish what actually changed

- Deploys in the window: <where to look, exact query>
- Feature flag changes in the window: <where to look>
- Configuration changes in the window: <where to look>
- Dependency incidents in the window: <where to look>

## Step 2 — confirm the symptom with data

<Exact queries, dashboards, and what a healthy baseline looks like. Include the numbers, not just the dashboard name.>

## Step 3 — narrow to a component

<Decision points. For each: the question, the query that answers it, and where each answer leads.>

## Step 4 — form and test the hypothesis

<How to falsify, not just confirm. What evidence would rule this out?>

## Step 5 — assess blast radius and safe mitigations

<Who is affected, what mitigations exist, which are reversible, which need approval and from whom.>

## Step 6 — verify after the fix

<The specific signal that must return to baseline, and how long to watch it.>

## Reference material

- <link to per-symptom reference file>
- <link to architecture notes for the affected system>

## Known dead ends

- <thing that looks causal and is not, and why>
```

## Source

- https://claude.com/blog/ai-ci-cd-on-call
