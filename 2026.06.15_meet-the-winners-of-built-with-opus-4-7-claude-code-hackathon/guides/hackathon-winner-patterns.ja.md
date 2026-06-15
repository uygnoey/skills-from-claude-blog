[English](./hackathon-winner-patterns.en.md) · [한국어](./hackathon-winner-patterns.ko.md) · [Español](./hackathon-winner-patterns.es.md) · **日本語**

## この記事ガイドについて
このガイドは、Claude の「Built with Opus 4.7」ハッカソン受賞者が共通して語った、構築と反復改善のパターンを短くまとめたものです。

## どんなときに役立つか
計画、並列化、評価、反復改善のための軽量なプレイブックが欲しいときに使います。

## 主なポイント
- 実装の前に、仕様と計画を先に作ります。
- コンポーネントを分割してコンテキストを整理（セッション分割）し、必要に応じてデバッグで複数エージェントを並列実行します。
- 次に進む前に、Claude に既存の成果物を監査（audit）してもらいます。
- 可能なら「評価（evals）優先」と、ドメイン特化の参照データの活用を検討します。

## 出典
- https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon
