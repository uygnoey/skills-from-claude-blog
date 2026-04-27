# Template fragments quoted from the post

These fragments are the concrete pieces of generator output that the May 20, 2024 launch post quotes. They are kept here verbatim so the SKILL can refer to them without expanding inline.

## Fragment 1 — Role setting (content moderation)

> "You will be acting as a content moderator…"

The post uses this opening line as its illustration of how generated prompts begin with a clear role definition.

## Fragment 2 — Chain-of-thought scratchpad

The post describes that for complex tasks (its example is a product recommendation prompt), the generator inserts a `<scratchpad>` block where Claude is told to think before answering. The post does not print the entire scratchpad text, but it names the technique and the placement.

## Fragment 3 — XML tag for code variable (code translation)

> `Here is the code to translate: <code>{{CODE}}</code>`

The post uses this to illustrate XML-tagged variables for ambiguous or large inputs.

## Fragment 4 — Inline handlebars variable

The post mentions `{{LANGUAGE}}` as a representative inline variable for short, simple slots, used alongside the XML-tagged `<code>{{CODE}}</code>` block above.

## Fragment 5 — ZoomInfo customer testimonial

> "We built a new RAG application and reached MVP in just a few days, reducing the time it took to refine prompts by 80%."
>
> — Spencer Fox, Principal Data Scientist, ZoomInfo

The post uses this quote as its main external validation that the generator-driven workflow shortens prompt iteration.

## Source

Generate better prompts in the developer Console — Anthropic, May 20, 2024: <https://claude.com/blog/prompt-generator>
