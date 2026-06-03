[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Lessons from building Claude Code: How we use skills

## この記事について
この記事は、Anthropic が Claude Code で数百の skills を構築・運用・スケールさせる中で得た学びをまとめたものです。skills の代表的なカテゴリと、書き方・構造化・配布に関する実践的なヒントを紹介します。

## どんなときに役立つか
Claude Code 向けに skills を設計する際に、何を入れるべきか（gotchas、参照、スクリプト、テンプレート等）、フォルダ構成で progressive disclosure をどう実現するか、リポジトリやプラグインとしてどう配布するか、といった具体的な指針が欲しいときに役立ちます。

## 主なポイント
- skills は Markdown 1枚ではなく、スクリプト・アセット・データ・設定を含められる **フォルダ**です。
- Anthropic は内部の skills を 9カテゴリに分類し、1カテゴリに明確に収まる skills のほうが概ねうまく動くと観察しました。
- もっとも信号が強い部分は、実際の失敗から蓄積する「Gotchas」セクションであることが多いです。
- skills は `./.claude/skills` へチェックインするか、マーケットプレイスからインストールできるプラグインとして配布できます。
- Hook は on-demand（skill が呼ばれたときだけ）有効化でき、常時フックよりも邪魔になりにくいです。

## 同梱リソース
- skills 設計・構造化のためのチェックリスト形式ガイド。
- skills のカテゴリと例の参照。

## 出典
- https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
