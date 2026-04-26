[English](./getting-started.en.md) · [한국어](./getting-started.ko.md) · [Español](./getting-started.es.md) · **日本語**

# Integrations と advanced Research の始め方

[Claude can now connect to your world](https://claude.com/blog/integrations)（2025-05-01 公開、2025-06-03 更新）に基づく短いガイドです。最初に何を有効化するか、接続アプリのカタログをどう捉えるか、接続を活かす Research リクエストをどう設計するかを扱います。

## 1. プラン提供範囲の確認

2025-06-03 のアップデート後、Integrations と advanced Research は Pro・Max・Team・Enterprise で利用できます。Web 検索は **すべて** の Claude プランでグローバル提供です。

公開当時の状態では、Integrations と Research は Max・Team・Enterprise でベータ、Web 検索は有料プランでグローバルでした。

## 2. 最初に接続するアプリを選ぶ

ローンチラインナップ（Atlassian Jira、Atlassian Confluence、Zapier、Cloudflare、Intercom、Asana、Square、Sentry、PayPal、Linear、Plaid）から選びます。未対応アプリの場合、Zapier Integration の事前定義ワークフローで代替できるか確認してください。記事時点のロードマップには Stripe、GitLab、Box が挙がっています。

候補ごとに次を書き出します: どの Claude タスクがそのデータへのアクセスを必要とするか、Claude にどのアクションを取らせるか、組織が許可している認証モデルは何か。

## 3. Integrations 画面から接続

各 Integration はリモート MCP サーバーを利用します。接続後、Claude はコンテキスト（プロジェクト履歴、タスク状態、組織知識）を読み取り、そのアプリに対して操作を実行できます。

独自 Integration を構築する場合、Cloudflare のホスティングを利用すると OAuth・トランスポート・デプロイが標準で提供されます。記事によれば新規 Integration は最短 30 分で構築可能です。

## 4. advanced Research リクエストの実行

- **Research** ボタンを有効化します。
- リクエストはブリーフのように記述します: 問い、スコープ、検索対象に含める接続アプリを明示。
- 大半のレポートは 5〜15 分、複雑な調査は最大 45 分。
- レポート内の引用リンクを直接確認した上で活用します。

## 5. 推奨される最初のワークフロー

- Zapier 経由: HubSpot の売上データ取得、カレンダーからミーティングブリーフ作成。
- Atlassian: Confluence スペースの要約、キックオフ文書から Jira 項目を一括作成。
- Intercom + Linear: 繰り返し発生するユーザーフィードバックのパターンを発見し、MCP クライアントとして動作する Fin が同じ会話内で Linear バグを起票。

## 出典

[Claude can now connect to your world](https://claude.com/blog/integrations)（公開日 2025-05-01、更新 2025-06-03）。
