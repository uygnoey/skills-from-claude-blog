[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
**Compliance API가 이제 Claude Cowork와 Claude Code까지 커버**한다는 발표입니다. 베타이며 Claude Enterprise 고객이 대상입니다. Cowork는 데스크톱·웹·모바일에서, Claude Code는 CLI와 데스크톱 앱에서 커버됩니다. 두 제품 모두 동일한 Compliance API 인터페이스로 읽히므로, 컴플라이언스·보안 팀은 세션 콘텐츠와 메타데이터를 두 곳이 아니라 한 곳에서 가져옵니다.

글은 세션 레코드에 무엇이 담기는지 나열합니다. 프롬프트와 응답, 툴 호출 콘텐츠(웹 및 Model Context Protocol), 그리고 트랜스크립트 텍스트로 캡처되는 스킬과 아티팩트입니다. 여기에 따라붙는 메타데이터는 검증된 사용자 ID와 이메일 주소, 조직 ID, 세션 ID와 메시지별 ID, 타임스탬프입니다. 또한 이번 베타가 커버하지 **않는** 범위를 명시하고, 새 인프라가 필요 없다는 점을 확인합니다. 커버리지는 Compliance API에 포함되어 기존 Compliance Access Key로 사용하며, 이미 OpenTelemetry 데이터를 내보내는 조직은 두 시스템을 나란히 계속 운영할 수 있습니다.

## 언제 유용한가요
- 컴플라이언스·보안 팀이 Cowork와 Claude Code 세션을 이미 쓰고 있는 Compliance API 감사 피드에 함께 담아야 할 때.
- 보존(retention), eDiscovery, 조사 프로그램의 범위를 잡으면서 오늘 기준으로 어떤 표면이 범위에 들어오는지 정확히 알아야 할 때.
- 세션별·메시지별로 어떤 필드가 캡처되는지 감사인이나 리뷰어에게 설명해야 할 때.
- Compliance API와 나란히 OpenTelemetry 내보내기를 계속 돌릴지 결정할 때.

## 핵심 포인트
- **베타, Claude Enterprise 전용.** 커버리지는 오늘부터 사용 가능하며 Compliance API에 포함됩니다. 별도 권한 없이 기존 Compliance Access Key를 그대로 씁니다.
- **단일 인터페이스.** Cowork와 Claude Code의 세션 콘텐츠·메타데이터를 동일한 Compliance API 인터페이스로 가져옵니다.
- **커버되는 표면.** Cowork는 데스크톱·웹·모바일, Claude Code는 CLI와 데스크톱 앱.
- **캡처되는 세션 콘텐츠.** 프롬프트와 응답, 툴 호출 콘텐츠(웹 및 Model Context Protocol), 트랜스크립트 텍스트로 캡처되는 스킬과 아티팩트.
- **캡처되는 세션 메타데이터.** 검증된 사용자 ID와 이메일 주소, 조직 ID, 세션 ID와 메시지별 ID, 타임스탬프.
- **베타 제외 범위.** 웹의 Claude Code, Claude Platform을 통한 Claude Code, 그리고 Amazon Bedrock·Google Cloud Vertex AI·Microsoft Foundry에서의 세션.
- **OpenTelemetry와 공존.** 이미 OTel 데이터를 내보내는 조직은 추가 인프라 요구사항 없이 두 시스템을 동시에 계속 운영할 수 있습니다.

## 번들 리소스
- `skills/compliance-session-coverage/SKILL.md` — Cowork와 Claude Code를 아우르는 Compliance API 조회 범위를 잡고, 의존하기 전에 커버리지를 확인합니다.
- `skills/compliance-session-coverage/references/coverage-matrix.md` — 커버되는 표면, 제외되는 표면, 글에 명시된 모든 캡처 필드.
- `skills/compliance-session-coverage/templates/coverage-verification-checklist.md` — 감사나 조사 전에 범위를 확정하는 기입식 체크리스트.

## 출처
- https://claude.com/blog/compliance-api-cowork-and-claude-code
