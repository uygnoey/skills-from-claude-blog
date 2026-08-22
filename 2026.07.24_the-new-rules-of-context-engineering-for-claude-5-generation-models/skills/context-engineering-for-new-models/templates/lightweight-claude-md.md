# CLAUDE.md template (lightweight)

Use this shape when rewriting a CLAUDE.md that has grown into a rulebook. The target is a short file:
what the repository is, plus the things that cannot be discovered by reading it. Anything that needs
more than a few lines becomes a skill.

```markdown
# <repository name>

<One or two sentences: what this repository is and what it produces.>

## Layout

<Only the parts a newcomer would not guess. Skip directories whose names already say what they hold.>

## Gotchas

<The non-obvious patterns. Each one should be something you would have to tell a new teammate out
loud, because nothing in the code says it.>

- <e.g. the generated client in `src/api/` is checked in; regenerate it with `<command>` rather than
  editing it>
- <e.g. `<directory>` looks unused but is loaded at runtime by `<mechanism>`>

## Commands

<Exact build, test, and lint commands — the ones you want run, not every command that exists.>

## Deeper guidance

<Point at skills rather than inlining. One line each.>

- `<skill-name>` — <when it applies>
```

## What does not belong here

- **Long instruction sets.** Move them into a skill and let them load when relevant.
- **Tool usage instructions.** They belong in the tool description, once.
- **Blanket prohibitions.** State the standard you actually want and let the model apply judgment.
- **Manually pinned memory.** Auto-memory handles it.
- **Anything that contradicts another layer.** Read the system prompt, this file, and your skills
  together before you keep a line.

## Before you hand-edit

Run `/doctor` in Claude Code (or `claude doctor` from the CLI). It rightsizes skills, CLAUDE.md files,
and system prompts for Claude 5 models automatically; hand-editing is for what it leaves behind.
