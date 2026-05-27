[English](./managed-agents-private-execution-overview.en.md) · **한국어** · [Español](./managed-agents-private-execution-overview.es.md) · [日本語](./managed-agents-private-execution-overview.ja.md)

# Claude Managed Agents 프라이빗 실행 옵션(개요)

## 이 문서는 무엇인가요
Code w/ Claude London 2026 리캡에서 언급된 두 가지 Claude Platform 기능( self-hosted sandbox, MCP tunnel )을 의사결정 관점에서 요약한 짧은 가이드입니다.

## 결정 트리
1) **에이전트 코드 실행 위치**를 직접 통제해야 하나요(데이터/파일이 경계 밖으로 나가면 안 됨)?
- 예 → Self-hosted sandbox.

2) 인바운드 엔드포인트를 공개하지 않고 Claude가 **프라이빗 MCP 서버**에 접근해야 하나요?
- 예 → MCP tunnel.

3) 둘 다 필요한가요?
- 예 → 두 기능을 함께 사용.

## 구현 체크리스트(상위 수준)
- 데이터 경계(리포지토리, 파일, 시크릿, 로그)를 정의합니다.
- 노출할 내부 도구(MCP 서버) 목록과 필요한 인증 방식을 정리합니다.
- 네트워크 egress 정책과 감사 로깅 요구사항을 확정합니다.
- 담당자를 지정합니다: 런타임/인프라, 보안, Console 관리자.

## 추가 읽을거리
- Reference: `../skills/managed-agents-private-execution/references/managed-agents-private-execution.md`
- 행사 리캡 출처: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
