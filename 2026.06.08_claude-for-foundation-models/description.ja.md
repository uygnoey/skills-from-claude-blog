[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# AppleのFoundation ModelsフレームワークでClaudeを使う

## この記事について
Anthropicは、AppleのFoundation ModelsフレームワークをClaudeに接続する新しいSwiftパッケージを紹介しています。オンデバイスモデルで簡単な処理を行い、より複雑なリクエストはClaudeへ引き継ぐパターンを説明します。

## どんなときに役立つか
- 高速でプライベートなオンデバイス要約/抽出を維持しつつ、複数ステップの推論が必要な場面で大規模モデルへ自然に切り替えたいとき
- Appleのguided generationで得られる型付きSwift出力を、Claude API呼び出しのクリーンで構造化された入力として使いたいとき

## 主なポイント
- オンデバイスモデル（要約、抽出など）とClaude（複数ステップの推論、コード生成、ウェブ検索、データ分析のためのコード実行など）を、タスクの複雑さで使い分けます。
- Claudeの応答を同じUIビューにストリーミングして、ユーザー体験を一続きに保ちます。
- guided generationによる型付き出力は、Claude呼び出し時の生のユーザーテキスト依存を減らします。

## 同梱リソース
- Apple Foundation Modelsアプリ向けの「まずオンデバイス、次にClaude」引き継ぎパターンをまとめた再利用可能なAgent Skill（`skills/foundation-models-handoff/SKILL.md`）。
- 配布用にskillを同梱するプラグインのひな形（`plugin/.claude-plugin/plugin.json`）。

## 出典
- https://claude.com/blog/claude-for-foundation-models
