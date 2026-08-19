[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
생명과학 조직을 위한 실무 배포 가이드인 Claude Science 제품 가이드를 소개하는 글입니다. 블로그 글 자체는 가이드의 요약이며 전체 PDF로 연결됩니다.

Claude Science(베타)는 생명과학의 모든 디지털 단계를 위한 애플리케이션으로 소개됩니다. 연구자의 데이터 옆에서 실행되며, 추적·재현·방어가 가능한 결과를 만들어내도록 설계되었습니다. 가이드는 어떤 작업에 어떤 Claude 표면(surface)을 써야 하는지, Claude Science가 내부적으로 어떻게 동작하는지, 분석이 검토를 견디게 만드는 설계 선택들, 3단계 도입 로드맵, 기능·워크플로 사용 사례, 그리고 CIO와 IT 리더를 위한 FAQ를 다룹니다.

## 언제 유용한가요
- 연구 조직이 어떤 종류의 과학 업무(분석 vs 문서 작업 vs 프로덕션 파이프라인)에 어떤 Claude 표면이 맞는지 정해야 할 때.
- 연구 IT가 과학자들이 통제 데이터를 다루기 전에 설치 풋프린트, 샌드박스, 네트워크 허용 목록, 컴퓨트 디스패치 대상을 검토해야 할 때.
- 조직 전체를 한 번에 켜는 대신 계산 그룹부터 단계적으로 롤아웃을 계획할 때.
- 논문, 규제 제출, 내부 검토를 위해 결과가 재현 가능하고 방어 가능해야 할 때.

## 핵심 포인트
- **표면 선택이 먼저다.** 분석·그림·결과는 Claude Science, 빠른 질문과 초안은 Claude Chat, 연구/제출 수준의 문서 작업은 Claude Cowork와 Claude for Microsoft 365, 산출물이 배포되는 소프트웨어일 때는 Claude Code, 임베디드·호스팅 에이전트는 Claude Platform과 Claude Managed Agents. 대부분의 조직은 둘 이상을 함께 배포합니다.
- **데이터가 있는 곳에서 실행된다.** macOS와 Linux에서 로컬 데몬으로 실행되며(노트북, 랩 Linux 장비, HPC 로그인 노드, 클라우드 VM), UI는 브라우저에 있습니다. 무거운 작업은 같은 세션에서 SSH 호스트, SLURM 클러스터(배치 지시문 자동 작성), 서버리스 GPU 계정으로 디스패치됩니다.
- **도메인 역량이 첫날부터 제공된다.** 일반적인 과학 워크플로용 구성 가능한 역량, 60개가 넘는 과학 데이터베이스에 대한 선택적 연결, 약 150개의 큐레이션된 스킬. 스킬은 문서를 검색하는 대신 코드를 실행하므로 한 분석 안에서 체이닝할 수 있고, 각 스킬은 오픈소스라 팀이 직접 검사·버전 고정·확장할 수 있습니다.
- **분석을 검토 가능하게 만드는 다섯 가지 설계 선택**: 지속 커널(에이전트가 자기 플롯을 직접 봄), 모든 아티팩트의 4계층 프로버넌스(설명, 코드, 대화, 환경 스냅샷), 근거를 추적할 수 없는 주장을 표시하는 백그라운드 리뷰어 에이전트, 실행 전 계획 수립과 가시적인 권한 모델, 그리고 내장 바이오시큐리티 안전장치.
- **3단계 로드맵**: Foundation(IT·데이터 거버넌스 검토, 데몬 호스트 패턴 결정, 2~3개 챔피언 그룹, SSO/SCIM, 관리자 활성화), Pilot(실제 랩 데이터로 실제 분석, 주간 체크인, 사이클 타임·유지율·콜드 재현율 측정), Scale(관리형 데몬 호스트 패턴, 조직 스킬 카탈로그 큐레이션, 검증된 허용 목록, 프로버넌스 보존 정책).
- **파일럿이 잘 되고 있다는 신호는 챔피언들이 자기 스킬을 저장하기 시작할 때**입니다. 랩 내부 정규화 파이프라인이나 LIMS API를 한 번 감싸두면 이후 모든 세션이 이를 물려받습니다.
- **스킬 vs 커넥터**: 답이 조직 자체 시스템에 있고 엔타이틀먼트가 중요하면 커넥터, 답이 공개 기록에 있으면 과학 데이터 스킬. 실제 질문 대부분은 둘 다 씁니다.
- **알려진 한계를 명확히 밝힙니다**: 연구 용도이며 임상·진단 의사결정용이 아님, GxP 검증 시스템이 아님, 출시 시점에 HIPAA 대응 아님, Windows 미지원, Bedrock·Vertex AI·Foundry로는 제공되지 않음, Zero Data Retention 미적용, NIH 통제 접근 데이터 규정 준수는 로드맵상 과제.

## 번들 리소스
- `skills/life-sciences-ai-rollout/SKILL.md` — AI 연구 워크벤치의 단계적 롤아웃을 계획하고 실행하는 방법.
- `skills/life-sciences-ai-rollout/references/surface-selection.md` — 어떤 업무에 어떤 표면을 쓸지 정리한 제품 매트릭스.
- `skills/life-sciences-ai-rollout/references/product-architecture.md` — 로컬 데몬, 컴퓨트 디스패치, 다섯 가지 설계 선택.
- `skills/life-sciences-ai-rollout/references/scientific-data-skills.md` — 답하는 질문 유형별로 묶은 스킬 카탈로그.
- `skills/life-sciences-ai-rollout/references/it-security-faq.md` — CIO·IT 리더용 FAQ.
- `skills/life-sciences-ai-rollout/templates/adoption-roadmap.md` — 단계별 롤아웃 계획 템플릿.
- `skills/life-sciences-ai-rollout/templates/pilot-scorecard.md` — 파일럿 측정 시트.
- `skills/life-sciences-ai-rollout/examples/workflow-use-cases.md` — 탐색·분석·발표 단계별 사용 사례.
- `guides/life-sciences-deployment.{en,ko,es,ja}.md` — 4개 언어 전체 배포 가이드.

## 출처
- https://claude.com/blog/the-claude-science-product-guide
