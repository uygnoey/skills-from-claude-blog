[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Comcast 와 Booz Allen 의 보안 팀이 Project Glasswing(핵심 인프라 방어자를 위한 Anthropic 의 제한
접근 프로그램)을 통해 Claude Mythos Preview 로 기존 스캐너가 놓친 취약점을 찾고, 검증하고, 고친
사례입니다. 특히 작은 약점들이 합쳐져 심각한 공격 경로가 되는 익스플로잇 체인에 초점을 둡니다.

## 언제 유용한가요
- 보안 팀이 대규모 소프트웨어 포트폴리오를 모델로 검토하려 할 때.
- 발견 건수가 검증·배정 속도를 앞지를 때.
- 단일 버그 스캐너가 놓치는 컴포넌트 간·언어 간 결함을 찾을 때.

## 핵심 포인트
- Comcast 는 업무상 핵심 시스템 258개(코드 약 1억 7천만 줄)를 평가했습니다. 모델은 각각은 올바르게
  보이는 여러 컴포넌트의 상호작용에서 생긴, 외부 공개 플랫폼의 치명적 인증 취약점을 찾았습니다.
  엔지니어가 실행 중인 애플리케이션에서 검증하고 근본 원인을 추적해 고쳤으며, 이전에 악용되지
  않았음을 확인했습니다.
- Comcast CISO Noopur Davis: 이제 병목은 발견이 아니라 쏟아지는 발견 건의 검증입니다.
- Booz Allen 은 부팅 시점 펌웨어 결함을 찾았습니다. 보호되지 않은 보안 키 때문에 공격자가 자기 키로
  바꿔치기하고 기기의 잠금·초기화 동작을 막을 수 있었습니다. 모델은 두 언어로 된 두 프로그램에
  걸쳐 문제를 추적했고, 수정안과 시스템 소유자용 증거 정리를 도왔습니다.
- 팀은 여전히 발견 건을 검증하고, 반복되는 패턴을 중복 제거하고, 소유자에게 배정합니다. Booz Allen
  분석가 한 명이 더 큰 팀으로 몇 달 걸렸을 포트폴리오 검토를 12일 만에 마쳤습니다.
- 판단은 사람이 내립니다. Anthropic 은 Cyber Verification Program(CVP)으로 접근을 넓힐 예정입니다.

## 번들 리소스
- Skill: `exploit-chain-validation` — 발견 이후 흐름(검증, 근본 원인, 악용 여부 확인, 수정, 중복
  제거, 배정)과 발견 건 증거 패킷 템플릿.

## 출처
- https://claude.com/resources/articles/how-comcast-booz-allen-use-claude-mythos-to-secure-their-codebases
