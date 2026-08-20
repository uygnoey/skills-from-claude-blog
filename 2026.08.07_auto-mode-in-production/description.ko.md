[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Claude Code의 **auto mode**를 프로덕션에서 일상 기본값으로 운영하는 세 고객 사례입니다. **Nuro**, **Gusto**, **Garner Health**. auto mode는 명령마다 승인을 요구하는 대신, 각 동작을 평가해 잠재적으로 유해한 것을 차단하는 분류기(classifier)를 사용합니다. 원문은 이를 에이전틱 코딩의 속도 대 안전 트레이드오프에 대한 해법으로 제시합니다. 모든 명령을 검토하면 사람이 루프 안에 남지만, 세션이 몇 시간씩 이어지거나 병렬로 늘어나면 그 감독이 병목이 됩니다. 반대로 권한 검사를 아예 건너뛰면 프롬프트 인젝션, 범위 이탈, 프로덕션 리소스 삭제가 그대로 통과합니다.

전체 Claude Code 사용 기준으로, Claude는 이전 기본값 대비 중단 사이 **9배 더 오래** 작업합니다.

## 언제 유용한가요
- auto mode를 팀·전사 기본값으로 삼을지 판단하면서, 기능 설명이 아니라 구체적인 운영 패턴이 필요할 때.
- auto mode를 둘러싸는 가드레일(deny 규칙, 분류기 튜닝, MCP 프록시, 텔레메트리)을 설계할 때.
- 실무자들이 의도적으로 auto mode에서 *빠져나오는* 지점을 알고 싶을 때.
- 장시간·야간 에이전트를 만들면서 무인 실행에 실제로 맞는 작업 형태를 찾을 때.

## 핵심 포인트
- **auto mode는 가드레일을 대체하지 않고 그 안에서 동작합니다.** Nuro 엔지니어들은 재귀 삭제 같은 가장 위험한 명령을 설정에서 아예 deny로 막고, 분류기는 그 한계 안에서 판단합니다. Gusto는 MCP 트래픽을 도구 가드와 프롬프트 검사를 갖춘 거버넌스 프록시 계층으로 라우팅해, auto mode가 판단하기 전에 에이전트가 이미 좁게 제한된 권한으로 동작하게 합니다.
- **핵심 이득은 단계별 속도가 아니라 무인 지속 시간입니다.** Nuro는 자율주행 스택의 평가 지표를 개선해 나가는 야간 리서치 에이전트를 돌립니다. 한 엔지니어는 밤 10시에 에이전트를 시작해 아침에 PR 3개를 받았습니다. 이 패턴은 에이전트가 스스로 반복 개선할 수 있는 명확한 평가 신호가 있는 모든 작업으로 일반화되며, Nuro의 다른 팀은 특정 바이너리의 메모리 사용량을 줄이는 데 활용했습니다.
- **짧은 세션에도 이득이 있습니다.** Gusto의 한 클라우드 엔지니어는 20분 단위의 짧은 작업(엔드포인트 조사, 로그 감사, 커넥터 관리, 여러 MCP 서버에 걸친 문서 인제스트)을 수행하며, 더 긴 실행이 아니라 프롬프트 인젝션 보호와 의도 일치 확인 때문에 bypass permissions 대신 auto mode를 선택했습니다.
- **분류기는 실제로 일을 하고 있습니다.** Gusto 자체 분석에서 2026년 5월 중순 이후 세션 트랜스크립트의 약 10%에 auto mode 차단이 포함됐습니다. 한 엔지니어는 12월 이후 2,425개 세션을 auto mode 기본으로 실행했습니다.
- **실무자들은 여전히 의도적으로 빠져나옵니다.** Nuro의 Kai는 Claude Code가 자기 대신 PR을 리뷰할 때 인터랙티브 모드로 돌아갑니다. Gusto의 Chad는 Terraform, AWS, 라이브 API에 대한 직접 POST 호출을 다룰 때 accept edits로 전환합니다. "결국 무슨 일이 일어나든 책임은 여전히 본인에게 있다"는 것입니다.
- **튜닝은 최소한이지만 요점이 분명합니다.** Garner Health의 유일한 조정은 Nuro와 같습니다. Slack 메시지나 이메일 발송처럼 다른 사람과 소통하는 동작은 auto mode가 승인하지 않도록 설정했습니다.
- **auto mode가 표준화된 SDLC의 전제 조건이 되기도 합니다.** Garner Health는 전 직원 550명에게 Claude Code를 배포하고 Salesforce, Zendesk, Snowflake에 연결했으며, 표준 스킬 플러그인으로 개발 수명주기를 운영합니다. 컨텍스트 탐색 → 컨텍스트 파일을 저장소에 커밋 → 스스로의 가정을 압박 검증하는 "antagonistic research" 수행 → 구현으로 진행하고, 스스로 찾을 수 없는 컨텍스트가 필요할 때만 사람을 부릅니다. 리서치 비중이 큰 단계들은 auto mode 이전에는 불가능했습니다.
- **텔레메트리가 이를 가능하게 하는 통제 수단입니다.** Garner의 조언은 워크플로와 텔레메트리를 먼저 구축하라는 것입니다. "모두에게 각자 워크플로를 만들라고 하면서 텔레메트리가 없다면 그건 매우 위험할 것입니다."

## 번들 리소스
- `skills/auto-mode-production-practices/SKILL.md` — auto mode를 일상 기본값으로 운영하는 패턴.
- `skills/auto-mode-production-practices/references/team-practices.md` — Nuro, Gusto, Garner Health가 각각 무엇을 어떻게 설정했고 그 이유는 무엇인지.
- `skills/auto-mode-production-practices/references/unattended-task-patterns.md` — 야간 무인 실행에 맞는 작업 형태와 그렇지 않은 형태.
- `skills/auto-mode-production-practices/templates/team-auto-mode-policy.md` — 가드레일, 예외, 텔레메트리를 담은 팀 정책 양식.
- `guides/auto-mode-in-production-patterns.{en,ko,es,ja}.md` — 세 사례와 공통 패턴을 담은 4개 언어 가이드.

## 출처
- https://claude.com/blog/auto-mode-in-production
