[English](./dynamic-workflows.en.md) · [한국어](./dynamic-workflows.ko.md) · [Español](./dynamic-workflows.es.md) · **日本語**

# Claude Code の Dynamic Workflows: 効果的な使い方

## Dynamic Workflows とは？
Dynamic Workflows は Claude Code の機能で、Claude がオーケストレーションスクリプトを生成し、1 セッション内で数十〜数百のサブエージェントを並列に調整して、ユーザーに提示する前に作業を検証できます。

## 使いどころ（避けるべき場面）
向いている場面:
- 対象範囲が広い（多くのファイル/モジュール/未知の領域）
- 大規模コードベース全体の発見（discovery）やレビューが必要
- コミット前に計画を多角的にストレステストしたい

避ける（または小さく始める）場面:
- すでにスコープが明確で、1 回の集中作業で終わる
- トークンコストに敏感（通常より大きく増える可能性）

## 推奨設定
- 最良の体験のため **auto mode** を有効にします。
- まずは **小さくスコープしたタスク** で費用対効果の感覚をつかみましょう。

## 開始方法（2 つ）
1. Claude に直接ワークフロー作成を依頼します。
2. effort メニューから **ultracode**（effort xhigh）を有効にし、必要に応じて Claude が自動で使えるようにします。

## 実行中に期待できること
- ワークフローが初めてトリガーされる際、Claude Code が実行内容を表示し確認を求めます。
- 長時間（数時間〜数日）の実行を想定しています。
- 進捗は保存されるため、中断しても再開できます。

## 出典
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
