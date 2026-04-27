[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# 開発者 Console でより良いプロンプトを生成する

## この記事について

Anthropic が 2024 年 5 月 20 日に公開した発表では、Anthropic Console 内に短いタスク説明を入力するだけで本番運用可能なプロンプトテンプレートに変換してくれる prompt generator が紹介されています。この生成機能には、明確なロール設定、chain-of-thought のスクラッチパッド、曖昧な変数を囲む XML タグ、シンプルな変数のインライン記法といったプロンプトエンジニアリング技術があらかじめ組み込まれているため、新しいプロジェクトを始めるたびに開発者が手作業でこれらのパターンを適用する必要がありません。

## どんなときに役立つか

- Claude を活用した新機能の開発を始めたばかりで、しっかりとした初期プロンプトのドラフトが欲しいとき。
- チーム全体で一貫したテンプレートスタイルを保ちつつ、そのスタイルが Anthropic のプロンプトエンジニアリングのベストプラクティスを既に反映していてほしいとき。
- 既存のプロンプトを Console に移行する際に、比較対象となるベースラインが欲しいとき。
- 評価データセットを構築していて、固定された指示と例ごとの変数を明確に分離したいとき。

## 主なポイント

- 生成されるプロンプトには明示的なロール設定が含まれます(例:"You will be acting as a content moderator")。
- 複雑なタスクには、回答前に考えさせるための chain-of-thought `<scratchpad>` ブロックが組み込まれます。
- 曖昧で大きな変数は `<code>{{CODE}}</code>` のような XML タグで囲み、境界を明確にします。
- 短くシンプルな変数は `{{LANGUAGE}}` のようにインラインで参照できます。
- 変数は handlebars 記法を使うため、同じテンプレートを Console workbench や下流のツールにそのまま渡せます。
- 内部的には長い meta-prompt がまず構造を計画し、XML タグを出力の "spine" として使います。
- ZoomInfo が顧客事例として登場します。ZoomInfo の Principal Data Scientist である Spencer Fox は、わずか数日で MVP に到達し、プロンプト調整時間を 80% 削減できたと述べています。

## 同梱リソース

- Skill: `skills/prompt-template-bootstrap/SKILL.md` — 生成機能をいつ使うか、出力に既に含まれている技術、編集と評価の進め方。
- リファレンス: `skills/prompt-template-bootstrap/references/best-practices-from-post.md` — 記事が生成機能に組み込まれていると明記しているプロンプトエンジニアリング技術。
- 例: `skills/prompt-template-bootstrap/examples/template-fragments.md` — 記事が引用しているテンプレート断片(コンテンツモデレーターのロール、scratchpad 推奨、コード翻訳の XML、ZoomInfo の引用)。

## 出典

Generate better prompts in the developer Console — Anthropic、2024 年 5 月 20 日: <https://claude.com/blog/prompt-generator>
