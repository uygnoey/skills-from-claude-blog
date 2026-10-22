[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic 엔지니어가 에이전틱 코딩으로 CI 잡이 6개월 만에 약 25배 늘어난 과정, 팀의 테스트 영향
분석(테스트 선택) 서비스가 병목이 될 뻔한 경위, 점점 짧아지는 세 번의 패치를 무상태 재설계로 대체한
이유를 설명합니다. 핵심 교훈은 "언제나 기하급수적 증가에 대비하라"입니다.

## 언제 유용한가요
- 에이전트가 작성한 PR 때문에 CI 물량이 인원보다 빠르게 늘어날 때.
- 테스트 선택 서비스가 지연되거나 호출(page)이 잦거나 메모리 한계에 부딪힐 때.
- 또 한 번의 임시방편과 재설계 사이에서 고민하거나, 새 CI 서비스의 규모를 정할 때.

## 핵심 포인트
- 엔지니어의 분기당 코드 배포량은 2021~2025년 대비 약 8배, 그중 약 80%를 Claude가 작성. 테스트는
  약 10배, CI 잡은 6개월 동안 약 25배 증가.
- 서비스는 리스너(결과 기록)와 셀렉터(PR별 테스트 선택)로 구성. 리스너가 밀리면 선택이 오래된
  데이터로 이뤄져 공동 실패, 불안정 테스트로 인한 머지 차단, 새로 추가·수정된 테스트 미실행이 발생.
- v0는 단일 writer 프로세스. 패치가 버틴 기간은 계속 짧아짐: 더 큰 머신(약 70일), 패키지별
  샤딩(29일), 매일 재시작(하루 미만).
- 장기 실행 Claude Tag 세션이 지연을 모니터링(5만 잡에서 알림)했고 꾸준히 전면 개편을 권함.
- 재설계: 상태를 인메모리 스토어로, 무상태 리스너 워커가 저널에 append, 컨슈머가 몇 초마다 테스트별
  이력으로 롤업. 엔지니어 한 명이 3주, 튜닝은 Claude가 대부분 자율 수행, 백로그는 평탄하게 유지.
- 조언: 두 분기 안에 25배 부하를 가정, 예산이 허락하면 v0를 10~20배로 설계, 상태는 프로세스 밖에,
  핵심 서비스의 단일 인스턴스 운영 지양, 들어온 잡 수와 나간 잡 수가 같은지 계측.

## 번들 리소스
- Skill: `agent-scale-ci-test-selection` — 리스너/셀렉터 모델, 지연 비용, 패치 수명, 무상태 재설계,
  계획 원칙 (`references/scaling-timeline.md`, `templates/ci-scaling-review.md`).
- Guide: `stateless-test-impact-analysis` (en/ko/es/ja) — 아키텍처와 계획 원칙.

## 출처
- https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
