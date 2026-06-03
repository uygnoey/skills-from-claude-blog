**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Lessons from building Claude Code: How we use skills

## What is this post?
This post summarizes Anthropic’s internal lessons from building and scaling hundreds of Claude Code skills, including common categories of skills and practical guidance for writing, structuring, and distributing them.

## When is it useful?
Use this when you are designing skills for Claude Code and want concrete heuristics for what to include (gotchas, references, scripts, templates), how to structure skills for progressive disclosure, and how to distribute skills via repos or plugins.

## Key points
- Skills are folders (not just a markdown file) and can include scripts, assets, data, and configuration.
- Internally, Anthropic observed nine broad “skill categories”; skills that stay within one category tend to work best.
- The highest-signal part of a skill is often a “Gotchas” section built from real failures.
- Skills can be shared by checking them into `./.claude/skills` or by distributing plugins via a marketplace.
- Hooks can be activated on-demand (only when a skill triggers) to avoid being disruptive.

## Bundled resources
- A reusable checklist-style guide for skill design and structure.
- A reference list of skill categories and examples.

## Source
- https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
