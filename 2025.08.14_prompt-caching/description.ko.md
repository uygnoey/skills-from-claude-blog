[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude의 프롬프트 캐싱

## 이 글이 뭔가요

Anthropic API의 프롬프트 캐싱 출시 발표 글입니다. 어떤 상황에 캐싱이 효과적인지, 출시 시점 모델(Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku), 세 가지 레퍼런스 워크로드의 지연/비용 감소 수치, 가격 모델(캐시 쓰기는 기본 input 대비 +25%, 캐시 읽기는 기본 input의 10%), 그리고 Notion 고객 사례를 다룹니다. 2024-12-17 업데이트 노트는 Anthropic API에서 **GA**로 승격, Amazon Bedrock과 Google Cloud Vertex AI에서 **프리뷰**로 제공됨을 알립니다.

## 언제 유용한가요

- 기존 Claude 연동에서 프롬프트 캐싱이 적절한 레버인지(짧게 줄이기·스트리밍·배칭·모델 변경과 비교) 판단할 때
- 본문의 세 벤치마크와 유사한 워크로드에서 지연/비용 절감을 가늠할 때
- 캐시 적중을 극대화하는 프롬프트 구조 설계 — 무엇을 캐시 prefix에 두고 무엇을 동적으로 유지할지 정할 때
- 공개된 수치(긴 프롬프트에서 비용 최대 90% 감소, 지연 최대 85% 감소; 100k 토큰 "책과 대화" 워크로드에서 TTFT 79% 개선)를 인용할 때

## 핵심 포인트

- 프롬프트 캐싱은 API 호출 간 자주 쓰는 컨텍스트를 캐시합니다. 큰 컨텍스트를 한 번 보내고 반복 참조하는 시나리오에서 사용합니다.
- 핵심 수치: 긴 프롬프트에서 **비용 최대 90% 감소**, **지연 최대 85% 감소**. 출시 시점에는 Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku에서 public beta(원문 기준), 이후 2024-12-17 업데이트로 GA.
- 글이 열거한 사용 사례: 대화형 에이전트, 코딩 어시스턴트, 대형 문서 처리, 상세 지시 세트(고품질 예시 수십 개 포함), 에이전틱 검색·툴 사용, 책/논문/문서/팟캐스트 등 장문 콘텐츠와의 "대화" 경험.
- 본문에 등장한 레퍼런스 워크로드:
  - 책과 대화(10만 토큰 캐시 프롬프트): TTFT 11.5s → 2.4s(-79%), 비용 -90%
  - Many-shot prompting(1만 토큰): TTFT 1.6s → 1.1s(-31%), 비용 -86%
  - 멀티턴 대화(긴 시스템 프롬프트 + 10턴): TTFT 약 10s → 약 2.5s(-75%), 비용 -53%
- 가격 모델: 캐시에 쓸 때는 모델별 기본 input 토큰 가격 대비 **+25%**, 캐시에서 읽을 때는 기본 input 가격의 **10%**.
- 고객 사례: Notion이 Notion AI 기능에 프롬프트 캐싱을 적용해 내부 운영을 최적화하고 응답성을 개선. Simon Last(Notion 공동 창업자) 인용: "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality."
- 2024-12-17 업데이트: Anthropic API에서 **GA**, Amazon Bedrock과 Google Cloud Vertex AI에서 **프리뷰** 제공.

## 번들 리소스

- [skills/prompt-caching-design-patterns/SKILL.md](./skills/prompt-caching-design-patterns/SKILL.md): 사용 시점, 캐시 적중을 위한 프롬프트 구조, 효과 추정 방법
- [references/use-cases-and-benchmarks.md](./skills/prompt-caching-design-patterns/references/use-cases-and-benchmarks.md): 출시 시 사용 사례 목록과 레퍼런스 워크로드 표 원문 그대로
- [examples/prompt-structure-patterns.md](./skills/prompt-caching-design-patterns/examples/prompt-structure-patterns.md): 캐시 prefix vs 동적 suffix 패턴 예시

## 출처

[Prompt caching with Claude](https://claude.com/blog/prompt-caching) (게시 2025-08-14, 2024-12-17 업데이트로 Anthropic API GA + Bedrock·Vertex AI 프리뷰) 내용을 바탕으로 정리했습니다.
