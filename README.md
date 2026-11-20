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

## 進み具合の記録

[data/progress.json](./data/progress.json) に、日付の順に足していきます。
いまあるのは、2026-11-19 に決めたこと、2026-11-20 に推薦の枠の状態を記録したこと、同じ日に決めた履修計画です。
同じ日に、在籍する大学は推薦状の依頼を受け付けないと、運営者から聞きました。
このことは、公開の頁では確かめていません。
済んだこととして書いた行の日付が、検査を走らせた日より後なら、検査が落ちます。

## 書かないもの

成績・点・GPA など、個人の学業の記録は書きません。
所属も書きません。
在籍する大学の名と、そのシラバスのアドレス、科目の担当の教員の名も書きません。
運営者の貯えの額は、どの通貨でも書きません。
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
