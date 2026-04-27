[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事では **Agent Skills** を紹介します。Skill は、指示と（任意で）スクリプトやリソースをまとめた再利用可能なフォルダで、Claude がタスクに関連すると判断したときに読み込みます。

## どんなときに役立つか
Excel ワークフロー、ドキュメント作成の標準、ブランドガイドラインなど、専門的な作業を Claude に一貫した手順で実行させたいときに有用です。Claude アプリ、Claude Code、API をまたいで再利用できます。

## 主なポイント
- Skill は **組み合わせ可能**・**移植可能**で、必要最小限だけ読み込むため **効率的**です。さらに実行可能なコードを同梱できるため **強力**です。
- Claude は Skill の関連性を自動判定し、必要最小限の内容のみをロードします。
- Skill は Claude アプリ、Claude Console、API（`/v1/skills` など）で管理できます。
- Claude Code では、プラグイン（例: anthropics/skills のマーケットプレイス）経由または `~/.claude/skills` に配置して Skill を利用できます。

## 同梱リソース
- Skill バンドル: `skills/agent-skills-overview/`（概要 + クイックスタート用チェックリストと参照リンク）

## 出典
- https://claude.com/blog/skills
