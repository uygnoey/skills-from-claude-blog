[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# How Claude Code works in large codebases: Best practices and where to start

## この記事について
この投稿は、大規模コードベースでClaude Codeを安定して動かすための設定・ツール・組織パターンと、スケール導入の始め方を解説します。

## どんなときに役立つか
モノレポやエンタープライズ規模のコードベースでClaude Codeを導入・拡大し、コンテキスト、自動化、責任分担、ナビゲーションの規約を決めたいときに役立ちます。

## 主なポイント
- Claude Code navigates codebases agentically (file traversal + targeted search) rather than relying on a pre-built index.
- The harness (e.g., CLAUDE.md, hooks, skills, plugins, MCP, LSP, subagents) often determines real-world performance.
- Keep CLAUDE.md files lean and layered, and review them periodically as model capabilities change.
- Treat adoption as an org problem too: define ownership (DRI / agent manager) and governance early.

## 同梱リソース
- Skills: 1
- Guides: 1

## 出典
- https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
