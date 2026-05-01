[English](./shipping-app-with-claude-code.en.md) · **한국어** · [Español](./shipping-app-with-claude-code.es.md) · [日本語](./shipping-app-with-claude-code.ja.md)

# Claude Code로 실제 앱 출시하기(사례 기반 체크리스트)

출처: https://claude.com/blog/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks

## 이 가이드의 범위
원문 사례를 바탕으로, 프로토타입 → 서브에이전트로 역할 분리 → 프로덕션 안정화 → App Store 출시 → 지표 기반 개선 흐름을 체크리스트로 정리합니다.

## 체크리스트
1. **한 문장 목표**를 쓰고 제약(플랫폼, 디바이스, 일정)을 정리합니다.
2. **빠른 프로토타입**으로 버려도 되는 end-to-end 슬라이스를 먼저 만듭니다.
3. **전문 역할 배정**(아키텍처, 구현, 리뷰, 플랫폼 특화)을 합니다.
4. **프로덕션 안정화**(크래시 리포팅, 분석, 스크린샷 기반 디버깅)를 진행합니다.
5. **런치 준비**(제출 자료, 스토어 카피, 마케팅 초안)를 합니다.
6. **측정과 반복 개선**(퍼널, 리텐션, DAU/MAU)을 합니다.

## 포함된 템플릿
- 프로젝트 브리프: ../skills/solo-to-ios-shipping-workflow/templates/project-brief.md
- 서브에이전트 역할 브리프: ../skills/solo-to-ios-shipping-workflow/templates/subagent-role-brief.md
- Day Zero Questionnaire: ../skills/solo-to-ios-shipping-workflow/templates/day-zero-questionnaire.md
