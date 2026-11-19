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
The status is one of: confirmed on the official page, from search results of the official page, from a third-party page, not confirmed.
omscs.gatech.edu cannot be reached from the environment this record was written in, so no row is confirmed on the official page.
There are 13 rows.

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
