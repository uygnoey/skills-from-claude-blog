[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude API skill, 이제 CodeRabbit·JetBrains·Resolve AI·Warp에서

## 이 글이 뭔가요

Anthropic이 2026년 4월 29일에 공개한 발표로, CodeRabbit·JetBrains·Resolve AI·Warp가 `claude-api` skill을 번들링해, 개발자가 이미 사용 중인 도구 안에서 프로덕션 수준의 Claude API 코드를 바로 받을 수 있게 됐다는 내용입니다. 이 skill은 3월에 Claude Code에서 처음 도입됐고, 이번 발표로 사용처가 더 넓어졌습니다. 글에 따르면 skill은 어떤 agent 패턴이 적합한지, 모델 세대 사이에서 파라미터가 어떻게 바뀌는지, prompt caching을 언제 적용해야 하는지 같은 디테일을 담고 있고, Anthropic SDK가 바뀌면 자동으로 최신 상태를 유지합니다.

## 언제 유용한가요

- CodeRabbit, JetBrains/Junie, Resolve AI, Warp, Claude Code 안에서 Claude API 코드를 작성할 때, 파라미터를 일일이 찾는 대신 번들된 skill을 활용하고 싶을 때.
- 새로운 Claude 모델로 마이그레이션할 때(글은 Claude Opus 4.7을 예시로 듦) — 모델명, thinking 설정, 파라미터, beta 헤더를 가이드된 방식으로 업데이트하고 싶을 때.
- 기존 agent에 prompt caching 또는 context compaction을 도입하고 싶은데, 문서를 다시 읽지 않고 안내받고 싶을 때.
- coding agent 제품을 만들고 있고, 오픈소스 `claude-api` skill을 번들링해 사용자에게 같은 전문성을 제공하고 싶을 때.

## 핵심 포인트

- `claude-api` skill은 3월에 Claude Code에서 출시된 데 더해, 이제 CodeRabbit·JetBrains·Junie·Resolve AI·Warp에 번들됩니다.
- skill은 SDK 변경에 맞춰 Claude를 항상 최신 상태로 유지해, stale한 API 지식이 만드는 리뷰 단계 사고를 줄입니다.
- 글이 강조하는 4가지 대표 프롬프트:
  - "Improve my cache hit rate." — 많이 놓치는 prompt caching 규칙을 적용.
  - "Add context compaction to my agent." — compaction 프리미티브와 agent 패턴 가이드.
  - "Upgrade me to the latest Claude model." — 가이드된 모델 마이그레이션. Claude Code에선 `/claude-api migrate`로 실행 가능.
  - "Build a deep research agent for my industry." — Claude Managed Agents 가이드 셋업. Claude Code에선 `/claude-api managed-agents-onboard`로 실행 가능.
- coding agent 빌더용: skill은 `anthropics/skills`에서 오픈소스. 번들링 가이드 기준 약 20줄 CI 셋업으로 자동 업데이트.
- 글에 실린 고객 인용: Warp, CodeRabbit, JetBrains, Resolve AI — 흐름 유지, 리뷰 단계 사고 감소, 모델 도입 속도에 초점.

## 번들 리소스

- Skill: `skills/bundled-api-skill-usage-patterns/SKILL.md` — 글이 명시한 4가지 프롬프트와 slash command로 번들 skill을 활용하는 방법.
- Reference: `skills/bundled-api-skill-usage-patterns/references/integrations-and-quotes-from-post.md` — 발표된 통합과 고객 인용의 정리.
- Examples: `skills/bundled-api-skill-usage-patterns/examples/usage-prompts.md` — 글에 나온 4가지 예시 프롬프트를 재사용 가능한 형태로 정리.

## 출처

Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp — Anthropic, 2026년 4월 29일: <https://claude.com/blog/claude-api-skill>
