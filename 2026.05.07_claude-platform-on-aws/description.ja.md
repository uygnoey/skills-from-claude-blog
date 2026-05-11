[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は **Claude Platform on AWS** を紹介します。Anthropic の first-party Claude Platform を、AWS の入口（IAM、請求、監査ログ）から利用できるようにする仕組みです。

## どんなときに役立つか
- 調達・課金・アクセス制御・監査を AWS の運用に統一したいとき
- Anthropic の別個の認証情報を管理せずに、Claude Platform のネイティブ体験を使いたいとき

## 主なポイント
- 既存の **AWS 認証情報** と **IAM ポリシー** で Claude Platform にアクセスします。
- 利用料金は **AWS の一括請求** で処理されます。
- アクティビティは **AWS CloudTrail** に記録されます。
- 重要な違い: この方式では **顧客データは AWS の境界外で Anthropic により処理** されます。

## 同梱リソース
- “Claude Platform on AWS” と “Claude on Amazon Bedrock” の違いを踏まえ、アクセス制御・監査・導入の検討ポイントを整理するスキル

## 出典
- https://claude.com/blog/claude-platform-on-aws
