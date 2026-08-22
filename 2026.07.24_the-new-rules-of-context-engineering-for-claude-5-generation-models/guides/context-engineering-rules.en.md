**English** · [한국어](./context-engineering-rules.ko.md) · [Español](./context-engineering-rules.es.md) · [日本語](./context-engineering-rules.ja.md)

# The new rules of context engineering

Anthropic removed **over 80% of Claude Code's system prompt** for Claude 5 models — with no measurable
loss in coding evaluations. The lesson generalizes: the context engineering that made earlier model
generations perform well is not what makes newer ones perform well, and a good deal of it now gets in
the way.

## Unhobbling Claude

The old approach over-constrained Claude. Rules accumulated across three layers — the system prompt,
CLAUDE.md files, and skills — and once there were enough of them, they started to conflict. One layer
said to leave documentation as appropriate; another said not to add comments. Both cannot be followed.

Newer models can interpret what the user actually wants without that scaffolding. So what remains of
the scaffolding is the part that hurts: contradictory orders narrowing behavior for no gain. Removing
them is not a loss of guidance. It is unhobbling.

The second thing that changed is where context can live. Claude used to rely on CLAUDE.md as its
source of memory, information, and guidance all at once. Memory, artifacts, and skills now give Claude
its own ways of loading and sharing context across sessions — which is why CLAUDE.md no longer has to
carry everything.

## Six shifts

**1. Give Claude rules → let Claude use judgment.** The old line read: default to writing no comments,
never write multi-paragraph docstrings or multi-line comment blocks, one short line max. The new one
reads: write code that reads like the surrounding code, matching its comment density, naming, and
idiom. The prohibition was standing in for a standard; state the standard.

**2. Give Claude examples → design interfaces.** Usage examples do not merely illustrate for a newer
model — they constrain it to the exploration space the examples cover. Move the teaching into the tool
itself: expressive parameters, options enumerated clearly enough that correct usage is visible from
the signature.

**3. Put it all upfront → use progressive disclosure.** Rather than a system prompt carrying
everything that might be needed, load context selectively through skills and deferred-loading tools,
so the right guidance arrives when it is relevant.

**4. Repeat yourself → simple tool descriptions.** Instructions used to appear in the system prompt
*and* the tool description. Put them in the tool description only. Earlier models benefited from the
repetition; current models consult tool descriptions reliably, and the duplicate is one more thing to
keep in sync.

**5. Memory in CLAUDE.md files → auto-memory.** Manually pinning context with the `#` hotkey is no
longer the mechanism. Claude preserves the memories relevant to the work and to you, automatically.

**6. Simple specs → rich references.** Markdown plans are the low-fidelity option. HTML artifacts,
code references, test suites, and rubrics carry the same intent with less ambiguity, and Claude
handles increasingly complex references.

## What each layer is for now

**System prompt.** Product context: what product the agent operates within and what role it plays.
Claude Code users rarely modify it, but for a custom agent it deserves significant effort.

**CLAUDE.md.** Keep it lightweight — a description of the repository, concentrating on the gotchas
that are only discoverable by being told. When instructions get complex, move them into a separate
skill and let progressive disclosure handle the loading.

**Skills.** Lightweight guides for finding information on demand. Avoid over-constraining except where
it critically matters, and encode the opinions and best practices specific to your team or product.
Divide long skills into multiple files.

**References.** Depth, pulled in by @mention: specs, mockups, codebases. Prefer code for clarity and
fidelity over descriptive text.

## Where to start

Run `/doctor` in Claude Code (`claude doctor` from the CLI). It automatically rightsizes skills,
CLAUDE.md files, and system prompts for Claude 5 models — which is the mechanical part of the job.
Hand-editing is for what it leaves behind: the contradictions between layers, and the rules that were
written to work around a limitation the model no longer has.

Then measure. The 80% figure came with evaluations attached, and "no measurable loss" is a claim worth
being able to make about your own agent rather than assuming.

As the post puts it: you may need to simplify just like we did.

## Source

["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
— Thariq Shihipar, July 24, 2026.
