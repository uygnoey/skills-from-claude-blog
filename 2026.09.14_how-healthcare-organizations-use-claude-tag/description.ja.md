[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Camy Pearson、Maria Howe、Araba Koomson によるベストプラクティス記事(2026年9月14日)です。医療機関が
Claude Tag(ベータ、Slack 上の Claude)を保護対象保健情報(PHI)に一切触れない業務でどう使っているかを、
Insight Health、Tennr、Medallion の事例で紹介します。

## どんなときに役立つか
- 医療・規制業界のチームが Slack に AI チームメイトを置きたいが、PHI は確実に遮断したいとき。
- Claude Tag パイロットのチャンネル、コネクタ、自律性レベルを決めるとき。
- 実績のある PHI 非接触のユースケース(障害対応、社内ツール保守、保険者ルールの知識)を探すとき。

## 主なポイント
- Claude Tag はまだ Anthropic の BAA の対象外のため、PHI のないチャンネルとコネクタでのみ使います。
- 管理者コントロール: デフォルト無効、承認チャンネルの許可リスト、DM 無効、チャンネル単位のコネクタ範囲、
  EHR・臨床システム・患者コミュニケーションを除外するアクセスバンドル。呼び出したメンバーが見られるものだけを見ます。
- Insight Health は PHI をマスクする BAA 対象の Agent SDK エージェント Zeus と Claude Tag を組み合わせ、
  重要アラートチャンネルのアラートの 97% がエンジニアの介入なしにクローズされました。
- Tennr は Claude Tag を社内オファーポータルの主要メンテナーとして使っています(約1か月で15件以上のチケット)。
- Medallion は保険者ルールの知識をチャンネルに蓄積し、Claude に確信がないときは専門家をタグ付けします。
- 1チャンネル・1〜2コネクタから始め、GitHub を接続して2週間パイロットします。
- クレジット(Enterprise $25,000 / Team 10席以上 $2,500)は2026年10月1日に失効しました。

## 同梱リソース
- スキル: `phi-safe-slack-agent-rollout`(`references/customer-patterns.md`、
  `templates/rollout-checklist.md`)。

## 出典
- https://claude.com/resources/articles/how-healthcare-organizations-use-claude-tag
