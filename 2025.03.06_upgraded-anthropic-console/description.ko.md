[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# 업그레이드된 Anthropic Console로 더 빨리 프로덕션까지 가기

## 이 글이 뭔가요

Anthropic이 2025년 3월 6일에 공개한 발표로, 새로 디자인된 Anthropic Console을 동료들과 함께 Claude로 AI 배포를 빌드/테스트/반복하는 단일 작업 공간으로 소개합니다. 4가지 프롬프트 엔지니어링 도구(Workbench, 자동 프롬프트 생성, side-by-side 비교 평가, 프롬프트 개선), 직군 간 협업을 위한 shareable prompts, 최신 Claude 3.7 Sonnet 지원, 그리고 extended thinking budget 제어 기능을 다룹니다.

## 언제 유용한가요

- 새로운 프롬프트를 프로덕션으로 올리려 하는데, 즉흥적 실험이 아닌 체계적인 빌드 → 테스트 → 반복 루프를 만들고 싶을 때.
- 개발자, 도메인 전문가, 제품 매니저, QA 등 여러 역할이 같은 프롬프트를 문서나 메신저 복붙 없이 함께 다듬어야 할 때.
- 다른 AI 모델용으로 작성된 프롬프트를 Anthropic의 프롬프트 엔지니어링 기법으로 다시 쓰고 싶을 때.
- Claude 3.7 Sonnet의 extended thinking을 도입하면서 thinking 토큰 예산을 명시적으로 관리하고 싶을 때.

## 핵심 포인트

- Workbench는 프롬프트 구조화, 예시 추가, 외부 도구 통합을 인터랙티브한 API 호출 테스트 환경에서 한 번에 처리합니다.
- 프롬프트 생성기는 태스크 설명을 입력하면 chain-of-thought 같은 기법을 활용한 프롬프트를 만들어 줍니다.
- 평가 도구는 테스트 케이스를 자동 생성하고 출력을 나란히 비교하며 응답 품질을 채점합니다.
- 프롬프트 개선 도구는 기존 프롬프트(다른 AI 모델용으로 쓰인 것 포함)를 더 다듬어 줍니다.
- "Get Code" 버튼은 바로 배포할 수 있는 프로덕션 수준의 API 호출 코드를 내보냅니다.
- shareable prompts는 조직 전체가 같은 프롬프트 라이브러리를 공유하고 표준화할 수 있게 합니다.
- Claude 3.7 Sonnet 지원과 함께, extended thinking을 위한 최대 thinking 토큰 예산 설정이 가능합니다.

## 번들 리소스

- Skill: `skills/console-build-test-iterate-workflow/SKILL.md` — 글이 설명하는 빌드 → 평가 → 개선 → 배포 루프와, shareable prompts·extended thinking budget 활용 가이드.
- Reference: `skills/console-build-test-iterate-workflow/references/console-tools-from-post.md` — 글이 명시한 Console 도구와 기능들의 정리.
- Examples: `skills/console-build-test-iterate-workflow/examples/team-collaboration-scenarios.md` — 글에 등장한 협업자 역할을 기반으로 한 shareable prompts 시나리오.

## 출처

Get to production faster with the upgraded Anthropic Console — Anthropic, 2025년 3월 6일: <https://claude.com/blog/upgraded-anthropic-console>
