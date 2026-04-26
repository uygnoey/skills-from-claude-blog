[English](./integration-planning-workflow.en.md) · [한국어](./integration-planning-workflow.ko.md) · [Español](./integration-planning-workflow.es.md) · **日本語**

# 統合計画ワークフロー

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly)（2025-10-27 公開）から抽出したステップバイステップのワークフローです。チームが Claude.ai と Claude Code を用いてサードパーティ API 統合を計画・実装・検証・出荷する手順を標準化するために使用します。

## 1. Claude.ai で API をトリアージ

- Claude.ai を開き、ドキュメント URL、OpenAPI 仕様、または関連する抜粋を貼り付けます。
- "Integration risks ranked by likelihood" をリクエスト。一般論ではなくベンダー固有の具体項目のみ受け取ります — レート制限の閾値、カウント方法（ユーザー別 / IP 別 / API キー別）、必須ヘッダー、冪等性キー、Webhook 配信保証、フィールドの nullability。
- 不明瞭な失敗モードはフォローアップで掘り下げます（例: "Why might OAuth tokens expire during multi-step checkout flows?"、"Here's a Stripe webhook signature error. What validation steps am I missing?"）。
- 出力: 具体的な失敗モードのリストと、認証戦略の決定（資格情報の保管先、更新頻度、ローテーション計画）。

## 2. Webhook と polling の選択

- 具体的なユースケースで比較します（例: "webhook vs polling for real-time inventory updates"）。
- レイテンシ・データ量・インフラ制約に基づいて選択。ハイブリッド（リアルタイムは Webhook、整合性検証は polling）も有効です。
- 決定とその根拠となった制約を記録します。

## 3. Claude Code で実装

- インストール: `npm install -g @anthropic-ai/claude-code`。プロジェクトルートで `claude` を起動。
- Claude Code に既存のプロジェクト規約に合わせた型付きクライアント生成を依頼します。
- 選択した認証フローを実装:
  - "Build OAuth2 flow for Google Calendar with automatic token refresh"
  - "Create rotating API key system for Twilio with monitoring"
  - "Implement JWT validation for microservices"
- レート制限ハンドリングを追加: 429 に対する jitter 付き指数バックオフ、必要に応じてリクエストキューイング、連鎖障害が起こりやすい呼び出しにはサーキットブレーカー。
- レスポンス境界でスキーマ検証を組み込み、バージョン付きクライアントにはアダプタ層を追加します。

## 4. 検証

Claude Code にテスト生成と実行を依頼:

- "Create tests that reproduce this rate limit scenario"
- "Generate contract tests for schema validation"
- "Run tests for authentication refresh during long operations"

ステップ 1 で洗い出した失敗モードを統合がすべて処理することがテストで確認できるまで反復します。

## 5. 出荷

Claude Code 内で実行:

```
> Commit these API changes and open a PR
```

Claude Code が説明的なコミットメッセージと、実装とテストカバレッジをリンクする PR 説明を生成します。

## 出典

[How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly)（公開日：2025-10-27）。
