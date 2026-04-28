[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# アップグレードされた Anthropic Console でより早く本番運用へ

## この記事について

Anthropic が 2025 年 3 月 6 日に公開した発表では、再設計された Anthropic Console を、Claude を用いた AI デプロイメントをチームで構築・テスト・反復する一つの場所として紹介しています。4 つのプロンプトエンジニアリングツール(Workbench、自動プロンプト生成、横並び比較による評価、プロンプト改善)、職能横断のコラボレーションのための共有可能プロンプト、最新モデル Claude 3.7 Sonnet のサポート、そして extended thinking budget の制御機能が取り上げられています。

## どんなときに役立つか

- 新しいプロンプトを本番環境へ持っていく際に、場当たり的な試行錯誤ではなく構築 → テスト → 反復の構造化されたループを作りたいとき。
- 開発者、ドメインエキスパート、プロダクトマネージャー、QA など複数の役割が、ドキュメントやチャットでのコピペなしに同じプロンプトを共同編集したいとき。
- 他の AI モデル向けに書かれたプロンプトを Anthropic のプロンプトエンジニアリング技術で書き直したいとき。
- Claude 3.7 Sonnet の extended thinking を導入し、thinking トークンの予算を明示的に管理したいとき。

## 主なポイント

- Workbench はプロンプトの構造化、例示の追加、外部ツールの統合を、対話的に API 呼び出しをテストできる環境で行えます。
- プロンプト生成機能はタスク説明から、chain-of-thought のような技術を使ったプロンプトを生成します。
- 評価ツールはテストケースを自動生成し、出力を横並びで比較してレスポンスの品質を採点します。
- プロンプト改善ツールは既存のプロンプト(他の AI モデル向けに書かれたものも含む)を洗練します。
- "Get Code" ボタンを押すと、すぐにデプロイできる本番品質の API 呼び出しコードを出力します。
- 共有可能プロンプトにより、チーム全体が同じプロンプトライブラリを共有し、標準化できます。
- Claude 3.7 Sonnet をサポートし、extended thinking のための最大 thinking トークン予算も設定できます。

## 同梱リソース

- Skill: `skills/console-build-test-iterate-workflow/SKILL.md` — 記事が説明する構築 → 評価 → 改善 → デプロイのループと、共有可能プロンプトおよび extended thinking budget の使い方ガイド。
- リファレンス: `skills/console-build-test-iterate-workflow/references/console-tools-from-post.md` — 記事で挙げられている Console のツールと機能の整理。
- 例: `skills/console-build-test-iterate-workflow/examples/team-collaboration-scenarios.md` — 記事に登場するコラボレーター役割をもとにした共有可能プロンプトのシナリオ。

## 出典

Get to production faster with the upgraded Anthropic Console — Anthropic、2025 年 3 月 6 日: <https://claude.com/blog/upgraded-anthropic-console>
