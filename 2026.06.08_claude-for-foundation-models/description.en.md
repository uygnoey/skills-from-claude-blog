**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude support for Apple’s Foundation Models framework

## What is this post?
Anthropic describes a new Swift package that connects Apple’s Foundation Models framework to Claude, letting developers route simple tasks to on-device models and hand off more complex requests to Claude.

## When is it useful?
- When you want fast, private, on-device summarization or extraction, but need a seamless fallback to a larger model for multi-step reasoning.
- When you want typed Swift outputs (via Apple’s guided generation) to become clean, structured inputs to a Claude API call.

## Key points
- Use Apple’s Foundation Models framework for quick local tasks (e.g., summarization, extraction), then escalate to Claude for multi-step reasoning, code generation, web search, and code execution.
- Keep the experience unified by streaming Claude’s response back into the same UI view.
- Typed outputs produced by guided generation reduce reliance on raw user text when calling Claude.

## Bundled resources
- A reusable Agent Skill that documents the “on-device first, then Claude” handoff pattern for Apple Foundation Models apps (see `skills/foundation-models-handoff/SKILL.md`).
- A plugin bundle scaffold that packages the skill for distribution (see `plugin/.claude-plugin/plugin.json`).

## Source
- https://claude.com/blog/claude-for-foundation-models
