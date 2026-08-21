# Wrapper (chained) skill template

Chaining is how you add verification to a skill you cannot modify — a built-in skill, or a
plugin-managed skill that gets overwritten on update. Build a custom wrapper skill that invokes
the original, then invokes your verification skill.

```markdown
# .claude/skills/safe-refactor/SKILL.md
Run /simplify on the current diff first.
When /simplify finishes, invoke /verify-no-public-api-changes.
```

## Generalized shape

```markdown
---
name: <wrapper-name>
description: <What the combined flow does.> Use when <the situation>.
---
Run /<producing-skill> on <the target> first.
When /<producing-skill> finishes, invoke /<verification-skill>.
```

## An end-to-end chain

Members of Anthropic's Claude Code team run this chain day to day:

1. `/code-review` — hunts for bugs.
2. `/simplify` — cleans up the diff.
3. `/verify` — confirms end-to-end behavior.
4. `/design` — a custom skill that checks against guidelines in a `DESIGN.md` file, if the change
   touched UI.

What started as a habit ("I always run `/verify` after `/simplify`") becomes a contract
("`/simplify` always runs `/verify` when it finishes"). The chain runs the whole dev cycle on its
own; you only step in when something escalates back to you.

## When not to chain

- The steps are independent enough that you sometimes want to run one without the others —
  chaining trades flexibility for automation.
- You have not tested the chain yet. Chained verification loops can increase token spend, so test
  before deploying broadly.

## Source

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
