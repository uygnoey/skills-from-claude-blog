[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
정식 출시(GA) 발표다. 컴퓨터 사용(computer use), Skills API, Files API가 Claude 플랫폼에서 정식 출시되었고, 컴퓨터 사용에는 웹 애플리케이션에서 동작하는 에이전트를 위한 새로운 브라우저 사용(browser use) 도구가 추가됐다. 이 세 가지를 합치면 소프트웨어를 조작하고, 팀의 전문성을 적용하고, 완성된 파일을 돌려주는 에이전트를 만들 수 있다는 것이 글의 틀이다. 이미 GA였던 코드 실행과 웹 검색도 같은 루프에 들어간다.

각 구성 요소의 용도도 설명한다. 컴퓨터 사용은 스크린샷을 받아 에이전트가 눈으로 보는 소프트웨어를 조작하게 하며, 그래서 애초에 자동화를 염두에 두지 않은 애플리케이션에서도 동작한다. 브라우저 사용 도구는 페이지 구조를 더해, 화면상의 위치가 아니라 특정 필드나 버튼을 대상으로 동작하게 한다. 스킬은 지시문·스크립트·템플릿이 담긴 폴더로 작업이 필요로 할 때만 로드되며, Skills API로 업로드·버전 관리하고 Claude의 코드 실행 샌드박스에서 실행된다. Files API는 에이전트가 읽고 쓰는 문서를 저장하고 요청 간에 ID로 참조하게 한다.

## 언제 유용한가요
- 에이전트가 API를 제공하지 않는 애플리케이션이나 포털 안에서 작업해야 할 때.
- 웹 작업에 대해 픽셀 기반 컴퓨터 사용과 구조를 인식하는 브라우저 사용 도구 중 무엇을 쓸지 정할 때.
- 팀 절차가 프롬프트 문자열 안에서 계속 커져, 버전 관리되는 산출물로 옮겨야 할 때.
- 여러 턴에 걸친 워크플로가 매 요청마다 같은 원본 문서를 다시 보내고 있을 때.
- 산출물이 응답 텍스트 한 문단이 아니라 파일일 때.
- 기존 베타 연동을 마이그레이션하면서 GA에서 무엇이 바뀌었는지 알아야 할 때.

## 핵심 포인트
- **턴당 다중 동작.** 업데이트된 컴퓨터 사용 도구는 모델 호출당 한 동작이 아니라 턴당 여러 동작을 수행해, 더 적은 호출과 더 짧은 시간에 작업이 끝난다. 브라우저 사용 도구도 같은 다중 동작 턴을 쓰면서 페이지 구조를 더한다.
- **컴퓨터 사용이 HIPAA 규제 워크로드에 사용 가능해졌다** — Anthropic BAA 하에서.
- **Skills API:** 자기 스킬을 업로드하고 버전 관리하는 더 단순한 API. 스킬은 Claude의 코드 실행 샌드박스에서 돌아가므로 직접 호스팅할 것이 없다.
- **Files API:** 파일 자동 만료, 5배 높아진 레이트 리밋, 조직당 1TB 저장 공간.
- **조합된 루프.** 예시는 클레임 처리 에이전트다. Files API에서 접수 문서를 읽고, 팀의 접수 절차를 담은 스킬을 따르고, 브라우저 사용 도구로 보험사 웹 포털에서 제출을 마치고, 확인서를 다시 파일로 저장한다.
- **새 컴퓨터 사용 도구의 보고된 결과.** API가 없는 의료·보험 시스템 안에서 동작하는 에이전트의 경우, 가장 긴 클레임 워크플로가 32분에서 13분으로 줄고, 테스트한 모든 워크플로에서 작업당 비용이 약 30% 감소했으며, 완료율은 100%에 도달했다. 프롬프트는 바꾸지 않았다.
- **커스터마이즈 지점으로서의 스킬.** Box는 Skills API로 Box Agent에 특화된 문서 생성 기능을 넣었다. 은행의 여신 방법론과 승인된 메모 형식을 스킬이 담고, Box Agent가 이미 Box에 있는 문서에 이를 적용해 애널리스트 검토용의 출처 기반 여신 메모를 만든다. 워크플로마다 에이전트를 처음부터 만들 필요가 없다는 것이다.
- **제공 현황.** Skills API와 Files API는 Microsoft Foundry에서도 제공되며, 업데이트된 컴퓨터 사용과 브라우저 사용은 Google Cloud Vertex AI에 곧 제공된다. 기존 베타 연동은 마이그레이션하는 동안 계속 동작한다.

## 번들 리소스
- `skills/software-operating-agent-stack/SKILL.md` — 네 기능을 하나의 에이전트로 조합하는 법과 선택 규칙.
- `skills/software-operating-agent-stack/references/capabilities.md` — 발표된 그대로의 각 기능과 GA에서 바뀐 점.
- `skills/software-operating-agent-stack/references/availability.md` — 클라우드별 제공 현황과 베타에서의 마이그레이션 순서.
- `skills/software-operating-agent-stack/examples/workflow-shapes.md` — 클레임 에이전트와 Box 조합을 단계별로 매핑.
- `guides/agent-capability-selection.{en,ko,es,ja}.md` — 프로덕션 에이전트를 위한 기능 선택.

## 출처
[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) — 2026-08-20 게시.
