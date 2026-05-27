[English](./managed-agents-private-execution-overview.en.md) · [한국어](./managed-agents-private-execution-overview.ko.md) · [Español](./managed-agents-private-execution-overview.es.md) · **日本語**

# Claude Managed Agents のプライベート実行オプション（概要）

## これは何？
Code w/ Claude London 2026 のまとめで触れられた Claude Platform の2つの機能（self-hosted sandbox と MCP トンネル）を、意思決定の観点で短く整理したガイドです。

## 判断フロー
1) **エージェントのコード実行場所**を制御したい（データ/ファイルを境界外に出せない）？
- はい → Self-hosted sandbox。

2) インバウンドのエンドポイントを公開せずに、Claude から **プライベートな MCP サーバー**に到達したい？
- はい → MCP トンネル。

3) 両方必要？
- はい → 両方を併用。

## 実装チェックリスト（概要）
- データ境界（リポジトリ、ファイル、シークレット、ログ）を定義する。
- 公開する内部ツール（MCP サーバー）と必要な認証を整理する。
- ネットワークの egress 方針と監査ログ要件を決める。
- 役割分担：ランタイム/インフラ、セキュリティ、Console 管理者。

## 追加の参照
- Reference: `../skills/managed-agents-private-execution/references/managed-agents-private-execution.md`
- 出典（イベントまとめ）: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
