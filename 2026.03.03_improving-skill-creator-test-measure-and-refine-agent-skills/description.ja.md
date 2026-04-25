[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について

この投稿は、Agent Skills の作者がスキルをテストし、測定し、改善し続けられるようにする「skill-creator」の更新を発表し、モデルの進化に合わせてスキルを保守できるようにする仕組みを説明します。

## どんなときに役立つか

スキルを長期運用しながら、回帰（regression）の早期検知、改善の測定、バリアントの比較、そして必要なときに確実に発火するための説明文の調整を行いたい場合に役立ちます。

## 主なポイント

- スキルを「capability uplift（能力向上）」と「encoded preference（好み・手順のエンコード）」の 2 種類に分けて説明します。
- skill-creator は、テスト用プロンプト（必要ならファイルも）と「良い結果の定義」を用意することで evals（テスト）を作成・実行できるようにします。
- evals は、モデル変更による品質回帰を検知し、capability uplift スキルがベースモデルに追いつかれたかどうかの判断にも役立ちます。
- benchmark モードは標準化された評価を実行し、合格率、経過時間、トークン使用量を追跡します。
- マルチエージェント対応により、クリーンなコンテキストで evals を並列実行し、各実行は独立したトークン/時間メトリクスを持ちます。
- comparator agent により、スキルあり/なし、または 2 つのスキル版をブラインド A/B 比較できます。
- 説明文の分析に基づき、誤発火（false positive）と未発火（false negative）を減らす編集提案を行います。

## 同梱リソース

- Skill: evals・ベンチマーク・説明文調整で Agent Skills を保守するための実践的プレイブック。
- Reference: capability uplift と encoded preference の定義。

## 出典

- https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
