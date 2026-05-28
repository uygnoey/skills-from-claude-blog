---
name: agent-orchestration-planning-layer
description: Add a structured planning-orchestration layer before code generation to make outcomes, assumptions, edge cases, and validation criteria explicit, producing a reviewable PRD-style plan.
---

## Instructions
Use this skill to create a reviewable planning artifact (a “collaborative PRD”) *before* any code generation.

1. Restate the goal as an outcome (what changes in the world) and how success is measured.
2. List all assumptions that are currently implicit.
3. Enumerate workflows and edge cases that are easy to forget.
4. Define how you will verify the output matches intent before rollout.
5. Produce a structured plan the team can review.

Use the bundled template to drive the planning pass, then output the collaborative PRD.

### Bundled resources
- Prompt template: [templates/planning-layer-prompt.md](./templates/planning-layer-prompt.md)
- PRD outline example: [examples/collaborative-prd-outline.md](./examples/collaborative-prd-outline.md)

## Examples
- Take a vague request (“Add SSO”) and produce a collaborative PRD capturing success metrics, assumptions (IdP support), key flows (login, account linking), edge cases (invited users), and validation checks.
- Before generating code for a refactor, produce a plan clarifying constraints (no behavior changes), assumptions (test coverage), and how you will confirm the result (golden tests, diff checks).
