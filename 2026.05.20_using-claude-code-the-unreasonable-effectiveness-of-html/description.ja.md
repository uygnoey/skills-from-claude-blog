[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Using Claude Code: The unreasonable effectiveness of HTML

## この記事について
この記事では、Claude Code チームのメンバーが Claude Code 利用時に Markdown ではなく **HTML ファイル**の生成を好む理由を説明し、HTML をよりリッチで読みやすく共有しやすいアウトプットとして活用する実践的な方法をまとめています。

## どんなときに役立つか
- Markdown よりも読みやすく、ざっと確認しやすい成果物が欲しいとき
- グリッド/カラム/コールアウトなどのレイアウト、SVG 図、軽いインタラクションが必要なとき
- 企画の探索、PR レビューの解説、インシデントレポートなど、共有して後から見返せるアーティファクトを作りたいとき
- 構造化データを編集するために目的特化の「使い捨て（throwaway）エディタ」を作り、結果を Claude Code に戻したいとき（例: JSON/プロンプト/diff へコピー）

## 主なポイント
- HTML は Markdown に比べて情報密度・可読性・共有性を高める「よりリッチなキャンバス」として位置づけられています。
- ブレインストーミング → 選択肢の探索 → モックアップ → 実装計画のように複数の HTML アーティファクトで反復し、準備ができたらそれらをコンテキストとして新しいセッションで実装に入るワークフローが推奨されています。
- HTML アーティファクトはコードレビュー/理解（diff の表示、注釈、重大度の色分け）、デザインのプロトタイピング、リサーチ/レポーティングに特に有効です。
- カスタム編集 UI では、「copy as JSON」「copy as prompt」「copy diff」などのエクスポートボタンで、結果を Claude Code やファイルに戻せる形で終えることが重要です。

## 同梱リソース
- Skill: `skills/html-artifacts/SKILL.md`
- Guide: `guides/html-artifacts-workflows.*.md`

## 出典
- https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
