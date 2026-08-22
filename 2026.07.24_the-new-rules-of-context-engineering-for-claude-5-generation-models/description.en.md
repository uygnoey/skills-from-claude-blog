**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Thariq Shihipar explains what changed about context engineering when Claude 5 generation models arrived — starting from the fact that Anthropic removed over 80% of Claude Code's system prompt for those models with no measurable loss in coding evaluations.

The diagnosis is that the old approach was *hobbling* Claude. Rules had accumulated across three layers — the system prompt, CLAUDE.md files, and skills — until they began contradicting each other, one layer saying to leave documentation as appropriate while another said not to add comments. Newer models read user intent without that scaffolding, so what remains of it is only the harm. The post lays out six then/now shifts and then restates what each layer of assembled context is now actually for.

## When is it useful?
- When a system prompt, CLAUDE.md, or skill has grown long enough that you suspect parts of it are working against you.
- When two layers of your context give instructions that cannot both be followed.
- When migrating an agent that was tuned for an earlier model generation.
- When deciding whether to teach a tool through examples or through its signature.
- When tool usage guidance is duplicated between the system prompt and the tool description.
- When choosing the format for a spec Claude will work from.

## Key points
- **Over 80% of Claude Code's system prompt was removed** for Claude 5 models, with no measurable loss in coding evaluations.
- **Rules → judgment.** "Default to writing no comments. Never write multi-paragraph docstrings or multi-line comment blocks — one short line max." became "Write code that reads like the surrounding code: match its comment density, naming, and idiom."
- **Examples → interface design.** Usage examples constrain a newer model to the exploration space they cover. Put the guidance in expressive parameters and clearly enumerated options instead.
- **Upfront → progressive disclosure.** Load context selectively through skills and deferred-loading tools rather than paying for everything in every request.
- **Repetition → one tool description.** Earlier models benefited from the same instruction appearing in both the system prompt and the tool description; current models consult tool descriptions reliably.
- **Manual memory → auto-memory.** Pinning context with the `#` hotkey gives way to Claude preserving what is relevant to the work and to you.
- **Simple specs → rich references.** HTML artifacts, code references, test suites, and rubrics carry intent with less ambiguity than a markdown plan.
- **Each layer has one job now.** System prompt: product context. CLAUDE.md: lightweight, concentrating on gotchas. Skills: on-demand guides carrying your team's opinions. References: depth by @mention, preferring code over prose.
- **`/doctor`** in Claude Code (`claude doctor` from the CLI) automatically rightsizes skills, CLAUDE.md files, and system prompts for Claude 5 models.

## Bundled resources
- `skills/context-engineering-for-new-models/SKILL.md` — find the contradictions, apply the six shifts, rewrite each layer, then measure.
- `skills/context-engineering-for-new-models/references/then-vs-now.md` — all six shifts with the then/now text and the reasoning behind each swap.
- `skills/context-engineering-for-new-models/references/context-layers.md` — what the system prompt, CLAUDE.md, skills, and references are each for now.
- `skills/context-engineering-for-new-models/templates/lightweight-claude-md.md` — the target shape for a CLAUDE.md that has grown into a rulebook, plus what no longer belongs in it.
- `skills/context-engineering-for-new-models/examples/rule-rewrites.md` — four before/after rewrites: a comment rule, a tool taught by example, a duplicated instruction, and a markdown spec.
- `guides/context-engineering-rules.{en,ko,es,ja}.md` — the full walkthrough in four languages.

## Source
[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) — Thariq Shihipar, July 24, 2026.
