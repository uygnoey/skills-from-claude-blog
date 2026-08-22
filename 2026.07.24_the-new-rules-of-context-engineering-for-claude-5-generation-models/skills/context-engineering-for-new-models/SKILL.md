---
name: context-engineering-for-new-models
description: Rightsize the context you hand a newer-generation model — system prompt, CLAUDE.md, skills, tool descriptions, and references — by removing rules the model no longer needs and replacing them with judgment, interface design, and progressive disclosure. Use when a system prompt or CLAUDE.md has grown long, when instructions contradict each other, when a skill over-constrains the model, when tool guidance is duplicated between the system prompt and the tool description, or when migrating an agent built for an older model generation.
---

# Context engineering for newer-generation models

Anthropic removed **over 80% of Claude Code's system prompt** for Claude 5 models with no measurable
loss in coding evaluations. The context that made older models perform well is not the context that
makes newer models perform well — and much of it is now actively holding them back.

The failure mode has a name in the post: **hobbling**. The system prompt, CLAUDE.md files, and skills
had all accumulated rules, and those rules started contradicting one another — one layer saying to
leave documentation as appropriate, another saying not to add comments at all. Newer models can read
user intent without those restrictions, so the restrictions are what remains: conflicting orders that
narrow behavior for no gain.

The other half of the shift is that CLAUDE.md is no longer the only place context can live. Claude
used to lean on it as memory, information, and guidance all at once. Memory, artifacts, and skills now
give Claude its own ways of loading and sharing context across sessions.

## Instructions

### 1. Find the contradictions first

Before adding anything, read your system prompt, CLAUDE.md, and skills together as one document — the
model sees them that way. Look for pairs of instructions that cannot both be followed, and for rules
that were written to work around a limitation the current model does not have. That is the material
to cut.

`/doctor` in Claude Code (`claude doctor` from the CLI) automatically rightsizes skills, CLAUDE.md
files, and system prompts for Claude 5 models. Run it before hand-editing.

### 2. Apply the six shifts

Each shift replaces something you used to write with something the newer model does better on its
own. Full then/now detail in [references/then-vs-now.md](references/then-vs-now.md).

1. **Rules → judgment.** Replace hard prohibitions with the outcome you want. Instead of a ban on
   comments, ask for code that reads like the code around it.
2. **Examples → interface design.** Stop teaching a tool through usage examples; put the teaching in
   the tool itself — expressive parameters, clearly enumerated options. Examples pin newer models to
   the exploration space the examples happen to cover.
3. **Everything upfront → progressive disclosure.** Load guidance when it is needed, through skills
   and deferred-loading tools, rather than paying for it in every request.
4. **Repetition → one clear tool description.** Say how a tool is used in the tool description only.
   Older models needed the reinforcement in the system prompt; current models do not.
5. **Manual memory → auto-memory.** Stop curating context into CLAUDE.md with the `#` hotkey. Claude
   saves the memories that are relevant to the work and to you.
6. **Simple specs → rich references.** Markdown plans are the low-fidelity option. Code, HTML
   artifacts, test suites, and rubrics say the same thing with less ambiguity.

### 3. Rewrite each layer for what it is actually for

The four layers now have distinct jobs. Details in
[references/context-layers.md](references/context-layers.md).

- **System prompt** — product context: what product the agent is inside and what role it plays. Most
  Claude Code users never touch it, but if you are building a custom agent it deserves real effort.
- **CLAUDE.md** — lightweight. What the repository is, plus the gotchas and non-obvious patterns that
  are only discoverable by being told. Anything long moves into a skill.
- **Skills** — lightweight guides for finding information on demand. Encode the opinions and best
  practices that are specific to your team or product; avoid over-constraining outside the areas that
  genuinely matter. Split a long skill across multiple files.
- **References** — depth, pulled in by @mention: specs, mockups, codebases. Prefer code over prose.

Start from [templates/lightweight-claude-md.md](templates/lightweight-claude-md.md) when rewriting a
CLAUDE.md that has outgrown itself.

### 4. Cut, then measure

The 80% number came with evaluations attached. Removing context is a change like any other: make the
cut, then check the behavior you care about still holds. "No measurable loss" is a claim you should be
able to make about your own agent, not one to assume.

## Examples

Worked before/after rewrites in [examples/rule-rewrites.md](examples/rule-rewrites.md). In outline:

**A comment rule.** "Default to writing no comments. Never write multi-paragraph docstrings or
multi-line comment blocks — one short line max." becomes "Write code that reads like the surrounding
code: match its comment density, naming, and idiom." The prohibition becomes a standard, and the model
resolves it per file.

**A tool taught by example.** A system prompt carrying three sample invocations of a search tool
becomes a tool description with an enumerated `scope` parameter and a `mode` option list. The hint
about correct usage moves into the signature, where it applies to every call rather than to the cases
the examples covered.

**A duplicated instruction.** Guidance that appeared in both the system prompt and the tool
description is deleted from the system prompt. Nothing replaces it.

**A markdown spec.** A written description of a component's states is replaced by an HTML artifact
plus the test suite that pins the behavior.

## Source

["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
— Thariq Shihipar, July 24, 2026.
