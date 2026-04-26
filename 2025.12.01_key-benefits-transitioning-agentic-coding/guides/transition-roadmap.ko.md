[English](./transition-roadmap.en.md) · **한국어** · [Español](./transition-roadmap.es.md) · [日本語](./transition-roadmap.ja.md)

# 전환 로드맵

[What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding) (2025-12-01)에서 정리한 짧은, 조직 단위 전환 가이드입니다. 단일 팀을 넘어 Claude Code 도입을 계획할 때 체크리스트로 사용합니다.

## 1. 메시지 프레이밍

청자에게 가장 와닿는 이점 2~3개를 선택합니다.

- 엔지니어링 리더십: 일정 단축 + 인력의 선형 증가 없는 스케일링
- 엔지니어링 매니저: 온보딩 압축 + 전문 역량 민주화
- 시니어 엔지니어: 자율 문제 해결 + 체계적 코드 품질
- 보안/플랫폼: 체계적 코드 품질 + 권한 모델
- 채용: 민주화(채용 전략 변화 — "기본기 + 에이전트가 보완하는 전문성")
- 재무: 일정 단축을 프로젝트 경제성과 연결

## 2. 근거로 뒷받침

- Augment Code의 2주 vs 4~8개월 엔터프라이즈 사례와 Guy Gur-Ari 인용: "Tasks that would take weeks for a developer to learn can now be completed in a day or two."
- Grafana의 자연어 PromQL/LogQL 어시스턴트(전문 역량의 민주화 사례).

## 3. 한 팀 파일럿

- 의지가 있는 시니어 챔피언이 있는 팀을 한 곳 선정.
- Claude Code를 터미널/IDE에 설치, 프로젝트 루트로 이동, `claude` 실행.
- 시작 작업 진행: 엔드포인트 에러 핸들링, 복잡한 컴포넌트 리팩터링, 미커버 코드의 테스트 작성.
- 파일럿 동안에는 모든 변경에 대해 쓰기 전 승인을 필수로.

## 4. 파일럿 종료 기준 정의

2~4주 뒤 다음을 평가합니다.

- 할당 작업의 사이클 타임을 파일럿 전 기준선과 비교
- 파일럿 기간 중 신규 합류자의 온보딩 시간
- 코드 품질 신호: 인시던트, PR당 리뷰 코멘트 수, 잡힌 결함
- 엔지니어 경험 신호: 엔지니어들이 계속 쓰고 싶어하는가

## 5. 신중한 확장

- 프로젝트 루트에 CLAUDE.md 추가 — 코딩 표준이 세션·컨트리뷰터 사이에 유지됨.
- 리포지토리 밖 도구(이슈 트래커·디자인 시스템·내부 문서)는 MCP 서버 연결로 통합.
- 책임 범위 정의 시 에이전트는 자율주행이 아니라 품질 게이트키퍼이자 사고 파트너로 위치시킴.

## 6. 결과 추적 및 공유

이점을 로컬 지표로 변환합니다. Augment Code의 2주 vs 8개월은 글의 페이싱 예시일 뿐, 팀별로 자체적인 사이클 타임·온보딩 시간·잡일 감소 수치를 공개해 리더십이 팀 간 도입 의사결정을 비교할 수 있게 합니다.

## 출처

[What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding) (게시일 2025-12-01).
