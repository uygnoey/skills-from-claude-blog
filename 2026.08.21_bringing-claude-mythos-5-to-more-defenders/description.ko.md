[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
프런티어 사이버 방어 역량을 더 많은 방어자의 손에 쥐어 주기 위한 진행 상황 업데이트입니다. Claude Mythos 5를 이제 Claude Security에서 쓸 수 있고, 파트너들의 사이버 방어 도구에도 곧 들어갑니다. 3,500만 달러 규모의 Defender Advantage Fund가 오픈소스 보안 작업을 지원하며, Cyber Verification Program은 Mythos급 접근으로 확대됩니다.

핵심 아이디어는 모델의 크기가 아니라 상호작용의 형태입니다. 모델에 직접 접근할 수 있을 때 악의적 행위자가 모델을 해로운 용도로 유도하려 시도할 수 있습니다. 사용자가 취약점 패치나 보안 경보 같은 특정 산출물만 받을 수 있다면 그 위험은 훨씬 낮아집니다. 네 가지 접근 경로 모두 모델 직접 접근에는 가드레일을 유지하면서 방어적 *결과물*에 대한 접근을 넓힙니다.

## 언제 유용한가요
- 어떤 접근 경로가 내 상황에 맞는지 정할 때: 코드를 소유했는지, 보안 제품을 만드는지, 오픈소스 메인테이너를 지원하는지, 승인된 방어 업무에 완화된 안전장치가 필요한지.
- 엔터프라이즈 관리자가 Claude Security를 활성화하고 팀에 리포지토리 스캔을 안내할 때.
- CWE 분류, 신뢰도·심각도 등급, 제안 수정안과 함께 반환된 스캔 결과를 분류할 때.
- 프런티어 역량 위에 제품이나 워크플로를 설계하면서 "모델 접근이 아니라 특정 산출물"이라는 형태를 유지해야 할 때.
- 오픈소스 프로젝트가 취약점 패치나 스캔 자동화를 위해 자원이 필요할 때.

## 핵심 포인트
- **상호작용의 형태가 곧 통제 수단입니다.** "사용자가 취약점 패치나 보안 경보 같은 특정 산출물만 받을 수 있다면 그 위험은 훨씬 낮아진다"는 것이 직접 모델 접근과의 대비입니다.
- **Project Glasswing**(4월)은 Mythos Preview와 Mythos 5를 세계에서 가장 중요한 소프트웨어를 지키는 소수 조직에 제공해, 동등한 역량이 널리 퍼지기 전에 방어자에게 시간 창을 벌어 줬습니다. **Claude Fable 5**는 널리 제공하되 이중 용도 사이버 작업을 차단한 첫 광범위 단계였습니다.
- **파트너 통합:** Mythos 5가 방어자들이 이미 쓰는 보안 운영·사고 대응·위협 인텔리전스·탐지 엔지니어링 제품에 탑재되고 있습니다. 최종 사용자는 정해진 작업을 위해 백그라운드에서 Mythos를 돌리는 목적 특화 인터페이스로 작업하고 의도된 산출물만 받습니다. 예컨대 제안 패치를 받되 익스플로잇을 요청할 방법은 없습니다. 오남용 방지 조치가 모델이 범위 안에 머무는지 확인합니다.
- **Claude Security 스캔이 이제 Mythos 5로 실행됩니다.** Claude Enterprise 대상 퍼블릭 베타이며, 관리자가 admin console에서 활성화하고, `claude.ai/security`에서 리포지토리를 선택합니다. 발견 사항은 CWE 분류, 신뢰도·심각도 등급, 제안 수정안과 함께 반환됩니다. 표준 토큰 사용량으로 과금되며 별도 애드온은 없습니다.
- **패치에는 사람이라는 관문이 남습니다.** 웹의 Claude Code를 열어 수정을 구현합니다. 인터랙티브 패치는 조직이 Claude Code에서 접근 권한을 가진 모델을 쓰며(Mythos 스캔이 다른 표면으로 Mythos 접근을 확장하지 않습니다), 모든 패치는 사람이 검토·승인해야 합니다.
- **Defender Advantage Fund(0xDAF):** 오픈소스 메인테이너를 돕는 조직에 3,500만 달러 상당의 Claude 크레딧. 실제 취약점 패치, 복제 가능한 스캔·패치 자동화, 공격의 한 부류 전체에 내성을 갖게 하는 접근에 초점을 둡니다. Glasswing 아래의 400만 달러 직접 기부와 Akrites·Gold Eagle 같은 협조적 노력 위에 쌓아 올린 것으로, 소수의 큰 파일럿 지원금으로 시작합니다.
- **Cyber Verification Program 확대:** 검증된 방어자는 이미 Opus와 Sonnet에서 완화된 안전장치를 받습니다. 앞으로 몇 주에 걸쳐 취약점 분류·검증 같은 방어 역량이 Mythos급 모델로 확대되고, Opus·Sonnet급에서는 차단이 줄어듭니다. 엄격한 보안 통제 요건을 충족하는 핵심 인프라 보호 주체를 대상으로 미국 정부 파트너와의 Glasswing 접근도 계속됩니다.

## 번들 리소스
- `skills/security-scan-triage/SKILL.md` — 활성화→스캔→분류→패치 워크플로, 사람 승인 관문, 접근 경로 선택법.
- `skills/security-scan-triage/references/access-paths.md` — 네 경로 상세와 Glasswing 배경, 선택 표.
- `skills/security-scan-triage/templates/finding-triage-report.md` — CWE·신뢰도·심각도·검증·결정·승인자를 축으로 한 항목별 분류 표와 상세 블록.
- `guides/defensive-capability-access.{en,ko,es,ja}.md` — 4개 언어 전체 해설.

## 출처
[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders) — 2026년 8월 21일.
