**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces Code Review in Claude Code: an automated pull request review feature that dispatches multiple agents to look for bugs and issues, and posts a consolidated review back on the PR.

## When is it useful?
- When you want deeper, more thorough review coverage than lightweight linters or quick LLM skims.
- When you want consistent review feedback on every PR, while keeping the final approval decision with humans.

## Key points
- A team of agents is dispatched on every PR; review depth scales with PR size and complexity.
- Results arrive as a single overview comment plus inline comments.
- It is designed for depth (and is correspondingly more expensive than lighter-weight options).
- The feature does not approve PRs; humans still decide whether to merge.

## Bundled resources
- Skill: "Automated PR review with agent teams" (derived from the post’s described workflow and admin/developer setup).

## Source
- https://claude.com/blog/code-review
