[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Claude Code の「dynamic workflows（ダイナミック・ワークフロー）」を紹介します。dynamic workflows は、複雑なタスクをより自然に解けるように、Claude Code がその場でマルチエージェントのハーネスを作成し、オーケストレーションできる機能です。

## どんなときに役立つか
dynamic workflows は、トリアージ、検証、複数ステップのエンジニアリング作業など、オーケストレーションの効果が大きい高価値で複雑なタスクに向いており、作業を複数の集中したサブエージェントに分割したいときに有効です。

## 主なポイント
- dynamic workflows は JavaScript のワークフローファイルを実行し、サブエージェントを生成・協調できます。
- 代表的パターン: classify-and-act、fan-out-and-synthesize、adversarial verification、generate-and-filter、トーナメント、停止条件までのループ。
- ワークフローは、エージェントごとのモデル選択や、サブエージェントを独立した worktree で実行するかを決められます。
- 中断しても、セッションを再開すると続きから進められます。
- `~/.claude/workflows` などに保存でき、Skill として配布することも可能です。

## 同梱リソース
- Skill: `skills/dynamic-workflows-harness/`（パターン集 + 再利用できるプロンプトテンプレート）
- Guide: `guides/dynamic-workflows.ja.md`（詳細解説 + ユースケース）

## 出典
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
