[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic이 빠르게 성장하는 12개 이상의 스타트업 — Artemis Security, Cainex, Clay, ClickHouse, Cognition, Commure, Crosby, Emergent, Harvey, Heidi, Higgsfield, Omni, Parahelp, Translucent, Zingage — 을 인터뷰해, 이들이 Claude Code로 어떻게 제품을 만들고 회사를 키우는지 듣고 그 답을 다섯 가지 운영 규칙으로 정리한 글이다. 글이 던지는 틀은 이것이다. 제품 개발 라이프사이클을 처음부터 Claude Code로 설계했다면 어떤 모습일까?

다섯 규칙은 모두가 출시한다, 지루한 일을 자동화한다, 믿되 검증한다, 다시 만들 것을 전제로 만든다, 프로토타입·도그푸딩·프로덕션화다. 각 장에는 창업자 인용과 구체적인 팁이 담겨 있고, 마지막에는 이를 한 페이지로 모은 체크리스트가 붙는다. 보고된 성과로는 출시 기능 30% 증가(ClickHouse), 엔지니어링 생산성 2~3배(Omni), 버그 트리아지 100% 자동화(Clay), 주당 6,000개 이상의 PR(Artemis Security)이 언급된다.

## 언제 유용한가요
- 기능 목록이 아니라, 작은 팀이 에이전틱 코딩을 중심으로 어떻게 조직되어야 하는지에 대한 그림이 필요할 때.
- 제품에 대한 통찰은 비개발자에게 있는데, 아이디어에서 동작하는 프로토타입까지 갈 길이 없을 때.
- SDLC의 어느 부분을 에이전트에 넘길지, 그리고 그것을 신뢰하기 전에 무엇이 갖춰져 있어야 하는지 판단할 때.
- 재작성이 늘 우선순위 싸움에서 밀리고, 기술 부채 정리가 일정에 오르지 못할 때.
- 사내 에이전트 실험을 고객용 제품으로 승격시킬 경로가 필요할 때.

## 핵심 포인트
- **0→1 단계는 모두에게 열리되, 분업은 남는다.** 마케터는 여전히 마케팅을, 개발자는 여전히 개발을 한다. 다만 문제를 이해하는 사람이 첫 버전을 만든다. Heidi는 기존의 핸드오프 사슬을 "고장 난 전화기 문제"라 부른다.
- **기여에는 독려가 아니라 장치가 필요하다.** MCP나 CLI로 Claude를 실제 도구에 연결하고, 프로토타입이 로드맵으로 이어지는 자리를 만들고(Clay의 분기 리뷰, Omni의 Slack 채널), 기준을 스킬로 만들어 디렉터리나 플러그인 마켓플레이스로 공유하라.
- **에이전트가 반복 업무를 끝까지 맡는다.** ClickHouse의 플레이키 테스트·커버리지 에이전트는 해당 저장소의 2위·3위 기여자이며, Clay는 최초 분류부터 수정 제안까지 버그 트리아지를 자동화했고, Translucent의 리뷰어는 변경 전체에 팬아웃해 여러 각도의 결과를 종합한다.
- **규칙 2와 3은 한 쌍이다.** Zingage는 초기에 Claude에 완전한 자율성을 줬다가 "겉보기에는 맞아 보이지만 실제로는 아닌" 방식으로 아키텍처에서 벗어난 그럴듯한 코드를 얻었다. 해법은 `CLAUDE.md`에 적은 567줄의 불변식이었다.
- **예시가 아니라 원칙을 고쳐라.** Cainex는 감사자의 교정 내용을 버전 관리되는 에이전트 지시문에 반영하고 골든 세트와 무작위 샘플로 백테스트한다. 첫 버전이 과적합되어 패치만 쌓인 경험에서 나온 방식이다.
- **영구적인 것은 없다.** Clay는 같은 것을 네 번 만들고, Harvey는 모델 역량의 파도마다 아키텍처를 다시 짰으며, Commure는 피처 플래그 정리를 스킬 호출 하나로 바꿨다. 재구축을 싸게 만드는 것은 git worktree와 플랜 모드다.
- **플라이휠.** 자신의 에이전틱 코딩 실무를 발전시키면 프론티어에서 하네스 설계가 어떻게 진화하는지 알게 되고, 그것을 자기 에이전트와 제품에 쓰게 된다. 사내 에이전트 → 도그푸딩 → Claude API·SDK·Managed Agents 기반 고객용 제품이라는 경로다.

## 번들 리소스
- `skills/agentic-coding-operating-rules/SKILL.md` — 다섯 규칙을 실제 운영 절차로 정리.
- `skills/agentic-coding-operating-rules/references/five-rules.md` — 각 규칙의 전문, 창업자 인용과 경계 조건 포함.
- `skills/agentic-coding-operating-rules/references/checklist.md` — 원문의 기술 체크리스트 통합본.
- `skills/agentic-coding-operating-rules/templates/root-context-file.md` — 불변식을 담는 루트 `CLAUDE.md` 스캐폴드.
- `skills/agentic-coding-operating-rules/examples/self-improvement-loop.md` — Cainex의 교정 루프를 단계별로.
- `skills/agentic-coding-operating-rules/examples/company-patterns.md` — 15개 회사가 실제로 한 것.
- `agents/flaky-test-fixer.md`, `agents/test-coverage-finder.md`, `agents/multi-angle-code-reviewer.md`, `agents/bug-triage.md` — 원문에 명시된 네 가지 에이전트 역할.
- `guides/startup-operating-model.{en,ko,es,ja}.md` — 운영 모델과 도입 순서.

## 출처
[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) — Michael Segner, 2026-08-20 게시.
