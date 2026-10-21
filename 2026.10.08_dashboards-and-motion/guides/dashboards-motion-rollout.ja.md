[English](./dashboards-motion-rollout.en.md) · [한국어](./dashboards-motion-rollout.ko.md) · [Español](./dashboards-motion-rollout.es.md) · **日本語**

# Dashboards・Motion の展開と Claude Design の移行

2026年10月8日の発表に基づく、管理者・チームリード向けチェックリストです。

## 1. 提供範囲の早見表
| 機能 | 状態 | プラン | Enterprise の既定値 |
|---|---|---|---|
| Claude Dashboards | ベータ | 有料プラン | オフ(Organization settings > Artifacts) |
| Claude Motion | ベータ | Team、Enterprise | オフ(Organization settings > Artifacts) |
| Claude Docs、Slides、Design | 正式リリース | Free を含む全プラン | 10月15日から既定でオン(前倒しで有効化可) |

## 2. Dashboards を有効にする前に
- 接続するデータプラットフォーム(Amazon Redshift、BigQuery、ClickHouse、Databricks、Snowflake)と、
  ダッシュボードが使えるその他のコネクタ(例:Salesforce)を決めます。
- Dashboards は素早い探索的な質問向けと位置づけます。より深い分析が必要なときにダッシュボードを渡す BI
  ツールを合意しておきます(Amplitude、Grafana、Hex、Mixpanel、Omni、Perplexity、PostHog、Sigma。
  Databricks Genie、Looker、monday.com、Tableau は近日対応)。
- 検証の習慣を教えます:数値をクリックしてクエリを見る、Claude に説明させる、各チャートの最終更新時刻を
  確認する。

## 3. Motion を有効にする前に
- Motion は自分の仕事を説明するためのものです。テキスト・チャート・図形・画像をコードで動かします。動画
  生成モデルは使わないため、生成映像も AI 生成の人物もありません。
- 出力:MP4 ダウンロード、または Adobe、Descript、HeyGen、Higgsfield、invideo、Luma AI、Runway で開く
  (Canva、Captions は近日対応)。

## 4. アーティファクトで使えるようになった Enterprise 向け管理機能
- アーティファクトの CMEK 対応。
- 組織で使うアーティファクトテンプレートを管理者が選択。
- 組織外やリンクを知る全員への共有は、管理者が許可した場合のみ。

## 5. Claude Design の移行(期限:12月14日)
Claude Design は claude.ai/design で始まり、9月16日からはすべての Claude の会話内でも動作します。単独
サイトは12月14日まで残ります。
- [ ] **デザインシステムの移行。** Artifacts ページで「Migrate team design systems」をクリックします。
  1回の移行で組織のすべてのデザインシステムが移り、元データは終了まで単独版にそのまま残ります。
- [ ] **プロジェクト。** 現時点で対応は不要です。終了まで単独版で動き続けます。
- [ ] **チャットとコメントの保存。** 単独版にのみ残り、終了後は参照できません。
- [ ] **公開リンク。** 単独版プロジェクトへのリンクは終了とともに無効になるため、代替を用意します。
- 詳細は原文からリンクされている移行ガイドを参照してください。

## 出典
- https://claude.com/resources/articles/dashboards-and-motion
