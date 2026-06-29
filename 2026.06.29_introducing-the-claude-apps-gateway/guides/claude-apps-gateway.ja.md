[English](./claude-apps-gateway.en.md) · [한국어](./claude-apps-gateway.ko.md) · [Español](./claude-apps-gateway.es.md) · **日本語**

# Claude apps gateway: デプロイと展開の概要

## このガイドについて
このガイドは、記事で説明されているデプロイ／展開モデルを要約します。SSO、ポリシー強制、テレメトリ、ルーティングといった機能、およびクライアント側の設定方法に焦点を当てています。

## どんなときに役立つか
Amazon Bedrock または Google Cloud 上で Claude Code を組織展開する際に、集中ログイン、ポリシーの一貫した強制、ユーザー別の使用量帰属が必要な場合のクイックリファレンスとして役立ちます。

## アーキテクチャ（記事の記述）
- **Gateway**: Linux 上の単一のステートレスなコンテナ、バックエンドは **PostgreSQL**。
- **Identity**: ゲートウェイは IdP（例: Google Workspace, Microsoft Entra ID, Okta）に対する **OIDC relying party** として動作し、短命セッションを発行します。
- **Policy**: Managed settings（ポリシー）はサーバーで一度定義され、クライアントはサインイン時に受け取り、ゲートウェイが各リクエストで強制します。
- **Telemetry**: クライアントはリクエストごとに使用量メトリクスを付与し、ゲートウェイが **OTLP** で指定したコレクタへ中継します。
- **Routing**: ゲートウェイが upstream 資格情報を保持し、**Claude API** / **Amazon Bedrock** / **Google Cloud** に推論をルーティングし、任意でプロバイダ間のフェイルオーバーをサポートします。

## 展開手順（記事の記述）
1. **ゲートウェイをデプロイ**
   - Claude Code CLI バイナリをダウンロードします。
   - `gateway.yaml` に OIDC issuer と upstream 資格情報を設定します。
   - IdP に OIDC アプリを 1 つ登録します。
2. **クライアントでゲートウェイログインを強制**
   - 開発者マシンへ `managed-settings.json` を配布します。
   - `forceLoginMethod` と `forceLoginGatewayUrl` を設定し、初回起動時にゲートウェイへ接続させます。
3. **中央で運用・調整**
   - 許可モデルや既定値を中央で管理します。
   - コレクタへ中継されたテレメトリをユーザー別の帰属に利用します。
   - 組織／グループ／ユーザー単位で日次・週次・月次の支出上限を適用します。

## 出典
- https://claude.com/blog/introducing-the-claude-apps-gateway
