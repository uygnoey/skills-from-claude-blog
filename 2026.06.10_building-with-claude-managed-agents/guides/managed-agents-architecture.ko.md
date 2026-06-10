[English](./managed-agents-architecture.en.md) · **한국어** · [Español](./managed-agents-architecture.es.md) · [日本語](./managed-agents-architecture.ja.md)

# Managed Agents 아키텍처 개요

## 이 가이드는 무엇인가요
이 문서는 “The evolution of agentic surfaces: building with Claude Managed Agents” 글을 바탕으로, Managed Agents의 핵심 아키텍처를 간단히 정리합니다.

## 핵심 아이디어
Managed Agents는 다음을 분리합니다.
- 하네스(두뇌): 오케스트레이션과 모델 호출
- 샌드박스(손): 도구/코드 실행 환경

그리고 세션이 두 컴포넌트를 연결하는 append-only 이벤트 로그를 제공합니다.

## 왜 분리가 중요한가요
- 보안: 자격증명을 샌드박스 밖에 둘 수 있습니다.
- 성능: 컨테이너가 존재하기 전부터 추론을 시작할 수 있고, 도구를 쓰지 않는 세션은 컨테이너 기동을 피할 수 있습니다.
- 운영성: 내구성 있는 세션은 디버깅 타임라인, pause/resume, 상위 기능(Memory, Dreaming)을 가능하게 합니다.

## 글에서 언급된 개념
- agents, environments, sessions를 조합형 리소스로 다룸
- 자격증명을 위한 Vaults
- 자체 호스팅 샌드박스(예: VPC 내부)
- 프라이빗 네트워크의 MCP 서버에 연결하기 위한 MCP tunnels

## 출처
- https://claude.com/blog/building-with-claude-managed-agents
