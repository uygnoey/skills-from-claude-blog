[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Steering Claude Code: skills, hooks, subagents and more

## この記事について

この記事は、Claude Code の挙動を指示する方法を整理し、指示をどこに置くべきかを判断するためのフレームワークを示します。

## どんなときに役立つか

Claude Code をカスタマイズする際に、コンテキストコスト、長いセッションでの持続性（compaction）、指示の権限（重み）を踏まえて配置を決めたいときに役立ちます。

## 主なポイント

- 7つの方法: CLAUDE.md、Rules、Skills、Subagents、Hooks、Output styles、system prompt の append。
- 各方法は、ロードタイミング、compaction 時の挙動、コンテキストコストが異なります。
- ルート CLAUDE.md は 200行未満に保ち、手順は skills に、制約は（path-scoped）rules に移すことを推奨しています。
- subagents は、途中経過をメインスレッドに残したくない隔離されたサイドタスクに向きます。
- hooks は決定的な自動化・強制のために使い、PreToolUse は exit code 2 でツール呼び出しをブロックできます。
- output styles は大きなロール変更にのみ使い、カスタム作成の前に組み込みスタイルを確認するよう勧めています。
- 複数の設定が揃ったら plugin として束ねて共有できると述べています。

## 同梱リソース

- 手法比較テーブル
- 例: paths 付き rule frontmatter、サブディレクトリ CLAUDE.md のロード挙動
- hook の種類とイベント（PreCompact, PreToolUse）

## 出典

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
