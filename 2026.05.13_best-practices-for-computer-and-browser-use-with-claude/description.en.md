**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Best practices for computer and browser use with Claude

## What is this post?
A practical set of recommendations for building reliable “computer use” and “browser use” automations with Claude, focused on screenshot sizing, coordinate handling, prompt formatting, reliability tuning, safety, and long-running context management.

## When is it useful?
- When you are building an agent that clicks/types in a UI using screenshots.
- When click accuracy is inconsistent (offset clicks, near-misses, wrong element).
- When you need guidance on downscaling, zoom, thinking effort, caching, and compaction for long sessions.
- When you are designing mitigations against prompt injection for agents operating on the open web.

## Key points
- Downscale screenshots before sending them, with a sensible default like 1280×720 (or start at 1080p for Opus 4.7).
- If you resize screenshots, you must scale the model’s returned coordinates back to native screen space before executing clicks.
- Put the text instruction before the image block in the message content.
- Use zoom or keyboard navigation for small targets; avoid overly low resolutions.
- Tune “thinking effort” by model family and scenario; consider orchestrator+executor patterns for planning vs. mechanical steps.
- Treat web content as untrusted; prefer built-in prompt injection classifiers, scope permissions, log actions, and add human confirmation for irreversible steps.
- For long-running agents, use cache breakpoints, prune old screenshots, and consider server-side compaction.

## Bundled resources
This folder includes:
- A reusable Agent Skill with checklists and implementation guidance.
- Companion scripts for screenshot preparation, coordinate scaling, cache-control placement, and screenshot pruning.
- A reference of recommended defaults and “things that didn’t help” during optimization.

## Source
Claude blog: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
