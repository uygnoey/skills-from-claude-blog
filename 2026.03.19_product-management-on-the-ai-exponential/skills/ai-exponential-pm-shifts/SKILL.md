---
name: ai-exponential-pm-shifts
description: A practical workflow guide for product teams operating under rapid model capability gains: short sprint exploration, demo/eval-driven discovery, revisiting features, and favoring simple implementations.
---

## Instructions

Use this workflow when model capability is improving quickly and you want your product process to keep up.

1) **Plan in short sprints (run side quests)**
   - Encourage short, self-directed experiments outside the main roadmap.
   - Treat an afternoon prototype or capability test as a first-class output.

2) **Prefer demos and evals over docs**
   - Build a rough prototype early to make the conversation concrete.
   - Create lightweight evals to measure whether the feature works and where it fails.

3) **Revisit features with new models**
   - Be a daily active user and deliberately test tasks you assumed were too hard.
   - If users are stitching together manual workflows, treat that as scaffolding to productize.

4) **Do the simple thing that works**
   - Avoid clever workarounds that only exist to compensate for current model limits.
   - Favor simple implementations that become easier to upgrade as models improve.

5) **Optimize for capability first**
   - Don’t cut token usage too early; first confirm the feature is possible and valuable.

## Examples

### Example: Turn a written spec into a prototype

Use the template below as a starting point:

- `templates/spec-to-prototype.md`

### Example: Create a small eval set for a risky feature

Start with:

- `examples/lightweight-eval-starter.md`

### Example: Daily active testing prompt

“Try doing the thing we assumed was too hard. If it works, suggest how we should productize the manual steps users are doing today.”

## Source

- Blog post: https://claude.com/blog/product-management-on-the-ai-exponential

