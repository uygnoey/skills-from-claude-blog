**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Claude Code works in large codebases: Best practices and where to start

## What is this post?
This post explains patterns that help Claude Code work reliably in large codebases, and where teams should start when rolling it out at scale.

## When is it useful?
Useful when you are setting up or scaling Claude Code in a monorepo or enterprise codebase, and need conventions for context, automation, ownership, and navigation.

## Key points
- Claude Code navigates codebases agentically (file traversal + targeted search) rather than relying on a pre-built index.
- The harness (e.g., CLAUDE.md, hooks, skills, plugins, MCP, LSP, subagents) often determines real-world performance.
- Keep CLAUDE.md files lean and layered, and review them periodically as model capabilities change.
- Treat adoption as an org problem too: define ownership (DRI / agent manager) and governance early.

## Bundled resources
- Skills: 1
- Guides: 1

## Source
- https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
