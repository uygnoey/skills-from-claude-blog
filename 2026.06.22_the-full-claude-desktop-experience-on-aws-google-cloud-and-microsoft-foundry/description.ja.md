[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、AWS・Google Cloud・Microsoft Foundry 経由で Claude Desktop を利用する組織が、1つのアプリで完全な Desktop 体験（チャット、Claude Cowork、Claude Code）を利用できるようになったことを発表しています。

## どんなときに役立つか
推論を選択したクラウド環境内に保ちながら、エンタープライズのID連携とデバイス管理で Claude Desktop を組織全体に展開したい管理者／IT・セキュリティ担当者に役立ちます。

## 主なポイント
- 単一の展開でチャット、Claude Cowork、Claude Code を提供し、各サーフェスごとにポリシーキーが分かれているため、誰に何を提供するか制御できます。
- 従業員は共有キーではなく、既存のエンタープライズIDプロバイダ（IAM Identity Center、Microsoft Entra ID、その他の OIDC プロバイダ等）でサインインします。
- 管理者はセットアップUIからポリシーテンプレートをエクスポートし、Intune、GPO、Jamf などの一般的な MDM／エンドポイント管理ツールで配布できます。エアギャップ環境向けのオフラインインストーラも言及されています。
- 展開前の検証として、コネクタのテスト、提供される Claude モデルの確認、接続検証を行うことが説明され、設定ミスがあっても Claude へのルーティングを維持するための “model guard” が言及されています。
- Microsoft 365 へのアクセスは、自社の Entra アプリを使うコネクタ（テナントの許可リスト）で提供でき、厳格なレジデンシ要件向けにローカルコネクタの選択肢も説明されています。

## 同梱リソース
- 記事はポリシーテンプレート（セットアップUIからエクスポート）と、管理者向けの展開ガイド（SSO、ポリシーテンプレート、事前検証）に言及しています。

## 出典
- https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
