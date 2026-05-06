[English](./managed-agents-upgrades.en.md) · **한국어** · [Español](./managed-agents-upgrades.es.md) · [日本語](./managed-agents-upgrades.ja.md)

# Managed Agents 업데이트: dreaming, outcomes, 오케스트레이션, 웹훅

## 이 가이드는 뭔가요
원문에서 소개한 네 가지 기능이 서로 어떻게 맞물리는지 간단히 정리한 가이드입니다.

## 언제 유용한가요
Managed Agent에 dreaming, outcomes, 멀티 에이전트 오케스트레이션 도입 여부를 판단할 때 유용합니다.

## 핵심 포인트
- **메모리 vs dreaming**: 메모리는 작업 중 학습을 저장하고, dreaming은 세션 사이에 메모리를 정교화합니다.
- **Outcomes**: 루브릭과 그레이더 조합으로, 그레이더가 별도 컨텍스트에서 결과를 평가합니다.
- **멀티 에이전트 오케스트레이션**: 리드 에이전트가 전문 에이전트에게 병렬로 작업을 위임하고 공유 파일시스템에서 협업합니다.
- **웹훅**: outcomes 평가 완료 시점을 알립니다.

## 출처
- https://claude.com/blog/new-in-claude-managed-agents
