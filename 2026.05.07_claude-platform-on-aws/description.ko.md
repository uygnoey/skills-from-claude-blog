[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 **Claude Platform on AWS**를 소개합니다. Anthropic의 1st-party Claude Platform을 AWS의 진입점(IAM, 결제, 감사 로그)을 통해 이용할 수 있게 하는 방식입니다.

## 언제 유용한가요
- 조직이 조달/과금/접근제어/감사를 AWS 흐름으로 통일하고 싶을 때
- 별도의 Anthropic 자격증명을 관리하지 않고 Anthropic의 네이티브 Claude Platform 경험을 쓰고 싶을 때

## 핵심 포인트
- 기존 **AWS 자격증명**과 **IAM 정책**으로 Claude Platform에 접근합니다.
- 사용량은 **AWS 통합 결제**로 청구됩니다.
- 활동 로그는 **AWS CloudTrail**에 남습니다.
- 중요한 구분: 이 방식에서는 **고객 데이터가 AWS 경계 밖에서 Anthropic에 의해 처리**됩니다.

## 번들 리소스
- “Claude Platform on AWS”와 “Claude on Amazon Bedrock”의 차이를 바탕으로 접근제어/로깅/도입 고려사항을 정리하는 스킬

## 출처
- https://claude.com/blog/claude-platform-on-aws
