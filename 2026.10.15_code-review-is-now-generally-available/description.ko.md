[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
Code Review가 리서치 프리뷰를 벗어나 Claude Team·Enterprise 조직에 정식 출시(GA)되었다는 공지입니다.
프리뷰 이후 달라진 점은 세 가지입니다. 리뷰 속도, 더 날카로워진 발견 내용, 그리고 관리자가 리포지토리
단위로 고르는 리뷰 깊이입니다.

## 언제 유용한가요
- Team·Enterprise 조직에서 Code Review를 켤지, 어떤 리포지토리에 적용할지 결정할 때
- 프리뷰 시절 리뷰가 일상적인 변경에는 너무 느리거나 시끄럽게 느껴졌고, 모든 리포지토리에 같은 설정을
  쓰는 대신 깊이를 리포지토리별로 조정하고 싶을 때
- 에이전트를 활용한 개발로 PR 양이 사람의 리뷰 용량보다 빠르게 늘어났을 때

## 핵심 포인트
- Code Review는 리서치 프리뷰를 졸업해 Claude Team·Enterprise 플랜에서 정식 제공됩니다.
- 자격이 되는 Claude Enterprise 조직은 2027년 1월 15일까지 최소 $10,000의 Code Review 크레딧을 신청할
  수 있습니다. 크레딧은 신청 후 30일이 지나면 만료되며, 약관이 적용됩니다.
- 속도: 대부분의 리뷰가 프리뷰 대비 약 3배 빨라졌습니다(약 20분 → 6~10분).
- 품질: 중요한 버그를 더 많이 찾아내고, 문제·발생 조건·수정 방법을 몇 문장으로 명확하고 간결하게
  제시합니다.
- 유연성: 관리자가 리포지토리별로 Quick, Standard(기본값), Deep 중 하나를 고릅니다. 일상적인 코드베이스는
  빠른 패스로, 가장 중요한 코드베이스는 깊은 리뷰로 처리합니다. 어떤 수준이든 품질 높은 리뷰를 제공합니다.
- Anthropic도 자사 PR에 Code Review를 돌리고 있으며, 이를 통해 리뷰가 자사 엔지니어의 속도를 어디서
  떨어뜨리는지 파악합니다.
- 관리자 설정: Claude Code 설정에서 Code Review를 활성화하고, GitHub App을 설치하고, 리뷰할 리포지토리를
  선택합니다. 개발자는 별도 설정이 필요 없습니다. 새 PR에서 리뷰가 자동으로 실행됩니다.

## 번들 리소스
- Skill: `code-review-rollout` — 조직에 Code Review를 도입하고 리포지토리별 리뷰 깊이를 배정하는 방법.
  세 가지 깊이 수준과 크레딧 프로그램 레퍼런스 포함.

## 출처
- https://claude.com/resources/articles/code-review-is-now-generally-available
