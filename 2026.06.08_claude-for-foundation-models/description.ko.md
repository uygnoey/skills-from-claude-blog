[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Apple Foundation Models 프레임워크에서 Claude를 쓰는 방법

## 이 글이 뭔가요
Anthropic이 Apple의 Foundation Models 프레임워크를 Claude와 연결하는 새로운 Swift 패키지를 소개합니다. 온디바이스 모델로 간단한 작업을 처리하고, 더 복잡한 요청은 Claude로 자연스럽게 넘기는 패턴을 설명합니다.

## 언제 유용한가요
- 빠르고 프라이빗한 온디바이스 요약/추출은 유지하면서, 멀티스텝 추론이 필요할 때 더 큰 모델로 매끄럽게 전환하고 싶을 때
- Apple의 guided generation으로 얻은 “타입이 있는 Swift 결과”를 Claude API 호출의 깔끔한 구조화 입력으로 쓰고 싶을 때

## 핵심 포인트
- 온디바이스 모델(요약, 추출 등)과 Claude(멀티스텝 추론, 코드 생성, 웹 검색, 데이터 분석용 코드 실행 등)를 작업 복잡도에 따라 분리해 사용합니다.
- Claude의 응답을 같은 UI 뷰로 스트리밍해 사용자 경험을 하나로 유지합니다.
- guided generation으로 생성된 타입 출력은 Claude 호출 시 원시 사용자 텍스트 의존도를 낮춰줍니다.

## 번들 리소스
- Apple Foundation Models 앱에서 “온디바이스 우선 → Claude 핸드오프” 패턴을 문서화한 재사용 가능한 Agent Skill( `skills/foundation-models-handoff/SKILL.md` )
- 배포를 위한 플러그인 번들 스캐폴드( `plugin/.claude-plugin/plugin.json` )

## 출처
- https://claude.com/blog/claude-for-foundation-models
