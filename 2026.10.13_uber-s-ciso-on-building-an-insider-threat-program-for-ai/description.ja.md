[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Uber の CISO、Philip Martin へのインタビューです。企業が従業員向けにすでに運用している内部脅威（insider
threat）プログラムが AI エージェントにも必要な理由、フロンティアモデルがセキュリティ業務をどう変えるか、
そして Uber のオープンソースツール AI Detection and Response（ADR）が Anthropic の Enterprise Frontier
Safeguards とどう連携するかを語っています。

## どんなときに役立つか
- 社内の AI エージェント向けに監視・検知・対応の仕組みを設計するとき。
- 自社のエージェントテレメトリーとモデル提供元のセーフガードシグナルを組み合わせるとき。
- AI システムのセキュリティで、防御側が次に注力すべき点を決めるとき。
- フロンティアモデルの導入に監視が必要な理由を経営層に説明するとき。

## 主なポイント
- フロンティアモデルは長い時間軸で大量のコンテキスト（コード、設計文書、Jira の課題、サービスの履歴）を
  取り込み、非常に具体的な脅威モデルやセキュリティレビューを生成できます。Martin はサービスごとの
  エージェントが互いに脅威モデルをやり取りする未来を想定しています。
- Enterprise Frontier Safeguards：Uber はデータの管理権（許可なく Anthropic はアクセス不可）と、
  セーフガード発動後の対応の決定権を保持します。
- Uber の AI セキュリティアーキテクチャ：境界としての LLM ゲートウェイ、エージェントハーネスでリアルタイムに
  テレメトリー収集と対応を行うオープンソースの ADR、検知環境に統合される提供元の分類器出力。
- 優先事項 1：リアルタイムの検知と介入。人がプロンプトを入力し、モデルがツールを呼び出す瞬間にできるだけ近づく。
- 優先事項 2：新たなパターンの理解。新しい挙動を発見し、セーフガードを作り、繰り返す（制約が新しい挙動を生む）。
- どの企業も人に対して内部脅威プログラムを運用しています。モデルも同じリスクをもたらすため、同等の仕組みが必要です。

## 同梱リソース
- Skill：`ai-insider-threat-program` — 階層型アーキテクチャ、リアルタイム介入、挙動発見ループ
  （`references/ai-security-architecture.md`）。
- Guide：「AI エージェントを内部者のように守る」（4 言語）。

## 出典
- https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
