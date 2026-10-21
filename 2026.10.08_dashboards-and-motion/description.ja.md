[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
2つのベータと1つの正式リリースを発表する記事です。Claude Dashboards(ベータ、有料プラン)は、社内データ
についての自然文の質問を、常に最新に保たれるダッシュボードに変えます。Claude Motion(ベータ、Team・
Enterprise)は、アイデアやレポートを編集可能なコードで作られたアニメーション解説に変えます。Claude Docs、
Slides、Design はベータを終え、Free を含む全プランで利用可能になり、単独の Claude Design サイトは Claude
本体に統合されます。

## どんなときに役立つか
- チケットを切ったり SQL を書いたりせずに、データウェアハウスや CRM から素早く答えを得たいとき。
- アイデアを静的なスライドよりも短いアニメーションで伝えたほうがよいとき。
- Enterprise 管理者がこれらの機能を有効化する、または Claude Design のデザインシステムを移行するとき。

## 主なポイント
- Dashboards は Amazon Redshift、BigQuery、ClickHouse、Databricks、Snowflake のほか、Salesforce などの
  コネクタに接続できます。数値をクリックするとクエリが見え、各チャートに最終更新時刻が表示されます。
- より深い分析には、ダッシュボードを Amplitude、Grafana、Hex、Mixpanel、Omni、Perplexity、PostHog、
  Sigma に送れます(Databricks Genie、Looker、monday.com、Tableau は近日対応)。
- Motion はテキスト・チャート・図形・画像を動かすコードを書きます。MP4 でダウンロードするか、Adobe、
  Descript、HeyGen、Higgsfield、invideo、Luma AI、Runway で開けます。動画生成モデルは使わないため、生成
  映像や AI 生成の人物はありません。
- Docs、Slides、Design(作成数4,500万超)が正式リリース:アーティファクトの CMEK、管理者が選ぶテンプ
  レート、共同編集、許可されていれば社外・リンク共有、書式を保つ PowerPoint/PDF 出力、編集可能な Google
  Slides 出力、モバイルでの編集。
- 単独の claude.ai/design は12月14日まで残ります。Artifacts ページからチームのデザインシステムを移行して
  ください。単独版のチャット・コメント・公開リンクは終了とともに使えなくなります。
- Enterprise:Dashboards と Motion は既定でオフ(Organization settings > Artifacts)、Docs・Slides・Design
  は10月15日に既定でオンになります。

## 同梱リソース
- Skill:`live-dashboards-and-motion` — 検証できるライブダッシュボードと、コードで作るアニメーション解説の
  作り方。スタータープロンプトは `examples/prompts.md`。
- Guide:「Dashboards・Motion の展開と Claude Design の移行」(4言語)。

## 出典
- https://claude.com/resources/articles/dashboards-and-motion
