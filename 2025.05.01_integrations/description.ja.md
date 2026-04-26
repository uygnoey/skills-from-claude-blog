[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude があなたの世界に接続できるようになりました

## この記事について

リモート MCP サーバー経由で Claude をアプリやツールに接続する **Integrations** の発表、そして **advanced Research** 拡張の発表記事です。両者を組み合わせることで、Claude は業務アプリからコンテキストを取得し、Web と Google Workspace を検索し、5〜45 分で引用付きの包括レポートを生成できます。2025-05-01 初公開、2025-06-03 のアップデートで Pro まで提供範囲が拡張され、Web 検索は全有料プランでグローバル提供になりました。

## どんなときに役立つか

- サードパーティアプリを独自自動化ではなく Integrations 経由で Claude に接続するかを判断するとき
- 通常なら何時間もかかる多ソース調査を advanced Research で代替する計画を立てるとき
- チームに Integrations + Research のワークフローを導入し、最初に接続すべきアプリを標準化したいとき
- 発表時点で利用可能だったサービスとロードマップを素早く確認したいとき

## 主なポイント

- Integrations は Web・デスクトップを横断する **リモート MCP サーバー** に Claude を接続します。2024 年 11 月の MCP 公開時に Claude Desktop のローカルサーバーに限られていた対応が拡張された形です。
- 発表時点のラインナップ 10 サービス: **Atlassian Jira、Atlassian Confluence、Zapier、Cloudflare、Intercom、Asana、Square、Sentry、PayPal、Linear、Plaid**。ロードマップに **Stripe、GitLab、Box**。
- 開発者は最短 30 分で独自 Integration を構築可能。Cloudflare は OAuth、トランスポート、デプロイを標準提供します。
- 具体パターン: Zapier で数千のアプリと事前定義ワークフローを接続（例: HubSpot 売上取得、カレンダーからミーティングブリーフ作成）、Atlassian でプロダクト計画と Confluence/Jira 一括更新、Intercom の AI エージェント **Fin** が MCP クライアントとして動作しユーザー報告から Linear のバグチケットを起票。
- Advanced Research は要求を複数のサブ調査に分解し数百のソースを横断検索、**5〜45 分** で引用付きレポートを返します。検索対象は Web・Google Workspace に加え、**接続済みの Integration** も含まれます。
- **提供範囲**: 公開時、Integrations と advanced Research は Max・Team・Enterprise でベータ、Web 検索は全有料プランでグローバル。2025-06-03 のアップデート後、Integrations と Research は Pro・Max・Team・Enterprise、Web 検索は全 Claude プランでグローバル。

## 同梱リソース

- [skills/connected-tools-research-playbook/SKILL.md](./skills/connected-tools-research-playbook/SKILL.md): Integrations + Research の併用パターン
- [references/launch-services.md](./skills/connected-tools-research-playbook/references/launch-services.md): 記事に登場するツール/サービスの一覧
- [examples/example-workflows.md](./skills/connected-tools-research-playbook/examples/example-workflows.md): 記事内の具体ワークフロー例
- [guides/getting-started.ja.md](./guides/getting-started.ja.md) (+ en/ko/es): Integrations と Research の有効化と利用開始方法

## 出典

[Claude can now connect to your world](https://claude.com/blog/integrations)（公開日 2025-05-01、更新 2025-06-03）より抽出。
