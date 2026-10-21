[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude for Google Workspace가 모든 유료 Claude 플랜에서 퍼블릭 베타로 나왔다는 발표입니다. 열어 둔
Google 문서, 시트, 슬라이드 옆에 Claude 사이드바가 열리고, 파일을 읽고 선택 영역을 보고 바로 편집할
수 있습니다. 새로 나온 Google Docs·Sheets·Slides 커넥터(베타)로는 Claude 채팅에서 Google 파일을
만들고 편집할 수도 있습니다.

## 언제 유용한가요
- 이미 열어 둔 Google 파일 안에서 Claude에게 편집·분석·작성을 맡기고 싶을 때.
- Claude에서 시작해 새 문서·시트·덱을 만들거나 여러 파일에 걸쳐 작업할 때.
- 관리자가 도메인 전체나 그룹 단위 배포를 계획할 때.

## 핵심 포인트
- Docs: 작은 수정은 그 자리에서 바로, 큰 재작성은 적용·무시할 수 있는 제안 카드로 나옵니다.
- Sheets: 수식, 피벗 테이블, 기본 차트, 새 탭, 그리고 범위에 Python을 실행해 데이터를 정리·결합한
  뒤 결과를 다시 씁니다.
- Slides: 덱의 레이아웃과 테마로 슬라이드를 만들고, 겹치거나 슬라이드 밖으로 나간 요소와 읽기 어려운
  텍스트를 점검합니다.
- 편집 모드: "Ask before edits"(기본값, 변경마다 승인 카드) 또는 "Accept all edits".
- 사이드바도 일반 Claude와 같은 모델·커넥터·스킬을 쓰며, 엔터프라이즈 통제(Compliance API, 고객 관리
  암호화 키, OpenTelemetry 감사 내보내기)도 적용됩니다.
- 파일 접근은 기존 Google 공유 권한을 따릅니다.
- 설정: Google Workspace Marketplace에서 설치 후 확장 프로그램 > Claude > Open Claude. 관리자는 Google
  관리 콘솔에서 도메인이나 그룹에 배포할 수 있고, Team·Enterprise 플랜에서는 소유자 또는 기본 소유자가
  먼저 커넥터를 켜야 합니다.

## 번들 리소스
- 스킬: `google-workspace-editing` — 애드온과 커넥터 중 고르기, 편집 모드, 앱별 작업 패턴.
  작업 예시는 `examples/task-prompts.md`.
- 가이드: `google-workspace-rollout`(en/ko/es/ja) — 개인 설정과 조직 도입.

## 출처
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
