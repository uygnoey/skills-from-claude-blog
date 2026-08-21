[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude 비용 가시성과 통제 가이드

## 이 글이 뭔가요

조직이 Claude에 쓰는 비용을 어떻게 들여다보고 통제할지 다룬, IT 관리자와 개발자를 위한 가이드. 핵심 주장은 토큰 소비량이 아니라 **성과당 비용(cost-per-outcome)**이 가치의 주된 지표여야 한다는 것, 그리고 대부분의 비용 문제는 사실 모델 매칭 문제라는 것이다.

가이드는 네 개의 면을 다룬다. 비용을 애초에 어떻게 생각할 것인가, Claude Enterprise에서 쓸 수 있는 관리자 통제(액세스 게이팅, 모델 통제, 하드 지출 상한), 사용량 관찰 도구(사용량 분석, Analytics API, Analytics Chat), 그리고 API 위에서 만드는 개발자가 쓸 수 있는 레버(프롬프트 캐싱, 배치 처리, effort 파라미터, 어드바이저 전략).

## 언제 유용한가요

- Claude Code나 Claude Cowork를 조직에 배포하면서 누구에게 먼저 열어 줄지 정할 때.
- 예산을 정했고, 지출이 실제로 그 선에서 멈추게 해야 할 때.
- Claude 지출을 인보이스와 대조하거나, 사용량 데이터를 BI·재무 시스템에 넣을 때.
- 어떤 워크로드를 어느 모델에 태울지, 그리고 더 싼 모델이 정말로 더 싼지 판단할 때.
- 중요한 지점의 품질을 포기하지 않으면서 프로덕션 API 워크로드 비용을 줄일 때.

## 핵심 포인트

- **토큰이 아니라 성과당 비용을 측정하라.** 어떤 프로젝트든 두 가지를 묻는다. AI 없이 이 일을 했다면 얼마나 들었을까(자원, 시간, 혹은 아예 시도조차 안 했을 일인지 포함)? 그리고 모델이 판단과 추론이 필요한 일을 하고 있나, 아니면 대량의 단순 작업을 처리하고 있나?
- **모델이 어긋나면 양방향으로 비용이 커진다.** 복잡한 추론에 덜 유능한 모델을 붙이면 재시도와 사람의 교정 때문에 최종 비용이 오히려 올라간다. 단순 문서 처리에 프런티어 모델을 붙이면 그 작업이 쓰지도 않는 능력에 돈을 낸다.
- **네 개 모델, 네 종류의 일.** 가장 어려운 문제엔 Fable, 장기 호흡 작업과 코딩엔 Opus, 일상 업무와 분석엔 Sonnet, 대량·정형 작업엔 Haiku.
- **엔터프라이즈 통제는 순서대로.** 먼저 *액세스 게이팅* — 어떤 그룹과 커스텀 역할이 어떤 제품(Claude Code, Claude Cowork 등)을 쓸 수 있는지 정해 전사 일괄이 아니라 부서 단위 단계적 롤아웃을 가능하게 한다. 다음 *모델 통제* — 팀이 접근할 수 있는 모델을 정하는 엔타이틀먼트와, 새 대화가 어떤 모델로 시작할지 정하는 기본값의 두 층위. 마지막 *하드 지출 상한* — 조직·개인·그룹 수준의 상한이며, 그룹에 걸면 구성원 각자가 그 한도를 받는다. 상한은 즉시 적용된다.
- **관찰 도구.** 사용량 분석은 사람별·팀별·모델별로 지출을 쪼개 보여 주고, 내보내기는 인보이스와 정렬된다. Analytics API는 같은 데이터를 기존 BI·재무·대시보드 시스템에 흘려 넣는다. Analytics Chat은 "이번 달 지출 상위자는 누구인가?", "이번 분기에 사용량이 가장 빠르게 증가한 팀은?" 같은 질문에 전체 리포트를 만들지 않고 자연어로 답한다.
- **API 쪽 레버.** 프롬프트 캐싱은 요청 간 재사용 가능한 내용을 저장해, 캐시 히트 시 일반 입력 단가의 약 10% 수준으로 낮춘다. 배치 처리는 급하지 않은 작업을 절반 가격으로 돌리며 캐싱과 중첩 적용된다. effort 파라미터는 호출 단위로 추론 강도를 조절한다. 어드바이저 전략은 대부분의 작업을 작은 모델로 처리하고, 결정적인 지점에서만 프런티어 모델에 자문한다.
- **관리자는 이 밖에도** 지출 한도 상향 요청을 자동화하고, 한도에 근접한 사용자를 찾아내고, 급변하는 사용 패턴을 추적할 수 있다.

## 번들 리소스

- `skills/cost-aware-model-selection/SKILL.md` — 판단 절차를 Agent Skill로 정리.
- `skills/cost-aware-model-selection/references/model-family.md` — 어떤 일에 어떤 모델인가.
- `skills/cost-aware-model-selection/references/enterprise-controls.md` — 세 가지 관리자 통제와 적용 순서.
- `skills/cost-aware-model-selection/references/api-cost-controls.md` — 캐싱, 배치, effort, 어드바이저 전략.
- `skills/cost-aware-model-selection/templates/cost-per-outcome-review.md` — 워크로드 평가 워크시트.
- `skills/cost-aware-model-selection/examples/usage-questions.md` — 분석 질문과 그 용도.
- `guides/cost-visibility-and-control.ko.md` — 4개 언어 전체 가이드.

## 출처

- [A Guide to Cost Visibility and Control in Claude](https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude) — 2026-08-04 게시
