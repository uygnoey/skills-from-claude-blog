**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
An announcement of **inference hooks**, a Claude Enterprise security feature that adds inline data loss prevention (DLP). Every inference request is routed over a signed WebSocket connection to a security server the organization controls. Before the model starts generating, Claude sends the prompt and its surrounding context to that server, waits for an allow/deny verdict, and only then proceeds. The same check runs on tool call responses before they are returned to the model.

Previously, native inline enforcement was limited to Claude Code's client-side hooks. Inference hooks extend a single enforcement layer across Claude Enterprise surfaces — chat, Claude Code, Claude Cowork, and tool calls made through MCP connectors, skills, and plugins — without per-product integration work.

## When is it useful?
- When a security or compliance team requires every channel that can move sensitive data to pass through an inspection point they control.
- When an existing DLP program (Netskope, Palo Alto Networks, Proofpoint, Zscaler, or an in-house server) should also cover AI usage.
- When you need one organization-level configuration instead of separate integrations per Claude product.
- When you are planning a staged rollout and need shadow mode, exclusions, and percentage ramps before enforcing.

## Key points
- **Pre-generation inspection.** The prompt and context go to your server before the model generates; Claude proceeds only after a verdict.
- **Tool responses are inspected too**, including tools reached through MCP connectors, skills, and plugins.
- **Open, webhook-based protocol with a published schema**, so an existing DLP server can be reused and security vendors can build integrations.
- **One org-level switch** covers Claude Enterprise surfaces rather than one integration per product.
- **Rollout controls**: shadow mode (always allow), role-based exclusions, percentage-based rollouts, plus configurable failure policy and timeouts.
- Available **in beta for Claude Enterprise** customers at the time of the post.
- Note the naming overlap: these are *server-side inference hooks*, not Claude Code's client-side lifecycle hooks (PreToolUse, PostToolUse, and so on).

## Bundled resources
- `skills/inference-dlp-rollout/SKILL.md` — a staged rollout procedure for turning on inline DLP without breaking users.
- `skills/inference-dlp-rollout/references/enforcement-model.md` — where inspection happens and what each control does.
- `skills/inference-dlp-rollout/templates/rollout-plan.md` — a fill-in rollout and decision-log template.
- `guides/inline-dlp-for-claude-enterprise.{en,ko,es,ja}.md` — the architecture and deployment guide in four languages.

## Source
- https://claude.com/blog/claude-enterprise-inference-hooks
