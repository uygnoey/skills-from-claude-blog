[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Preview, review, and merge with Claude Code

## この記事について
この記事は、Claude Code デスクトップの新機能（実行中アプリのプレビュー、プッシュ前のローカル差分レビュー、GitHub PR の状態監視と auto-fix / auto-merge オプション）を紹介します。

## どんなときに役立つか
ターミナル・ブラウザ・PR 画面を行き来せずに、「変更→確認→マージ」までを短縮したいときに役立ちます。

## 主なポイント
- プレビュー: デスクトップ内で開発サーバーを起動し UI を確認。Claude が画面状態とコンソールログを読み取り反復します。
- レビュー: ‘Review code’ ボタンでローカル差分をプッシュ前にチェックし、インラインコメントを反映できます。
- PR 監視: GitHub PR の CI 状態をアプリ内で追跡し、失敗時の auto-fix と成功時の auto-merge を任意で有効化できます。
- 継続性: `/desktop` で CLI セッションをデスクトップへ移し、デスクトップのセッションを Web/モバイルへ引き継げます。

## 同梱リソース
- スキル: `skills/code-pr-review-loop/` (workflow checklist and reusable command snippets).

## 出典
- https://claude.com/blog/preview-review-and-merge-with-claude-code
