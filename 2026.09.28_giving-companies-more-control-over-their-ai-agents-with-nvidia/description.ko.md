[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
NVIDIA의 Open Agent Safety Platform 발표에 맞춰, Anthropic과 NVIDIA가 에이전트 스택에 보안·통제 계층을
더하는 방법을 소개한 발표 글입니다. Claude Managed Agents는 이미 샌드박스에서 작업을 실행하며, 셀프 호스팅
샌드박스로 실행을 자사 경계 안에 두고, NVIDIA OpenShell이 그 샌드박스 안에서 에이전트가 접근하고 할 수 있는
일을 정책으로 통제합니다.

## 언제 유용한가요
- 에이전트가 저장소를 클론하고, 웹사이트를 읽고, 도구 출력을 파싱하거나 패키지를 설치할 때
- 코드와 데이터가 기업·규제 경계 밖으로 나가면 안 될 때
- 에이전트에 필요한 최소 권한을 정하고 증명해야 할 때

## 핵심 포인트
- 샌드박스에 들어온 신뢰할 수 없는 콘텐츠에는 프롬프트 인젝션이나 실행되는 코드가 섞일 수 있습니다.
- '두뇌'와 '손'을 분리합니다. 하네스·세션 상태·자격 증명은 샌드박스 밖의 내구성 있는 인프라에 두고,
  샌드박스는 실행용 도구로만 씁니다.
- 셀프 호스팅 샌드박스: 에이전트 루프(오케스트레이션, 컨텍스트 관리, 오류 복구)는 Anthropic 인프라에
  남고, 각 세션의 도구 호출은 자사 인프라나 관리형 샌드박스 제공자에서 실행됩니다.
- NVIDIA OpenShell은 규칙이 허용하지 않으면 모두 차단하고, 도구 사용마다 검사하며, 파일·네트워크·데이터에
  규칙을 적용합니다. 규칙은 에이전트 밖에서 강제되고 모든 허용·차단 결정이 기록됩니다.
- 좁은 권한으로 시작해 로그를 검토하고 Claude로 규칙을 좁혀 갑니다. OpenShell의 policy prover는 수학적
  증명으로 에이전트가 닿을 수 있는 범위를 확인합니다.
- 사례: Clay의 Sculptor(외부 파일 저장소 마운트, 패키지 즉석 설치), Rogo(규제 산업 고객을 위한 격리
  microVM).
- Managed Agents는 퍼블릭 베타, OpenShell은 Apache 2.0 오픈소스입니다.

## 번들 리소스
- 스킬: `isolate-agent-execution` — 두뇌/손 분리, 셀프 호스팅 샌드박스, 기본 거부 정책 런타임 적용 절차와
  아키텍처 체크리스트 레퍼런스

## 출처
- https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia
