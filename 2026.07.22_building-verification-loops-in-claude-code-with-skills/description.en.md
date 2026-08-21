**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Delba de Oliveira of the Claude Code team explains how to turn the manual checks you repeat after every change into skills, so Claude closes its own feedback loop. Most agentic coding sessions follow a loop — gather context, take action, verify results, loop back if needed — and Claude already verifies some things on its own from the deterministic signals in a codebase: type checkers, linters, tests, runtime errors. Whatever Claude cannot infer becomes the steps you take by hand. Those are the steps worth encoding.

The post covers the built-in loops to try first, the minimal `SKILL.md` shape for a verification skill, and the four ways a check can be deployed — standalone, embedded in the producing skill, chained after another skill, or run on every PR — each with the situation it fits, its cost, and the signal that you have outgrown it.

## When is it useful?
- When you keep making the same small correction every time Claude implements a feature.
- When a project-specific rule is real but deterministic enough that no generic linter catches it.
- When starting a new project and you need to write down how it should behave.
- When deciding whether a check should be invoked deliberately, embedded, chained, or made a team-wide PR gate.
- When you want to add verification to a skill you cannot edit — a built-in or plugin-managed one.
- When a personal habit is ready to become team infrastructure.

## Key points
- **A verification loop is a repeating cycle where the agent checks its own work** — running tests, linters, or custom checks — and fixes what fails before moving on. Packaged as skills, every session applies the same checks instead of relying on a human to remember them.
- **Try the built-ins first**: `/verify`, toolchain error codes (list exact build and test commands in `CLAUDE.md`), Code Review in research preview, GitHub Actions, spec validation, and rubrics in Claude Managed Agents where a separate grader agent loops failures back for rework.
- **Write the check in plain English, the way you'd hand it to a new teammate on day one.** If it is hard to articulate, ask Claude for best practices first and edit — your differences are exactly what to capture.
- **The check need not be qualitative.** "Reject any migration that drops a column without a backfill step" is deterministic, project-specific, and no generic linter will catch it.
- **The simplest verification skill is a few lines of frontmatter plus a body**: what to read, what to confirm, how to report and fix. `skill-creator` will interview you if you'd rather not hand-write it.
- **Standalone** earns its place for cross-cutting checks that don't apply every time; the cost is remembering to invoke it, and running it after every change is the signal to embed or chain.
- **Embedded** is a one-line append to the producing skill's body — but only works on skills you can edit; built-in and plugin-managed skills get overwritten on update.
- **Chained** turns a habit into a contract: "I always run `/verify` after `/simplify`" becomes "`/simplify` always runs `/verify` when it finishes." Anthropic's Claude Code team chains `/code-review` → `/simplify` → `/verify` → `/design`. It trades flexibility for automation and can increase token spend.
- **On every PR** is where verification stops being personal infrastructure and becomes team infrastructure — but hold off while the chain is still in flux, since every adjustment becomes a team-visible event.

## Bundled resources
- `skills/verification-loop-builder/SKILL.md` — the built-in loops, how to write the check, the four deployment patterns, and the six-step creation process.
- `skills/verification-loop-builder/templates/verification-skill.md` — the minimal frontmatter-plus-body shape, with guidance on each field.
- `skills/verification-loop-builder/templates/wrapper-chain-skill.md` — the wrapper pattern for chaining onto a skill you cannot modify.
- `skills/verification-loop-builder/examples/verify-log-hygiene.md` — the worked log-hygiene skill from the post.
- `skills/verification-loop-builder/examples/scaffold-component-embedded.md` — the one-line embed inside a component-scaffolding skill.
- `skills/verification-loop-builder/references/built-in-loops.md` — the six built-in verification approaches in detail.
- `skills/verification-loop-builder/references/deployment-patterns.md` — standalone, embedded, chained, and PR-wide, with costs and outgrow signals.
- `guides/verification-loops.{en,ko,es,ja}.md` — the full walkthrough in four languages.

## Source
[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) — Delba de Oliveira, July 22, 2026.
