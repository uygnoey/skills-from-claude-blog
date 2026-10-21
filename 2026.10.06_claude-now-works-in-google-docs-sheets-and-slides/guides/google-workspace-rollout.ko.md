[English](./google-workspace-rollout.en.md) · **한국어** · [Español](./google-workspace-rollout.es.md) · [日本語](./google-workspace-rollout.ja.md)

# Claude for Google Workspace 도입하기

Google Docs, Sheets, Slides에서 Claude를 쓰는 방법은 두 가지다. 이 가이드는 개인 사용자와 조직
각각에서 어떻게 설정하는지 정리한다.

## 두 가지 사용 방식

| | 애드온(사이드바) | 커넥터(채팅에서) |
|---|---|---|
| 시작 지점 | 열어 둔 Google 파일 | Claude 대화 |
| 적합한 작업 | 지금 열린 파일 편집, 선택 영역 작업 | 새 파일, 여러 파일에 걸친 작업 |
| 상태 | 퍼블릭 베타, 모든 유료 Claude 플랜 | 베타 |
| 파일 접근 | 기존 Google 공유 권한을 따름 | 기존 Google 공유 권한을 따름 |

애드온도 일반 Claude와 같은 모델·커넥터·스킬을 쓴다.

## 개인 설정
1. Google Workspace Marketplace에서 Claude를 설치한다.
2. Docs, Sheets, Slides 파일을 열고 확장 프로그램 > Claude > Open Claude를 선택한다.
3. 편집 모드를 고른다. **Ask before edits**(기본값, 변경마다 승인 카드) 또는
   **Accept all edits**(멈추지 않고 바로 적용).
4. 채팅에서 작업하려면 Google Docs·Sheets·Slides 커넥터를 켠 뒤 파일 링크를 붙여 넣거나 새 파일을
   요청한다.

## 조직 도입
1. **애드온 배포**: Google 관리 콘솔에서 도메인 전체 또는 선택한 그룹에 배포한다.
2. **커넥터 활성화**: Team·Enterprise 플랜에서는 소유자 또는 기본 소유자가 먼저 Google 커넥터를
   켜야 사용자가 쓸 수 있다.
3. **엔터프라이즈 통제 확인**: Compliance API, 고객 관리 암호화 키, OpenTelemetry 감사 내보내기가
   애드온에도 그대로 적용된다.
4. **팀별 기본 편집 모드 정책 정하기**(예: 공유 파일은 "Ask before edits" 유지). 원문의 요구사항이
   아니라 권장 운영 방식이다.
5. **재사용 형식은 스킬로 공유**해 팀 결과물을 일관되게 만든다(예: 리뷰 덱 형식).

## 유의할 점
- 두 방식 모두 베타다.
- 원문은 버전 기록이나 되돌리기를 다루지 않는다. 도움말 센터의 설정 가이드를 참고한다.

## 출처
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
