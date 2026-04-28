[English](./web-search-and-fetch.en.md) · **한국어** · [Español](./web-search-and-fetch.es.md) · [日本語](./web-search-and-fetch.ja.md)

## 개요
이 가이드는 Claude를 활용해 웹 검색을 활성화할 때(그리고 업데이트로 언급된 web fetch 기능까지) 어떤 식으로 적용할지의 관점을 정리합니다.

## 선택: search vs fetch
- **web search**: 여러 출처를 탐색해야 하고 citations가 필요한 경우.
- **web fetch**: 이미 URL을 알고 있고, Claude가 해당 페이지를 읽고 분석하면 되는 경우.

## 운영 관점
- 외부 요청으로 지연 시간이 변동될 수 있습니다.
- 핵심 주장에 대해 citations가 근거를 제공하는지 점검하세요.
- 조직의 allow/block 리스트를 사용한다면 허용/차단 도메인에서의 동작을 테스트하세요.

## 출처
https://claude.com/blog/web-search-api
