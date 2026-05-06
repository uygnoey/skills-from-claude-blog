[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Managed Agents의 신규 기능인 dreaming(리서치 프리뷰), outcomes, 멀티 에이전트 오케스트레이션, 웹훅을 소개합니다.

## 언제 유용한가요
메모리와 dreaming으로 시간이 지날수록 개선되는 에이전트를 만들고, outcomes로 자동 채점(그레이딩) 기반의 품질 기준을 적용하며, 멀티 에이전트 오케스트레이션으로 병렬 전문 작업을 수행하고 싶을 때 유용합니다.

## 핵심 포인트
- Dreaming은 과거 세션과 메모리를 주기적으로 검토해 패턴을 추출하고, 에이전트가 기억해야 할 내용을 더 잘 정리하도록 돕는 과정입니다.
- Outcomes는 성공 기준(루브릭)을 정의하고, 별도의 그레이더가 결과를 평가한 뒤 에이전트가 기준을 충족하도록 반복 개선하게 합니다.
- 멀티 에이전트 오케스트레이션은 리드 에이전트가 작업을 쪼개 전문 에이전트(모델/프롬프트/툴이 각각 다름)에 병렬로 위임하고, 공유 파일시스템에서 협업하게 합니다.
- 웹훅으로 outcome 평가 완료 시점을 알릴 수 있습니다.

## 번들 리소스
- Skill: `managed-agent-orchestration` (outcomes 루브릭 템플릿, dreaming/메모리 점검 체크리스트, 역할 용어집)

## 출처
- https://claude.com/blog/new-in-claude-managed-agents
