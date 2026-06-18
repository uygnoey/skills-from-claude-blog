[English](./steering-claude-code.en.md) · [한국어](./steering-claude-code.ko.md) · [Español](./steering-claude-code.es.md) · **日本語**

# Claude Code を steer するための判断フレームワーク

## 概要

Claude Code には指示を置ける場所が複数あり、ロードタイミング、compaction、コンテキストコスト、権限（重み）がそれぞれ異なります。

## 7つの方法

この記事は、CLAUDE.md、Rules、Skills、Subagents、Hooks、Output styles、system prompt の append を扱います。

## 実践ガイド

- ルート CLAUDE.md は 200行未満に保ち、owner を決めてコードのようにレビューします。
- フォルダ固有の慣習はサブディレクトリ CLAUDE.md に置きます。
- 制約は rules に置き、可能なら paths 付きでスコープします。
- 手順（デプロイ、リリースチェックリスト、レビュー手順）は skills に置きます。
- 中間結果をメインスレッドに残したくないサイドタスクは subagents に分離します。
- 決定的な自動化・強制は hooks を使います。
- output styles は大きなロール変更にのみ使い、カスタムの前に組み込みスタイルを確認します。
- append-system-prompt は 1回限りの追加指示（トーン/フォーマット）に使います。

## 出典

- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
