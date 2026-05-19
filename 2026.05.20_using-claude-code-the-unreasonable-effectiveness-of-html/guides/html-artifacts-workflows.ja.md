[English](./html-artifacts-workflows.en.md) · [한국어](./html-artifacts-workflows.ko.md) · [Español](./html-artifacts-workflows.es.md) · **日本語**

# Claude Code における HTML アーティファクトのワークフロー

## この記事について
Claude Code で Markdown の代わりに HTML ファイルを作業アーティファクトとして使い、計画立案・コード理解・プロトタイピング・レポーティングをより読みやすくリッチにするための実践ガイドです。

## どんなときに役立つか
Markdown では可読性やレイアウト、軽いインタラクションが不足すると感じるときに役立ちます。

## 主なポイント
- グリッド/カラム/コールアウトなど、よりリッチなレイアウトと高い情報密度が必要なら HTML を優先します。
- 大きな作業は、選択肢 → モックアップ → 実装計画のように複数の HTML アーティファクトで反復し、その後に新しいセッションで実装に入ると効果的です。
- レビュー/理解タスクでは、diff の表示、インライン注釈、重大度の色分けを依頼すると有効です。
- 「使い捨てエディタ」では、エクスポートボタン（copy as JSON/プロンプト/diff/Markdown）を必ず入れます。

## 推奨ワークフローパターン
1. **探索グリッド**: 複数案を並べて比較
2. **実装計画**: モック、データフロー、重要スニペットを 1 ページに集約
3. **PR/システム解説**: diff + 注釈 + 注意点（gotchas）
4. **インタラクションの試作**: スライダー/ノブでパラメータ調整
5. **目的特化エディタ**: 1 回限りの UI とエクスポートで durable 形式へ戻す

## 同梱リソース
- プロンプトテンプレート: `../skills/html-artifacts/templates/prompt-patterns.md`

## 出典
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
