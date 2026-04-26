[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Making Claude a better electrical engineer

## この記事について
この記事は、Anthropic が Diode Computers と協力し、Zener 言語で PCB のリファレンス設計を生成する Claude の能力を改善した取り組みを説明します。

## どんなときに役立つか
専門家と協業し、ベンチマークを作り、失敗パターンを反復的に改善することで、特定ドメインでのモデル性能を高めたい場合に役立ちます。

## 主なポイント
- 具体的なエージェント型タスクと、ドメイン基準で成否を判定する評価ハーネス（テストベンチ）を定義します。
- 専門家のフィードバックで典型的な失敗モードを特定し、評価基準を洗練します。
- 部品の厳密一致よりも、『最低容量』など要件ベースのチェックを優先します。
- ベースラインモデルとのブラインド比較で改善を検証します。

## 同梱リソース
- Skill: skills/domain-partnership-benchmarking/SKILL.md

## 出典
- https://claude.com/blog/making-claude-a-better-electrical-engineer
