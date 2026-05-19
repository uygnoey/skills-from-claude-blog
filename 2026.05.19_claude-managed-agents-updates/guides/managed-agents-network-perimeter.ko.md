[English](./managed-agents-network-perimeter.en.md) · **한국어** · [Español](./managed-agents-network-perimeter.es.md) · [日本語](./managed-agents-network-perimeter.ja.md)

# 실행과 연결을 퍼리미터 내부에 유지하기

## 이 가이드가 다루는 내용
- self-hosted sandbox가 Claude Managed Agents의 실행 경계를 어떻게 바꾸는지
- MCP tunnel이 MCP 서버를 공용 인터넷에 노출하지 않고도 사설 연결을 제공하는 방식

## 실무 가이드

### 실행 경계
- 리포지토리/파일/의존성/연산이 큰 툴 실행은 샌드박스 내부에서 수행합니다.
- 에이전트 루프는 관리형 컨트롤 플레인에 둡니다.

### 연결
- 사설 MCP 서버는 MCP tunnel을 우선 고려해 inbound 방화벽 규칙이나 공용 엔드포인트 없이 연결합니다.
- 트래픽이 종단 간 암호화되는지 확인합니다.

## 출처
- https://claude.com/blog/claude-managed-agents-updates
