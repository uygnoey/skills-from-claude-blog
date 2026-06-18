[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Claude Platform에서 Workload Identity Federation(WIF)이 정식(GA) 출시되었음을 알립니다.

## 언제 유용한가요
CI, 클라우드 서비스, Kubernetes 잡 등 “워크로드”가 장기 보관되는 정적 API 키를 관리하지 않고 Claude API를 호출해야 할 때 유용합니다.

## 핵심 포인트
- WIF는 정적 API 키 대신, 요청 시점에 발급되는 단기·스코프 제한 자격 증명으로 인증합니다.
- WIF는 OIDC 호환 IDP와 함께 동작하며, 모든 Claude API 엔드포인트(퍼스트파티 SDK 및 Claude Code 경유 포함)에 적용됩니다.
- Claude Platform에 서비스 계정이 도입되어, 워크로드별로 고유한 아이덴티티/역할/감사 추적(audit trail)을 가질 수 있습니다.
- 페더레이션 규칙이 외부 아이덴티티(OIDC 토큰 클레임)를 Claude 서비스 계정에 바인딩합니다.
- API 키와 WIF는 공존하므로, 워크로드를 하나씩 점진적으로 마이그레이션할 수 있습니다.

## 번들 리소스
- Agent Skill: WIF 서비스 계정 및 페더레이션 규칙 구성(체크리스트).

## 출처
- https://claude.com/blog/workload-identity-federation
