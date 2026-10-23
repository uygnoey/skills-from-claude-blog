[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Balyasny Asset Management（BAM）の Chief AI Officer、Charlie Flanagan 氏へのインタビューです（2026年9月17日公開）。
BAM が Claude Fable 5 を有効化する前にどう評価したか、モデルの外側に置く統制でエージェントをどう管理しているか、
社内エージェント基盤 BAMAgent で何が可能になったかを説明しています。

## どんなときに役立つか
- 本番のエージェント業務を新しいフロンティアモデルに切り替えるか判断するとき。
- 公開ベンチマークではなく、実際の検証可能なタスクで社内評価セットを作るとき。
- 高リスク領域でエージェントのアクセス範囲を広げる前に、権限・ログ・人によるレビューを決めるとき。

## 主なポイント
- BAM にとって 2026 年は「検索する AI」から「仕事を完了する AI」へ移った年で、Claude Code のような
  エージェントハーネスがその契機でした。
- 評価：株式・マクロ・コモディティにわたる検証可能な金融タスク数千件を、モデル単体と BAM のエージェント
  ハーネス内の両方で実行。該当サブセットで Fable は 89.4%、従来の本番モデルは 86.1% で、計画・分析・
  エージェント実行で最も大きく改善しました。
- これまでどのモデルも解けなかった経済学の問題を解いたという意外な結果は、まず評価の欠陥を疑い、再実行・
  タスクと採点ロジックの独立検証・Anthropic とのレビューを経て受け入れました。
- 安全性はモデルの外側の統制で担保します：承認済みデータ境界、最小権限、ツール単位の権限、ログ、重要な
  成果物の人によるレビュー、エスカレーション経路。より有能なモデルでも権限は広がらず、投資判断は人が担います。
- BAMAgent は数千の自律エージェントを運用しています。合併アービトラージ分析は 3〜5 日から 1 日未満
  （エージェント実行は約 30 分）に、中央銀行分析は約 2 日から約 30 分に短縮され、レビューは維持されています。
  300 を超えるエージェントを動かすチームもあります。

## 同梱リソース
- スキル：`frontier-model-eval-governance`（`references/eval-dimensions.md`、`templates/controls-checklist.md`、`examples/workflows.md`）。
- ガイド：`guides/agentic-model-evaluation-and-governance`（4 言語）。

## 出典
- https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
