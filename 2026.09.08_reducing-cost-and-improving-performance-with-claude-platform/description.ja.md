[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Claude Platform ではコストと性能をトレードオフする必要はない、と論じるベストプラクティス記事です
(2026年9月8日、のちに Opus 5.5 のベンチマークを追記)。プロンプトキャッシュのヒット最大化、
フロンティアモデル移行時のプロンプトのアンチパターン除去、タスクに合わせた effort の調整という
3つのレバーが、たいてい両方を改善します。この指針は `claude-api` スキルにまとめられています。

## どんなときに役立つか
- API の支出が大きい、またはキャッシュヒット率が低いとき。
- 新しいモデルに移行したが、古いプロンプト・スキル・ツール説明をそのまま使っているとき。
- eval を基準にモデルと effort レベルを選ぶとき。

## 主なポイント
- プロンプトキャッシュ: モデルに固定され、プレフィックスのバイト単位の一致が必要で、既定の TTL は5分。
  タイムスタンプや ID、順序が変わるツールをプレフィックスから外し、`defer_loading` を使い、
  システムプロンプトの更新はメッセージで送り、`max_tokens: 0` で事前ウォームし、長い待ちには1時間 TTL を検討します。
- アンチパターン: 検証の儀式、徹底さの強調、スクラッチパッドの枠組み、古い例、矛盾したルール、
  古い設定。`/claude-api prompt-audit` が検出し、事例ではコストをさらに約9%削減、精度を約2ポイント向上させました。
- Effort: 高すぎると考えすぎ、低すぎると根拠集めを省きます。effort をスイープし、より強いモデルを低い
  effort で試します。`/claude-api hillclimb` が held-out テストセット付きで探索を自動化します。
- `/claude-api cost-optimize` はレバー(キャッシュ、内容の削減、出力の上限、Batch API)を順位付けし、
  公開ベンチマークで品質をほぼ変えずにコストを約24〜73%削減しました。

## 同梱リソース
- スキル: `api-cost-performance-tuning`(`references/prompt-cache-checklist.md`、
  `references/prompt-anti-patterns.md`、`references/benchmark-results.md`、
  `templates/cost-audit-report.md`)。

## 出典
- https://claude.com/resources/articles/reducing-cost-and-improving-performance-with-claude-platform
