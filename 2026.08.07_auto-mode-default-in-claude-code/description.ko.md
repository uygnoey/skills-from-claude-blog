[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
**Claude Code의 기본 권한 모드가 auto mode로 바뀐다**는 발표입니다. 2026년 8월 14일부터 Pro, Max, Team 플랜의 새 세션이 auto mode로 시작합니다. 매 도구 호출마다 사용자에게 승인을 요청하는 대신, auto mode는 모든 도구 호출을 분류기(classifier)에 통과시켜 되돌릴 수 없거나, 파괴적이거나, 사용자 환경 바깥을 향하는 동작을 차단합니다. 분류기가 무언가를 막으면 Claude는 대개 스스로 더 안전한 경로를 찾거나 사용자에게 직접 확인을 요청하며, 진행이 불가능하면(연속 3회 차단, 또는 한 세션에서 20회 차단) Claude Code가 수동 승인 방식으로 되돌아갑니다.

이 글은 변경의 근거가 된 안전성 데이터도 함께 공개합니다. 내부 레드티밍, Apollo Research와 진행한 외부 레드티밍, Trajectory Labs의 프롬프트 인젝션 평가, 유급 테스터 1,053명 대상 통제 실험, 그리고 안전 파이프라인이 플래그한 실제 프로덕션 세션 분석입니다. Pro, Max, Team 플랜에서는 분류기 오버헤드 토큰에 더 이상 과금하지 않습니다. Claude Enterprise, Claude API, AWS의 Claude Platform, Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry에서는 당분간 opt-in으로 남습니다.

## 언제 유용한가요
- auto mode를 기본값으로 둘지, 다른 기본값을 고정할지 판단해야 할 때.
- 관리자가 변경이 사용자에게 도달하기 전에 조직 차원의 롤아웃 또는 의도적인 opt-out을 계획해야 할 때.
- 사내에서 이 변경을 정당화하기 위해 수치·방법론·한계를 포함한 안전성 근거가 필요할 때.
- auto mode에서 어떤 권한 규칙이 계속 적용되고 어떤 규칙이 유보되는지 알아야 할 때.

## 핵심 포인트
- **수동 검토는 습관화된다.** 사용자는 권한 프롬프트의 97%를 승인하고 3%만 거부합니다. 반면 Claude가 계획을 제시하면 39%를 거부합니다. 2026년 6월 기준 활성 CLI 사용자의 49.5%가 Bash allow 규칙을 직접 작성했고, 62%가 `bypassPermissions` 또는 Bash의 "다시 묻지 않기"를 사용했으며, 인터랙티브 세션의 25%가 bypass permissions 모드로 시작합니다.
- **통제 실험.** 유급 테스터 1,053명 중 사람은 위험한 명령의 13.6%(1,053건 중 143건)만 잡아냈고, auto mode는 89%(1,053건 중 937건)를 차단했습니다. 정면 비교에서 auto mode는 사람이 승인한 명령 800건을 차단했고, 사람이 auto mode가 허용한 명령을 차단한 것은 6건뿐이었습니다. 세션이 길어질수록 사람의 차단율은 떨어졌지만(초반 약 17%, 프롬프트 50회 이후 약 5%) auto mode는 일정하게 유지됐습니다.
- **실제 세션.** 2026년 5~6월 안전 플래그가 붙은 세션 중, 사용자가 명시적으로 요청하지 않은 프로덕션 수준(심각도 7 이상) 유해 동작이 수동 승인 세션에서는 6.3%, auto mode 세션에서는 2.4% 발생했습니다.
- **Apollo Research 레드티밍**으로 분류기 미탐률이 12%에서 7%로 낮아졌고, 이 강화는 접근할 수 없었던 홀드아웃 공격 세트에도 일반화됐습니다.
- **프롬프트 인젝션.** Trajectory Labs 평가(시나리오 72개 × 10회)에서 auto mode로 실행된 Fable 5, Opus 5, Sonnet 5에 대한 720회 시도는 모두 실패했습니다. Codex Auto-review의 GPT-5.6 Sol은 5.83%, Full Access 모드에서는 19.03%가 성공했습니다.
- **권한 규칙은 여전히 분류기보다 먼저 적용됩니다.** 다만 임의 코드 실행을 허용할 만큼 광범위한 allow 규칙(예: `Bash(python:*)`)은 분류기를 건너뛰게 만들 수 있으므로 auto mode에서는 유보됩니다. 설정 파일 자체는 수정되지 않습니다.
- **최근 강화 사항**: 데이터 유출에 대한 hard deny(설정으로 규칙 추가 가능), 비밀정보·민감정보 구분 규칙과 git push/PR 대상이 public·private·trusted인지 확인, 파괴적 git 명령 전 git status 확인, 외부 콘텐츠에 대한 API 측 프롬프트 인젝션 스크리닝.
- **프로덕션 결과**: Teams·Enterprise 도입 조직에서 auto mode 사용자는 PR을 약 25% 더 많이 냅니다. Adobe, Nuro, Gusto, Garner Health가 프로덕션 기본값으로 사용 중입니다.
- **제어 수단**: CLI에서 `Shift+Tab`, 데스크톱 앱에서는 모드 드롭다운으로 전환. 관리형 설정의 `defaultMode`로 조직 기본값 고정, `disableAutoMode`로 완전 비활성화.
- **원문이 밝힌 한계**: auto mode는 분류 시스템에 의존하므로 위험을 없애지는 못합니다. 프로덕션 인프라에 대한 고위험 변경은 직접 검토하도록 권장합니다.

## 번들 리소스
- `skills/auto-mode-adoption/SKILL.md` — 기본 권한 모드를 결정·설정·롤아웃하는 절차.
- `skills/auto-mode-adoption/references/safety-evidence.md` — 공개된 모든 수치와 방법론, 그리고 명시된 한계.
- `skills/auto-mode-adoption/references/permission-model.md` — 분류기, 권한 규칙, 폴백, 강화 기능이 맞물리는 방식.
- `skills/auto-mode-adoption/templates/rollout-decision-record.md` — 기본 모드 결정을 기록하는 양식.
- `guides/auto-mode-safety-and-rollout.{en,ko,es,ja}.md` — 변경 내용과 근거를 담은 4개 언어 가이드.

## 출처
- https://claude.com/blog/auto-mode-default-in-claude-code
