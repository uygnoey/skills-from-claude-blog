[English](./claude-platform-on-aws-vs-bedrock.en.md) · [한국어](./claude-platform-on-aws-vs-bedrock.ko.md) · [Español](./claude-platform-on-aws-vs-bedrock.es.md) · **日本語**

# Claude Platform on AWS vs Claude on Amazon Bedrock

## このガイドで扱うこと

次の2つの選択肢のどちらを選ぶかを素早く判断するための短いガイドです。

- **Claude Platform on AWS**（Anthropic が運用するプラットフォームに、AWS の入口からアクセス）
- **Claude on Amazon Bedrock**（AWS の境界内で提供される AWS 管理型サービス）

## 判断チェックリスト

### Claude Platform on AWS を選ぶとよい場合

- AWS の IAM／請求／CloudTrail を通じて、Anthropic のネイティブ Claude Platform 体験を使いたい
- 顧客データが AWS の境界外で Anthropic により処理されることを許容できる

### Claude on Amazon Bedrock を選ぶとよい場合

- データを AWS インフラ内に留める必要がある
- 単一の AWS サービスの中で、AWS 管理型の機能やより幅広いモデル選択を重視する

## 出典

- https://claude.com/blog/claude-platform-on-aws
