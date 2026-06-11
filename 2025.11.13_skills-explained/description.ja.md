[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Skills をプロンプト、Projects、MCP、Subagent と比較し、Claude のスタックの中で Skills がどこに位置するかを説明します。さらに、これらを組み合わせたワークフロー例も示します。

## どんなときに役立つか
繰り返しの指示を Skill にするか、会話のプロンプトのままにするか、背景知識を Project に置くか、MCP でデータを接続するか、Subagent に委任するかを判断するときに役立ちます。

## 主なポイント
- Skill は（手順 + 任意のコード/アセット）からなる再利用可能なバンドルで、progressive disclosure により必要なときだけ動的にロードされます。
- プロンプトは会話中の一回限りの指示です。
- Project は知識ベースを持つ永続的なワークスペースです。
- Subagent は独自のプロンプトとツール権限を持つ専門アシスタントです。
- MCP はデータが存在する外部システムに Claude を接続します。

## 同梱リソース
- Skill: `skills/skills-stack-explainer/`
- Agent: `agents/market-researcher.md`, `agents/technical-analyst.md`, `agents/code-reviewer.md`
- Guide: `guides/skills-vs-prompts.*.md`, `guides/skills-vs-projects.*.md`, `guides/skills-vs-mcp.*.md`, `guides/skills-vs-subagents.*.md`

## 出典
- https://claude.com/blog/skills-explained
