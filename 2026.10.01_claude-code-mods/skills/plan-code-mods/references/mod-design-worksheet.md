# Mod design worksheet

## 1. Need
- What should change? (prompt / tool call / permission / output / UI / built-in feature / new feature)
- Could a hook do it? Hooks cannot rewrite events, draw new UI, or replace features. → If yes, use a hook.

## 2. Hook point
| Field | Answer |
|---|---|
| Event (e.g. tool call, permission request, screen drawing) | |
| Phase: before / after / instead of / wrap | |
| Surface (UI mods): terminal / desktop app / both | |
| Replaces a built-in? (e.g. `/diff`) | |

## 3. Stacking
- Other mods on the same event: ______
- Load position: first mods see the event first and the result last.
- Guard and audit mods → load first.

## 4. Trust and governance
- [ ] Source is trusted (mods are not sandboxed; same machine access as Claude Code)
- [ ] Packaged in a plugin
- [ ] Marketplace allowed by admin (admin console or managed settings)
- [ ] If admin loads custom mods first, `sec-default` is in the list

## Team patterns from the post
| Pattern | What it does | Where it hooks |
|---|---|---|
| CI/CD status | Pane beside the conversation showing pipeline status, updated as builds pass or fail | UI |
| Production safeguards | Require confirmation before any command touches production config | Tool call, before |
| Audit logging | Records every call every other mod makes | Loads first |
| Secret redaction | Removes secrets from tool output before Claude reads it | Tool output, after |
| `sec-default` | Stops user mods from risky actions like overriding permission deny rules | Built-in, loads first |
