[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Code의 “다이내믹 워크플로(dynamic workflows)”를 소개합니다. 다이내믹 워크플로는 Claude Code가 복잡한 작업을 더 자연스럽게 해결하도록, 그때그때 멀티 에이전트 하네스를 작성하고 오케스트레이션할 수 있게 해주는 기능입니다.

## 언제 유용한가요
다이내믹 워크플로는 트리아주, 검증, 여러 단계로 이루어진 엔지니어링 작업처럼 오케스트레이션의 이점이 큰 복잡하고 고가치 작업에 특히 유용하며, 작업을 여러 개의 집중된 서브에이전트로 분해해야 할 때 효과적입니다.

## 핵심 포인트
- 다이내믹 워크플로는 JavaScript 워크플로 파일을 실행하며, 서브에이전트를 생성하고 조율할 수 있습니다.
- 대표 패턴으로 classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop until done 등이 있습니다.
- 워크플로는 에이전트별 모델 선택과, 서브에이전트를 별도 worktree에서 실행할지 여부를 결정할 수 있습니다.
- 중단되더라도 세션을 재개하면 이어서 진행할 수 있습니다.
- 워크플로는 로컬(예: `~/.claude/workflows`)에 저장할 수 있고, Skill로 배포할 수도 있습니다.

## 번들 리소스
- Skill: `skills/dynamic-workflows-harness/` (패턴 라이브러리 + 재사용 프롬프트 템플릿)
- Guide: `guides/dynamic-workflows.ko.md` (장문 설명 + 활용 예)

## 출처
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
