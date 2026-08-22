[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
Thariq Shihipar が、Claude 5 世代のモデルの登場でコンテキストエンジニアリングの何が変わったのかを説明する。出発点は一つの事実だ。Anthropic はこれらのモデル向けに Claude Code のシステムプロンプトの 80% 以上を削除し、コーディング評価で測定可能な性能低下はなかった。

診断は、従来のやり方が Claude に*足かせ*をはめていたというものだ。ルールはシステムプロンプト、CLAUDE.md ファイル、スキルという 3 つの層に積み上がり、やがて互いに矛盾しはじめた。ある層は「適切にドキュメントを残せ」と言い、別の層は「コメントを追加するな」と言う。新しいモデルはそうした足場なしでもユーザーの意図を読み取れるので、残るのは害の部分だけだ。記事は 6 つの「以前／いま」の転換を示し、続いて組み立てられたコンテキストの各層がいま実際には何のためのものかを定義し直す。

## どんなときに役立つか
- システムプロンプト、CLAUDE.md、スキルが長くなり、その一部が逆効果ではないかと疑うとき。
- コンテキストの 2 つの層が、同時には従えない指示を出しているとき。
- 以前の世代のモデルに合わせて調整したエージェントを移行するとき。
- ツールを例で教えるかシグネチャで教えるかを決めるとき。
- ツールの使用ガイドがシステムプロンプトとツール説明に重複しているとき。
- Claude が参照する仕様の形式を選ぶとき。

## 主なポイント
- Claude 5 モデル向けに **Claude Code のシステムプロンプトの 80% 以上が削除**され、コーディング評価で測定可能な損失はなかった。
- **ルール → 判断。**「デフォルトではコメントを書かない。複数段落の docstring や複数行のコメントブロックは決して書かない — 短い 1 行まで」が「周囲のコードのように読めるコードを書く: コメントの密度、命名、イディオムを周囲に合わせる」になった。
- **例 → インターフェース設計。** 使用例は新しいモデルを、その例がカバーする探索空間に縛りつける。代わりに表現力のあるパラメータと明確に列挙された選択肢にガイドを込める。
- **前もって全部 → プログレッシブディスクロージャ。** 毎リクエストですべての費用を払うのではなく、スキルと遅延読み込みツールでコンテキストを選択的に読み込む。
- **繰り返し → 一つのツール説明。** 以前のモデルは同じ指示がシステムプロンプトとツール説明の両方にあると恩恵を受けたが、いまのモデルはツール説明を確実に参照する。
- **手動メモリ → 自動メモリ。** `#` ホットキーでコンテキストを固定する方式は、作業とユーザーに関連するものを Claude が保持する方式に置き換わる。
- **単純な仕様 → 豊かなリファレンス。** HTML アーティファクト、コードリファレンス、テストスイート、ルーブリックは Markdown の計画書より少ない曖昧さで意図を伝える。
- **いま各層は一つの役割を持つ。** システムプロンプトはプロダクトのコンテキスト、CLAUDE.md は落とし穴に集中した軽量なファイル、スキルはチームの考え方を載せたオンデマンドのガイド、リファレンスは @メンションで持ち込む深さ（散文よりコードを優先）。
- Claude Code の **`/doctor`**（CLI では `claude doctor`）が、スキル、CLAUDE.md ファイル、システムプロンプトを Claude 5 モデル向けに自動で適正サイズに整える。

## 同梱リソース
- `skills/context-engineering-for-new-models/SKILL.md` — 矛盾を見つけ、6 つの転換を適用し、各層を書き直し、そして測定する。
- `skills/context-engineering-for-new-models/references/then-vs-now.md` — 6 つの転換すべてと、以前／いまの文言、その置き換えが効く理由。
- `skills/context-engineering-for-new-models/references/context-layers.md` — システムプロンプト、CLAUDE.md、スキル、リファレンスがいまそれぞれ何のためのものか。
- `skills/context-engineering-for-new-models/templates/lightweight-claude-md.md` — ルールブックに育ってしまった CLAUDE.md を戻すための目標形と、もうそこに置くべきでないもの。
- `skills/context-engineering-for-new-models/examples/rule-rewrites.md` — 4 つのビフォー／アフター: コメント規則、例で教えていたツール、重複した指示、Markdown の仕様。
- `guides/context-engineering-rules.{en,ko,es,ja}.md` — 4 言語での完全な解説。

## 出典
[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) — Thariq Shihipar、2026年7月24日。
