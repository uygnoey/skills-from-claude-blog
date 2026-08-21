# Example: embedding a check in a producing skill

The embedded pattern in its simplest form — a one-line append to the producing skill's body. The
check belongs to one specific workflow, and the workflow now runs it without you asking.

```markdown
# .claude/skills/scaffold-component/SKILL.md
---
name: scaffold-component
description: Scaffold a new React component under src/components/, including the component file, its co-located test, and an index export. Use when the user asks to create a new component.
allowed-tools: [Read, Write, Edit, Bash, Glob]
---
# Scaffold a new React component

Given a component name (PascalCase), create the following under `src/components/<Name>/`:

1. `<Name>.tsx`: function component with a typed props interface and a default export.
2. `<Name>.test.tsx`: React Testing Library test that renders the component and asserts it mounts without throwing.
3. `index.ts`: re-export the default and any named exports.

Follow the patterns in `src/components/Button/` as the reference. Match the import alias style (`@/components/...`) used throughout the codebase.

# code continues...

After creating the component file, run eslint on it and
address any errors before reporting completion.
```

## The appended step

The last two lines are the whole embed:

```
After creating the component file, run eslint on it and
address any errors before reporting completion.
```

## Verifying the embed

Invoke the skill on a fresh task and confirm the new step runs as part of the output. If it does
not, the skill's description or earlier instructions are not pulling the appended check in.

## Limits of this pattern

- **Only works on skills you can edit** — ones you wrote yourself, or ones installed at a project
  level where the `SKILL.md` file is under your control. Built-in skills and plugin-managed skills
  (the kind that get overwritten on update) are off-limits; chain instead.
- **Skip embedded for checks that span workflows.** Those want standalone, so you can invoke them
  from any context.

## Source

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
