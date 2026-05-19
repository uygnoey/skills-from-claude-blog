**English** · [한국어](./html-artifacts-workflows.ko.md) · [Español](./html-artifacts-workflows.es.md) · [日本語](./html-artifacts-workflows.ja.md)

# HTML artifacts workflows in Claude Code

## What is this guide?
A practical guide to using HTML files as working artifacts in Claude Code for planning, code understanding, prototyping, and reporting.

## When is it useful?
Use this when Markdown feels limiting for readability, layout, or when you want to include lightweight interactivity.

## Key points
- Prefer HTML when you want richer layout (grids/columns/callouts) and higher information density.
- For larger efforts, iterate across multiple HTML artifacts (options → mockups → implementation plan), then start a fresh session for implementation.
- For review/understanding tasks, ask for diffs rendered with inline annotations and severity color-coding.
- For “throwaway editors”, always include an export button (copy as JSON/prompt/diff/Markdown).

## Suggested workflow patterns
1. **Exploration grid**: generate multiple alternatives side-by-side.
2. **Implementation plan**: capture mockups, data-flow diagrams, and key snippets in one readable page.
3. **Explain a PR/system**: render the diff, annotate, and highlight gotchas.
4. **Prototype interactions**: add sliders/knobs to tune parameters.
5. **Purpose-built editor**: create a one-off UI that exports back into a durable format.

## Bundled resources
- Prompt templates: `../skills/html-artifacts/templates/prompt-patterns.md`

## Source
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
