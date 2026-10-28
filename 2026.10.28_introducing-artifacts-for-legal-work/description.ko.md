[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
2026년 10월 28일 발표 글입니다. Claude for Legal 에 바로 쓸 수 있는 아티팩트가 들어왔습니다. 트래커, 대시보드
같은 대화형 도구로, 법무팀이 자기 데이터와 커넥터로 맞춰 쓰고 회사 안에서 공유할 수 있습니다. 5월에
Claude for Legal 을 낸 뒤 법무팀이 가장 많이 요청한 것은 더 쉬운 설정과 동료와 함께 일하는 더 쉬운 방법이었습니다.

## 언제 유용한가요
- 법무팀이 계약서 묶음 검토, 인용 확인, 관할별 규정 비교, 진행 중인 사건 추적, 다가오는 규제 파악을 해야 하고,
  다시 쓸 수 있는 도구가 필요할 때.
- 현업 동료가 법무 요청을 Claude 안의 한 곳으로 보내게 하고 싶을 때.
- 동료, 고객, 파트너와 법무 결과물을 공유하면서 비밀 유지와 윤리적 차단벽(ethical wall)을 지켜야 할 때.
- 법률 구조나 공익 법률 일을 하며, 사법 접근성(access to justice) 업무의 출발점이 될 도구가 필요할 때.

## 핵심 포인트
- 일하는 방식: 법률 전문가가 문서와 근거 자료를 가져오면 Claude 가 1차 작업을 하고, 변호사가 판단을 더합니다.
  아티팩트마다 예시가 먼저 열리고, 답마다 출처 링크가 붙습니다.
- 갤러리 아티팩트: Cite check(원문과 다른 인용, 틀린 쪽 번호, 주장을 뒷받침하지 않는 출처 표시), Jurisdiction
  survey matrix(한 주제를 주·국가별로 한 표에 비교, 법령 링크), Matter board(담당자, 다음 단계, 다음 기한),
  Playbook deviation board(표준 조건과 다른 조항을 표시해 예외 승인자에게 전달), Regulatory horizon scan(다가오는
  규제를 타임라인에 놓고 영향도순 정렬), Tabular review(계약서 묶음에서 원하는 조건을 표로, 정확한 문구 링크).
- 아티팩트를 팀에 맞게 바꿔 달라고 Claude 에 요청할 수 있고, 플레이북과 리서치 소스는 수동 업로드 대신 커넥터로
  가져옵니다. Bloomberg Law, Filevine, Ivo, Legora, Patlytics 등 법무 커넥터가 60개 넘게 추가되었습니다.
- 아티팩트는 조직 안팎에 공유할 수 있고, 공유 설정으로 비밀을 지키고 팀 사이 윤리적 차단벽을 유지합니다.
- 파트너 아티팩트: AI Governance Benchmark(Goodwin), Harvey Intake(Harvey), Obligations Checker(Foley & Lardner),
  Subpoena Response Tool(PwC). Legora 와 Orrick 의 아티팩트도 나올 예정입니다.
- 사법 접근성 아티팩트 9개 가운데 5개는 Claude 크레딧을 지원받은 비영리 단체가 만들었습니다: Criminal Charge
  Reality Check(Zealous, 뉴욕), Immigration Papers Reader(Mobile Pathways), Rent Ledger Reviewer 와 Record-Sealing
  Screener(Rising for Justice, D.C.), Record Clearance(The Access Project).
- Anthropic 은 공익 단체와 법학 교육 프로그램을 지원하고, Legal Ambassadors Program 을 시작합니다(대기자 명단
  모집 중). 도입 계획은 영업팀이나 Accenture, Deloitte, KPMG, PwC 같은 구현 파트너와 세울 수 있습니다.

## 번들 리소스
- 스킬: `legal-artifact-workflows` (`references/gallery-artifacts.md`,
  `references/partner-and-access-to-justice-artifacts.md`, `references/connectors-and-rollout.md`,
  `templates/tailoring-requests.md`, `templates/sharing-checklist.md`, `examples/scenarios.md`).

## 출처
- https://claude.com/resources/articles/introducing-artifacts-for-legal-work
