#!/usr/bin/env python3
"""The checks of omscs-preparation.

  python3 verification/check.py           every check passes
  python3 verification/check.py --break   every check fails when the thing it watches is broken

The checks of this repository's subject come first: the rows of requirements, the courses, the
progress log, the assets and the recommendation slots, and the agreement of README with the data. The checks shared with the other two
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
# The pages opened and read on 2026-11-20, once the network setting let omscs.gatech.edu and grad.gatech.edu through.
# A row can be confirmed only on one of these, with the page's own sentences in its quotes.
READ_ON = "2026-11-20"
PAGES_READ = {
    "https://omscs.gatech.edu/admission-criteria",
    "https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines",
    "https://omscs.gatech.edu/additional-app-guidelines",
    "https://omscs.gatech.edu/preparing-yourself-omscs",
    "https://omscs.gatech.edu/prospective-student-faqs",
    "https://grad.gatech.edu/english-proficiency",
}
# Evidence in data/assets.json: public URLs that were already in the operator's repositories (cpsbvbng26-dotcom's
# README for the two certificates; its index.html and cv.html for the GitHub page).
EVIDENCE = {
    "https://courses.edx.org/certificates/eac0a01d3d424a32a00114c487288fbc",
    "https://courses.edx.org/certificates/a746620b6d7d45b583cb41b125e5f807",
    "https://github.com/cpsbvbng26-dotcom",
}
ALLOWED_URLS = PAGES_READ | EVIDENCE | {EDX}
URL = re.compile(r"https?://[^\s\"'<>)|]+")
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
    if set(R.get("pages_read", {})) != PAGES_READ:
        bad.append("the pages read are not the six pages opened on 2026-11-20")
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
        seen = r.get("seen_on_2026_11_19")
        # null only for a row added on 2026-11-20 from a page that was read; every older row keeps its answer.
        if not isinstance(seen, bool) and not (seen is None and r.get("status") == "confirmed" and r.get("read_on") == READ_ON):
            bad.append(k + ": seen_on_2026_11_19")
        # A row is confirmed only on a page that was opened and read, on the day it was read, with the page's sentences.
        if r.get("status") == "confirmed":
            if r.get("source") not in PAGES_READ:
                bad.append(k + ": confirmed, but the source is not a page that was read")
            if r.get("read_on") != READ_ON:
                bad.append(k + ": confirmed, but not on the day the pages were read")
            q = r.get("quotes")
            if not isinstance(q, list) or not q or not all(isinstance(x, str) and len(x.strip()) >= 15 for x in q):
                bad.append(k + ": confirmed, but no sentence of the page in quotes")
            if "頁" not in r.get("how", ""):
                bad.append(k + ": confirmed, but the way it was read does not name the page")
        elif r.get("source") in PAGES_READ:
            bad.append(k + ": the page was read, but the row is not confirmed")
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


def section(text, heading):
    """The text from a heading to the next heading of the same or a higher level."""
    i = text.find("\n" + heading + "\n")
    if i < 0:
        return ""
    level = len(heading) - len(heading.lstrip("#"))
    rest = text[i + len(heading) + 2:]
    m = re.search(r"^#{1,%d} " % level, rest, re.M)
    return rest[:m.start()] if m else rest


def table_lines(text):
    return [line for line in text.split("\n") if line.startswith("| ") and not line.startswith("| ---")]


def asset_lines(A, lang):
    """The rows of the table of assets, the slots and the guidance, as each README must show them."""
    sep, none = ("、", "なし") if lang == 0 else (", ", "none")
    sfx = "" if lang == 0 else "_en"
    items = []
    for a in A["items"]:
        srcs = []
        for q in a["official_quotes"]:
            if q["source"] not in srcs:
                srcs.append(q["source"])
        items.append("| %s | %s | %s | %s | %s | %s |" % (
            a["id"], a["what" + sfx], A["statuses"][a["status"]][lang], a["evidence"] or none,
            a["official" + sfx], sep.join(srcs)))
    slots = ["| %d | %s |" % (s["slot"], A["slot_statuses"][s["status"]][lang]) for s in A["recommendation_slots"]]
    guide = []
    for g in A["recommendation_guidance"]:
        srcs = []
        for q in g["quotes"]:
            if q["source"] not in srcs:
                srcs.append(q["source"])
        guide.append("| %s | %s |" % (g["text" + sfx], sep.join(srcs)))
    return items, slots, guide


ASSET_HEADS = (("## いま持っているもの・出願で使えるもの", "### 推薦の枠"),
               ("## What the owner has now, and what can be used in the application", "### Recommendation slots"))


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
    for f, text_key, lang, head in (("README.md", "requirement", 0, "## 出願の要件"),
                                    ("README.en.md", "requirement_en", 1, "## Application requirements")):
        rows = [line.split(" | ") for line in section(F.get(f, ""), head).split("\n")
                if re.match(r"^\| [a-z][a-z-]+ \| ", line)]
        got = [(r[0][2:], r[1], r[2].rstrip(" |")) for r in rows if len(r) == 3]
        want = [(r["id"], r.get(text_key), R["statuses"].get(r["status"], ["?", "?"])[lang]) for r in R["rows"]]
        if got != want or len(rows) != len(got):
            bad.append(f + ": the table of requirements differs from data/requirements.json")
        for status in R["statuses"].values():
            if not re.search(r"^\| " + re.escape(status[lang]) + r" \| [^|]+ \|$", F.get(f, ""), re.M):
                bad.append(f + ": the status " + status[lang] + " is not explained")
    # The table of assets, the slots and the guidance on recommenders are copies of data/assets.json.
    A = jload(F, "data/assets.json")
    for f, lang in (("README.md", 0), ("README.en.md", 1)):
        if not A:
            bad.append("data/assets.json cannot be read")
            break
        try:
            items, slots, guide = asset_lines(A, lang)
        except Exception as e:
            bad.append(f + ": the tables of data/assets.json cannot be made (" + str(e) + ")")
            continue
        sec = section(F.get(f, ""), ASSET_HEADS[lang][0])
        sub_ = section(F.get(f, ""), ASSET_HEADS[lang][1])
        top = sec[:sec.find("\n" + ASSET_HEADS[lang][1] + "\n")] if ASSET_HEADS[lang][1] in sec else sec
        got = [line for line in table_lines(top) if re.match(r"^\| [a-z][a-z0-9-]+ \| ", line)]
        if got != items:
            bad.append(f + ": the table of assets differs from data/assets.json")
        for status in A["statuses"].values():
            if not re.search(r"^\| " + re.escape(status[lang]) + r" \| [^|]+ \|$", top, re.M):
                bad.append(f + ": the status of assets " + status[lang] + " is not explained")
        if [line for line in table_lines(sub_) if re.match(r"^\| \d+ \| ", line)] != slots:
            bad.append(f + ": the slots differ from data/assets.json")
        if [line for line in table_lines(sub_) if re.search(r"\| https://", line)] != guide:
            bad.append(f + ": the guidance on recommenders differs from data/assets.json")
    return bad


def urls_allowed(F):
    """Every URL in data/assets.json is a page that was read, the edX page of courses.json, or evidence already
    in the operator's repositories."""
    t = F.get("data/assets.json", "")
    return ["data/assets.json: a URL not in the allowed list " + u for u in URL.findall(t) if u not in ALLOWED_URLS]


def assets(F):
    A = jload(F, "data/assets.json")
    if not A:
        return ["data/assets.json cannot be read"]
    bad = []
    if set(A.get("statuses", {})) != {"met", "partly", "not-yet"}:
        bad.append("the three statuses of assets")
    ids = [a.get("id") for a in A.get("items", [])]
    if len(ids) != len(set(ids)) or not ids:
        bad.append("an id twice, or no item")
    for a in A.get("items", []):
        k = str(a.get("id", "?"))
        if not re.fullmatch(r"[a-z][a-z0-9-]+", k):
            bad.append(k + ": the id")
        for field in ("what", "what_en", "evidence_note", "official", "official_en"):
            if not str(a.get(field, "")).strip():
                bad.append(k + ": no " + field)
        if a.get("status") not in A.get("statuses", {}):
            bad.append(k + ": the status " + str(a.get("status")))
        if a.get("evidence") is not None and a.get("evidence") not in EVIDENCE:
            bad.append(k + ": evidence that is not already in the operator's repositories")
        if a.get("status") == "met" and a.get("evidence") is None:
            bad.append(k + ": held, but no evidence")
        qs = a.get("official_quotes")
        if not isinstance(qs, list) or not qs:
            bad.append(k + ": no sentence of the official pages")
            qs = []
        for q in qs:
            if q.get("source") not in PAGES_READ or len(str(q.get("quote", "")).strip()) < 15:
                bad.append(k + ": a quote without a page that was read")
        # Whether the edX certificates are verified certificates is not confirmed: the record does not say so.
        if a.get("evidence", "") and "edx.org" in str(a.get("evidence")):
            if "確かめていない" not in a.get("what", "") or "not confirmed" not in a.get("what_en", ""):
                bad.append(k + ": an edX certificate that does not say its kind is not confirmed")
        # What the owner holds carries no personal academic record. The official fields describe requirements.
        for key in ("what", "what_en", "evidence_note"):
            if RECORD_VALUES.search(str(a.get(key, ""))):
                bad.append(k + ": a personal academic record (" + key + ")")
        for key in a:
            if RECORD_KEYS.search(key):
                bad.append(k + ": a field for a personal academic record (" + key + ")")
    for g in A.get("recommendation_guidance", []):
        if not g.get("text") or not g.get("text_en") or not g.get("quotes"):
            bad.append("a guidance row without text or quotes")
        for q in g.get("quotes", []):
            if q.get("source") not in PAGES_READ or len(str(q.get("quote", "")).strip()) < 15:
                bad.append("a guidance quote without a page that was read")
    return bad


# Kinds of detail a slot must not carry: schools and universities, titles and positions, ties to the owner, social
# networks, handles and links. The slots hold only their number and their state (rule 6).
SLOT_WORDS = re.compile(
    r"大学|学校|高校|中学|小学|学園|学院|学部|学科|研究科|研究室|研究所|専攻|ゼミ|教授|講師|助教|教員|教諭|先生|名誉|博士|修士|"
    r"院生|学生|生徒|同級|同期|同窓|先輩|後輩|友人|友達|知人|同僚|上司|恩師|親戚|家族|さん|氏|様|"
    r"univ|college|school|institute|academy|faculty|professor|prof\.|emerit|doctor|doctoral|ph\.?d|dr\.|master|"
    r"student|lecturer|teacher|classmate|alumn|friend|colleague|mentor|cousin|mr\.|ms\.|mrs\.|"
    r"instagram|twitter|x\.com|facebook|linkedin|threads|tiktok|youtube|bluesky|mastodon|discord|note\.com|mixi|"
    r"researchgate|researchmap|orcid|github|@|https?:|www\.", re.I)


def slots(F):
    A = jload(F, "data/assets.json")
    if not A:
        return ["data/assets.json cannot be read"]
    bad = []
    S = A.get("recommendation_slots", [])
    if [s.get("slot") for s in S] != [1, 2, 3]:
        bad.append("the slots are not the three slots 1, 2, 3")
    if set(A.get("slot_statuses", {})) != {"chosen", "undecided"}:
        bad.append("the two states of a slot")
    for s in S:
        if set(s) != {"slot", "status"}:
            bad.append("slot %s: a field other than its number and its state: %s" % (s.get("slot"), sorted(set(s) - {"slot", "status"})))
        if s.get("status") not in A.get("slot_statuses", {}):
            bad.append("slot %s: the state %s" % (s.get("slot"), s.get("status")))
    texts = [json.dumps(S, ensure_ascii=False), json.dumps(A.get("slot_statuses", {}), ensure_ascii=False)]
    for f, head in (("README.md", ASSET_HEADS[0][1]), ("README.en.md", ASSET_HEADS[1][1])):
        texts += [line for line in table_lines(section(F.get(f, ""), head)) if re.match(r"^\| \d+ \| ", line)]
    P = jload(F, "data/progress.json") or {"entries": []}
    texts += [json.dumps(e, ensure_ascii=False) for e in P["entries"] if e.get("date") == "2026-11-20"]
    for t in texts:
        for m in SLOT_WORDS.finditer(rules.norm(t)):
            bad.append("a slot or its record carries a kind of detail it must not: " + m.group(0))
    return bad


COUNTERS = {
    "requirements": lambda F: len((jload(F, "data/requirements.json") or {"rows": []})["rows"]),
    "courses": lambda F: len((jload(F, "data/courses.json") or {"courses": []})["courses"]),
    "confirmed": lambda F: sum(r.get("status") == "confirmed" for r in (jload(F, "data/requirements.json") or {"rows": []})["rows"]),
    "pages_read": lambda F: len((jload(F, "data/requirements.json") or {}).get("pages_read", {})),
    "assets": lambda F: len((jload(F, "data/assets.json") or {"items": []})["items"]),
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
    ("Every asset has what it is, a status of the three, evidence already public or none, and the official pages' sentences", assets),
    ("Every URL in data/assets.json is in the allowed list", urls_allowed),
    ("The recommendation slots hold only their number and state, and nothing about a person", slots),
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


def _no_quotes(G):
    R = json.loads(G["data/requirements.json"])
    R["rows"][0]["quotes"] = []
    G["data/requirements.json"] = json.dumps(R, ensure_ascii=False)


def _how_without_page(G):
    R = json.loads(G["data/requirements.json"])
    R["rows"][0]["how"] = "読んだ。"
    G["data/requirements.json"] = json.dumps(R, ensure_ascii=False)


def _seen_null_not_confirmed(G):
    R = json.loads(G["data/requirements.json"])
    R["rows"].append({"id": "extra", "requirement": "x", "requirement_en": "x", "source": "https://omscs.gatech.edu/apply",
                      "read_on": "2026-11-19", "status": "search", "seen_on_2026_11_19": None, "how": "検索の要約による。"})
    G["data/requirements.json"] = json.dumps(R, ensure_ascii=False)


def _extra_page(G):
    R = json.loads(G["data/requirements.json"])
    R["pages_read"]["https://omscs.gatech.edu/summary"] = "x"
    G["data/requirements.json"] = json.dumps(R, ensure_ascii=False)


def _drop_guidance_row(G):
    lines = G["README.md"].split("\n")
    i = next(n for n, line in enumerate(lines) if line.startswith("| 推薦者は 3 人。"))
    G["README.md"] = "\n".join(lines[:i] + lines[i + 1:])


C = [c[0] for c in CHECKS]
BREAKS = [
    (C[0], "a row without a source", sub("data/requirements.json", '"source": "https://omscs.gatech.edu/admission-criteria",', '"source": "",')),
    (C[0], "a row with a status outside the four", sub("data/requirements.json", '"status": "confirmed"', '"status": "probably"')),
    (C[0], "a row confirmed on a page that was not read", sub("data/requirements.json", '"source": "https://omscs.gatech.edu/admission-criteria",', '"source": "https://omscs.gatech.edu/apply",')),
    (C[0], "a row confirmed without the page's sentences", _no_quotes),
    (C[0], "a row confirmed on a day other than the day the pages were read", sub("data/requirements.json", '"read_on": "2026-11-20"', '"read_on": "2026-11-19"')),
    (C[0], "a row confirmed, but how it was read does not name the page", _how_without_page),
    (C[0], "a page that was read, but the row is left as from search results", sub("data/requirements.json", '"status": "confirmed"', '"status": "search"')),
    (C[0], "a row not confirmed, but with no answer for the search of 2026-11-19", _seen_null_not_confirmed),
    (C[0], "a page added to the pages read", _extra_page),
    (C[0], "a row read on a date in the future", sub("data/requirements.json", '"read_on": "2026-11-20"', '"read_on": "' + FUTURE + '"')),
    (C[0], "a source that is not a Georgia Tech page", sub("data/requirements.json", '"source": "https://grad.gatech.edu/english-proficiency"', '"source": "https://example.org/toefl"')),
    (C[1], "a URL that was not verified", sub("data/courses.json", '"name": "Introduction to Object-Oriented Programming with Java", "area": "CS1331 の教材", "url": null', '"name": "Introduction to Object-Oriented Programming with Java", "area": "CS1331 の教材", "url": "https://www.edx.org/java"')),
    (C[2], "a future date marked as done", _future_entry),
    (C[2], "a grade in the progress log", _grade),
    (C[2], "a GPA in the text of an entry", sub("data/progress.json", "評価を受ける課題は、AI を使わずに仕上げます。", "評価を受ける課題は、AI を使わずに仕上げます。GPA は 3.5 です。")),
    (C[2], "the decision moved off the first entry", sub("data/progress.json", '"kind": "decision"', '"kind": "other"')),
    (C[3], "README changes one item of the decision", sub("README.md", "- AI は、概念の説明を受けるためにだけ使います。", "- AI は、課題にも使います。")),
    (C[3], "README changes the status of a row", sub("README.md", "| english-faq-toefl | OMSCS の FAQ の頁は、留学生に TOEFL 100 以上を求めると書いている | 公式の頁で確かめた |", "| english-faq-toefl | OMSCS の FAQ の頁は、留学生に TOEFL 100 以上を求めると書いている | 確かめていない |")),
    (C[3], "README.en.md changes the text of a requirement", sub("README.en.md", "| deadline-fall | The application deadline for Fall matriculation is March 1 |", "| deadline-fall | The application deadline for Fall matriculation is March 15 |")),
    (C[3], "README.en.md changes the status of a row", sub("README.en.md", "| english-faq-toefl | The OMSCS FAQ page asks international applicants for a TOEFL score of at least 100 | confirmed on the official page |", "| english-faq-toefl | The OMSCS FAQ page asks international applicants for a TOEFL score of at least 100 | from search results of the official page |")),
    (C[3], "README.en.md drops a row", sub("README.en.md", "| deadline-spring | The application deadline for Spring matriculation is August 15 | confirmed on the official page |\n", "")),
    (C[3], "README.md changes the status of an asset", sub("README.md", "| resume | 履歴書（résumé）。この出願のためのものは、まだ書いていない | まだ無い |", "| resume | 履歴書（résumé）。この出願のためのものは、まだ書いていない | 持っている |")),
    (C[3], "README.en.md changes the text of an asset", sub("README.en.md", "| math | Preparation in mathematics (linear algebra, probability, statistics).", "| math | Preparation in mathematics (linear algebra, probability, statistics, calculus).")),
    (C[3], "README.en.md drops the evidence of an asset", sub("README.en.md", "| has it | https://github.com/cpsbvbng26-dotcom |", "| has it | none |")),
    (C[3], "README.md changes the state of a slot", sub("README.md", "| 3 | 決めていない |", "| 3 | 依頼する候補を決めた |")),
    (C[3], "README.en.md drops a slot", sub("README.en.md", "| 3 | not decided |\n", "")),
    (C[3], "README.md drops a row of the guidance on recommenders", _drop_guidance_row),
    (C[3], "README.en.md does not explain a status of assets", sub("README.en.md", "| in progress | Under way and not yet earned |\n", "")),
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
    (C[11], "a count that differs from the data", sub("README.md", "要件の行は 24 行です。", "要件の行は 23 行です。")),
    (C[11], "a count of confirmed rows that differs from the data", sub("README.en.md", "Of them, 24 are confirmed", "Of them, 23 are confirmed")),
    (C[11], "a count of assets that differs from the data", sub("README.md", "項目は 10 件です。", "項目は 11 件です。")),
    (C[11], "a count of pages read that differs from the data", sub("README.md", "開いて読んだ頁は 6 つです。", "開いて読んだ頁は 5 つです。")),
    (C[11], "a number not in the ledger", add("README.md", "\n準備には 2 年かけます。\n")),
    (C[11], "a number in kanji", add("README.md", "\n科目は十三本です。\n")),
    (C[11], "a date not in the ledger", add("README.en.md", "\nDecided on 2026-11-18.\n")),
    (C[12], "README.en.md loses the disclosure", sub("README.en.md", "Claude is not an author.", "Claude helped.")),
    (C[13], "an asset with a status outside the three", sub("data/assets.json", '"status": "met"', '"status": "verified"')),
    (C[13], "an asset held, but without evidence", sub("data/assets.json", '"evidence": "https://courses.edx.org/certificates/eac0a01d3d424a32a00114c487288fbc"', '"evidence": null')),
    (C[13], "evidence that is not already in the operator's repositories", sub("data/assets.json", '"evidence": "https://github.com/cpsbvbng26-dotcom"', '"evidence": "https://courses.edx.org/certificates/eac0a01d3d424a32a00114c487288fbc0"')),
    (C[13], "an edX certificate called verified", sub("data/assets.json", "verified の種類の修了証かどうかは、ここでは確かめていない", "verified の修了証である")),
    (C[13], "an official quote from a page that was not read", sub("data/assets.json", '"source": "https://omscs.gatech.edu/preparing-yourself-omscs"', '"source": "https://omscs.gatech.edu/summary"')),
    (C[13], "an asset without its English text", sub("data/assets.json", '"what_en": "Answers to the supplemental questions, not yet written"', '"what_en": ""')),
    (C[13], "a score of the owner in an asset", sub("data/assets.json", "TOEFL か IELTS の試験。まだ受けていない", "TOEFL か IELTS の試験。得点は 95")),
    (C[13], "a fourth status of assets", sub("data/assets.json", '"not-yet": [', '"maybe": ["x", "x"], "not-yet": [')),
    (C[14], "a URL outside the allowed list", sub("data/assets.json", '"evidence_note": "まだ無い。"', '"evidence_note": "まだ無い。https://example.org/cv"')),
    (C[14], "another edX page", add("data/assets.json", " https://courses.edx.org/certificates/0000")),
    (C[15], "a slot with a name", sub("data/assets.json", '"slot": 1,\n      "status": "chosen"', '"slot": 1,\n      "name": "X",\n      "status": "chosen"')),
    (C[15], "a slot with a state outside the two", sub("data/assets.json", '"status": "undecided"', '"status": "asked"')),
    (C[15], "a fourth slot", sub("data/assets.json", '"recommendation_slots": [', '"recommendation_slots": [{"slot": 4, "status": "undecided"}, ')),
    (C[15], "a title in the state of a slot", sub("data/assets.json", '"依頼する候補を決めた",', '"依頼する候補（教授）を決めた",')),
    (C[15], "an honorary title in the state of a slot", sub("data/assets.json", '"依頼する候補を決めた",', '"依頼する候補（名誉職）を決めた",')),
    (C[15], "a social network in the English state of a slot", sub("data/assets.json", '"a candidate to ask has been chosen"', '"a candidate to ask has been chosen on Instagram"')),
    (C[15], "a doctorate in a slot row of README.md", sub("README.md", "| 2 | 依頼する候補を決めた |", "| 2 | 依頼する候補を決めた（博士） |")),
    (C[15], "a university in a slot row of README.en.md", sub("README.en.md", "| 1 | a candidate to ask has been chosen |", "| 1 | a candidate to ask has been chosen (University) |")),
    (C[15], "a high school in the record of the slots", sub("data/progress.json", "枠には状態だけを書き、人については書きません。", "枠には状態だけを書き、人については書きません。候補は高校で知った人です。")),
]

if __name__ == "__main__":
    sys.exit(rules.run(CHECKS, BREAKS, rules.load(), sys.argv))
