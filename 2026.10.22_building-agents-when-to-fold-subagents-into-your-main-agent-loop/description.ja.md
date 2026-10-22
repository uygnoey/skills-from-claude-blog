[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
ルーター、プランナー、ドメイン別サブエージェントを、スキルとツール検索を段階的開示(progressive
disclosure)で使う単一のメインエージェントループにいつ統合すべきか、そして Claude Platform 上で
どう段階的に移行するかを解説したベストプラクティス記事です(2026年10月22日、Diane Sarkis)。

## どんなときに役立つか
- エージェント構成が組織図の写しになってしまったとき(チームごとにサブエージェント1つ)。
- マルチエージェント構成が遅い、口調が揃わない、エンドツーエンドで評価しにくいとき。
- どのサブエージェントを残し、ツールとして呼び、統合し、スキルとツールに畳み込むかを計画するとき。

## 主なポイント
- 複数のエンタープライズ導入の比較では、スキルを持つ単一エージェントが、単一プロンプト設計にも
  サブエージェント設計にも品質で勝ることが多く、コストとレイテンシも低いことが多かった。
- サブエージェントを残す条件: コンテキスト肥大による測定可能な性能低下、使い捨てのコンテキストで
  並列に処理すべき作業、ツール選択の失敗や矛盾する指示。
- 失敗パターン: コンテキスト管理、サブエージェントの乱立、「フランケンプロンプト」、局所的すぎる評価、
  レイテンシ(ある顧客は単一ループで約2倍速い実行時間を確認)。
- 目標設計: モデル1つ、コンテキストウィンドウ1つ、並列のツール呼び出しバッチ、ハーネス側の予算と
  書き込みゲート、コンテキスト内で書いて修正する計画。手順はスキルへ、強い制約はツールへ。
- タスク完了評価(まずはゴールデン例10件)を用意し、サブエージェントを1つずつ移行し、結果が
  反転したタスクを確認し、各タスクを複数回実行する。
- 各チームはスキル、MCP ツール(ユーザー意図単位でまとめる。定義が30〜50を超えると選択精度が低下)、
  ナレッジベースを担当し、小さな中央チームがシステムプロンプトとエンドツーエンド品質を担う。
- 補助: `/claude-api build-eval`、`prompt-audit`、`hillclimb`、`cost-optimize`、`/skill-creator`、
  `/skill-doctor`、デモ付きの移行キット。

## 同梱リソース
- スキル: `fold-subagents-into-agent-loop`(`references/decision-criteria.md`、
  `references/single-loop-design.md`、`templates/migration-plan.md`、`templates/eval-plan.md`)。
- ガイド: `guides/subagent-to-single-loop-migration.{en,ko,es,ja}.md`。

## 出典
- https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
