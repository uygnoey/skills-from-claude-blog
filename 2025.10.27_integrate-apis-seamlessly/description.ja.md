[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# APIをシームレスに統合する方法

## この記事について

API 統合作業を「障害が出てからの後追いデバッグ」から「事前の体系的な設計」へ移すための実践ガイドです。原文は、多くのチームがレート制限・トークン失効・スキーマ変更・Webhook 順序などの失敗モードを本番でようやく発見し、後付けでエラーハンドリングを差し込んでいると指摘します。代替として、Claude.ai で認証・レート制限・エッジケースを事前に分析し、Claude Code で型付きクライアント・OAuth/JWT/キーローテーションのフロー・契約/リフレッシュテストをコードベース全体に生成する流れを示します。

## どんなときに役立つか

- 新しいサードパーティ API を導入する前に、コードを書く前段階で失敗モードのチェックリストが欲しいとき
- 既存統合が 401/429/タイムアウトの障害対応に追われており、体系的な改善計画が必要なとき
- Webhook と polling のどちらを採るか、あるいはスキーマ変更に耐えるバージョン付きクライアントを設計するとき
- チームでの Claude.ai（計画）と Claude Code（実装・テスト・PR）の使い分けを標準化したいとき

## 主なポイント

- Claude.ai は計画に: API ドキュメントを貼り付け、「発生確率順の統合リスク」を要求 → レート制限の閾値、必須ヘッダー、フィールドの nullability、冪等性、429 への jitter 付きバックオフなど具体項目を取得
- Claude Code は実装に: `npm install -g @anthropic-ai/claude-code` → `claude` 起動 → OAuth2 自動トークン更新、JWT 検証、モニタリング付き API キーローテーション、契約/リフレッシュテスト生成を依頼
- スキーマ変更はアダプタ層とバージョン付きクライアントで吸収し、スキーマ検証で破壊的変更を早期検知
- Webhook と polling はレイテンシ・データ量・インフラに応じて選択。ハイブリッドも有効
- 出荷も Claude Code で: `> Commit these API changes and open a PR` の一行でコミットメッセージと PR 説明を生成

## 同梱リソース

- [skills/api-integration-resilience-playbook/SKILL.md](./skills/api-integration-resilience-playbook/SKILL.md): 計画＋実装のプレイブックとプロンプト
- [templates/risk-discovery-prompt.md](./skills/api-integration-resilience-playbook/templates/risk-discovery-prompt.md): 失敗モードのランキング作成用プロンプト
- [templates/auth-implementation-prompt.md](./skills/api-integration-resilience-playbook/templates/auth-implementation-prompt.md): OAuth2 / JWT / キーローテーション用プロンプト
- [references/failure-mode-catalog.md](./skills/api-integration-resilience-playbook/references/failure-mode-catalog.md): 原文に挙げられた失敗モードのカタログ
- [examples/example-prompts.md](./skills/api-integration-resilience-playbook/examples/example-prompts.md): 原文の Claude.ai / Claude Code プロンプトの原文ママ
- [guides/integration-planning-workflow.ja.md](./guides/integration-planning-workflow.ja.md) (+ en/ko/es): ステップバイステップの計画ワークフロー

## 出典

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly)（公開日：2025-10-27）より抽出。
