[English](./verification-loops.en.md) · **한국어** · [Español](./verification-loops.es.md) · [日本語](./verification-loops.ja.md)

# Claude Code에서 스킬로 검증 루프 만들기

## 에이전틱 루프

대부분의 에이전틱 코딩 세션은 하나의 루프를 따릅니다. 변경을 요청하면 Claude가 **컨텍스트를 수집하고**,
**행동을 취하고**, **결과를 검증하고**, 필요하면 다시 컨텍스트 수집 단계로 돌아갑니다.

검증은 에이전트가 응답하기 전에 자기 작업을 확인하는 방식입니다. Claude는 이미 코드베이스의 결정론적
신호 — 타입 체커, 린터, 테스트, 런타임 오류 — 를 관찰하며 일부를 스스로 수행합니다. Claude가 추론할 수
없는 나머지가 바로 *여러분이* 기능을 손으로 확인하는 단계가 됩니다.

그 수동 단계들을 검증 루프로 바꿀 수 있습니다. Claude Code에서 검증 루프란 Claude가 작업을 확인하고
고치려고 시도하는 반복 프로세스입니다. 즉 에이전트가 테스트·린터·커스텀 체크를 돌리고, 실패한 것을
고친 뒤에 다음으로 넘어가는 반복 사이클입니다. 스킬로 패키징하면 사람이 기억해내는 데 의존하지 않고
모든 세션이 자동으로 동일한 체크를 적용합니다.

## 내장 루프부터 시작하세요

- **`/verify`** — 애플리케이션을 빌드하고 실행하며 변경 사항을 관찰합니다.
- **툴체인** — Claude는 린터처럼 여러분이 제공한 도구의 오류 코드와 경고를 잡아 대응하려 합니다. 정확한
  빌드·테스트 명령어를 `CLAUDE.md`에 적어두면 Claude가 추론할 필요가 없습니다.
- **Code Review (리서치 프리뷰)** — 활성화한 리포지토리의 PR에 자동 리뷰 패스를 돌리는 매니지드 멀티
  에이전트 서비스입니다. 발견 사항을 직접 고쳐 푸시하거나, 해당 발견에 `@claude`로 코멘트해 루프를 닫을
  수 있습니다(GitHub Actions가 이미 설정돼 있어야 합니다).
- **GitHub Actions** — 검증 스킬로 Claude를 호출하는 잡을 정의하면, 로컬에서 돌리던 체크가 모든 푸시나
  PR에서 동일하게 실행됩니다.
- **스펙 검증** — 리포지토리의 마크다운 스펙에 대해 각 변경을 검증하고 위반을 고치려 시도하는 스킬입니다.
- **Claude Managed Agents의 루브릭(베타)** — 별도의 채점(grader) 에이전트로 결과를 루브릭에 비춰
  검증합니다. 실패하면 자동으로 재작업 루프로 돌아갑니다.

## 직접 작성하기

기존 프로젝트에서는 반복이 신호입니다. Claude가 기능을 구현할 때마다 매번 같은 작은 수정을 하고 있다면,
매번 하고 있는 일을 전부 적어두세요.

새 프로젝트라면 모범 사례 버전을 평범한 문장으로, **입사 첫날의 새 팀원에게 건네듯이** 쓰세요.

체크 자체를 말로 풀기 어렵다면 Claude에게 모범 사례를 먼저 물어보고 거기서 고쳐 나가세요. 여러분의
버전은 몇 가지 구체적인 지점에서 다를 텐데, 바로 그 차이가 담아내야 할 내용입니다.

> **팁.** 여기에 담을 체크가 정성적일 필요는 없습니다. "백필 단계 없이 컬럼을 삭제하는 마이그레이션은
> 거부한다"는 일반 린터는 잡지 못하지만 프로젝트 전용 규칙이라면 잡아내는 결정론적 규칙입니다. 손으로
> 계속 강제해야 하는 것은 무엇이든 루프로 담아낼 자격이 있습니다.

### 스킬로 만들기

가장 빠른 길은 `skill-creator` 플러그인을 설치하고 Claude가 인터뷰하게 하는 것입니다.

```
/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.
```

프로젝트 안 `.claude/skills/`에 마크다운 파일을 넣어 직접 작성할 수도 있습니다. 가장 단순한 검증 스킬은
몇 줄의 frontmatter와 본문이 전부입니다.

```markdown
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling
  or logging.
allowed-tools: [Read, Edit, Grep]
---
Read the error-handling paths in the current diff.

For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.

Report each violation with file:line, then fix it: add the request ID
where it's missing and strip the payload from the log call.
```

## 체크를 실행 위치에 맞추기

### 독립 실행(Standalone)

산출물이 생긴 뒤에 여러분이 의도적으로 호출합니다. 매번 적용되지는 않는 횡단 관심사 체크에 어울립니다.
커밋 전 보안 스캔, PR 전 접근성 감사, 리포지토리 전반의 라이선스 헤더 검증 같은 것들입니다. 여러 워크플로에서
쓰고 싶지만 모든 코드 변경마다 발동하길 원치는 않는 체크입니다.

대가는 호출할 때마다 여러분이 기억해서 한 턴을 써야 한다는 점입니다. 매 변경마다 돌리고 있다면 독립 실행
단계를 졸업한 신호이고, 그 절차는 영구적인 자리를 얻을 자격이 있습니다.

### 임베디드(Embedded)

산출 스킬의 일부로 자동 실행됩니다. 체크가 특정 워크플로 하나에 속하고, 이제 그 워크플로가 요청 없이도
체크를 돌립니다. 가장 단순한 형태는 산출 스킬 본문에 한 줄을 덧붙이는 것입니다.

```
After creating the component file, run eslint on it and
address any errors before reporting completion.
```

임베드가 동작하는지는 새 작업에서 그 스킬을 호출해 새 단계가 출력의 일부로 실행되는지 확인하면 됩니다.
실행되지 않는다면 스킬의 description이나 앞쪽 지시가 덧붙인 체크를 끌어오지 못하고 있는 것입니다.

임베디드는 편집할 수 있는 스킬에서만 동작합니다. 직접 쓴 스킬이거나, `SKILL.md` 파일이 여러분 통제 아래
있는 프로젝트 수준 설치 스킬이어야 합니다. 내장 스킬과 플러그인이 관리하는 스킬(업데이트 시 덮어써지는
종류)은 이 패턴의 대상이 아니니 체이닝을 쓰세요. 여러 워크플로에 걸치는 체크는 임베디드 대신 독립 실행이
맞습니다.

### 체이닝(Chained)

한 스킬이 끝날 때 다른 스킬을 호출해, 검증된 인계가 여러 번 이어지며 엔드투엔드로 돌아갑니다. Anthropic
Claude Code 팀 구성원들은 이 패턴을 매일 씁니다. `/code-review`가 버그를 찾고, `/simplify`가 diff를
정리하고, `/verify` 스킬이 엔드투엔드 동작을 확인하고, 변경이 UI를 건드렸다면 커스텀 `/design` 스킬이
`DESIGN.md`의 가이드라인에 비춰 확인합니다.

체이닝은 수정할 수 없는 스킬에 검증을 붙이는 방법이기도 합니다. 원본을 호출한 뒤 검증 스킬을 호출하는
커스텀 래퍼 스킬을 만드세요.

```markdown
# .claude/skills/safe-refactor/SKILL.md
Run /simplify on the current diff first.
When /simplify finishes, invoke /verify-no-public-api-changes.
```

습관("나는 늘 `/simplify` 뒤에 `/verify`를 돌린다")이었던 것이 계약("`/simplify`는 끝나면 항상
`/verify`를 돌린다")이 됩니다. 체인이 개발 사이클 전체를 스스로 돌리고, 여러분은 무언가가 다시
에스컬레이션될 때만 개입합니다.

단계들이 서로 독립적이어서 때때로 하나만 돌리고 싶다면 체이닝은 건너뛰세요. 체이닝은 유연성을 자동화와
맞바꿉니다. 체인 검증 루프는 토큰 소비를 늘릴 수 있으니 넓게 배포하기 전에 먼저 테스트하세요.

### 모든 PR에서

자기 변경에 대해 체인이 안정되면, 같은 절차를 모든 PR에서 돌릴 수 있습니다. 동료의 변경도 체인을 호출할
것을 기억했든 아니든 여러분의 변경과 같은 게이트를 통과합니다. 인프라는 이미 작성한 체인과 같은 종류가
한 걸음 더 나아간 것일 뿐입니다. 같은 스킬, 같은 루브릭, 같은 기준을 작성자의 성실함에 의존하지 않고
적용합니다.

여기서 검증은 개인 인프라를 넘어 팀 인프라가 됩니다. 다만 체인이 아직 유동적인 동안에는 PR 전역 게이트를
미루세요. 조정 하나하나가 팀 전체에 보이는 이벤트가 됩니다.

## 프로세스

1. 이번 주에 가장 자주 했던 수동 후속 작업을 고르세요.
2. 내장 `/verify` 스킬을 먼저 써보고 프로세스에 도움이 되는지 확인하세요.
3. 절차를 평범한 문장으로, 입사 첫날의 새 팀원에게 건네듯이 쓰세요.
4. `skill-creator`에 넘기거나, 마크다운 파일을 직접 `.claude/skills/`에 넣으세요.
5. 새 작업에서 호출해 체크가 출력의 일부로 실행되는지 확인하고, 필요하면 반복 개선하세요.
6. 스킬 체이닝으로 엔드투엔드 검증 흐름을 실험해 보세요.

Claude가 따를 수 있도록 더 많이 인코딩할수록, Claude의 응답은 더 자주 첫 시도부터 원하는 결과에 가까워집니다.
더 이상 손댈 필요가 없어진 수정들이, 어떤 스킬도 대신 적어줄 수 없는 일에 쓸 주의력을 되돌려 줍니다.

## 출처

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
— Delba de Oliveira, Claude Code 팀, 2026년 7월 22일.
