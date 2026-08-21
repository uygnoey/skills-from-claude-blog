**English** · [한국어](./verification-loops.ko.md) · [Español](./verification-loops.es.md) · [日本語](./verification-loops.ja.md)

# Building verification loops in Claude Code with skills

## The agentic loop

Most agentic coding sessions follow a loop: you ask for a change, Claude **gathers context**,
**takes action**, **verifies the results**, and if needed loops back to gather more context.

Verification is how an agent checks its work before responding. Claude already does some of this
on its own, by observing the deterministic signals in your codebase — type checkers, linters,
tests, runtime errors. Whatever Claude cannot infer becomes the steps *you* take to manually check
a feature.

Those manual steps can be transformed into verification loops. In Claude Code, a verification loop
is an iterative process where Claude checks and attempts to fix the work: a repeating cycle where
the agent runs tests, linters, or custom checks, and fixes what fails before moving on. Packaged
as skills, every session applies the same checks automatically instead of relying on a human to
remember them.

## Start with the built-in loops

- **`/verify`** — builds, runs, and observes the changes in your application.
- **Toolchain** — Claude aims to catch and act on error codes and warnings from any tool you
  provide, such as a linter. List your exact build and test commands in `CLAUDE.md` so Claude does
  not have to infer them.
- **Code Review (research preview)** — a managed multi-agent service that runs an automated review
  pass on PRs in the repos you enable. Fix the finding and push, or close the loop by commenting
  `@claude` on the finding (requires GitHub Actions already configured).
- **GitHub Actions** — define a job that invokes Claude with a verification skill, and the same
  checks you run locally fire on every push or PR.
- **Spec validation** — a skill that verifies each change against a markdown spec in the repo and
  looks to fix violations.
- **Rubrics in Claude Managed Agents (beta)** — verify outcomes against a rubric using a separate
  grader agent. Failures loop back for rework automatically.

## Writing your own

On an existing project, the trigger is repetition: you keep making the same small corrections
every time Claude implements a feature. Write down everything you find yourself doing every time.

On a new project, write the best-practices version in plain English, the way you would hand it to
a new teammate on day one.

If you are struggling to articulate the check itself, ask Claude for best practices first and edit
from there. Your version probably differs on a few specific points, and those differences are
exactly what you want to capture.

> **Pro tip.** The check does not have to be qualitative to belong here. "Reject any migration
> that drops a column without a backfill step" is a deterministic rule no generic linter will
> catch but a project-specific one will. Anything you keep having to enforce by hand as a manual
> check qualifies for capture as a loop.

### Make it a skill

The fastest way is to install the `skill-creator` plugin and let Claude interview you:

```
/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.
```

You can also hand-write a skill by dropping a markdown file in `.claude/skills/` inside your
project. The simplest possible verification skill is a few lines of frontmatter plus a body:

```markdown
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling
  or logging.
allowed-tools: [Read, Edit, Grep]
---
Read the error-handling paths in the current diff.

For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.

Report each violation with file:line, then fix it: add the request ID
where it's missing and strip the payload from the log call.
```

## Match the check to where it runs

### Standalone

You invoke it deliberately, after the artifact exists. A standalone skill earns its place for
cross-cutting checks that do not apply every time: a pre-commit security scan, a pre-PR
accessibility audit, license-header verification across a repo. Anything you want available across
many workflows but do not want firing on every code change.

The cost is that each invocation is still a turn you have to remember to take. The signal that you
have outgrown standalone is when you are running it after every change — at that point the
procedure has earned a permanent home.

### Embedded

Fires automatically as part of the producing skill. The check belongs to one specific workflow,
and the workflow now runs it without you asking. The simplest version is a one-line append to the
producing skill's body:

```
After creating the component file, run eslint on it and
address any errors before reporting completion.
```

Verify the embed works by invoking the skill on a fresh task and confirming the new step runs as
part of the output. If it does not, the skill's description or earlier instructions are not
pulling the appended check in.

Embedded only works on skills you can edit: ones you wrote yourself, or ones installed at a
project level where the `SKILL.md` file is under your control. Built-in skills and plugin-managed
skills (the kind that get overwritten on update) are off-limits for this pattern — chain instead.
Skip embedded for checks that span workflows; those want standalone.

### Chained

One skill calls another at its end, and several verified handoffs run end-to-end. Members of
Anthropic's Claude Code team use this pattern day to day: `/code-review` hunts for bugs,
`/simplify` cleans up the diff, a `/verify` skill confirms end-to-end behavior, and a custom
`/design` skill checks against guidelines in a `DESIGN.md` file if the change touched UI.

Chaining is also how you add verification to a skill you cannot modify — build a custom wrapper
skill that invokes the original, then invokes your verification skill:

```markdown
# .claude/skills/safe-refactor/SKILL.md
Run /simplify on the current diff first.
When /simplify finishes, invoke /verify-no-public-api-changes.
```

What started as a habit ("I always run `/verify` after `/simplify`") becomes a contract
("`/simplify` always runs `/verify` when it finishes"). The chain runs the whole dev cycle on its
own; you only step in when something escalates back to you.

Skip chaining when the steps are independent enough that you sometimes want to run one without the
others — chaining trades flexibility for automation. Chained loops can also increase token spend,
so test them before deploying broadly.

### On every PR

Once the chain is solid for your own changes, the same procedure can run on every PR. A
teammate's change passes the same gates yours did, whether or not they remembered to invoke the
chain. The infrastructure is the same kind of thing as the chain you already wrote, one step
further along: the same skills, the same rubrics, the same standards, applied without depending on
the author's diligence.

This is where verification stops being personal infrastructure and becomes team infrastructure.
Hold off on PR-wide gates while the chain is still in flux; every adjustment becomes a
team-visible event.

## The process

1. Pick the manual follow-up you did most often this week.
2. Try out the built-in `/verify` skill first and see if it helps your process.
3. Write the procedure in plain English, the way you would hand it to a new teammate on day one.
4. Hand it to `skill-creator`, or drop the markdown file in `.claude/skills/` yourself.
5. Invoke it on a new task and confirm the check runs as part of the output; iterate if needed.
6. Experiment with skill chaining to create an end-to-end verification flow.

The more you can encode for Claude to follow, the more often Claude's response will land closer to
what you want on the very first try. The corrections you no longer have to fiddle with free up
your attention for the work no skill can write down for you.

## Source

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
— Delba de Oliveira, Claude Code team, July 22, 2026.
