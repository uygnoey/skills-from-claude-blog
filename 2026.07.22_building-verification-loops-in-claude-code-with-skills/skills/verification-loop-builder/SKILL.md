---
name: verification-loop-builder
description: Turn the manual checks you repeat after every change into Claude Code skills, so Claude closes its own feedback loop instead of waiting for a human to remember the check. Use when you keep making the same small corrections after Claude implements a feature; when a project-specific rule ("reject any migration that drops a column without a backfill step") is real but no generic linter catches it; when deciding whether a check should run standalone, embedded in the producing skill, chained after another skill, or on every PR; or when adding verification to a skill you cannot edit. Covers the built-in loops to try first (/verify, toolchain signals, Code Review, GitHub Actions, spec validation, rubrics in Claude Managed Agents), the minimal SKILL.md shape for a verification skill, the four deployment patterns with their costs, and the six-step creation process.
---

# Building verification loops

Most agentic coding sessions follow a loop: you ask for a change, Claude gathers context, takes
action, verifies the results, and if needed loops back to gather more context.

Verification is how an agent checks its work before responding. Claude already does some of this
by observing the deterministic signals in a codebase — type checkers, linters, tests, runtime
errors. **Whatever Claude cannot infer becomes the steps you take to manually check a feature.**
Those manual steps are what this skill turns into loops.

A verification loop is a repeating cycle where the agent checks its own work — running tests,
linters, or custom checks — and fixes what fails before moving on. Packaged as a skill, every
session applies the same checks automatically instead of relying on a human to remember them.

## Instructions

### 1. Try the built-in loops first

Before writing anything, check whether an existing loop already covers the case. Full detail in
[references/built-in-loops.md](references/built-in-loops.md).

- **`/verify`** — builds, runs, and observes the changes in the application.
- **Toolchain** — Claude aims to catch and act on error codes and warnings from any tool you
  provide, such as a linter. List the exact build and test commands in `CLAUDE.md` so Claude does
  not have to infer them.
- **Code Review (research preview)** — a managed multi-agent service that runs an automated
  review pass on PRs in the repos you enable. Fix the finding and push, or close the loop by
  commenting `@claude` on the finding (requires GitHub Actions set up).
- **GitHub Actions** — define a job that invokes Claude with a verification skill, and the same
  checks you run locally fire on every push or PR.
- **Spec validation** — a skill that verifies each change against a markdown spec in the repo and
  looks to fix violations.
- **Rubrics in Claude Managed Agents (beta)** — verify outcomes against a rubric using a separate
  grader agent; failures loop back for rework automatically.

### 2. Write down what you keep doing by hand

On an existing project, the trigger is repetition: you find yourself making the same small
corrections every time Claude implements a feature. Write down everything you do every time.

On a new project, write the best-practices version in plain English, **the way you would hand it
to a new teammate on day one.**

If the check is hard to articulate, ask Claude for best practices first and edit from there. Your
version probably differs on a few specific points — those differences are exactly what to capture.

> The check does not have to be qualitative to belong here. "Reject any migration that drops a
> column without a backfill step" is a deterministic rule no generic linter will catch but a
> project-specific one will. Anything you keep enforcing by hand qualifies for capture as a loop.

### 3. Make it a skill

Fastest path: install the `skill-creator` plugin and let Claude interview you.

```
/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.
```

Or hand-write it by dropping a markdown file in `.claude/skills/` inside the project. The simplest
possible verification skill is a few lines of frontmatter plus a body — see
[templates/verification-skill.md](templates/verification-skill.md) for the shape and
[examples/verify-log-hygiene.md](examples/verify-log-hygiene.md) for a worked example.

Keep the body in the same imperative register you would use with a teammate: what to read, what to
confirm, how to report a violation, and what to fix.

### 4. Match the check to where it runs

Decide how the loop kicks off. The four patterns, their costs, and their outgrow signals are in
[references/deployment-patterns.md](references/deployment-patterns.md).

| Pattern | Fires when | Use for | Cost |
|---|---|---|---|
| **Standalone** | you invoke it deliberately, after the artifact exists | cross-cutting checks that do not apply every time — pre-commit security scan, pre-PR accessibility audit, license-header verification | each invocation is a turn you have to remember to take |
| **Embedded** | automatically, as part of the producing skill | a check that belongs to one specific workflow | only works on skills you can edit |
| **Chained** | one skill calls another at its end | running several verified handoffs end-to-end | trades flexibility for automation; can increase token spend |
| **On every PR** | on every change, regardless of author | team-wide standards | every adjustment becomes a team-visible event |

**Standalone → embedded/chained.** The signal that you have outgrown standalone is running the
skill after every change. At that point the procedure has earned a permanent home.

**Embedded** is a one-line append to the producing skill's body — see
[examples/scaffold-component-embedded.md](examples/scaffold-component-embedded.md). Verify the
embed works by invoking the skill on a fresh task and confirming the new step runs as part of the
output. If it does not, the skill's description or earlier instructions are not pulling the
appended check in. Built-in skills and plugin-managed skills (the kind that get overwritten on
update) are off-limits for this pattern — chain instead. Skip embedded for checks that span
workflows; those want standalone so you can invoke them from any context.

**Chained** is also how you add verification to a skill you cannot modify: build a custom wrapper
skill that invokes the original, then invokes your verification skill — see
[templates/wrapper-chain-skill.md](templates/wrapper-chain-skill.md). Members of Anthropic's
Claude Code team use this pattern day to day: `/code-review` hunts for bugs, `/simplify` cleans up
the diff, a `/verify` skill confirms end-to-end behavior, and a custom `/design` skill checks
against guidelines in a `DESIGN.md` file if the change touched UI. What started as a habit ("I
always run `/verify` after `/simplify`") becomes a contract ("`/simplify` always runs `/verify`
when it finishes"). Skip chaining when the steps are independent enough that you sometimes want to
run one without the others.

**On every PR** once the chain is solid for your own changes. Same skills, same rubrics, same
standards, applied without depending on the author's diligence. Hold off on PR-wide gates while
the chain is still in flux.

### 5. The creation process

Consistent no matter what you are automating or in what environment:

1. Pick the manual follow-up you did most often this week.
2. Try the built-in `/verify` skill first and see if it helps your process.
3. Write the procedure in plain English, the way you would hand it to a new teammate on day one.
4. Hand it to `skill-creator`, or drop the markdown file in `.claude/skills/` yourself.
5. Invoke it on a new task and confirm the check runs as part of the output; iterate if needed.
6. Experiment with skill chaining to create an end-to-end verification flow.

The more you can encode for Claude to follow, the more often Claude's response will land closer to
what you want on the very first try.

## Examples

### Capturing a repeated correction

> You keep noticing that Claude's error logs omit the request ID, and sometimes dump the request
> body into the log line.

Write it as a check in plain English, then encode it as `.claude/skills/verify-log-hygiene/SKILL.md`
with `allowed-tools: [Read, Edit, Grep]`. The body tells Claude to read the error-handling paths in
the current diff, confirm each log call on an error path includes the request ID and does not pass
the request body, headers, or any user-supplied payload, report each violation with `file:line`,
then fix it. Full file in [examples/verify-log-hygiene.md](examples/verify-log-hygiene.md).

### Embedding a check in a producing skill

> A `scaffold-component` skill creates a React component, its co-located test, and an index export
> — and you always run eslint on the result afterwards.

Append one step to the producing skill's body: *"After creating the component file, run eslint on
it and address any errors before reporting completion."* Then invoke the skill on a fresh task and
confirm eslint runs as part of the output. Full file in
[examples/scaffold-component-embedded.md](examples/scaffold-component-embedded.md).

### Adding verification to a skill you cannot edit

> You want `/simplify` — which you do not own — to always be followed by a public-API check.

Write a wrapper skill instead of editing the original:

```markdown
# .claude/skills/safe-refactor/SKILL.md
Run /simplify on the current diff first.
When /simplify finishes, invoke /verify-no-public-api-changes.
```

### Deciding standalone vs. embedded

> A license-header check applies across the whole repo, not to one workflow.

Keep it standalone — you want it available from many workflows without firing on every code change.
If you find yourself running it after every change anyway, that is the signal to embed or chain it.

## Source

- [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) — Delba de Oliveira, Claude Code team, July 22, 2026.
