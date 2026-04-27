---
name: prompt-template-bootstrap
description: Use Anthropic Console's prompt generator to bootstrap a production-ready prompt template from a short task description, then know what prompt-engineering techniques the output already carries (role setting, chain-of-thought scratchpad, XML tags, handlebars variables) and how to edit, version, and evaluate the result.
---

# Prompt template bootstrap

The May 20, 2024 launch post introduces a prompt generator inside the Anthropic Console. It turns a short task description into a structured prompt template that already follows Anthropic's prompt-engineering best practices. This skill documents how to lean on it without losing track of what is being applied for you.

## Instructions

### 1. Decide whether the generator is the right starting point

Use the generator when:

- You have a new task and want a strong first draft instead of writing the prompt from scratch.
- You want a consistent, opinionated baseline that already includes role setting, chain-of-thought, and XML-tagged variables.
- You are bootstrapping a Console workbench session and need a template that plugs directly into Console variable management.

Skip the generator when the post does not describe a matching scenario, for example purely conversational chit-chat with no task structure. Do not invent capabilities the post does not mention.

### 2. Recognize the techniques baked into the output

The post explicitly lists the techniques the generator applies. Treat these as features of the output, not your own additions:

- Role setting at the top of the prompt (e.g., "You will be acting as a content moderator…").
- A chain-of-thought `<scratchpad>` block where Claude is told to think before answering.
- XML tags around ambiguous or large variables, for example `<code>{{CODE}}</code>`.
- Inline handlebars references for short, simple variables, for example `{{LANGUAGE}}`.
- A meta-prompt running behind the scenes that first plans the structure and uses XML tags as a "spine" for the output.

The full quoted descriptions are in [references/best-practices-from-post.md](./references/best-practices-from-post.md).

### 3. Edit the generated template, do not rewrite it

When you tweak the output, preserve the structure the generator chose:

- Keep the role-setting paragraph; refine wording, do not delete it.
- Keep `<scratchpad>` if it is present; if you remove it, you are removing the chain-of-thought scaffolding the post recommends.
- Keep XML tags around long or ambiguous slots. Replace placeholder names but keep the tag pair.
- Keep handlebars variables (`{{NAME}}`) so the template remains compatible with the Console workbench.

### 4. Use the template as the seed for evaluations

Because the template cleanly separates fixed instructions from per-example variables, it is well suited to be the system prompt of an evaluation set:

- Hold the system prompt fixed.
- Vary only the handlebars variables across evaluation rows.
- Compare outputs against expected behavior described in the role-setting paragraph.

### 5. Treat the customer evidence as evidence, not as numbers to repeat blindly

ZoomInfo is featured as a customer in the post. Spencer Fox, Principal Data Scientist at ZoomInfo, is quoted as saying the team reached MVP in just a few days, reducing prompt-refinement time by 80%. Cite this when justifying the approach internally; do not generalize it to your own workload without measuring.

## Examples

### Example A: Bootstrap a content moderation prompt

The post quotes a generated content moderation template that begins with role setting:

> "You will be acting as a content moderator…"

Workflow:

1. In the Console prompt generator, describe the task as "Moderate user comments for a community forum."
2. Inspect the output. Confirm it opens with a role-setting paragraph and that it wraps the input comment in an XML tag.
3. Edit the role description to match your community policy, but keep the structure.

The verbatim quote and additional template fragments from the post are in [examples/template-fragments.md](./examples/template-fragments.md).

### Example B: Bootstrap a code translation prompt

The post highlights that ambiguous or large variables are wrapped in XML tags such as `<code>{{CODE}}</code>` for a code translation task:

> "Here is the code to translate: <code>{{CODE}}</code>"

Workflow:

1. Describe the task as "Translate code between programming languages."
2. Confirm the generated template uses an XML tag around the code variable and uses an inline handlebars variable like `{{LANGUAGE}}` for the target language.
3. Use the template directly in the Console workbench; vary `{{CODE}}` and `{{LANGUAGE}}` across evaluation rows.

### Example C: Bootstrap a product recommendation prompt

The post notes that for complex tasks the generator inserts a `<scratchpad>` block where Claude is told to think before answering. For a product recommendation example, this lets Claude brainstorm options before committing.

Workflow:

1. Describe the task as "Recommend products from our catalog given a user request."
2. Confirm the generated template includes a `<scratchpad>` step where Claude considers multiple candidate products before producing the final answer.
3. If you ever feel tempted to remove the scratchpad to "save tokens", remember the post explicitly attributes recommendation quality to having that thinking step.

## Source

Generate better prompts in the developer Console — Anthropic, May 20, 2024: <https://claude.com/blog/prompt-generator>
