[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# 커넥터를 만드는 개발자를 위한 관측 가능성(Observability)

## 이 글이 뭔가요
이 글은 Claude 디렉터리에 게시된 커넥터에 대해, Claude 제품 전반에서의 성능을 확인할 수 있는 새로운 관측 가능성 대시보드와, 앱 내에서 MCP 서버를 디렉터리에 직접 제출할 수 있는 기능을 소개합니다.

## 언제 유용한가요
- 게시된 커넥터의 소유자/운영자로서, Claude 제품 표면 전반에서의 채택(사용)과 안정성, 성능을 파악해야 할 때.
- MCP 서버를 커넥터 디렉터리에 제출하는 과정을 더 간단하게 만들고 싶을 때.

## 핵심 포인트
- 디렉터리의 게시된 커넥터에 대시보드가 제공되어 Claude 제품 전반에서의 성능을 모니터링할 수 있습니다.
- 대시보드에서 채택(활성 사용자, 총 도구 호출 수, 디렉터리 순위 추이)을 추적할 수 있습니다.
- 대시보드에서 문제를 진단할 수 있습니다(헬스 스코어, 오류율, 지연 시간, 도구별 오류 분해).
- 제품별 사용량(예: Claude, Claude Code, Cowork 등)을 비교할 수 있습니다.
- 접근 권한은 Team/Enterprise 플랜의 Admin/Owner(또는 Enterprise의 Libraries 권한을 가진 커스텀 역할)에게 제공됩니다.

## 번들 리소스
- Skill: `skills/connector-observability/SKILL.md`
- Guide: `guides/connector-observability-dashboard.ko.md` (+ en/es/ja)

## 출처
- https://claude.com/blog/observability-for-developers-building-connectors
