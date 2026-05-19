[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Managed Agents의 두 가지 기능 업데이트를 소개합니다. 하나는 사용자가 제어하는 샌드박스에서 툴 실행을 수행하는 **self-hosted sandbox**이고, 다른 하나는 사설 네트워크 내부의 Model Context Protocol(MCP) 서버에 안전하게 연결하는 **MCP tunnel**입니다.

## 언제 유용한가요
민감한 코드·파일·내부 시스템을 다루면서도 실행 환경과 네트워크 접근을 기업 보안 경계(퍼리미터) 안에 유지해야 할 때 유용합니다.

## 핵심 포인트
- self-hosted sandbox는 툴 실행을 사용자가 제어하는 인프라(또는 관리형 샌드박스 제공자)로 옮기고, 에이전트 루프(오케스트레이션, 컨텍스트 관리, 오류 복구)는 Anthropic 인프라에서 계속 동작합니다.
- Cloudflare, Daytona, Modal, Vercel 등 제공자별 특성(격리, 확장성, 네트워킹, 런타임)을 기준으로 샌드박스 클라이언트를 선택할 수 있습니다.
- MCP tunnel은 사설 네트워크 내부 MCP 서버를 공용 인터넷에 노출하지 않고도 에이전트가 접근할 수 있게 합니다(단일 outbound 연결, inbound 방화벽 규칙 불필요, 종단 간 암호화).
- 제공 현황: self-hosted sandbox는 공개 베타, MCP tunnel은 리서치 프리뷰이며 액세스 요청이 필요합니다.

## 번들 리소스
- Skill: managed-agents-secure-sandboxing (self-hosted sandbox 및 MCP tunnel 선택/운영 패턴과 체크리스트)
- Guide: managed-agents-network-perimeter (실행/연결을 퍼리미터 내부에 유지하기 위한 배포 중심 가이드)

## 출처
- https://claude.com/blog/claude-managed-agents-updates
