---
name: managed-agent-orchestration
description: Create better Claude Managed Agents runs by defining outcomes rubrics, clarifying multiagent roles (lead/specialist/grader), and using a lightweight dreaming review checklist.
---

## Instructions

Use this skill when you are setting up or iterating on Claude Managed Agents that use memory, outcomes (rubric + grader), multiagent orchestration (lead + specialists), and/or webhooks.

1) **Define the run goal and constraints**
- Write a short success statement (1–3 sentences).
- List non-goals and constraints (latency, cost, safety, data access).

2) **Write an outcomes rubric**
- Use the rubric template in `templates/outcomes-rubric.md`.
- Keep criteria testable: each criterion should be answerable with Yes/No or a small ordinal scale.
- Add “failure modes” that the grader should look for.

3) **Plan multiagent orchestration**
- Identify whether you need a **lead agent** and which **specialist agents** are required.
- Keep specialists narrow and tool-focused; avoid overlapping scopes.
- Use the role glossary in `references/role-glossary.md` to keep terminology consistent.

4) **Add a dreaming/memory review loop**
- After runs, review what the agent learned and what it missed.
- Use `references/dreaming-review-checklist.md` to capture recurring mistakes, preferred workflows, and user-specific preferences.

5) **Integrate webhooks (if needed)**
- If your product needs async completion notifications, add a webhook for “outcome done” events.
- Treat webhook delivery as best-effort and design idempotent handlers.

## Examples

### Example: outcomes rubric skeleton
See `templates/outcomes-rubric.md`.

### Example: role mapping
See `references/role-glossary.md`.

### Example: dreaming review checklist
See `references/dreaming-review-checklist.md`.

## Source
- https://claude.com/blog/new-in-claude-managed-agents
