---
name: html-artifacts
description: Use HTML artifacts (instead of Markdown) in Claude Code to produce richer, more readable, and more shareable outputs for planning, code review/understanding, prototyping, and reporting.
---

## Instructions

Use HTML files as the primary output format when you need:

- **Richer layout** than Markdown (grids, columns, callouts).
- **Higher information density** while staying readable.
- **Shareable artifacts** you can revisit later (plans, explainers, reports).
- **Light interactivity** (e.g., simple controls, live previews) where it helps decision-making.

When prompting for an HTML artifact:

1. State the purpose of the artifact and who will read it.
2. Specify the desired structure (sections, grid layout, side-by-side comparisons).
3. Ask for legibility features (headings, spacing, summaries) and, when relevant, visual encoding (e.g., color-code findings by severity).
4. If the artifact is an editor, include an explicit export mechanism (e.g., “copy as JSON”, “copy as prompt”, “copy diff”).

Recommended workflow for larger tasks:

- Create multiple HTML files for different stages (brainstorm → option exploration → mockups → implementation plan).
- Start a fresh implementation session later and provide those files as context.
- Use a verification agent to read the files when you want a broader-context review.

For more detail and ready-to-reuse prompt patterns, see:
- `templates/prompt-patterns.md`
- `guides/html-artifacts-workflows.en.md`

## Examples

### 1) Side-by-side options exploration

Use when you want multiple approaches rendered in one place for comparison.

- Prompt: See `templates/prompt-patterns.md#options-exploration-grid`

### 2) PR review / code understanding explainer

Use when you want the diff rendered with annotations and severity.

- Prompt: See `templates/prompt-patterns.md#pr-review-html-explainer`

### 3) Purpose-built “throwaway editor” with export

Use when editing structured data is painful in plain text.

- Prompt: See `templates/prompt-patterns.md#throwaway-editor-with-export`

## Source

- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
