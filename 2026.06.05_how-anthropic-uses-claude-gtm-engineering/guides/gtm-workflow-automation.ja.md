[English](./gtm-workflow-automation.en.md) · [한국어](./gtm-workflow-automation.ko.md) · [Español](./gtm-workflow-automation.es.md) · **日本語**

# Claude Code による GTM ワークフロー自動化

## このガイドの内容
この記事のやり方を、繰り返し使える方法として整理します。GTM チーム向けに Claude Code のワークフローを作る際、狭いユースケースから始め、最新コンテキストを取り込み、文体が合うまでプロンプトを反復し、その後チーム全体で使えるように束ねます。

## 手順
1. **最も痛いワークフローを 1 つ選ぶ**（例：顧客メール返信）。
2. 実行時に使う **コンテキスト源** を定義する（メール、カレンダー、CRM、ドキュメント）。
3. **システムプロンプト** を作り、出力がチームの声になるまで反復する。
4. 関係性に応じた **トーンのバリエーション** を追加する。
5. 最初が安定したら、隣接ワークフロー（事前ブリーフ、日次リキャップ）へ拡張する。
6. **導入のために束ねる**（スキル + 連携/コネクタ）ことで、他の人がすぐ使えるようにする。

## 推奨アーティファクト
- Skill: [../skills/sales-workflow-briefing/SKILL.md](../skills/sales-workflow-briefing/SKILL.md)
- テンプレート: [../skills/sales-workflow-briefing/templates/](../skills/sales-workflow-briefing/templates/)

## 出典
- https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
