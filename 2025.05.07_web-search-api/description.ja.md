[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Anthropic Messages API の Web Search ツールを紹介し、Claude がウェブ検索を行って出典（citations）付きで回答できることを説明します。

## どんなときに役立つか
学習カットオフ以降の最新情報や、根拠を確認できる回答が必要な場合（市場・規制の更新、最新ドキュメント、時事情報など）に役立ちます。

## 主なポイント
- Messages API リクエストで web search ツールを有効化します。
- Claude が検索の必要性を判断し、狙いを絞ったクエリを生成し、必要に応じて複数回の検索を行います（max_uses で制御）。
- 回答には取得したソースへの citations が含まれます。
- 管理者は組織単位でドメインの allow/block リストにより利用を管理できます。
- アップデート欄で、特定 URL を取得して解析する Web Fetch 機能にも触れています。

## 同梱リソース
Skill: api-web-search-with-citations. Guide: web-search-and-fetch.

## 出典
https://claude.com/blog/web-search-api
