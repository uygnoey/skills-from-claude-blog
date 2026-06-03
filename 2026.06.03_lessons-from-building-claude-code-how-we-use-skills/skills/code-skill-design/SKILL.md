---
name: code-skill-design
description: Use this skill when you are writing, reviewing, or refactoring Claude Code skills and want proven structure, content patterns (Gotchas, references, scripts, templates), and distribution guidance.
---

# Claude Code skill design playbook

## Instructions

### What a skill is (and why structure matters)
A skill is a **folder** of instructions and supporting resources, not just a single markdown file. Use the file system for progressive disclosure so the agent reads the right level of detail at the right time.

### Keep a skill in one category
Skills that fit cleanly into a single category tend to work best; avoid mixing multiple categories in one skill.

See the category reference:
- `references/skill_categories.md`

### Write the description for the model
Treat the `description` field as trigger text (when to use the skill), not as a human-oriented summary.

### Make “Gotchas” the highest-signal section
Capture real failure cases and footguns Claude hits in your environment, and update over time.

### Use progressive disclosure (files, not one long document)
Split long details into companion files:
- API/CLI references → `references/*.md`
- Setup/config → `templates/config.json`
- Output templates to copy → `templates/*`

### When scripts help, ship scripts
If a step can be made deterministic (validation, formatting, generating boilerplate), include scripts in the skill folder.

### Use on-demand hooks
If a hook is too disruptive to be always-on, activate it only when the skill triggers for the session.

## Examples
- Use `templates/config.json` as a starting point when a skill requires per-user setup.

## Source
- https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
