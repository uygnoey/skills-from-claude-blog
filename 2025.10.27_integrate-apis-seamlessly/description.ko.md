[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# API를 매끄럽게 통합하는 방법

## 이 글이 뭔가요

API 통합 작업을 "장애가 터진 뒤 사후 디버깅"에서 "사전 설계"로 바꾸는 실전 가이드입니다. 원문은 대부분의 팀이 rate limit, 토큰 만료, 스키마 변경, 웹훅 순서 등 실패 모드를 프로덕션에서야 발견하고 그제서야 에러 핸들링을 끼워 넣는다고 지적합니다. 그 대안으로, Claude.ai로는 인증·레이트 리밋·엣지 케이스를 사전에 분석하고, Claude Code로는 타입드 클라이언트·OAuth/JWT/키 로테이션 흐름·컨트랙트/리프레시 테스트를 코드베이스 전반에 생성하는 흐름을 제시합니다.

## 언제 유용한가요

- 새 서드파티 API를 도입할 때, 코드 작성 전 실패 모드 체크리스트가 필요할 때
- 기존 통합이 401/429/timeout 사고로 시달리고 있어 체계적 개선이 필요할 때
- 웹훅 vs 폴링을 결정해야 하거나, 스키마 변경을 견디는 버전드 클라이언트를 설계할 때
- 팀이 Claude.ai(설계)와 Claude Code(구현·테스트·PR)를 어떻게 나눠 쓸지 표준화하고 싶을 때

## 핵심 포인트

- Claude.ai는 설계용: API 문서 붙여 넣고 "가능성 높은 통합 리스크 순위"를 요청 → rate limit 임계치, 필수 헤더, 필드 nullability, idempotency, 429 응답에 jitter 적용 등 구체적 항목 확보
- Claude Code는 구현용: `npm install -g @anthropic-ai/claude-code` → `claude` 실행 → OAuth2 자동 토큰 갱신, JWT 검증, 모니터링 포함 API 키 로테이션, 컨트랙트/리프레시 테스트 생성 요청
- 스키마 변경은 어댑터 레이어와 버전드 클라이언트로 흡수, 스키마 검증으로 깨짐을 조기 감지
- 웹훅 vs 폴링은 지연시간·트래픽·인프라에 따라 선택. 두 방식 혼합 전략도 유효
- 출시는 Claude Code로: `> Commit these API changes and open a PR` 한 줄로 커밋 메시지와 PR 설명을 자동 생성

## 번들 리소스

- [skills/api-integration-resilience-playbook/SKILL.md](./skills/api-integration-resilience-playbook/SKILL.md): 설계+구현 플레이북과 프롬프트
- [templates/risk-discovery-prompt.md](./skills/api-integration-resilience-playbook/templates/risk-discovery-prompt.md): 실패 모드 랭킹용 재사용 프롬프트
- [templates/auth-implementation-prompt.md](./skills/api-integration-resilience-playbook/templates/auth-implementation-prompt.md): OAuth2/JWT/키 로테이션 프롬프트
- [references/failure-mode-catalog.md](./skills/api-integration-resilience-playbook/references/failure-mode-catalog.md): 원문에서 언급된 실패 모드 카탈로그
- [examples/example-prompts.md](./skills/api-integration-resilience-playbook/examples/example-prompts.md): 원문에 등장한 Claude.ai/Claude Code 프롬프트 그대로
- [guides/integration-planning-workflow.ko.md](./guides/integration-planning-workflow.ko.md) (+ en/es/ja): 단계별 계획 워크플로우

## 출처

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) (게시일: 2025-10-27) 내용을 바탕으로 정리했습니다.
