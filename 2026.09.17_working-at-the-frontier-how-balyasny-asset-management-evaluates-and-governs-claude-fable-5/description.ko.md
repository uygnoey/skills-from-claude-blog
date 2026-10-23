[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Balyasny Asset Management(BAM)의 최고 AI 책임자(CAIO) Charlie Flanagan 인터뷰입니다(2026년 9월 17일).
BAM이 Claude Fable 5를 켜기 전에 어떻게 평가했는지, 모델 바깥의 통제로 에이전트를 어떻게 관리하는지,
사내 에이전트 플랫폼 BAMAgent로 무엇이 가능해졌는지를 설명합니다.

## 언제 유용한가요
- 프로덕션 에이전트 업무를 새 프런티어 모델로 옮길지 결정할 때.
- 공개 벤치마크 대신 실제·검증 가능한 업무로 사내 평가 세트를 만들 때.
- 고위험 영역에서 에이전트 접근 범위를 넓히기 전에 권한·로깅·사람 검토를 정할 때.

## 핵심 포인트
- BAM에게 2026년은 "검색하는 AI"에서 "일을 끝내는 AI"로 넘어간 해이며, Claude Code 같은 에이전트
  하네스가 그 계기였습니다.
- 평가: 주식·매크로·원자재 영역의 검증 가능한 금융 과제 수천 개를, 모델 단독과 BAM 에이전트 하네스
  안에서 각각 돌립니다. 관련 부분집합에서 Fable은 89.4%, 기존 프로덕션 모델은 86.1%였고 계획·분석·
  에이전트 실행에서 개선 폭이 가장 컸습니다.
- 이전 어떤 모델도 못 푼 경제학 문제를 풀었다는 의외의 결과는 먼저 평가 결함 가능성으로 보고, 재실행·
  과제와 채점 로직 독립 점검·Anthropic과의 검토를 거쳐 받아들였습니다.
- 안전은 모델 바깥 통제로 지킵니다: 승인된 데이터 경계, 최소 권한, 도구 단위 권한, 로깅, 중요한
  산출물의 사람 검토, 에스컬레이션 경로. 더 유능한 모델이라고 권한이 늘지 않으며 투자 판단은 사람의 몫입니다.
- BAMAgent는 수천 개의 자율 에이전트를 운영합니다. 합병 차익거래 분석은 3~5일에서 하루 미만(에이전트
  실행 약 30분)으로, 중앙은행 분석은 약 2일에서 약 30분으로 줄었고 검토는 유지됩니다. 300개가 넘는
  에이전트를 돌리는 팀도 있습니다.

## 번들 리소스
- 스킬: `frontier-model-eval-governance` (`references/eval-dimensions.md`, `templates/controls-checklist.md`, `examples/workflows.md`).
- 가이드: `guides/agentic-model-evaluation-and-governance` (4개 언어).

## 출처
- https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
