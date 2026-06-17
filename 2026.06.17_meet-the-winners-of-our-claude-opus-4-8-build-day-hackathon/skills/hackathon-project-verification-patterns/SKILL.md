---
name: hackathon-project-verification-patterns
description: Patterns observed in Build Day projects for planning, verification with independent sub-agents, and cost/latency optimization under tight time constraints.
---

## Instructions

Use these patterns when you need to build a working demo quickly, while still keeping outputs verifiable and costs under control.

1) Plan before building
- Write a lightweight PRD with success criteria.
- Break work into parallel workflows (e.g., data prep, UI, backend, evaluation).

2) Add an evidence chain (when claims must be traceable)
- For each generated component, record where it came from (source document, image, diagram) and why it was placed/derived.

3) Verify with independent sub-agents
- Run verification in isolated context windows so reviewers are not biased by prior steps.
- Use a self-correction loop that rechecks failed components until all tests pass.

4) Optimize expensive simulations
- If you start with per-entity calls (e.g., one call per persona/agent), look for batching or clustering approaches that preserve accuracy.
- Evaluate against real-world baselines (historical outcomes, known distributions, external benchmarks).

5) Use Claude for tool selection, not just code writing
- Ask Claude to research and choose the right model/tool for a specific subtask.
- Hand it unfamiliar technologies and ask it to integrate them into your pipeline.

## Examples

### Example: verification loop with independent reviewers
See [examples/verification-loop.md](./examples/verification-loop.md).

### Example: clustering to reduce inference cost
See [examples/cost-cutting-clustering.md](./examples/cost-cutting-clustering.md).

## Source

- https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon
