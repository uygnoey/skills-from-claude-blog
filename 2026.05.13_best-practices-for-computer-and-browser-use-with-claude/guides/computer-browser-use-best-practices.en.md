**English** · [한국어](./computer-browser-use-best-practices.ko.md) · [Español](./computer-browser-use-best-practices.es.md) · [日本語](./computer-browser-use-best-practices.ja.md)

# Best practices guide: Claude computer and browser use

This guide summarizes recommended defaults and debugging tactics for building reliable computer/browser use agents with Claude.

## 1) Image sizing and scaling
- Downscale screenshots before sending them.
- A simple default is 1280×720; for Opus 4.7, start at 1080p.
- Avoid very low resolutions (< ~960×540).
- If you need max fidelity under limits, compute a “max API fit” size that preserves aspect ratio.

## 2) Coordinate correctness
If you resized screenshots, scale API-returned coordinates back to native screen coordinates before executing clicks.

## 3) Message formatting
Put the text instruction before the image block in the message content.

## 4) Small targets
- Enable zoom for dense UIs.
- Prefer keyboard navigation when targets are tiny.
- For 4K+ screens, either use Opus 4.7 (higher image budget) or reduce DPI / focus the screenshot to the relevant region.

## 5) Thinking effort (computer use)
- Opus 4.7: default `high`; use `low` for throughput/cost; consider `max` only for very difficult one-shot tasks.
- Claude 4.6: default `medium`; use `low` for throughput/cost; disable thinking only for simple workflows where latency is priority.

## 6) Prompt injection safety
- Treat all web content as untrusted.
- Prefer built-in classifiers via `computer_20251124`.
- Require human confirmation for irreversible actions.
- Scope permissions and keep detailed logs.

## 7) Long-running context management
A practical default from the post:
- One cache breakpoint on the stable prefix, plus three on trailing tool results.
- Rolling buffer pruning for screenshots (e.g., keep_n=3, prune every ~25 screenshots).
- Server-side compaction triggered around ~150k input tokens with a custom compaction prompt.

## Source
https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
