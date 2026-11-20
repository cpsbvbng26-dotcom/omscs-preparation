# omscs-preparation

[日本語](./README.md)

A dated record of the preparation for an application to Georgia Tech's OMSCS (Online Master of Science in Computer Science).
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

## Progress log

[data/progress.json](./data/progress.json) grows in date order and holds the decision of 2026-11-19, the record of 2026-11-20 on the recommendation slots, and the course plan decided on the same day.
On the same day the owner reported that the university where the owner is enrolled does not take requests for letters of recommendation.
This was received from the owner and not confirmed on a page.
A row marked as done with a date after the day the check runs fails the check.

## Not recorded

No grades, scores, GPA or other personal academic records, and no affiliation.
No name of the university where the owner is enrolled, no address of its syllabus, and no names of the instructors of its courses.
No amount of the owner's savings, in any currency.
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
