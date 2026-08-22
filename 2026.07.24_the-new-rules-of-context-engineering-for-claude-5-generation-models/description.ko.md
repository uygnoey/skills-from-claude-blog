[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Thariq Shihipar가 Claude 5 세대 모델이 등장하면서 컨텍스트 엔지니어링에서 무엇이 달라졌는지를 설명한다. 출발점은 하나의 사실이다. Anthropic은 이 모델들을 위해 Claude Code 시스템 프롬프트의 80% 이상을 제거했고, 코딩 평가에서 측정 가능한 성능 저하는 없었다.

진단은 기존 방식이 Claude에게 *족쇄*였다는 것이다. 규칙은 시스템 프롬프트, CLAUDE.md 파일, 스킬이라는 세 계층에 쌓이다가 서로 모순되기 시작했다. 한쪽은 문서를 적절히 남기라 하고, 다른 쪽은 주석을 달지 말라고 한다. 새 모델은 그런 발판 없이도 사용자 의도를 읽어내므로, 남는 것은 해로운 부분뿐이다. 글은 여섯 가지 전(前)/후(後) 전환을 제시하고, 이어서 조립된 컨텍스트의 각 계층이 이제 실제로 무엇을 위한 것인지를 다시 정의한다.

## 언제 유용한가요
- 시스템 프롬프트, CLAUDE.md, 스킬이 길어져 일부가 오히려 방해가 된다고 의심될 때.
- 컨텍스트의 두 계층이 동시에 따를 수 없는 지시를 내리고 있을 때.
- 이전 세대 모델에 맞춰 튜닝한 에이전트를 이전할 때.
- 도구를 예시로 가르칠지 시그니처로 가르칠지 결정할 때.
- 도구 사용 지침이 시스템 프롬프트와 도구 설명에 중복되어 있을 때.
- Claude가 참고할 명세의 형식을 고를 때.

## 핵심 포인트
- Claude 5 모델을 위해 **Claude Code 시스템 프롬프트의 80% 이상이 제거**되었고, 코딩 평가에서 측정 가능한 손실은 없었다.
- **규칙 → 판단.** "기본적으로 주석을 쓰지 말 것. 여러 문단짜리 독스트링이나 여러 줄 주석 블록은 절대 쓰지 말 것 — 최대 한 줄"이 "주변 코드처럼 읽히는 코드를 쓸 것: 주석 밀도, 이름 짓기, 관용구를 주변에 맞출 것"으로 바뀌었다.
- **예시 → 인터페이스 설계.** 사용 예시는 새 모델을 그 예시가 다루는 탐색 공간 안에 묶는다. 대신 표현력 있는 파라미터와 명확히 열거된 옵션에 지침을 담아라.
- **선(先)적재 → 점진적 공개.** 매 요청마다 모든 것의 비용을 치르는 대신 스킬과 지연 로딩 도구로 컨텍스트를 선택적으로 불러온다.
- **반복 → 하나의 도구 설명.** 이전 모델은 같은 지시가 시스템 프롬프트와 도구 설명 양쪽에 있을 때 이득을 봤지만, 지금 모델은 도구 설명을 안정적으로 참조한다.
- **수동 메모리 → 자동 메모리.** `#` 단축키로 컨텍스트를 고정하던 방식은, 작업과 사용자에게 관련 있는 것을 Claude가 보존하는 방식으로 대체된다.
- **단순한 명세 → 풍부한 레퍼런스.** HTML 아티팩트, 코드 레퍼런스, 테스트 스위트, 루브릭은 마크다운 계획서보다 적은 모호함으로 의도를 전달한다.
- **이제 각 계층은 하나의 역할을 맡는다.** 시스템 프롬프트는 제품 컨텍스트, CLAUDE.md는 함정에 집중한 가벼운 파일, 스킬은 팀의 관점을 담은 온디맨드 안내서, 레퍼런스는 @멘션으로 끌어오는 깊이(서술보다 코드 우선).
- Claude Code의 **`/doctor`**(CLI에서는 `claude doctor`)가 스킬, CLAUDE.md 파일, 시스템 프롬프트를 Claude 5 모델에 맞게 자동으로 적정 크기로 줄여준다.

## 번들 리소스
- `skills/context-engineering-for-new-models/SKILL.md` — 모순 찾기, 여섯 전환 적용하기, 각 계층 다시 쓰기, 그리고 측정하기.
- `skills/context-engineering-for-new-models/references/then-vs-now.md` — 여섯 전환 전체와 각 전/후 문구, 그리고 그 교체가 통하는 이유.
- `skills/context-engineering-for-new-models/references/context-layers.md` — 시스템 프롬프트, CLAUDE.md, 스킬, 레퍼런스가 지금 각각 무엇을 위한 것인지.
- `skills/context-engineering-for-new-models/templates/lightweight-claude-md.md` — 규칙집으로 자라버린 CLAUDE.md를 되돌릴 목표 형태와, 더 이상 여기 두지 말아야 할 것들.
- `skills/context-engineering-for-new-models/examples/rule-rewrites.md` — 네 가지 전/후 재작성: 주석 규칙, 예시로 가르치던 도구, 중복된 지시, 마크다운 명세.
- `guides/context-engineering-rules.{en,ko,es,ja}.md` — 4개 언어 전체 해설.

## 출처
[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) — Thariq Shihipar, 2026년 7월 24일.
