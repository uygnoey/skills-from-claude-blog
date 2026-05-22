---
name: finance-narrative-integrity-layer
description: Keep finance narratives (board decks, monthly reviews) coherent as numbers refresh by using Claude as an integrity layer for reconciliation, consistency checks, and first-pass variance commentary.
---

## Purpose
Use Claude to maintain a single coherent story behind financial numbers as inputs change, by (1) reconciling narrative claims to a source of truth, (2) reviewing the narrative like a board reader, and (3) drafting recurring variance commentary in an established voice.

## When to use
- You ship a board deck where numbers refresh up to the last minute and multiple stakeholders edit in parallel.
- You publish a monthly financial review that must keep consistent voice and conventions month over month.
- You inherit or open a model you don’t fully understand and want an initial driver/structure sanity check.

## Inputs
- A board deck or narrative doc (slides or document).
- A single source of truth for the numbers (model output tables, dashboards, or approved extracts).
- Prior-month commentary (for voice/convention consistency).

## Instructions
### 1) Reconcile claims to a single source of truth
1. Provide Claude the narrative document/deck and the latest source-of-truth tables.
2. Use the reconciliation prompt template: [templates/reconcile-claims.md](./templates/reconcile-claims.md)
3. Apply fixes in the narrative and rerun whenever numbers move.

### 2) Read the narrative like a board member
1. Use the board-reader prompt template: [templates/board-reader-review.md](./templates/board-reader-review.md)
2. Resolve contradictions, missing context, and places where the narrative assumes internal knowledge.

### 3) Draft first-pass variance commentary in an established voice
1. Provide the month’s table and prior-month commentary.
2. Use the variance draft template: [templates/variance-commentary-first-pass.md](./templates/variance-commentary-first-pass.md)
3. Edit the output for judgment, nuance, and stakeholder alignment.

### 4) Separate projects by audience (memory hygiene)
- Keep separate Claude projects for distinct audiences (e.g., board deck vs. monthly review) so tone and conventions remain stable.
- Commit important documents to project memory.

### 5) Extract decisions from long cross-functional threads
- When a long thread produces a key conclusion, ask Claude to extract the conclusion and reasoning and store it where you will reuse it.

## Examples
- Board deck workflow (checklist): [examples/board-deck-checklist.md](./examples/board-deck-checklist.md)
- Monthly review workflow (checklist): [examples/monthly-review-checklist.md](./examples/monthly-review-checklist.md)
- New model first-look prompts: [examples/new-model-first-look.md](./examples/new-model-first-look.md)

## Source
This skill is derived from: https://claude.com/blog/how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers
