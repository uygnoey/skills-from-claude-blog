[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Models on Google Cloud (Anthropic managed)가 정식 출시(GA)되었다는 발표입니다(2026년 10월 22일).
Google Cloud 고객은 Google Cloud IAM, 결제, 약정 차감을 그대로 쓰면서 Claude Platform 기능 전체를
이용할 수 있습니다. Google이 관리하는 Google managed 제공 방식도 계속 제공됩니다.

## 언제 유용한가요
- Google Cloud 고객이 Anthropic managed와 Google managed 중 하나를 골라야 할 때.
- Google Cloud를 떠나지 않고 새 Claude 기능과 베타를 출시 당일부터 쓰고 싶을 때.
- 온보딩 전에 결제, IAM, 할인 처리를 계획할 때.

## 핵심 포인트
- Anthropic managed: Claude API 기능 전체를 제공하고, 새 기능과 베타가 네이티브 Claude Platform과 같은 날
  나옵니다. 서비스 운영과 데이터 처리자(data processor)는 Anthropic입니다.
- 기존 Google Cloud IAM 자격 증명으로 동작하고, Google Cloud 청구서 하나로 결제되며, Google Cloud 약정을
  차감합니다. 현재 US와 Global 엔드포인트를 지원합니다.
- 포함 기능: Managed Agents(베타), 코드 실행, 컴퓨터 사용, 에이전트 스킬, 어드바이저 전략(베타),
  Files API, 인용(citations), 웹 검색과 웹 페치, MCP 커넥터(베타), 프롬프트 캐싱, 배치 처리.
- Claude Opus 5.5의 Fast Mode도 여기서 GA입니다. 출력 생성 최대 2.5배 빠르며, 입력·출력 100만 토큰당
  $8 / $40입니다.
- Claude Console로 프롬프트 작성, 에이전트 구성과 호스팅 실행, 사용량·비용 모니터링, 워크스페이스별
  접근 관리를 할 수 있습니다. 모델: Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5.
- Google이 데이터 처리자여야 하거나, 엄격한 지역 데이터 레지던시가 필요하거나, Model Armor나 Agent Engine
  같은 네이티브 통합이 필요하면 Google managed가 여전히 맞는 선택입니다.
- 기존 할인이 있다면 먼저 담당 어카운트 이그제큐티브에 연락하세요. 할인은 소급 적용되지 않습니다.

## 번들 리소스
- 스킬: `google-cloud-offering-selector` (`references/feature-matrix.md`,
  `templates/offering-decision.md`).

## 출처
- https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
