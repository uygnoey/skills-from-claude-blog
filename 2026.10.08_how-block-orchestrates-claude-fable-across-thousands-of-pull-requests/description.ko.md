[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Block(Square, Cash App)의 AI Capabilities 책임자 Bradley Axen 인터뷰입니다. Block이 모델을 평가하는
방법, Claude Fable 5가 수천 개의 PR에 걸친 전사 코드 마이그레이션을 오케스트레이션하는 방식, 직원들이
모델을 효율적으로 쓰도록 이끄는 방법, 모든 기술직 직원이 프런티어 모델을 쓰는 환경에서 의지하는
세이프가드를 다룹니다.

## 언제 유용한가요
- 여러 저장소에 걸쳐 수백~수천 개의 PR이 필요한 마이그레이션을 계획할 때.
- 특정 종류의 에이전트 작업에 어떤 모델과 effort 수준을 쓸지 정할 때.
- 대규모 조직에서 코드를 쓰는 에이전트의 가드레일을 설계할 때.

## 핵심 포인트
- 계층형 오케스트레이션: 사람이 방향을 잡고, Fable이 사전 설계(데이터 모델, API 스펙, 알고리즘)를 맡아
  파일 수정과 테스트 실행을 하는 더 작은 모델(Opus, Sonnet)을 최대 수십 개까지 지휘합니다. 초기 결과로는
  품질 저하 없이 토큰의 더 큰 비중이 작업자 모델로 옮겨 갔고, 한 마이그레이션에서 Fable이 오케스트레이션한
  PR 천 개를 머지하기도 합니다.
- Block은 이를 사람과 에이전트가 채널과 스레드를 공유하는 오픈소스 워크스페이스 Buzz에서 돌립니다.
- 에이전트가 약 백만 줄 규모의 코드베이스를 매일 또는 매주 훑으며 정리·통합할 기술 부채를 찾습니다.
- 효율: 기술직에게 프런티어 모델 전면 접근을 주되, 모델 선택을 돕는 자동 선택기를 만들고 있습니다. 모든
  사용 사례를 모든 모델 × 모든 effort 수준으로 벤치마크합니다 — 슬라이더가 아니라 격자입니다.
- 세이프가드: main 머지, 프로덕션 배포, 피처 플래그는 사람 몫. 에이전트 변경은 보안 검사를 통과해야 하고
  배포에는 사람 두 명의 승인이 필요합니다. 원격 워크스테이션, 네트워크 허용 목록, 모델 루프 밖의 값싼
  검사(정규식, 작은 분류기). PR 생성, 코드 리뷰, 로그·분석 DB 조회는 일부러 허용합니다. Claude는 이중
  승인을 우회하라는 요청을 거부하며, Block은 이것도 벤치마크합니다.
- 조직의 성숙도란 배운 맥락을 개인이 아닌 시스템 수준에서 기억하는 것입니다.

## 번들 리소스
- Skill: `orchestrated-code-migrations` — 오케스트레이터/작업자 계층형 마이그레이션, 모델 × effort 선택
  (`templates/model-effort-grid.md`), 세이프가드(`references/safeguards.md`).
- Agents: 글에 나온 두 역할 `migration-orchestrator`, `migration-worker`.
- Guide: "프런티어 모델을 대규모로 효율적이고 안전하게 운영하기" (4개 언어).

## 출처
- https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
