[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
라우터·플래너·도메인 서브에이전트를 언제 하나의 메인 에이전트 루프로 접어 넣을지, 그리고 Claude
Platform 에서 어떻게 단계적으로 옮길지 다룬 모범 사례 글입니다(2026년 10월 22일, Diane Sarkis).
메인 루프는 스킬과 도구 검색을 점진적 공개(progressive disclosure) 방식으로 씁니다.

## 언제 유용한가요
- 에이전트 구조가 조직도를 그대로 닮아 버렸을 때(팀마다 서브에이전트 하나).
- 멀티 에이전트 구성이 느리거나, 말투가 들쭉날쭉하거나, 처음부터 끝까지 평가하기 어려울 때.
- 어떤 서브에이전트를 유지하고, 도구로 호출하고, 합치고, 스킬·도구로 접을지 계획할 때.

## 핵심 포인트
- 여러 엔터프라이즈 배포를 비교한 결과, 스킬을 갖춘 단일 에이전트가 단일 거대 프롬프트 방식과
  서브에이전트 방식보다 품질이 자주 더 좋았고, 비용과 지연도 자주 더 낮았습니다.
- 서브에이전트를 유지할 조건: 컨텍스트 비대화로 인한 측정 가능한 성능 저하, 버려도 되는 새
  컨텍스트로 병렬 처리할 작업, 도구 선택 실패나 상충하는 지시.
- 실패 양상: 컨텍스트 관리, 서브에이전트 난립, "프랑켄프롬프트", 국소화된 평가, 지연(한 고객은 단일
  루프에서 약 2배 빠른 실행 시간을 확인).
- 목표 설계: 모델 하나, 컨텍스트 윈도 하나, 병렬 도구 호출 묶음, 하네스의 예산·쓰기 게이트, 컨텍스트
  안에서 쓰고 고치는 계획. 절차는 스킬에, 강제 제한은 도구에.
- 작업 완료 평가(골든 예시 10개로 시작) 뒤에서 서브에이전트를 하나씩 옮기고, 결과가 뒤집힌 과제를
  확인하며, 각 과제를 두 번 이상 돌립니다.
- 팀은 스킬, MCP 도구(사용자 의도 단위로 묶음, 정의가 30~50개를 넘으면 선택 품질 저하), 지식 베이스를
  맡고, 작은 중앙 팀 하나가 시스템 프롬프트와 전체 품질을 맡습니다.
- 보조 도구: `/claude-api build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`, `/skill-creator`,
  `/skill-doctor`, 데모가 포함된 마이그레이션 키트.

## 번들 리소스
- 스킬: `fold-subagents-into-agent-loop` (`references/decision-criteria.md`,
  `references/single-loop-design.md`, `templates/migration-plan.md`, `templates/eval-plan.md`).
- 가이드: `guides/subagent-to-single-loop-migration.{en,ko,es,ja}.md`.

## 출처
- https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
