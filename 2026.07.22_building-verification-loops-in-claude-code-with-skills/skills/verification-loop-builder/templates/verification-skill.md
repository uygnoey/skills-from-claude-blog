# Verification skill template

Drop this at `.claude/skills/<name>/SKILL.md` inside your project. The simplest possible
verification skill is a few lines of frontmatter plus a body.

```markdown
---
name: verify-<what>
description: <What the check confirms, in one sentence.> Use when <the situation that should
  trigger it — a diff touching a particular area, a workflow finishing, a pre-PR moment>.
allowed-tools: [Read, Edit, Grep]
---
<What to read.> Read the <relevant paths> in the current diff.

<What to confirm.> For each <unit>, confirm it <holds the property> and does not <violate the rule>.

<How to report and fix.> Report each violation with file:line, then fix it: <the correction to make>.
```

## Filling it in

- **`name`** — matches the folder name; lowercase, hyphenated.
- **`description`** — say both *what* the check is and *when* it applies. The "use when" half is
  what pulls the skill in at the right moment.
- **`allowed-tools`** — the minimum the check needs. A read-and-fix check typically needs
  `Read`, `Edit`, `Grep`; a check that runs a command also needs `Bash`.
- **Body** — plain English, the way you would hand the procedure to a new teammate on day one.
  Three moves: what to read, what to confirm, how to report and fix.

## Writing the body

If you are struggling to articulate the check, ask Claude for best practices first and edit from
there. Your version probably differs on a few specific points, and those differences are exactly
what you want to capture.

The check does not have to be qualitative. A deterministic project rule — "reject any migration
that drops a column without a backfill step" — belongs here too: no generic linter will catch it,
but a project-specific one will.

## Faster path

Install the `skill-creator` plugin and let Claude interview you instead of writing the file by hand:

```
/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.
```

## Source

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
