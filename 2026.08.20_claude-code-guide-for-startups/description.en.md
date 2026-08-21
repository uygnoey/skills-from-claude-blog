**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic interviewed more than a dozen fast-growing startups — Artemis Security, Cainex, Clay, ClickHouse, Cognition, Commure, Crosby, Emergent, Harvey, Heidi, Higgsfield, Omni, Parahelp, Translucent, Zingage — about how they use Claude Code to build products and scale their companies, and distilled the answers into five operating rules. The framing question is what a product development lifecycle would look like if it were built with Claude Code from the ground up.

The five rules: everyone ships, automate the tedium, trust but verify, build for rebuilding, and prototype-dogfood-productionize. Each chapter carries founder quotes and concrete tips, and the guide ends with a one-page checklist consolidating them. Reported outcomes include 30% more features shipped (ClickHouse), 2–3x engineering productivity (Omni), 100% of bug triage automated (Clay), and 6,000+ PRs a week (Artemis Security).

## When is it useful?
- When a small team wants a shape for how to organize around agentic coding rather than a list of features.
- When non-engineers have the best product insight but no path from idea to working prototype.
- When you are deciding which parts of the SDLC to hand to agents and what has to be in place before you can trust them.
- When rewrites keep losing the prioritization fight and technical debt teardown never gets scheduled.
- When internal agent experiments need a route into the customer-facing product.

## Key points
- **The 0→1 step opens to everyone; the division of labor stays.** Marketers still market and developers still develop, but the person who understands the problem builds the first version. Heidi calls the old hand-off chain the "broken telephone problem."
- **Contributions need mechanisms, not encouragement.** Connect Claude to real tools via MCP or CLI, give prototypes a forum that feeds the roadmap (Clay's quarterly reviews, Omni's Slack channel), and share standards as skills through a directory or plugin marketplace.
- **Agents take recurring work end to end.** ClickHouse's flaky-test and missing-coverage agents are the #2 and #3 contributors to their repo; Clay automated bug triage from first pass to suggested fix; Translucent's reviewer fans out across a change and synthesizes multiple angles.
- **Rules 2 and 3 are a pair.** Zingage gave Claude full autonomy early and got plausible code that drifted from their architecture "in ways that looked right but weren't" — the fix was 567 lines of invariants in `CLAUDE.md`.
- **Fix the principle, not the example.** Cainex routes auditor corrections into versioned agent instructions and back-tests against a golden set plus random samples, after a first version that overfitted and accumulated patches.
- **Nothing is permanent.** Clay builds it four times; Harvey re-architected for each wave of model capability; Commure turned feature-flag teardown into a single skill invocation. Git worktrees and plan mode are what make rebuilding cheap.
- **The flywheel.** Advancing your own agentic coding practice teaches you how harness design evolves at the frontier, which you then spend on your own agents and products — internal agent → dogfood → customer-facing product on the Claude API, SDK, or Managed Agents.

## Bundled resources
- `skills/agentic-coding-operating-rules/SKILL.md` — the five rules as an applicable operating procedure.
- `skills/agentic-coding-operating-rules/references/five-rules.md` — each rule in full, with the founder quotes and boundaries.
- `skills/agentic-coding-operating-rules/references/checklist.md` — the guide's consolidated technical checklist.
- `skills/agentic-coding-operating-rules/templates/root-context-file.md` — a root `CLAUDE.md` scaffold for invariants.
- `skills/agentic-coding-operating-rules/examples/self-improvement-loop.md` — Cainex's correction loop, step by step.
- `skills/agentic-coding-operating-rules/examples/company-patterns.md` — what each of the fifteen companies actually did.
- `agents/flaky-test-fixer.md`, `agents/test-coverage-finder.md`, `agents/multi-angle-code-reviewer.md`, `agents/bug-triage.md` — the four agent roles named in the guide.
- `guides/startup-operating-model.{en,ko,es,ja}.md` — the operating model and an adoption sequence.

## Source
[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) by Michael Segner — published 2026-08-20.
