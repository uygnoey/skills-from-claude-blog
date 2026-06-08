[English](./foundation-models-handoff.en.md) · **한국어** · [Español](./foundation-models-handoff.es.md) · [日本語](./foundation-models-handoff.ja.md)

# Apple Foundation Models → Claude 핸드오프 설계

이 가이드는 Claude 공식 블로그 글의 통합 접근을 반복 가능한 설계 체크리스트 형태로 정리한 것입니다.

## 글에서 설명하는 내용
- Swift에서 Apple의 Foundation Models 프레임워크를 사용해 요약/추출 같은 온디바이스 작업을 수행합니다.
- 사용자 요청이 더 복잡한 처리를 필요로 하면, Claude를 호출해 멀티스텝 추론, 코드 생성, 웹 검색, 데이터 분석을 위한 코드 실행 등을 수행합니다.
- Claude의 응답을 같은 UI 뷰로 스트리밍해 흐름을 하나로 유지합니다.

## 권장 워크플로 구조
1. **온디바이스 패스(빠르고 로컬)**
   - 무엇을 추출/요약할지 정의합니다.
   - guided generation을 활용해 타입이 있는 Swift 값을 생성하는 것을 선호합니다.
2. **Claude로 에스컬레이션(복잡)**
   - 타입 값을 Claude 입력으로 사용해 입력을 정제합니다.
   - Claude에 멀티스텝 추론을 요청해 최종 답을 생성합니다.
3. **단일 UX 표면**
   - Claude 출력 스트리밍을 통해 동일한 뷰에서 연속적인 상호작용으로 보이게 합니다.

## 글에 나온 예시 활용처
- 저널링 앱: 온디바이스 일일 프롬프트 → Claude가 수개월 기록에서 공통 스레드를 탐색
- 학습 앱: 온디바이스 정의 → Claude가 더 깊은 개념적 후속 질문에 답변

## 출처
- https://claude.com/blog/claude-for-foundation-models
