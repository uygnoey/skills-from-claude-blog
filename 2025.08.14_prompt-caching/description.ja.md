[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude のプロンプトキャッシング

## この記事について

Anthropic API におけるプロンプトキャッシングのローンチ記事です。どのような場面でキャッシングが効くか、ローンチ時のモデルラインナップ（Claude 3.5 Sonnet、Claude 3 Opus、Claude 3 Haiku）、3 つのリファレンスワークロードでの公開されたレイテンシ／コスト削減数値、価格モデル（キャッシュ書き込みは基本 input より +25%、キャッシュ読み込みは基本 input の 10%）、Notion の顧客事例を取り上げます。2024 年 12 月 17 日のアップデート注記で、Anthropic API では **GA**、Amazon Bedrock と Google Cloud Vertex AI では **プレビュー** となったことが追記されています。

## どんなときに役立つか

- 既存の Claude 連携でプロンプトキャッシングが正しいレバーか（プロンプト短縮・ストリーミング・バッチング・モデル変更との比較）を判断するとき
- 記事の 3 つのベンチマークに似たワークロードでレイテンシ／コスト効果を見積もりたいとき
- キャッシュヒットを最大化するプロンプト構造を設計するとき — 何をキャッシュ済み prefix に置き、何を動的のまま残すか
- 公開された数値（長プロンプトでコスト最大 90% 削減、レイテンシ最大 85% 削減、10 万トークンの「本との対話」ワークロードで TTFT 79% 改善）を引用するとき

## 主なポイント

- プロンプトキャッシングは API 呼び出しの間でよく使うコンテキストをキャッシュします。大きなコンテキストを 1 回送り、その後繰り返し参照する用途に使います。
- 主要数値: 長プロンプトで **コスト最大 90% 削減**、**レイテンシ最大 85% 削減**。ローンチ時点では Claude 3.5 Sonnet、Claude 3 Opus、Claude 3 Haiku で public beta（原文時点）、2024-12-17 アップデートで GA。
- 記事に列挙されたユースケース: 会話エージェント、コーディングアシスタント、大規模文書処理、詳細な指示セット（数十件の高品質な例を含む）、エージェント的検索・ツール利用、書籍／論文／ドキュメント／ポッドキャストとの「対話」体験。
- 記事に登場するリファレンスワークロード:
  - 本との対話（10 万トークンのキャッシュ済みプロンプト）: TTFT 11.5s → 2.4s（-79%）、コスト -90%。
  - Many-shot prompting（1 万トークンプロンプト）: TTFT 1.6s → 1.1s（-31%）、コスト -86%。
  - マルチターン会話（長い system prompt + 10 ターン）: TTFT 約 10s → 約 2.5s（-75%）、コスト -53%。
- 価格モデル: キャッシュへの書き込みは各モデルの基本 input の **+25%**、キャッシュからの読み出しは基本 input の **10%**。
- 顧客事例: Notion が Notion AI の機能にプロンプトキャッシングを採用し、内部運用最適化と応答性向上を実現。Simon Last（Notion 共同創業者）コメント: "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality."
- 2024-12-17 アップデート: Anthropic API で **GA**、Amazon Bedrock と Google Cloud Vertex AI で **プレビュー**。

## 同梱リソース

- [skills/prompt-caching-design-patterns/SKILL.md](./skills/prompt-caching-design-patterns/SKILL.md): 使うべき場面、キャッシュヒットを狙うプロンプト構造、効果見積もりの方法
- [references/use-cases-and-benchmarks.md](./skills/prompt-caching-design-patterns/references/use-cases-and-benchmarks.md): ローンチ時のユースケース一覧とリファレンスワークロード表をそのまま転載
- [examples/prompt-structure-patterns.md](./skills/prompt-caching-design-patterns/examples/prompt-structure-patterns.md): キャッシュ済み prefix と動的 suffix のパターン例

## 出典

[Prompt caching with Claude](https://claude.com/blog/prompt-caching)（公開 2025-08-14、2024-12-17 アップデートで Anthropic API GA + Bedrock・Vertex AI プレビュー）より抽出。
