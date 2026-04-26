[English](./getting-started-with-claude-code.en.md) · **한국어** · [Español](./getting-started-with-claude-code.es.md) · [日本語](./getting-started-with-claude-code.ja.md)

# Claude Code 시작 가이드

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (2025-10-30)에서 정리한 짧은 도입 가이드입니다. 프로젝트에 Claude Code를 처음 들이는 날의 체크리스트로 사용합니다.

## 1. 워크플로우 적합도 확인

설치 전, 위임하려는 작업이 적합한지 확인합니다.

- 여러 파일을 가로지르거나
- 커맨드를 실행하고 결과를 해석해야 하거나
- 일은 많지만 정의가 명확한 작업(테스트 보강, 문서 생성, 일상적 리팩터링)

개념적 질문이거나 문제 자체를 스코핑 중이라면 Claude.ai에 머무르는 게 낫습니다.

## 2. Claude Code 설치

```
npm install -g @anthropic-ai/claude-code
```

## 3. 프로젝트에서 실행

프로젝트 루트로 이동한 뒤:

```
claude
```

Claude Code는 설정 파일·테스트·임포트를 먼저 읽어 내부 지도를 만든 후 작업을 시작합니다.

## 4. 권장 온보딩 프롬프트 3종 시험

순서대로:

```
Explain the structure of this codebase and how the main components interact
```

```
Review the authentication module for potential security issues
```

```
Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching
```

첫 번째는 Claude Code가 프로젝트를 어떻게 읽는지 감을 잡게 합니다. 두 번째는 분석 능력을, 세 번째는 다중 파일 구현 전체를 시연합니다.

## 5. 승인·수정·거부

Claude Code는 파일 수정 전에 승인을 요청하며 계획된 diff를 보여줍니다. 이해되는 것만 승인하고, 어색하면 거부하거나 수정 요청합니다.

## 6. CLAUDE.md에 프로젝트 지식 영속화

프로젝트 루트에 `CLAUDE.md`를 두어 코딩 표준·아키텍처 결정·프로젝트별 요구사항을 기록합니다. Claude Code는 매 세션에서 이 파일을 읽습니다.

## 7. 빠른 효과 영역으로 확장

첫 세션 이후, 글이 강조하는 카테고리에서 의도적인 사용 사례를 3개 정해 진행합니다.

- 미커버 경로의 테스트 자동화
- 레거시 시스템의 문서 생성
- 기술 부채에 대한 일상적 리팩터링
- 명확하게 정의된 기능 구현

이 경험으로 팀 내 Claude Code 신뢰 영역을 결정합니다.

## 8. (선택) MCP 서버 연결

이슈 트래커·디자인 시스템·내부 문서 등 리포지토리 밖 도구가 필요하면 MCP 서버를 연결해 Claude Code가 계획에 그 컨텍스트를 끌어올 수 있게 합니다.

## 출처

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (게시일 2025-10-30).
