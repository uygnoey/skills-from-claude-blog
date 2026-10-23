[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
2026년 10월 23일 발표입니다. 9월에 Pro·Max 요금제에 먼저 나온 채팅 + Cowork 통합 경험이 이제 Claude
Enterprise에서 정식 출시(GA)되었습니다. 사용자가 얻는 것, 보안 방식, 관리자의 비용 관리 방법, 시작 방법을
다룹니다.

## 언제 유용한가요
- Enterprise 관리자로서 통합 경험을 켜려고 계획할 때.
- 출시 전에 보안·재무 담당자가 클라우드 세션, 데이터 처리, 지출에 대한 답을 원할 때.

## 핵심 포인트
- 웹·데스크톱·모바일에서 하나의 Claude. 대화는 채팅으로 시작하고, 코드나 파일 작업이 필요한 작업은
  클라우드에서 이어져 완성된 문서·분석·덱으로 돌아옵니다. 노트북을 덮어도 작업은 계속됩니다. 채팅,
  프로젝트, 커넥터, 스킬, 플러그인이 그대로 이어집니다.
- 보안: SSO와 Compliance API 위에 구축, 전송 중·저장 시 암호화, 기본적으로 학습에 사용하지 않음,
  클라우드 세션마다 격리된 VM, 네트워크 egress 기본 차단, 커넥터 자격증명은 샌드박스 밖에 보관,
  보안팀을 위한 중앙 가시성.
- 비용: 사용량 기반 요금. Opus 5.5는 일반 워크로드에서 Opus 5보다 40% 저렴, Sonnet 5.5는 Sonnet 5보다
  최대 30% 저렴. 관리자 통제: efficient mode, 모델 권한(entitlements), 지출 한도(조직/그룹/구성원),
  그룹 공동 예산.
- 출시는 Organization settings에서 관리합니다. Claude Code 무보존(ZDR), HIPAA 대응 구성, 고객 관리
  암호화 키를 쓰는 조직은 현재 구성을 유지합니다.

## 번들 리소스
- 스킬: `enterprise-unified-rollout` (`references/security-posture.md`, `references/cost-controls.md`,
  `templates/rollout-checklist.md`).

## 출처
- https://claude.com/resources/articles/unified-claude-enterprise
