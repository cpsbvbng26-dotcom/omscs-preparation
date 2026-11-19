# omscs-preparation

[English](./README.en.md)

Georgia Tech の OMSCS（Online Master of Science in Computer Science）に出願するための準備を、日付つきで残す記録です。
決めたことと、したことだけを書きます。
これからの作業の一覧は置きません。

## 2026-11-19 に決めたこと

- 学士号を得たあと、Georgia Tech の OMSCS（Online Master of Science in Computer Science）で修士号を取ることを目指します。
- Georgia Tech が自分で出している MOOC を、月に 1 本ずつ受けます。
- 最初の MOOC は、edX の Computing in Python I: Fundamentals and Procedural Programming です。
- 評価を受ける課題は、AI を使わずに仕上げます。
- AI は、概念の説明を受けるためにだけ使います。

修士号の目標は、プロフィールの頁の目標の表と同じです。
その表の源は、`researcher-profile` の `site.json` の `aims` です。
MOOC の進め方と AI の使い方は、2026-11-19 に利用者が決めました。
MOOC の進め方と AI の使い方は、同じ日の `site.json` には書かれていません。
決めたことの元の文は、[data/progress.json](./data/progress.json) の最初の行にあります。

## 出願の要件

要件は、[data/requirements.json](./data/requirements.json) に行ごとに置いてあります。
どの行も、出典の URL、読んだ日、状態、確かめ方を持ちます。
状態は、次のどれかです。

| 状態 | 意味 |
| --- | --- |
| 公式の頁で確かめた | 公式の頁を開いて読んだ |
| 公式の頁の検索結果から | 検索の結果に出た要約か抜粋で読んだ。頁は開いていない |
| 第三者の頁から | 公式でない頁で読んだ |
| 確かめていない | 出典が読めていない |

omscs.gatech.edu は、この作業の環境から届きません。
そのため、公式の頁で確かめた行はありません。
要件の行は 13 行です。

| 行 | 要件 | 状態 |
| --- | --- | --- |
| degree | 入学までに学士号を得ていること。教育の年数は 16 年以上 | 公式の頁の検索結果から |
| field-and-gpa | 計算機科学か近い分野の学士号と、累積 GPA 3.0 以上が望ましい（必須ではない）。満たさない出願は一件ずつ判断される | 公式の頁の検索結果から |
| recommenders | 推薦者が 3 人 | 公式の頁の検索結果から |
| resume | 履歴書（résumé）。出さなければ出願は評価されない | 公式の頁の検索結果から |
| supplemental-questions | 補足の質問への答え。自由記述には字数の上限があり、最後の 8 問は確認の質問 | 公式の頁の検索結果から |
| english-test | 留学生には TOEFL か IELTS-Academic の点が要る。点は出願を終えるときまでに出す | 公式の頁の検索結果から |
| english-minimum | Georgia Tech の大学院の最低点は、TOEFL iBT で合計 90 以上かつ各技能 19 以上、または IELTS で総合 7.0 以上 | 公式の頁の検索結果から |
| english-old-faq | 古い OMSCS の FAQ は、TOEFL 100 と書いていた | 確かめていない |
| toefl-scale | TOEFL の点の尺度が 2026 年 1 月に変わった | 公式の頁の検索結果から |
| deadline-fall | 秋の入学の出願の締め切りは 3 月 1 日 | 公式の頁の検索結果から |
| deadline-spring | 春の入学の出願の締め切りは 8 月 15 日 | 公式の頁の検索結果から |
| conditional-admission | 入学は条件付き。入学から 1 年のうちに、基礎の科目 2 つを B 以上で終えると、正式の入学になる | 公式の頁の検索結果から |
| preparation-by-application | 勧められた準備は、出願を出すときまでに終えていることが期待される。MOOC だけでは、STEM の学士号の無い人には足りることがまれ | 公式の頁の検索結果から |

出典の URL と確かめ方は、行ごとに `data/requirements.json` にあります。

## 勧められている科目

[data/courses.json](./data/courses.json) に、Preparing Yourself for OMSCS の頁が勧める科目を並べています。
科目は 13 本です。
URL を置いたのは、確かめた頁だけです。
いま確かめてあるのは、[Computing in Python I の edX の頁](https://edx.org/es/learn/python/the-georgia-institute-of-technology-computing-in-python-i-fundamentals-and-procedural-programming)だけです。

## 進み具合の記録

[data/progress.json](./data/progress.json) に、日付の順に足していきます。
いまあるのは、2026-11-19 に決めたことだけです。
済んだこととして書いた行の日付が、検査を走らせた日より後なら、検査が落ちます。

## 書かないもの

成績・点・GPA など、個人の学業の記録は書きません。
所属も書きません。
要件の行にある GPA は、出願の要件の文であって、運営者の記録ではありません。

## 運営者

運営者は、根本卓哉（Takuya Nemoto）です。
ORCID iD は [0009-0000-1406-0547](https://orcid.org/0009-0000-1406-0547) です。

## 誤りの知らせ

[誤りの知らせ](https://github.com/cpsbvbng26-dotcom/omscs-preparation/issues/new?template=error-report.yml)の様式で受けます。
安全の問題は、[SECURITY.md](./SECURITY.md) の入口で受けます。

## 検査

```
python3 verification/check.py           # 要件・科目・記録・書き方・写し
python3 verification/check.py --break   # 検査を一つずつ壊し、落ちることを確かめる
```

## 言語モデルの使い方

このリポジトリの頁とコードは、運営者が求め、Claude Code（Anthropic）が書きました。
Claude は著者ではありません。
上の決めごとにある AI の使い方は、MOOC の課題についての決めごとで、この記録の書き方とは別のものです。

## ライセンス

文とデータは [CC BY 4.0](./LICENSE)、コードは [MIT](./LICENSE-CODE) です。
