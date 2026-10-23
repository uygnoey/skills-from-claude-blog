[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic 세일즈 개발 리더 Carl Johnson이 쓴 사례 글입니다(2026년 9월 30일). Claude Managed Agents(베타)
위에 만든 구매 에이전트(buying agent)가 이제 인바운드 고객 대부분을 응대하며 "회사에 Claude를 도입하고
싶다"에서 구매 완료까지 이끄는 방식과, 그로 인해 세일즈 팀의 일이 어떻게 바뀌었는지를 설명합니다.

## 언제 유용한가요
- 인바운드 수요가 폼 → BDR → AE 프로세스를 넘어서서 구매자가 간단한 답을 며칠씩 기다릴 때.
- 복잡한 딜은 여전히 영업 담당자에게 넘기면서, 상시 셀프서브 구매 경험을 설계할 때.
- 고객 대면 세일즈 에이전트의 프롬프트를 작성하고 반복 개선할 때.

## 핵심 포인트
- 이전 프로세스: 월 수만 건의 인바운드 요청, 담당자들은 문서에 이미 있는 질문에 답하느라 시간을 썼습니다.
- 에이전트는 Contact Sales·Pricing 페이지, 제품 내부, 이메일에 배치되며 고객이 선택하는 opt-in 방식입니다.
- 대화는 구매, 전체 맥락을 담은 담당자 핸드오프, 빠른 답변 중 하나로 끝납니다.
- 구조: 프롬프트, 소수의 도구, 그리고 Managed Agents 위의 Claude(호스팅·세션·도구 오케스트레이션은 플랫폼 담당).
- Managed Agents를 고른 이유: 엔지니어 한 명이 몇 주 만에 출시, 세일즈·콘텐츠 리드가 Console에서 스테이징
  에이전트로 프롬프트를 직접 수정, 모든 변경이 버전으로 저장(내부 테스트 약 1주 만에 v7).
- 교훈: 규칙 대신 목표를 줄 것, 짧을수록 좋다, SME를 개발 루프에 넣을 것, 고객에게 맞는 플랜을 추천할 것
  (예: Enterprise 대신 Team), 모든 에스컬레이션 사유를 피드백으로 삼을 것(사람이 필요한 비율이 약 절반으로 감소).
- 결과: 하루 수천 건 대화, 에스컬레이션된 리드의 기회 전환율이 기존 폼 대비 2배 이상, 성사까지 약 5일 단축,
  한 담당자는 딜당 이메일이 약 10통에서 6통으로 줄고 성사 건수가 2.5배가 되었습니다.

## 번들 리소스
- 스킬: `inbound-buying-agent-design` (`references/conversation-outcomes.md`,
  `references/lessons-and-results.md`, `templates/goal-first-system-prompt.md`,
  `templates/escalation-feedback-log.md`).

## 출처
- https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
