[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# エージェンティックコーディング入門

## この記事について

エージェンティックコーディングの入門記事です。次の行を予測する AI ツールから、上位ゴールを受け取り複数ステップを計画し、コードベース全体のファイルを変更し、テストを実行し完了まで反復する AI システムへの移行を解説します。オートコンプリート → チャットアシスタント → エージェンティックシステムという進化を辿り、Claude Code がプロジェクトコンテキストをどう読み取り、多ファイル変更をどう調整し、明示的な権限モデルをどう守るかを説明します。Rakuten による 7 時間の自律的 vLLM 実装が看板の実例として取り上げられています。

## どんなときに役立つか

- 「エージェンティックコーディングはオートコンプリートやチャット型アシスタントと何が違うのか」をチームへ説明したいとき
- Claude Code に最初に委任するワークフロー（テスト自動化、ドキュメント生成、リファクタリング、要件が明確な機能実装）を見極めたいとき
- Rakuten 事例の具体数値（機能リリース 79% 短縮、99.9% 精度、5 倍の並列処理能力）を引用したいとき
- インストールコマンドと記事推奨の 3 つの「最初のタスク」プロンプトを素早く取り出したいとき

## 主なポイント

- エージェンティックコーディング = 自律性 + スコープ。ツールがコードベース全体を読み、依存関係を辿り、コマンドを実行し、反復する。オートコンプリートはコンテキスト窓が狭く、チャットは反復可能だが手動、エージェントはオーケストレーションも自分で担う。
- 2 フェーズ: コンテキスト収集と計画（設定・テスト・インポート・依存関係マップ → 適応的プラン）と、実装と調整（複数ファイル編集、テストでの検証）。
- Claude Code のインストール: `npm install -g @anthropic-ai/claude-code`、プロジェクトディレクトリで `claude` を起動。
- 権限モデル: Claude Code はファイル変更前に承認を求め、計画された差分を表示する。承認・修正・拒否が可能。
- 既存ツール（npm、Jest、pytest、Git、dev サーバー）と統合され、MCP サーバー接続で追加ツールも活用可能。
- Rakuten 事例: vLLM（12.5M 行、Python/C++/CUDA）にアクティベーションベクトル抽出メソッドを 7 時間の自律作業で実装。数値精度 99.9%、機能リリース 79% 短縮（24 日 → 5 日）、並列タスク処理 5 倍。Kenta Naruse のコメント: "I didn't write any code during those seven hours, I just provided occasional guidance." Yusuke Kaji のコメント: "You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."
- 推奨される最初のプロンプト: "Explain the structure of this codebase and how the main components interact"、"Review the authentication module for potential security issues"、"Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching"。
- "Start slow, then expand"。即効性のある領域: テスト自動化、ドキュメント生成、定型リファクタリング、要件明確な機能実装。
- Claude Code は CLAUDE.md ファイルにコーディング標準・アーキテクチャ決定・プロジェクト固有要件を保存し、セッションをまたいで一貫性を保つ。

## 同梱リソース

- [skills/agentic-coding-foundations/SKILL.md](./skills/agentic-coding-foundations/SKILL.md): Claude Code を呼び出すべき場面、2 フェーズワークフロー、インストール／起動コマンド、オンボーディングプロンプト
- [references/evolution-of-ai-coding.md](./skills/agentic-coding-foundations/references/evolution-of-ai-coding.md): オートコンプリート → チャット → エージェンティックの比較
- [examples/first-prompts.md](./skills/agentic-coding-foundations/examples/first-prompts.md): 推奨される 3 つのオンボーディングプロンプトと Rakuten 事例のまとめ
- [guides/getting-started-with-claude-code.ja.md](./guides/getting-started-with-claude-code.ja.md) (+ en/ko/es): ステップバイステップの導入ガイド

## 出典

[Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding)（公開日：2025-10-30）より抽出。
