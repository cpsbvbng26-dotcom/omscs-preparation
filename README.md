# omscs-preparation

[English](./README.en.md)

大学院への進学の準備を、日付つきで残す記録です。
Georgia Tech の OMSCS（Online Master of Science in Computer Science）に出願するための準備を記録しています。
2026-11-20 からは、University at Buffalo の応用オントロジーの博士課程（PhD in Applied Ontology）の準備も記録しています。
2026-11-26 からは、博士号を得たあとに、研究を続けながら同時に並行して取る MBA の計画も記録しています。
リポジトリの名は、最初の目標の OMSCS のままです。
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

omscs.gatech.edu は、2026-11-19 にはこの作業の環境から届きませんでした。
2026-11-20 に、網の設定が omscs.gatech.edu と grad.gatech.edu を通すようになりました。
同じ日に、Georgia Tech の Bursar の学費の頁（bursar.gatech.edu）も開いて読みました。
その日に開いて読んだ頁は 7 つです。
公式の頁で確かめた行には、その頁の英語の文を一字一句そのまま添えてあります。
要件の行は 24 行です。
公式の頁で確かめた行は 24 行です。
前の版の degree の行にあった教育の年数の下限は、読んだどの頁にもありませんでした。
そのため、その部分を行から外しました。

| 行 | 要件 | 状態 |
| --- | --- | --- |
| degree | 入学までに、学士号かそれと同等以上の学位を得ていること。職歴は学位の代わりにならない | 公式の頁で確かめた |
| field-and-gpa | 計算機科学か近い分野の学士号と、累積 GPA 3.0 以上が望ましい（必須ではない）。満たさない出願は一件ずつ判断される | 公式の頁で確かめた |
| recommenders | 推薦者が 3 人。出願では推薦者のメールアドレスを書き、推薦者にはメールで案内が届き、推薦はオンラインで出す。紙の推薦状は要らない | 公式の頁で確かめた |
| recommenders-not | 推薦状を頼まない相手として、職場の同僚、今か前の同級生、家族（配偶者と親族を含む）、宗教の指導者、友人が挙がっている | 公式の頁で確かめた |
| academic-references | 学術の推薦者を少なくとも 1 人、できれば 2 人。計算機科学に関わる授業（そうした授業が少なければ、難しい技術の授業）で教えた教員に頼み、技術の力について具体的に書いてもらう | 公式の頁で確かめた |
| resume | 履歴書（résumé）。出さなければ出願は評価されない | 公式の頁で確かめた |
| supplemental-questions | 補足の質問への答えが全部要る。自由記述の問いは答えの長さに上限があり、最後の 8 問は Yes/No で答える確認の問い | 公式の頁で確かめた |
| no-statement-of-purpose | 志望理由書（Statement of Purpose）やほかの補足の文書は出さない。出しても読まれない | 公式の頁で確かめた |
| transcripts | 単位を得るために通ったすべての教育機関の、正式に発行された成績証明書などの写し（スキャン）を出す。学位を終えていない機関のものも要る | 公式の頁で確かめた |
| transcripts-problems | よくある問題として、在学中の学位の成績証明書が出願の日より 30 日を超えて古いことが挙がっている。10 頁を超える成績証明書は出し直しを求められ、出願は止まる | 公式の頁で確かめた |
| transcripts-translation | 留学生は、出願のときに、成績証明書の英語の非公式の訳と、元の言語の成績証明書を出す。GPA を自分で換算しない | 公式の頁で確かめた |
| english-test | 留学生には、TOEFL か IELTS-Academic の十分な点が要る | 公式の頁で確かめた |
| english-test-due | TOEFL か IELTS の点は、出願を終えるときまでに出す。出願の手続きが終わったあとには出せない | 公式の頁で確かめた |
| english-faq-toefl | OMSCS の FAQ の頁は、留学生に TOEFL 100 以上を求めると書いている | 公式の頁で確かめた |
| english-minimum | Georgia Tech の大学院の最低点は、TOEFL iBT では 2026 年 1 月より前の尺度で合計 90 以上かつ各技能 19 以上、後の尺度で合計 4.5 以上。IELTS Academic では総合 7 以上 | 公式の頁で確かめた |
| toefl-scale | TOEFL の点は、2026-01-21 からは 1 から 6 の新しい尺度で出る。それより前の点は 0 から 120 の尺度 | 公式の頁で確かめた |
| deadline-fall | 秋の入学の出願の締め切りは 3 月 1 日 | 公式の頁で確かめた |
| deadline-spring | 春の入学の出願の締め切りは 8 月 15 日 | 公式の頁で確かめた |
| after-deadline | 締め切りのあとに終えた学業は、出願の評価に入らない。締め切りまでに終わらない在学中の科目も入らない | 公式の頁で確かめた |
| conditional-admission | 入学は条件付き。入学から 1 年のうちに、基礎の科目 2 つを B 以上で終えると、正式の入学になる | 公式の頁で確かめた |
| preparation-by-application | 勧められた準備は、出願を出すときまでに終えていることが期待される。MOOC だけでは、STEM の学士号の無い人には足りることがまれ | 公式の頁で確かめた |
| no-mooc-listing | 成績の付かない、単位にならない MOOC の類の学習は、出願に並べない | 公式の頁で確かめた |
| no-pre-undergrad | 学部より前（中等教育や高校）の経歴は並べない | 公式の頁で確かめた |
| professional-development | 補足の書類は、出願の Professional Development の欄に上げる。成績証明書は Academic History の欄に上げる | 公式の頁で確かめた |

出典の URL と確かめ方と頁の文は、行ごとに `data/requirements.json` にあります。

## いま持っているもの・出願で使えるもの

[data/assets.json](./data/assets.json) に、項目ごとに置いてあります。
どの項目も、何か、状態、証拠の URL、公式の頁の扱い、その出典を持ちます。
証拠の URL は、運営者のリポジトリにすでにある公開の URL だけです。
公式の頁の扱いは、2026-11-20 に読んだ頁の文によります。
元の英語の文は、データの `official_quotes` にあります。
edX の頁は、この作業の環境から開けませんでした。
そのため、CS50x と CS50AI の修了証が verified の種類かどうかは確かめていません。
項目は 11 件です。
状態は、次のどれかです。

| 状態 | 意味 |
| --- | --- |
| 持っている | いま持っている |
| 途中 | 途中で、まだ得ていない |
| まだ無い | まだ持っていない |

| 項目 | 何か | 状態 | 証拠 | 公式の頁の扱い | 出典 |
| --- | --- | --- | --- | --- | --- |
| cs50x | CS50x（HarvardX）の edX の修了証。計算機科学の入門で、C・Python・SQL・Web の課題と最終課題を出して修了した。verified の種類の修了証かどうかは、ここでは確かめていない | 持っている | https://courses.edx.org/certificates/eac0a01d3d424a32a00114c487288fbc | 検証済みの修了証のある MOOC は考慮されうるが、単位の付く授業ほど厳密で記録の整ったものはまれ。ほかの MOOC の提供者の単位にならない課程も、足りるとされることはまれ。成績の付かない、単位にならない MOOC の類の学習は、出願に並べない | https://omscs.gatech.edu/preparing-yourself-omscs、https://omscs.gatech.edu/additional-app-guidelines |
| cs50ai | CS50AI（HarvardX）の edX の修了証。Python による人工知能の入門で、探索・論理推論・確率・最適化・機械学習・ニューラルネットワーク・言語処理を課題として実装した。verified の種類の修了証かどうかは、ここでは確かめていない | 持っている | https://courses.edx.org/certificates/a746620b6d7d45b583cb41b125e5f807 | 検証済みの修了証のある MOOC は考慮されうるが、単位の付く授業ほど厳密で記録の整ったものはまれ。ほかの MOOC の提供者の単位にならない課程も、足りるとされることはまれ。成績の付かない、単位にならない MOOC の類の学習は、出願に並べない | https://omscs.gatech.edu/preparing-yourself-omscs、https://omscs.gatech.edu/additional-app-guidelines |
| gt-moocs | Georgia Tech の professional certificate（Python の入門、Java のオブジェクト指向、データ構造とアルゴリズム）の verified certificate の課程。最初の Computing in Python I を受けることは、2026-11-19 に決めた（data/progress.json） | まだ無い | なし | 望ましい資格を満たさない出願のために、この課程を、中の評価と試験まで含めて終えることを勧めている。終えても入学は保証されず、STEM の学士号の無い人には、これだけで足りることはまれ | https://omscs.gatech.edu/preparing-yourself-omscs |
| bachelors | 学士号。在学中で、まだ得ていない。大学の名は書かない | 途中 | なし | 入学までに、学士号か同等以上の学位が要る。在学中の学位の成績証明書が出願の日より 30 日を超えて古いのは、よくある問題として挙がっている。締め切りのあとに終えた学業は評価に入らない | https://omscs.gatech.edu/admission-criteria、https://omscs.gatech.edu/additional-app-guidelines、https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines |
| github | 公開のリポジトリと、その機械の検査。プログラムを書いた記録。補足の書類として出すなら、Professional Development の欄に上げることになる | 持っている | https://github.com/cpsbvbng26-dotcom | 補足の書類は、出願の Professional Development の欄に上げる。望ましい資格を満たさない出願では、客観的に記録された計算機科学の力が見られる。読んだ頁は、公開のコードの扱いを書いていない。重く見ているのは、単位の付く上級の授業をこなせることである | https://omscs.gatech.edu/additional-app-guidelines、https://omscs.gatech.edu/preparing-yourself-omscs |
| resume | 履歴書（résumé）。この出願のためのものは、まだ書いていない | まだ無い | なし | 要る。出さなければ出願は評価されない | https://omscs.gatech.edu/additional-app-guidelines、https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines |
| supplemental-answers | 補足の質問への答え。まだ書いていない | まだ無い | なし | 全部の問いに答えが要る。志望理由書は読まれない。入学審査の委員会が見るのは、短い答えだけ | https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines、https://omscs.gatech.edu/additional-app-guidelines |
| english-test | TOEFL か IELTS の試験。まだ受けていない | まだ無い | なし | 留学生には十分な点が要り、点は出願を終えるときまでに出す。OMSCS の FAQ の頁は、TOEFL 100 以上と書いている | https://omscs.gatech.edu/admission-criteria、https://omscs.gatech.edu/prospective-student-faqs |
| upper-level-courses | 上級の、単位の付く計算機科学の科目を 2 から 4 つ、B 以上で終えること。この記録には、まだ無い | まだ無い | なし | 出願を強くする最もよい道は、ACM と IEEE の Computer Science Curricula 2013 を手がかりに、上級の科目を 2 から 4 つ選び、B 以上を取れることを示すこと。成績証明書は大学から出るもので、MOOC の提供者のような第三者のものではいけない | https://omscs.gatech.edu/preparing-yourself-omscs |
| math | 数学の準備（線形代数・確率・統計）。Preparing Yourself for OMSCS の頁が挙げる Georgia Tech の数学の MOOC は、この記録では、まだ受けていない | まだ無い | なし | 人工知能と機械学習の分野をはじめ、いくつかの科目は、線形代数・確率・統計の確かな素地を求める。Georgia Tech の公開の MOOC が、準備の助けとして挙がっている | https://omscs.gatech.edu/preparing-yourself-omscs |
| tuition | 学費の見通し。運営者の申告では、いまの貯えで、見積もりの総額をまかなえる。申告は 2026-11-20 に受けた。運営者の申告であり、証拠は置かない。額は書かない | 持っている | なし | 授業料は登録した単位時間ごとに、費用は登録した学期ごとに払う。修了には 30 単位時間が要る。OMSCS の授業料は、国外の学生（Out-of-Country）で 1 単位時間あたり 248 ドル。必須の費用（Mandatory Student Fees）は学期ごとに、4 単位時間未満で 212 ドル、4 単位時間以上で 531 ドル（Fall 2026、Spring 2027、Summer 2027 の表で同じ）。Claude の計算では、この額が変わらないとして、授業料の合計は 7440 ドル。1 学期に 1 科目（3 単位時間）ずつ 10 学期なら、費用を含めて合計 9560 ドル。1 学期に 2 科目ずつ 5 学期なら、合計 10095 ドル。額は改定される。本・試験・出願料は含めない。為替の率を出典から読んでいないので、円には換算しない | https://bursar.gatech.edu/tuition-fees、https://omscs.gatech.edu/prospective-student-faqs |

### 学費の見積もり

学費の項目は、運営者の申告によります。
証拠は置かず、運営者の持つ額も書きません。
次の数は、Claude が読んだ頁の額から計算した見積もりです。
額が変わらないと仮定しています。
額は改定されます。
本・試験・出願料は含めていません。
為替の率を出典から読んでいないため、円には換算していません。
授業料は、国外の学生で 1 単位時間あたり 248 ドルです。
必須の費用は、学期ごとに、4 単位時間未満で 212 ドル、4 単位時間以上で 531 ドルです。
修了には 30 単位時間が要ります。
授業料の合計は 7440 ドルです。
1 学期に 1 科目（3 単位時間）ずつなら、10 学期です。
1 科目ずつの合計は、費用を含めて 9560 ドルです。
1 学期に 2 科目（6 単位時間）ずつなら、5 学期です。
2 科目ずつの合計は、費用を含めて 10095 ドルです。
科目あたりの単位時間は、FAQ の頁の例によります。

### 推薦の枠

枠ごとに、状態だけを書きます。
推薦を頼む人の名や、その人についてのことは書きません。

| 枠 | 状態 |
| --- | --- |
| 1 | 依頼する候補を決めた |
| 2 | 依頼する候補を決めた |
| 3 | 決めていない |

公式の頁は、推薦者を次のように扱っています。

| 公式の頁の扱い | 出典 |
| --- | --- |
| 推薦者は 3 人。推薦者にはメールで案内が届き、推薦はオンラインで出す | https://omscs.gatech.edu/prospective-student-faqs |
| 学術の推薦者を少なくとも 1 人、できれば 2 人。教えた授業での技術の力について、具体的に書いてもらう | https://omscs.gatech.edu/additional-app-guidelines |
| 頼まない相手として、職場の同僚、今か前の同級生、家族、宗教の指導者、友人が挙がっている | https://omscs.gatech.edu/additional-app-guidelines |

## 必須ではないが、出願を強くするもの

[data/plus.json](./data/plus.json) に、行ごとに置いてあります。
必須の要件は、上の「出願の要件」の節と、博士課程の要件の節にあります。
どの行も、入学を保証しません。

### 修士課程（OMSCS）

この小節の行は、OMSCS の公式の頁が、出願を強くするものとして挙げているものです。
頁は、2026-11-21 に開いて読みました。
どの行にも、頁の英語の文を一字一句そのまま添えてあります。
出願を強くするものは 12 件です。
関わる項目の欄は、data/assets.json の項目です。
いまのところの欄は、この記録にある事実だけで書きました。

| 行 | 出願を強くするもの | 関わる項目 | いまのところ |
| --- | --- | --- | --- |
| document-cs | 計算機科学の知識を、記録と裏付けで示すこと。大学院の水準の厳しい授業をこなせる理由を、説明すること | github、supplemental-answers | 公開のリポジトリと、その機械の検査がある（github の項目）。出願では Professional Development の欄に上げることになる。読んだ頁は、公開のコードの扱いを書いていない |
| succinct | 問いに、短く要点だけで答えること | supplemental-answers | 補足の質問への答えは、まだ書いていない |
| upper-level | 上級（3・4 年次か大学院）の計算機科学の単位科目を 2 から 4 つ選び、B 以上を取れることを示すこと。頁は、出願を強くする最もよい道として CS2013 を手がかりにすることを挙げ、続けてこれを勧めている | upper-level-courses | まだ無い。在籍する大学の履修計画に 25 科目があるが、上級に当たるかは確かめていない |
| gt-certificates | 望ましい資格の力を示せない人に向けて、Georgia Tech の三つの professional certificate の課程を、中の評価と試験まで含めて、verified certificate の形で終えることが勧められている。終えても入学は保証されない | gt-moocs | 最初の Computing in Python I を受けると、2026-11-19 に決めた。verified certificate の形で受けるかは、記録に無い |
| other-credentials | 客観的に記録された、ほかの資格。verified certificate のある MOOC や bootcamp は考慮されうるが、単位の付く授業ほど厳密で記録の整ったものはまれ | cs50x、cs50ai | CS50x と CS50AI の edX の修了証がある。verified の種類かどうかは確かめていない。成績の付かない、単位にならない MOOC の類は出願に並べないとも、頁は書いている |
| languages | 複数のプログラミング言語に慣れていること | なし | CS50x で C・Python・SQL・Web の課題を出した（cs50x の項目）。公開のリポジトリには、Python と JavaScript で書いた検査がある |
| math-moocs | 線形代数・確率・統計を学んでいないか、学び直したいときは、Georgia Tech の公開の数学の MOOC が準備の助けになりうる | math | Georgia Tech の数学の MOOC は、まだ受けていない（math の項目）。在籍する大学の履修計画に、線形代数・確率・統計の科目がある |
| technical-letters | 推薦状が、人柄ではなく計算機科学の技術の力について書くこと。推薦者が、計算機科学について書ける理由（その人の資格）を書くこと | なし | 推薦の枠の状態だけを記録している。推薦者についてのことは、この記録に書かない |
| work-reference | 職場の推薦者なら、技術の仕事を直に知る上司に頼むこと。仕事の技術の中身を分からない上の役職の人は、よい推薦状を書けない | なし | 推薦の枠の状態だけを記録している。推薦者についてのことは、この記録に書かない |
| compelling-recommenders | よく知っていて、知的な力・分野の知識・伝える力などについて確かに書ける人を推薦者に選ぶこと。一般に、今か前の教員や上司のほうが、前の同級生や同僚より説得力がある | なし | 推薦の枠の状態だけを記録している。推薦者についてのことは、この記録に書かない |
| explain-gpa | 学部か大学院の GPA が低いときに、その理由を説明すること。説明しないことが、よくある問題として挙がっている | なし | この記録には、成績を書かない（決めごと 4） |
| awards | 受賞・表彰・フェローシップ・奨学金。出願で書く欄がある | なし | この記録には、受賞などの項目は無い |

出典の URL と頁の文は、行ごとに data/plus.json にあります。

### 博士課程（応用オントロジー）

www.buffalo.edu の頁は、2026-11-21 にも開けませんでした。
そのため、検索の結果の要約だけで探しました。
出願を強くするものを書いた University at Buffalo の文は、見つかりませんでした。
入学のあとに関わることとして、次の行を見つけました。
この行は、検索の要約を頁の文と突き合わせていません。

| 行 | 見つけたこと | 状態 | 出典 |
| --- | --- | --- | --- |
| prior-learning | 資格のある学業・産業・政府・商業の経験に、先行学習の単位（prior learning credit）が出る | 公式の頁の検索結果から | https://www.buffalo.edu/cas/philosophy/graduate/phd-ontology.html |

## 勧められている科目

[data/courses.json](./data/courses.json) に、Preparing Yourself for OMSCS の頁が勧める科目を並べています。
科目は 13 本です。
URL を置いたのは、確かめた頁だけです。
いま確かめてあるのは、[Computing in Python I の edX の頁](https://edx.org/es/learn/python/the-georgia-institute-of-technology-computing-in-python-i-fundamentals-and-procedural-programming)だけです。

## 在籍する大学の科目の履修計画

[data/course-plan.json](./data/course-plan.json) に、科目ごとに置いてあります。
出典は、「在籍する大学の公開のシラバス（2026-11-20 に読んだ。大学の名とアドレスは決めごと 5 により書かない）」です。
シラバスは、ブラウザで描いて読みました。
読んだのは、情報の分類と数理の分類です。
情報の分類には 65 科目、数理の分類には 47 科目がありました。
データには、読んだ科目の名を、sha256 の値だけで置いています。
検査は、計画の科目の名が、その値のどれかに当たることを確かめます。
計画の行は 25 行です。
状態は、どの行も「履修計画中」です。
これは、2026-11-20 に運営者が決めたことです。
項目の欄は、Preparing Yourself for OMSCS の頁が挙げる準備の項目です。
群の欄は、科目をまとめるための見出しです。
理由の欄は、シラバスの科目の説明だけによります。
body-of-knowledge の項目が指す CS2013 そのものは、読んでいません。

| 項目 | 頁の挙げ方 | 出典 |
| --- | --- | --- |
| programming | プログラミングの基礎 | https://omscs.gatech.edu/preparing-yourself-omscs |
| oop | オブジェクト指向の設計の原則（カプセル化・抽象化・多態・継承） | https://omscs.gatech.edu/preparing-yourself-omscs |
| data-structures | データ構造（リスト・スタック・キュー・木・ハッシュマップ） | https://omscs.gatech.edu/preparing-yourself-omscs |
| algorithms | アルゴリズム（AVL・MST・Dijkstra 法・動的計画法） | https://omscs.gatech.edu/preparing-yourself-omscs |
| languages | 複数のプログラミング言語に慣れていること | https://omscs.gatech.edu/preparing-yourself-omscs |
| body-of-knowledge | 上級の科目で扱う、CS2013 の Body of Knowledge の領域 | https://omscs.gatech.edu/preparing-yourself-omscs |
| math | 人工知能と機械学習のための数学（線形代数・確率・統計） | https://omscs.gatech.edu/preparing-yourself-omscs |

| 科目 | 開講 | 群 | 項目 | 理由 | 状態 |
| --- | --- | --- | --- | --- | --- |
| Pythonプログラミング | 2026年度開講 | プログラミングの基礎 | programming | Python で簡単な作業を自動化するプログラムを書き、コーディングの演習でプログラミングの基礎を身に付ける科目です。 | 履修計画中 |
| コンピューターサイエンス概論 | 2026年度開講 | データ構造・アルゴリズム・計算量 | data-structures | アルゴリズムとデータ構造の基礎と、プログラムの効率や計算複雑性を、Python でプログラムを動かしながら扱う科目です。 | 履修計画中 |
| オブジェクト指向プログラミング | 2026年度開講 | オブジェクト指向 | oop | Scala で、オブジェクト指向プログラミングの基本の概念と使い方を、デザインパターンまで含めて身につける科目です。 | 履修計画中 |
| Javaプログラミング演習 | 2026年度開講 | オブジェクト指向 | oop | Java で、オブジェクト指向プログラミングの要素と、データ構造などの基本の文法、標準 API、単体テストを学ぶ科目です。 | 履修計画中 |
| 関数型プログラミング | 2027年度開講 | 複数の言語と考え方 | languages | Scala で関数型プログラミングの考え方と技法を学び、パーサーコンビネーターのライブラリを実装する科目です。 | 履修計画中 |
| 論理回路概論 | 2027年度開講 | システム | body-of-knowledge | ブール関数と論理ゲートから始め、HDL で論理回路を作り、機械語でのプログラミングまでを扱う科目です。 | 履修計画中 |
| コンピュータ概論 | 2026年度開講 | システム | body-of-knowledge | コンピュータの発展を概観し、いまのコンピュータの仕組みを理解する科目です。 | 履修計画中 |
| Linux概論 | 2026年度開講 | システム | body-of-knowledge | Linux のコマンド操作、シェルプログラミング、セキュリティ対策を、手を動かしながら学ぶ科目です。 | 履修計画中 |
| 並行処理プログラミング | 2027年度開講 | システム | body-of-knowledge | マルチスレッドによる並行処理の基本（スレッドセーフ、メモリの可視性）を、Java を中心に、ほかの言語とも比べて学ぶ科目です。 | 履修計画中 |
| オートマトンと形式言語理論 | 2027年度開講 | 理論 | body-of-knowledge | オートマトンなどの計算機のモデルと形式言語、正則言語と文脈自由言語を扱う科目です。 | 履修計画中 |
| グラフ理論 | 2026年度開講 | 理論 | body-of-knowledge | 離散数学の主要な主題であるグラフ理論の、数理的な構造と定理と、工学や情報学への応用を扱う科目です。 | 履修計画中 |
| 集合と論理 | 2026年度開講 | 理論 | body-of-knowledge | 集合論と論理学の基本の概念と、述語論理や量化子を用いた証明を扱う科目です。 | 履修計画中 |
| 記号論理 | 2026年度開講 | 理論 | body-of-knowledge | 命題と述語で文を論理式に表し、定理証明系を使って証明を書く科目です。 | 履修計画中 |
| 組合せ論 | 2027年度開講 | 理論 | body-of-knowledge | 有限集合に入る構造を研究する組合せ論の、基本の概念と手法を、演習の形で扱う科目です。 | 履修計画中 |
| インターネット概論 | 2026年度開講 | ネットワーク | body-of-knowledge | AS と BGP、TCP/IP、DNS など、インターネットを支える技術を解説する科目です。 | 履修計画中 |
| インターネットのしくみ | 2026年度開講 | ネットワーク | body-of-knowledge | IP アドレスとドメイン名、その二つを紐づける DNS を、演習の形で学ぶ科目です。 | 履修計画中 |
| データベース運用実践 | 2027年度開講 | データと安全 | body-of-knowledge | データベースのインストールから運用までを、特に PostgreSQL の構築と運用で学ぶ科目です。 | 履修計画中 |
| 暗号技術とその応用 | 2027年度開講 | データと安全 | body-of-knowledge | 共通鍵暗号、公開鍵暗号、電子署名の安全性とその限界、代表的な実現方法を扱う科目です。 | 履修計画中 |
| 機械学習概論 | 2026年度開講 | 人工知能・機械学習 | body-of-knowledge | 線形モデル、SVM、決定木、教師なし学習、次元圧縮など、機械学習の基本から応用までを実践的に学ぶ科目です。 | 履修計画中 |
| ディープラーニング1 | 2026年度開講 | 人工知能・機械学習 | body-of-knowledge | 多層パーセプトロンから、活性化関数、確率的勾配降下法、最適化・初期化・正則化まで、深層学習の基礎を扱う科目です。 | 履修計画中 |
| 線形代数1 | 2026年度開講 | 人工知能・機械学習のための数学 | math | ベクトルと行列の演算、連立方程式、基底と次元、直交化法と QR 分解を扱う科目です。 | 履修計画中 |
| 線形代数2 | 2026年度開講 | 人工知能・機械学習のための数学 | math | ベクトル空間と線型写像、固有値と固有ベクトル、対角化、特異値分解を扱う科目です。 | 履修計画中 |
| 統計学入門 | 2026年度開講 | 人工知能・機械学習のための数学 | math | 確率と確率分布、推測統計学を学ぶ科目です。 | 履修計画中 |
| 計算機実験で学ぶ確率とモンテカルロ法 | 2026年度開講 | 人工知能・機械学習のための数学 | math | 乱数を使った計算機実験で、大数の法則や中心極限定理などの確率の基礎と、モンテカルロ法の基礎を学ぶ科目です。 | 履修計画中 |
| 数理統計 | 2027年度開講 | 人工知能・機械学習のための数学 | math | 確率変数と確率分布、極限定理、標本分布、統計的推測、仮説検定、区間推定、回帰を扱う科目です。 | 履修計画中 |

### 確かめていないこと・足りないところ

- 読んだ分類のどの科目の説明も、平衡木（AVL）、最小全域木、Dijkstra 法、動的計画法を挙げていません。グラフ理論は数学の理論の科目で、その説明も、これらのアルゴリズムを挙げていません。準備の頁は、項目として「Algorithms such as AVL, MST, Dijkstra’s, and dynamic programming.」を挙げています。同じ頁は「We recommend completing the verified certificate tracks (including all embedded assessments and exams) for the following three Georgia Tech professional certificate programs.」と書き、その中に「Data Structures & Algorithms, using the same material as CS1332: Data Structures & Algorithms at Georgia Tech.」を挙げています。この課程の中身は、この記録では読んでいません。
- 科目ごとの履修想定年次は、確かめていません。
- これらの科目が、準備の頁の言う「upper-level (i.e., junior, senior, or graduate level)」に当たるかどうかは、確かめていません。頁の文は「Find 2-4 upper-level (i.e., junior, senior, or graduate level) courses of interest that cover some of these areas and demonstrate the ability to earn a B or better in those courses.」です。
- 準備の頁は「Note that academic coursework means that the university is able to provide a transcript notating your performance is worthy of academic credit; this must come from the university, not a third-party intermediary or platform such as a MOOC provider.」と書いています。計画の科目は大学の単位の付く科目なので、その大学の成績証明書に載ります。どの科目が頁の求める水準に当たるかは、入学審査の委員会が判断することです。

## 博士課程の準備（University at Buffalo、応用オントロジー）

この節は、博士課程の準備の記録です。
目指す課程は、University at Buffalo の哲学科の、オンラインの応用オントロジーの博士課程（PhD in Applied Ontology）です。
前の節までの OMSCS の修士号は、それより前からの別の目標です。

### 2026-11-20 に決めた博士課程の目標

- University at Buffalo の、オンラインの応用オントロジーの博士課程（PhD in Applied Ontology）を、博士課程の目標にします。
- 学費は、運営者の貯えからまかないます。
- 学費の分が貯まってから、この課程に進みます。
- 額は、この記録に書きません。

これは、2026-11-20 に運営者が決めたことです。
決めたことの元の文は、[data/progress.json](./data/progress.json) の `topic` が `doctorate` の行にあります。
額は、どの通貨でも書きません。

### 読めた出典と、読めなかった出典

www.buffalo.edu の頁は、この作業の環境から開けませんでした。
自動の要求には、Akamai が「Access Denied」（HTTP 403）を返しました。
その拒否を回り込むことは、していません。
そのため、University at Buffalo の頁の事実は、検索の結果の要約だけで読んでいます。
その行の状態は、「公式の頁の検索結果から」です。
出典の URL は、検索の結果がその要約の出典として示した頁です。
検索の要約は、頁の文とは突き合わせていません。
第三者の頁として、Daily Nous の記事を 2026-11-20 に開いて読みました。
博士課程の記録で読めた頁は、Daily Nous の 1 頁だけです。
Daily Nous の行には、記事の英語の文を一字一句そのまま添えてあります。
状態の意味は、出願の要件の節の表と同じです。

### 博士課程の要件

[data/phd-requirements.json](./data/phd-requirements.json) に、行ごとに置いてあります。
どの行も、出典の URL、読んだ日、状態、確かめ方を持ちます。
博士課程の要件の表は 27 行です。
公式の頁の検索結果から読んだ行は 16 行です。
第三者の頁から読んだ行は 3 行です。
出典が見つからず、確かめていない行は 8 行です。
公式の頁を開いて確かめた行は 0 行です。
University at Buffalo が自らを応用オントロジーの大学院の学位を出す世界で唯一の大学と言っているのは、大学自身の主張です。
独立の確認は、見つけていません。
締め切りの行は、古いかもしれません。
別の University at Buffalo の頁が、出願は「will open soon」と書いていたためです。
頁に載っている問い合わせ先の名・メールアドレス・電話番号は、写していません。

| 行 | 要件 | 状態 | 出典 |
| --- | --- | --- | --- |
| credit-hours | 修了には 72 単位時間が要る | 公式の頁の検索結果から | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| time-to-degree | 修了までの年限（time to degree）は 5 年 | 公式の頁の検索結果から | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| online | 学位の要件は、すべてオンラインで満たせる。ハイブリッドの形も用意されている | 公式の頁の検索結果から | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| f1-visa | 全部オンラインの課程で、F-1 の学生の在留資格を保つ要件を満たさない | 公式の頁の検索結果から | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| contact-listed | 頁には課程の問い合わせ先が載っている。この記録には、その人の名・メールアドレス・電話番号を写さない | 公式の頁の検索結果から | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| start-fall-2026 | 2026 年の秋学期に始まる、新しい、全部オンラインで非同期の博士課程 | 公式の頁の検索結果から | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| worlds-only-claim | University at Buffalo は、応用オントロジーの大学院の学位を出す世界で唯一の大学だと自ら言っている。これは大学自身の主張で、独立の確認は見つけていない | 公式の頁の検索結果から | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| undergraduate-degree | 博士課程の出願者には、学部の学位が要る | 公式の頁の検索結果から | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| application-fee | 出願料は 75 ドル。2027 年の春と秋の学期には、出願料の免除がありうる | 公式の頁の検索結果から | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| deadlines | 応用オントロジーの MS と PhD の締め切りは、春の入学が 1 月 5 日、秋の入学が 8 月 1 日。別の University at Buffalo の頁は出願が「will open soon」と書いていたので、この締め切りは古いかもしれない | 公式の頁の検索結果から | https://www.buffalo.edu/cas/philosophy/graduate/admissions.html |
| competence | 博士課程の出願者は、応用オントロジーのどこかの領域での力を示す必要がある | 公式の頁の検索結果から | https://www.buffalo.edu/cas/philosophy/graduate/admissions.html |
| format | オンラインかハイブリッドか、全日制か定時制かを選べる。秋か春に始められる | 公式の頁の検索結果から | https://www.buffalo.edu/cas/philosophy/graduate/phd-ontology.html |
| qualifying-paper | 早い段階で qualifying paper を出す | 公式の頁の検索結果から | https://www.buffalo.edu/cas/philosophy/graduate/phd-ontology.html |
| rate-winter-2026 | Winter 2026、州外の学生、オンラインの課程の Graduate (includes Certificates) の額は、1 単位時間あたり授業料 565.00 ドルと費用 76.16 ドルで、合わせて 641.16 ドル | 公式の頁の検索結果から | https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/winter-tuition-and-fees-for-online-academic-programs.non-resident-online.html |
| rate-spring-2027 | Spring 2027、州外の学生、全日制の大学院の額は、1 学期あたり授業料 6785.00 ドルと費用 1003.92 ドルで、合わせて 7788.92 ドル | 公式の頁の検索結果から | https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/spring-tuition-online-academic-programs.non-resident-online-full-time.html |
| comprehensive-fee-waiver | オンラインの課程の学生は、Comprehensive Fee の免除の対象になる | 公式の頁の検索結果から | https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/spring-tuition-online-academic-programs.non-resident-online-full-time.html |
| dn-first-phd | Daily Nous は、University at Buffalo の哲学科が、応用オントロジーで最初になる博士課程を始めると伝えている | 第三者の頁から | https://dailynous.com/2026/05/13/new-doctoral-program-in-applied-ontology/ |
| dn-online-fall | Daily Nous は、全部オンラインで非同期の課程で、記事の年の秋から学生を受け入れると伝えている | 第三者の頁から | https://dailynous.com/2026/05/13/new-doctoral-program-in-applied-ontology/ |
| dn-masters | Daily Nous は、同じ学科が記事の前の年に、オンラインの応用オントロジーの修士課程を始めたと伝えている | 第三者の頁から | https://dailynous.com/2026/05/13/new-doctoral-program-in-applied-ontology/ |
| programme-tuition | この課程だけの学費の額 | 確かめていない | なし |
| dissertation | 博士論文の要件 | 確かめていない | なし |
| english-test | この博士課程の英語の試験の要件 | 確かめていない | なし |
| recommendations | この博士課程の推薦状の要件 | 確かめていない | なし |
| statement | この博士課程の志望の文書（statement）の要件 | 確かめていない | なし |
| transcripts | この博士課程の成績証明書の要件 | 確かめていない | なし |
| master-transfer | 修士課程の単位を移せるかどうか | 確かめていない | なし |
| funding | 奨学金や助成などの資金があるかどうか | 確かめていない | なし |

### 博士課程（応用オントロジー）で持っているもの・使えるもの

[data/phd-assets.json](./data/phd-assets.json) に、項目ごとに置いてあります。
状態の分け方は、OMSCS の持っているものの表と同じです。
要件の欄は、読んだ出典がその項目を要件に挙げているかを示します。
要件の行の欄は、その根拠になる要件の表の行です。
博士課程の持ち物の表は 7 項目です。
数えると、持っているものは 0 件、途中のものは 1 件、まだ無いものは 6 件です。
そのうち、読んだ出典が要件に挙げているものは 3 件です。
証拠の無い「持っている」は置いていません。

| 項目 | 何か | 状態 | 要件 | 要件の扱い | 要件の行 |
| --- | --- | --- | --- | --- | --- |
| bachelors | 学士号。在学中で、まだ得ていない。大学の名は書かない | 途中 | 読んだ出典が要件に挙げている | 博士課程の出願者には、学部の学位が要る（検索の結果の要約による） | undergraduate-degree |
| ontology-competence | 応用オントロジーのどこかの領域での力。これを示すものは、まだ無い。関わる事実は別に挙げるが、それが要件を満たすとはしない | まだ無い | 読んだ出典が要件に挙げている | 博士課程の出願者は、応用オントロジーのどこかの領域での力を示す必要がある（検索の結果の要約による）。どの水準で足りるかは、読んだ出典に無い | competence |
| tuition | 学費。運営者の貯えからまかなう。学費の分が貯まってから、この課程に進む。額は書かない | まだ無い | 読んだ出典が要件に挙げている | この課程だけの学費の額は、どの出典にも見つかっていない。Claude の見積もりは、この項目の estimate にある | rate-winter-2026、rate-spring-2027、comprehensive-fee-waiver |
| masters | 修士号。持っていない。OMSCS の修士号は、この記録の前からの別の目標 | まだ無い | 読んだ出典は要件に挙げていない | 読んだ出典は、博士課程の出願に学部の学位が要るとだけ書き、修士号を要件に挙げていない。修士の単位を移せるかどうかは見つかっていない | undergraduate-degree、master-transfer |
| english-test | 英語の試験。まだ受けていない | まだ無い | 要件が見つからない（確かめていない） | この博士課程の英語の試験の要件は、見つかっていない | english-test |
| recommendations | 推薦状。この博士課程のためのものは、まだ無い | まだ無い | 要件が見つからない（確かめていない） | この博士課程の推薦状の要件は、見つかっていない | recommendations |
| statement | 志望の文書（statement）。この博士課程のためのものは、まだ書いていない | まだ無い | 要件が見つからない（確かめていない） | この博士課程の志望の文書の要件は、見つかっていない | statement |

### 応用オントロジーの力に関わる事実

応用オントロジーの力の項目に関わる事実として、公開した哲学の論文と、履修計画中の科目を、題だけで挙げます。
これらが要件を満たすとは、この記録では言いません。
どの論文も査読前です。
どの科目も、まだ履修していません。

| 事実 | 種類 | 出典 |
| --- | --- | --- |
| The Nobility and Exemplarity of the Celibate Individual | 公開した哲学の論文（査読前） | cpsbvbng26-dotcom の README.md の論文の表（2026-11-20 に、main のコミット 7cc1521 で読んだ） |
| Manifesto of Imperial Selfhood | 公開した哲学の論文（査読前） | cpsbvbng26-dotcom の README.md の論文の表（2026-11-20 に、main のコミット 7cc1521 で読んだ） |
| Fragmentarian Spiritual Individualism | 公開した哲学の論文（査読前） | cpsbvbng26-dotcom の README.md の論文の表（2026-11-20 に、main のコミット 7cc1521 で読んだ） |
| Machine-mediated Rediscovery: A Case Study in Novelty, Priority, and Self-correction | 公開した哲学の論文（査読前） | cpsbvbng26-dotcom の README.md の論文の表（2026-11-20 に、main のコミット 7cc1521 で読んだ） |
| 記号論理 | 在籍する大学の科目（履修計画中） | data/course-plan.json |
| 集合と論理 | 在籍する大学の科目（履修計画中） | data/course-plan.json |

### 博士課程の学費の見積もり

次の表の数は、Claude が計算した見積もりです。
もとの額は、検索の結果の要約で読んだ University at Buffalo の学費の頁の額です。
額が変わらないと仮定しています。
額は改定されます。
この課程だけの学費の額は、どの出典にも見つかっていません。
そのため、オンラインの課程の大学院の単位時間ごとの額と、全日制の大学院の学期ごとの額を使いました。
学期の数は Claude の仮定で、出典にはありません。
全日制の学期あたりの単位時間も、読んだ出典にはありません。
Comprehensive Fee の免除は、差し引いていません。
出願料・本・試験は含めていません。
為替の率を出典から読んでいないため、円には換算していません。
学費は、運営者の貯えからまかなうと決めています。
運営者の貯えの額は書きません。

| 見積もり | 計算 | 合計 |
| --- | --- | --- |
| 1 単位時間あたりの額（授業料と費用）で 72 単位時間 | 72 × 641.16 | 46163.52 ドル |
| 1 単位時間あたりの授業料だけで 72 単位時間 | 72 × 565.00 | 40680.00 ドル |
| 全日制の 1 学期あたりの額で 6 学期（学期の数は Claude の仮定） | 6 × 7788.92 | 46733.52 ドル |

## MBA の計画（ウェールズ大学トリニティセントデイビッド、ヒューマンアカデミービジネススクール）

この節は、MBA の計画の記録です。
目指すプログラムは、ウェールズ大学トリニティセントデイビッド（UWTSD）MBAプログラムです。
このプログラムは、ヒューマンアカデミービジネススクールが日本の国内で運営しています。
学位は、University of Wales Trinity Saint David（UWTSD）が授与します。
博士号を得たあと、研究を続けながら、同時に並行して取る計画です。

### 2026-11-26 に決めた MBA の計画

- 博士号を得たあと、ヒューマンアカデミービジネススクールが運営するウェールズ大学トリニティセントデイビッド（UWTSD）MBAプログラムで、MBA を取ることを計画します。
- MBA は、研究を続けながら、同時に並行して取ります。
- 出願の実務の要件については、運営者がプログラムの担当とすでに話をしてあります。
- 実務の要件の中身は、この記録に書きません。

これは、2026-11-26 に運営者が決めたことです。
決めたことの元の文は、[data/progress.json](./data/progress.json) の `topic` が `mba` の行にあります。
プログラムの名の片仮名は、頁の綴りに合わせています。

### MBA の出典

mba.athuman.com の頁は、この作業の環境から開けませんでした。
この作業の環境の網の設定が、その接続を通しませんでした。
その設定を回り込むことは、していません。
そのため、プログラムの頁の事実は、検索の結果の要約だけで読んでいます。
その行の状態は、「公式の頁の検索結果から」です。
出典の URL は、検索の結果がその要約の出典として示した頁です。
検索の要約は、頁の文とは突き合わせていません。
状態の意味は、出願の要件の節の表と同じです。

### MBA のプログラムの事実

[data/mba.json](./data/mba.json) に、行ごとに置いてあります。
どの行も、出典の URL、読んだ日、状態、確かめ方を持ちます。
MBA の事実の表は 11 行です。
MBA の行のうち、公式の頁の検索結果から読んだものは 11 行です。
MBA の行のうち、公式の頁を開いて確かめたものは 0 行です。

| 行 | 事実 | 状態 | 出典 |
| --- | --- | --- | --- |
| programme-name | プログラムの名は、ウェールズ大学トリニティセントデイビッド（UWTSD）MBAプログラム | 公式の頁の検索結果から | https://mba.athuman.com/admission/application |
| page-title | 頁の題は「英国国立ウェールズ大学トリニティセントデイビッド　MBAプログラム」を含む | 公式の頁の検索結果から | https://mba.athuman.com/admission |
| run-by | ヒューマンアカデミー株式会社が、ヒューマンアカデミービジネススクール（HABS）として、日本の国内で開講し運営している | 公式の頁の検索結果から | https://mba.athuman.com/ |
| degree | 授与される学位は、MBA（Master of Business Administration） | 公式の頁の検索結果から | https://mba.athuman.com/admission/application |
| awarded-by | MBA の学位は、UWTSD が授与する | 公式の頁の検索結果から | https://mba.athuman.com/ |
| language | 講義は、すべて日本語で行う | 公式の頁の検索結果から | https://mba.athuman.com/admission/faq |
| online-weekends | 講義は、土曜日を中心とした週末に、オンラインで行う。平均で月に 3 日 | 公式の頁の検索結果から | https://mba.athuman.com/admission/faq |
| standard-length | 標準の修了の年限は 2 年 | 公式の頁の検索結果から | https://mba.athuman.com/admission |
| max-enrolment | 在籍できる期間は、最長で 6 年 | 公式の頁の検索結果から | https://mba.athuman.com/admission/faq |
| completion | 修了には、必修の 4 科目と選択の 2 科目を履修し、修士論文を書いて、合わせて 180 単位を得ることが要る | 公式の頁の検索結果から | https://mba.athuman.com/admission/faq |
| intakes | 入学の時期は、4 月と 10 月 | 公式の頁の検索結果から | https://mba.athuman.com/admission |

### MBA の記録に書かないもの

出願の実務の要件は、この記録に書きません。
その中身は、運営者が伏せると決めました。
運営者がプログラムの担当とすでに話をしてあることだけを、書きます。
担当の人の名は書きません。
学費の額は書きません。
頁に載っている事務局の所在地と電話番号も、写しません。

## 進み具合の記録

[data/progress.json](./data/progress.json) に、日付の順に足していきます。
いまあるのは、2026-11-19 に決めたこと、2026-11-20 に推薦の枠の状態を記録したこと、同じ日に決めた履修計画と博士課程の目標です。
同じ日に、在籍する大学は推薦状の依頼を受け付けないと、運営者から聞きました。
このことは、公開の頁では確かめていません。
2026-11-21 には、必須ではないが出願を強くするものを記録しました。
2026-11-26 には、博士号を得たあとの MBA の計画を記録しました。
済んだこととして書いた行の日付が、検査を走らせた日より後なら、検査が落ちます。

## 書かないもの

成績・点・GPA など、個人の学業の記録は書きません。
所属も書きません。
在籍する大学の名と、そのシラバスのアドレス、科目の担当の教員の名も書きません。
運営者の貯えの額は、どの通貨でも書きません。
博士課程の頁に載っている問い合わせ先の名・メールアドレス・電話番号も写しません。
MBA の出願の実務の要件の中身と、学費の額は書きません。
MBA のプログラムの担当の人の名も書きません。
推薦を頼む人の名や、その人についてのことも書きません。
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
