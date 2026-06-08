**English** · [한국어](./foundation-models-handoff.ko.md) · [Español](./foundation-models-handoff.es.md) · [日本語](./foundation-models-handoff.ja.md)

# Designing an Apple Foundation Models → Claude handoff

This guide summarizes the integration approach described in the Claude blog post and turns it into a repeatable design checklist.

## What the post describes
- Use Apple’s Foundation Models framework from Swift for on-device tasks like summarization and extraction.
- When the user request requires more complex work, call Claude for multi-step reasoning, code generation, web search, or code execution for data analysis.
- Stream Claude’s response back into the same UI view.

## Recommended workflow structure
1. **On-device pass (fast, local)**
   - Define what to extract or summarize.
   - Prefer guided generation to produce typed Swift values.
2. **Escalation to Claude (complex)**
   - Use the typed values as clean inputs to Claude.
   - Ask Claude to perform multi-step reasoning and produce the final answer.
3. **Single UX surface**
   - Present results as one continuous interaction by streaming the Claude output back into the same view.

## Example use cases from the post
- Journaling apps: on-device daily prompts → Claude finds threads across months.
- Study apps: on-device definitions → Claude answers deeper conceptual follow-ups.

## Source
- https://claude.com/blog/claude-for-foundation-models
