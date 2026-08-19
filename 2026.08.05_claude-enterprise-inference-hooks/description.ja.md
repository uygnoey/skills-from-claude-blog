[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Claude Enterprise にインラインのデータ損失防止（DLP）を追加するセキュリティ機能 **inference hooks** の発表記事です。有効化すると、すべての推論リクエストが署名付き WebSocket 接続を通じて組織が管理するセキュリティサーバーへ送られます。モデルが生成を始める前に、Claude はプロンプトと周辺コンテキストをそのサーバーへ送り、allow / deny の判定を受け取ってから処理を進めます。ツール呼び出しの応答も、モデルへ返される前に同じ検査を受けます。

これまでネイティブなインライン強制は Claude Code のクライアント側フックに限られていました。inference hooks は、チャット、Claude Code、Claude Cowork、そして MCP コネクタ・スキル・プラグイン経由のツール呼び出しまで、Claude Enterprise の各サーフェスに単一の強制レイヤーを広げます。製品ごとの個別統合は不要です。

## どんなときに役立つか
- 機微データが流れうるすべての経路を、セキュリティチームが管理する検査点に通す必要があるとき。
- 既存の DLP プログラム（Netskope、Palo Alto Networks、Proofpoint、Zscaler、または自社構築サーバー）を AI 利用にも広げたいとき。
- 製品ごとに統合を作らず、組織レベルの設定ひとつでカバーしたいとき。
- 強制適用の前に、シャドーモード・除外設定・割合ベースの段階展開が必要な導入計画を立てるとき。

## 主なポイント
- **生成前の検査。** プロンプトとコンテキストは生成前に自社サーバーへ送られ、Claude は判定を受け取ってからのみ続行します。
- **ツール応答も検査対象**で、MCP コネクタ・スキル・プラグイン経由のツールも含まれます。
- **公開スキーマを備えたオープンな webhook ベースのプロトコル**なので、既存の DLP サーバーをそのまま利用でき、セキュリティベンダーは統合を構築できます。
- **組織レベルのスイッチひとつ**で Claude Enterprise のサーフェスを覆い、製品ごとの統合を作る必要がありません。
- **展開の制御**：シャドーモード（常に許可）、ロールベースの除外、割合ベースの展開、加えて失敗時ポリシーとタイムアウトの設定。
- 記事の時点では **Claude Enterprise 顧客向けのベータ**として提供されています。
- 名称の重なりに注意してください。ここで扱うのは*サーバー側の inference hooks* であり、Claude Code のクライアント側ライフサイクルフック（PreToolUse、PostToolUse など）とは別物です。

## 同梱リソース
- `skills/inference-dlp-rollout/SKILL.md` — 利用者の作業を止めずにインライン DLP を有効化する段階的な展開手順。
- `skills/inference-dlp-rollout/references/enforcement-model.md` — 検査が行われる場所と各制御の役割。
- `skills/inference-dlp-rollout/templates/rollout-plan.md` — 記入式の展開計画・意思決定ログのテンプレート。
- `guides/inline-dlp-for-claude-enterprise.{en,ko,es,ja}.md` — 4 言語のアーキテクチャ・導入ガイド。

## 出典
- https://claude.com/blog/claude-enterprise-inference-hooks
