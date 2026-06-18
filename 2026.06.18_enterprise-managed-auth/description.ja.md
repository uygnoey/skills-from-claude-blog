[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Claude の MCP コネクターに対して、Okta を起点に IdP で組織的に権限付与を集中管理できる「エンタープライズ管理型の認可」を紹介します。

## どんなときに役立つか
企業環境でコネクターのアクセスを IT が一元管理し、ユーザーは初回ログイン時から自動で利用でき、失効（回収）も IdP 主導で運用したい場合に役立ちます。

## 主なポイント
- 管理者がコネクターを一度承認すれば、ユーザーは IdP の既存グループ/ロールによりアクセスを継承します。
- ユーザー側の個別 OAuth 承認が不要になり、「ゼロタッチ」で利用開始できます。
- Claude チャット、Claude Code、Cowork でアクセスが一貫します。
- Model Context Protocol の Enterprise-Managed Authorization 拡張（オープン標準）に基づき、カスタムコネクターでも対応可能です。
- 集中管理により、トークン有効期限を短くしても運用を崩しにくく、権限回収時の残存リスクを減らせます。

## 同梱リソース
- Skill: enterprise-managed-connector-auth（導入チェックリスト + 運用手順）
- Guide: enterprise-managed-connector-auth-rollout（実運用ガイド）

## 出典
- https://claude.com/blog/enterprise-managed-auth
