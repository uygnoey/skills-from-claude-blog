**English** · [한국어](./startup-operating-model.ko.md) · [Español](./startup-operating-model.es.md) · [日本語](./startup-operating-model.ja.md)

# Running a startup on agentic coding

A survey of how more than a dozen fast-growing startups organize their product
development lifecycle around Claude Code — and what to copy first.

The underlying question the guide asks: what would it look like if an
organization built their product development lifecycle with Claude Code from the
ground up?

## Reported outcomes

| Company | Reported |
| --- | --- |
| ClickHouse | 30% more features shipped |
| Omni | 2–3x engineering productivity |
| Clay | 100% of bug triage automated |
| Artemis Security | 6,000+ PRs a week |

## The operating model in five rules

1. **Everyone ships.** The barrier to a working first version drops far enough
   that the person who understands the problem builds it.
2. **Automate the tedium.** Agents own the mechanical 80% of the lifecycle.
3. **Trust, but verify.** You cannot automate what you cannot check.
4. **Build for rebuilding.** Model capability shifts underneath you; treat
   scaffolding as disposable.
5. **Prototype, dogfood, productionize.** Building with AI is how you learn to
   build products with AI.

Rules 2 and 3 are a pair. Adopting 2 without 3 is how teams get plausible code
that drifts from their architecture in ways that look right but aren't.

## What changes organizationally

**The hand-off chain collapses.** Heidi calls the old path the broken telephone
problem: idea → PM → designer → engineer, essence lost along the way, weeks
elapsed. The person who understands the problem now ships the PR and brings in
designers and engineers for the parts where their expertise matters.

**The division of labor survives.** Marketers still market and developers still
develop. What opens to everyone is the 0→1 step.

**Contributions need a road.** Without a forum, non-engineer contributions stay
a matter of individual ambition. Clay runs quarterly reviews where prototypes
enter the formal roadmap. Omni keeps a Slack channel for Claude-generated
prototypes and pairs "everyone ships" with "everyone talks with customers,"
deliberately putting engineers in front of customers to shorten the feedback
loop.

**Standards move into shared files.** Skills — reusable instruction files
encoding team standards and context — keep a democratized process producing a
cohesive product. Share them through a directory or a company plugin marketplace.
Emergent's tolerance is worth adopting: slightly outdated context files are fine
as long as the agent can quickly verify and course correct.

## What changes technically

**Connect Claude to ground truth.** It cannot understand what it cannot see. Use
MCP wherever your team is copying and pasting between a tool and Claude; use the
CLI where a mature command-line tool already exists (`gh`, `kubectl`, `bq`,
`psql`) and you want the agent working against the same ground truth as your
engineers — often more token-efficient.

**Layer the context.** Root `CLAUDE.md` for what cannot change. Subdirectory
`CLAUDE.md` for conventions that apply every time in that part of the repo.
Skills for on-demand procedural workflows.

**Put agents on recurring work.** ClickHouse's flaky-test and missing-coverage
agents are the #2 and #3 contributors to their repo. Clay automated bug triage
from first pass to suggested fix. Translucent's reviewer fans out across a change
and synthesizes findings from multiple angles.

**Automate outside the SDLC too.** Self-service data analytics was the most
commonly automated non-engineering process — internal analytics agents,
feedback categorization against usage data, summarizing thousands of legal
documents with subagents, sweeping claims data for anomalies, mining hospital
financial data continuously.

**Gate the deterministic parts.** Hooks fire at fixed points in the lifecycle and
execute regardless of what the model decides: block a write that fails a lint,
require a test pass before commit, strip secrets before anything leaves the
sandbox. Dynamic workflows give deterministic sequencing with separate context
windows and focused goals; `/goal` helps where a long task risks premature
completion or drift.

**Make rebuilding cheap.** Git worktrees run v2 next to v1 in an isolated
checkout on its own branch, sharing one object store — run evals against both and
merge only when the new one wins. Plan mode before non-trivial rewrites catches
drift before any code is written.

## Verification is the gating investment

Artemis Security attributes its deployment speed to testing infrastructure,
codebase organization, and knowledge systems, not to the agents themselves:
structure those correctly and every contribution compounds.

The concrete practices:

- **Invariants written down.** Zingage's 567 lines of how the team thinks, after
  full autonomy produced architectural drift.
- **Loops with self-contained stop conditions.** A flaky-test agent verifies its
  own fix by rerunning the test.
- **Expert review that improves the principle.** Cainex routes auditor
  corrections into versioned agent instructions and back-tests against a golden
  set plus random samples. "Fix the principle, not the example." Their first
  version overfitted and accumulated patches, so they capped how many specifics
  can enter a change.
- **Multiple eval sets, maintained.** The breaking point for teams running on
  intuition is when users report the agent feels worse and there is no way to
  verify except guess and check.

## Sequencing your adoption

1. Write the root `CLAUDE.md` invariants and connect Claude to your real tools.
   Without these, everything downstream drifts.
2. Stand up a golden set and one eval suite for your highest-stakes use case.
3. Put an agent on one recurring, self-verifying task — flaky tests are the
   standard first choice.
4. Open the 0→1 path to non-engineers, and create the forum where prototypes get
   prioritized.
5. Add hooks where a step must be identical every time.
6. Use worktrees and plan mode for the first rebuild, and finish it — the rebuild
   is done when the old path is gone.

## Source

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups)
by Michael Segner (published 2026-08-20).
