# Prompt-engineering best practices baked into the generator

This reference reproduces the prompt-engineering techniques the May 20, 2024 launch post says the Console prompt generator applies on your behalf.

## 1. Role setting

The post calls out that generated prompts begin with a clear role definition. The example given is a content moderation prompt that opens with:

> "You will be acting as a content moderator…"

The takeaway from the post: a role-setting paragraph at the top of the prompt grounds Claude's behavior for the rest of the template.

## 2. Chain-of-thought via `<scratchpad>`

The post highlights that for complex tasks the generator inserts a `<scratchpad>` block where Claude is told to think before answering. The product recommendation example uses this to let Claude brainstorm candidate products before committing to a final list.

The takeaway from the post: chain-of-thought is implemented as a structural element of the template, not as an afterthought.

## 3. XML tags around ambiguous or large variables

The post notes that ambiguous or large variables are wrapped in XML tags. The code translation example shows:

> `<code>{{CODE}}</code>`

The takeaway from the post: XML tags act as unambiguous boundaries for big or ambiguous slots so Claude does not confuse them with the surrounding instructions.

## 4. Inline handlebars variables for simple slots

For short, simple variables, the generator uses inline handlebars references. The post mentions `{{LANGUAGE}}` as a representative example.

The takeaway from the post: not every variable needs an XML wrapper — short, single-token slots stay inline.

## 5. Meta-prompt with planning and an XML "spine"

Behind the scenes, the post says the generator runs a long meta-prompt that:

- Includes examples of well-structured prompts.
- Plans the template's structure first, before writing any of it.
- Uses XML tags as a "spine" that holds the output together.

The takeaway from the post: the techniques above are not heuristics layered after the fact — they emerge from how the meta-prompt itself is engineered.

## Customer evidence cited in the post

ZoomInfo is featured as a launch customer. Spencer Fox, Principal Data Scientist at ZoomInfo, is quoted:

> "We built a new RAG application and reached MVP in just a few days, reducing the time it took to refine prompts by 80%."

Treat this as the post's anecdotal proof point that the techniques above pay off in practice.

## Source

Generate better prompts in the developer Console — Anthropic, May 20, 2024: <https://claude.com/blog/prompt-generator>
