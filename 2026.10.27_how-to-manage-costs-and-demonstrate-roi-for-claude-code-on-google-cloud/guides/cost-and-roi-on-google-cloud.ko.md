[English](./cost-and-roi-on-google-cloud.en.md) · **한국어** · [Español](./cost-and-roi-on-google-cloud.es.md) · [日本語](./cost-and-roi-on-google-cloud.ja.md)

# Google Cloud 의 Claude Code 비용과 ROI: 통제 -> 추적 -> 증명

Google Cloud 에서 Claude Code 를 운영하는 플랫폼 팀을 위한 Anthropic 지침을 방법론 중심으로 정리했습니다.

## 1. 청구액이 이렇게 나오는 이유
Google Cloud 의 Claude 는 사용량 기반 과금입니다. 도입이 사용량을 만들고, 사용량이 곧 비용이며, 가치도
거기서 나옵니다. 비용 = 작업당 토큰 × 모델 가격. 에이전트형 도구는 파일을 읽고 도구를 실행하며 작업
전체를 추론하므로 채팅보다 작업당 토큰을 더 씁니다. 작업에 맞는 모델 선택이 또 하나의 큰 통제
수단입니다. 가시성은 Claude apps gateway 와 Google Cloud 서비스에서 얻습니다.

## 2. 도구 상자
| 계층 | 기능 |
|---|---|
| Google Cloud | 프로젝트별 결제, 예산·알림, 지출 상한(Preview), BigQuery 내보내기, 할당량(모델 계열·위치별 분당 요청·입출력 토큰), 프로비저닝된 처리량 |
| Claude apps gateway | 같은 `claude` 바이너리에 들어 있는 자체 호스팅 서비스로 프로젝트 안에서 실행. IdP 로그인(예: Google Workspace)으로 모든 요청에 검증된 신원. 그룹별 모델 허용 목록. 사용자·IdP 그룹·조직 단위 일·주·월 지출 상한 |

## 3. 레버 1 - 통제
제한하지 말고 이끕니다. 고비용 세션은 가치 높은 작업을 하는 파워 유저인 경우가 많고, 낭비는 고액
사용자의 중간층(일상 작업에 비싼 모델, 잊힌 예약 작업)에 있습니다.
- **지출 상한**: 사용자·그룹·조직 단위. 그룹·조직 상한은 공유 풀이 아니라 구성원마다 상속되는 1인당 기본값.
- **임계 알림**: 75%·95% 초과 시 CLI 안 경고, 상한에서 재설정이나 상향 전까지 429. Cloud Billing 알림은 관리자용.
- **기본 모델·허용 목록**: IdP 그룹별, 서버 측에서 강제. 대부분은 기본값을 그대로 씁니다.
- **Gateway admin API**: 티켓 등에서 상한을 프로그래밍 방식으로 변경.

## 4. 레버 2 - 추적
- Claude Code OpenTelemetry: 세션, 활성 시간, 코드 줄 수, 커밋, PR, 토큰, 비용 - 사용자·팀·모델별, 이제
  스킬·플러그인·에이전트·MCP 서버별까지. 컬렉터나 gateway 를 거쳐 OTLP 로 보냅니다.
- Gateway 텔레메트리: 목적지 하나로 전원 적용, 검증된 이메일과 IdP 그룹으로 태그.
- `OTEL_RESOURCE_ATTRIBUTES`(예: `department=engineering,cost_center=eng-123`)로 Cloud Monitoring·Grafana·Splunk 에서 비용 센터별 보기.
- 대시보드: 활성 개발자, 최근 24시간 세션, 토큰, 차단된 요청(상한 상향 티켓 흐름과 짝지음).
  "Claude Code Monitoring" 템플릿은 Cloud Monitoring 콘솔에서 복사할 수 있습니다.
- OTel 퀵스타트: Cloud Logging·Monitoring 과 이벤트 유형별(API 요청, 도구 결정, 도구 결과, 어시스턴트
  응답, 훅 실행) 파티션 BigQuery 테이블, 개발자·모델별 지출, 도구 성공률·지연, 훅 대기 시간, 턴·세션
  분석용 SQL 제공.
- Cloud Billing → BigQuery: 모델·토큰 유형별로 Claude SKU 필터링.

## 5. 레버 3 - 증명
| 차원 | 예시 | 출처 |
|---|---|---|
| 도입·사용 | 활성화 사용자, 일·주간 사용, 유지율, 파워 유저 | OTel |
| 만족도 | 만족감, 체감 시간 절약, 결과물 신뢰도, 마찰 | 도입 전후 설문 + 정기 점검 |
| 임팩트 | 시간(PR 오픈 -> 병합, 리뷰 회신), 노력(PR당 리뷰 반복·코멘트·재작업), 양(엔지니어당 PR, 배포 빈도, 이름 붙은 작업 묶음) | 소스 관리 + 티켓 기준선 |

**작업 단위**: 정의된 종류의 병합 PR(Claude 가 열고 사람이 출시 여부 결정)을 라벨, 티켓 ID, Claude 관여
여부로 찾아 셉니다. PR 이 아닌 작업은 끝난 한 가지를 그것이 기록되는 곳에서 셉니다.

**네이티브 텔레메트리**: 수락률, 수정한 줄 수, 커밋, 생성한 PR, 사용자당 PR, 산출 단위당 비용. 생성된
PR 은 병합된 PR 이 아니므로 GitHub·GitLab·티켓과 대조합니다. 프롬프트 로깅은 옵트인이며 PR 이 아닌
가치(인시던트를 디버깅하는 SRE, 데모 데이터를 만드는 세일즈 엔지니어)를 보여 줍니다.

## 6. 참고 성과
- Delivery Hero: UI 컴포넌트 100개에 걸친 디자인 시스템 개편을 약 1주 대신 몇 분 만에.
- Shopify: 비엔지니어가 내부 도구를 며칠 대신 몇 분 만에 구축.
- Fifth Dimension: 월 30만 줄 이상, 수락률 98%.

## 7. 시작하기
연속 루프를 돌립니다. 조직 전체 지출 상한, 기본 모델, 모델 허용 목록으로 시작하고, 데이터가 쌓이면
역할·팀별로 다듬고, 지표를 가치와 연결해 이해관계자에게 보고합니다.

## 출처
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
