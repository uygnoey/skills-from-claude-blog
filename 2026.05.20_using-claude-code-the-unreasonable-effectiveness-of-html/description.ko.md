[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Using Claude Code: The unreasonable effectiveness of HTML

## 이 글이 뭔가요
이 글은 Claude Code 팀 구성원이 Claude Code를 사용할 때 Markdown 대신 **HTML 파일** 생성을 선호하는 이유를 설명하고, HTML을 더 풍부하고 읽기 쉽고 공유하기 쉬운 형태의 작업 산출물로 활용하는 실전 방법을 정리합니다.

## 언제 유용한가요
- Markdown보다 읽고 훑기 쉬운 산출물이 필요할 때
- 그리드/컬럼/콜아웃 같은 레이아웃, SVG 다이어그램, 간단한 상호작용이 필요할 때
- 기획 탐색, PR 리뷰 설명서, 인시던트 리포트처럼 공유하고 나중에 다시 보기 좋은 아티팩트가 필요할 때
- 구조화된 데이터를 편집하기 위해 목적에 맞는 “일회성(throwaway) 에디터”가 필요하고, 결과를 Claude Code로 다시 내보내야 할 때(예: JSON/프롬프트/diff로 복사)

## 핵심 포인트
- HTML은 Markdown보다 정보 밀도, 가독성, 공유성을 높여주는 “더 풍부한 캔버스”로 제시됩니다.
- 브레인스토밍 → 옵션 탐색 → 목업 → 구현 계획처럼 여러 HTML 아티팩트를 통해 반복한 뒤, 준비된 파일들을 컨텍스트로 새 세션을 열어 구현 단계로 들어가는 워크플로를 권장합니다.
- HTML 아티팩트는 코드 리뷰/이해(디프 렌더링, 주석, 심각도 색상 표시), 디자인 프로토타이핑, 리서치/리포팅에 특히 유용합니다.
- 커스텀 편집 UI를 만들 때는 “copy as JSON”, “copy as prompt”, “copy diff” 같은 내보내기 버튼으로 결과를 Claude Code나 파일로 되돌릴 수 있게 마무리하는 것이 중요합니다.

## 번들 리소스
- Skill: `skills/html-artifacts/SKILL.md`
- Guide: `guides/html-artifacts-workflows.*.md`

## 출처
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
