[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は Claude apps gateway を紹介します。これは Amazon Bedrock と Google Cloud で Claude Code を運用する際に、認証・ポリシー・コスト管理を中央で統制できるセルフホスト型ゲートウェイです。

## どんなときに役立つか
開発者ごとにクラウド資格情報を配布せずに Claude Code を大規模展開したいときに有用です。あわせて、モデルや既定値などの組織ポリシーを一貫して強制し、ユーザー別のコスト帰属や支出上限を適用できます。

## 主なポイント
- ゲートウェイは Linux 上の単一のステートレスなコンテナとしてデプロイされ、PostgreSQL をバックエンドに利用します。
- 上流（upstream）プロバイダの資格情報を保持し、開発者を IdP（OIDC）で認証します。
- Managed settings（ポリシー）はサーバーで一度定義され、クライアントのサインイン時に適用され、すべてのリクエストで強制されます。
- クライアントはリクエストごとに使用量メトリクスを付与し、ゲートウェイが OTLP で設定したコレクタへ中継します。
- Claude API / Amazon Bedrock / Google Cloud へルーティングでき、プロバイダ間のフェイルオーバーを任意でサポートします。
- 日次・週次・月次の支出上限を、組織・グループ・ユーザー単位で適用できます。

## 同梱リソース
- 記事で言及されている設定ファイル例: `gateway.yaml` と `managed-settings.json`（例: `forceLoginMethod`, `forceLoginGatewayUrl`）。
- ゲートウェイは開発者が既に導入している同一の `claude` CLI バイナリに同梱されています。

## 出典
- https://claude.com/blog/introducing-the-claude-apps-gateway
