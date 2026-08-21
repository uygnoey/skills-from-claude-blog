**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic describes the six-step process it uses to run large-scale code migrations with Claude Code, turning what used to be multi-year projects into work measured in weeks. The organizing principle is stated up front: you don't fix the code, you fix the process (loop) that produced it.

The six steps are (1) write the rulebook, dependency map, and gap inventory, (2) stress-test the rules on a throwaway mini-migration, (3) translate everything with parallel agents, then (4) compile, (5) run, and (6) match behavior against the original. Two migrations anchor the guide: Jarred Sumner's port of Bun from Zig to Rust — about a million lines in under two weeks, 100% of the existing test suite green before merge — and Mike Krieger's Python-to-TypeScript port of 165,000 lines over a weekend.

## When is it useful?
- When a port or rewrite is too large to review file by file, and hand-porting would never catch up with the original.
- When a migration is producing plausible-looking code that quietly diverges from the original's behavior.
- When you need to decide how to split translation work across parallel agents and in what order.
- When a rewrite keeps stalling because there is no agreed definition of "done" or "correct."
- When you are estimating what a migration of this shape would actually cost in tokens and time.

## Key points
- **Build the judge first.** Sort existing tests into portable and internals-bound, rewrite the portable ones as assertions that run against both codebases, then validate the judge in both directions — it must pass on the original and fail on deliberately broken code. Without a test suite, build a parity harness of real end-to-end scenarios instead.
- **Rulebook before gap inventory.** The gap inventory is defined by what the rulebook's defaults won't cover, so it can't be written first. And the rulebook's shape depends on an earlier decision: a structure-preserving port yields lookup tables, a redesign yields a design document.
- **The stress test's output is a better rulebook, not progress.** Run a mini-migration with a translator, a reviewer, and a rule extractor — then throw the translated files away, so their embedded decisions can't create pressure to keep them.
- **Done must be mechanical.** The queue's completion test is that the output file exists on disk. Anything requiring judgment can't be resumed, and every long migration gets interrupted.
- **Flag, never guess.** An unsure implementer emits `// TODO(port): <reason>` and moves on, converting an invisible correctness risk into a visible queue item. The reason string is what lets a later pass cluster fifty markers into one decision.
- **Adversarial review.** Two reviewers per unit of work in separate contexts, with disagreement escalating to a third agent. A single reviewer converges on the implementer's framing and approves a systemic error a thousand times over.
- **When a reviewer keeps catching the same mistake, add a sentence to the rulebook and regenerate the batch** — a per-file patch leaves the generator still producing the error.
- **Don't use the largest model for everything.** Token spend concentrates in the loops: implementers on smaller models (twelve parallel Sonnet subagents on the TypeScript port), reviewers and delegators on larger ones. Bun's migration ran 5.9B input / 690M output tokens, roughly $165,000 at API pricing, for a 19% smaller binary and 2–5% faster real-world performance.
- **Success includes regressions.** Bun merged clean and produced 19 afterward, all fixed. The question is whether regressions are findable and cheap, not whether they're absent.

## Bundled resources
- `skills/large-scale-code-migration/SKILL.md` — the six-step process as an executable procedure.
- `skills/large-scale-code-migration/references/six-step-process.md` — each step in full, including where Step 4 folds into Step 3.
- `skills/large-scale-code-migration/references/verification-harness.md` — building and validating the judge, with a checklist.
- `skills/large-scale-code-migration/references/loop-design.md` — queue design, TODO(port) markers, adversarial review, model selection, orchestrator scripts.
- `skills/large-scale-code-migration/templates/rulebook.md`, `templates/dependency-map.md`, `templates/gap-inventory.md` — the three phase-one documents as fillable scaffolds.
- `skills/large-scale-code-migration/examples/case-studies.md` — the Bun and Python-to-TypeScript numbers, with what to take from each.
- `agents/migration-translator.md`, `migration-reviewer.md`, `rule-extractor.md`, `review-tiebreaker.md`, `migration-fixer.md` — the five agent roles the post names.
- `guides/migration-playbook.{en,ko,es,ja}.md` — the method as a narrative playbook.

## Source
[How Anthropic Runs Large-Scale Code Migrations with Claude Code](https://claude.com/blog/ai-code-migration) — published 2026-07-16.
