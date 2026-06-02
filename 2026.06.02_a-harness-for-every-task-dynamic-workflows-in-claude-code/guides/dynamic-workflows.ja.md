[English](./dynamic-workflows.en.md) · [한국어](./dynamic-workflows.ko.md) · [Español](./dynamic-workflows.es.md) · **日本語**

# ガイド: Claude Code の dynamic workflows

## 何か
dynamic workflows は、サブエージェントを生成・協調できる JavaScript ワークフローファイルを実行することで、Claude Code がオンデマンドにマルチエージェントのハーネスを作成して実行できる機能です。

## 仕組み（概要）
- ワークフローは、サブエージェントの生成/協調のための特別なヘルパー関数を備えた JavaScript ファイルを実行します。
- JSON/Math/Array などの標準 JavaScript 機能でデータ処理ができます。
- エージェントごとのモデル選択や、サブエージェントを独立した worktree で実行するかを決められます。
- 中断しても、セッションを再開すると続きから進められます。

## どんなときに役立つか
隔離されたコンテキスト、専門化された役割、構造化された統合/検証が効く、複雑で高価値なタスクに向いています。

## よくあるパターン
- classify-and-act
- fan-out-and-synthesize（バリア + マージ）
- adversarial verification（ルーブリックに基づくレビュー）
- generate-and-filter（大量生成 → 重複除去 → 上位のみ）
- tournament（ペアワイズ審査で勝者/top-k）
- loop until done（固定回数ではなく停止条件）

## ユースケース
- エンジニアリング: failing test/module/callsite で分割 → worktree で並列修正 → 対抗的レビュー/マージ。
- トリアージ: 分類、既存トラッキングと重複排除、不確実なものを quarantine してから実行。
- 軽量 eval: worktree 上で候補解を実行し、ルーブリックで比較/採点。
- 非技術: 多視点の批評、ルーブリック面接付きのレジュメ選定、ネーミングのトーナメント。

## 保存と共有
- ワークフローメニューで `s` を押して保存し、`~/.claude/workflows` 配下に置けます。
- Skill として配布する場合は、ワークフロー JavaScript ファイルを skill フォルダに入れ、`SKILL.md` から参照します。
- 柔軟性のため、ワークフローを「そのまま実行すべきスクリプト」ではなく「テンプレート」として扱うとよい場合があります。

## 出典
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
