[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
ライフサイエンス組織向けの実践的な導入ガイドである「Claude Science プロダクトガイド」の告知記事です。記事本体はガイドの要約であり、全文 PDF へリンクしています。

Claude Science（ベータ）は、ライフサイエンスのあらゆるデジタル工程のためのアプリケーションとして紹介されています。研究者のデータのすぐ隣で動作し、追跡・再現・説明が可能な結果を生み出すように作られています。ガイドでは、どの作業にどの Claude サーフェスを使うか、Claude Science の内部の仕組み、分析がレビューに耐えるための設計上の選択、3 フェーズの導入ロードマップ、機能別・ワークフロー別のユースケース、そして CIO と IT リーダー向けの FAQ を扱います。

## どんなときに役立つか
- 研究組織が、どの種類の科学業務（分析／文書作業／本番パイプライン）にどの Claude サーフェスが適合するかを決めるとき。
- 研究 IT が、科学者が管理対象データを扱う前にインストールの footprint、サンドボックス、ネットワーク許可リスト、計算ディスパッチ先をレビューする必要があるとき。
- 全社一斉有効化ではなく、計算系グループから段階的に展開を計画するとき。
- 論文・規制申請・社内レビューに向けて、結果が再現可能かつ説明可能である必要があるとき。

## 主なポイント
- **まずサーフェス選定から。** 分析・図・結果は Claude Science、素早い質問や下書きは Claude Chat、試験・申請レベルの文書作業は Claude Cowork と Claude for Microsoft 365、成果物が出荷されるソフトウェアなら Claude Code、組み込み・ホスト型エージェントは Claude Platform と Claude Managed Agents。多くの組織は複数を併用します。
- **データのある場所で動く。** macOS と Linux 上のローカルデーモン（ノート PC、ラボの Linux マシン、HPC ログインノード、クラウド VM）として動作し、UI はブラウザにあります。重いジョブは同じセッションから SSH ホスト、SLURM クラスタ（バッチディレクティブは自動生成）、サーバーレス GPU アカウントへディスパッチされます。
- **ドメイン能力は初日から利用できる**: 一般的な科学ワークフロー向けの設定可能な機能、60 を超える科学データベースへのオプション接続、約 150 のキュレーションされたスキル。スキルは文書を検索するのではなくコードを実行するため、1 つの分析の中で連鎖させられます。各スキルはオープンソースなので、クエリロジックの確認、バージョン固定、拡張が可能です。
- **分析をレビュー可能にする 5 つの設計上の選択**: 永続カーネル（エージェントは自分のプロットも見る）、すべての成果物に付く 4 層のプロベナンス（説明・コード・会話・環境スナップショット）、根拠にたどれない主張を指摘するバックグラウンドレビューアエージェント、実行前のプラン提示と可視化された権限モデル、そして組み込みのバイオセキュリティ保護。
- **3 フェーズのロードマップ**: Foundation（IT とデータガバナンスのレビュー、デーモンホストのパターン決定、2〜3 のチャンピオングループ、SSO/SCIM、管理者による有効化）、Pilot（実際のラボデータでの実分析、週次チェックイン、サイクルタイム・keep rate・コールド再現率の測定）、Scale（管理されたデーモンホストパターン、組織スキルカタログの整備、検証済み許可リスト、プロベナンス保持ポリシー）。
- **パイロットがうまくいっているサインは、チャンピオンが自分のスキルを保存し始めること**です。ラボ内部の正規化パイプラインや LIMS API を一度ラップしておけば、以降のすべてのセッションがそれを引き継ぎます。
- **スキルとコネクタの使い分け**: 答えが組織自身のシステムにあり、エンタイトルメントが問題になるならコネクタ。答えが公開された記録にあるなら科学データスキル。実際の問いの多くは両方を使います。
- **既知の制約は明示されています**: 研究用途であり臨床・診断の意思決定用ではない、GxP のバリデーション済みシステムではない、リリース時点で HIPAA 対応ではない、Windows 非対応、Bedrock・Vertex AI・Foundry 経由では提供されない、Zero Data Retention は適用外、NIH のアクセス制限データへの準拠はロードマップ上。

## 同梱リソース
- `skills/life-sciences-ai-rollout/SKILL.md` — AI 研究ワークベンチの段階的展開を計画・実行する方法。
- `skills/life-sciences-ai-rollout/references/surface-selection.md` — どの業務にどのサーフェスを使うかのプロダクトマトリクス。
- `skills/life-sciences-ai-rollout/references/product-architecture.md` — ローカルデーモン、計算ディスパッチ、5 つの設計上の選択。
- `skills/life-sciences-ai-rollout/references/scientific-data-skills.md` — 答える問いの種類ごとにまとめたスキルカタログ。
- `skills/life-sciences-ai-rollout/references/it-security-faq.md` — CIO・IT リーダー向け FAQ。
- `skills/life-sciences-ai-rollout/templates/adoption-roadmap.md` — フェーズ別展開計画のテンプレート。
- `skills/life-sciences-ai-rollout/templates/pilot-scorecard.md` — パイロット測定シート。
- `skills/life-sciences-ai-rollout/examples/workflow-use-cases.md` — 探索・分析・発表の各段階のユースケース。
- `guides/life-sciences-deployment.{en,ko,es,ja}.md` — 4 言語の完全な導入ガイド。

## 出典
- https://claude.com/blog/the-claude-science-product-guide
