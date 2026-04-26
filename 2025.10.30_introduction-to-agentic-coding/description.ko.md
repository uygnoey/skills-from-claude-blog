[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# 에이전틱 코딩 입문

## 이 글이 뭔가요

에이전틱 코딩 입문서입니다. 다음 줄을 예측하는 AI 도구에서, 고수준 목표를 받아 다단계 작업을 계획하고, 코드베이스 전반의 파일을 수정하고, 테스트를 실행하며 완료될 때까지 반복하는 AI 시스템으로의 전환을 설명합니다. 자동완성 → 챗 어시스턴트 → 에이전틱 시스템으로의 진화를 정리하고, Claude Code가 프로젝트 컨텍스트를 어떻게 읽고 다중 파일 변경을 조율하며 명시적 권한 모델을 어떻게 따르는지 설명합니다. 라쿠텐의 7시간 자율 vLLM 구현 사례가 메인 사례로 등장합니다.

## 언제 유용한가요

- 팀원에게 "에이전틱 코딩이 자동완성·챗 기반 어시스턴트와 어떻게 다른가"를 설명할 때
- Claude Code에 처음으로 위임할 워크플로우(테스트 자동화, 문서 생성, 리팩터링, 명확한 기능 구현)를 가늠할 때
- 라쿠텐 사례의 구체 수치(79% 빠른 출시, 99.9% 정확도, 5배 병렬 작업 처리)를 인용할 때
- 설치 커맨드와 글이 권장하는 세 가지 "첫 작업" 프롬프트를 빠르게 꺼내 쓸 때

## 핵심 포인트

- 에이전틱 코딩 = 자율성 + 범위. 도구가 전체 코드베이스를 읽고 의존성을 추적하며 커맨드를 실행하고 반복합니다. 자동완성은 컨텍스트 창이 좁고, 챗은 반복은 가능하지만 수동, 에이전트는 오케스트레이션을 직접 처리합니다.
- 두 단계: 컨텍스트 수집 & 계획(설정·테스트·임포트·의존성 매핑 → 적응형 계획), 그다음 구현 & 조율(다중 파일 편집, 테스트 검증).
- Claude Code 설치: `npm install -g @anthropic-ai/claude-code`, 프로젝트 디렉터리에서 `claude` 실행.
- 권한 모델: Claude Code가 파일 수정 전에 승인을 요청하고 계획된 diff를 보여줍니다. 승인·수정·거부 가능.
- 기존 도구(npm, Jest, pytest, Git, dev server)와 통합되고, MCP 서버 연결로 추가 도구도 활용 가능.
- 라쿠텐 사례: vLLM(12.5M LOC, Python/C++/CUDA)에 활성화 벡터 추출 메서드를 7시간 자율 작업으로 구현. 수치 정확도 99.9%, 기능 출시 79% 단축(24일 → 5일), 병렬 작업 5배. Kenta Naruse 인용: "I didn't write any code during those seven hours, I just provided occasional guidance." Yusuke Kaji 인용: "You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."
- 권장 첫 프롬프트: "Explain the structure of this codebase and how the main components interact"; "Review the authentication module for potential security issues"; "Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching".
- "Start slow, then expand" 권고. 즉시 효과를 볼 수 있는 영역: 테스트 자동화, 문서 생성, 일상적 리팩터링, 명확하게 정의된 기능 구현.
- Claude Code는 CLAUDE.md 파일에 코딩 표준·아키텍처 결정·프로젝트별 요구사항을 저장해 세션 간 일관성을 유지합니다.

## 번들 리소스

- [skills/agentic-coding-foundations/SKILL.md](./skills/agentic-coding-foundations/SKILL.md): Claude Code를 언제 꺼낼지, 두 단계 워크플로우, 설치·실행 커맨드, 온보딩 프롬프트
- [references/evolution-of-ai-coding.md](./skills/agentic-coding-foundations/references/evolution-of-ai-coding.md): 자동완성 → 챗 → 에이전틱 비교
- [examples/first-prompts.md](./skills/agentic-coding-foundations/examples/first-prompts.md): 권장 온보딩 프롬프트 3개와 라쿠텐 사례 요약
- [guides/getting-started-with-claude-code.ko.md](./guides/getting-started-with-claude-code.ko.md) (+ en/es/ja): 단계별 도입 가이드

## 출처

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) (게시일 2025-10-30) 내용을 바탕으로 정리했습니다.
