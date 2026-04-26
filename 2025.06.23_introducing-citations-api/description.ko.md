[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Anthropic API의 Citations 기능을 소개합니다. Claude가 사용자가 제공한 문서에 근거해 답변을 만들고, 사용한 구절(문장/패시지)을 정확히 인용해 근거를 남길 수 있습니다.

## 언제 유용한가요
요약, 질의응답, 고객지원 등에서 결과의 검증 가능성이 중요하고, 각 주장(claim)이 출처 텍스트로 추적 가능해야 할 때 유용합니다.

## 핵심 포인트
- Citations는 답변의 주장들을 소스 문서의 특정 문장/구절과 연결합니다.
- 입력 소스는 PDF 또는 일반 텍스트이며, 개발자가 미리 청킹한 텍스트를 제공할 수도 있습니다.
- Citations는 Anthropic API와 Google Cloud Vertex AI에서 사용 가능하며, 업데이트로 Amazon Bedrock 지원도 언급됩니다.

## 번들 리소스
- Skill: 인용 기반의 “근거 있는 답변” 경험을 만들기 위한 재사용 워크플로.
- Guide: 구현 체크리스트 및 제품 관점(UX, 가격/토큰, 평가) 정리.

## 출처
https://claude.com/blog/introducing-citations-api
