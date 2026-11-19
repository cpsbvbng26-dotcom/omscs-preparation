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

omscs.gatech.edu cannot be reached from the environment this record was written in, so no row is confirmed on the official page.
There are 13 rows.

| Row | Requirement | Status |
| --- | --- | --- |
| degree | A bachelor's degree, with at least 16 years of education, before matriculation | from search results of the official page |
| field-and-gpa | An undergraduate degree in computer science or a related field and a cumulative GPA of 3.0 or higher are preferred, not required. Applicants who do not meet them are evaluated case by case | from search results of the official page |
| recommenders | Recommendations from three individuals | from search results of the official page |
| resume | A résumé. Without one, the application is not evaluated | from search results of the official page |
| supplemental-questions | Answers to the supplemental questions. The free-form answers have length limits, and the last eight questions are checklist questions | from search results of the official page |
| english-test | International applicants need TOEFL or IELTS-Academic scores, due when the application is completed | from search results of the official page |
| english-minimum | The Institute minimum is a TOEFL iBT total of 90 with at least 19 in each section, or an IELTS overall band of 7.0 | from search results of the official page |
| english-old-faq | An old OMSCS FAQ gave TOEFL 100 | not confirmed |
| toefl-scale | The TOEFL score scale changed in January 2026 | from search results of the official page |
| deadline-fall | The application deadline for Fall matriculation is March 1 | from search results of the official page |
| deadline-spring | The application deadline for Spring matriculation is August 15 | from search results of the official page |
| conditional-admission | Admission is conditional. Passing two foundational courses with a B or better within a year of matriculation gives full admission | from search results of the official page |
| preparation-by-application | The recommended preparation is expected to be complete when the application is submitted. These MOOCs alone are rarely sufficient for applicants without a bachelor's degree in a STEM field | from search results of the official page |

The source URL and how each row was read are in `data/requirements.json`.

## Recommended courses

[data/courses.json](./data/courses.json) lists the courses recommended by the page Preparing Yourself for OMSCS.
There are 13 courses.
A URL is given only where it was verified: so far, only [the edX page of Computing in Python I](https://edx.org/es/learn/python/the-georgia-institute-of-technology-computing-in-python-i-fundamentals-and-procedural-programming).

## Progress log

[data/progress.json](./data/progress.json) grows in date order and holds only the decision of 2026-11-19 so far.
A row marked as done with a date after the day the check runs fails the check.

## Not recorded

No grades, scores, GPA or other personal academic records, and no affiliation.
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
