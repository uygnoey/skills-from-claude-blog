[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
베타 두 개와 정식 출시 하나를 알리는 글입니다. Claude Dashboards(베타, 유료 플랜)는 회사 데이터에 대한
자연어 질문을 항상 최신 상태로 유지되는 대시보드로 만들어 줍니다. Claude Motion(베타, Team·Enterprise)은
아이디어나 보고서를 편집 가능한 코드로 만든 애니메이션 설명 영상으로 바꿔 줍니다. Claude Docs, Slides,
Design은 베타를 벗어나 Free를 포함한 모든 플랜에서 쓸 수 있고, 독립 Claude Design 사이트는 Claude 안으로
통합됩니다.

## 언제 유용한가요
- 티켓을 올리거나 SQL을 쓰지 않고 데이터 웨어하우스나 CRM에서 빠르게 답을 얻고 싶을 때.
- 아이디어를 정적인 슬라이드 한 장보다 짧은 애니메이션으로 전달하는 편이 나을 때.
- Enterprise 관리자가 이 기능들을 켜거나 Claude Design 디자인 시스템을 이전하려 할 때.

## 핵심 포인트
- Dashboards는 Amazon Redshift, BigQuery, ClickHouse, Databricks, Snowflake와 Salesforce 같은 다른
  커넥터에 연결됩니다. 숫자를 클릭하면 그 쿼리를 볼 수 있고, 차트마다 마지막 새로고침 시각이 표시됩니다.
- 더 깊은 분석이 필요하면 대시보드를 Amplitude, Grafana, Hex, Mixpanel, Omni, Perplexity, PostHog,
  Sigma로 보낼 수 있습니다(Databricks Genie, Looker, monday.com, Tableau는 지원 예정).
- Motion은 텍스트·차트·도형·이미지를 움직이는 코드를 작성합니다. MP4로 내려받거나 Adobe, Descript,
  HeyGen, Higgsfield, invideo, Luma AI, Runway에서 열 수 있습니다. 영상 생성 모델을 쓰지 않으므로 생성된
  영상이나 AI가 만든 사람은 없습니다.
- Docs, Slides, Design(4,500만 개 이상 제작)이 정식 출시됩니다: 아티팩트 CMEK, 관리자가 고르는 템플릿,
  공동 편집, 허용 시 외부·링크 공유, 서식을 유지하는 PowerPoint/PDF 내보내기, 편집 가능한 Google Slides
  내보내기, 모바일 편집.
- 독립 claude.ai/design은 12월 14일까지 유지됩니다. Artifacts 페이지에서 팀 디자인 시스템을 이전하세요.
  독립 버전의 채팅·코멘트·공개 링크는 종료와 함께 사라집니다.
- Enterprise: Dashboards와 Motion은 기본 꺼짐(Organization settings > Artifacts), Docs·Slides·Design은
  10월 15일에 기본 켜짐으로 바뀝니다.

## 번들 리소스
- Skill: `live-dashboards-and-motion` — 검증 가능한 라이브 대시보드와 코드 기반 애니메이션 설명 영상
  만들기. 시작 프롬프트는 `examples/prompts.md`.
- Guide: "Dashboards·Motion 도입과 Claude Design 이전" (4개 언어).

## 출처
- https://claude.com/resources/articles/dashboards-and-motion
