[English](./enterprise-managed-connector-auth-rollout.en.md) · [한국어](./enterprise-managed-connector-auth-rollout.ko.md) · [Español](./enterprise-managed-connector-auth-rollout.es.md) · **日本語**

# エンタープライズ管理型コネクター認可の展開ガイド（Okta）

## 目的
MCP コネクターの認可を IdP のグループ/ロールで一元管理し、ユーザーが初回ログインから自動で利用できる状態にします。

## 推奨フェーズ
1. スコープ定義：対象コネクター、パイロットグループ、成功基準。
2. 集中プロビジョニング：管理者が一度承認し、IdP グループ/ロールで範囲を付与。
3. パイロット検証：ゼロタッチ利用と失効（回収）動作を確認。
4. 本番展開：割り当て拡大、運用/サポート手順を文書化。

## 運用上の注意
- コネクターアクセスも他のアクセス管理と同様に、IdP でプロビジョニング/監査/回収します。
- 権限回収後にアクセスが残らないよう、トークン有効期限の短縮を検討します。
- 必要に応じて IdP 経由のみの接続を強制し、個人/業務アカウントの混在を減らします。

## 出典
- https://claude.com/blog/enterprise-managed-auth
