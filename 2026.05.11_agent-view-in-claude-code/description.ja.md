[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude Code の Agent view

## この記事について
Agent view は、Claude Code の複数のバックグラウンドセッションを 1 画面で管理するフルスクリーンのターミナル UI です。

## どんなときに役立つか
バグ修正、PR レビュー、ログ調査など、互いに独立した作業を並列で走らせ、セッションが入力を求めたときだけ介入したい場合に役立ちます。

## 主なポイント
- `claude agents` で agent view を開きます。
- 新しいバックグラウンドセッションのディスパッチ、状態監視、peek での返信、attach/detach ができます。
- agent view は research preview で、Claude Code v2.1.139 以降が必要です。
- セッションは supervisor プロセス配下で動作し、ターミナル再起動後もディスク上に状態が残ります。

## 同梱リソース
- Skill: `manage-agent-view-sessions`（コマンド、フィルター文法、繰り返し使えるセッション管理チェックリスト）
- ガイド: `agent-view-quickstart`（日常業務で agent view を導入する方法）

## 出典
- https://claude.com/blog/agent-view-in-claude-code
- https://code.claude.com/docs/en/agent-view
