[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Preview, review, and merge with Claude Code

## 이 글이 뭔가요
이 글은 Claude Code 데스크톱에 새로 추가된 기능(실행 중인 앱 미리보기, 로컬 변경사항 사전 리뷰, GitHub PR 상태 모니터링 및 자동 수정/자동 머지 옵션)을 소개합니다.

## 언제 유용한가요
터미널·브라우저·PR UI를 오가며 컨텍스트 스위칭을 반복하지 않고, ‘코드 수정→검증→머지’까지의 시간을 줄이고 싶을 때 유용합니다.

## 핵심 포인트
- 미리보기: 데스크톱 앱 안에서 개발 서버를 띄우고 UI를 미리보며, Claude가 화면 상태와 콘솔 로그를 읽고 반복 개선합니다.
- 리뷰: ‘Review code’ 버튼으로 로컬 diff를 푸시 전에 검토받고, 인라인 코멘트를 바탕으로 수정할 수 있습니다.
- PR 모니터링: GitHub PR의 CI 상태를 앱에서 추적하며, 실패 감지 시 자동 수정(auto-fix)과 통과 시 자동 머지(auto-merge)를 옵션으로 켤 수 있습니다.
- 연속성: CLI 세션은 `/desktop`으로 데스크톱으로 가져오고, 데스크톱 세션은 웹/모바일로 이어갈 수 있습니다.

## 번들 리소스
- 스킬: `skills/code-pr-review-loop/` (workflow checklist and reusable command snippets).

## 출처
- https://claude.com/blog/preview-review-and-merge-with-claude-code
