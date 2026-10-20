---
name: code-review-rollout
description: Roll out Claude Code's Code Review across an organization's repositories — enable it, install the GitHub App, pick which repositories to review, and assign each one a Quick, Standard, or Deep review depth. Use when an admin on a Claude Team or Enterprise plan is turning Code Review on, adding repositories, or deciding how deep reviews should run for a given codebase.
---

## Purpose
Get automated pull request review running on the repositories that benefit from it, at a depth that
matches each codebase, without making developers configure anything.

## When to use
- An organization on a Claude Team or Enterprise plan is enabling Code Review for the first time.
- New repositories need to be added to an existing Code Review setup.
- Review depth needs revisiting: routine repositories feel over-reviewed, or a critical one is not
  getting a deep enough pass.
- Pull request volume has grown faster than human review capacity — the usual effect of
  agent-assisted development.

## Instructions

1. **Confirm eligibility.** Code Review is generally available for Claude Team and Enterprise plans.
   Check the credit program before rolling out, since it is time-bound: see
   [references/review-depth-levels.md](./references/review-depth-levels.md).

2. **Enable and connect (admin steps).**
   - Enable Code Review in your Claude Code settings.
   - Install the GitHub App.
   - Select the repositories you want reviews to run on.

3. **Choose a depth per repository.** Admins set Quick, Standard, or Deep for each repository.
   Standard is the default; every level delivers high-quality reviews, so the choice is about how
   much review each codebase warrants, not about settling for less.
   - Routine codebases → a quick pass.
   - The most critical codebases → a deep review.
   - Everything else → Standard.
   The per-level description and selection criteria are in
   [references/review-depth-levels.md](./references/review-depth-levels.md).

4. **Tell developers there is nothing to do.** Once Code Review is enabled for a repository, reviews
   run automatically on new pull requests with no developer configuration.

5. **Set expectations on turnaround.** Most reviews finish in about 6–10 minutes, roughly 3x faster
   than during the research preview (~20 minutes). Plan review-blocking checks around that window
   rather than around preview-era timings.

6. **Read findings as problem / trigger / fix.** Findings are written to state the problem, what
   triggers it, and the fix in a few sentences. Treat anything that does not fit that shape as a
   signal to re-read the diff rather than as a verdict.

7. **Revisit depth with evidence.** If reviews feel noisy on a routine repository or thin on a
   critical one, change that repository's depth. Depth is a per-repository setting precisely so one
   organization-wide choice does not have to fit every codebase.

## Examples

- **First rollout on a Team plan.** An admin enables Code Review, installs the GitHub App, and
  selects three repositories: the main product service (Standard), a payments service (Deep), and an
  internal tooling repository (Quick). Developers are told only that reviews will appear on new PRs.
- **Reacting to review noise.** A repository of generated client bindings produces long reviews on
  mechanical changes. The admin moves that repository from Standard to Quick; the critical services
  keep Standard and Deep.
- **Raising depth for a risky codebase.** An authentication service moves from Standard to Deep ahead
  of a migration, so reviews cover it more thoroughly while the risky changes land.
- **Claiming credits.** An eligible Enterprise organization claims its Code Review credits before
  January 15, 2027, and schedules the rollout so the repositories are already enabled when the 30-day
  credit window starts — see
  [references/review-depth-levels.md](./references/review-depth-levels.md).

## Notes
- Code Review is designed to catch bugs before they reach production; it is one input to a human
  decision, not an approval.
- Anthropic runs Code Review on its own pull requests, which is part of how the team finds where
  reviews slow engineers down.
- Consult the official Code Review docs for the settings and GitHub App details; this skill covers
  the rollout decisions, not the UI.

## Source
Distilled from [Code Review is now generally available](https://claude.com/resources/articles/code-review-is-now-generally-available)
(published 2026-10-15).
