[English](./transition-roadmap.en.md) · [한국어](./transition-roadmap.ko.md) · [Español](./transition-roadmap.es.md) · **日本語**

# 移行ロードマップ

[What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding)（2025-12-01）から抽出した、短い組織レベルの移行ガイドです。単一チームを超えて Claude Code 導入を計画する際のチェックリストとして使います。

## 1. メッセージのフレーミング

オーディエンスに最も響くメリットを 2〜3 個選びます。

- エンジニアリングリーダーシップ: 期間短縮 + ヘッドカウントを線形に増やさないスケール
- エンジニアリングマネージャー: オンボーディング圧縮 + アクセスの民主化
- シニアエンジニア: 自律的問題解決 + 体系的なコード品質
- セキュリティ／プラットフォーム: 体系的なコード品質 + 権限モデル
- 採用: 民主化（採用戦略の変化 — 「基礎力 + エージェントが補う専門性」）
- 財務: 期間短縮をプロジェクト経済性に結びつける

## 2. エビデンスで裏付ける

- Augment Code の 2 週間 vs 4〜8 か月のエンタープライズ事例と、Guy Gur-Ari のコメント: "Tasks that would take weeks for a developer to learn can now be completed in a day or two."
- Grafana の自然言語 PromQL/LogQL アシスタント（アクセス民主化の事例）。

## 3. 一つのチームでパイロット

- 意欲あるシニアチャンピオンを擁するチームを 1 つ選ぶ。
- Claude Code をターミナル／IDE にインストールし、プロジェクトルートで `claude` を起動。
- 初手タスクを実行: エンドポイントへのエラーハンドリング、複雑コンポーネントのリファクタリング、未カバーコードのテスト作成。
- パイロット期間中はすべての変更で書き込み前承認を必須に。

## 4. パイロット終了基準を定義

2〜4 週間後、以下を評価:

- 割り当てタスクのサイクルタイムをパイロット前ベースラインと比較
- パイロット中に合流した新メンバーのオンボーディング所要時間
- 品質シグナル: インシデント、PR あたりのレビューコメント、捕捉できた欠陥
- エンジニア体験シグナル: 使い続けたいと感じているか

## 5. 慎重な拡張

- プロジェクトルートに CLAUDE.md を追加し、コーディング標準がセッション・コントリビューターを跨いで維持されるようにする。
- リポジトリ外のツール（イシュートラッカー・デザインシステム・社内ドキュメント）は MCP サーバー接続で統合。
- 責任範囲を定義する際、エージェントは自動操縦ではなく品質ゲートキーパー兼思考パートナーとして位置付ける。

## 6. 結果の追跡と共有

メリットをローカル指標に翻訳します。Augment Code の「2 週間 vs 8 か月」は記事のペーシング例にすぎないため、各チームが独自のサイクルタイム・オンボーディング時間・低減したトイル量などを公開し、リーダーシップがチーム間の採用判断を比較できるようにします。

## 出典

[What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding)（公開日：2025-12-01）。
