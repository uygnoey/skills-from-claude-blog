**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Anthropic opens plugins as the main way for developers to build third-party extensions for Claude.
A plugin packages MCP connectors, Agent Skills, or both, and approved plugins are listed in the
Claude directory. A submission portal is now open to developers on paid Claude plans.

## When is it useful?
- When deciding whether to ship a single MCP connector or a full plugin bundle.
- When preparing a submission and wanting to know what review checks.
- When planning how to measure a listing after it goes live.

## Key points
- Two paths: a single MCP connector (point to a remote MCP server) or a GitHub-hosted plugin bundle
  of MCP servers and skills. Claude Code bundles can also include LSPs, commands, hooks, and agents.
- Submissions are auto-validated and safety-scanned; the portal shows review status, scan results,
  and recommended changes. After approval the developer chooses when to publish.
- Analytics: installs by product surface and version; discovery metrics show listing views and the
  searches that lead to them.
- Claude supports the latest MCP spec (stateless core) plus MCP Apps (interactive UI in chat) and
  Enterprise Managed Auth (zero-touch OAuth for enterprise users).
- One discovery experience is coming to Claude and Claude Code; existing skills, connectors, and
  plugins need no changes, and connector listings can later be turned into plugins.

## Bundled resources
- Skill: `plugin-directory-submission` — choosing a submission path, review lifecycle, publishing,
  analytics, MCP 2.0 extensions (`references/submission-portal.md`).

## Source
- https://claude.com/resources/articles/build-plugins-for-claude
