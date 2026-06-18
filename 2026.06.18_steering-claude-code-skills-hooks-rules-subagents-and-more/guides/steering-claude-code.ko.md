[English](./steering-claude-code.en.md) · **한국어** · [Español](./steering-claude-code.es.md) · [日本語](./steering-claude-code.ja.md)

# Claude Code 지시문 배치(steering) 프레임워크

## 요약

Claude Code에는 지시문을 둘 수 있는 여러 위치가 있고, 각각 로드 시점/컴팩션/컨텍스트 비용/권한이 다릅니다.

## 7가지 방법

이 글은 CLAUDE.md, Rules, Skills, Subagents, Hooks, Output styles, 시스템 프롬프트 append를 다룹니다.

## 실전 가이드

- 루트 CLAUDE.md는 200줄 이하로 유지하고(오너 지정 + 코드처럼 리뷰) ‘항상 필요한 사실’만 둡니다.
- 폴더 한정 규칙은 서브디렉터리 CLAUDE.md로 둡니다.
- 제약은 rules에 두고, 가능하면 path-scoped rules로 범위를 제한합니다.
- 절차(배포, 릴리스, 리뷰)는 skills로 옮깁니다.
- 메인 스레드를 더럽히기 싫은 사이드 태스크는 subagents로 격리합니다.
- 결정적 자동화/강제는 hooks로 구현합니다.
- output styles는 큰 역할 변화에만 사용하고, 커스텀 전에 내장 스타일을 확인합니다.
- append-system-prompt는 1회성 추가 지시(톤/형식)에 사용합니다.

## 출처

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
