[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
FedRAMP High 인가 환경에서 Claude 의 코딩·에이전트 작업 기능을 제공하는 Claude for Government 가
7월부터 이어 온 공개 베타를 마치고 미국 연방·주 정부 기관에 정식 출시(GA)되었다는 발표입니다.
Claude Code CLI 와 Claude for Microsoft 365 도 같은 환경에서 얼리 액세스로 제공되기 시작했습니다.

## 언제 유용한가요
- 기관이 Claude for Government 도입을 검토하거나 온보딩할 때.
- 관리자가 지출 상한, 좌석 등급, 하위 기관 관리를 설계할 때.
- 보안팀·인가 책임자가 ATO 나 감사관(IG) 요청에 쓸 근거를 모을 때.
- 조달 담당자가 GA 조건으로 Anthropic 과 직접 계약하려 할 때.

## 핵심 포인트
- 상용 고객과 비슷한 기능을 쓰며, 새 기능은 대체로 상용 출시 주기에 맞춰 들어옵니다. 직원은 데스크톱
  파일에서 skill·plugin·project 로 메모 작성, RFP 검토, 민원 처리 등을 하고, Claude Code 로 공공
  서비스 소프트웨어를 만들고 현대화합니다.
- 좌석 요금 없음: 고정 단위로 사용량을 구매하고 초과 불가 상한을 둡니다. 그룹별 지출·모델 한도,
  사용자·모델별 사용량 추적, 잔액 소진 전 알림을 제공합니다.
- 부처 관리자가 선불 사용량을 하위 기관에 배분하고, 하위 기관은 자기 사용자를 관리합니다. 기관 자체
  IdP 로 SSO(셀프 설정), SCIM 그룹 매핑으로 등급별 rate limit·금액 상한·허용 모델을 정하고, 계층형
  설정 기본값으로 연결 대상과 기능을 제어합니다.
- 감독: 관리 작업 감사 로그, Anthropic 측 민감 작업의 2인 승인, 미터링 데이터만 담은 사용량
  내보내기, 대화 기록은 기관 관리 기기에 로컬 보관.
- 별도의 클라우드 사업자 계약 불필요, MDM 배포, 앱 내 기록 가져오기, Anthropic trust center 의
  FedRAMP Secure Configuration Guide.

## 번들 리소스
- Skill: `government-agency-rollout` — 관리자·보안·조달 담당자를 위한 단계별 도입 계획과 관리자
  도입 체크리스트 템플릿.

## 출처
- https://claude.com/resources/articles/claude-for-government-is-now-generally-available
