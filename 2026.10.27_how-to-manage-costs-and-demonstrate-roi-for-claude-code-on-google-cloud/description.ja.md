[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
2026年10月27日公開のベストプラクティス記事で、Google Cloud との共催ウェビナーをもとにしています。
プラットフォームチームが Google Cloud 上の Claude Code のコストを管理し、その価値を示す方法を、
コントロール(control)、トラッキング(track)、証明(prove)という3つの独立したレバーで解説します。

## どんなときに役立つか
- Google Cloud で Claude Code を展開し、ガードレール、予算、モデルポリシーが必要なとき。
- 支出が増え、価値の高いパワーユーザーの利用と無駄を見分けたいとき。
- 利用状況ダッシュボードを作る、または経営層に Claude Code の ROI を示す必要があるとき。

## 主なポイント
- 請求額はタスクあたりのトークン数 × モデル単価です。エージェント型の作業はチャットよりタスクあたりの
  トークンが多いため、タスクに合ったモデル選びが大きなレバーになります。トークン単価よりタスクあたりの
  コストが重要です。
- ツールボックス: Google Cloud のプロジェクト単位の課金、予算とアラート、支出上限(Preview)、
  BigQuery エクスポート、割り当て(クォータ)、プロビジョンドスループット、さらに IdP サインイン付きの
  セルフホスト型 Claude apps gateway。
- コントロール ― 制限ではなく誘導: ユーザー・IdP グループ・組織単位で日・週・月ごとの支出上限
  (共有プールではなく各メンバーが継承する1人あたりの既定値)、75% と 95% を超えると CLI 内で警告、
  上限で 429、グループごとの既定モデルと許可リスト、上限を変更できる管理 API。無駄は高額利用者の
  中間層(定型作業に高価なモデル、忘れられた定期タスク)に潜んでいます。
- トラッキング: ユーザー・チーム・モデル・スキル・プラグイン・エージェント・MCP サーバー別の
  Claude Code OpenTelemetry、検証済み ID でタグ付けされる gateway 管理のテレメトリ、コストセンター用の
  `OTEL_RESOURCE_ATTRIBUTES`、Cloud Monitoring のダッシュボードテンプレート、イベントを BigQuery に
  格納し SQL を同梱する OTel クイックスタート、Cloud Billing の BigQuery エクスポート。
- 証明: 導入と利用、開発者満足度(導入前後のアンケート)、ベースラインと比べたインパクト
  (時間・労力・量)。ラベル付きのマージ済み PR のような作業単位を定義します。テレメトリの「作成された
  PR」は「マージされた PR」ではないため、ソース管理やチケットと突き合わせます。プロンプトのログ記録は
  オプトインです。
- 顧客事例: Delivery Hero、Shopify、Fifth Dimension。既定値(組織全体の上限、既定モデル、許可リスト)
  から始め、役割やチームごとに調整する継続的なループを回します。

## 同梱リソース
- スキル: `coding-agent-spend-roi`(`references/governance-toolbox.md`、`references/telemetry-and-tracking.md`、
  `references/roi-metrics.md`、`references/resources.md`、`examples/customer-outcomes.md`、
  `templates/rollout-defaults.md`、`templates/roi-report.md`、`templates/otel-resource-attributes.env`)。
- ガイド: `guides/cost-and-roi-on-google-cloud.{en,ko,es,ja}.md`。

## 出典
- https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
