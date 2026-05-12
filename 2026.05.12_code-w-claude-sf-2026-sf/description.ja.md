[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Code w/ Claude SF 2026: AI の指数曲線の上で作る

## この記事について

Anthropic が 2026 年 5 月 12 日に公開した年次デベロッパーカンファレンス Code w/ Claude SF のリキャップです。Claude Code のレート制限を 2 倍に、Claude Opus の API 制限を引き上げ、Claude Platform 上の Claude Managed Agents に 4 つの新機能(Dreaming、Multiagent orchestration、Outcomes、Webhooks)を追加したことを発表し、キーノートとブレイクアウトセッションの YouTube アーカイブを案内します。

## どんなときに役立つか

- Claude Managed Agents 上で構築するチームが、GA となった Dreaming、Multiagent orchestration、Outcomes、Webhooks を採用するか判断するとき。
- 共有ファイルシステム上で、リードエージェントが並列のスペシャリストサブエージェントに作業を委譲するアーキテクチャを設計するとき。
- エージェント出力の品質基準を定義し、別グレーダーとリビジョンループを本番パイプラインに組み込むとき。
- ポーリングではなく webhook で非同期エージェントの実行結果を既存システムに接続するとき。

## 主なポイント

- Claude Code のレート制限が 2 倍、Claude Opus の API 制限が引き上げ。どちらも発表時点で有効。
- すべての開発者に公開された Claude Managed Agents の 4 つの新機能:
  - **Dreaming** — 過去のエージェントセッションを精査してパターンを抽出し、メモリをキュレーションすることで、実行間でエージェントが改善されるスケジュールプロセス。
  - **Multiagent orchestration** — リードエージェントが共有ファイルシステム上で、モデル・プロンプト・ツールが異なるスペシャリストサブエージェントへ並列に委譲。全体フローは Claude Console で追跡可能。
  - **Outcomes** — 開発者が「良い出力」のルーブリックを定義し、別グレーダーが独立した context window で結果を評価して、基準を満たすまでエージェントがリビジョン。社内ベンチマークの最難問で最大 10 ポイントの向上が報告されている。
  - **Webhooks** — outcome を定義したら、エージェントを走らせきり、完了時に webhook で通知。
- 本文で言及された顧客トーク: Asana、Cursor、GitHub、Replit、Vercel。
- Code w/ Claude はロンドン(5 月 19〜18 [原文ママ])と東京(6 月 5〜6)へ続き、Day 1 のキーノートとブレイクアウトはライブ配信。

## 同梱リソース

- `skills/managed-agents-new-capabilities/SKILL.md` — 4 つの新機能を採用するためのプレイブックスキル。
- `skills/managed-agents-new-capabilities/references/announcements-from-post.md` — 本文中のカンファレンス発表項目と顧客リファレンスの逐語カタログ。
- `skills/managed-agents-new-capabilities/examples/outcomes-and-multiagent-patterns.md` — Outcomes、Multiagent orchestration、Webhooks を組み合わせたワーキング例。

## 出典

- [Code w/ Claude SF 2026: Building on the AI exponential](https://claude.com/blog/code-w-claude-sf-2026-sf) (Anthropic ブログ、2026 年 5 月 12 日)
