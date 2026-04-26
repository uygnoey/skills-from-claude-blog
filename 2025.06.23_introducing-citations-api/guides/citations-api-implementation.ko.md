[English](./citations-api-implementation.en.md) · **한국어** · [Español](./citations-api-implementation.es.md) · [日本語](./citations-api-implementation.ja.md)

# Citations API 구현 체크리스트

## 구축
- 대상 작업(요약, Q&A, 고객지원)과 인용이 필요한 범위를 정합니다.
- 소스 문서(PDF/텍스트)를 제공하고 청킹 전략을 선택합니다.
- 인용 표시 방식(인라인 마커, 각주, 원문 점프)을 설계합니다.

## 평가
- 인용 recall/precision을 측정합니다.
- 근거가 없는 질문에서 “소스에 없음” 비율을 추적합니다.

## 출처
- https://claude.com/blog/introducing-citations-api
