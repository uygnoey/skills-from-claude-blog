[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
FedRAMP High 認可環境で Claude のコーディングとエージェント作業の機能を提供する Claude for Government
が、7月からのパブリックベータを経て、米国の連邦・州政府機関向けに一般提供（GA）されたという発表です。
Claude Code CLI と Claude for Microsoft 365 も同じ環境でアーリーアクセスとして提供が始まっています。

## どんなときに役立つか
- 機関が Claude for Government の導入を検討・オンボーディングするとき。
- 管理者が支出上限、シート階層、下位機関の管理を設計するとき。
- セキュリティチームや認可担当者が ATO や監察官（IG）の要請に向けて証跡を集めるとき。
- 調達担当者が GA 条件で Anthropic と直接契約したいとき。

## 主なポイント
- 商用顧客と同等の機能を使え、新機能はおおむね商用のリリースサイクルで届きます。職員はデスクトップ上の
  ファイルで skill・plugin・project を使い、メモ作成、RFP レビュー、ケース処理などを行い、Claude Code
  で公共サービスのソフトウェアを構築・刷新できます。
- シート料金なし：固定単位で使用量を購入し、超過できない上限を設定。グループ別の支出・モデル制限、
  ユーザー別・モデル別の使用量追跡、残高が減る前のアラート。
- 部門管理者が前払い使用量を下位機関に配分し、各下位機関が自らのユーザーを管理します。機関自身の IdP
  による SSO（セルフ設定）、SCIM グループマッピングでレート制限・金額上限・許可モデルを設定し、階層化
  された既定設定で接続先と機能を制御します。
- 監督：管理操作の監査ログ、Anthropic 側の機微な操作には 2 名承認、計量データのみの使用量エクスポート、
  会話履歴は機関管理端末にローカル保存。
- 別途クラウド事業者との契約は不要、MDM で配布、アプリ内で履歴をインポート、Anthropic の trust center
  に FedRAMP Secure Configuration Guide。

## 同梱リソース
- Skill: `government-agency-rollout` — 管理者・セキュリティ・調達向けの段階的な導入計画と、管理者向け
  導入チェックリストのテンプレート。

## 出典
- https://claude.com/resources/articles/claude-for-government-is-now-generally-available
