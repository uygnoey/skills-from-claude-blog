[English](./agent-view-quickstart.en.md) · [한국어](./agent-view-quickstart.ko.md) · [Español](./agent-view-quickstart.es.md) · **日本語**

# Agent view クイックスタート（Claude Code）

## 概要
Agent view は、Claude Code のバックグラウンドセッションを 1 つの画面で実行・管理できるようにします。

## 前提条件
- Claude Code v2.1.139 以降
- research preview（仕様が変わる可能性あり）

## 使い始める
1. `claude agents` を実行します。
2. プロンプトを入力して `Enter` を押し、バックグラウンドセッションをディスパッチします。
3. 同様に複数セッションを並列で起動します。

## 日常の運用
- working と blocked（入力が必要）を見分けて監視します。
- `Space` で peek パネルを開き、一覧から離れずに返信します。
- 深い協業が必要なときだけ attach（`Enter`）します。
- 空のプロンプトで `←` を押して detach し、一覧に戻ります。

## 安全な並列ファイル編集
複数セッションがファイルを編集する場合、worktree による分離が使われることがあります。worktree は `.claude/worktrees/` 配下に作成され、セッション削除時に一緒に削除されます。

## 出典
- https://code.claude.com/docs/en/agent-view
