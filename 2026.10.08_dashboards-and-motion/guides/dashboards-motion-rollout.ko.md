[English](./dashboards-motion-rollout.en.md) · **한국어** · [Español](./dashboards-motion-rollout.es.md) · [日本語](./dashboards-motion-rollout.ja.md)

# Dashboards·Motion 도입과 Claude Design 이전

2026년 10월 8일 발표를 바탕으로 한 관리자·팀 리드용 체크리스트입니다.

## 1. 한눈에 보는 제공 범위
| 기능 | 상태 | 플랜 | Enterprise 기본값 |
|---|---|---|---|
| Claude Dashboards | 베타 | 유료 플랜 | 꺼짐 (Organization settings > Artifacts) |
| Claude Motion | 베타 | Team, Enterprise | 꺼짐 (Organization settings > Artifacts) |
| Claude Docs, Slides, Design | 정식 출시 | Free 포함 전 플랜 | 10월 15일부터 기본 켜짐 (미리 켤 수 있음) |

## 2. Dashboards를 켜기 전에
- 연결할 데이터 플랫폼(Amazon Redshift, BigQuery, ClickHouse, Databricks, Snowflake)과 대시보드가 쓸
  수 있는 다른 커넥터(예: Salesforce)를 정합니다.
- Dashboards는 빠르고 탐색적인 질문용으로 자리매김합니다. 더 깊은 분석이 필요할 때 대시보드를 넘길 BI
  도구를 합의합니다(Amplitude, Grafana, Hex, Mixpanel, Omni, Perplexity, PostHog, Sigma; Databricks
  Genie, Looker, monday.com, Tableau는 지원 예정).
- 검증 습관을 교육합니다: 숫자를 클릭해 쿼리 보기, Claude에게 설명 요청, 차트별 마지막 새로고침 시각 확인.

## 3. Motion을 켜기 전에
- Motion은 자신의 작업을 설명하기 위한 도구입니다. 텍스트·차트·도형·이미지를 코드로 움직입니다. 영상
  생성 모델을 쓰지 않으므로 생성된 영상도, AI가 만든 사람도 없습니다.
- 출력: MP4 다운로드, 또는 Adobe, Descript, HeyGen, Higgsfield, invideo, Luma AI, Runway에서 열기
  (Canva, Captions는 지원 예정).

## 4. 이제 아티팩트에 쓸 수 있는 Enterprise 통제
- 아티팩트 CMEK 지원.
- 조직이 사용할 아티팩트 템플릿을 관리자가 선택.
- 조직 외부 공유나 링크 소지자 공유는 관리자가 허용한 경우에만.

## 5. Claude Design 이전 (마감: 12월 14일)
Claude Design은 claude.ai/design에서 시작했고, 9월 16일부터 모든 Claude 대화 안에서도 동작합니다. 독립
사이트는 12월 14일까지 유지됩니다.
- [ ] **디자인 시스템 이전.** Artifacts 페이지에서 "Migrate team design systems"를 클릭합니다. 한 번의
  이전으로 조직의 모든 디자인 시스템이 옮겨지고, 원본은 종료 때까지 독립 버전에 그대로 남습니다.
- [ ] **프로젝트.** 아직 할 일은 없습니다. 종료 때까지 독립 버전에서 계속 동작합니다.
- [ ] **채팅·코멘트 보관.** 독립 버전에만 남으며 종료 후에는 볼 수 없습니다.
- [ ] **공개 링크.** 독립 프로젝트 링크는 종료와 함께 끊기므로 대체 링크를 준비합니다.
- 자세한 내용은 원문에 링크된 마이그레이션 가이드를 참고하세요.

## 출처
- https://claude.com/resources/articles/dashboards-and-motion
