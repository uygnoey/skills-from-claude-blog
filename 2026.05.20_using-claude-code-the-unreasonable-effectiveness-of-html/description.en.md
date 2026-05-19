**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Using Claude Code: The unreasonable effectiveness of HTML

## What is this post?
This post explains why a member of the Claude Code team prefers generating **HTML files** (instead of Markdown) when using Claude Code, and outlines practical ways to use HTML as a richer, more readable, and more shareable medium for AI-assisted work.

## When is it useful?
- When you want outputs that are easier to read and skim than Markdown.
- When you need richer layouts (grids, columns, callouts), diagrams (SVG), or embedded interactivity.
- When you want artifacts that are easy to share and revisit later (e.g., planning explorations, PR review explainers, incident reports).
- When a purpose-built “throwaway editor” would make it easier to edit structured data and export it back into Claude Code (e.g., copy as JSON/prompt/diff).

## Key points
- HTML is framed as a “richer canvas” that improves information density, readability, and shareability compared to Markdown.
- A productive workflow is to iterate across multiple HTML artifacts (brainstorm → options exploration → mockups → implementation plan), then start a fresh session for implementation using those artifacts as context.
- HTML artifacts can be especially useful for code review/understanding (render diffs, annotate, color-code findings), for design prototyping, and for research/reporting.
- For custom editing interfaces, end with an export button (e.g., “copy as JSON”, “copy as prompt”, “copy diff”) so the result can be pasted back into Claude Code or committed to a file.

## Bundled resources
- Skill: `skills/html-artifacts/SKILL.md`
- Guide: `guides/html-artifacts-workflows.*.md`

## Source
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
