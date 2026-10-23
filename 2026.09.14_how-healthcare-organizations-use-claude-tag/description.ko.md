[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Camy Pearson, Maria Howe, Araba Koomson이 쓴 베스트 프랙티스 글입니다(2026년 9월 14일). 의료 기관들이
Claude Tag(베타, Slack 속 Claude)를 보호 대상 건강정보(PHI)에 전혀 닿지 않는 업무에서 어떻게 쓰는지
Insight Health, Tennr, Medallion 사례로 설명합니다.

## 언제 유용한가요
- 의료·규제 산업 팀이 Slack에 AI 팀원을 두고 싶지만 PHI는 반드시 차단해야 할 때.
- Claude Tag 파일럿의 채널, 커넥터, 자율성 수준을 정할 때.
- 검증된 PHI 없는 사용 사례(장애 대응, 내부 도구 유지보수, 보험사 규칙 지식)를 찾을 때.

## 핵심 포인트
- Claude Tag는 아직 Anthropic BAA 적용 대상이 아니므로 PHI 없는 채널과 커넥터에서만 사용합니다.
- 관리자 통제: 기본 비활성, 승인 채널 허용 목록, DM 비활성, 채널별 커넥터 범위 지정, EHR·임상 시스템·
  환자 커뮤니케이션을 제외한 액세스 번들. 호출한 구성원이 볼 수 있는 것만 봅니다.
- Insight Health는 PHI를 마스킹하는 BAA 적용 Agent SDK 에이전트 Zeus와 Claude Tag를 함께 씁니다.
  긴급 알림 채널의 알림 97%가 엔지니어 개입 없이 종료됐습니다.
- Tennr는 Claude Tag를 내부 오퍼 포털의 주 유지보수자로 씁니다(약 한 달에 티켓 15건 이상).
- Medallion은 보험사 규칙 지식을 채널에 축적하고, Claude가 확신이 없으면 전문가를 태그합니다.
- 채널 하나, 커넥터 한두 개로 시작해 GitHub를 연결하고 2주간 파일럿합니다.
- 크레딧(Enterprise $25,000 / Team 10석 이상 $2,500)은 2026년 10월 1일에 만료됐습니다.

## 번들 리소스
- 스킬: `phi-safe-slack-agent-rollout` (`references/customer-patterns.md`,
  `templates/rollout-checklist.md`).

## 출처
- https://claude.com/resources/articles/how-healthcare-organizations-use-claude-tag
