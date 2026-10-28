[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
2026년 10월 28일 발표 글로, Claude Enterprise 에 세 가지 기능이 정식 출시(GA)되었다는 내용입니다.
스마트 리포트(smart reports)는 팀마다 Claude 로 무엇을 하고 비용이 얼마인지 보여 주고, 인앱 설문(in-app
surveys)은 구성원이 직접 느끼는 가치를 모으며, 풀링 그룹 예산(pooled group budgets)은 팀마다 공유 월 예산
하나를 둡니다.

## 언제 유용한가요
- Claude Enterprise 를 운영하면서 일부 팀이 이미 하고 있는 일을 모든 팀으로 넓히고 싶을 때.
- 투자 계획을 세우려고 도입 현황, 지출, 마찰 지점을 근거 있게 봐야 할 때.
- 많이 쓰는 사람은 월초에 개인 한도에 걸리고, 다른 사람은 예산을 남길 때.

## 핵심 포인트
- 스마트 리포트: 팀, 기간, 포함할 제품을 고릅니다. Claude 가 팀 대화 기록의 표본을 분석해 작업을
  워크스트림으로 묶고, 각각의 지출, 산출물, 흔한 마찰 지점(예: 빠진 커넥터, 실패한 도구 호출)을 보여 줍니다.
- 리포트마다 권고 목록이 하나로 정리됩니다. 스킬로 만들 반복 워크플로, 코드 저장소에 넣을 규칙 등입니다.
  발견 사항은 아티팩트로 공유할 수 있습니다. 모델 사용량·비용에 관한 맞춤 질문은 템플릿으로 저장할 수 있고,
  결제 권한 관리자는 리포트에서 바로 지출 한도를 올릴 수 있습니다.
- 소유자(Owner)는 관리자가 아닌 팀 리드에게 자기 그룹 리포트를 돌릴 권한을 줄 수 있습니다. 리포트는 도입
  이해와 투자 계획용이며, 개인 성과 평가나 고용 결정에 쓰지 않습니다.
- 인용된 고객: Monday, Slalom, Wix, Deloitte, DoorDash, Docusign.
- 인앱 설문: 가치 중심 기본 질문 4개(최근 가장 가치 있었던 사용, 걸린 시간의 변화, 동료가 따라 할 만한
  사용, 내일 접근이 끊기면 먼저 멈출 일). 관리자가 질문, 대상, 시기, 위치를 바꿀 수 있고, 구성원은 답변 뒤에
  짧은 카드로 봅니다. 응답은 스프레드시트로 내보냅니다. 고객 관리 키(CMEK)와 함께 쓸 수 있고 조직 전체
  보존 기간을 따릅니다.
- 풀링 그룹 예산: 그룹마다 공유 월 예산 하나와, 가드레일로서의 구성원 한도. 모든 요청이 둘 다에서 차감되고
  먼저 소진되는 쪽에서 멈춥니다. 구성원은 Claude 안에서 증액을 요청할 수 있습니다. 설정 시 최근 사용량
  기반 금액을 제안하고, 결제 권한 관리자는 50%, 75%, 95%, 100% 에서 이메일 알림을 받습니다.
- 가용성은 구성(예: HIPAA, 고객 관리 암호화 키)에 따라 다릅니다. Help Center 를 참고하세요.

## 번들 리소스
- 스킬: `enterprise-adoption-insights` (`references/smart-reports.md`, `references/pooled-group-budgets.md`,
  `templates/smart-report-run.md`, `templates/survey-questions.md`, `examples/customer-voices.md`).

## 출처
- https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets
