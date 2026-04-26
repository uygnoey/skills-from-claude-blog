[English](./getting-started-with-claude-code.en.md) · [한국어](./getting-started-with-claude-code.ko.md) · [Español](./getting-started-with-claude-code.es.md) · **日本語**

# Claude Code の始め方

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding)（2025-10-30 公開）から抽出した短い導入ガイドです。プロジェクトに Claude Code を導入する初日のチェックリストとして使います。

## 1. ワークフロー適合の確認

インストール前に、委任しようとしているタスクが適切か確認します。

- 複数ファイルにまたがるか
- コマンド実行と結果解釈が必要か
- 量は多いが要件が明確（テスト補完、ドキュメント、定型リファクタリング）

概念的な質問や、問題のスコープがまだ固まっていない段階では Claude.ai を使い続ける方が無難です。

## 2. Claude Code をインストール

```
npm install -g @anthropic-ai/claude-code
```

## 3. プロジェクトで起動

プロジェクトルートに移動して:

```
claude
```

Claude Code は設定ファイル・テスト・インポートを読んで内部マップを作成してから作業を始めます。

## 4. 推奨される 3 つの初回プロンプトを試す

順番に:

```
Explain the structure of this codebase and how the main components interact
```

```
Review the authentication module for potential security issues
```

```
Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching
```

1 つ目は Claude Code がプロジェクトをどう読むかを掴むため。2 つ目は分析能力、3 つ目は複数ファイルにまたがる実装能力を試します。

## 5. 承認・修正・拒否

Claude Code はファイル変更の前に承認を求め、計画された差分を表示します。理解できるものだけ承認し、違和感があれば拒否や修正を依頼してください。

## 6. CLAUDE.md にプロジェクト知識を保持

プロジェクトルートに `CLAUDE.md` を置き、コーディング標準・アーキテクチャ決定・プロジェクト固有要件を記録します。Claude Code はセッションごとにこのファイルを読みます。

## 7. 即効性のある領域に拡張

初回セッションの後、記事が挙げるカテゴリで意図的な使い方を 3 件計画します。

- 未カバー経路のテスト自動化
- レガシーシステムのドキュメント生成
- 技術的負債の定型リファクタリング
- 要件が明確な機能実装

その経験を踏まえて、チーム内で Claude Code がどこで信頼を得られるかを判断します。

## 8. オプション: MCP サーバーの接続

イシュートラッカー・デザインシステム・社内ドキュメントなどリポジトリ外のツールが必要なら、MCP サーバーを接続して Claude Code が計画にそのコンテキストを取り込めるようにします。

## 出典

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding)（公開日：2025-10-30）。
