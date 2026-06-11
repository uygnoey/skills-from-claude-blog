[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Skills를 프롬프트, Projects, MCP, Subagent와 비교해 Claude 생태계에서 Skills가 어디에 위치하는지 설명하고, 이 요소들을 어떻게 조합해 워크플로를 구성하는지 예시로 보여줍니다.

## 언제 유용한가요
반복되는 지시를 Skill로 만들지, 대화형 프롬프트로 남길지, 배경 지식을 Project에 둘지, MCP로 데이터를 연결할지, Subagent로 작업을 위임할지 판단해야 할 때 유용합니다.

## 핵심 포인트
- Skill은 (지침 + 선택적 코드/에셋)으로 구성된 재사용 번들이며, progressive disclosure 방식으로 관련 있을 때만 동적으로 로드됩니다.
- 프롬프트는 대화 중에 주는 일회성 지시입니다.
- Project는 자체 지식 베이스를 가진 지속형 워크스페이스입니다.
- Subagent는 별도의 프롬프트와 툴 권한을 가진 전문화된 보조 에이전트입니다.
- MCP는 데이터가 있는 외부 시스템에 Claude를 연결합니다.

## 번들 리소스
- Skill: `skills/skills-stack-explainer/`
- Agent: `agents/market-researcher.md`, `agents/technical-analyst.md`, `agents/code-reviewer.md`
- Guide: `guides/skills-vs-prompts.*.md`, `guides/skills-vs-projects.*.md`, `guides/skills-vs-mcp.*.md`, `guides/skills-vs-subagents.*.md`

## 출처
- https://claude.com/blog/skills-explained
