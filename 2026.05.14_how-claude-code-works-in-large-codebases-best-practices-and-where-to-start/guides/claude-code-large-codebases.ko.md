[English](./claude-code-large-codebases.en.md) · **한국어** · [Español](./claude-code-large-codebases.es.md) · [日本語](./claude-code-large-codebases.ja.md)

# Guide: Rolling out Claude Code in large codebases

## 개요
이 가이드는 원문을 바탕으로, 대규모 레포에서 Claude Code를 효과적으로 도입·확대하기 위한 실천 항목을 정리합니다.

## 적용 방법
- Start Claude Code sessions from the relevant subdirectory, not the repo root.
- Keep a lean root CLAUDE.md for global conventions, and add subdirectory CLAUDE.md files for local rules.
- Use deterministic tooling (hooks/scripts) for formatting, linting, and other checks instead of relying on memory.
- Use skills for specialized workflows to keep the default session context small.
- Establish clear ownership (DRI/agent manager) for configuration, permissions, and rollout governance.

## 체크리스트
- Root CLAUDE.md exists and is concise.
- Key subdirectories have their own CLAUDE.md with local conventions.
- Generated/build/vendor paths are excluded via ignore files and permissions rules.
- At least one hook enforces deterministic checks (format/lint/test) where applicable.
- A DRI is named for maintaining Claude Code configuration and reviewing it every 3–6 months.

## 출처
- https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
