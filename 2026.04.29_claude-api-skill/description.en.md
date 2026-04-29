**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp

## What is this post?

Anthropic's April 29, 2026 announcement reports that CodeRabbit, JetBrains, Resolve AI, and Warp are now bundling the `claude-api` skill, putting production-ready Claude API code inside the tools developers already use. The post says the skill — first introduced in Claude Code in March — captures details that make Claude API code work well, such as which agent pattern fits a given job, what parameters change between model generations, and when to apply prompt caching. It stays current as Anthropic's SDKs evolve, so as soon as a new model or API feature ships, Claude already knows.

## When useful

- You write Claude API code inside CodeRabbit, JetBrains/Junie, Resolve AI, Warp, or Claude Code, and want to leverage the bundled skill instead of looking parameters up manually.
- You are migrating to a newer Claude model (the post calls out Claude Opus 4.7) and want guided help updating model names, thinking settings, parameters, and beta headers.
- You want to apply prompt caching or context compaction to an existing agent without re-reading the docs from scratch.
- You are building a coding agent product and want to bundle the open-source `claude-api` skill so your users get the same expertise.

## Key points

- The `claude-api` skill is now bundled in CodeRabbit, JetBrains, Junie, Resolve AI, and Warp — in addition to Claude Code where it launched in March.
- The skill keeps Claude current as the SDKs change, reducing review-time surprises caused by stale API knowledge.
- Four representative prompts the post highlights:
  - "Improve my cache hit rate." — applies prompt-caching rules many developers miss.
  - "Add context compaction to my agent." — walks through compaction primitives and agent patterns.
  - "Upgrade me to the latest Claude model." — guided model migration; in Claude Code, runnable as `/claude-api migrate`.
  - "Build a deep research agent for my industry." — guided Claude Managed Agents setup; in Claude Code, runnable as `/claude-api managed-agents-onboard`.
- For coding-agent builders: the skill is open source at `anthropics/skills`; the bundling guide describes the setup in about 20 lines of CI, with automatic updates.
- Customer testimonials in the post: Warp, CodeRabbit, JetBrains, and Resolve AI — focused on staying in flow, fewer review-time surprises, and faster model adoption.

## Bundled resources

- Skill: `skills/bundled-api-skill-usage-patterns/SKILL.md` — the four post-named prompts and slash commands for working with the bundled skill.
- Reference: `skills/bundled-api-skill-usage-patterns/references/integrations-and-quotes-from-post.md` — verbatim summary of the integrations announced and the customer quotes.
- Examples: `skills/bundled-api-skill-usage-patterns/examples/usage-prompts.md` — the post's four illustrative prompts kept as a reusable reference.

## Source

Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp — Anthropic, April 29, 2026: <https://claude.com/blog/claude-api-skill>
