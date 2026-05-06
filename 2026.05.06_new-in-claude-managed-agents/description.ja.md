[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この投稿では、Claude Managed Agents の新機能である dreaming（研究プレビュー）、outcomes、マルチエージェント・オーケストレーション、Webhook を紹介します。

## どんなときに役立つか
メモリと dreaming によって時間とともに改善するエージェントを作りたい場合、outcomes で自動評価による品質基準を適用したい場合、そして複数の専門エージェントに並列で作業させたい場合に役立ちます。

## 主なポイント
- Dreaming は、過去のセッションやメモリを定期的に見直してパターンを抽出し、エージェントが記憶する内容を洗練するプロセスです。
- Outcomes は成功のルーブリックを定義し、別のグレーダーが出力を評価して、基準を満たすまでエージェントが反復改善します。
- マルチエージェント・オーケストレーションでは、リードエージェントが作業を分割し、各専門エージェント（独自のモデル／プロンプト／ツール）に並列で委任し、共有ファイルシステム上で協働します。
- Webhook により outcomes の評価完了を通知できます。

## 同梱リソース
- Skill: `managed-agent-orchestration`（outcomes 用ルーブリックテンプレート、dreaming/メモリ見直しチェックリスト、役割用語集）。

## 出典
- https://claude.com/blog/new-in-claude-managed-agents
