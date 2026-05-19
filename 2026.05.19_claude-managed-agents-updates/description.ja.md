[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Claude Managed Agentsの2つの新機能を紹介します。1つはユーザーが管理するサンドボックス（self-hosted sandbox）でツール実行を行うこと、もう1つはMCPトンネルを使ってプライベートなModel Context Protocol（MCP）サーバーへ安全に接続することです。

## どんなときに役立つか
機密性の高いコード・ファイル・社内システムを扱いつつ、実行環境とネットワーク接続を企業のセキュリティ境界（perimeter）内に保ちたい場合に役立ちます。

## 主なポイント
- self-hosted sandboxはツール実行をユーザー側インフラ（または管理型プロバイダ）へ移し、エージェントループ（オーケストレーション、コンテキスト管理、エラー回復）はAnthropicのインフラで継続します。
- Cloudflare / Daytona / Modal / Vercelなど、隔離・スケール・ネットワーク・ランタイム要件に応じてサンドボックスプロバイダを選択できます。
- MCPトンネルは、プライベートネットワーク内のMCPサーバーを公開インターネットに露出させずに、エージェントから到達可能にします（単一のアウトバウンド接続、インバウンドのファイアウォール設定不要、エンドツーエンド暗号化）。
- 提供状況: self-hosted sandboxはパブリックベータ、MCPトンネルはリサーチプレビューでアクセス申請が必要です。

## 同梱リソース
- Skill: managed-agents-secure-sandboxing（self-hosted sandboxとMCPトンネルの選定・運用パターン／チェックリスト）
- Guide: managed-agents-network-perimeter（実行と接続性をperimeter内に保つためのデプロイ指向ガイド）

## 出典
- https://claude.com/blog/claude-managed-agents-updates
