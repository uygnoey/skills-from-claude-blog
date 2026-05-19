[English](./html-artifacts-workflows.en.md) · **한국어** · [Español](./html-artifacts-workflows.es.md) · [日本語](./html-artifacts-workflows.ja.md)

# Claude Code에서 HTML 아티팩트를 활용하는 워크플로

## 이 가이드가 뭔가요
Claude Code에서 Markdown 대신 HTML 파일을 작업 아티팩트로 활용해 기획, 코드 이해, 프로토타이핑, 리포팅을 더 읽기 쉽고 풍부하게 만드는 실전 가이드입니다.

## 언제 유용한가요
Markdown의 표현력이 부족하거나, 가독성/레이아웃/가벼운 상호작용이 필요한 경우에 유용합니다.

## 핵심 포인트
- 그리드/컬럼/콜아웃 등 더 풍부한 레이아웃과 높은 정보 밀도가 필요하면 HTML을 우선 고려합니다.
- 큰 작업은 옵션 탐색 → 목업 → 구현 계획처럼 여러 HTML 아티팩트로 반복한 뒤, 새 세션에서 구현을 진행하는 흐름이 효과적입니다.
- 리뷰/이해 작업은 디프 렌더링, 인라인 주석, 심각도 색상 표시를 요청하면 도움이 됩니다.
- “일회성(throwaway) 에디터”는 반드시 내보내기 버튼(copy as JSON/프롬프트/diff/Markdown)을 포함합니다.

## 추천 워크플로 패턴
1. **탐색 그리드**: 여러 대안을 한 화면에서 비교
2. **구현 계획**: 목업, 데이터 흐름, 핵심 스니펫을 한 페이지로 정리
3. **PR/시스템 설명**: 디프 렌더링 + 주석 + 주의점(gotchas)
4. **상호작용 프로토타입**: 슬라이더/노브로 파라미터 튜닝
5. **목적 특화 에디터**: 일회성 UI로 편집하고, 내보내기로 결과를 되돌림

## 번들 리소스
- 프롬프트 템플릿: `../skills/html-artifacts/templates/prompt-patterns.md`

## 출처
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
