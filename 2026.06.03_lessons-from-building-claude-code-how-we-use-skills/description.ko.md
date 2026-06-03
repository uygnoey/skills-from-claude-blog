[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Lessons from building Claude Code: How we use skills

## 이 글이 뭔가요
이 글은 Anthropic이 Claude Code 스킬을 수백 개 규모로 만들고 운영하면서 얻은 교훈을 정리합니다. 스킬의 대표적인 유형(카테고리)과, 스킬을 작성·구조화·배포하는 실전 팁을 다룹니다.

## 언제 유용한가요
Claude Code용 스킬을 설계할 때, 무엇을 포함해야 하는지(가장 흔한 실패인 gotchas, 레퍼런스, 스크립트, 템플릿 등), 파일 구조를 어떻게 잡아 progressive disclosure를 구현할지, 리포지토리/플러그인 형태로 어떻게 배포할지에 대한 휴리스틱이 필요할 때 유용합니다.

## 핵심 포인트
- 스킬은 마크다운 파일 하나가 아니라, 스크립트·에셋·데이터·설정을 포함할 수 있는 **폴더 번들**입니다.
- Anthropic은 내부 스킬을 9개 카테고리로 분류했으며, 한 카테고리에 명확히 속하는 스킬이 대체로 더 잘 작동했습니다.
- 스킬에서 가장 신호가 큰 부분은 실제 실패를 바탕으로 쌓이는 “Gotchas” 섹션인 경우가 많습니다.
- 스킬은 `./.claude/skills`에 체크인하거나, 마켓플레이스에서 설치 가능한 플러그인 형태로 배포할 수 있습니다.
- Hook은 스킬이 호출될 때만(on-demand) 활성화할 수 있어, 상시 훅 대비 방해가 덜합니다.

## 번들 리소스
- 스킬 설계/구조화용 체크리스트 가이드.
- 스킬 카테고리와 예시 레퍼런스.

## 출처
- https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
