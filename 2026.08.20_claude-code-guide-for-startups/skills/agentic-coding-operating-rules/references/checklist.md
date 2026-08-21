# The checklist

The guide's consolidated technical tips, one page, in the order the chapters
introduce them.

## Chapter 1: Everyone ships

- [ ] Claude can't understand what it can't see. Connect it to sources of truth
      and the tools your team uses every day via MCP or CLI.
      - MCP when your team is copying and pasting information from a tool into
        Claude.
      - CLI when a mature command-line tool already exists (`gh`, `kubectl`,
        `bq`, `psql`) and you want Claude working against the same ground truth
        your engineers do — often more token-efficient.
- [ ] Create a company plugin marketplace so one employee's best practice can be
      instantly transferred to another via a skill.
- [ ] Use `CLAUDE.md` files in each subdirectory of your repo for coding
      conventions specific to that subdirectory that apply every time.
- [ ] Use skills for on-demand procedural workflows.

## Chapter 2: Automate the tedium

- [ ] Set up Code Review (research preview) on a repo for an automated review
      pass on PRs. Findings carry a severity level; fix and push manually, or
      comment `@Claude` on a finding to close the loop with GitHub Actions
      configured.
- [ ] Make Claude Tag (public beta) part of your CI/CD on-call response and bug
      triage.
- [ ] Use dynamic workflows to fan multiple subagents out over large amounts of
      data in parallel, or to conduct an adversarial review of another agent's
      work. With a model like Opus or Fable, say "fan out multiple subagents" or
      "use a workflow."

## Chapter 3: Trust, but verify

- [ ] Put what can't change in `CLAUDE.md` at the root of your repo. Claude reads
      it at the start of every session, so architecture rules, security
      boundaries, and non-negotiables travel with every session.
- [ ] Use loops — agents that repeat cycles of work until a stop condition is met
      — for more autonomous or long-horizon work. Define the criteria in a skill;
      the more clearly defined, the better.
- [ ] Establish a process for creating and maintaining agent evaluations. Keep
      multiple eval sets for your key use cases and update them regularly, so you
      can prevent drift and evaluate future models.
- [ ] Use hooks — user-defined commands that fire at fixed points in Claude
      Code's lifecycle and execute every time regardless of what the model
      decides — where components of the work need to be deterministic. Named
      examples: block a write that fails a lint, require a test pass before
      commit, strip secrets before anything leaves the sandbox.
- [ ] Use `/goal` on long complex tasks where Claude may prematurely call the job
      done, prefer its own findings when reviewing, or drift from the original
      goal.

## Chapter 4: Build for rebuilding

- [ ] Use git worktrees to run a rebuild in an isolated copy of the repo while
      the current version stays untouched. One repository and one object store,
      several checkouts you can work in simultaneously, each on its own branch.
      Each linked worktree is an ordinary directory with its own checked-out
      branch. This is what makes "build it four times" cheap.
- [ ] For non-trivial rewrites, start Claude Code in plan mode (`--plan` or
      Shift+Tab). Claude explores the codebase and proposes the rebuild approach
      before writing any code — you approve or redirect. It's the cheapest place
      to catch a rebuild about to drift from your architecture.

## Signals that you are ready to formalize evals

The guide's account of the breaking point: teams get surprisingly far on manual
testing, dogfooding, and intuition. It breaks when users report the agent feels
worse after changes and the team is flying blind with no way to verify except
guess and check — unable to distinguish real regressions from noise, to test
changes automatically against hundreds of scenarios before shipping, or to
measure improvements.

## Source

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) (published 2026-08-20).
