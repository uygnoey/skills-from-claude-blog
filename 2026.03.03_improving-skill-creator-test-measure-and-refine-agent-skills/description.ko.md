[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요

이 글은 Agent Skills 작성·유지보수를 돕는 “skill-creator”의 업데이트를 소개하며, 모델이 변해도 스킬이 계속 잘 동작하도록 테스트(evals), 벤치마크, 비교 평가, 트리거 설명 튜닝을 지원한다고 설명합니다.

## 언제 유용한가요

스킬을 장기간 운영하면서 회귀(regression)를 빨리 감지하고, 개선 효과를 측정하고, 버전 간 비교를 수행하고, 스킬 설명을 다듬어 필요한 순간에 안정적으로 트리거되게 만들고 싶을 때 유용합니다.

## 핵심 포인트

- 스킬은 “capability uplift(능력 보강)”과 “encoded preference(선호·프로세스 인코딩)” 두 부류로 나뉠 수 있다고 설명합니다.
- skill-creator는 테스트 프롬프트(필요 시 파일 포함)와 “좋은 결과의 기준”을 정의해 evals(테스트)를 작성·실행하도록 지원합니다.
- evals는 모델 변경으로 인한 품질 회귀를 잡고, 기본 모델이 capability uplift 스킬을 ‘따라잡았는지’도 판단하는 데 도움 됩니다.
- 벤치마크 모드는 eval pass rate, 실행 시간, 토큰 사용량을 추적하는 표준화된 평가를 제공합니다.
- 멀티 에이전트 지원으로 eval을 병렬 실행하며, 각 실행은 독립 컨텍스트/토큰/시간 지표를 갖습니다.
- comparator agent는 두 스킬 버전 또는 스킬 vs 무스킬을 블라인드 A/B로 비교해 실제 개선 여부를 판단합니다.
- 트리거 신뢰도를 위해, skill-creator가 설명을 분석하고 false positive/false negative를 줄이는 편집을 제안합니다.

## 번들 리소스

- Skill: evals/벤치마크/설명 튜닝으로 Agent Skills를 유지보수하는 실전 플레이북.
- Reference: capability uplift vs encoded preference 정의.

## 출처

- https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
