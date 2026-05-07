[English](./m365-collaboration.en.md) · [한국어](./m365-collaboration.ko.md) · [Español](./m365-collaboration.es.md) · **日本語**

# Claude を使った Microsoft 365 アプリ横断ワークフロー

## この記事について
Excel・PowerPoint・Word・Outlook で Claude と協働しながら、単一の会話コンテキストを維持して作業をつなぐための短い実践ガイドです。

## 推奨ワークフロー
1. **メール → 添付 → 分析 → 文章化 → スライド**
   - Outlook で依頼内容を把握します。
   - 添付を Word/Excel で開き、依頼の文脈を保ちます。
   - Excel で分析し、Word で文章を作り、PowerPoint でスライド化します。

2. **成果物を並べて開く**
   - 可能なら、スプレッドシート／メモ／デッキを同時に開いて進めます。
   - 前提が変わったら、グラフと文章内の参照箇所を更新します。

3. **Outlook の下書きを「最後の工程」にする**
   - 返信や予定招待は Claude に下書きを作らせます。
   - 送信前に必ず人が確認します。

## 管理者向けの考慮事項（エンタープライズ）
- 展開は Microsoft の管理機能および AppSource の一覧から行えます。
- 組織は OpenTelemetry による可観測性や Analytics API による利用状況レポートを設定できます。

## 出典
- https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
