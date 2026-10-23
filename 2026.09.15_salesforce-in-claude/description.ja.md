[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Salesforce と共同で開発したベータ版プラグイン Salesforce in Claude の発表です(2026年9月15日)。
営業担当者のアカウント・商談・パイプラインを、既存の Salesforce 権限のまま Claude に取り込みます。
アカウントエグゼクティブの日常業務向けに37個のスキルが含まれます。

## どんなときに役立つか
- 営業担当者が Salesforce、メール、通話録音、Slack から文脈を集めるのに時間を取られているとき。
- 会議後の CRM 更新が遅れがちなとき。
- 管理者が営業チームへの展開方法を計画するとき。

## 主なポイント
- Salesforce コネクタは CRM データを読み取り操作し、Slack コネクタはディールチャンネルの要約や
  アカウントチームのスレッドを読み書きします。初回利用時にセットアップスキルが役割に合わせた
  Claude Artifact を作成します。
- ワークフロー: 予約実行の朝のブリーフ(金曜は週次まとめとマネージャー向け更新の下書き)、通話準備、
  日付入りの相互クロージングプランを含む商談レビュー、会議後のフォローアップと商談更新、
  共有可能なパイプライン・フォーキャストのダッシュボード。
- Salesforce が記録システムのままで、Claude は担当者の権限で許される範囲だけを見て、既定では書き込み前に
  承認を求めます。Team/Enterprise の顧客データは既定で学習に使われません。
- すべての有料プランでベータ提供。Salesforce MCP はマーケットプレイスからインストールし、管理者は
  AgentExchange でアクセスを申請、組織全体で Salesforce を一度接続し、プラグインを配布するグループを選びます。
- GitLab、Siemens、Legora と 7,000 人の Salesforce 営業担当者が利用しています。

## 同梱リソース
- スキル: `crm-seller-workflows`(`references/workflows.md`、`references/setup-and-permissions.md`、
  `templates/close-plan.md`、`templates/post-meeting-update.md`)。

## 出典
- https://claude.com/resources/articles/salesforce-in-claude
