[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Code w/ Claude SF 2026: AI 지수곡선 위에서 만들기

## 이 글이 뭔가요

Anthropic이 2026년 5월 12일에 공개한 연례 개발자 콘퍼런스 Code w/ Claude SF 후기입니다. Claude Code rate limit 2배 인상, Claude Opus API 한도 상향, 그리고 Claude Platform의 Claude Managed Agents에 추가된 네 가지 신기능(Dreaming, Multiagent orchestration, Outcomes, Webhooks)을 발표하며, 키노트와 브레이크아웃 세션의 YouTube 녹화본을 안내합니다.

## 언제 유용한가요

- Claude Managed Agents 기반으로 빌드하는 팀이 GA된 Dreaming, Multiagent orchestration, Outcomes, Webhooks를 지금 도입할지 판단해야 할 때.
- 리드 에이전트가 공용 파일시스템 위에서 병렬 specialist 서브에이전트들에게 작업을 분배하는 아키텍처를 설계할 때.
- 에이전트 출력의 품질 기준을 정의하고, 별도의 grader와 리비전 루프를 운영 파이프라인에 엮어야 할 때.
- 폴링 대신 webhook으로 비동기 에이전트 실행 결과를 기존 시스템과 연결할 때.

## 핵심 포인트

- Claude Code rate limit 2배, Claude Opus API 한도 상향. 발표 시점에 모두 라이브.
- 모든 개발자에게 공개된 Claude Managed Agents 신기능 4개:
  - **Dreaming** — 과거 에이전트 세션을 검토해 패턴을 뽑아내고 메모리를 큐레이션해 다음 실행에서 더 나아지게 하는 스케줄 프로세스.
  - **Multiagent orchestration** — 리드 에이전트가 공용 파일시스템 위에서 모델·프롬프트·툴이 다른 specialist 서브에이전트들에게 병렬로 위임. 전체 흐름은 Claude Console에서 추적 가능.
  - **Outcomes** — 개발자가 좋은 결과물의 루브릭을 정의하고, 별도 grader가 자신의 context window에서 결과를 평가하며 기준을 통과할 때까지 에이전트가 리비전. 가장 어려운 내부 벤치마크 문제에서 최대 10포인트 향상이 보고됨.
  - **Webhooks** — outcome이 정의되면 에이전트가 끝까지 실행되고 완료 시 webhook으로 알림.
- 본문에서 언급된 고객 토크: Asana, Cursor, GitHub, Replit, Vercel.
- Code w/ Claude는 런던(5월 19–18 [원문대로])과 도쿄(6월 5–6)로 이어지며, Day 1 키노트와 브레이크아웃 세션은 라이브 스트리밍.

## 번들 리소스

- `skills/managed-agents-new-capabilities/SKILL.md` — 네 가지 신기능을 도입하기 위한 플레이북 스킬.
- `skills/managed-agents-new-capabilities/references/announcements-from-post.md` — 본문 발표 항목과 고객 사례 카탈로그.
- `skills/managed-agents-new-capabilities/examples/outcomes-and-multiagent-patterns.md` — Outcomes, Multiagent orchestration, Webhooks를 결합한 작동 예시.

## 출처

- [Code w/ Claude SF 2026: Building on the AI exponential](https://claude.com/blog/code-w-claude-sf-2026-sf) (Anthropic 블로그, 2026년 5월 12일)
