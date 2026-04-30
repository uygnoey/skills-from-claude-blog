[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Code를 만들며 배운 것: prompt caching이 전부다

## 이 글이 뭔가요

Anthropic이 2026년 4월 30일에 공개한 글로, Claude Code 팀의 Thariq Shihipar(member of technical staff)가 Claude Code 하네스를 만들면서 익힌 prompt caching 교훈을 공유합니다. prefix 매칭이 어떻게 동작하는지, Claude Code가 정적/동적 컨텐츠를 어떤 순서로 배치하는지, 시스템 프롬프트를 즉흥적으로 수정하면 왜 캐시가 깨지는지, 세션 도중 모델·툴 변경이 왜 위험한지, Plan Mode와 tool search가 캐시를 깨뜨리지 않으면서 어떻게 동작하는지, compaction이 어떻게 cache-safe forking으로 구현되는지를 설명합니다. 마지막으로 어떤 agent 빌더든 재사용할 수 있는 5개의 패턴으로 정리합니다.

## 언제 유용한가요

- 장시간 동작하는 agent를 만들거나 운영 중이며, prompt cache hit rate를 높게 유지하는 게 목표일 때.
- 코드 변경 후 캐시 적중률이 떨어진 회귀를 디버깅 중일 때(타임스탬프, 툴 순서, 파라미터 조정 등).
- Plan Mode처럼 "툴셋을 바꿔야 할 것 같은" 기능을 설계 중인데, 캐시-세이프 대안이 필요할 때.
- compaction이나 요약을 구현 중인데, 부모의 캐시 prefix를 공유해 uncached input 요금을 피하고 싶을 때.
- cache hit rate에 대한 SLO/알람 모델을 잡고 싶을 때.

## 핵심 포인트

- prompt caching은 prefix match — prefix 안에서 무엇이든 바뀌면 그 뒤 전체가 무효화됩니다.
- Claude Code 하네스 배치: static system prompt + tools(글로벌 캐시) → CLAUDE.md(프로젝트 내 캐시) → session context(세션 내 캐시) → 대화 메시지.
- 캐시 순서가 깨지는 흔한 케이스: static system prompt에 시점성 타임스탬프 포함, 툴 정의 비결정적 순서, 툴 파라미터 변경.
- 동적 정보(현재 시간, 파일 변경 등)는 메시지로 전달 — Claude Code는 다음 user message 또는 tool result에 `<system-reminder>` 태그를 붙여 시스템 프롬프트를 수정하지 않습니다.
- 세션 도중 모델 변경 금지. Opus와 100k 토큰까지 진행했는데 Haiku로 바꾸면 Haiku용 캐시를 처음부터 다시 만들어야 해서 그냥 Opus로 답하는 것보다 비싸집니다. 꼭 바꿔야 하면 subagent에 hand-off 메시지를 준비시키세요 — Claude Code의 Explore agent(Haiku 사용)에서 이 패턴을 사용합니다.
- 세션 도중 툴 추가/제거 절대 금지. Plan Mode는 모든 툴을 유지한 채 EnterPlanMode/ExitPlanMode를 툴 자체로 사용합니다. tool search는 `defer_loading: true` 스텁을 써서 툴 제거 없이 지연 로딩합니다.
- compaction은 cache-safe forking으로 구현됩니다: 부모와 동일한 system prompt, user/system context, tools 정의 + 끝에 compaction 프롬프트를 새 user message로 추가. context window에 "compaction buffer"를 예약해 둡니다. compaction은 이제 API에 내장되어 있습니다.
- 팀은 cache hit rate를 uptime처럼 모니터링하고, 너무 떨어지면 SEV를 선언합니다.

## 번들 리소스

- Skill: `skills/agent-prompt-caching-best-practices/SKILL.md` — prefix를 안정적으로 유지하기 위한 실행 가능한 규칙과 설계 패턴을 체크리스트 형태로 정리.
- Reference: `skills/agent-prompt-caching-best-practices/references/lessons-from-claude-code.md` — 글이 제시한 교훈을 그대로 인용한 레퍼런스(레이아웃, 메시지 활용, 모델·툴 안정성, cache-safe forking, 5개 요약 패턴).
- Examples: `skills/agent-prompt-caching-best-practices/examples/cache-safe-feature-design.md` — 글에서 발췌한 구체적 예시(툴로서의 Plan Mode, tool search의 defer_loading, cache-safe forking으로서의 compaction).

## 출처

Lessons from building Claude Code: Prompt caching is everything — Anthropic(Thariq Shihipar), 2026년 4월 30일: <https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything>
