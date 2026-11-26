# omscs-preparation

[日本語](./README.md)

A dated record of the preparation for graduate study.
It records the preparation for an application to Georgia Tech's OMSCS (Online Master of Science in Computer Science).
From 2026-11-20 it also records the preparation for the University at Buffalo's PhD in Applied Ontology.
From 2026-11-26 it also records the plan for an MBA, to be taken after the doctorate, in parallel, while research continues.
The repository keeps the name of the first aim, OMSCS.
It records what was decided and what was done.
It holds no list of tasks to come.

## The decision of 2026-11-19

- The aim is a master's degree through Georgia Tech's OMSCS (Online Master of Science in Computer Science), after the bachelor's degree.
- Georgia Tech's own MOOCs are taken one per month.
- The first MOOC is Computing in Python I: Fundamentals and Procedural Programming, on edX.
- Graded work is done without AI.
- AI is used only to explain concepts.

The aim of the master's degree is the one in the table of aims on the profile site, whose source is `aims` in `site.json` of `researcher-profile`.
The pace of the MOOCs and the use of AI were decided by the owner on 2026-11-19 and are not in `site.json` of that day.
The original text of the decision is the first entry of [data/progress.json](./data/progress.json).

## Application requirements

[data/requirements.json](./data/requirements.json) holds one row per requirement, each with its source URL, the date it was read, a status and how it was checked.
The status is one of the following.

| Status | Meaning |
| --- | --- |
| confirmed on the official page | The official page was opened and read |
| from search results of the official page | Read in the summary or excerpt of a search result; the page was not opened |
| from a third-party page | Read on a page that is not official |
| not confirmed | The source could not be read |

omscs.gatech.edu could not be reached from the environment of this record on 2026-11-19.
On 2026-11-20 the network setting let omscs.gatech.edu and grad.gatech.edu through, and 7 pages were opened and read that day.
One of them is the Bursar's page of tuition and fee rates (bursar.gatech.edu), the source of the tuition item.
Each row confirmed on the official page carries the page's own English sentences, word for word.
There are 24 rows.
Of them, 24 are confirmed on the official page.
The lower bound on years of education in the earlier degree row is on none of the pages read, so that part was dropped.

| Row | Requirement | Status |
| --- | --- | --- |
| degree | A bachelor's degree, its equivalent, or a higher degree before matriculation. Work experience does not substitute for a degree | confirmed on the official page |
| field-and-gpa | An undergraduate degree in computer science or a related field and a cumulative GPA of 3.0 or higher are preferred, not required. Applicants who do not meet them are evaluated case by case | confirmed on the official page |
| recommenders | Recommendations from three individuals. The application gives their e-mail addresses, they are contacted by e-mail and submit online, and no physical letter is required | confirmed on the official page |
| recommenders-not | Work peers, current or former classmates, family (spouses and relatives included), religious leaders and friends are listed as people not to ask for letters | confirmed on the official page |
| academic-references | At least one academic reference, preferably two: a teacher who taught the applicant in a computer science related class, or else in a challenging technical course, writing specifically about technical abilities | confirmed on the official page |
| resume | A résumé. Without one, the application is not evaluated | confirmed on the official page |
| supplemental-questions | Answers to all of the supplemental questions are required. The free-form answers have length limits, and the final eight questions are Yes/No checklist questions | confirmed on the official page |
| no-statement-of-purpose | No Statement of Purpose or any other supplementary statement. It will not be read | confirmed on the official page |
| transcripts | Scans of officially issued academic documents, such as transcripts, from every institution attended for academic credit, even where no degree was completed | confirmed on the official page |
| transcripts-problems | Listed as common problems: a transcript for a degree in progress that is more than 30 days older than the application date. A transcript longer than 10 pages must be resubmitted, and the application is put on hold | confirmed on the official page |
| transcripts-translation | International applicants provide an unofficial English translation of the transcript and the native language transcript with the application. The GPA is not converted by the applicant | confirmed on the official page |
| english-test | International applicants need satisfactory TOEFL or IELTS-Academic scores | confirmed on the official page |
| english-test-due | TOEFL or IELTS scores are due when the application is completed, not after the application process ends | confirmed on the official page |
| english-faq-toefl | The OMSCS FAQ page asks international applicants for a TOEFL score of at least 100 | confirmed on the official page |
| english-minimum | The Institute minimum is a TOEFL iBT total of 90 with at least 19 in each section on the scale before January 2026, or 4.5 on the later scale, or an IELTS Academic overall band of 7 | confirmed on the official page |
| toefl-scale | TOEFL scores earned on or after 2026-01-21 are reported on the new 1 to 6 scale, and earlier scores on the 0 to 120 scale | confirmed on the official page |
| deadline-fall | The application deadline for Fall matriculation is March 1 | confirmed on the official page |
| deadline-spring | The application deadline for Spring matriculation is August 15 | confirmed on the official page |
| after-deadline | Academic work completed after the application deadline is not considered, including coursework in progress and not completed before the deadline | confirmed on the official page |
| conditional-admission | Admission is conditional. Passing two foundational courses with a B or better within a year of matriculation gives full admission | confirmed on the official page |
| preparation-by-application | The recommended preparation is expected to be complete when the application is submitted. These MOOCs alone are rarely sufficient for applicants without a bachelor's degree in a STEM field | confirmed on the official page |
| no-mooc-listing | Non-graded, non-academic-credit MOOC-type coursework is not listed in the application | confirmed on the official page |
| no-pre-undergrad | No background before undergraduate study, such as secondary or high school, is listed | confirmed on the official page |
| professional-development | Supporting documents are uploaded to the Professional Development area of the application, and transcripts to the Academic History area | confirmed on the official page |

The source URL, how each row was read and the page's sentences are in `data/requirements.json`.

## What the owner has now, and what can be used in the application

[data/assets.json](./data/assets.json) holds one entry per item: what it is, a status, the evidence URL, how the official pages treat it, and their source.
Evidence URLs are only public URLs already in the operator's repositories.
The official treatment rests on sentences of the pages read on 2026-11-20, kept word for word in `official_quotes`.
The edX pages could not be opened from this environment, so whether the CS50x and CS50AI certificates are verified certificates is not confirmed.
There are 11 items.
The status is one of the following.

| Status | Meaning |
| --- | --- |
| has it | Held now |
| in progress | Under way and not yet earned |
| not yet | Not held yet |

| Item | What it is | Status | Evidence | How the official pages treat it | Source |
| --- | --- | --- | --- | --- | --- |
| cs50x | The edX certificate of CS50x (HarvardX), an introduction to computer science, completed with the problem sets in C, Python, SQL and the Web and a final project. Whether it is a verified certificate is not confirmed here | has it | https://courses.edx.org/certificates/eac0a01d3d424a32a00114c487288fbc | MOOCs with verified certificates may be considered, but they are rarely as rigorous and well documented as for-credit classes. Non-credit courses from other MOOC providers are rarely considered sufficient. Non-graded, non-academic-credit MOOC-type coursework is not listed | https://omscs.gatech.edu/preparing-yourself-omscs, https://omscs.gatech.edu/additional-app-guidelines |
| cs50ai | The edX certificate of CS50AI (HarvardX), an introduction to artificial intelligence with Python, with search, logical inference, probability, optimization, machine learning, neural networks and language processing implemented as problem sets. Whether it is a verified certificate is not confirmed here | has it | https://courses.edx.org/certificates/a746620b6d7d45b583cb41b125e5f807 | MOOCs with verified certificates may be considered, but they are rarely as rigorous and well documented as for-credit classes. Non-credit courses from other MOOC providers are rarely considered sufficient. Non-graded, non-academic-credit MOOC-type coursework is not listed | https://omscs.gatech.edu/preparing-yourself-omscs, https://omscs.gatech.edu/additional-app-guidelines |
| gt-moocs | The verified certificate tracks of Georgia Tech's professional certificates (Introduction to Python Programming, Object-Oriented Programming with Java, Data Structures & Algorithms). Taking Computing in Python I first was decided on 2026-11-19 (data/progress.json) | not yet | none | For applicants without the preferred qualifications, the page recommends completing these verified certificate tracks, including all embedded assessments and exams. Completing them does not guarantee admission, and they alone are rarely sufficient without a bachelor's degree in a STEM field | https://omscs.gatech.edu/preparing-yourself-omscs |
| bachelors | A bachelor's degree, in progress and not yet earned. The university is not named | in progress | none | A bachelor's degree, its equivalent or a higher degree is required before matriculation. A transcript for a degree in progress more than 30 days older than the application date is listed as a common problem. Academic work completed after the deadline is not considered | https://omscs.gatech.edu/admission-criteria, https://omscs.gatech.edu/additional-app-guidelines, https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines |
| github | The public repositories and their machine checks, a record of programming. Given as a supporting document, it would go in the Professional Development area | has it | https://github.com/cpsbvbng26-dotcom | Supporting documents go in the Professional Development area. For applicants without the preferred qualifications, objectively documented capability in computer science is looked for. The pages read do not say how public code is treated. What they weigh is the ability to do upper level for-credit coursework | https://omscs.gatech.edu/additional-app-guidelines, https://omscs.gatech.edu/preparing-yourself-omscs |
| resume | A résumé. One for this application has not been written yet | not yet | none | Required. Without one, the application is not evaluated | https://omscs.gatech.edu/additional-app-guidelines, https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines |
| supplemental-answers | Answers to the supplemental questions, not yet written | not yet | none | Answers to all of the questions are required. A Statement of Purpose is not read. The short answers are all the Admissions Committee looks at | https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines, https://omscs.gatech.edu/additional-app-guidelines |
| english-test | The TOEFL or IELTS test, not taken yet | not yet | none | International applicants need satisfactory scores, due when the application is completed. The OMSCS FAQ page asks for a TOEFL score of at least 100 | https://omscs.gatech.edu/admission-criteria, https://omscs.gatech.edu/prospective-student-faqs |
| upper-level-courses | Two to four upper level for-credit computer science courses passed with a B or better. None is in this record yet | not yet | none | The best way to strengthen an application is to use Computer Science Curricula 2013 by the ACM and IEEE, choose two to four upper level courses, and show the ability to earn a B or better. The transcript comes from the university, not from a third party such as a MOOC provider | https://omscs.gatech.edu/preparing-yourself-omscs |
| math | Preparation in mathematics (linear algebra, probability, statistics). The Georgia Tech mathematics MOOCs named on Preparing Yourself for OMSCS have not been taken in this record | not yet | none | Some courses, especially in artificial intelligence and machine learning, require a solid background in linear algebra, probability and statistics. Georgia Tech's public MOOCs are named as help | https://omscs.gatech.edu/preparing-yourself-omscs |
| tuition | Tuition covered. By the owner's own report, current savings cover the estimated total. The report was received on 2026-11-20. This is a self-report: no evidence is kept, and no amount is written | has it | none | Tuition is paid per credit hour of enrollment, and fees per semester of enrollment. 30 credit hours are required to graduate. OMSCS tuition for Out-of-Country students is 248 dollars per credit hour. Mandatory Student Fees per semester are 212 dollars for fewer than 4 credit hours and 531 dollars for 4 or more (the same in the Fall 2026, Spring 2027 and Summer 2027 tables). By Claude's own computation at those rates, assuming they do not change, tuition comes to 7440 dollars. At one course (3 credit hours) per semester over 10 semesters, the total with fees is 9560 dollars. At two courses per semester over 5 semesters, it is 10095 dollars. Rates are revised. Books, tests and the application fee are excluded. No exchange rate was read from a source, so nothing is converted to yen | https://bursar.gatech.edu/tuition-fees, https://omscs.gatech.edu/prospective-student-faqs |

### Estimate of tuition

The tuition item rests on the owner's own report.
No evidence is kept, and no amount the owner holds is written.
The figures below are an estimate that Claude computed at the rates of the pages read.
They assume that the rates do not change.
Rates are revised.
Books, tests and the application fee are excluded.
No exchange rate was read from a source, so nothing is converted to yen.
Out-of-Country tuition is 248 dollars per credit hour.
Mandatory student fees are 212 dollars per semester for fewer than 4 credit hours, and 531 dollars for 4 or more.
30 credit hours are required to graduate.
Tuition comes to 7440 dollars in all.
At one course (3 credit hours) per semester, it takes 10 semesters.
The total at one course per semester, with fees, is 9560 dollars.
At two courses (6 credit hours) per semester, it takes 5 semesters.
The total at two courses per semester, with fees, is 10095 dollars.
The credit hours of a course follow the example on the FAQ page.

### Recommendation slots

Each slot records only its state.
Nothing is written about the people to be asked, not even their names.

| Slot | State |
| --- | --- |
| 1 | a candidate to ask has been chosen |
| 2 | a candidate to ask has been chosen |
| 3 | not decided |

The official pages treat recommenders as follows.

| How the official pages treat it | Source |
| --- | --- |
| Three recommenders, who are contacted by e-mail and submit online | https://omscs.gatech.edu/prospective-student-faqs |
| At least one academic reference, preferably two, writing specifically about technical abilities in the course taught | https://omscs.gatech.edu/additional-app-guidelines |
| Work peers, current or former classmates, family, religious leaders and friends are listed under DO NOT | https://omscs.gatech.edu/additional-app-guidelines |

## Not required, but strengthening an application

[data/plus.json](./data/plus.json) holds them row by row.
The required items are in the section "Application requirements" above and in the section of doctoral requirements.
No row guarantees admission.

### Master's degree (OMSCS)

The rows of this subsection are what the official OMSCS pages name as strengthening an application.
The pages were opened and read on 2026-11-21.
Every row carries the page's English sentences word for word.
12 things that strengthen an application are recorded.
The column of related items names items of data/assets.json.
The column "Now" uses only facts already in this record.

| Row | What strengthens an application | Related items | Now |
| --- | --- | --- | --- |
| document-cs | Documenting and substantiating computer science knowledge, and explaining why one is capable of rigorous, graduate-level coursework | github, supplemental-answers | Public repositories with their machine checks (item github); in an application they would go in the Professional Development area. The pages read do not say how public code is treated |
| succinct | Answering every question succinctly and to the point | supplemental-answers | The answers to the supplemental questions are not written yet |
| upper-level | Choosing 2 to 4 upper-level (junior, senior or graduate) computer science courses and showing the ability to earn a B or better; the page names referring to CS2013 as the best way to strengthen an application and recommends this as its next step | upper-level-courses | None yet. The plan at the owner's university has 25 courses, but whether they are upper-level is not checked |
| gt-certificates | For those who cannot yet demonstrate the competencies, completing the verified certificate tracks of three Georgia Tech professional certificate programmes, with every embedded assessment and exam, is recommended; completing them does not guarantee admission | gt-moocs | Taking Computing in Python I first was decided on 2026-11-19. Whether it is taken as a verified certificate is not in the record |
| other-credentials | Other objectively documented credentials: MOOCs with verified certificates and bootcamps may be considered, but they are rarely as rigorous and well documented as for-credit classes | cs50x, cs50ai | edX certificates of CS50x and CS50AI. Whether they are verified certificates is not checked. The pages also say not to list non-graded, non-academic-credit MOOC-type coursework |
| languages | Familiarity with several programming languages | none | Assignments in C, Python, SQL and the web were submitted in CS50x (item cs50x). The public repositories hold checks written in Python and JavaScript |
| math-moocs | Georgia Tech's public mathematics MOOCs may help with preparation, where linear algebra, probability and statistics have not been studied or need brushing up | math | Georgia Tech's mathematics MOOCs are not taken yet (item math). The plan at the owner's university has courses in linear algebra, probability and statistics |
| technical-letters | Letters that speak to technical computer science skills rather than personal characteristics, with the recommender stating their own credentials in computer science | none | Only the state of the recommendation slots is recorded. Nothing about a recommender is written here |
| work-reference | For a work reference, a supervisor with direct knowledge of technical work; a high-level executive who does not understand its details cannot write a good letter | none | Only the state of the recommendation slots is recorded. Nothing about a recommender is written here |
| compelling-recommenders | Recommenders who know the applicant well and can comment with authority on scholarly characteristics; generally, current and former teachers and supervisors are more compelling than former classmates or co-workers | none | Only the state of the recommendation slots is recorded. Nothing about a recommender is written here |
| explain-gpa | Explaining a poor undergraduate or graduate GPA; failing to explain one is listed among the most common problems | none | This record does not hold grades (rule 4) |
| awards | Awards, recognitions, fellowships and scholarships, for which the application has a place | none | This record has no item of awards or the like |

The source URL and the page's sentences of each row are in data/plus.json.

### Doctorate (Applied Ontology)

The pages of www.buffalo.edu could not be opened on 2026-11-21 either.
The search was therefore made in the summaries of search results only.
No sentence of the University at Buffalo on what strengthens an application was found.
The row below was found, which concerns the time after admission.
Its summary was not compared with the page's own sentences.

| Row | What was found | Status | Source |
| --- | --- | --- | --- |
| prior-learning | Prior learning credit is available for qualifying academic, industry, government or commercial experience | from search results of the official pages | https://www.buffalo.edu/cas/philosophy/graduate/phd-ontology.html |

## Recommended courses

[data/courses.json](./data/courses.json) lists the courses recommended by the page Preparing Yourself for OMSCS.
There are 13 courses.
A URL is given only where it was verified: so far, only [the edX page of Computing in Python I](https://edx.org/es/learn/python/the-georgia-institute-of-technology-computing-in-python-i-fundamentals-and-procedural-programming).

## Planned courses at the owner's university

[data/course-plan.json](./data/course-plan.json) holds one row per course.
The source is the public syllabus of the university where the owner is enrolled (read on 2026-11-20; the university's name and address are not written, by rule 5).
The syllabus was rendered in a browser and read.
Two of its categories were read: information and mathematical sciences.
The information category has 65 courses, and the mathematical sciences category has 47.
The data keeps the titles of the courses read only as sha256 values.
The check confirms that each planned title matches one of them.
The plan has 25 rows.
Every row has the status planned, which the owner decided on 2026-11-20.
The item column is an item of preparation named on the page Preparing Yourself for OMSCS.
The group column is a heading that gathers the courses.
The reason column rests only on the course's description in the syllabus.
CS2013 itself, which the item body-of-knowledge points to, was not read.

| Item | As the page names it | Source |
| --- | --- | --- |
| programming | The fundamentals of programming | https://omscs.gatech.edu/preparing-yourself-omscs |
| oop | Object-oriented design principles (encapsulation, abstraction, polymorphism, inheritance) | https://omscs.gatech.edu/preparing-yourself-omscs |
| data-structures | Data structures (lists, stacks, queues, trees, hashmaps) | https://omscs.gatech.edu/preparing-yourself-omscs |
| algorithms | Algorithms (AVL, MST, Dijkstra’s, dynamic programming) | https://omscs.gatech.edu/preparing-yourself-omscs |
| languages | Familiarity with multiple programming languages | https://omscs.gatech.edu/preparing-yourself-omscs |
| body-of-knowledge | Areas of the CS2013 Body of Knowledge, covered by upper-level courses | https://omscs.gatech.edu/preparing-yourself-omscs |
| math | Mathematics for AI and machine learning (linear algebra, probability, statistics) | https://omscs.gatech.edu/preparing-yourself-omscs |

| Course | Offered | Group | Item | Reason | Status |
| --- | --- | --- | --- | --- | --- |
| Pythonプログラミング | academic year 2026 | Programming fundamentals | programming | Writes Python programs that automate simple tasks, and builds the fundamentals of programming through coding exercises. | planned |
| コンピューターサイエンス概論 | academic year 2026 | Data structures, algorithms and complexity | data-structures | Covers the basics of algorithms and data structures, program efficiency and computational complexity, running and changing programs in Python. | planned |
| オブジェクト指向プログラミング | academic year 2026 | Object-oriented programming | oop | Teaches the basic concepts and use of object-oriented programming in Scala, including design patterns. | planned |
| Javaプログラミング演習 | academic year 2026 | Object-oriented programming | oop | Teaches the elements of object-oriented programming in Java, with its basic syntax including data structures, its standard API and unit testing. | planned |
| 関数型プログラミング | academic year 2027 | Multiple languages and paradigms | languages | Teaches the thinking and techniques of functional programming in Scala, up to implementing a parser-combinator library. | planned |
| 論理回路概論 | academic year 2027 | Systems | body-of-knowledge | Starts from Boolean functions and logic gates, builds logic circuits in an HDL, and ends with programming in machine language. | planned |
| コンピュータ概論 | academic year 2026 | Systems | body-of-knowledge | Surveys how computers developed, to understand how present-day computers work. | planned |
| Linux概論 | academic year 2026 | Systems | body-of-knowledge | Teaches Linux commands, shell programming and security measures through hands-on work. | planned |
| 並行処理プログラミング | academic year 2027 | Systems | body-of-knowledge | Teaches the basics of multithreaded concurrency (thread safety, memory visibility), mainly in Java and compared with other languages. | planned |
| オートマトンと形式言語理論 | academic year 2027 | Theory | body-of-knowledge | Covers models of computation such as automata, formal languages, and regular and context-free languages. | planned |
| グラフ理論 | academic year 2026 | Theory | body-of-knowledge | Covers the mathematical structure and theorems of graph theory, a main topic of discrete mathematics, with applications in engineering and informatics. | planned |
| 集合と論理 | academic year 2026 | Theory | body-of-knowledge | Covers the basic concepts of set theory and logic, and proofs with predicate logic and quantifiers. | planned |
| 記号論理 | academic year 2026 | Theory | body-of-knowledge | Expresses statements as formulas with propositions and predicates, and writes proofs with a theorem prover. | planned |
| 組合せ論 | academic year 2027 | Theory | body-of-knowledge | Covers the basic concepts and methods of combinatorics, the study of structures on finite sets, as an exercise course. | planned |
| インターネット概論 | academic year 2026 | Networks | body-of-knowledge | Explains the technologies behind the Internet, such as AS and BGP connections, TCP/IP and DNS. | planned |
| インターネットのしくみ | academic year 2026 | Networks | body-of-knowledge | Teaches IP addresses, domain names and the DNS that links them, in the form of exercises. | planned |
| データベース運用実践 | academic year 2027 | Data and security | body-of-knowledge | Teaches databases from installation to operation, in particular building and running PostgreSQL. | planned |
| 暗号技術とその応用 | academic year 2027 | Data and security | body-of-knowledge | Covers symmetric-key and public-key cryptography and digital signatures: their security, its limits and typical constructions. | planned |
| 機械学習概論 | academic year 2026 | AI and machine learning | body-of-knowledge | Teaches machine learning from the basics to applications in practice, including linear models, SVMs, decision trees, unsupervised learning and dimensionality reduction. | planned |
| ディープラーニング1 | academic year 2026 | AI and machine learning | body-of-knowledge | Covers the basics of deep learning, from multilayer perceptrons to activation functions, stochastic gradient descent, optimisation, initialisation and regularisation. | planned |
| 線形代数1 | academic year 2026 | Mathematics for AI and machine learning | math | Covers vector and matrix operations, systems of linear equations, bases and dimension, orthogonalisation and QR decomposition. | planned |
| 線形代数2 | academic year 2026 | Mathematics for AI and machine learning | math | Covers vector spaces and linear maps, eigenvalues and eigenvectors, diagonalisation and singular value decomposition. | planned |
| 統計学入門 | academic year 2026 | Mathematics for AI and machine learning | math | Teaches probability, probability distributions and inferential statistics. | planned |
| 計算機実験で学ぶ確率とモンテカルロ法 | academic year 2026 | Mathematics for AI and machine learning | math | Teaches the basics of probability, including the law of large numbers and the central limit theorem, and of Monte Carlo methods, through computer experiments with random numbers. | planned |
| 数理統計 | academic year 2027 | Mathematics for AI and machine learning | math | Covers random variables and distributions, limit theorems, sampling distributions, statistical inference, hypothesis tests, interval estimation and regression. | planned |

### What was not checked, and gaps

- No course description in the categories read names balanced trees (AVL), minimum spanning trees, Dijkstra's algorithm or dynamic programming. Graph theory (グラフ理論) is a mathematical theory course, and its description does not name these algorithms either. The preparation page names the item “Algorithms such as AVL, MST, Dijkstra’s, and dynamic programming”. The same page says “We recommend completing the verified certificate tracks (including all embedded assessments and exams) for the following three Georgia Tech professional certificate programs”. Among those programs it names “Data Structures & Algorithms, using the same material as CS1332: Data Structures & Algorithms at Georgia Tech”. The content of that track was not read for this record.
- The year in which each course is expected to be taken was not checked.
- Whether these courses are “upper-level (i.e., junior, senior, or graduate level)” in the sense of the preparation page was not checked.
- The preparation page says that “academic coursework means that the university is able to provide a transcript”. It adds that “this must come from the university, not a third-party intermediary or platform such as a MOOC provider”. The planned courses are for-credit courses at a university, so they appear on that university's transcript. Whether a given course meets the level the page asks for is for the Admissions Committee to judge.

## Doctoral preparation (University at Buffalo, Applied Ontology)

This section is the record of the preparation for a doctorate.
The program aimed at is the online PhD in Applied Ontology of the Department of Philosophy at the University at Buffalo.
The OMSCS master's degree of the sections above is a separate, earlier aim.

### The doctoral decision of 2026-11-20

- The doctoral aim is the University at Buffalo's online PhD in Applied Ontology.
- The tuition is paid from the owner's savings.
- The program is pursued once the tuition has been saved.
- No amount is written in this record.

This was decided by the owner on 2026-11-20.
The original text of the decision is the entry of [data/progress.json](./data/progress.json) whose `topic` is `doctorate`.
No amount is written, in any currency.

### Sources read, and sources that could not be opened

The pages of www.buffalo.edu could not be opened from the environment of this record.
Akamai answered every automated request with "Access Denied" (HTTP 403).
Nothing was done to get around the refusal.
The facts from the University at Buffalo's pages were therefore read only in search-result summaries.
Those rows have the status "from search results of the official page".
Each source URL is the page that the search result named as the source of its summary.
The summaries were not compared with the text of the pages.
The Daily Nous article, a third-party page, was opened and read on 2026-11-20.
Only 1 page was read for the doctoral record: the Daily Nous article.
The Daily Nous rows carry the article's own English sentences, word for word.
The statuses mean the same as in the table of the section on application requirements.

### Doctoral requirements

[data/phd-requirements.json](./data/phd-requirements.json) holds one row per requirement or fact, each with its source URL, the date it was read, a status and how it was read.
The doctoral table of requirements has 27 rows.
Of them, 16 rows come from search results of the official pages.
3 rows come from a third-party page.
8 rows are not confirmed, because no source was found.
0 rows were confirmed on an opened official page.
The University at Buffalo's description of itself as the world's only university offering graduate-level degrees in applied ontology is the university's own claim.
No independent confirmation was found.
The row of deadlines may be out of date, because another University at Buffalo page said that applications "will open soon".
The name, e-mail address and telephone number of the contact on the page are not copied.

| Row | Requirement | Status | Source |
| --- | --- | --- | --- |
| credit-hours | 72 credit hours are required | from search results of the official page | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| time-to-degree | The time to degree is 5 years | from search results of the official page | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| online | 100 percent of the degree requirements can be fulfilled online; a hybrid option is also offered | from search results of the official page | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| f1-visa | The program is fully online and does not meet the requirements for maintaining F-1 student visa status | from search results of the official page | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| contact-listed | The page lists a program contact. The contact's name, e-mail address and telephone number are not copied into this record | from search results of the official page | https://www.buffalo.edu/grad/programs/applied-ontology-phd.html |
| start-fall-2026 | A new, fully online, asynchronous PhD program, beginning in the fall 2026 semester | from search results of the official page | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| worlds-only-claim | UB calls itself the world's only university offering graduate-level degrees in applied ontology. This is the university's own claim; no independent confirmation was found | from search results of the official page | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| undergraduate-degree | PhD applicants require an undergraduate degree | from search results of the official page | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| application-fee | The application fee is 75 dollars; fee waivers may be available for the spring and fall 2027 terms | from search results of the official page | https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html |
| deadlines | The deadlines for the MS and PhD in Applied Ontology are January 5 (spring enrollment) and August 1 (fall enrollment). Another UB page said that applications "will open soon", so these deadlines may be out of date | from search results of the official page | https://www.buffalo.edu/cas/philosophy/graduate/admissions.html |
| competence | PhD applicants must show competence in some area of applied ontology | from search results of the official page | https://www.buffalo.edu/cas/philosophy/graduate/admissions.html |
| format | Online or hybrid, full-time or part-time; the program can be started in fall or spring | from search results of the official page | https://www.buffalo.edu/cas/philosophy/graduate/phd-ontology.html |
| qualifying-paper | A qualifying paper is submitted early on | from search results of the official page | https://www.buffalo.edu/cas/philosophy/graduate/phd-ontology.html |
| rate-winter-2026 | Winter 2026, non-resident, online academic programs, Graduate (includes Certificates): tuition 565.00 dollars and fees 76.16 dollars, 641.16 dollars per credit hour in all | from search results of the official page | https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/winter-tuition-and-fees-for-online-academic-programs.non-resident-online.html |
| rate-spring-2027 | Spring 2027, non-resident, full-time graduate: tuition 6785.00 dollars and fees 1003.92 dollars, 7788.92 dollars per semester in all | from search results of the official page | https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/spring-tuition-online-academic-programs.non-resident-online-full-time.html |
| comprehensive-fee-waiver | Students in online academic programs are eligible for a Comprehensive Fee waiver | from search results of the official page | https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/spring-tuition-online-academic-programs.non-resident-online-full-time.html |
| dn-first-phd | Daily Nous reports that the University at Buffalo Department of Philosophy is launching what will be the first PhD program in applied ontology | from a third-party page | https://dailynous.com/2026/05/13/new-doctoral-program-in-applied-ontology/ |
| dn-online-fall | Daily Nous reports that it will be a fully online, asynchronous program, enrolling students from the fall of the article's year | from a third-party page | https://dailynous.com/2026/05/13/new-doctoral-program-in-applied-ontology/ |
| dn-masters | Daily Nous reports that the department introduced an online master's degree in applied ontology the year before the article | from a third-party page | https://dailynous.com/2026/05/13/new-doctoral-program-in-applied-ontology/ |
| programme-tuition | A tuition rate specific to this program | not confirmed | none |
| dissertation | The dissertation requirements | not confirmed | none |
| english-test | The English-test requirement for this PhD | not confirmed | none |
| recommendations | The requirement for letters of recommendation for this PhD | not confirmed | none |
| statement | The requirement for a statement for this PhD | not confirmed | none |
| transcripts | The transcript requirement for this PhD | not confirmed | none |
| master-transfer | Whether credit from a master's degree transfers | not confirmed | none |
| funding | Whether funding is available | not confirmed | none |

### What the owner has, and what can be used, for the doctorate (Applied Ontology)

[data/phd-assets.json](./data/phd-assets.json) holds one entry per item.
The statuses are those of the OMSCS table of what the owner has.
The requirement column tells whether a source read lists the item as a requirement.
The rows column names the rows of the table of requirements that the item rests on.
The doctoral table of assets has 7 items.
The doctoral count is: held 0, in progress 1, not yet 6.
Of the doctoral items, 3 are stated as requirements in the sources read.
No item is marked as held without evidence.

| Item | What | Status | Requirement | How the sources treat it | Rows |
| --- | --- | --- | --- | --- | --- |
| bachelors | A bachelor's degree, in progress and not yet earned. The university is not named | in progress | stated as a requirement in a source read | PhD applicants require an undergraduate degree (from search results) | undergraduate-degree |
| ontology-competence | Competence in some area of applied ontology. Nothing that shows it is held yet. Related facts are listed separately, and they are not claimed to meet the requirement | not yet | stated as a requirement in a source read | PhD applicants must show competence in some area of applied ontology (from search results). What level suffices is not in the sources read | competence |
| tuition | Tuition, to be paid from the owner's savings. The program is pursued once the tuition has been saved. No amount is written | not yet | stated as a requirement in a source read | No tuition rate specific to this program was found in any source. Claude's estimate is in this item's estimate | rate-winter-2026, rate-spring-2027, comprehensive-fee-waiver |
| masters | A master's degree. Not held. The OMSCS master's degree is a separate, earlier aim of this record | not yet | not stated as a requirement in the sources read | The sources read say only that PhD applicants require an undergraduate degree, and do not list a master's degree as a requirement. Whether master's credit transfers was not found | undergraduate-degree, master-transfer |
| english-test | An English test, not yet taken | not yet | requirement not found (not confirmed) | The English-test requirement for this PhD was not found | english-test |
| recommendations | Letters of recommendation. None yet for this PhD | not yet | requirement not found (not confirmed) | The requirement for letters of recommendation for this PhD was not found | recommendations |
| statement | A statement. Not yet written for this PhD | not yet | requirement not found (not confirmed) | The requirement for a statement for this PhD was not found | statement |

### Facts related to competence in applied ontology

The philosophy papers made public and the planned courses are listed, by title only, as facts related to the item on competence in applied ontology.
This record does not say that they meet the requirement.
None of the papers is peer-reviewed.
None of the courses has been taken yet.

| Fact | Kind | Source |
| --- | --- | --- |
| The Nobility and Exemplarity of the Celibate Individual | philosophy paper made public (not peer-reviewed) | the table of papers in cpsbvbng26-dotcom's README.md (read on 2026-11-20, at commit 7cc1521 of main) |
| Manifesto of Imperial Selfhood | philosophy paper made public (not peer-reviewed) | the table of papers in cpsbvbng26-dotcom's README.md (read on 2026-11-20, at commit 7cc1521 of main) |
| Fragmentarian Spiritual Individualism | philosophy paper made public (not peer-reviewed) | the table of papers in cpsbvbng26-dotcom's README.md (read on 2026-11-20, at commit 7cc1521 of main) |
| Machine-mediated Rediscovery: A Case Study in Novelty, Priority, and Self-correction | philosophy paper made public (not peer-reviewed) | the table of papers in cpsbvbng26-dotcom's README.md (read on 2026-11-20, at commit 7cc1521 of main) |
| 記号論理 | course at the owner's university (planned) | data/course-plan.json |
| 集合と論理 | course at the owner's university (planned) | data/course-plan.json |

### Estimate of doctoral tuition

The figures in the table below are Claude's estimate.
The rates are those of the University at Buffalo's tuition pages, as read in search-result summaries.
The estimate assumes that the rates do not change.
Rates are revised.
No tuition rate specific to this program was found in any source.
The graduate rate per credit hour for online academic programs and the full-time graduate rate per semester were therefore used.
The number of semesters is Claude's assumption and is in no source.
The sources read do not give the credit hours of a full-time semester either.
The Comprehensive Fee waiver is not subtracted.
The application fee, books and tests are left out.
No exchange rate was read from a source, so nothing is converted to yen.
The tuition is to be paid from the owner's savings.
The amount of the owner's savings is not written.

| Estimate | Computation | Total |
| --- | --- | --- |
| The rate per credit hour (tuition and fees) for 72 credit hours | 72 × 641.16 | 46163.52 dollars |
| The tuition per credit hour alone for 72 credit hours | 72 × 565.00 | 40680.00 dollars |
| The full-time rate per semester for 6 semesters (the number of semesters is Claude's assumption) | 6 × 7788.92 | 46733.52 dollars |

## MBA plan (University of Wales Trinity Saint David, Human Academy Business School)

This section is the record of the MBA plan.
The programme aimed at is the University of Wales Trinity Saint David (UWTSD) MBA programme.
Human Academy Co., Ltd. runs it in Japan as Human Academy Business School (HABS).
The degree is awarded by the University of Wales Trinity Saint David (UWTSD).
The plan is to take it after the doctorate, in parallel, while research continues.

### The MBA plan decided on 2026-11-26

- After the doctorate, the plan is to take an MBA through the University of Wales Trinity Saint David (UWTSD) MBA programme run by Human Academy Business School.
- The MBA is taken in parallel, while research continues.
- The owner has already spoken with the programme's staff about the work-experience requirement for admission.
- What that requirement says is not written in this record.

This was decided by the owner on 2026-11-26.
The original text of the decision is the entry of [data/progress.json](./data/progress.json) whose `topic` is `mba`.
The Japanese name of the programme follows the spelling on its pages.

### Sources of the MBA record

The pages of mba.athuman.com could not be opened from the environment of this record.
The network setting of this environment did not let the connection through.
Nothing was done to get around the setting.
The facts from the programme's pages were therefore read only in search-result summaries.
Those rows have the status "from search results of the official page".
Each source URL is the page that the search result named as the source of its summary.
The summaries were not compared with the text of the pages.
The statuses mean the same as in the table of the section on application requirements.

### Facts of the MBA programme

[data/mba.json](./data/mba.json) holds one row per fact, each with its source URL, the date it was read, a status and how it was read.
The table of MBA facts has 11 rows.
Of the MBA rows, 11 come from search results of the official pages.
Of the MBA rows, 0 were confirmed on an opened official page.

| Row | Fact | Status | Source |
| --- | --- | --- | --- |
| programme-name | The programme's name is ウェールズ大学トリニティセントデイビッド（UWTSD）MBAプログラム, the University of Wales Trinity Saint David (UWTSD) MBA programme | from search results of the official page | https://mba.athuman.com/admission/application |
| page-title | The page titles include 「英国国立ウェールズ大学トリニティセントデイビッド　MBAプログラム」 | from search results of the official page | https://mba.athuman.com/admission |
| run-by | Human Academy Co., Ltd. offers and runs it in Japan as Human Academy Business School (HABS) | from search results of the official page | https://mba.athuman.com/ |
| degree | The degree awarded is the MBA (Master of Business Administration) | from search results of the official page | https://mba.athuman.com/admission/application |
| awarded-by | The MBA degree is awarded by UWTSD | from search results of the official page | https://mba.athuman.com/ |
| language | All lectures are given in Japanese | from search results of the official page | https://mba.athuman.com/admission/faq |
| online-weekends | Lectures are held online at weekends, mainly on Saturdays, on 3 days a month on average | from search results of the official page | https://mba.athuman.com/admission/faq |
| standard-length | The standard length of the programme is 2 years | from search results of the official page | https://mba.athuman.com/admission |
| max-enrolment | The maximum period of enrolment is 6 years | from search results of the official page | https://mba.athuman.com/admission/faq |
| completion | Completion requires 4 core modules and 2 optional modules, a master's dissertation, and 180 credits in all | from search results of the official page | https://mba.athuman.com/admission/faq |
| intakes | Intakes are in April and October | from search results of the official page | https://mba.athuman.com/admission |

### Not recorded for the MBA

The work-experience requirement for admission is not written in this record.
The owner decided to withhold what it says.
Only the fact that the owner has already spoken with the programme's staff about it is written.
The staff member's name is not written.
No amount of the fees is written.
The address and telephone number of the programme office on the pages are not copied.

## Progress log

[data/progress.json](./data/progress.json) grows in date order and holds the decision of 2026-11-19, the record of 2026-11-20 on the recommendation slots, and the course plan and the doctoral aim decided on the same day.
On the same day the owner reported that the university where the owner is enrolled does not take requests for letters of recommendation.
This was received from the owner and not confirmed on a page.
On 2026-11-21, what strengthens an application without being required was recorded.
On 2026-11-26, the plan for an MBA after the doctorate was recorded.
A row marked as done with a date after the day the check runs fails the check.

## Not recorded

No grades, scores, GPA or other personal academic records, and no affiliation.
No name of the university where the owner is enrolled, no address of its syllabus, and no names of the instructors of its courses.
No amount of the owner's savings, in any currency.
No name, e-mail address or telephone number of the contact on the doctoral program's page.
Nothing of what the MBA's work-experience requirement for admission says, and no amount of its fees.
No name of the MBA programme's staff member.
Nothing about the people to be asked for recommendations, not even their names.
The GPA in the rows of requirements is part of the text of a requirement, not a record of the operator.

## Operator

Takuya Nemoto. ORCID iD [0009-0000-1406-0547](https://orcid.org/0009-0000-1406-0547).

## Errors

[Report an error](https://github.com/cpsbvbng26-dotcom/omscs-preparation/issues/new?template=error-report.yml). Security issues go through [SECURITY.md](./SECURITY.md).

## Checks

```
python3 verification/check.py
python3 verification/check.py --break
```

## Use of a language model

The pages and the code of this repository were written by Claude Code (Anthropic) at the operator's request.
Claude is not an author.
The use of AI in the decision above is about the work for the MOOCs, not about how this record is written.

## Licence

Text and data are [CC BY 4.0](./LICENSE); code is [MIT](./LICENSE-CODE).
