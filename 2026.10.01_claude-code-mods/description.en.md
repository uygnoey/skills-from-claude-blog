**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic introduces mods: small TypeScript functions that change how Claude Code works and looks.
A mod can rewrite a prompt, add new UI, replace a built-in feature, or add new functionality. Mods
ship inside plugins and work in the Claude Code CLI and desktop app.

## When is it useful?
- When you want Claude Code to behave your way without waiting for a feature.
- When a hook is not enough — you need to rewrite an event, draw UI, or replace a feature.
- When a team wants its own controls such as CI status, production safeguards, or audit logs.
- When admins need to govern which mods users can install.

## Key points
- Claude Code emits an event each time it does something (tool call, permission request, drawing
  part of the screen). A mod hooks an event and runs before, after, instead of, or around it.
- One function can rewrite a prompt, block/rewrite/retry a tool call, approve or deny a permission,
  or redact secrets from tool output. Mods can also edit or replace UI and add buttons and inputs,
  in the terminal, the desktop app, or both.
- Mods on the same event run in load order: the first to load sees the event first and the result
  last, so mods from different authors stack.
- Built-ins are moving to mods — `/diff` is now a mod you can turn off in `/plugin` or replace.
- Mods are not sandboxed; install only from trusted sources. Existing plugin controls apply, and on
  Team/Enterprise or managed-settings machines the built-in `sec-default` mod loads first to stop
  risky actions like overriding permission deny rules.
- Claude Code can write, install, and hot reload a mod for you.

## Bundled resources
- Skill: `plan-code-mods` — how to scope a mod (event, phase, surface, load order), decide mod vs
  hook, and govern mods for teams, with a mod design worksheet.

## Source
- https://claude.com/resources/articles/claude-code-mods
