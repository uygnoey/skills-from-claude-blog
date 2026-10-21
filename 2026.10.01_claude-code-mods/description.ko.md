[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Code 의 동작과 모양을 바꾸는 작은 TypeScript 함수인 mod 를 소개하는 글입니다. mod 는 프롬프트를
고쳐 쓰고, 새 UI 를 더하고, 내장 기능을 대체하거나, 완전히 새 기능을 추가할 수 있습니다. mod 는
plugin 안에 담겨 배포되며 Claude Code CLI 와 데스크톱 앱에서 동작합니다.

## 언제 유용한가요
- 기능 출시를 기다리지 않고 Claude Code 를 내 방식대로 바꾸고 싶을 때.
- hook 으로는 부족할 때 — 이벤트를 고쳐 쓰거나, UI 를 그리거나, 기능을 대체해야 할 때.
- 팀이 CI 상태, 운영 환경 보호, 감사 로그 같은 자체 통제를 만들고 싶을 때.
- 관리자가 사용자가 설치할 수 있는 mod 를 통제해야 할 때.

## 핵심 포인트
- Claude Code 는 무언가 할 때마다 이벤트를 냅니다(도구 호출, 권한 요청, 화면 일부 그리기). mod 는
  이벤트에 걸려 그 앞·뒤·대신, 또는 감싸서(앞뒤 모두) 실행됩니다.
- 함수 하나로 프롬프트 재작성, 도구 호출 차단·재작성·재시도, 권한 승인·거부, 도구 출력의 비밀값
  가리기를 할 수 있습니다. UI 를 고치거나 바꾸고 버튼·입력란을 더할 수도 있으며, 대상은 터미널,
  데스크톱 앱, 또는 둘 다입니다.
- 같은 이벤트의 mod 들은 로드 순서대로 실행됩니다. 먼저 로드된 mod 가 이벤트를 가장 먼저, 결과를 가장
  나중에 봅니다. 그래서 여러 작성자의 mod 를 쌓을 수 있습니다.
- 내장 기능이 mod 로 옮겨지는 중입니다 — `/diff` 는 이제 mod 이며 `/plugin` 에서 끄거나 대체할 수
  있습니다.
- mod 는 샌드박스가 없으므로 신뢰하는 출처에서만 설치합니다. 기존 plugin 통제가 그대로 적용되고,
  Team/Enterprise 또는 managed settings 가 있는 기기에서는 내장 `sec-default` mod 가 먼저 로드되어
  권한 deny 규칙 무시 같은 위험한 동작을 막습니다.
- Claude Code 에게 mod 를 만들어 달라고 하면 TypeScript 작성, 설치, 세션 내 hot reload 까지 해 줍니다.

## 번들 리소스
- Skill: `plan-code-mods` — mod 의 범위(이벤트, 단계, 화면, 로드 순서) 정하기, mod 와 hook 중 선택,
  팀 단위 통제 방법과 mod 설계 워크시트.

## 출처
- https://claude.com/resources/articles/claude-code-mods
