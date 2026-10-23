[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Anthropic이 2026년 10월 23일에 Claude Duet의 보호 방식을 설명한 글입니다. Claude Duet은 클라우드 컴퓨터에서
계속 실행되며 사용자가 연결한 앱을 쓰는 리서치 프리뷰 에이전트입니다. 글은 세 원칙(정보를 신중하게 다루기,
사용자의 통제 유지, 자격증명을 에이전트에게서 떼어 놓기)을 중심으로 구성됩니다.

## 언제 유용한가요
- 사용자를 대신해 메시지 전송·결제·삭제·로그인을 하는 에이전트를 설계하거나 감사할 때.
- 프롬프트 주입과 과잉 행동까지 다루는 평가·레드팀 계획을 세울 때.
- 위임형 에이전트가 비밀번호와 토큰을 모델에서 어떻게 떼어 놓는지 이해관계자에게 설명할 때.

## 핵심 포인트
- 민감한 행동은 행동·대상·내용을 보여 주고 승인을 기다립니다. 모델 바깥의 의도 검사(Claude Code auto mode
  분류기 확장)가 페이지에 숨은 지시에 흔들리지 않습니다. 증권 거래, 계좌 간 자금 이동, 타인 계정 접근은
  승인이 있어도 금지입니다. 구매는 Link(Stripe)의 일회용 카드를 씁니다.
- 별도 분류기가 나가는 메시지를 검사합니다: 자격증명·전체 카드/계좌 번호·신분증 번호는 절대 공유 금지,
  그 밖의 개인 정보는 동의 필요(사용자의 요청이 곧 동의). 차단된 메시지는 고쳐 써서 승인을 받을 수 있습니다.
- 작업 목록으로 진행 상황을 보고 도중에 방향을 바꿀 수 있으며, 기록과 메모리는 삭제·초기화 전까지 유지됩니다.
- 비밀번호는 앱 폼으로 입력되고 일회용 키로 암호화되어 브라우저 머신이 입력합니다. 토큰은 플레이스홀더로
  두고 외부 프록시가 채웁니다. 브라우저는 별도 VM에서 고정 명령으로만 조작합니다. 고유 User-Agent와 공개
  IP를 씁니다.
- 테스트: 정상·주입·과잉 유도 변형 작업, 레드팀, 시스템 전체 위협 모델, 외부 침투 테스트, HackerOne 버그
  바운티.

## 번들 리소스
- 스킬: `delegated-agent-safeguards` (`references/information-sharing-tiers.md`,
  `references/credential-and-browser-isolation.md`, `templates/approval-request.md`,
  `examples/evaluation-plan.md`).
- 가이드: `guides/delegated-agent-security-architecture` (4개 언어).

## 출처
- https://claude.com/resources/articles/claude-duet-safety-privacy-and-security
