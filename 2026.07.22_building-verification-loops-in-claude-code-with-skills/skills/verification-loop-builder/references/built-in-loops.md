# Built-in verification loops

Before designing a custom loop, check what Claude Code already supports. Reaching for one of these
first is step 2 of the creation process.

## `/verify`

A skill that builds, runs, and observes the changes in your application. The default first thing
to try when you notice a manual follow-up step.

## Toolchain signals

Claude aims to catch and act on error codes and warnings from any tool you provide, such as a
linter. This is the verification Claude already does on its own, from the deterministic signals in
your codebase: type checkers, linters, tests, runtime errors.

**Good practice:** list your exact build and test commands in `CLAUDE.md` so Claude does not have
to infer them.

## Code Review (research preview)

A managed multi-agent service that runs an automated review pass on PRs in the repos you enable.
Two ways to close the loop on a finding:

- Fix it manually and push.
- Comment `@claude` on the finding — requires GitHub Actions already set up and configured.

## GitHub Actions

Define a job that invokes Claude with a verification skill, and the same checks you run locally
fire on every push or PR. This is the mechanism behind the "on every PR" deployment pattern.

## Spec validation

A skill that helps verify each change against a markdown spec in the repo, and looks to fix
violations.

## Rubrics in Claude Managed Agents (beta)

A managed agentic service that verifies outcomes against a rubric using a **separate grader
agent**. Failures loop back for rework automatically.

## What is left over

Whatever Claude cannot infer becomes the steps you take to manually check a feature. Those are the
steps that turn into custom verification skills.

## Source

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
