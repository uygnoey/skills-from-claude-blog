[English](./computer-browser-use-best-practices.en.md) · [한국어](./computer-browser-use-best-practices.ko.md) · [Español](./computer-browser-use-best-practices.es.md) · **日本語**

# ガイド: Claude の computer use / browser use ベストプラクティス

このガイドは、Claude を用いた computer/browser use エージェントを信頼性高く構築するための推奨デフォルトとデバッグの要点をまとめます。

## 1) 画像サイズとスケーリング
- スクリーンショットは送信前にダウンスケールする。
- 単純な既定値は 1280×720。Opus 4.7 は 1080p から開始することが推奨される。
- 極端に低い解像度（< およそ 960×540）は避ける。
- 制限内で画質を最大化したい場合は、アスペクト比を維持した “max API fit” サイズを計算する。

## 2) 座標の正しさ
スクリーンショットをリサイズした場合は、API が返す座標をネイティブ画面座標へ再スケーリングしてからクリックを実行する。

## 3) メッセージの形式
メッセージ content 内では、テキスト指示を画像ブロックより前に置く。

## 4) 小さなターゲット
- 密な UI ではズームを有効化する。
- ターゲットが小さい場合はキーボード操作を優先する。
- 4K+ 画面では Opus 4.7（より大きい画像予算）を使うか、DPI/スケールを下げ、必要領域に絞ったスクリーンショットを検討する。

## 5) Thinking effort（computer use）
- Opus 4.7: 既定は `high`。スループット／コスト優先は `low`。非常に難しい一発勝負のみ `max` を検討。
- Claude 4.6: 既定は `medium`。スループット／コスト優先は `low`。単純フローで低遅延が最優先なら thinking 無効化を検討。

## 6) プロンプトインジェクション安全
- Web コンテンツは信頼しない。
- `computer_20251124` による内蔵分類器を優先する。
- 不可逆操作は人間の確認を必須にする。
- 権限を絞り、詳細ログを残す。

## 7) 長時間セッションのコンテキスト管理
記事の実用的なデフォルト例:
- 安定プレフィックスにキャッシュブレークポイント 1つ、直近のツール結果に 3つ。
- スクリーンショットをローリングバッファで整理（例: keep_n=3、約 25 枚ごとに整理）。
- 入力トークン約 150k 付近で、カスタムの compaction プロンプトを用いたサーバー側 compaction。

## 出典
https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
