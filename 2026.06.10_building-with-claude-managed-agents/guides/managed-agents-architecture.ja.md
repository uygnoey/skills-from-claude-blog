[English](./managed-agents-architecture.en.md) · [한국어](./managed-agents-architecture.ko.md) · [Español](./managed-agents-architecture.es.md) · **日本語**

# Managed Agents アーキテクチャ概要

## これはどんなガイド？
この記事は「The evolution of agentic surfaces: building with Claude Managed Agents」をもとに、Managed Agents の要点をアーキテクチャ観点で簡潔にまとめます。

## 中核となる考え方
Managed Agents は以下を分離します。
- ハーネス（「脳」）: オーケストレーションとモデル呼び出し
- サンドボックス（「手」）: ツール/コードの実行環境

そして、セッションが両者を結ぶ append-only のイベントログとして機能します。

## なぜ分離が重要か
- セキュリティ: 認証情報をサンドボックスの外に置けます。
- パフォーマンス: コンテナが存在する前から推論を開始でき、ツールを使わないセッションはコンテナ起動を回避できます。
- 運用性: 耐久性のあるセッションにより、デバッグのタイムライン、停止/再開、上位機能（Memory, Dreaming）が可能になります。

## 記事で触れられている概念
- agents / environments / sessions を組み合わせ可能なリソースとして扱う
- 認証情報のための Vaults
- オプションのセルフホストサンドボックス（例: VPC 内）
- プライベートネットワーク内の MCP サーバーに接続する MCP tunnels

## 出典
- https://claude.com/blog/building-with-claude-managed-agents
