**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post explains how Brendan MacLean (MacCoss Lab, University of Washington) onboards Claude Code the same way he onboards new developers to a large, long-lived codebase: by treating context and process documentation as first-class project artifacts.

## When is it useful?
- When you need Claude Code to work effectively in a large, mature repository with lots of implicit knowledge.
- When your team rotates contributors (students, open source contributors) and you need onboarding to be repeatable.
- When you want to reduce iteration cost by keeping durable, versioned context alongside the code.

## Key points
- Maintain a separate “AI context” repository (the post’s example is `pwiz-ai`) so guidance survives branch churn and keeps improving over time.
- Put a `CLAUDE.md` at the repo root to describe environment setup and point to deeper documentation (“reference, don’t embed”).
- Build a small, reusable skill library for recurring work patterns (e.g., debugging, version control conventions, project orientation).
- Use integrations (the post mentions MCP servers) to give Claude Code access to project data like test results, exceptions, support threads, and release tags.

## Bundled resources
- None published as downloadable attachments in the post; it references project artifacts like `CLAUDE.md` and an auxiliary repository (`pwiz-ai`).

## Source
- https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development
