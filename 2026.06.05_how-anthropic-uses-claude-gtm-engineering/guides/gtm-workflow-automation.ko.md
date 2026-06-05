[English](./gtm-workflow-automation.en.md) · **한국어** · [Español](./gtm-workflow-automation.es.md) · [日本語](./gtm-workflow-automation.ja.md)

# Claude Code로 GTM 워크플로 자동화하기

## 이 가이드에서 다루는 내용
이 가이드는 블로그 글의 접근법을 반복 가능한 방법으로 정리합니다. GTM 팀을 위해 Claude Code 워크플로를 만들 때, 하나의 좁은 워크플로에서 시작하고, 최신 컨텍스트를 가져오며, 문체를 맞추도록 프롬프트를 반복 개선한 뒤, 조직 전체가 쉽게 쓰도록 번들링합니다.

## 방법
1. **가장 고통스러운 워크플로 하나를 선택**합니다(예: 고객 이메일 답장).
2. 실행 시점에 사용할 **컨텍스트 소스**를 정의합니다(이메일, 캘린더, CRM, 문서).
3. **시스템 프롬프트 초안**을 만들고, 출력이 팀의 문체에 맞을 때까지 반복 조정합니다.
4. 관계 유형별로 **톤 변형**을 추가합니다.
5. 첫 워크플로가 안정화되면 **인접 워크플로로 확장**합니다(프리콜 브리프, 데일리 리캡).
6. **채택을 위한 번들링**(스킬 + 연동/커넥터)으로 다른 사람이 바로 설치·사용할 수 있게 합니다.

## 추천 아티팩트
- Skill: [../skills/sales-workflow-briefing/SKILL.md](../skills/sales-workflow-briefing/SKILL.md)
- Templates: [../skills/sales-workflow-briefing/templates/](../skills/sales-workflow-briefing/templates/)

## 출처
- https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
