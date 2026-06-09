[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude Managed Agents の新機能: スケジュール実行と Vault の環境変数

## この記事について
この記事は、Claude Managed Agents の2つの新機能（パブリックベータ）を紹介します。cron のように定期実行できるスケジュールドデプロイメントと、CLI 認証のために Vault に環境変数を保存できる機能です。

## どんなときに役立つか
独自のスケジューラを構築・運用せずにエージェントに定例作業をスケジュール実行させたいとき、また API キーなどの秘密情報をモデルに見せずに CLI ツールへ安全に渡したいときに役立ちます。

## 主なポイント
- スケジュールドデプロイメントは cron スケジュールごとに新しいセッションを開始し、一時停止/再開/アーカイブや手動トリガーにも対応します。
- Vault が環境変数をサポートし、CLI が認証付きリクエストを送れるようになります。実際のキーは許可したドメインへの通信時にネットワーク境界で注入され、モデルはキーを見ません。

## 同梱リソース
- Skill: managed-agents-scheduled-deployments（運用チェックリストと活用パターン）

## 出典
- https://claude.com/blog/whats-new-in-claude-managed-agents
