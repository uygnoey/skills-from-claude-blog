[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Managed Agents 업데이트: 스케줄 실행과 Vault 환경 변수

## 이 글이 뭔가요
이 글은 Claude Managed Agents의 두 가지 신규 기능(퍼블릭 베타)을 소개합니다: 크론처럼 주기적으로 실행되는 스케줄 배포(scheduled deployments)와, CLI 인증을 위해 Vault에 환경 변수를 저장하는 기능입니다.

## 언제 유용한가요
에이전트가 정기 작업을 스케줄에 맞춰 자동 수행하게 하고 싶지만 별도의 스케줄러를 구축·운영하고 싶지 않을 때, 그리고 API 키 같은 비밀 값을 모델에 노출하지 않으면서 CLI 도구에 안전하게 전달하고 싶을 때 유용합니다.

## 핵심 포인트
- 스케줄 배포는 크론 스케줄마다 새 세션을 시작하며, 일시정지/재개/아카이브 및 필요 시 수동 트리거도 가능합니다.
- Vault가 환경 변수를 지원해 CLI가 인증 요청을 보낼 수 있으며, 도메인 허용 목록을 통해 네트워크 경계에서만 실제 키가 주입되어 모델은 키를 볼 수 없습니다.

## 번들 리소스
- Skill: managed-agents-scheduled-deployments (운영 체크리스트 및 활용 패턴)

## 출처
- https://claude.com/blog/whats-new-in-claude-managed-agents
