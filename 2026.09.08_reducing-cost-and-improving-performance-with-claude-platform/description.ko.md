[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Platform에서 비용과 성능을 맞바꿀 필요가 없다고 주장하는 모범 사례 글입니다(2026년 9월 8일,
이후 Opus 5.5 벤치마크 추가). 프롬프트 캐시 적중 극대화, 프런티어 모델로 옮길 때 프롬프트 안티패턴 제거,
작업에 맞는 effort 보정이라는 세 가지 레버가 보통 둘 다 개선합니다. 이 지침은 `claude-api` 스킬로
제공됩니다.

## 언제 유용한가요
- API 비용이 높거나 캐시 적중률이 낮을 때.
- 새 모델로 옮겼지만 예전 프롬프트·스킬·도구 설명을 그대로 쓰고 있을 때.
- eval을 기준으로 모델과 effort 수준을 고를 때.

## 핵심 포인트
- 프롬프트 캐시: 특정 모델에 고정, 접두부가 바이트 단위로 같아야 하고 기본 TTL은 5분. 타임스탬프·ID나
  순서가 바뀌는 도구를 접두부에서 빼고, `defer_loading`을 쓰고, 시스템 프롬프트 변경은 메시지로 보내고,
  `max_tokens: 0`으로 미리 데우고, 긴 대기에는 1시간 TTL을 고려합니다.
- 안티패턴: 검증 의식, 철저함 강조, 스크래치패드 틀, 낡은 예시, 모순된 규칙, 오래된 설정.
  `/claude-api prompt-audit`이 찾아 주며, 사례 연구에서 비용을 추가로 약 9% 줄이고 정확도를 약 2%p 높였습니다.
- Effort: 너무 높으면 과하게 생각하고, 너무 낮으면 근거를 건너뜁니다. effort를 스윕하고 더 강한 모델을
  낮은 effort로 시험하세요. `/claude-api hillclimb`이 held-out 테스트 세트로 이 탐색을 자동화합니다.
- `/claude-api cost-optimize`는 레버(캐싱, 내용 축소, 출력 제한, Batch API)를 순위화하며, 공개
  벤치마크에서 품질 변화가 거의 없이 비용을 약 24~73% 줄였습니다.

## 번들 리소스
- 스킬: `api-cost-performance-tuning` (`references/prompt-cache-checklist.md`,
  `references/prompt-anti-patterns.md`, `references/benchmark-results.md`,
  `templates/cost-audit-report.md`).

## 출처
- https://claude.com/resources/articles/reducing-cost-and-improving-performance-with-claude-platform
