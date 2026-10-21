[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Uber의 CISO Philip Martin 인터뷰입니다. 기업이 직원을 대상으로 이미 운영하는 내부자 위협(insider threat)
프로그램이 AI 에이전트에도 필요한 이유, 프런티어 모델이 보안 업무를 어떻게 바꾸는지, 그리고 Uber의 오픈소스
AI Detection and Response(ADR) 도구가 Anthropic의 Enterprise Frontier Safeguards와 어떻게 함께 동작하는지
다룹니다.

## 언제 유용한가요
- 사내 AI 에이전트의 모니터링·탐지·대응 체계를 설계할 때.
- 자체 에이전트 텔레메트리와 모델 제공사의 세이프가드 신호를 함께 쓰려 할 때.
- AI 시스템 보안에서 방어자가 다음에 집중할 곳을 정할 때.
- 프런티어 모델 배포에 모니터링이 필요하다는 점을 경영진에게 설명할 때.

## 핵심 포인트
- 프런티어 모델은 긴 시간 범위에 걸쳐 훨씬 많은 맥락(코드, 설계 문서, Jira 이슈, 서비스 이력)을 받아들여
  매우 구체적인 위협 모델과 보안 리뷰를 만듭니다. Martin은 서비스마다 에이전트가 붙어 서로 위협 모델을
  주고받는 미래를 예상합니다.
- Enterprise Frontier Safeguards: Uber는 데이터에 대한 통제권(허가 없이는 Anthropic이 접근 불가)과
  세이프가드가 작동한 뒤의 조치에 대한 통제권을 유지합니다.
- Uber의 AI 보안 아키텍처: 경계 역할의 LLM 게이트웨이, 에이전트 하네스에서 실시간 텔레메트리 수집과 조치를
  하는 오픈소스 ADR, 그리고 탐지 환경에 통합되는 제공사 분류기 출력.
- 우선순위 1: 실시간 탐지와 개입 — 사람이 프롬프트를 입력하거나 모델이 도구를 호출하는 순간에 최대한 가깝게.
- 우선순위 2: 새로 나타나는 패턴 이해 — 새 행동을 발견하고 세이프가드를 만들고 반복(제약이 새 행동을 낳음).
- 모든 기업은 사람을 대상으로 내부자 위협 프로그램을 운영합니다. 모델도 같은 위험을 가져오므로 같은 역량이
  필요합니다.

## 번들 리소스
- Skill: `ai-insider-threat-program` — 계층형 아키텍처, 실시간 개입, 행동 발견 루프
  (`references/ai-security-architecture.md`).
- Guide: "AI 에이전트를 내부자처럼 보호하기" (4개 언어).

## 출처
- https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
