[English](./web-search-and-fetch.en.md) · [한국어](./web-search-and-fetch.ko.md) · [Español](./web-search-and-fetch.es.md) · **日本語**

## 概要
このガイドでは、Claude で web search（およびアップデートで言及されている web fetch）を有効にする判断と適用観点をまとめます。

## 判断: search vs fetch
- **web search**: 複数ソースの探索が必要で、citations が欲しい場合。
- **web fetch**: 既に URL があり、そのページを Claude に読ませて解析したい場合。

## 運用上の注意
- 外部リクエストによりレイテンシが変動します。
- 重要な主張が citations により裏付けられているか確認します。
- allow/block リスト運用がある場合、許可・拒否ドメインで挙動をテストします。

## 出典
https://claude.com/blog/web-search-api
