[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# 개발자 Console에서 더 나은 프롬프트 생성하기

## 이 글이 뭔가요

Anthropic이 2024년 5월 20일에 공개한 발표로, Anthropic Console 안에 짧은 태스크 설명을 입력하면 프로덕션에서 바로 쓸 수 있는 프롬프트 템플릿으로 만들어 주는 prompt generator를 소개합니다. 이 생성기는 명확한 역할 설정, chain-of-thought 스크래치패드, 모호한 변수 주위의 XML 태그, 간단한 변수의 인라인 사용 같은 프롬프트 엔지니어링 기법을 기본으로 포함하고 있어, 새 프로젝트를 시작할 때마다 이런 패턴을 수동으로 적용하지 않아도 됩니다.

## 언제 유용한가요

- 새로운 Claude 기능을 만들기 시작했고 탄탄한 초안 프롬프트가 필요할 때.
- 팀 전체에서 일관된 템플릿 스타일을 유지하고 싶은데, 그 스타일이 Anthropic의 프롬프트 엔지니어링 베스트 프랙티스를 이미 반영하고 있길 바랄 때.
- 기존 프롬프트를 Console로 옮기면서 비교 기준이 될 베이스라인이 필요할 때.
- 평가 세트를 만들고 있고, 고정된 지침과 예시별 변수의 경계를 깔끔하게 분리하고 싶을 때.

## 핵심 포인트

- 생성되는 프롬프트는 명시적인 역할 설정을 포함합니다(예: "You will be acting as a content moderator").
- 복잡한 태스크는 답변 전에 생각하도록 지시하는 chain-of-thought `<scratchpad>` 블록으로 보강됩니다.
- 모호하거나 큰 변수는 `<code>{{CODE}}</code>` 같은 XML 태그로 감싸 경계를 분명히 합니다.
- 짧고 단순한 변수는 `{{LANGUAGE}}`처럼 인라인으로 참조할 수 있습니다.
- 변수는 handlebars 표기법을 사용해 Console workbench와 다른 도구에 그대로 연결됩니다.
- 내부적으로는 긴 meta-prompt가 먼저 구조를 계획하고, XML 태그를 출력의 "spine"으로 사용합니다.
- ZoomInfo가 고객 사례로 등장합니다. ZoomInfo의 Principal Data Scientist Spencer Fox는 며칠 만에 MVP에 도달했고 프롬프트 정제 시간을 80% 줄였다고 말합니다.

## 번들 리소스

- Skill: `skills/prompt-template-bootstrap/SKILL.md` — 생성기를 언제 쓸지, 출력에 어떤 기법이 이미 들어 있는지, 그리고 결과물을 어떻게 편집하고 평가할지.
- Reference: `skills/prompt-template-bootstrap/references/best-practices-from-post.md` — 글에서 생성기에 내장되어 있다고 명시한 프롬프트 엔지니어링 기법들.
- Examples: `skills/prompt-template-bootstrap/examples/template-fragments.md` — 글이 직접 인용한 템플릿 단편들(콘텐츠 모더레이터 역할, scratchpad 권고, 코드 번역 XML, ZoomInfo 인용).

## 출처

Generate better prompts in the developer Console — Anthropic, 2024년 5월 20일: <https://claude.com/blog/prompt-generator>
