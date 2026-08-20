[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
25만 개 이상의 기업이 쓰는 업무 관리 플랫폼 monday.com이, 사람이 업데이트해야 하는 도구에서 사람과 에이전트가 같은 아이템 위에서 함께 일하는 에이전트 우선(agent-first) 제품으로 스스로를 다시 만든 고객 사례. 재구축된 경험은 2026년 5월에 출시됐고, 두 달 만에 에이전트 상호작용 500만 건에 도달했다.

글은 잘 안 됐던 시도부터 짚는다. 2025년 5월 "AI month" 동안 monday는 기존 워크플로에 AI 기능을 얹었다. 텍스트 요약, 정보 분류 같은 것들이다. 도입 자체는 실제로 일어났지만 패턴이 자리 잡지는 못했다. 제품 담당 VP Orly Stern Izhaki는 그 시기를 "AI dust"를 만들던 때 — 그 외에는 바뀐 게 없는 워크플로 위에 자동화를 흩뿌리던 때 — 라고 부르고, 거기서 내린 결론은 AI 기능을 도입하는 것과 AI 회사가 되는 것은 다르다는 것이었다. 최고 제품·기술 책임자 Daniel Lereya는 에이전트 우선 제품으로의 전환을 회사가 내린 가장 중요한 결정 중 하나로 설명한다.

이후에 일어난 것은 추가가 아니라 재구축이었다. Claude를 플랫폼에 들이는 네 가지 방식, IT·HR·마케팅·경영진 오피스 전반에 걸쳐 정의된 역할을 가진 이름 붙은 에이전트들, 그리고 별도의 챗 창이 아니라 보드 안의 트리거와 멘션으로 일을 배정받는 팀원으로서의 에이전트다.

## 언제 유용한가요
- AI 기능을 이미 출시했고 첫 달 지표는 괜찮아 보였는데, 사용량이 가끔 하는 요약 정도로 평평해졌을 때.
- 에이전트를 기존 워크플로에 끼워 넣을지, 아니면 워크플로 자체를 에이전트 중심으로 다시 만들지 판단해야 할 때.
- 에이전트가 실제 업무가 놓인 곳과 평행한 챗 화면에서 동작해서, 맥락을 사람이 손으로 붙여 넣어야 할 때.
- 거버넌스·권한·신뢰성을 처음부터 설계하지 않아서 에이전트 파일럿이 프로덕션 직전에 계속 멈출 때.
- 범용 어시스턴트 하나를 배포하는 대신, 기능 조직별로 구체적인 에이전트 업무를 정의해야 할 때.

## 핵심 포인트
- **"AI dust"가 실패 양상이다.** 기존 워크플로 위에 자동화를 흩뿌리면 요약·분류처럼 도움은 되는 기능이 생기지만 일하는 방식은 바뀌지 않고, 사용량도 복리로 쌓이지 않는다.
- **네 가지 배포 경로.** Claude를 모델로 삼아 프롬프트로 만드는 monday Agents, Claude Managed Agents를 플랫폼에 합류시키는 BYOA(bring your own agent), 법무·재무 플러그인을 포함해 monday Agents Store에서 가져오는 사전 구축 전문 에이전트, 그리고 대시보드에서 Claude를 연결해 작업을 배정하고 고객 환경에서 실행하는 코딩 통합.
- **에이전트에는 범용 권한이 아니라 이름 붙은 업무를 준다.** IT는 Intake & Triage Agent, Knowledge Agent, Incident Agent를 운영하고, HR은 이력서 스크리닝·면접 일정·채용 코디네이션·피드백 관리를, 마케팅은 경쟁 인텔리전스와 배틀카드를, 경영진 오피스는 Operator Agent, Org Health Agent, Strategy Consultant Agent를 둔다.
- **팀원으로 설계한다.** 각 에이전트는 이름과 아바타, 그리고 워크플로 안의 자리를 갖는다. 일은 별도 챗 인터페이스가 아니라 직원들이 이미 있는 곳에서 트리거와 멘션으로 배정된다.
- **생산 라인이 하나의 아이템 위에서 돌아간다.** 캠페인 예시에서 브리프는 마케터와 콘텐츠 리드가 잡고, Strategist Agent가 목표·메시징 축·채널·지표로 구조화하고, Claude Managed Agent가 랜딩 페이지 변형을 만들고, Brand Reviewer가 브랜드 가이드라인 대조로 문제를 표시하고, 사람이 승인한 뒤 발행된다.
- **고객의 고객, Cooke Seafood.** 세계 최대 가족 소유 수산 기업으로, 진행·제안 중인 약 200개 프로젝트의 딜리버리와 리소스 관리, 130건의 계약 관리, 그리고 리스크를 RAID 로그로 올려 주는 자동 리포팅을 운영한다. 전략 담당 디렉터 Patti Stevens는 이 변화를 업데이트해야 했던 플랫폼에서 그 위에서 운영하는 플랫폼으로 바뀐 것이라고 표현한다.
- **다섯 가지 교훈.** 기술보다 멘탈 모델을 옮기는 게 더 어려웠다. 방향·UX·기술·가격·신뢰 모델·품질 정의가 동시에 움직이는 동안, 소유권이 분명하고 결정이 빠른 소규모 팀이 계층 구조보다 정렬을 잘 유지했다. 도입 여부는 거버넌스·권한·투명성·신뢰성이라는 신뢰 인프라에 달려 있었다. 에이전트 역량은 백엔드 투자에 좌우됐고, 엔터프라이즈 규모에서 라이브 프로젝트 데이터에 에이전트를 붙들어 두기 위해 monday DB에 투자했다. 그리고 이 전환은 기존 정체성을 대체한 게 아니라 확장한 것이었다.

## 번들 리소스
- `skills/agent-first-product-transformation/SKILL.md` — AI 기능 단계에서 에이전트 우선 제품으로 옮겨 가기.
- `skills/agent-first-product-transformation/references/deployment-models.md` — 에이전트를 플랫폼에 들이는 네 가지 방식과 각각이 맞는 상황.
- `skills/agent-first-product-transformation/references/agent-job-map.md` — 기능 조직별 이름 붙은 에이전트 업무.
- `skills/agent-first-product-transformation/references/transformation-lessons.md` — 다섯 가지 교훈과 각각이 계획에 의미하는 것.
- `skills/agent-first-product-transformation/examples/campaign-production-line.md` — 마케팅 엔드투엔드 예시와 Cooke 배포 사례.
- `agents/*.md` — 글에 이름이 나온 역할에서 도출한 서브에이전트 다섯 개.
- `guides/agent-first-platform-rollout.{en,ko,es,ja}.md` — AI 기능에서 에이전트 우선으로 가는 롤아웃 순서.

## 출처
[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) — 2026-08-20 게시.
