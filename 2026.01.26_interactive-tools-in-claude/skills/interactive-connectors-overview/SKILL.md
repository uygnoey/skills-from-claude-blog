---
name: interactive-connectors-overview
description: Turn a connector feature announcement (like MCP Apps interactive connectors) into a practical evaluation and rollout checklist your team can reuse.
---

## Instructions
Use this skill to translate a product announcement about interactive connectors into a repeatable plan your team can apply across tools.

1) Identify the connector’s interactive surface
- What UI is rendered in-chat (preview, editor, chart, diagram, timeline)?
- What actions can be executed from the UI?

2) Define “preview-before-action” guardrails
- Require a human review step for irreversible actions (posting, sending, deleting).
- Decide what “approval” means (explicit confirmation message vs. UI submit).

3) Map the interaction loop
- What parameters can the user adjust in-place?
- What is the success signal shown in the UI?

4) Establish adoption criteria
- Prefer interactive connectors when there’s meaningful risk, formatting nuance, or parameter tuning.
- Prefer non-interactive tool calls for simple, low-risk actions.

5) Rollout checklist
- Pilot with 1–2 workflows.
- Collect feedback on trust, speed, and error rates.
- Document best-practice prompts and edge cases.

## Examples
- “We want to draft Slack messages but always review formatting before posting. Create a rollout plan that requires preview + explicit confirmation.”
- “List which of our top 5 workflows would benefit most from interactive connectors and why.”

## Source
- https://claude.com/blog/interactive-tools-in-claude
