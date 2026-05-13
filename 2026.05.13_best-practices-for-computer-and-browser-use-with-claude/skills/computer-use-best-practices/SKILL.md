---
name: computer-use-best-practices
description: Best practices and reusable helpers for building reliable Claude computer/browser use agents: screenshot sizing, coordinate scaling, message ordering, small-target handling, safety, and long-running context management.
---

## Instructions
Use this skill when you are implementing an agent that operates a UI via screenshots (computer use / browser use) and you need reliability, cost, and safety guardrails.

### 1) Screenshot sizing (downscaling)
- Downscale screenshots before sending them to the API.
- Start with 1280×720 as a simple default; for Opus 4.7 start at 1080p.
- Avoid extremely low resolutions (below ~960×540) and avoid sending native 4K.
- If you want maximum fidelity within limits, compute a “max API fit” resolution that preserves aspect ratio.

Implementation helpers:
- `scripts/screenshot_pipeline.py` (prepare_screenshot + compute_max_api_fit)

### 2) Coordinate scaling
If you resized the screenshot before sending it, scale the API-returned coordinates back to native screen space before executing the click.

Implementation helpers:
- `scripts/screenshot_pipeline.py` (scale_coordinates)

### 3) Message ordering
When sending a text instruction with an image, put the text block before the image block in the message content.

### 4) Small targets
- Use zoom for dense UIs (tool config).
- Prefer keyboard navigation (tab, shortcuts) for tiny targets.
- If you control the UI, increase target size via scaling/zoom.

Reference:
- `references/small-targets.md`

### 5) Thinking effort defaults
Use model-appropriate defaults for computer use:
- Opus 4.7: default `high`
- Claude 4.6 family: default `medium`

Reference:
- `references/thinking-effort.md`

### 6) Prompt injection safety
Treat all web content as untrusted:
- Use built-in prompt injection classifiers via `computer_20251124`.
- Require human confirmation before irreversible actions.
- Scope permissions and log actions.

Reference:
- `references/prompt-injection-safety.md`

### 7) Long-running context management
- Use cache breakpoints: one on a stable prefix, plus up to three on recent tool results.
- Prune old screenshots in batches; consider server-side compaction for very long sessions.

Implementation helpers:
- `scripts/cache_helpers.py` (set_trailing_cache_control)
- `scripts/prune_helpers.py` (prune_old_screenshots)
- `templates/compact_prompt.txt` (example compaction prompt)

### 8) What did not help (avoid wasting time)
See `references/optimization-myths.md`.

## Examples
### Example: prepare screenshot + send instruction before image
See `examples/python_api_example.md`.

### Example: enable zoom for dense UIs
See `examples/enable_zoom_snippet.md`.

## Source
https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
