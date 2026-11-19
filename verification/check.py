#!/usr/bin/env python3
"""The checks of omscs-preparation.

  python3 verification/check.py           every check passes
  python3 verification/check.py --break   every check fails when the thing it watches is broken

The checks of this repository's subject come first: the rows of requirements, the courses, the
progress log, and the agreement of README with the data. The checks shared with the other two
new repositories (copies of the canonical files, words not written, e-mail addresses, workflows,
CLAUDE.md, the writing rules, the ledger of numbers) are in verification/rules.py.
"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules  # noqa: E402
from rules import add, jload, sub  # noqa: E402

PROSE = ["README.md", "README.en.md"]
OFFICIAL = ("https://omscs.gatech.edu/", "https://grad.gatech.edu/", "https://inta.gatech.edu/")
EDX = ("https://edx.org/es/learn/python/the-georgia-institute-of-technology-computing-in-python-i-"
       "fundamentals-and-procedural-programming")
# Keys and words that would carry a personal academic record. None of them may appear in progress.json.
RECORD_KEYS = re.compile(r"grade|score|gpa|mark|result|成績|点|評定|合否", re.I)
RECORD_VALUES = re.compile(r"\bGPA\b|成績|点数|評定|得点|合否|\bscored?\b", re.I)


def today():
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()


def is_date(s):
    try:
        return datetime.date.fromisoformat(s).isoformat() == s
    except Exception:
        return False


def requirements(F):
    R = jload(F, "data/requirements.json")
    if not R:
        return ["data/requirements.json cannot be read"]
    bad = []
    if set(R["statuses"]) != {"confirmed", "search", "third-party", "unconfirmed"}:
        bad.append("the four statuses")
    ids = [r.get("id") for r in R["rows"]]
    if len(ids) != len(set(ids)):
        bad.append("an id twice")
    for r in R["rows"]:
        k = r.get("id", "?")
        for field in ("requirement", "requirement_en", "source", "read_on", "status", "how"):
            if not str(r.get(field, "")).strip():
                bad.append(k + ": no " + field)
        if r.get("status") not in R["statuses"]:
            bad.append(k + ": the status " + str(r.get("status")))
        if not str(r.get("source", "")).startswith(OFFICIAL):
            bad.append(k + ": the source is not a Georgia Tech page")
        if not is_date(r.get("read_on", "")) or r.get("read_on", "") > today():
            bad.append(k + ": the date read")
        if not isinstance(r.get("seen_on_2026_11_19"), bool):
            bad.append(k + ": seen_on_2026_11_19")
        # omscs.gatech.edu was not reachable: a row cannot say it was confirmed on the page.
        if r.get("status") == "confirmed":
            bad.append(k + ": confirmed on the official page, but no official page was opened")
        if r.get("status") == "search" and "検索" not in r.get("how", ""):
            bad.append(k + ": from search results, but the way it was read does not name the search")
        if r.get("status") == "unconfirmed" and r.get("seen_on_2026_11_19"):
            bad.append(k + ": not confirmed, but seen in the search")
    return bad


def courses(F):
    C = jload(F, "data/courses.json")
    if not C:
        return ["data/courses.json cannot be read"]
    bad = []
    for c in C["courses"]:
        if not c.get("name") or not c.get("area"):
            bad.append(c.get("id", "?") + ": name or area")
        u = c.get("url")
        if u is not None and u not in C["verified_urls"]:
            bad.append(c["id"] + ": a URL that was not verified")
    if list(C["verified_urls"]) != [EDX]:
        bad.append("the verified URLs are not the one edX page")
    if C["courses"][0]["url"] != EDX or not C["courses"][0]["name"].startswith("Computing in Python I:"):
        bad.append("the first course")
    return bad


def progress(F):
    P = jload(F, "data/progress.json")
    if not P:
        return ["data/progress.json cannot be read"]
    bad = []
    E = P["entries"]
    if not E or E[0].get("date") != "2026-11-19" or E[0].get("kind") != "decision":
        bad.append("the first entry is not the decision of 2026-11-19")
    dates = [e.get("date", "") for e in E]
    if dates != sorted(dates):
        bad.append("the entries are not in date order")
    for e in E:
        d = e.get("date", "")
        if not is_date(d):
            bad.append("a date that is not a date: " + str(d))
        if e.get("kind") not in ("decision", "started", "finished", "other"):
            bad.append(d + ": the kind " + str(e.get("kind")))
        if e.get("done") is True and d > today():
            bad.append(d + ": a date in the future marked as done")
        if not isinstance(e.get("done"), bool):
            bad.append(d + ": done")
        if len(e.get("items", [])) != len(e.get("items_en", [])) or not e.get("items"):
            bad.append(d + ": the items in Japanese and English")
        for key, val in e.items():
            if RECORD_KEYS.search(key) or RECORD_VALUES.search(json.dumps(val, ensure_ascii=False)):
                bad.append(d + ": a personal academic record (" + key + ")")
    return bad


def bullets(text, heading):
    i = text.find(heading)
    if i < 0:
        return []
    block = text[i:].split("\n\n", 2)
    return [line[2:] for line in (block[1] if len(block) > 1 else "").split("\n") if line.startswith("- ")]


def readme_and_data(F):
    bad = []
    P = jload(F, "data/progress.json") or {"entries": [{}]}
    R = jload(F, "data/requirements.json") or {"rows": [], "statuses": {}}
    first = P["entries"][0]
    if bullets(F.get("README.md", ""), "## 2026-11-19 に決めたこと") != first.get("items"):
        bad.append("README.md: the decision differs from data/progress.json")
    if bullets(F.get("README.en.md", ""), "## The decision of 2026-11-19") != first.get("items_en"):
        bad.append("README.en.md: the decision differs from data/progress.json")
    # The table of requirements in each README is a copy of data/requirements.json: id, the requirement in that
    # language, and the status in that language. Each README also explains every status in a table of its own.
    for f, text_key, lang in (("README.md", "requirement", 0), ("README.en.md", "requirement_en", 1)):
        rows = [line.split(" | ") for line in F.get(f, "").split("\n")
                if re.match(r"^\| [a-z][a-z-]+ \| ", line)]
        got = [(r[0][2:], r[1], r[2].rstrip(" |")) for r in rows if len(r) == 3]
        want = [(r["id"], r.get(text_key), R["statuses"].get(r["status"], ["?", "?"])[lang]) for r in R["rows"]]
        if got != want or len(rows) != len(got):
            bad.append(f + ": the table of requirements differs from data/requirements.json")
        for status in R["statuses"].values():
            if not re.search(r"^\| " + re.escape(status[lang]) + r" \| [^|]+ \|$", F.get(f, ""), re.M):
                bad.append(f + ": the status " + status[lang] + " is not explained")
    return bad


COUNTERS = {
    "requirements": lambda F: len((jload(F, "data/requirements.json") or {"rows": []})["rows"]),
    "courses": lambda F: len((jload(F, "data/courses.json") or {"courses": []})["courses"]),
}


def orcid_ok(F):
    N = jload(F, "verification/numbers.json") or {"fixed": []}
    bad = []
    for x in N["fixed"]:
        if x.get("check") == "orcid":
            d = x["re"].replace("-", "")
            t = 0
            for c in d[:-1]:
                t = (t + int(c)) * 2
            r = (12 - t % 11) % 11
            if ("X" if r == 10 else str(r)) != d[-1]:
                bad.append("the check digit of the ORCID iD")
    return bad


CHECKS = [
    ("Every row of requirements has a source, a date read, a status and how it was read", requirements),
    ("The courses link only verified pages", courses),
    ("The progress log starts with the decision of 2026-11-19, keeps date order, and has no future date as done and no personal academic record", progress),
    ("Both READMEs agree with the data: the decision, the table of requirements, the statuses", readme_and_data),
    ("Copies of the canonical files and the licences are byte-identical (sha256)", rules.copies),
    ("No name of the operator's own university in any spelling, other place of creative work, self-title, item of rule 10 or single relative", rules.words_not_written),
    ("No e-mail address in any file", rules.no_email),
    ("Workflows: actions pinned to commits, permissions, timeouts; Dependabot", rules.workflows),
    ("labels.yml makes the labels of the canonical workflows", lambda F: rules.labels(F)),
    ("CLAUDE.md carries rules 16, 17 and 18 (10 times)", rules.claude_md),
    ("The writing rules: です/ます, no second person, no bold, one dash per paragraph, short sentences", lambda F: rules.prose(F, PROSE, allow=("Preparing Yourself for OMSCS",))),
    ("Every number in prose is in the ledger of numbers, and every count matches the data", lambda F: rules.numbers(F, PROSE, COUNTERS, ("README.md", "README.en.md")) + orcid_ok(F)),
    ("README.md and README.en.md link each other, disclose the language model and name the licences", rules.readme_pair),
    (".zenodo.json: one creator with the ORCID iD, the licence of LICENSE, the disclosure, the licence sentence, related identifiers found in the repository", rules.zenodo),
]

FUTURE = (datetime.date.today() + datetime.timedelta(days=400)).isoformat()


def _future_entry(G):
    P = json.loads(G["data/progress.json"])
    P["entries"].append({"date": FUTURE, "kind": "finished", "done": True, "items": ["x"], "items_en": ["x"]})
    G["data/progress.json"] = json.dumps(P, ensure_ascii=False)


def _grade(G):
    P = json.loads(G["data/progress.json"])
    P["entries"].append({"date": "2026-11-19", "kind": "finished", "done": True, "items": ["x"], "items_en": ["x"], "grade": "A"})
    G["data/progress.json"] = json.dumps(P, ensure_ascii=False)


C = [c[0] for c in CHECKS]
BREAKS = [
    (C[0], "a row without a source", sub("data/requirements.json", '"source": "https://omscs.gatech.edu/admission-criteria",', '"source": "",')),
    (C[0], "a row with a status outside the four", sub("data/requirements.json", '"status": "unconfirmed"', '"status": "probably"')),
    (C[0], "a row claimed as confirmed on the official page", sub("data/requirements.json", '"status": "unconfirmed"', '"status": "confirmed"')),
    (C[0], "a row read on a date in the future", sub("data/requirements.json", '"read_on": "2026-11-19"', '"read_on": "' + FUTURE + '"')),
    (C[0], "a source that is not a Georgia Tech page", sub("data/requirements.json", "https://grad.gatech.edu/english-proficiency", "https://example.org/toefl")),
    (C[1], "a URL that was not verified", sub("data/courses.json", '"name": "Introduction to Object-Oriented Programming with Java", "area": "CS1331 の教材", "url": null', '"name": "Introduction to Object-Oriented Programming with Java", "area": "CS1331 の教材", "url": "https://www.edx.org/java"')),
    (C[2], "a future date marked as done", _future_entry),
    (C[2], "a grade in the progress log", _grade),
    (C[2], "a GPA in the text of an entry", sub("data/progress.json", "評価を受ける課題は、AI を使わずに仕上げます。", "評価を受ける課題は、AI を使わずに仕上げます。GPA は 3.5 です。")),
    (C[2], "the decision moved off the first entry", sub("data/progress.json", '"kind": "decision"', '"kind": "other"')),
    (C[3], "README changes one item of the decision", sub("README.md", "- AI は、概念の説明を受けるためにだけ使います。", "- AI は、課題にも使います。")),
    (C[3], "README changes the status of a row", sub("README.md", "| english-old-faq | 古い OMSCS の FAQ は、TOEFL 100 と書いていた | 確かめていない |", "| english-old-faq | 古い OMSCS の FAQ は、TOEFL 100 と書いていた | 公式の頁の検索結果から |")),
    (C[3], "README.en.md changes the text of a requirement", sub("README.en.md", "| deadline-fall | The application deadline for Fall matriculation is March 1 |", "| deadline-fall | The application deadline for Fall matriculation is March 15 |")),
    (C[3], "README.en.md changes the status of a row", sub("README.en.md", "| english-old-faq | An old OMSCS FAQ gave TOEFL 100 | not confirmed |", "| english-old-faq | An old OMSCS FAQ gave TOEFL 100 | from search results of the official page |")),
    (C[3], "README.en.md drops a row", sub("README.en.md", "| recommenders | Recommendations from three individuals | from search results of the official page |\n", "")),
    (C[3], "README.en.md does not explain a status", sub("README.en.md", "| from a third-party page | Read on a page that is not official |\n", "")),
    (C[4], "one character of SECURITY.md", sub("SECURITY.md", "7 日以内", "8 日以内")),
    (C[4], "one character of LICENSE-CODE", sub("LICENSE-CODE", "MIT License", "MIT Licence")),
    (C[4], "the note on the copies says the cross-repository check compares them", sub("verification/copies.json", "いま正本と写しを突き合わせるのは、このリポジトリの検査（verification/rules.py の copies）だけです。cpsbvbng26-dotcom の横断の検査（verification/check_ecosystem.js）は、まだこのリポジトリを見ていません。", "cpsbvbng26-dotcom の verification/check_ecosystem.js も、正本と写しを突き合わせます。")),
    (C[5], "the university's name", add("README.md", "\n" + rules.dec("WkVO") + rules.dec("5aSn5a2m") + "\n")),
    (C[5], "the university's name, romanised", add("README.md", "\n" + rules.dec("emVu") + " " + rules.dec("ZGFpZ2FrdQ==") + "\n")),
    (C[5], "the university's name in hiragana", add("README.md", "\n" + rules.dec("44Gc44KT") + rules.dec("44Gg44GE44GM44GP") + "\n")),
    (C[5], "the university's name in katakana, spelt out", add("README.md", "\n" + rules.dec("44K844Oz") + rules.dec("44OA44Kk44Ks44Kv") + "\n")),
    (C[5], "the other place of creative work", add("data/progress.json", rules.OTHER_PLACE[0])),
    (C[5], "a self-title", add("README.en.md", "\n" + rules.dec("SW5kZXBlbmRlbnQ=") + " " + rules.dec("UmVzZWFyY2hlcg==") + "\n")),
    (C[5], "a word for a single relative", add("README.md", "\n" + rules.RELATIVES[0] + "\n")),
    (C[6], "an e-mail address", add("data/courses.json", "someone" + "@" + "example.org")),
    (C[7], "an action named by its version", sub(".github/workflows/check.yml", "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1", "actions/checkout@v7")),
    (C[7], "the check workflow writes", sub(".github/workflows/check.yml", "contents: read", "contents: write")),
    (C[7], "a job without a timeout", sub(".github/workflows/check.yml", "    timeout-minutes: 10\n", "")),
    (C[8], "labels.yml drops a label", sub(".github/workflows/labels.yml", 'gh label create "not verified"', 'gh label create "unverified"')),
    (C[9], "CLAUDE.md goes back to 3 times", sub("CLAUDE.md", "**合っているかを、最低 10 回確かめる。**", "**合っているかを、最低 3 回確かめる。**")),
    (C[10], "a sentence not in です/ます", add("README.md", "\n記録は日付の順に足す。\n")),
    (C[10], "an instruction to the reader", add("README.md", "\n要件は公式の頁で確かめてください。\n")),
    (C[10], "bold", sub("README.md", "決めたことと、したことだけを書きます。", "**決めたことと、したことだけを書きます。**")),
    (C[10], "you in English", add("README.en.md", "\nYou can read the data.\n")),
    (C[11], "a count that differs from the data", sub("README.md", "要件の行は 13 行です。", "要件の行は 12 行です。")),
    (C[11], "a number not in the ledger", add("README.md", "\n準備には 2 年かけます。\n")),
    (C[11], "a number in kanji", add("README.md", "\n科目は十三本です。\n")),
    (C[11], "a date not in the ledger", add("README.en.md", "\nDecided on 2026-11-18.\n")),
    (C[12], "README.en.md loses the disclosure", sub("README.en.md", "Claude is not an author.", "Claude helped.")),
    (C[13], ".zenodo.json loses the disclosure", sub(".zenodo.json", "Claude is not an author.", "Claude helped.")),
    (C[13], ".zenodo.json gives an affiliation", sub(".zenodo.json", '"orcid": "0009-0000-1406-0547"', '"orcid": "0009-0000-1406-0547", "affiliation": "x"')),
    (C[13], ".zenodo.json names the MIT licence", sub(".zenodo.json", '"license": "cc-by-4.0"', '"license": "mit"')),
    (C[13], ".zenodo.json drops the name of the repository from the title", sub(".zenodo.json", '"title": "omscs-preparation: ', '"title": "')),
    (C[13], ".zenodo.json names another repository in the title", sub(".zenodo.json", '"title": "omscs-preparation: ', '"title": "self-correction: ')),
    (C[13], ".zenodo.json gives a contributor an affiliation and says no affiliation elsewhere", sub(".zenodo.json", '"upload_type": ', '"contributors": [{"name": "x", "type": "Other", "affiliation": "y"}], "comment": "no affiliation", "upload_type": ')),
]

if __name__ == "__main__":
    sys.exit(rules.run(CHECKS, BREAKS, rules.load(), sys.argv))
