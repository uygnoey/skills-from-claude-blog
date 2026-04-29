---
name: bundled-api-skill-usage-patterns
description: Get the most out of the bundled claude-api skill (now shipping in CodeRabbit, JetBrains, Junie, Resolve AI, Warp, and Claude Code) by triggering the four post-named workflows — improving cache hit rate, adding context compaction, upgrading to the latest Claude model, and onboarding a deep research agent — instead of looking up API parameters manually.
---

# Bundled API skill usage patterns

The April 29, 2026 launch announces that the `claude-api` skill — first introduced in Claude Code in March — is now bundled in CodeRabbit, JetBrains, Junie, Resolve AI, and Warp. This skill captures how to get value out of that bundling without re-reading the docs.

## Instructions

### 1. Confirm your tool actually has the bundled skill

Per the post, the bundled `claude-api` skill ships in:

- Claude Code (since March)
- CodeRabbit
- JetBrains IDEs (and Junie)
- Resolve AI
- Warp

If your tool is not on this list, fall back to the docs at the link the post calls out (`anthropics/skills`) instead of assuming the skill is available.

The full list and the verbatim customer quotes are in [references/integrations-and-quotes-from-post.md](./references/integrations-and-quotes-from-post.md).

### 2. Use the four post-named prompts as your default starting menu

The post puts four prompts up front:

- "Improve my cache hit rate." — applies prompt-caching rules many developers miss.
- "Add context compaction to my agent." — walks you through the compaction primitives and agent patterns the docs describe.
- "Upgrade me to the latest Claude model." — reviews your code and updates model names, prompts, and effort settings for a new model (the post's example is Opus 4.7). In Claude Code, runnable directly as `/claude-api migrate`.
- "Build a deep research agent for my industry." — walks you through configuring Claude Managed Agents. In Claude Code, runnable directly as `/claude-api managed-agents-onboard`.

These prompts are reproduced as standalone reusable snippets in [examples/usage-prompts.md](./examples/usage-prompts.md).

### 3. Prefer the slash commands when you are inside Claude Code

The post explicitly names two slash commands:

- `/claude-api migrate` for the model upgrade flow.
- `/claude-api managed-agents-onboard` for the deep-research-agent flow.

When you are in Claude Code, prefer these slash commands over typing the long-form prompts — the post positions them as the direct, guided entry points for the same workflows.

### 4. Trust the skill to stay current with the SDKs

The post says: "It stays current as our SDKs change. When a new model is released or the API gains a feature, Claude already knows."

Practical implications:

- When migrating to a new Claude model, ask the skill rather than copy-pasting from older blog posts. Examples mentioned in the post for Opus 4.7: updating model references, moving manual thinking settings to adaptive thinking, cleaning up outdated parameters and beta headers, suggesting the right effort level inline.
- If the skill's behavior contradicts a stale snippet you remember, defer to the skill.

### 5. If you are building a coding agent, bundle the skill

The post tells coding-agent builders that the skill is open source at `anthropics/skills`, and that the bundling guide describes the setup in about 20 lines of CI. Updates flow automatically afterward, so the skill in your product stays current without manual maintenance.

Decision criteria from the post:

- You are building a tool where developers write Claude API code.
- You want users to get expertise around the Claude API without leaving your product.

If both are true, follow the bundling guide referenced by the post; otherwise just use the bundled skill as a consumer.

## Examples

### Example A: Lift cache hit rate on an existing agent

Inside any of the supported tools, send: "Improve my cache hit rate." The skill applies prompt-caching rules that many developers miss. Pair this with a code reference (open the file or paste the relevant snippet) so the skill has the context it needs.

### Example B: Add context compaction to a long-running agent

Inside any of the supported tools, send: "Add context compaction to my agent." The skill walks through the compaction primitives and the agent patterns documented by Anthropic.

### Example C: Migrate to Opus 4.7

In Claude Code, run `/claude-api migrate`. Outside Claude Code, send: "Upgrade me to the latest Claude model." The skill reviews your code and updates model references, thinking settings, parameters, and beta headers — the exact updates the post describes for the Opus 4.7 example.

### Example D: Onboard a deep research agent

In Claude Code, run `/claude-api managed-agents-onboard`. Outside Claude Code, send: "Build a deep research agent for my industry." The skill configures Claude Managed Agents so long-running research is, in the post's words, "a few prompts, not a custom project."

## Source

Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp — Anthropic, April 29, 2026: <https://claude.com/blog/claude-api-skill>
