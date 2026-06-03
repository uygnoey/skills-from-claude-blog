[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Anthropic enables self-service data analytics with Claude

## 이 글이 뭔가요
이 글은 Anthropic이 Claude를 활용해 사내 비즈니스 애널리틱스 요청의 대부분을 자동화하는 방식과, 애널리틱스에서의 정확도가 단순한 SQL 생성 문제가 아니라 **컨텍스트·검색·검증** 문제라는 점을 설명합니다.

## 언제 유용한가요
데이터 웨어하우스를 기반으로 질문에 **신뢰성 있게** 답해야 하는 에이전틱 애널리틱스 워크플로(“애널리틱스 코파일럿”)를 만들 때 유용합니다. 특히 엔터티 모호성, 데이터 최신성(스테일), 검색(리트리벌) 누락 같은 실패를 줄이는 가드레일이 필요할 때 참고할 수 있습니다.

## 핵심 포인트
- 애널리틱스는 소프트웨어 개발과 다릅니다. 보통 데이터 모델의 **특정 최신 엔터티**에 연결된 단 하나의 정답이 존재합니다.
- 대표적인 실패 모드는 (1) 개념–엔터티 모호성, (2) 데이터 스테일(최신성 문제), (3) 리트리벌 실패입니다.
- Anthropic은 강한 데이터 파운데이션, 명시적인 소스 오브 트루스, 스킬 기반 절차 지식, 검증(오프라인 평가 + 온라인 모니터링)에 초점을 둡니다.
- 부록에 “웨어하우스 스킬” 스켈레톤과 도메인 테이블 레퍼런스 문서 스켈레톤이 포함됩니다.

## 번들 리소스
- 재사용 가능한 “웨어하우스 스킬” 스켈레톤(`skills/<skill-name>/SKILL.md`에 적합).
- 재사용 가능한 레퍼런스 문서 스켈레톤(`skills/<skill-name>/references/*.md`에 적합).

## 출처
- https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
