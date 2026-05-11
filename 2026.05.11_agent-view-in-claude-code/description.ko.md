[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Code의 Agent view

## 이 글이 뭔가요
Agent view는 Claude Code의 여러 백그라운드 세션을 한 화면에서 관리하는 풀스크린 터미널 UI입니다.

## 언제 유용한가요
버그 수정, PR 리뷰, 로그 조사처럼 서로 독립적인 작업을 병렬로 돌리고, 세션이 입력을 요구할 때만 개입하고 싶을 때 유용합니다.

## 핵심 포인트
- `claude agents`로 agent view를 엽니다.
- 새 백그라운드 세션을 디스패치하고, 상태를 모니터링하며, peek로 답장하거나 attach/detach 할 수 있습니다.
- agent view는 research preview이며 Claude Code v2.1.139 이상이 필요합니다.
- 세션은 supervisor 프로세스 아래에서 실행되며, 터미널을 닫아도 디스크에 상태가 남습니다.

## 번들 리소스
- Skill: `manage-agent-view-sessions` (명령어, 필터 문법, 반복 가능한 세션 관리 체크리스트)
- Guide: `agent-view-quickstart` (실무에서 agent view를 도입하는 방법)

## 출처
- https://claude.com/blog/agent-view-in-claude-code
- https://code.claude.com/docs/en/agent-view
