[English](./agent-view-quickstart.en.md) · **한국어** · [Español](./agent-view-quickstart.es.md) · [日本語](./agent-view-quickstart.ja.md)

# Agent view 빠른 시작 (Claude Code)

## 개요
Agent view는 Claude Code의 여러 백그라운드 세션을 한 화면에서 실행·관리할 수 있게 해줍니다.

## 사전 조건
- Claude Code v2.1.139+
- 기능이 변경될 수 있음(research preview)

## 시작하기
1. `claude agents`를 실행합니다.
2. 프롬프트를 입력하고 `Enter`를 눌러 백그라운드 세션을 디스패치합니다.
3. 같은 방식으로 여러 세션을 병렬로 실행합니다.

## 실무 흐름
- working vs. blocked(입력 필요) 상태를 모니터링합니다.
- `Space`로 peek 패널을 열어 테이블을 떠나지 않고 답장합니다.
- 깊게 협업해야 할 때만 attach(`Enter`)합니다.
- 빈 프롬프트에서 `←`로 detach하여 테이블로 돌아옵니다.

## 파일 편집 병렬성(충돌 방지)
여러 세션이 파일을 편집할 수 있다면 worktree 격리가 사용될 수 있습니다. worktree는 `.claude/worktrees/` 아래에 생성되며, 세션을 삭제할 때 함께 정리됩니다.

## 출처
- https://code.claude.com/docs/en/agent-view
