[English](./api-console-workspaces-operations.en.md) · [한국어](./api-console-workspaces-operations.ko.md) · [Español](./api-console-workspaces-operations.es.md) · **日本語**

# Workspaces 運用チェックリスト（Anthropic API Console）

## 1) 計画
- Workspace が何を表すかを決めます（プロジェクト、環境、チーム、またはその組み合わせ）。
- 何を分離するかを決めます（API キー、上限、アクセス制御、レポート）。

## 2) 作成
- Anthropic API Console で Workspace を作成します。
- その Workspace 用のスコープ付き API キーを作成します。

## 3) 制御
- Workspace の月次支出上限を設定します。
- 組織の上限内で Workspace 固有のレート制限を設定します。
- Workspace レベルでユーザー権限を最小権限で付与します。

## 4) 監視
- Workspace 別の利用状況とコストを定期的に確認します。
- トラフィックの変化に応じて支出上限・レート制限を調整します。

## 出典
- https://claude.com/blog/workspaces
