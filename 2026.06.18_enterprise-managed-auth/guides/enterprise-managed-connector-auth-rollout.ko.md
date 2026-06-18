[English](./enterprise-managed-connector-auth-rollout.en.md) · **한국어** · [Español](./enterprise-managed-connector-auth-rollout.es.md) · [日本語](./enterprise-managed-connector-auth-rollout.ja.md)

# 엔터프라이즈 관리형 커넥터 인증(authorization) 배포 가이드(Okta)

## 목표
MCP 커넥터 권한 부여를 IdP의 그룹/역할 기반으로 중앙 관리하여, 사용자가 첫 로그인부터 커넥터를 자동으로 사용할 수 있게 합니다.

## 권장 배포 단계
1. 범위 정의: 대상 커넥터, 파일럿 그룹, 성공 기준.
2. 중앙 프로비저닝: 관리자가 한 번 승인하고, IdP 그룹/역할로 범위를 부여.
3. 파일럿 검증: 제로 터치 접근과 권한 회수 동작 확인.
4. 전사 배포: 그룹 할당 확장, 운영/지원 플레이북 문서화.

## 운영 고려사항
- 커넥터 접근을 다른 접근 권한과 동일하게 IdP에서 프로비저닝/감사/회수합니다.
- 퇴사/권한 회수 후 잔여 접근을 줄이기 위해 토큰 수명을 더 짧게 가져가는 것을 검토합니다.
- 필요 시 IdP 경유 연결만 허용하여 개인/업무 계정 혼동을 줄입니다.

## 출처
- https://claude.com/blog/enterprise-managed-auth
