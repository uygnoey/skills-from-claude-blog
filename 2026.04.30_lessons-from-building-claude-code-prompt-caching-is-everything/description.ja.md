[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude Code を作って学んだこと:prompt caching こそすべて

## この記事について

Anthropic が 2026 年 4 月 30 日に公開した記事で、Claude Code チームの member of technical staff である Thariq Shihipar が、ハーネス構築の中で得た prompt caching の教訓を共有しています。prefix マッチングの仕組み、Claude Code が静的・動的コンテンツをどの順序で配置しているか、システムプロンプトをその場で書き換えるとなぜキャッシュが壊れるか、セッション中のモデル/ツール変更がなぜ危険か、Plan Mode や tool search がキャッシュを壊さずに動く仕組み、そして compaction が cache-safe forking としてどう実装されているかを解説し、最後にエージェント構築者が再利用できる 5 つのパターンにまとめています。

## どんなときに役立つか

- 長時間動作する agent を構築・運用しており、prompt cache hit rate を高く保つことが目標のとき。
- コード変更後にキャッシュ命中率が落ちた回帰をデバッグしているとき(タイムスタンプ、ツール順序、パラメータ調整など)。
- Plan Mode のように「ツールセットを切り替えたくなる」機能を設計中で、cache-safe な代替が必要なとき。
- compaction や要約を実装中で、親の prefix キャッシュを共有して uncached input 料金を回避したいとき。
- cache hit rate に対する SLO・アラート設計の参考が欲しいとき。

## 主なポイント

- prompt caching は prefix match — prefix のどこかが変わると、それ以降がすべて無効化されます。
- Claude Code ハーネスの配置:静的 system prompt + ツール(グローバルキャッシュ)→ CLAUDE.md(プロジェクト内キャッシュ)→ セッションコンテキスト(セッション内キャッシュ)→ 会話メッセージ。
- キャッシュ順序が壊れる典型例:静的 system prompt にタイムスタンプを入れる、ツール定義の順序が非決定的、ツールのパラメータ変更。
- 動的情報(現在時刻、ファイル変更など)はメッセージで渡す — Claude Code は次の user message または tool result に `<system-reminder>` タグを付与し、system prompt を書き換えません。
- セッション中のモデル変更は禁止。Opus で 100k トークン進めた時点で Haiku に切り替えると、Haiku 用キャッシュをゼロから再構築する必要があり、Opus にそのまま答えさせるより高くつきます。やむを得ず切り替えるなら、subagent に hand-off メッセージを準備させる — Claude Code は Haiku を使う Explore agent でこのパターンを採用しています。
- セッション中のツール追加・削除は絶対禁止。Plan Mode は全ツールを残したまま EnterPlanMode/ExitPlanMode をツールとして提供します。tool search は `defer_loading: true` のスタブを使い、ツールを取り除く代わりに遅延ロードします。
- compaction は cache-safe forking として実装されます:親と同じ system prompt、ユーザー/システムコンテキスト、ツール定義に、compaction プロンプトを末尾の新しい user message として追加します。コンテキストウィンドウには "compaction buffer" を確保します。compaction は API に組み込み済みです。
- チームは cache hit rate を uptime と同じレベルで監視し、低下し過ぎたら SEV を宣言します。

## 同梱リソース

- Skill: `skills/agent-prompt-caching-best-practices/SKILL.md` — prefix を安定させるための実行可能なルールと設計パターンをチェックリスト形式に整理。
- リファレンス: `skills/agent-prompt-caching-best-practices/references/lessons-from-claude-code.md` — 記事の教訓を原文どおりに引用したリファレンス(レイアウト、メッセージでの更新、モデル/ツールの安定性、cache-safe forking、5 つのパターン要約)。
- 例: `skills/agent-prompt-caching-best-practices/examples/cache-safe-feature-design.md` — 記事から具体例を整理(ツールとしての Plan Mode、tool search の defer_loading、cache-safe forking としての compaction)。

## 出典

Lessons from building Claude Code: Prompt caching is everything — Anthropic(Thariq Shihipar)、2026 年 4 月 30 日: <https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything>
