[English](./hackathon-winner-patterns.en.md) · **한국어** · [Español](./hackathon-winner-patterns.es.md) · [日本語](./hackathon-winner-patterns.ja.md)

## 이 가이드는 무엇인가요
이 가이드는 Claude의 “Built with Opus 4.7” 해커톤 수상자들이 공통으로 언급한 빌드·반복 개선 패턴을 간단히 정리합니다.

## 언제 유용한가요
기획, 병렬화, 평가, 반복 개선을 위한 가벼운 플레이북이 필요할 때 사용하세요.

## 핵심 포인트
- 구현 전에 스펙과 계획을 먼저 세웁니다.
- 책임을 분리해 컨텍스트를 깔끔하게 유지(세션 분리)하거나, 디버깅 시 여러 에이전트를 병렬로 돌립니다.
- 다음 기능을 만들기 전에 Claude에게 현재 결과물을 감사(audit)해 달라고 요청합니다.
- 가능하면 평가(evals)를 먼저 만들고, 도메인 특화 레퍼런스 데이터를 활용합니다.

## 출처
- https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon
