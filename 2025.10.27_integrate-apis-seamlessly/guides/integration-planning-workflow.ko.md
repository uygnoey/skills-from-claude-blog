[English](./integration-planning-workflow.en.md) · **한국어** · [Español](./integration-planning-workflow.es.md) · [日本語](./integration-planning-workflow.ja.md)

# 통합 계획 워크플로우

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (2025-10-27)에서 정리한 단계별 워크플로우입니다. 팀이 Claude.ai와 Claude Code를 사용해 서드파티 API 통합을 계획·구현·검증·출시하는 절차를 표준화하기 위해 사용합니다.

## 1. Claude.ai에서 API 트리아지

- Claude.ai를 열고 문서 URL, OpenAPI 스펙, 또는 관련 발췌문을 붙여 넣습니다.
- "Integration risks ranked by likelihood"를 요청합니다. 일반론은 거부하고 벤더별 구체 항목만 받습니다 — rate limit 임계치, 카운팅 방식(유저별/IP별/API 키별), 필수 헤더, 멱등성 키, 웹훅 전달 보장, 필드 nullability 등.
- 명확하지 않은 실패 모드는 후속 질문으로 디버깅합니다(예: "Why might OAuth tokens expire during multi-step checkout flows?", "Here's a Stripe webhook signature error. What validation steps am I missing?").
- 결과: 구체적인 실패 모드 리스트와 인증 전략 결정(자격 증명 보관 위치, 갱신 주기, 로테이션 계획).

## 2. 웹훅 vs 폴링 결정

- 구체 유스케이스로 비교합니다(예: "webhook vs polling for real-time inventory updates").
- 지연시간·트래픽·인프라 제약으로 결정합니다. 하이브리드(실시간은 웹훅, 정합성 검증은 폴링)도 유효합니다.
- 결정과 그 근거가 된 제약을 기록합니다.

## 3. Claude Code로 구현

- 설치: `npm install -g @anthropic-ai/claude-code`. 프로젝트 루트에서 `claude` 실행.
- Claude Code에 기존 프로젝트 컨벤션에 맞는 타입드 클라이언트 생성을 요청합니다.
- 결정된 인증 흐름 구현:
  - "Build OAuth2 flow for Google Calendar with automatic token refresh"
  - "Create rotating API key system for Twilio with monitoring"
  - "Implement JWT validation for microservices"
- 레이트 리밋 처리 추가: 429에 jitter 포함 지수 백오프, 필요시 요청 큐잉, 연쇄 장애 위험이 있는 호출에는 서킷 브레이커.
- 응답 경계에서 스키마 검증을 연결하고, 버전드 클라이언트라면 어댑터 레이어를 추가합니다.

## 4. 검증

Claude Code에 테스트 생성·실행을 요청합니다:

- "Create tests that reproduce this rate limit scenario"
- "Generate contract tests for schema validation"
- "Run tests for authentication refresh during long operations"

1단계에서 정리한 실패 모드를 통합이 모두 처리한다고 테스트가 확인할 때까지 반복합니다.

## 5. 출시

Claude Code 안에서 실행:

```
> Commit these API changes and open a PR
```

Claude Code가 설명이 담긴 커밋 메시지와, 구현과 테스트 커버리지를 연결한 PR 설명을 생성합니다.

## 출처

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (게시일: 2025-10-27).
