[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude의 MCP 커넥터에 대해, Okta 기반으로 조직 차원의 권한 부여를 중앙에서 관리하는 ‘엔터프라이즈 관리형 인증(authorization)’ 기능을 소개합니다.

## 언제 유용한가요
팀/엔터프라이즈 환경에서 커넥터 접근을 IT가 중앙에서 관리하고, 사용자는 첫 로그인 시점부터 자동으로 접근할 수 있게 하며, 회수(해지)도 IdP 기반으로 일관되게 운영해야 할 때 유용합니다.

## 핵심 포인트
- 관리자가 커넥터를 한 번만 승인하면, 사용자는 IdP의 기존 그룹/역할을 통해 접근 권한을 상속합니다.
- 사용자는 별도의 개인별 OAuth 승인 절차 없이 ‘제로 터치’로 커넥터를 사용할 수 있습니다.
- Claude 채팅, Claude Code, Cowork 전반에서 접근이 일관됩니다.
- Model Context Protocol의 Enterprise-Managed Authorization 확장(오픈 표준)에 기반해, 커스텀 커넥터도 지원할 수 있습니다.
- 중앙 관리를 통해 토큰 수명을 더 짧게 가져가거나, 퇴사/권한 회수 시 잔여 토큰 문제를 줄일 수 있습니다.

## 번들 리소스
- Skill: enterprise-managed-connector-auth (도입 체크리스트 + 운영 절차)
- Guide: enterprise-managed-connector-auth-rollout (배포 가이드)

## 출처
- https://claude.com/blog/enterprise-managed-auth
