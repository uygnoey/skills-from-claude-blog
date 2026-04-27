[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Developer Platform의 **structured outputs(구조화 출력)** 기능을 소개합니다. API 응답이 사용자가 제공한 JSON 스키마 또는 tool 정의와 항상 일치하도록 보장할 수 있습니다.

## 언제 유용한가요
프로덕션 앱/에이전트가 구조화된 데이터를 안정적으로 받아야 할 때 유용합니다(예: 데이터 추출 파이프라인, 멀티 에이전트 간 통신, 여러 제약 필드를 정확히 채워야 하는 검색 도구 등).

## 핵심 포인트
- 구조화 출력은 스키마(또는 tool 스펙)에 대한 준수를 보장하여 파싱 오류와 tool 호출 실패를 줄입니다.
- 모델 성능에 영향을 주지 않으면서 프로덕션 신뢰성을 높이는 기능으로 설명됩니다.
- 데이터 추출, 멀티 에이전트 아키텍처, 복잡한 검색 도구 같은 활용 사례를 강조합니다.

## 번들 리소스
- Skill 번들: `skills/structured-outputs-reliability-guide/` (신뢰성 체크리스트 + 레퍼런스)

## 출처
- https://claude.com/blog/structured-outputs-on-the-claude-developer-platform
