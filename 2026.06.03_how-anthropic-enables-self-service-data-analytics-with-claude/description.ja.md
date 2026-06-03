[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# How Anthropic enables self-service data analytics with Claude

## この記事について
この記事は、Anthropic が Claude を使って社内のビジネス分析（アナリティクス）依頼の大半を自動化している方法と、分析の正確性が単なる SQL 生成の問題ではなく、**コンテキスト・検索（retrieval）・検証**の問題であることを説明します。

## どんなときに役立つか
データウェアハウスに基づく質問へ**信頼性高く**回答するエージェント型アナリティクス（分析コパイロット）を構築する際に役立ちます。特に、エンティティの曖昧さ、データの鮮度（staleness）、検索（retrieval）不足といった失敗を減らすガードレールが必要な場合に参考になります。

## 主なポイント
- アナリティクスはソフトウェア開発と異なり、多くの場合、データモデル内の**特定の最新エンティティ**に結びつく唯一の正解があります。
- 代表的な失敗モードは (1) 概念–エンティティの曖昧さ、(2) データの staleness（鮮度の問題）、(3) retrieval（検索）失敗です。
- Anthropic は、強いデータ基盤、明確なソース・オブ・トゥルース、手順知識を skills として整理すること、そして検証（オフライン評価＋オンライン監視）を組み合わせます。
- 付録に「warehouse skill」のスケルトンと、ドメイン別テーブル参照ドキュメントのスケルトンが含まれます。

## 同梱リソース
- 再利用可能な「warehouse skill」スケルトン（`skills/<skill-name>/SKILL.md` に適しています）。
- 再利用可能な参照ドキュメントのスケルトン（`skills/<skill-name>/references/*.md` に適しています）。

## 出典
- https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
