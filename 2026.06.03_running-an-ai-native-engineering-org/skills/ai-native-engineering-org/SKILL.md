---
name: ai-native-engineering-org
description: Practices for adapting engineering planning, context sharing, code review, and team operating norms once agentic coding becomes the default.
---

## Instructions

Use this skill to audit and redesign engineering workflows when agentic coding dramatically increases code output and shifts bottlenecks toward verification, review, and safety.

1) Identify the workflow you want to change
- Choose the “noisiest” workflow (high friction, slow, or frequently discussed).

2) Evaluate whether it still serves its purpose
- Be explicit about the purpose and what signals success.

3) Decide: keep, automate, or drop
- If it still matters, ask whether the step can be automated (partially or fully).
- If it no longer matters, remove it.

4) Apply the post’s operating changes
- Planning: move from long-range roadmaps to just-in-time planning; prefer PR discussions and prototypes.
- Context gathering: ask Claude first; only then ask humans if needed; consider automation.
- Code review: let Claude handle style/lint, tests, and obvious bugs; reserve human review for trust boundaries, security-sensitive code, legal risk, and product taste.
- Team structure: expect role boundaries to blur; keep teams flat; dogfood the product; kill processes that stop working.

5) Roll out new norms
- Define a small set of non-negotiable principles.
- Let pods adapt the details for their local workflows.

6) Track whether changes stick
- Track onboarding ramp time, PR cycle time, and whether commits are Claude-assisted.

## Examples

- Workflow evaluation questions: [templates/workflow-evaluation-questions.md](./templates/workflow-evaluation-questions.md)
- “Before / after” communication table: [templates/before-after-table.md](./templates/before-after-table.md)
- Non-negotiable principles checklist: [templates/non-negotiable-principles.md](./templates/non-negotiable-principles.md)
