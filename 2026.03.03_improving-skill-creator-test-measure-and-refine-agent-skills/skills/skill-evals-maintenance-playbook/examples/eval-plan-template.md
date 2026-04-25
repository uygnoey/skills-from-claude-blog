# Eval plan template

Use this as a lightweight structure for defining evals for a skill.

## 1) Purpose

- What behavior should this skill reliably produce?
- What failure modes are you trying to prevent?

## 2) Skill type

- Capability uplift / Encoded preference (see ../references/skill-types.md)

## 3) Eval cases

For each eval case:

- **Prompt**: (paste the exact prompt)
- **Files**: (list any required files and how to provide them)
- **What good looks like**:
  - Required elements
  - Forbidden elements
  - Quality bar

## 4) Regression cadence

- When will you rerun evals? (e.g., after model upgrades, weekly, before release)

## 5) Metrics to record

- Pass/fail per case
- Notes on failure modes
- Elapsed time
- Token usage

## Source

- https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
