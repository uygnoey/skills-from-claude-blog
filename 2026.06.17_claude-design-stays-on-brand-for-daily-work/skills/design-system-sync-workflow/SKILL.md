---
name: design-system-sync-workflow
description: A repeatable workflow to import design systems into Claude Design, keep output on-brand, and hand off designs to Claude Code without restarting from screenshots.
---

## Instructions

Follow this workflow when you want Claude Design to stay consistent with your team’s design system and keep work synchronized with Claude Code.

1) Import a design system
- Bring in one or more systems from a GitHub repo, design files, or raw uploads.
- Ensure the system includes components and guidelines Claude can reference.

2) Build with components, then validate
- Ask Claude Design to build using your components rather than inventing new ones.
- Have Claude check output against the system and correct mismatches before reviewing.

3) Sync design ↔ code
- Use /design-sync to pull your design system into Claude Design so new work starts from existing components.
- Use /design in Claude Code to create, edit, and sync design projects from the terminal.
- When the design is ready, hand it off to Claude Code so implementation continues from the design artifact (not a screenshot).

4) Export and send to downstream tools
- Export to PDF or PowerPoint when you need stable sharing artifacts.
- Send to connected apps when your workflow needs specialized editing or publishing.

## Examples

### Example: daily landing-page exploration
See [examples/landing-page-directions.md](./examples/landing-page-directions.md).

## Source

- https://claude.com/blog/claude-design-stays-on-brand-for-daily-work
