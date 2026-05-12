[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Anthropic 보안팀이 Claude Code로 위협 탐지 플랫폼을 만든 이야기

## 이 글이 뭔가요

2026년 5월 11일에 Anthropic Detection Platform Engineering 팀의 테크 리드 Jackie Bow가 공개한 케이스 스터디입니다. 팀이 만든 **CLUE(Claude Looks Up Evidence)** — CLUE Triage와 CLUE Investigate라는 두 가지 surface로 구성된 탐지·대응 플랫폼 — 가 Claude를 자연어 인터페이스로 삼아 Anthropic 내부 시스템 위에서 동작하는 방식, 측정한 임팩트(거짓 양성 비율, 쿼리·tool call 수, 절감 시간), 그리고 SOAR식 스크립트 플레이북에서 "Claude에게 경계만 주고 조사 경로는 맡기는" 철학으로 옮겨간 과정을 정리합니다.

## 언제 유용한가요

- 방어 보안팀이 자사 SIEM과 내부 시스템 위에 Claude 기반 트리아지·조사 surface를 올릴지 결정할 때.
- 결정론적 플레이북과 에이전트 주도 조사 사이의 경계, 그리고 에이전트가 읽을 수 있는 데이터 거버넌스 범위를 설계할 때.
- 내부 탐지 플랫폼 비즈니스 케이스(알람 볼륨, 거짓 양성 감소, 절감 시간, 저신뢰 신호 커버리지)를 정리할 때.
- 조직의 컨텍스트(Slack, 내부 문서, 데이터 웨어하우스, 코드 저장소)를 보안 에이전트에 어떻게 tool로 꽂을지 그릴 때.

## 핵심 포인트

- CLUE Triage는 들어오는 모든 알람에 대해 1차 트리아지를 수행하고 Slack·내부 문서·코드·데이터 웨어하우스 컨텍스트로 보강. 분석가는 disposition과 confidence score를 받는다.
- CLUE Investigate는 자연어 쿼리 인터페이스. Claude가 에이전틱 루프에서 오케스트레이터로 sub-agent들에게 병렬 쿼리를 시키고 결과를 합쳐 조사 요약을 만든다.
- 보고된 임팩트: 거짓 양성 비율이 **약 1/3 → 7%**, 30일 기준 **약 12,000 쿼리·27,000 tool call**을 자동화해 **약 1,870시간(234 person-day)** 의 수작업을 절감, **5–10배** 시간 절감. 조사당 평균 약 25 tool call·11 쿼리.
- Claude Code가 "디자인 파트너 겸 협업자" 역할. PoC 1일, 설계·구현 1주.
- 철학: 경계(접근 가능한 tool·데이터)는 인코딩하되 전략은 열어둔다. Claude는 사람이 미리 짜두지 못했을 조사 경로를 자주 찾아낸다.
- 향후 방향: 알람 응답에서 지속적 사전 헌팅으로, 조사 transcript를 조직의 기억으로, 그리고 여러 조사 전략을 병렬로 돌려 결과를 비교하는 비결정성 수용.

## 번들 리소스

- `skills/clue-style-detection-platform-playbook/SKILL.md` — CLUE 스타일 탐지 플랫폼 설계(서피스, 에이전틱 루프 모양, 컨텍스트 소스, 지표, 거버넌스) 플레이북.
- `skills/clue-style-detection-platform-playbook/references/clue-architecture-from-post.md` — 본문에서 언급된 컴포넌트·지표·인용문의 원문 카탈로그.
- `skills/clue-style-detection-platform-playbook/examples/data-governance-investigation.md` — 본문 속 계약직 데이터 거버넌스 시나리오를 따라간 작동 예시.

## 출처

- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity) (Anthropic 블로그, 2026년 5월 11일)
