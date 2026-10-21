---
name: plan-code-mods
description: Plan, scope, and safely adopt Claude Code mods — small TypeScript functions, shipped inside plugins, that hook Claude Code events (tool calls, permission requests, screen drawing) to run before, after, instead of, or around them. Covers choosing a mod versus a hook, event phases, load-order stacking, UI changes in the terminal and desktop app, replacing built-in features such as /diff, team and enterprise controls (marketplace allow/block lists, managed settings, the sec-default mod), and trust rules for installing mods. Use when someone wants to customize Claude Code behavior or UI, write or install a mod, or govern mods across a team.
---

## Purpose
Mods change how Claude Code works and looks. A mod can rewrite a prompt, add new UI, replace a
built-in feature, or add entirely new functionality. This skill helps decide what a mod should do,
where it hooks in, how it interacts with other mods, and how to roll it out safely. It follows the
announcement post; for the actual TypeScript API, see the official mods documentation and getting
started guide.

## When to use
- A user wants Claude Code to behave differently without waiting for a new feature.
- A hook is not enough: the change must rewrite an event, draw new UI, or replace a feature.
- A team wants its own controls (CI status, production safeguards, audit logging).
- An admin needs to govern which mods users may install.

## Instructions

1. **Check trust first.** Mods run with the same access to the machine as Claude Code itself and are
   not sandboxed. Only install mods from sources you trust, as with any code.

2. **Mod or hook?** Hooks give some control, but cannot rewrite events, draw new UI, or replace
   features. If the need is any of those, use a mod.

3. **Pick the event.** Claude Code emits an event each time it does something — for example calling a
   tool, asking for permission, or drawing part of the screen. Name the event the mod hooks into.

4. **Pick the phase.** A mod runs *before* the event, *after* it, *instead of* it, or *wraps* it
   (code before and after). Typical one-function mods:
   - Rewrite a prompt before it reaches the model.
   - Block, rewrite, or retry a tool call.
   - Approve or deny a permission request.
   - Redact secrets from tool output before Claude reads it.

5. **Decide the surface (if UI).** A mod can edit or replace part of the interface, such as a tool
   result or a question from Claude, and add buttons and inputs that other mods can respond to.
   Target the terminal, the desktop app, or both.

6. **Plan load order.** When several mods hook the same event, they run in load order. The first mod
   to load sees the event first and the result last. Put guard or logging mods first.

7. **Replace instead of add, where possible.** Some built-in features ship as mods — e.g. `/diff`.
   Turn a built-in off in `/plugin` or replace it with your own version.

8. **Let Claude write it.** Ask Claude Code to create the mod; it can write the TypeScript, install
   it, and hot reload it in the session.

9. **Package and share.** Mods ship inside plugins. Install from the Claude directory or with
   `/plugin` in the CLI. To share, package the mod in a plugin and submit it to the directory.

10. **Govern for teams.** Existing plugin controls apply: admins allow or block plugin marketplaces
    (admin console on Team/Enterprise; managed settings on Claude API and third-party API plans).
    With Team/Enterprise or managed settings, the built-in `sec-default` mod loads first and stops
    user-installed mods from risky actions such as overriding permission deny rules. Admins may load
    their own mods first instead — if so, add `sec-default` to the list to keep its restrictions.

11. Fill in [references/mod-design-worksheet.md](./references/mod-design-worksheet.md) before
    building; see it for the team patterns from the post.

## Examples

**Redact secrets from tool output**
- Event: tool call result. Phase: after. Effect: strip secrets before Claude reads the output.
- Load early so later mods also see redacted output.

**Production safeguard**
- Event: tool call (shell command). Phase: before. Effect: require confirmation when a command
  touches production config.

**CI/CD status pane**
- Surface: a pane beside the conversation (desktop app) showing pipeline status, updated as builds
  pass or fail.

**Audit logging for an enterprise**
- A mod that loads first records every call every other mod makes. Keep `sec-default` in the
  admin load list.
