[English](./foundation-models-handoff.en.md) · [한국어](./foundation-models-handoff.ko.md) · [Español](./foundation-models-handoff.es.md) · **日本語**

# Apple Foundation Models → Claude のハンドオフ設計

このガイドは、公式ブログ記事で述べられている統合アプローチを、再利用できる設計チェックリストとして整理したものです。

## 記事が説明していること
- SwiftからAppleのFoundation Modelsフレームワークを使い、要約や抽出などのオンデバイス処理を行います。
- ユーザーの要求がより複雑な作業を必要とする場合、Claudeを呼び出して複数ステップの推論、コード生成、ウェブ検索、データ分析のためのコード実行などを行います。
- Claudeの応答を同じUIビューにストリーミングして、体験を一続きに保ちます。

## 推奨ワークフロー構成
1. **オンデバイス段階（高速・ローカル）**
   - 何を抽出/要約するかを定義します。
   - guided generationで型付きSwift値を生成することを優先します。
2. **Claudeへのエスカレーション（複雑）**
   - 型付き値をClaudeのクリーンな入力として利用します。
   - Claudeに複数ステップの推論を依頼し、最終回答を生成します。
3. **単一のUX**
   - 同じビューにClaudeの出力をストリーミングし、連続した対話として提示します。

## 記事の例
- ジャーナリングアプリ：オンデバイスの日次プロンプト → Claudeが数か月分の記録から共通のスレッドを見つける
- 学習アプリ：オンデバイスの定義 → Claudeがより深い概念的なフォローアップに回答

## 出典
- https://claude.com/blog/claude-for-foundation-models
