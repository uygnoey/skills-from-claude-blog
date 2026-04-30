[English](./verifiable-ai-for-finance.en.md) · [한국어](./verifiable-ai-for-finance.ko.md) · [Español](./verifiable-ai-for-finance.es.md) · **日本語**

# 金融リサーチのための検証可能なAI（要約ガイド）

## このガイドについて
Kepler のパターンを実務向けに要約したガイドです。Claude は解釈と曖昧さの扱いに集中し、決定論的なインフラが検証済みの検索・計算・プロビナンス・監査ログを担います。

## どんなときに役立つか
すべての数値が監査可能で、出典文書まで追跡できる必要がある規制環境向けのAIを構築するときに有用です。

## 主なポイント
- 正確性のために、確率的推論と決定論的実行を分離します。
- すべての出力にプロビナンス（文書 → ページ → 行項目）を持たせるよう設計します。
- ワークフローを段階に分解し、段階ごとにモデルを割り当てます。
- 構造化されたドメインコンテキストと自動評価パイプラインで信頼性を維持します。

## 出典
- https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude
