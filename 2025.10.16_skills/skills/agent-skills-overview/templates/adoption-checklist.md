# Agent Skills adoption checklist

Use this checklist to plan and roll out a skill.

## 1) Scope
- Define the single workflow you want to make more consistent.
- List required inputs and expected outputs.
- Identify any steps that must be deterministic (candidates for scripts).

## 2) Bundle design
- Keep `SKILL.md` short; move detailed material into companion files.
- Add reusable prompts/instructions as templates.
- Add long references (glossaries, schemas, standards) under `references/`.

## 3) Safety
- Use trusted sources, especially if the skill includes executable code.
- Document what each script does and what it can access.

## 4) Installation & sharing
- Choose a distribution method:
  - version control for team sharing
  - plugin distribution (Claude Code)
  - organization-wide enablement (Claude apps)

## 5) Iteration
- Start with one team/user group.
- Collect failure cases and refine templates and checks.
- Version and roll out updates deliberately.
