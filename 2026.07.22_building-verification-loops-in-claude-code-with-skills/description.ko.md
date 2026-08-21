[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Code 팀의 Delba de Oliveira가 변경할 때마다 반복하는 수동 체크를 스킬로 바꿔 Claude가 스스로 피드백 루프를 닫게 만드는 방법을 설명합니다. 대부분의 에이전틱 코딩 세션은 컨텍스트 수집 → 행동 → 결과 검증 → 필요 시 되돌아가기라는 루프를 따르고, Claude는 이미 코드베이스의 결정론적 신호(타입 체커, 린터, 테스트, 런타임 오류)를 보고 일부를 스스로 검증합니다. Claude가 추론할 수 없는 나머지가 바로 사람이 손으로 밟는 단계이며, 그것이 인코딩할 가치가 있는 단계입니다.

글은 먼저 시도해볼 내장 루프들, 검증 스킬의 최소 `SKILL.md` 형태, 그리고 체크를 배치하는 네 가지 방식 — 독립 실행, 산출 스킬에 임베드, 다른 스킬 뒤에 체이닝, 모든 PR에서 실행 — 을 각각의 적합한 상황·비용·졸업 신호와 함께 다룹니다.

## 언제 유용한가요
- Claude가 기능을 구현할 때마다 매번 같은 작은 수정을 반복하고 있을 때.
- 프로젝트 고유의 규칙이 분명 존재하지만 일반 린터로는 잡히지 않을 때.
- 새 프로젝트를 시작하며 프로젝트가 어떻게 동작해야 하는지 적어둬야 할 때.
- 체크를 의도적으로 호출할지, 임베드할지, 체이닝할지, 팀 전체 PR 게이트로 만들지 정할 때.
- 편집할 수 없는 스킬(내장 또는 플러그인 관리 스킬)에 검증을 붙이고 싶을 때.
- 개인의 습관이 팀 인프라가 될 준비가 되었을 때.

## 핵심 포인트
- **검증 루프는 에이전트가 자기 작업을 확인하는 반복 사이클입니다.** 테스트·린터·커스텀 체크를 돌리고, 실패한 것을 고친 뒤 다음으로 넘어갑니다. 스킬로 패키징하면 사람이 기억해내는 데 의존하지 않고 모든 세션이 같은 체크를 적용합니다.
- **내장 기능부터 시도하세요**: `/verify`, 툴체인 오류 코드(정확한 빌드·테스트 명령어를 `CLAUDE.md`에 명시), 리서치 프리뷰 Code Review, GitHub Actions, 스펙 검증, 그리고 별도의 채점 에이전트가 실패를 재작업 루프로 되돌리는 Claude Managed Agents의 루브릭.
- **체크는 입사 첫날의 새 팀원에게 건네듯 평범한 문장으로 쓰세요.** 말로 풀기 어렵다면 Claude에게 모범 사례를 먼저 물어보고 고쳐 나가세요. 여러분의 버전이 다른 지점이 바로 담아내야 할 내용입니다.
- **체크가 정성적일 필요는 없습니다.** "백필 단계 없이 컬럼을 삭제하는 마이그레이션은 거부한다"는 결정론적이고 프로젝트 고유이며, 일반 린터는 잡지 못합니다.
- **가장 단순한 검증 스킬은 몇 줄의 frontmatter와 본문이 전부입니다**: 무엇을 읽고, 무엇을 확인하고, 어떻게 보고하고 고칠지. 손으로 쓰기 싫다면 `skill-creator`가 인터뷰해 줍니다.
- **독립 실행**은 매번 적용되지 않는 횡단 체크에 어울립니다. 대가는 호출을 기억해야 한다는 점이고, 매 변경마다 돌리고 있다면 임베드하거나 체이닝하라는 신호입니다.
- **임베디드**는 산출 스킬 본문에 한 줄을 덧붙이는 것이지만, 편집할 수 있는 스킬에서만 동작합니다. 내장 스킬과 플러그인 관리 스킬은 업데이트 시 덮어써집니다.
- **체이닝**은 습관을 계약으로 바꿉니다. "나는 늘 `/simplify` 뒤에 `/verify`를 돌린다"가 "`/simplify`는 끝나면 항상 `/verify`를 돌린다"가 됩니다. Anthropic Claude Code 팀은 `/code-review` → `/simplify` → `/verify` → `/design`을 체이닝합니다. 유연성을 자동화와 맞바꾸며 토큰 소비가 늘 수 있습니다.
- **모든 PR에서** 돌리는 순간 검증은 개인 인프라를 넘어 팀 인프라가 됩니다. 다만 체인이 아직 유동적일 때는 미루세요. 조정 하나하나가 팀 전체에 보이는 이벤트가 됩니다.

## 번들 리소스
- `skills/verification-loop-builder/SKILL.md` — 내장 루프, 체크 작성법, 네 가지 배치 패턴, 여섯 단계 제작 프로세스.
- `skills/verification-loop-builder/templates/verification-skill.md` — frontmatter + 본문의 최소 형태와 각 필드 작성 지침.
- `skills/verification-loop-builder/templates/wrapper-chain-skill.md` — 수정할 수 없는 스킬에 체이닝하는 래퍼 패턴.
- `skills/verification-loop-builder/examples/verify-log-hygiene.md` — 글에 나온 로그 위생 스킬 완성본.
- `skills/verification-loop-builder/examples/scaffold-component-embedded.md` — 컴포넌트 스캐폴딩 스킬 안의 한 줄 임베드.
- `skills/verification-loop-builder/references/built-in-loops.md` — 여섯 가지 내장 검증 방식 상세.
- `skills/verification-loop-builder/references/deployment-patterns.md` — 독립 실행·임베디드·체이닝·PR 전역과 각각의 비용 및 졸업 신호.
- `guides/verification-loops.{en,ko,es,ja}.md` — 4개 언어 전체 해설.

## 출처
[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) — Delba de Oliveira, 2026년 7월 22일.
