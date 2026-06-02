[English](./dynamic-workflows.en.md) · **한국어** · [Español](./dynamic-workflows.es.md) · [日本語](./dynamic-workflows.ja.md)

# Claude Code의 다이내믹 워크플로 가이드

## 무엇인가요
다이내믹 워크플로는 Claude Code가 JavaScript 워크플로 파일을 실행하면서 서브에이전트를 생성·조율해, “그때그때” 커스텀 멀티 에이전트 하네스를 만들고 실행할 수 있게 해주는 기능입니다.

## 어떻게 동작하나요(개요)
- 워크플로는 서브에이전트 생성/조율을 돕는 특수 헬퍼 함수가 포함된 JavaScript 파일을 실행합니다.
- JSON/Math/Array 같은 표준 JavaScript 기능으로 데이터를 처리할 수 있습니다.
- 에이전트별 모델 선택, 서브에이전트의 worktree 분리 실행 여부를 결정할 수 있습니다.
- 중단되더라도 세션을 재개하면 계속 진행할 수 있습니다.

## 언제 쓰면 좋나요
격리된 컨텍스트, 전문화된 역할, 구조화된 합성/검증이 필요한 복잡하고 고가치 작업에 적합합니다.

## 대표 패턴
- classify-and-act
- fan-out-and-synthesize(배리어 + 병합)
- adversarial verification(루브릭 기반 리뷰)
- generate-and-filter(대량 생성 → 중복 제거 → 상위만)
- tournament(페어와이즈 심사로 우승자/top-k)
- loop until done(고정 횟수 대신 정지 조건)

## 활용 예
- 엔지니어링: failing test/module/callsite 단위로 분해 → 병렬 worktree 수정 → 적대적 리뷰/머지.
- 트리아주: 항목 분류, 기존 트래킹과 중복 제거, 불확실 항목 quarantine 후 조치.
- 경량 eval: 후보 해법을 worktree에서 실행해 비교/채점(루브릭 기반).
- 비기술 작업: 다각도 비평, 루브릭 기반 이력서 랭킹, 네이밍 토너먼트.

## 저장과 공유
- 워크플로 메뉴에서 `s`로 저장하고 `~/.claude/workflows` 아래에 둘 수 있습니다.
- Skill로 배포하려면 워크플로 JavaScript 파일을 skill 폴더에 두고 `SKILL.md`에서 참조합니다.
- 유연성을 위해 워크플로를 “그대로 실행해야 하는 스크립트”가 아니라 “템플릿”으로 다루는 접근이 유용할 수 있습니다.

## 출처
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
