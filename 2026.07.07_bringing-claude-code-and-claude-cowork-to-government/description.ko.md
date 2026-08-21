[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic이 Claude Code와 Claude Cowork을 Claude for Government Desktop을 통해 퍼블릭 베타로 제공한다고 발표했다. FedRAMP High 인증 환경을 통해 전달되며, 기관은 상용 고객과 동일한 릴리스 일정으로 기능을 받는다.

발표는 네 가지 영역을 다룬다. 데이터가 어디에 있는지(추론은 인증 환경 안에서, 대화 기록은 기관이 관리하는 기기에 로컬 저장), 지출을 어떻게 제한하는지(표준 시트 또는 맞춤 티어, 고정 단위 구매와 하드 not-to-exceed 상한), 관리 권한을 어떻게 위임하는지(부처 수준의 시트 배분, 레이트 리밋·달러 상한·허용 모델을 정하는 SCIM 그룹 매핑, 하위 기관 기본값을 정하는 계층형 구성), 그리고 감독이 어떻게 작동하는지(제품 내에서 검토 가능한 해시 체인 감사 로그, Anthropic 측 민감 작업에 대한 2인 승인, 미터링 데이터만 담긴 사용량 내보내기)다. 뒷받침 문서로는 공개된 FedRAMP Secure Configuration Guide와 공식 변경 고지, 그리고 트러스트 센터를 통해 NDA 하에 제공되는 침투 테스트 요약본이 있다. 데스크톱 앱은 표준 기관 MDM 플랫폼을 통해 배포된다.

## 언제 유용한가요
- ATO 패키지나 보안 심사를 준비하면서 처리가 어디서 일어나고 데이터가 어디에 남는지 기술해야 할 때.
- 하나의 인가 아래에서 부처가 여러 하위 기관에 시트와 서로 다른 제한을 배분해야 할 때.
- 재무 부서가 종량제 가격을 세출 예산과 맞춰야 할 때.
- 감찰관이나 감사인이 사용량 수치를 요구하는데 민감 자료를 경계 밖으로 내보낼 수 없을 때.
- 대화 기록이 노트북에 남는 도구의 MDM 배포와 엔드포인트 정책을 계획할 때.

## 핵심 포인트
- **FedRAMP High이고, 추론도 경계 안에서 실행된다.** Claude for Government Desktop을 통해 전달되며 현재 퍼블릭 베타다.
- **대화 기록은 로컬에 있다.** 기관이 관리하는 기기에 저장되므로 엔드포인트가 심사 범위에 들어온다. 디스크 암호화, 백업, 보존, 기기 분실 절차는 벤더 보존이 아니라 기관 엔드포인트 정책의 문제다.
- **지출은 하드 상한으로 제한된다.** 사용량은 고정 단위로 구매되고 not-to-exceed 상한이 걸리며, 관리 콘솔에서 사용자별·모델별로 추적되고, 잔액 소진 전에 자동 번다운 알림이 나간다.
- **제한은 아이덴티티를 따라 붙는다.** SCIM 그룹 매핑이 그룹별 레이트 리밋·달러 상한·허용 모델을 정하고, 계층형 구성이 Claude가 무엇에 연결할 수 있고 어떤 기능을 쓸 수 있는지에 대한 하위 기관 기본값을 정한다.
- **감독 기능이 내장되어 있다.** 조직 관리자가 제품 안에서 직접 검토할 수 있는 해시 체인 감사 로그가 있고, Anthropic 측 민감 작업에는 2인 승인이 필요하다.
- **사용량 내보내기에는 미터링 데이터만 담기므로,** 민감 자료를 옮기지 않고도 ATO와 IG 질의에 답할 수 있다.
- **문서는 두 단계로 제공된다.** FedRAMP Secure Configuration Guide와 공식 변경 고지는 공개, 침투 테스트 요약본은 트러스트 센터를 통해 NDA 하에 제공된다.
- **상용 고객과 동일한 릴리스 일정** — 이점인 동시에 변경 관리 의무이기도 하다.
- **Anthropic이 계약상 청구 주체이며,** 별도의 클라우드 사업자 관계는 필요하지 않다. 신규 고객은 claude.com/solutions/government 에서 액세스를 요청한다.

## 번들 리소스
- `skills/government-deployment-planning/SKILL.md` — 인가 경계에서 리스크 레지스터까지, 배포를 7단계 절차로.
- `skills/government-deployment-planning/references/controls-inventory.md` — 발표된 전체 통제 항목을, 심사자가 던질 질문별로 묶어서.
- `skills/government-deployment-planning/templates/rollout-checklist.md` — 인가, 증거, 아이덴티티, 비용, 감독, 엔드포인트, 계약, 사용자를 아우르는 실무 체크리스트.
- `skills/government-deployment-planning/templates/evidence-map.md` — ATO 패키지용, 심사 질문과 산출물을 한 장으로 대응시킨 표.
- `guides/agency-rollout.{en,ko,es,ja}.md` — 인가·예산·운영·배포를 맡은 사람들에게 이 발표가 실제로 무엇을 뜻하는지.

## 출처
[Bringing Claude Code and Claude Cowork to government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government) — 2026-07-07 게시.
