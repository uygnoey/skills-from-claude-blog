[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요
이 글은 Anthropic Messages API에서 사용할 수 있는 Web Search 도구를 소개하며, Claude가 웹 검색을 수행하고 출처(citations)와 함께 답변을 반환할 수 있음을 설명합니다.

## 언제 유용한가요
모델 학습 시점 이후의 최신 정보가 필요하거나, 근거를 확인할 수 있는 답변이 필요한 애플리케이션(예: 시장/규제 업데이트, 최신 문서, 시사 이슈)에 유용합니다.

## 핵심 포인트
- Messages API 요청에서 web search 도구를 활성화합니다.
- Claude가 웹 검색 필요 여부를 판단하고, 타깃 쿼리를 생성하며, 필요 시 여러 번의 검색을 수행할 수 있습니다(max_uses로 제어).
- 응답에는 검색된 자료에 대한 citations가 포함됩니다.
- 관리자는 조직 단위로 도메인 allow/block 리스트로 사용을 제어할 수 있습니다.
- 업데이트 섹션에서 특정 URL을 가져와 분석하는 Web Fetch 기능도 언급합니다.

## 번들 리소스
Skill: api-web-search-with-citations. Guide: web-search-and-fetch.

## 출처
https://claude.com/blog/web-search-api
