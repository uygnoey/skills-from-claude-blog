**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces that Claude Opus 4.6 and Claude Sonnet 4.6 now support a full 1M-token context window at generally available (GA) status on the Claude Platform.

## When is it useful?
Use this when you need to analyze or reference very large inputs in a single request (e.g., large codebases, long legal documents, big diffs, long-running agent traces, large PDFs, datasets, and many images) without engineering around shorter context limits.

## Key points
- 1M context is GA for Opus 4.6 and Sonnet 4.6.
- Standard pricing applies across the full 1M window (no long-context premium).
- Standard rate limits apply across the full window.
- Media limits increase to up to 600 images or PDF pages per request (up from 100).
- Requests over 200K tokens work without a beta header; if you already send the beta header, it is ignored.
- 1M context is also available in Claude Code for Max, Team, and Enterprise users with Opus 4.6.

## Bundled resources
- Skill: Guidance for using 1M-context models effectively (use-case framing, operational considerations).

## Source
- https://claude.com/blog/1m-context-ga
