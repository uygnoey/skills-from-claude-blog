[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic이 개발자가 Claude용 서드파티 확장을 만드는 기본 방식으로 플러그인을 열었다는 발표입니다.
플러그인은 MCP 커넥터, Agent Skills, 또는 둘 다를 묶으며, 승인된 플러그인은 Claude 디렉터리에
등록됩니다. 유료 Claude 플랜 개발자에게 제출 포털이 열렸습니다.

## 언제 유용한가요
- MCP 커넥터 하나만 낼지, 플러그인 번들 전체를 낼지 정할 때.
- 제출을 준비하면서 심사에서 무엇을 확인하는지 알고 싶을 때.
- 등록 후 리스팅 성과를 어떻게 측정할지 계획할 때.

## 핵심 포인트
- 제출 경로 두 가지: 단일 MCP 커넥터(원격 MCP 서버 지정) 또는 GitHub에 호스팅한 MCP 서버·스킬
  플러그인 번들. Claude Code 번들에는 LSP, 커맨드, 훅, 에이전트도 넣을 수 있습니다.
- 제출 시 자동 검증과 안전 스캔이 돌고, 포털에서 심사 상태·스캔 결과·권장 수정 사항을 봅니다.
  승인 후 공개 시점은 개발자가 정합니다.
- 분석: 제품 표면별·버전별 설치 수, 리스팅 조회수와 그 리스팅으로 이어진 검색어.
- 최신 MCP 스펙(stateless 코어)과 함께 MCP Apps(채팅 안 인터랙티브 UI), Enterprise Managed
  Auth(엔터프라이즈 사용자용 무개입 OAuth)를 지원합니다.
- Claude와 Claude Code에 하나의 탐색 경험이 도입될 예정이며, 기존 스킬·커넥터·플러그인은 바꿀
  필요가 없습니다. 이후 커넥터 리스팅을 플러그인으로 전환할 수 있게 됩니다.

## 번들 리소스
- 스킬: `plugin-directory-submission` — 제출 경로 선택, 심사 흐름, 공개, 분석, MCP 2.0 확장
  (`references/submission-portal.md`).

## 출처
- https://claude.com/resources/articles/build-plugins-for-claude
