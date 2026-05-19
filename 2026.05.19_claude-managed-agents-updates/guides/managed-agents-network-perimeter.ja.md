[English](./managed-agents-network-perimeter.en.md) · [한국어](./managed-agents-network-perimeter.ko.md) · [Español](./managed-agents-network-perimeter.es.md) · **日本語**

# 実行と接続性をperimeter内に保つ

## このガイドの内容
- self-hosted sandboxがClaude Managed Agentsの実行境界をどう変えるか
- MCPトンネルがMCPサーバーを公開せずにプライベート接続を提供する仕組み

## 実務ガイダンス

### 実行境界
- リポジトリ、ファイル、依存関係、計算負荷の高いツール実行をサンドボックス内に配置します。
- 管理されたエージェントループはコントロールプレーンに残します。

### 接続性
- プライベートなMCPサーバーには、インバウンドのFW設定や公開エンドポイントを避けるためMCPトンネルを優先します。
- エンドツーエンド暗号化を確認します。

## 出典
- https://claude.com/blog/claude-managed-agents-updates
