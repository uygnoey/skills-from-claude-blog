[English](./google-workspace-rollout.en.md) · [한국어](./google-workspace-rollout.ko.md) · [Español](./google-workspace-rollout.es.md) · **日本語**

# Claude for Google Workspace の導入

Google ドキュメント、スプレッドシート、スライドで Claude を使う方法は 2 つあります。このガイドでは、
個人ユーザーと組織それぞれの設定方法をまとめます。

## 2 つの使い方

| | アドオン(サイドバー) | コネクタ(チャットから) |
|---|---|---|
| 起点 | 開いている Google ファイル | Claude の会話 |
| 向いている作業 | 目の前のファイルの編集、選択範囲での作業 | 新規ファイル、複数ファイルにまたがる作業 |
| 状態 | パブリックベータ、すべての有料 Claude プラン | ベータ |
| ファイルアクセス | 既存の Google 共有権限に従う | 既存の Google 共有権限に従う |

アドオンも通常の Claude と同じモデル・コネクタ・スキルを使います。

## 個人の設定
1. Google Workspace Marketplace から Claude をインストールします。
2. ドキュメント、スプレッドシート、スライドを開き、拡張機能 > Claude > Open Claude を選びます。
3. 編集モードを選びます。**Ask before edits**(既定。変更ごとに承認カード)または
   **Accept all edits**(止まらずにそのまま適用)。
4. チャットから作業する場合は、Google Docs・Sheets・Slides のコネクタを有効にし、ファイルのリンクを
   貼るか新しいファイルを依頼します。

## 組織での導入
1. **アドオンを配布**: Google 管理コンソールからドメイン全体または選択したグループに配布します。
2. **コネクタを有効化**: Team・Enterprise プランでは、オーナーまたはプライマリオーナーが先にコネクタを
   有効にする必要があります。
3. **エンタープライズ管理を確認**: Compliance API、顧客管理の暗号鍵、OpenTelemetry 監査エクスポートは
   アドオンにも適用されます。
4. **チームごとの既定の編集モードを決める**(例: 共有ファイルでは "Ask before edits" を維持)。記事の
   要件ではなく、推奨される運用です。
5. **再利用できる形式はスキルとして共有**し、チームの成果物をそろえます(例: レビュー用デッキの形式)。

## 注意点
- どちらもベータです。
- 記事はバージョン履歴や取り消しについて触れていません。ヘルプセンターの設定ガイドを参照してください。

## 出典
- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides
