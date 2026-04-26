[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Making Claude a better electrical engineer

## 이 글이 뭔가요
이 글은 Anthropic이 Diode Computers와 협업하여 Zener 언어로 PCB 레퍼런스 디자인을 생성하는 Claude의 능력을 개선한 과정을 설명합니다.

## 언제 유용한가요
특정 도메인에서 모델 성능을 끌어올리기 위해 전문가와 협업하고, 벤치마크를 만들고, 실패 패턴을 반복적으로 개선하려는 경우에 유용합니다.

## 핵심 포인트
- 구체적인 에이전틱 작업과 도메인 기준의 성공/실패를 판정하는 그레이딩 하네스(테스트벤치)를 정의합니다.
- 전문가 피드백으로 대표 실패 모드를 파악하고 평가 기준을 다듬습니다.
- 부품의 정확한 일치 대신 ‘최소 커패시턴스’ 같은 요구사항 기반 체크를 선호합니다.
- 기준 모델 대비 블라인드 비교로 개선 효과를 검증합니다.

## 번들 리소스
- Skill: skills/domain-partnership-benchmarking/SKILL.md

## 출처
- https://claude.com/blog/making-claude-a-better-electrical-engineer
