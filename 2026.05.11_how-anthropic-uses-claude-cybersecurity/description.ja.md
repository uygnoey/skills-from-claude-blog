[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Anthropic セキュリティチームが Claude Code で脅威検知プラットフォームを作った話

## この記事について

2026 年 5 月 11 日に Anthropic の Detection Platform Engineering チームのテクニカルリード Jackie Bow が公開したケーススタディです。チームが構築した **CLUE(Claude Looks Up Evidence)** — CLUE Triage と CLUE Investigate という 2 つのサーフェスからなる検知・対応プラットフォーム — が Claude を自然言語インターフェースとして Anthropic 内部システム上で動く仕組み、計測したインパクト(誤検知率、クエリ・tool call 数、削減時間)、そして SOAR 的なスクリプトプレイブックから「Claude に境界だけ与え、調査経路は任せる」哲学へとシフトした経緯をまとめています。

## どんなときに役立つか

- 防御側セキュリティチームが、自社 SIEM と内部システムの上に Claude 駆動のトリアージ・調査サーフェスを載せるか判断するとき。
- 決定的プレイブックとエージェント主導の調査との境界、そしてエージェントが読めるデータガバナンスのスコープを設計するとき。
- 社内検知プラットフォームのビジネスケース(アラート量、誤検知低減、削減時間、低信頼シグナルのカバレッジ)を整理するとき。
- 組織のコンテキスト(Slack、社内ドキュメント、データウェアハウス、コードリポジトリ)をセキュリティエージェントへ tool として接続する設計を描くとき。

## 主なポイント

- CLUE Triage は入ってくる全アラートに対して一次トリアージを実施し、Slack・社内ドキュメント・コード・データウェアハウスからのコンテキストでエンリッチ。アナリストは disposition と confidence score を受け取る。
- CLUE Investigate は自然言語クエリインターフェース。Claude がエージェンティックループで動き、オーケストレーターがサブエージェントへ並列にクエリを発行し、結果を統合して調査サマリーにまとめる。
- 報告されたインパクト: 誤検知率が **約 3 分の 1 から 7%** へ。30 日で **約 12,000 クエリと 27,000 tool call** を自動化、**約 1,870 時間(234 人日)** の手作業を削減し、**5〜10 倍**の時間削減。調査 1 件あたり平均約 25 tool call・11 クエリ。
- Claude Code を「デザインパートナー兼コラボレーター」として活用。PoC は 1 日、設計と実装は 1 週間。
- 哲学: 境界(触れる tool とデータ)はコード化するが戦略はオープンに残す。Claude は人間が事前に書いておかなかった調査経路をしばしば見つける。
- 今後の方向: アラート応答から継続的なプロアクティブハンティングへ、調査トランスクリプトの集合体を組織の記憶として、そして複数の調査戦略を並列に走らせ結果を比較することで非決定性を受け入れる。

## 同梱リソース

- `skills/clue-style-detection-platform-playbook/SKILL.md` — CLUE スタイルの検知プラットフォーム設計(サーフェス、エージェンティックループの形、コンテキストソース、メトリクス、ガバナンス)のプレイブック。
- `skills/clue-style-detection-platform-playbook/references/clue-architecture-from-post.md` — 本文中で言及されたコンポーネント・メトリクス・引用の逐語カタログ。
- `skills/clue-style-detection-platform-playbook/examples/data-governance-investigation.md` — 本文の契約者データガバナンスのシナリオに沿ったワーキングサンプル。

## 出典

- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity) (Anthropic ブログ、2026 年 5 月 11 日)
