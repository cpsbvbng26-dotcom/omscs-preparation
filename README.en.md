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
On 2026-11-20 the network setting let omscs.gatech.edu and grad.gatech.edu through, and 6 pages were opened and read that day.
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
There are 10 items.
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

## Progress log

[data/progress.json](./data/progress.json) grows in date order and holds the decision of 2026-11-19 and the record of 2026-11-20 on the recommendation slots.
A row marked as done with a date after the day the check runs fails the check.

## Not recorded

No grades, scores, GPA or other personal academic records, and no affiliation.
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
