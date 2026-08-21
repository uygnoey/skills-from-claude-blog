[English](./ai-native-sdlc-playbook.en.md) · **한국어** · [Español](./ai-native-sdlc-playbook.es.md) · [日本語](./ai-native-sdlc-playbook.ja.md)

# AI 네이티브 SDLC 플레이북

Anthropic의 Applied AI 팀이 사내에서, 그리고 고객사와 함께 실천해 온 방식을 바탕으로 소프트웨어 개발
수명주기(SDLC)를 단계별로 전환하는 가이드.

## 코드는 더 이상 병목이 아니다

조직들은 1년 전만 해도 상상하기 어려웠던 속도로 AI에게 코드를 쓰게 하기 시작했다. 그런데 코드를 둘러싼
프로세스는 같은 속도로 바뀌지 않았다. 승인 게이트, 리뷰, 핸드오프, 정책이 그대로 남아 에이전틱 코딩이
가져다줄 생산성 향상을 가로막는다.

전통적 SDLC(계획 → 설계 → 빌드 → 테스트 → 배포 → 유지보수)는 코드를 쓰고 구현하는 일이 가장 오래 걸리고
가장 비싼 단계였던 시대에 효율을 극대화하도록 설계됐다. PRD, 산정 의례, 제품 보안 리뷰는 몇 주에서 몇 분기에
이르는 개발 기간 동안 정렬을 강제하기 위해 존재했다. 게다가 전통적 SDLC의 통제 장치는 모든 단계를 사람이
수행한다고 전제한다.

빌드가 몇 시간으로 압축되면 세 가지가 참이 된다.

1. **병목이 빌드의 좌우 단계로 이동한다.** 계획, 리뷰·테스트, 배포는 여전히 사람의 속도로 돌아간다.
2. **통제가 현실과 어긋난다.** 사람이 한 줄씩 썼을 때는 한 줄씩 손으로 리뷰하는 것이 말이 됐지만, 에이전트가
   diff의 대부분을 쓰기 시작하면 따라갈 수 없다.
3. **거버넌스 비용이 올라간다.** 예외 처리는 여전히 주 단위·월 단위로 열리는 회의와 위원회를 거치기 때문이다.

보안이 가장 분명한 예다. 보안 팀은 사람의 산출량에 맞춰 인원이 잡혀 있으므로, 에이전트가 코드 산출량을
몇 배로 늘리면 리뷰 큐가 쌓이거나 충분히 리뷰되지 않은 코드가 배포된다. 규제 산업의 조직은 둘 다 받아들일 수
없으므로, 보안·정책 점검이 에이전트의 속도를 따라가야 한다.

## AI 네이티브 SDLC란

AI 네이티브 SDLC는 기존의 통제 목표는 유지하되 집행 방식을 바꾼다. 선형 흐름 대신 프로세스가 루프가 되고 각
지점에 AI가 내장되며, 단계 간 인계는 수작업이 아니라 자동으로 이뤄진다.

| 단계 | 전통적 SDLC | AI 네이티브 SDLC |
|---|---|---|
| 계획 | 위원회가 요구사항을 모으고 워크숍과 사인오프로 정제해 손으로 정리 | Claude가 소스에서 곧바로 문제점을 종합해 사람이 읽을 수 있고 기계가 실행할 수 있는 `intent.md`로 포착 |
| 설계 | 분석가가 스펙을 쓰고 디자이너가 그것을 다시 해석 | 요구사항과 설계를 에이전트와의 한 세션으로 압축. 스킬로 인코딩된 표준이 가이드하고 git으로 버전 관리 |
| 빌드 | 테스트와 코드는 손으로 쓰고, 문서는 개발이 끝난 뒤에 작성 | 테스트와 코드는 AI가 생성하고, 조직 지식은 버전 관리되는 기계 판독 가능한 `CLAUDE.md`와 스킬로 유지 |
| 테스트 | 단계 경계마다 QA 게이트 | 구현 과정에 짜여 들어간 지속적 eval |
| 배포 | 사람이 모든 줄을 리뷰하고 거버넌스는 리뷰 사이클에서, 종종 일관성 없이 이뤄짐 | 여러 겹의 에이전틱 리뷰. 사람의 리뷰는 규제·핵심 코드에 집중. 거버넌스는 AI가 행동하는 순간 집행되고 훅이 승인 게이트가 됨 |
| 유지보수 | 사람이 프로덕션의 버그를 감시 | 에이전트가 라이브 배포를 모니터링. 관리 밴드가 깨지면 진단해 새 `intent.md`로 루프에 되돌려 씀 |

대부분의 조직은 두 열 사이 어딘가에 있다.

### 커밋된 아티팩트가 실이다

각 단계는 아티팩트를 버전 관리에 쓰면서 끝나고, 다음 단계는 그것을 읽으며 시작한다. `intent.md`, `spec.md`,
`plan.md`, diff와 그 테스트, 리뷰 결과가 담긴 PR, 그리고 인시던트 기록이다. 초반 단계에서 마크다운이
아티팩트인 이유는 프로덕트 오너와 에이전트가 같은 파일을 함께 읽고 실행할 수 있기 때문이다. 빌드부터는
아티팩트가 코드와 그 기록이 된다.

커밋의 사슬은 곧 감사 추적이다. 누가 무엇을 요청했고, 에이전트가 무엇을 만들었고, 누가 승인했는가. 판단이
필요한 모든 결정에 대해서는 사람이 계속 책임을 진다. 바뀌는 것은 사람의 주의가 어떤 아티팩트에 놓이는가다.

승인된 `intent.md`가 요구사항·설계 패스를 촉발하고, 승인된 `spec.md`가 플랜 모드를 촉발하고, 머지된 PR이
파이프라인을 촉발하고, 프로덕션에서 깨진 관리 밴드가 다음 `intent.md`를 쓴다. 처음에는 각 단계를 손으로
프롬프트한다. 도달점은 승인된 아티팩트가 다음 게이트를 자동으로 여는 루프다.

## 1단계 — 계획: 의도를 포착한다

*아이디어가 누군가 정리해 주기를 기다리지 않게 된다.*

전통적으로 아이디어는 백로그 항목, 유저 스토리, 스토리 포인트, 리파인먼트 회의를 거쳐야 비로소 누군가 손을
댈 수 있다. 핸드오프마다 소유권이 옮겨 가므로, 엔지니어링에 도착하는 것은 최초 발의자의 의도에서 몇 단계
떨어져 있다.

대신 발의자가 Claude와 브레인스토밍하고 그 결과를 `intent.md`로 적는다. 자신의 언어로 쓴 프로토 스펙이며,
무엇을 원하는지, 왜, 어떤 제약 아래서인지를 담는다. 형식적인 문장은 필요 없다. Claude는 분석가가 물을 법한
질문을 한다. 범위, 사용자, 제약, 성공의 모습. 발의자가 Claude가 잘못 이해한 부분을 고친 뒤 파일을 커밋한다.

**시작하기.** 선행 조건 없음. 엔지니어가 아닌 사람들을 위한 Claude 접근 권한(claude.ai 또는 Cowork), 합의된
`intent.md` 템플릿, 프로덕트 오너가 지켜보는 공유 버전 관리 저장 위치가 필요하다. 단일 제품이라면 제품
리포지토리 안의 `intent/` 폴더가 가장 단순하며, 아티팩트 사슬이 그로부터 파생된 코드 옆에 놓인다는 장점이
있다. 전용 intent 리포지토리는 의도가 여러 리포지토리에 걸칠 때만 오버헤드를 감수할 가치가 있다.

이 준비는 플랫폼 팀의 일회성 작업이며, 누가 쓰기 권한을 가질지도 이때 정한다. 리포지토리가 생기고 나면 git
경험이 없는 기여자는 claude.ai나 Cowork에서 버전 관리 커넥터를 통해 커밋하면 된다.

**실제 `intent.md`:**

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.

## Problem
Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.

## Proposed outcome
Customers see claim status, next step and expected date in the portal.

## Affected users and systems
Claims handlers, portal team, claims-core API.

## Constraints
No new PII in the portal session. Existing authentication only.

## Open questions
Do third-party loss adjusters need access too?
```

**거버넌스.** 증거는 커밋된 파일 자체이며, 작성자·타임스탬프·전체 개정 이력이 git에 남는다. 프로덕트 오너가
승인하고, 수락/거절 결정은 머지 또는 리뷰 종료로 기록된다.

**측정.** 선행 지표: 첫 대화부터 `intent.md` 커밋까지의 시간. 몇 주짜리 요구사항 도출·정제 사이클에서 몇
시간으로 줄어드는 것이 기대치다. 후행 지표: 의도가 설계 단계로 살아남는 비율, 그리고 첫 `spec.md` 커밋 이후
`intent.md`에 가해진 변경 횟수.

## 2단계 — 설계: 요구사항과 설계가 하나로 합쳐진다

요구사항과 설계는 전통적으로 서로 다른 팀이 맡는 별개의 단계다. 책임 소재를 위해 분리했지만 느리고 손실이 크다.

이제 둘은 하나의 프롬프트된 세션에서 일어난다. Claude가 승인된 `intent.md`를 받아 요구사항·설계 스펙을
만들며, 브랜드·보안·컴플라이언스·UX 스킬이 제약으로 작용하고 우려 지점은 플래그로 표시된다. 프로덕트 오너는
스펙을 리뷰하되 직접 쓰지는 않는다.

출발점이 되는 프롬프트:

```text
Read the attached intent.md and produce a requirements and design spec for
integrating it into our existing codebase. Apply the skills available to you so
the plan conforms to our brand guidelines, security policies and UX standards.
Document the spec fully as spec.md, ready to hand to the engineering team.
Describe clearly any areas of concern, especially where you cannot satisfy
contradicting policies.
```

처음에는 손으로 실행하고, 다음에는 조직 수준의 슬래시 커맨드로 코드화하고, 그다음에는 의도 승인을 트리거로
삼아 비대화형 작업이 `spec.md`를 풀 리퀘스트로 커밋하게 한다. 그 시점부터 프로덕트 오너의 첫 관여는 리뷰다.

플래그된 우려부터 처리한다. 분석가라면 에스컬레이션했을 지점이기 때문이다. 각각을 해당 정책 오너와 함께
해소한 뒤 엔지니어링에 스펙을 넘긴다. `spec.md`는 `intent.md` 옆에 커밋한다. 이 한 쌍이 무엇을 요청했고 무엇을
결정했는지를 기록한다.

프런트엔드 작업이 이 압축을 가장 잘 보여 준다. 의도가 승인되면 프로덕트 오너가 `intent.md`로부터 Claude
Design(베타)에서 목업을 만들고, 목업을 다듬은 뒤 Claude Code로 내보내 빌드한다.

**거버넌스.** 살아 있는 정책이 몇 주 뒤 리뷰에서 발견되는 대신 스펙이 쓰이는 동안 읽히고 적용된다. 스펙,
그것을 만든 프롬프트, 그리고 적용된 스킬 버전이 모두 버전 관리에 기록된다.

**측정.** 선행 지표: 같은 변경에 대한 `intent.md` 커밋과 `spec.md` 커밋 사이의 경과 시간(두 개의 git
타임스탬프). 후행 지표: 빌드 시작 이후의 요구사항 재작업 — 같은 변경의 첫 `plan.md` 커밋보다 늦은 `spec.md`
커밋 수로 센다.

## 3단계 — 빌드: 승인된 플랜 없이는 아무것도 구현되지 않는다

### 기본 출발점은 플랜 모드

전통적으로는 변경을 어떻게 만들 것인지가 — 어떤 파일, 어떤 테스트 — 엔지니어의 머릿속이나 잘해야 티켓 코멘트에
남는다. 리뷰어가 처음 보는 것은 완성된 diff이고, 그때는 재작업이 느리다.

대신 일은 Claude가 플랜 모드에서 만든 문서화된 플랜으로 시작한다. 플랜 모드에서 Claude는 코드베이스를 읽되
바꾸지는 못한다. `intent.md`와 `spec.md`를 주고, 바뀌는 파일, 작업 순서, 그것을 증명할 테스트를 명시한 구현
플랜을 요구한다. 그리고 캐묻는다. 이 변경이 무엇을 깨뜨릴 수 있는가, 어떤 단계가 가장 위험한가, 무엇을 하지
않기로 했는가. 그 대화를 본 적 없는 엔지니어가 플랜만으로 구현할 수 있을 때까지 반복한 뒤 `plan.md`로
커밋한다.

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)
## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py
## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.
## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.
## Proof
test_status.py covers the four claim states; screenshot matches the
approved mock.
```

플랜이 탄탄하면 구현은 종종 한 번에 끝난다. 구현이 플랜에서 벗어나면 같은 커밋에서 `plan.md`를 갱신한다. 훅으로
둘의 동기화를 강제할 수도 있다.

플랜 모드는 설계 리뷰 자체를 강제한다. 엔지니어가 플랜을 수락하기 전에는 Claude가 파일을 편집할 수 없으므로,
방향을 바꾸는 일이 아직 문서를 고치는 수준에 머문다.

### 오토 모드

Claude Code는 오토 모드로도 돌 수 있다. 플랜이 승인되면 편집마다 확인을 받지 않고 변경을 적용한다. 이후
플레이들의 가드레일이 성숙할수록 — 잘 다듬어진 `CLAUDE.md`, 정책을 인코딩한 스킬, 위험한 행동을 막는 훅,
Claude가 돌릴 수 있는 테스트 스위트 — 오토 액셉트는 일상 작업의 기본값이 된다. 촘촘한 스펙, 좁은 폭발 반경,
이미 테스트가 덮고 있는 코드가 조건이다. 초점은 에이전트가 편집하는 것을 지켜보는 데서, 더 긴 자율 세션 이후
아티팩트를 리뷰하는 쪽으로 옮겨 간다.

### `CLAUDE.md`

`CLAUDE.md`는 새로 합류한 사람에게 필요한 맥락 — 컨벤션, 명령어, 아키텍처, 팀이 가장 자주 겪는 실수 — 을
Claude에게 준다. 사람들의 머릿속과 위키에 흩어져 있던 지식이 매 세션 시작마다 에이전트가 읽는 파일이 된다.

`/init`을 돌리고, 생성된 파일을 새 합류자가 첫날 필요로 할 만큼으로 줄이고, 리포지토리 루트에 체크인해 팀 전체가
한 버전을 공유하고 변경이 코드처럼 리뷰되게 한다. 실무 규칙: Claude가 같은 실수를 두 번 하면 그 교정이
`CLAUDE.md`로 들어간다. 한 페이지 이내로 유지한다. Claude는 세션 시작에 전체를 읽으므로, 낡은 내용은 아무
이득 없이 컨텍스트만 차지한다.

```markdown
# Payments service

## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)

## Conventions
- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
- Every endpoint needs an integration test in src/itest.

## Architecture
- api/ holds REST controllers, core/ holds domain logic,
  adapters/ talks to external systems.
- Kafka events are defined in schemas/; never edit generated classes.

## Things Claude gets wrong
- Do not bump dependency versions; the platform team owns them.
- The legacy v1/ package is frozen; changes go in v2/.
```

### 조직 지식으로서의 스킬

스킬은 조직 지식을 실행 가능하게 만드는 방법이다. 명시적이고, 버전 관리되고, 넓게 적용되며, 정책이 바뀌면
중앙에서 갱신된다. 원칙: **일관되게 적용되어야 하는 조직 지식은 스킬로 쓰고, `CLAUDE.md`나 프롬프트에 속하는
것은 스킬로 쓰지 않는다.**

오늘 일관성 없이 지켜지는 지식 하나를 고르고, 언제 발동하는지를 프런트매터에 쓰고 무엇을 할지를 본문에 쓴
`SKILL.md`를 담은 폴더로 만든다. 코드와 함께 배포되도록 `.claude/skills/<name>/`에 두거나, 플러그인으로 조직
전체에 배포한다. 실제로 발동하는지 테스트한다 — 같은 작업을 여러 방식으로 요청해 매번 로드되는지 확인한다.
정책이 바뀌면 스킬을 바꾸고 정책 오너가 사인오프한다. 엔지니어는 다음 세션에서 새 버전을 자동으로 집는다.

```markdown
---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
  modifying an external-facing endpoint, reviewing API code, or
  generating an OpenAPI spec.
---

# Secure API review

When you create or change an API endpoint:

1. Authentication: every endpoint requires the gateway JWT;
   no anonymous routes outside /health.
2. Input validation: validate request bodies against the OpenAPI
   schema and reject unknown fields.
3. Audit: every state-changing endpoint emits an audit event with
   actor, action, entity and timestamp.
4. Data classification: fields tagged pii in the schema must never
   appear in logs or error messages.

Run the endpoint check script and include its output in your summary.
```

**스킬은 통제이지만 권고적 통제다.** 코드가 쓰이는 동안 Claude가 정책을 적용할 가능성을 높일 뿐, 세션이 반드시
따르도록 강제하지는 않는다. 언제나 지켜져야 하는 정책에는 그 뒤에 결정론적인 무언가가 필요하다. 행동을 막는
훅이거나, PR에서 정책을 다시 확인하는 리뷰 패스다. 스킬은 위반을 드물게 만들고, 훅은 거의 불가능하게 만든다.

### 빌드타임 가드레일로서의 훅

구현 중 Claude의 행동은 대부분 파일 편집과 셸 명령이므로, 훅이 가장 자주 발동하는 곳이 빌드 단계다. 빌드 단계의
훅은 생성된 클래스나 동결된 패키지 같은 보호 경로의 편집을 막고, 파일 편집 후 포매터와 린터를 돌려 드리프트가
쌓이지 않게 하고, 자격 증명이 diff에 들어가지 않게 한다.

예외 없이 지켜져야 하는 정책의 스킬은 훅으로 뒷받침한다. 훅은 매칭되는 행동마다 실행되므로 빌드 단계의 훅은
빠르고 변경된 파일에 한정돼야 한다. 전체 테스트 스위트 같은 무거운 점검은 커밋이나 PR에 속한다. 사람에게 승인을
묻는 훅은 배포 게이트에 속한다 — 빌드 도중의 승인 프롬프트는 병렬로 도는 모든 세션의 임계 경로에 사람을 다시
올려놓기 때문이다.

### 병렬 세션과 서브에이전트

병렬 세션은 자체 git worktree에서 별도 작업을 수행하는 또 하나의 완전한 Claude Code 인스턴스다. 세션들이
공유하는 것은 그것들을 몰고 가는 엔지니어뿐이다. 서브에이전트는 하나의 세션 안에서 자체 컨텍스트 윈도와 도구
제한을 가진 범위 한정 조력자로 돌며, 여러 작업에 걸쳐 반복되는 일에 어울린다.

서로 다른 파일을 건드리는 작업으로 일을 쪼갠다. 어디가 독립적인지는 플랜을 보면 알 수 있다. 파일을 공유하는
작업은 한 세션에서 차례로 돌린다. 병렬 작업마다 자체 worktree를 준다(한 터미널에서
`claude --worktree feature-auth`, 다른 터미널에서 `claude --worktree fix-rate-limit`). 두세 개 세션이 합리적인
출발점이며, 현실적 상한은 한 사람이 제대로 리뷰할 수 있는 스트림 수다.

반복되는 일은 `.claude/agents/`에 정의한 서브에이전트로 만든다. 메인 에이전트가 끝난 뒤 불필요한 복잡성을
걷어내는 코드 심플리파이어, 앱을 돌려 동작을 확인하는 베리파이어, 코드베이스를 탐색해 메인 컨텍스트를 채우지
않고 보고하는 리서처 같은 것들이다. 정의는 git에 체크인한다.

```markdown
---
name: verifier
description: Runs the app and checks the change works before the session
  reports done
tools: Bash, Read
---
Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

### 레거시 시스템과 단일 진실 공급원

기존 프로세스도 이미 이 아티팩트들을 추적한다. 다만 마크다운이 아닐 뿐이다. 작업 항목은 Jira에, 요구사항은
규제 추적성이 내장된 도구에, 디자인은 Figma에, 변경 승인은 변경 심의 위원회에 있을 수 있다. 감사인과 규제
기관이 이미 인정하는 시스템이라 밀어내기 어렵다.

프로세스가 만들어 내는 아티팩트마다 **하나의** 시스템을 진실 공급원으로 지정하고 나머지는 사본이나 링크만
갖게 한다. 세 가지 구성이 가능하다. 리포지토리를 진실 공급원으로 삼고 레거시 시스템이 커밋 안의 파일을
참조하게 하거나, 레거시 시스템을 진실 공급원으로 삼고 Claude가 세션 시작에 기록을 읽어 같은 세션에서 MCP
커넥터를 통해 결과를 되써 넣게 하거나, 최소선으로 연결만 유지해 아티팩트에는 레코드 ID를, 레코드에는 마크다운
파일의 커밋 SHA를 적어 두는 방식이다. 진실 공급원이 둘이라는 점을 감수한다면 연결만 유지하는 방식이 전환의
출발점으로 좋다.

## 4단계 — 테스트: 검증이 세션 안으로 들어온다

### Claude에게 피드백 루프를 준다

코드가 동작한다는 신호는 전통적으로 늦게 온다. CI는 몇 분 뒤, 테스터는 며칠 뒤, 프로덕션은 몇 주 뒤다.
에이전트가 코드를 만들어 내는 상황에서 늦은 신호는 사람이 그 산출물 전부를 확인해야 한다는 뜻이고, 그 사람이
병목이 된다.

Claude에게 언제나 자기 작업을 검증할 방법을 준다. 테스트, 빌드, 또는 스크린샷 비교다.

1. 오늘 작업 확인에 여러 명령과 환경 지식이 필요하다면, 실패 시 0이 아닌 값으로 종료하는 단일 타깃으로 감싼다.
2. `CLAUDE.md`의 Commands 섹션에 각 명령을 정상 출력 예시와 함께 적는다.
3. Claude가 물어보지 않고 스스로 확인할 수 있도록 정량화된 목표를 제시한다. "test_status.py의 모든 테스트 통과",
   "스크린샷이 첨부된 목업과 일치", "엔드포인트가 새 필드와 함께 200 반환" 같은 식이다.
4. 버그 수정은 실패하는 테스트를 먼저 쓴다. Claude에게 버그를 테스트로 재현하게 하고, 돌려서, 기대한 이유로
   실패하는지 확인한다. 그 테스트를 커밋한다. 그런 다음에야 테스트를 건드리지 않고 통과시키라고 요청한다. 수정
   이전부터 존재했고 에이전트가 다시 쓸 수 없었던 테스트가 버그가 사라졌다는 증거다.
5. UI 작업은 시각적 확인으로 루프를 닫는다. 브라우저나 스크린샷 도구와 목업을 주고 구현 → 스크린샷 → 비교 →
   조정을 반복하게 한다. 두세 번이 보통이다.
6. 검증을 "완료"의 일부로 만든다. 지침은 `CLAUDE.md`에 둔다.

```markdown
## Verifying your work
- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)

Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

루프 자체도 보호해야 한다. 코드를 고치는 에이전트가 그 코드에 대한 검사를 약화시킬 수 있어서는 안 된다. 수정
작업 중 테스트 파일 편집을 막는 훅이 이 역할을 한다. 대안은 리뷰에서 diff를 확인해 테스트를 건드린 변경을
거부하는 것이다.

피드백 루프와 베리파이어 서브에이전트를 혼동하지 말 것. 루프는 작업 내내 필요한 만큼 반복해서 돈다. 베리파이어는
세션이 작업이 끝났다고 판단한 뒤 새 컨텍스트 윈도에서 한 번 도는 최종 확인이라, 그 판정이 코드를 만들어 낸
가정에 물들지 않는다.

### CI에서의 지속적 eval

Eval은 단계 게이트 QA의 AI 네이티브 등가물이다. 에이전트의 구성이 바뀔 때마다 도는 스위트다. 새 모델로 교체되거나
프롬프트가 다시 쓰이면, 스위트가 에이전트가 여전히 같은 수준으로 일하는지 말해 준다. 살아 있는 스위트로 다뤄야
한다. 모델이 좋아지면서 한때 변별력이 있던 케이스가 그렇지 않게 되므로, 지속적 모니터링에서 나온 새 케이스를
계속 넣어야 한다.

최근 작업에서 실제 태스크 20~50개를 기대/수용 결과와 함께 모으고, 각각을 프롬프트와 수용 기준(테스트 통과, 린트
클린, 동작 불변, 정책 준수)으로 쓴다. 스위트는 CI에서 비대화형으로, 일정에 따라 그리고 `CLAUDE.md`·스킬·훅의
모든 변경에 대해 돈다. 그 구성이 에이전트를 조종하므로 코드가 받는 회귀 테스트를 똑같이 받아야 한다. 구성 변경은
결과로 게이트한다. 통과율을 떨어뜨리는 스킬 변경은 머지 전에 리뷰된다. 모든 프로덕션 인시던트는 그 인시던트를
소유한 팀이 쓴 eval이 되어 회귀 테스트로 스위트에 남는다.

```yaml
name: Agent evals
on:
  pull_request:
    paths: ['CLAUDE.md', '.claude/**']
  schedule:
    - cron: '0 2 * * *'
jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - name: Run eval suite
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for eval in evals/*.json; do
            claude -p "$(jq -r '.prompt' $eval)" \
              --allowedTools "Read,Edit,Bash(make test)" \
              --output-format json > result.json
            ./evals/check.sh "$eval" result.json
          done
```

## 5단계 — 배포: 리뷰는 양방향으로, 릴리스는 게이트로

### PR 리뷰 루프 속의 AI

리뷰 용량은 사람의 산출량에 맞춰 계획됐다. PR은 리뷰어가 전부 읽을 때까지 기다리고, 품질은 리뷰어의 부하에 따라
달라지며, 작성자가 재촉하는 동안 백로그가 쌓인다.

Claude는 리뷰를 하기도 하고 받기도 한다. 모든 PR이 동일한 리뷰 패스 세트를 거치고 결과는 심각도로 정렬된다.
사람의 주의는 한 단계 위로 올라간다. 이 변경이 플랜이 의도한 일을 하는가, 그리고 그 위험이 수용 가능한가.

가장 빠른 출발은 관리형 Code Review 서비스(리서치 프리뷰)다. 관리자가 활성화하고 리포지토리를 선택한다.
파이프라인을 직접 통제하고 싶거나 API 호출을 자체 클라우드 계약(Bedrock, Vertex, Foundry)으로 라우팅해야 하면
`claude-code-action`으로 자체 CI에서 리뷰를 돌린다.

테크 리드가 리뷰 정책을 리포지토리 루트의 `REVIEW.md`로 쓴다.

```markdown
# Review instructions

## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles

## What Important means here
Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.

## Cap the nits
Report at most five nits per review; summarize the rest as a count.

## Do not report
Generated files under src/gen/ and anything CI already enforces.
```

발견 사항 자체가 PR을 승인하거나 막지는 않는다. 브랜치 보호는 여전히 코드 오너의 승인을 요구한다. 발견 사항으로
머지를 게이트하고 싶은 플랫폼 엔지니어는 체크 런이 게시하는 기계 판독 가능한 심각도 집계를 읽으면 된다.

리뷰어나 작성자가 리뷰 코멘트에 `@claude`를 태그하면 Claude가 그 코멘트를 처리하고 수정을 푸시하며, 스레드에
요청과 변경이 함께 기록된다. Claude가 연 PR이라면 팀은 미해결 코멘트와 실패한 체크를 훑어 처리하고 푸시하는
루프를 커스텀 커맨드로 감싸, PR이 그린이 되고 코드 오너 승인만 남을 때까지 돌리기도 한다.

리뷰 발견 사항은 `CLAUDE.md`로 되먹임된다. 같은 실수가 두 번째로 지적되면 그 교정이 해당 리뷰의 일부로 파일에
들어가고, 리뷰가 `CLAUDE.md`를 읽으므로 다음 PR부터는 그 실수가 잡힌다. 한 달에 한 번 테크 리드가 발견 사항에
평점을 매기고 nit 분량에 상한을 두어 설정을 튜닝한다.

**직무 분리는 유지된다.** 코드를 쓴 에이전트에게는 그것을 승인할 방법이 없다.

### 승인 게이트로서의 훅

훅은 **묻기**도 할 수 있다. 특정 인물이 승인할 때까지 행동을 멈춘다. 릴리스 게이트에 필요한 것이 바로 이것이다.
엔지니어링 리더십이 변경 관리·컴플라이언스와 함께 반드시 남아야 할 사람의 승인 게이트를 나열한다. 변경 관리
사인오프, 릴리스 승인, 보호 경로 편집 같은 것들이다. 플랫폼 엔지니어가 각각을 허용·질문·차단할 수 있는 훅으로
표현한다.

팀 훅은 git의 `.claude/settings.json`에, 타협 불가한 훅은 플랫폼·IT 관리자가 소유하는 managed settings에 둔다.
후자는 개별 엔지니어가 끌 수 없다. 차단은 스스로를 설명해야 한다. 훅이 행동을 막으면 그 이유와 승인 경로가
Claude의 출력에 나타나야 한다.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# Production deploys require a named release authorization
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
  if [ -z "$RELEASE_APPROVAL" ]; then
    echo "Production deploys need a release authorization." >&2
    exit 2   # exit 2 blocks the action; the message goes to Claude
  fi
fi
exit 0
```

훅은 배포 전용이 아니다. Claude가 행동하는 어디서든 돈다. 빌드 단계에서 변경 티켓 없이 마이그레이션과 인프라를
편집하는 것을 막을 수도 있고, 수정 작업 중 에이전트가 테스트 파일을 편집하는 것을 막을 수도 있다.

### 규제 기업을 위한 managed settings

플랫폼 팀이 MDM이나 관리 콘솔로 배포하며 엔지니어는 편집할 수 없다. deny 규칙은 비밀 정보를 에이전트의 컨텍스트
밖에 두고 도구를 통한 네트워크 유출을 막으며, allow 목록은 안전한 이너 루프를 사전 승인해 deny 목록이 프롬프트
피로로 이어지지 않게 한다. `disableBypassPermissionsMode`와 `allowManagedPermissionRulesOnly`는 어떤 엔지니어도,
프로젝트 파일도, 커맨드라인 플래그도 규칙을 넓히지 못하게 한다. 샌드박스는 권한이 메우지 못하는 틈을 막는다.
도구 수준의 deny는 셸 명령이 네트워크에 닿는 것을 막지 못하지만 OS 수준 도메인 허용 목록은 유출 자체를 차단하고,
`failIfUnavailable`은 샌드박스를 선호가 아닌 게이트로 만든다. credentials 블록은 샌드박스된 셸이 `~/.ssh`나
클라우드 자격 증명을 읽는 것을 막고 지정된 비밀을 모든 샌드박스 명령의 환경에서 제거한다. `allowManagedHooksOnly`,
`disableSideloadFlags`, `strictKnownMarketplaces`, `allowManagedMcpServersOnly`는 엔지니어 머신의 모든 스킬,
에이전트, 훅, MCP 서버가 승인된 마켓플레이스를 거쳐 왔음을 보장하고, `requiredMinimumVersion`은 조직이 평가하지
않은 빌드에서는 시작을 거부한다.

이런 구성은 그대로 복사할 권고가 아니라 다듬어 쓸 출발점으로 다뤄야 한다. 모든 deny는 역량과의 맞교환이고,
적절한 균형은 리포지토리의 데이터 분류에 달려 있다.

### CI/CD 통합과 배포

파이프라인은 전통적으로 결정론적 스크립트를 돌리고, 판단이 필요한 것은 사람을 기다린다. 대신 판단이 필요한
단계에 대해 스코프된 자격 증명을 가진 샌드박스 안에서 Claude를 비대화형으로 파이프라인 안에서 돌린다.

읽기 전용 판단 단계부터 시작한다. 실패한 빌드 트리아지, 플레이키 테스트 요약, 체인지로그 초안 같은 것들이다.

```yaml
- name: Triage failed build
  if: failure()
  run: >
    claude -p "Read the build log at out/build.log. Identify the most
    likely cause, say whether the failure looks flaky or real, and write a
    three-line summary for the PR thread." >> triage.md
```

그다음 기존 게이트 뒤에 쓰기 단계를 더한다. 린트 수정, 생성 문서 갱신, `@claude` 멘션을 통한 리뷰 코멘트 처리
같은 것들이다. 에이전트가 쓰는 모든 것은 브랜치 보호를 거쳐 PR로 도착하며, 에이전트에게 main으로 직접 푸시할
경로는 없다. 에이전트 작업은 네트워크 정책 아래 컨테이너에서 단기 스코프 토큰으로 돌고, 기본적으로 프로덕션
자격 증명을 갖지 않는다.

배포는 MCP로 노출해 deploy, status, rollback을 환경별로 스코프된 도구로 만든다. 자격 증명을 품은 셸 스크립트가
아니라 허용 목록이 된다. 자율성은 환경별로 등급을 매긴다. 개발에서는 에이전트가 자유롭게 배포하고, 프로덕션에서는
에이전트가 릴리스를 준비하고 릴리스 매니저가 승인하며 훅이 게이트를 집행한다. 롤백은 파이프라인에서 가장 자주
리허설되는 경로여야 한다. 스테이징에서 정기적으로 돌려 봐야 하는데, 유지보수 루프가 이것을 호출하기 때문이다.

**지배 원칙: 에이전트는 프로덕션 게이트까지 행동할 수 있고, 그 너머로는 갈 수 없다.**

## 6단계 — 유지보수: 루프를 닫는다

유지보수는 전통적으로 반응적이다. 새벽 3시에 알럿이 울리고 놓칠 수 있고, 티켓은 누군가 집을 때까지 백로그에
앉아 있으며, 다른 불이 나면 포스트모템 액션이 코드베이스에 끝내 닿지 못하기도 한다.

대신 트리거 — 관리 밴드 이탈, 티켓, 채널 메시지, 스케줄 — 가 사람을 거치지 않고 Claude를 호출한다. Claude는
진단하고, 게이트된 경로로만 행동하며, 찾아낸 것을 `intent.md`로 써서 위의 단계들을 다시 태운다. 이 단계는
헤드리스로 돌고, 단계 사이의 독립적 신뢰도 게이트 — 결정론적 검사이거나 적대적 리뷰 에이전트 — 가 앞 단계의
출력을 계속 진행시킬지 사람에게 에스컬레이션할지 결정한다.

**루프를 닫는 단계:**

1. 안정적인 롤링 베이스라인을 가진 지표 하나를 고른다. CI 테스트 실패율, 배포 후 5xx 비율, PR 사이클 타임 등.
2. 탐지 스크립트를 쓴다. 보통은 롤링 윈도의 평균과 표준편차에 Western Electric 같은 규칙을 얹어, 스파이크뿐
   아니라 느린 드리프트도 잡히게 한다. 버전 관리하고 유닛 테스트한다. **탐지는 전적으로 결정론적이며 모델이
   개입하지 않는다.**
3. 대응 등급을 버전 관리되는 설정에 정의한다. 1σ에서는 로그만 남기고, 2σ에서는 Claude를 읽기 전용으로 호출해
   진단하게 하며, 3σ에서는 Claude가 행동할 수 있되 리뷰 게이트로 들어가는 PR을 열거나 사전 승인된 런북을
   트리거하는 방식으로만 가능하다.
4. 트리거는 GitHub/GitLab의 스케줄 워크플로, 기존 모니터링 스택의 웹훅, 또는 네트워크 내부의 크론 잡이 될 수
   있다. Claude는 상태를 갖지 않고 돈다. CI 러너의 비대화형 스텝이거나 샌드박스 컨테이너 안의 Agent SDK
   서비스다. 상태가 없고 비대화형이므로 아무도 시작하지 않아도 루프가 시작되고 끝날 수 있다.
5. 에이전트는 진단을 1단계 형식의 `intent.md`로 쓴다. 이상 징후와 그 증거, 제안 결과, 영향받는 시스템, 남은
   질문을 담는다.
6. 서비스 오너나 온콜 엔지니어가 큐를 트리아지한다. 지금 고칠지, 일정에 넣을지, 기각할지. 기각은 밴드를
   조정하고 노이즈를 줄이는 데 쓰인다.
7. 수정이 배포되면 그 인시던트에 대한 eval을 추가해 같은 종류의 문제가 앞으로 방지되게 한다.

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose, tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose, routes: [pull_request, runbook:rollback-deploy] }
```

실제로 어떤 모습인가. CI 테스트 실패율이 3σ를 넘으면 에이전트가 플레이키 테스트를 격리하거나 리버트 PR을 열고
리뷰 게이트가 판단한다. 배포 후 5xx 비율이 그 창 안의 배포와 함께 3σ를 넘으면 에이전트가 기존 롤백 파이프라인을
트리거한다. PR 사이클 타임이 드리프트 규칙을 건드리면 에이전트가 엔지니어링 리더십을 위한 리포트를 쓴다. 이
하네스가 프로덕션 지표뿐 아니라 프로세스 지표에도 작동한다는 것을 보여 주는 예다.

### Claude Tag로 온콜에 서는 Claude

인시던트는 업무용 커뮤니케이션 앱으로도 들어온다. 인시던트 채널의 밤 10시 슬랙 메시지도 이제 즉시 처리될 수
있다. Claude Tag(퍼블릭 베타, 현재 Slack)는 Claude를 자체 아이덴티티로 채널의 구성원으로 만든다. 그래서 모든 새
인시던트에 최초 대응자가 생기고, 그 대응 자체가 루프의 일부이자 이후 인시던트를 위한 기억이 된다.

대화와 조직 지식은 채널에 남는다. 채널의 누구든 대응을 이끌고, 가설을 시험하고, 실시간으로 조사할 수 있으며,
채널 히스토리가 감사 가능성을 더한다. MCP 접근을 통해 Claude는 지표가 베이스라인으로 돌아왔는지 확인해 스레드에
알리고, 포스트모템을 이후 조사가 읽을 수 있는 버전 관리된 lessons 파일에 쓴다.

Claude Tag가 집는 일이 인시던트만은 아니다. MCP로 티켓에 태그되거나 채널에서 요청받으면 Claude는 같은 방식으로
트리아지한다. 작고 경계가 분명한 수정은 리뷰 게이트를 거쳐 PR로 도착하고, 그보다 큰 것은 1단계를 위한
`intent.md`로 정리된다. 이 지점에서 루프는 스스로를 먹이기 시작한다.

## 맺음말

모델과 하네스가 충분히 발전해, 조직은 코드를 생산하는 방식뿐 아니라 소프트웨어 개발 수명주기 전체를 전환할 수
있게 됐다. 사람의 판단을 중심에 두고, 대기업의 거버넌스·규제 요구를 충족하면서 말이다.

루프는 계속 돈다. 사람의 판단은 그 위에 남는다.

## 출처

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) — 저자 Louis Claxton,
기여 Jim Blackhurst, Will Steuk, Jamal Arif. 2026-08-21 게시.
