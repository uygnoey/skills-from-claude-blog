[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

## 이 글이 뭔가요

이 글은 Claude Platform의 web search / web fetch 도구가 검색·가져오기 결과를 컨텍스트 윈도우에 넣기 전에, 코드 실행을 통해 관련 내용만 남기고 나머지를 자동으로 걸러내는(동적 필터링) 업데이트를 소개합니다.

## 언제 유용한가요

웹 검색 과정에서 불필요한 HTML/긴 페이지가 많이 섞여 정확도가 떨어지거나 토큰 사용량이 커지는 경우에 유용합니다. 특히 기술 문서 탐색이나 인용·출처 검증처럼 “필요한 부분만” 남겨야 하는 작업에 적합합니다.

## 핵심 포인트

- 웹 검색은 여러 사이트의 HTML을 통째로 가져와 추론하는 경우가 많아 토큰 소모가 큰 작업입니다.
- 동적 필터링에서는 web search / web fetch 도구가 결과를 후처리하기 위해 코드를 작성·실행하고, 컨텍스트에 넣기 전에 관련 부분만 남깁니다.
- BrowseComp에서 정확도가 Sonnet 4.6은 33.3% → 46.6%, Opus 4.6은 45.3% → 61.6%로 향상되었습니다.
- DeepsearchQA에서 F1 점수가 Sonnet 4.6은 52.6% → 59.4%, Opus 4.6은 69.8% → 77.3%로 향상되었습니다.
- 두 벤치마크 평균으로 성능이 11% 개선되었고, 입력 토큰은 24% 감소했습니다.
- Claude API에서 Sonnet 4.6 및 Opus 4.6과 함께 새 버전 도구를 사용할 때 동적 필터링이 기본 활성화됩니다.

## 번들 리소스

- Skill: web_search + web_fetch를 효율적으로 쓰고 결과/인용을 검증하는 재사용 워크플로.
- 원문에 포함된 API 요청 JSON 예시.

## 출처

- https://claude.com/blog/improved-web-search-with-dynamic-filtering
