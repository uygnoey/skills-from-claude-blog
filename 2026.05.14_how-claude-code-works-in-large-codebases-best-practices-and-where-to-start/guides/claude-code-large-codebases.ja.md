[English](./claude-code-large-codebases.en.md) · [한국어](./claude-code-large-codebases.ko.md) · [Español](./claude-code-large-codebases.es.md) · **日本語**

# Guide: Rolling out Claude Code in large codebases

## 概要
本ガイドは原文に基づき、実行しやすい形に要点を整理します。

## 適用方法
- Start Claude Code sessions from the relevant subdirectory, not the repo root.
- Keep a lean root CLAUDE.md for global conventions, and add subdirectory CLAUDE.md files for local rules.
- Use deterministic tooling (hooks/scripts) for formatting, linting, and other checks instead of relying on memory.
- Use skills for specialized workflows to keep the default session context small.
- Establish clear ownership (DRI/agent manager) for configuration, permissions, and rollout governance.

## チェックリスト
- Root CLAUDE.md exists and is concise.
- Key subdirectories have their own CLAUDE.md with local conventions.
- Generated/build/vendor paths are excluded via ignore files and permissions rules.
- At least one hook enforces deterministic checks (format/lint/test) where applicable.
- A DRI is named for maintaining Claude Code configuration and reviewing it every 3–6 months.

## 出典
- https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
