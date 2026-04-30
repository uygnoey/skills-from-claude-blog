[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Security 이제 public beta

## 이 글이 뭔가요

Anthropic이 2026년 4월 30일에 공개한 발표로, 이전에는 Claude Code Security로 불리던 Claude Security를 모든 Claude Enterprise 고객에게 public beta로 오픈한다는 내용입니다. 이 제품은 Claude Opus 4.7을 사용해 코드베이스를 스캔하고, 타깃 패치를 생성하며, 발견된 이슈를 기존 보안 워크플로우로 흘려보냅니다. Claude Team·Max 고객 대상 액세스는 "coming soon". 글은 스캔 동작 방식, 한정 preview 이후 바뀐 점, 명시된 기술/서비스 파트너, 고객 인용을 다룹니다.

## 언제 유용한가요

- Claude Enterprise 고객으로서, 코드베이스 전반에 Claude Security를 도입할지 평가 중일 때.
- 스캔 주기, 범위(repository / directory / branch), 그리고 결과가 Slack·Jira·감사 시스템·취약점 관리 프로그램으로 어떻게 흐를지 설계해야 할 때.
- 도입 경로 비교가 필요할 때: `claude.ai/security` 직접 사용 / 파트너 플랫폼(CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, Wiz) 임베드 / 서비스 파트너(Accenture, BCG, Deloitte, Infosys, PwC)와 함께 진행.
- 엔지니어링 팀과 공유하기 전에 dismiss-with-reason과 confidence rating 워크플로우를 이해하고 싶을 때.

## 핵심 포인트

- Claude Security는 Claude Enterprise 고객 대상 public beta. Claude Team·Max 고객용은 곧 제공.
- Claude Opus 4.7 기반이며 Claude.ai 사이드바 또는 `claude.ai/security`에서 접근 — API 통합이나 커스텀 agent 빌드 불필요.
- 스캔 범위는 repository, 특정 디렉터리, 또는 branch 단위로 좁힐 수 있음.
- Claude는 보안 연구자처럼 코드를 추론합니다: 알려진 시그니처를 패턴 매칭하는 대신 파일·모듈 간 상호작용과 데이터 흐름을 추적합니다.
- 각 결과에는 confidence rating, severity, 예상 impact, 재현 절차, 그리고 Claude Code on the Web에서 바로 열 수 있는 타깃 패치가 포함됩니다.
- 한정 preview 이후 개선: scheduled scans, 디렉터리 단위 타깃 스캔, 이유 명시 dismiss, CSV/Markdown export, Slack/Jira 등으로의 webhook.
- Opus 4.7을 임베드하는 기술 파트너: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Trend.ai, Wiz.
- 서비스 파트너: Accenture, BCG, Deloitte, Infosys, PwC.
- 글에 실린 고객 인용: DoorDash 외에 Staff Product Security Engineer, Information Security Officer, Head of Security, Head of Security.
- Claude Opus 4.7에는 새로운 cyber safeguard가 있고, 합법적 보안 업무가 이를 트리거할 수 있는 조직은 Cyber Verification Program에 참여 가능.

## 번들 리소스

- Skill: `skills/security-public-beta-rollout-guide/SKILL.md` — Claude Security 사용 시점, 스캔 범위 지정, 결과 해석, 그리고 직접 / 파트너 플랫폼 / 서비스 파트너 중 적합한 도입 경로 선택.
- Reference: `skills/security-public-beta-rollout-guide/references/features-and-partners-from-post.md` — 기능, 스캔 워크플로우, 파트너, 고객 인용을 글의 표현 그대로 정리.
- Examples: `skills/security-public-beta-rollout-guide/examples/scan-and-triage-workflows.md` — 글에 기반한 스코핑·스케줄링·트리아지 예시 워크플로우.

## 출처

Claude Security is now in public beta — Anthropic, 2026년 4월 30일: <https://claude.com/blog/claude-security-public-beta>
