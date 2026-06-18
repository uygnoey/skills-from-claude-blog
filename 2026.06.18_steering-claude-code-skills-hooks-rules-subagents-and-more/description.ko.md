[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Steering Claude Code: skills, hooks, subagents and more

## 이 글이 뭔가요

이 글은 Claude Code의 동작을 ‘어디에 어떤 지시를 두어야 하는지’에 대한 방법들을 정리하고, 컨텍스트 비용·지속성(컴팩션)·권한(가중치) 관점의 판단 프레임워크를 제공합니다.

## 언제 유용한가요

Claude Code를 커스터마이즈할 때, 지시문을 CLAUDE.md/Rules/Skills/Subagents/Hooks/Output styles/시스템 프롬프트 append 중 어디에 둘지 결정해야 하는 경우에 유용합니다.

## 핵심 포인트

- 7가지 방법을 다룹니다: CLAUDE.md, Rules, Skills, Subagents, Hooks, Output styles, 시스템 프롬프트 append.
- 각 방법은 로드 시점, 컴팩션 시 동작, 컨텍스트 비용이 다릅니다.
- 루트 CLAUDE.md는 200줄 이하로 유지하고, 절차는 skills로, 제약은 (path-scoped) rules로 옮기라고 권장합니다.
- subagents는 메인 스레드에 중간 결과를 남기고 싶지 않은 ‘격리된 사이드 태스크’에 적합합니다.
- hooks는 결정적 자동화/강제에 적합하며, PreToolUse는 exit code 2로 도구 호출을 차단할 수 있습니다.
- output styles는 큰 역할 변화에만 사용하고, 커스텀 작성 전 내장 스타일을 먼저 확인하라고 안내합니다.
- 여러 설정이 쌓이면 plugin으로 번들링해 공유할 수 있다고 언급합니다.

## 번들 리소스

- 방법별 비교 표(트레이드오프)
- 예시: path-scoped rule frontmatter; 서브디렉터리 CLAUDE.md 로드 방식
- hook 타입과 라이프사이클 이벤트(PreCompact, PreToolUse) 설명

## 출처

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
