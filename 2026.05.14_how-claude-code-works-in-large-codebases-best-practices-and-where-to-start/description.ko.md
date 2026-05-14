[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Claude Code works in large codebases: Best practices and where to start

## 이 글이 뭔가요
이 글은 Claude Code가 대규모 코드베이스에서 안정적으로 동작하도록 만드는 구성/도구/조직 패턴과, 어디서부터 시작해야 하는지 설명합니다.

## 언제 유용한가요
모노레포/엔터프라이즈 코드베이스에서 Claude Code를 도입·확대하며 컨텍스트, 자동화, 책임 구조, 네비게이션 규칙을 정립해야 할 때 유용합니다.

## 핵심 포인트
- Claude Code navigates codebases agentically (file traversal + targeted search) rather than relying on a pre-built index.
- The harness (e.g., CLAUDE.md, hooks, skills, plugins, MCP, LSP, subagents) often determines real-world performance.
- Keep CLAUDE.md files lean and layered, and review them periodically as model capabilities change.
- Treat adoption as an org problem too: define ownership (DRI / agent manager) and governance early.

## 번들 리소스
- Skills: 1
- Guides: 1

## 출처
- https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
