[English](./citations-api-implementation.en.md) · [한국어](./citations-api-implementation.ko.md) · [Español](./citations-api-implementation.es.md) · **日本語**

# Citations API 実装チェックリスト

## 構築
- 対象タスク（要約、Q&A、サポート）と、どこまで引用必須かを決める。
- ソース文書（PDF/テキスト）を用意し、分割（チャンク）方針を選ぶ。
- 引用の表示方法（インライン、脚注、原文へのジャンプ）を設計する。

## 評価
- 引用の再現率（recall）と適合率（precision）を測る。
- 根拠がない質問に対する「ソースに見当たらない」の割合を追跡する。

## 出典
- https://claude.com/blog/introducing-citations-api
