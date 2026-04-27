**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Generate better prompts in the developer Console

## What is this post?

Anthropic's May 20, 2024 announcement introduces a prompt generator inside the Anthropic Console that turns a short task description into a production-ready prompt template. The generator bakes in prompt-engineering techniques — clear role setting, chain-of-thought scratchpads, XML tags around ambiguous variables, and inline simple variables — so developers do not have to apply these patterns manually each time they start a new project.

## When useful

- You are starting a new Claude-powered feature and need a strong first draft prompt.
- You want a consistent template style across teams that already encodes Anthropic's prompt-engineering best practices.
- You are migrating an existing prompt to the Console and want a baseline to compare against.
- You are building an evaluation set and need a clean separation between fixed instructions and per-example variables.

## Key points

- Generated prompts include explicit role setting (for example, "You will be acting as a content moderator").
- Complex tasks are scaffolded with a chain-of-thought `<scratchpad>` block where Claude is told to think before answering.
- Ambiguous or large variables are wrapped in XML tags such as `<code>{{CODE}}</code>` to make boundaries unambiguous.
- Simple short variables can be referenced inline, for example `{{LANGUAGE}}`.
- Variables use handlebars notation so the same template plugs into the Console workbench and downstream tooling.
- Behind the scenes, the generator runs a long meta-prompt that plans the structure first and uses XML tags as a "spine" for the output.
- ZoomInfo is featured as a customer; Spencer Fox, Principal Data Scientist at ZoomInfo, says the team reached MVP in just a few days, reducing prompt-refinement time by 80%.

## Bundled resources

- Skill: `skills/prompt-template-bootstrap/SKILL.md` — when to use the generator, what techniques the output already carries, and how to edit and evaluate it.
- Reference: `skills/prompt-template-bootstrap/references/best-practices-from-post.md` — the prompt-engineering techniques the post says are baked into the generator.
- Examples: `skills/prompt-template-bootstrap/examples/template-fragments.md` — verbatim template fragments the post quotes (content moderator role, scratchpad recommendation, code translation XML, ZoomInfo testimonial).

## Source

Generate better prompts in the developer Console — Anthropic, May 20, 2024: <https://claude.com/blog/prompt-generator>
