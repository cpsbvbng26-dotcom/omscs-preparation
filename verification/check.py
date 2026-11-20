#!/usr/bin/env python3
"""The checks of omscs-preparation.

  python3 verification/check.py           every check passes
  python3 verification/check.py --break   every check fails when the thing it watches is broken

The checks of this repository's subject come first: the rows of requirements, the courses, the
progress log, the assets and the recommendation slots, the agreement of README with the data, the course plan at the owner's
university (and the words it must not carry), the tuition item with its estimate, and the doctoral record (University at
Buffalo, PhD in Applied Ontology). The checks shared with the other two
new repositories (copies of the canonical files, words not written, e-mail addresses, workflows,
CLAUDE.md, the writing rules, the ledger of numbers) are in verification/rules.py.
"""
import datetime
import json
import os
import re
import sys
from decimal import Decimal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules  # noqa: E402
from rules import add, jload, sub  # noqa: E402

PROSE = ["README.md", "README.en.md"]
OFFICIAL = ("https://omscs.gatech.edu/", "https://grad.gatech.edu/", "https://inta.gatech.edu/")
EDX = ("https://edx.org/es/learn/python/the-georgia-institute-of-technology-computing-in-python-i-"
       "fundamentals-and-procedural-programming")
# The pages opened and read on 2026-11-20, once the network setting let omscs.gatech.edu and grad.gatech.edu through.
# A row can be confirmed only on one of these, with the page's own sentences in its quotes. The Bursar's page of tuition and
# fee rates was read on the same day; it is the source of the tuition item of data/assets.json, not of a requirement.
READ_ON = "2026-11-20"
PAGES_READ = {
    "https://omscs.gatech.edu/admission-criteria",
    "https://omscs.gatech.edu/deadlines-decisions-requirements-and-guidelines",
    "https://omscs.gatech.edu/additional-app-guidelines",
    "https://omscs.gatech.edu/preparing-yourself-omscs",
    "https://omscs.gatech.edu/prospective-student-faqs",
    "https://grad.gatech.edu/english-proficiency",
    "https://bursar.gatech.edu/tuition-fees",
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
        bad.append("the pages read are not the seven pages opened on 2026-11-20")
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


# Items that may be held on the owner's own report, without evidence. The owner reported on 2026-11-20 that current savings
# cover the estimated tuition; no amount and no evidence is kept. No other item is held without evidence.
SELF_REPORTED = {"tuition"}


def self_reported(a):
    sr = a.get("self_report")
    return (a.get("id") in SELF_REPORTED and isinstance(sr, dict) and set(sr) == {"by", "reported_on"}
            and sr.get("by") == "owner" and is_date(sr.get("reported_on", "")) and sr["reported_on"] <= today()
            and "申告" in a.get("what", "") and "self-report" in a.get("what_en", ""))


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
        if a.get("status") == "met" and a.get("evidence") is None and not self_reported(a):
            bad.append(k + ": held, but no evidence")
        if "self_report" in a and (a.get("evidence") is not None or not self_reported(a)):
            bad.append(k + ": a self-report that is not one of the owner, dated, on an item allowed to be self-reported")
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
    # Every entry of 2026-11-20 but the doctoral decision, which phd_decision checks to carry nothing about the slots.
    texts += [json.dumps(e, ensure_ascii=False) for e in P["entries"] if e.get("date") == "2026-11-20" and e.get("topic") != "doctorate"]
    for t in texts:
        for m in SLOT_WORDS.finditer(rules.norm(t)):
            bad.append("a slot or its record carries a kind of detail it must not: " + m.group(0))
    return bad


# ------------------------------------------------------------------ the course plan at the owner's university

PREP = "https://omscs.gatech.edu/preparing-yourself-omscs"
PLAN_SOURCE = ("在籍する大学の公開のシラバス（2026-11-20 に読んだ。大学の名とアドレスは決めごと 5 により書かない）",
               "the public syllabus of the university where the owner is enrolled (read on 2026-11-20; "
               "the university's name and address are not written, by rule 5)")
# The items of preparation that the Preparing Yourself for OMSCS page names, with the page's own sentences, read on
# 2026-11-20. A row of the plan serves exactly one of them.
COMPETENCIES = {
    "programming": "The fundamentals of programming.",
    "oop": "Object-oriented design principles such as encapsulation, abstraction, polymorphism, and inheritance.",
    "data-structures": "Data structures such as lists, stacks, queues, trees, and hashmaps.",
    "algorithms": "Algorithms such as AVL, MST, Dijkstra’s, and dynamic programming.",
    "languages": "Familiarity with multiple programming languages is recommended.",
    "body-of-knowledge": "Find 2-4 upper-level (i.e., junior, senior, or graduate level) courses of interest that cover some of "
                         "these areas and demonstrate the ability to earn a B or better in those courses.",
    "math": "In addition to CS knowledge, some classes in the OMSCS program—especially in the artificial intelligence and "
            "machine learning areas—require a solid background in advanced mathematics, especially linear algebra, "
            "probability, and statistics.",
}
PLAN_GROUPS = {"programming", "dsa", "oop", "languages", "systems", "theory", "networks", "data-security", "ai-ml", "math"}
PLAN_ROW_KEYS = {"title", "category", "offered", "group", "competency", "source", "reason", "reason_en", "status"}
PLAN_HEADS = ("## 在籍する大学の科目の履修計画", "## Planned courses at the owner's university")
GAP_HEADS = ("### 確かめていないこと・足りないところ", "### What was not checked, and gaps")
PLAN_STATUS = ["履修計画中", "planned"]


def plan_load(F):
    return jload(F, "data/course-plan.json")


def course_plan(F):
    D = plan_load(F)
    if not D:
        return ["data/course-plan.json cannot be read"]
    bad = []
    if (D.get("source"), D.get("source_en")) != PLAN_SOURCE:
        bad.append("the source is not described in the fixed words")
    if D.get("read_on") != READ_ON or D.get("decided_on") != READ_ON:
        bad.append("the syllabus was read, and the plan decided, on 2026-11-20")
    if D.get("statuses") != {"planned": PLAN_STATUS}:
        bad.append("the only status is 履修計画中 / planned")
    S = D.get("syllabus", {})
    if set(S) != {"information", "mathematics"}:
        bad.append("the two categories of the syllabus")
    for k, cat in S.items():
        h = cat.get("title_sha256", [])
        if not h or len(h) != len(set(h)) or not all(re.fullmatch(r"[0-9a-f]{64}", x) for x in h):
            bad.append(k + ": the sha256 of the syllabus titles")
    C = D.get("competencies", {})
    if set(C) != set(COMPETENCIES):
        bad.append("the competencies are not the items of the preparation page")
    for k, c in C.items():
        if c.get("quote") != COMPETENCIES.get(k) or c.get("source") != PREP or not c.get("ja") or not c.get("en"):
            bad.append(k + ": the competency is not the page's item, in its words, with the page's URL")
    G = D.get("groups", {})
    if set(G) != PLAN_GROUPS:
        bad.append("the groups")
    for k, g in G.items():
        if g.get("competency") not in COMPETENCIES or not g.get("ja") or not g.get("en"):
            bad.append(k + ": a group without a competency of the page")
    rows = D.get("rows", [])
    titles = [r.get("title") for r in rows]
    if not rows or len(titles) != len(set(titles)):
        bad.append("no row, or a title twice")
    for r in rows:
        t = str(r.get("title"))
        if set(r) != PLAN_ROW_KEYS:
            bad.append(t + ": the fields of a row " + str(sorted(set(r) ^ PLAN_ROW_KEYS)))
        if rules.sha(t) not in S.get(r.get("category"), {}).get("title_sha256", []):
            bad.append(t + ": not a title of the syllabus read, in its category")
        if not re.fullmatch(r"20\d\d年度開講", str(r.get("offered"))):
            bad.append(t + ": the year marker of the syllabus")
        if r.get("status") != "planned":
            bad.append(t + ": a status other than 履修計画中")
        if r.get("group") not in G or r.get("competency") != G.get(r.get("group"), {}).get("competency"):
            bad.append(t + ": the group and its competency")
        if r.get("competency") not in COMPETENCIES:
            bad.append(t + ": a competency outside the page's items")
        if r.get("source") != PREP:
            bad.append(t + ": the competency is not given with the preparation page's URL")
        if not str(r.get("reason", "")).endswith("。") or not str(r.get("reason_en", "")).strip():
            bad.append(t + ": the reason")
        for key, val in r.items():
            if RECORD_KEYS.search(key) or RECORD_VALUES.search(str(val)):
                bad.append(t + ": a personal academic record (" + key + ")")
    used = {r.get("competency") for r in rows}
    gaps = {g.get("id"): g for g in D.get("gaps", [])}
    if set(gaps) != {"algorithms", "year", "upper-level", "transcript"}:
        bad.append("the gaps are not the four recorded")
    # The gap on algorithms says no course names them; it stays exactly while no row serves that item.
    if ("algorithms" in used) == ("algorithms" in gaps):
        bad.append("a row serves the item on algorithms, and the gap still says none does, or the reverse")
    for k, g in gaps.items():
        if not g.get("text") or not g.get("text_en"):
            bad.append(k + ": a gap without its text in both languages")
        for q in g.get("quotes", []):
            if q.get("source") not in PAGES_READ or q.get("quote", "") not in g.get("text", ""):
                bad.append(k + ": a quote not from a page read, or not in the text")
    for u in URL.findall(F.get("data/course-plan.json", "")):
        if u not in PAGES_READ:
            bad.append("data/course-plan.json: a URL not read " + u)
    P = jload(F, "data/progress.json") or {"entries": []}
    dec_ = [e for e in P["entries"] if e.get("date") == READ_ON and e.get("kind") == "decision"]
    if not dec_ or not re.search(r"に挙げた %d 科目を、履修計画中" % len(rows), " ".join(dec_[0].get("items", []))) \
            or "the %d courses listed in data/course-plan.json" % len(rows) not in " ".join(dec_[0].get("items_en", [])):
        bad.append("the decision of 2026-11-20 does not name the plan and its number of rows")
    return bad


def plan_lines(D, lang):
    sfx = "" if lang == 0 else "_en"
    lab = "ja" if lang == 0 else "en"
    comps = ["| %s | %s | %s |" % (k, c[lab], c["source"]) for k, c in D["competencies"].items()]
    rows = []
    for r in D["rows"]:
        y = re.fullmatch(r"(\d{4})年度開講", r["offered"])
        off = r["offered"] if lang == 0 else "academic year " + (y.group(1) if y else "?")
        rows.append("| %s | %s | %s | %s | %s | %s |" % (r["title"], off, D["groups"][r["group"]][lab], r["competency"],
                                                         r["reason" + sfx], D["statuses"][r["status"]][lang]))
    gaps = [g["text" + sfx] for g in D["gaps"]]
    return comps, rows, gaps


def plan_readme(F):
    D = plan_load(F)
    if not D:
        return ["data/course-plan.json cannot be read"]
    bad = []
    for f, lang in (("README.md", 0), ("README.en.md", 1)):
        try:
            comps, rows, gaps = plan_lines(D, lang)
        except Exception as e:
            bad.append(f + ": the tables of data/course-plan.json cannot be made (" + str(e) + ")")
            continue
        sec = section(F.get(f, ""), PLAN_HEADS[lang])
        if not sec:
            bad.append(f + ": no section " + PLAN_HEADS[lang])
            continue
        if PLAN_SOURCE[lang] not in sec:
            bad.append(f + ": the source is not described in the fixed words")
        top = sec[:sec.find("\n" + GAP_HEADS[lang] + "\n")] if GAP_HEADS[lang] in sec else sec
        lines = table_lines(top)
        if [x for x in lines if x.endswith(" | " + PREP + " |")] != comps:
            bad.append(f + ": the table of competencies differs from data/course-plan.json")
        if [x for x in lines if x.endswith(" | " + PLAN_STATUS[lang] + " |")] != rows:
            bad.append(f + ": the table of planned courses differs from data/course-plan.json")
        if len(lines) != 2 + len(comps) + len(rows):
            bad.append(f + ": a table row that is not in data/course-plan.json")
        if bullets(sec, GAP_HEADS[lang]) != gaps:
            bad.append(f + ": the gaps differ from data/course-plan.json")
    return bad


# Words that the course plan must not carry, kept in base64 like rules.SCHOOL: the names of the company and partners behind
# a course unique to the owner's university, the name of that course, and the syllabus site's address.
PLAN_WORDS = [rules.dec(x) for x in ("44OJ44Ov44Oz44K0", "ZHdhbmdv", "cGl4aXY=", "44Ky44Oz44Ot44Oz", "Z2Vucm9u", "5p2+5bC+56CU",
                                     "44K/44Kk44OS44Of44Ol", "dGVpY2ht", "5a6H5a6Z6Zqb", "c3lsbGFidXMuemVu")]


def instructor_hits(F, names):
    """The files in which some substring, normalised as the names were, hashes to one of the names."""
    hs = set(names.get("sha256", []))
    hits = []
    for f, t in F.items():
        if f in rules.SELF or f == "verification/excluded-names.json":
            continue
        n = re.sub(r"\s+", "", rules.norm(t))
        for L in names.get("lengths", []):
            if any(rules.sha(n[i:i + L]) in hs for i in range(len(n) - L + 1)):
                hits.append(f)
                break
    return hits


def plan_words(F):
    bad = []
    N = jload(F, "verification/excluded-names.json") or {}
    H = N.get("sha256", [])
    if len(H) != 36 or len(set(H)) != 36 or not all(re.fullmatch(r"[0-9a-f]{64}", x) for x in H) or not N.get("lengths"):
        bad.append("verification/excluded-names.json does not hold the 36 hashed names and their lengths")
    for f, t in F.items():
        if f in rules.SELF:
            continue
        n = rules.norm(t)
        if any(r.search(n) for r in rules.SCHOOL):
            bad.append(f + ": the name or the domain of the owner's university")
        for w in PLAN_WORDS:
            if rules.norm(w) in n:
                bad.append(f + ": a word of the forbidden list of the course plan")
    bad += [f + ": the name of an instructor" for f in instructor_hits(F, N)]
    return bad


# ------------------------------------------------------------------ tuition: the rates read, Claude's estimate, no amount of the owner's

BURSAR = "https://bursar.gatech.edu/tuition-fees"
FAQ = "https://omscs.gatech.edu/prospective-student-faqs"
OMSCS_ROW = re.compile(r"^Master of Science in Computer Science \(OMSCS\) \| \$(\d+) \| \$(\d+) \| \$(\d+) \| \$(\d+) \| \$(\d+)$")
FAQ_TUITION = "Generally, students pay tuition per credit hour of enrollment, as well as fees per semester of enrollment."
FAQ_HOURS = re.compile(r"^(\d+) credit hours are required to graduate\.$")
FAQ_COURSE = "Therefore someone taking two courses at three credit hours each can expect to spend roughly 18 hours per week on coursework."
# An amount in yen, in figures or in kanji, or a figure in the same sentence as a word for savings. Written with escapes so that
# this file does not itself carry them.
YEN = re.compile("\\d[\\d,.]*\\s*[\u4e07\u5343\u767e\u5104]?\\s*\u5186|[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\u4e07\u5104]+\u5186|"
                 "[\u00a5\uffe5]\\s*\\d|\\d\\s*(?:yen|jpy)\\b|\\b(?:yen|jpy)\\s*\\d", re.I)
SAVINGS = re.compile("\u8caf|\u9810\u91d1|\u8cc7\u7523|\u6240\u6301\u91d1|\u624b\u6301\u3061|\\bsavings?\\b|\\bsaved\\b|\\bbalance\\b", re.I)
FIGURE = re.compile("\\d|[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\u4e07\u5104]+(?:\u5186|\u4e07)")


def tuition_item(F):
    A = jload(F, "data/assets.json") or {"items": []}
    return next((a for a in A.get("items", []) if a.get("id") == "tuition"), None)


def tuition_rates(F):
    """The rates as the pages give them: from the row of the Bursar's table and the FAQ's sentences, not from the estimate."""
    a = tuition_item(F) or {}
    qs = [q.get("quote", "") for q in a.get("official_quotes", [])]
    row = next((OMSCS_ROW.match(q) for q in qs if OMSCS_ROW.match(q)), None)
    hours = next((FAQ_HOURS.match(q) for q in qs if FAQ_HOURS.match(q)), None)
    if not row or not hours or FAQ_COURSE not in qs:
        return None
    r = {"rate": int(row.group(3)), "fee_small": int(row.group(4)), "fee_large": int(row.group(5)),
         "hours": int(hours.group(1)), "per_course": 3}
    r["tuition"] = r["hours"] * r["rate"]
    for n in (1, 2):
        h = n * r["per_course"]
        r["semesters_%d" % n] = r["hours"] // h if r["hours"] % h == 0 else None
        fee = r["fee_small"] if h < 4 else r["fee_large"]
        r["total_%d" % n] = r["semesters_%d" % n] * (h * r["rate"] + fee) if r["semesters_%d" % n] else None
    return r


def tuition_texts(F):
    """The tuition item, its rows in both READMEs, and the README sections on the estimate."""
    a = tuition_item(F)
    out = [json.dumps(a, ensure_ascii=False)] if a else []
    for f, head in (("README.md", TUITION_HEADS[0]), ("README.en.md", TUITION_HEADS[1])):
        out += [x for x in F.get(f, "").split("\n") if x.startswith("| tuition | ")]
        out.append(section(F.get(f, ""), head))
    return out


TUITION_HEADS = ("### 学費の見積もり", "### Estimate of tuition")


def tuition(F):
    a = tuition_item(F)
    if not a:
        return ["no tuition item in data/assets.json"]
    bad = []
    if a.get("status") != "met" or a.get("evidence") is not None or not self_reported(a):
        bad.append("tuition: held on the owner's report of 2026-11-20, without evidence")
    srcs = {q.get("source") for q in a.get("official_quotes", [])}
    if srcs != {BURSAR, FAQ}:
        bad.append("tuition: the sources are the Bursar's page and the FAQ page")
    if FAQ_TUITION not in [q.get("quote") for q in a.get("official_quotes", [])]:
        bad.append("tuition: the FAQ's sentence on tuition per credit hour and fees per semester")
    r = tuition_rates(F)
    E = a.get("estimate", {})
    if not r:
        bad.append("tuition: the rates cannot be read from the quotes of the pages")
    else:
        want = {"tuition_per_credit_hour": r["rate"], "fee_fewer_than_4": r["fee_small"], "fee_4_or_more": r["fee_large"],
                "credit_hours": r["hours"], "credit_hours_per_course": r["per_course"], "tuition_total": r["tuition"],
                "plans": [{"courses_per_semester": 1, "semesters": r["semesters_1"], "total": r["total_1"]},
                          {"courses_per_semester": 2, "semesters": r["semesters_2"], "total": r["total_2"]}]}
        for k, v in want.items():
            if E.get(k) != v:
                bad.append("tuition: the estimate's %s is %s, the pages give %s" % (k, E.get(k), v))
        for key in ("official", "official_en"):
            for v in (r["rate"], r["fee_small"], r["fee_large"], r["hours"], r["tuition"], r["total_1"], r["total_2"]):
                if not re.search(r"(?<![\d,])%d(?![\d,])" % v, a.get(key, "")):
                    bad.append("tuition: %s does not carry %d" % (key, v))
    for f, head in (("README.md", TUITION_HEADS[0]), ("README.en.md", TUITION_HEADS[1])):
        if not section(F.get(f, ""), head).strip():
            bad.append(f + ": no section " + head)
    if E.get("by") != "Claude" or E.get("currency") != "USD":
        bad.append("tuition: the estimate is Claude's own, in dollars")
    note = E.get("note", "") + a.get("official", "")
    note_en = E.get("note_en", "") + a.get("official_en", "")
    if not all(w in note for w in ("Claude", "改定", "出願料", "為替")) or \
            not all(w in note_en for w in ("Claude", "revised", "application fee", "exchange rate")):
        bad.append("tuition: the estimate does not say it is Claude's, that rates are revised, what it leaves out, and why no yen")
    # No amount of the owner's money: no amount in yen anywhere, and no figure beside a word for savings in the item or its rows.
    for f, t in F.items():
        if f not in rules.SELF and YEN.search(rules.norm(t)):
            bad.append(f + ": an amount in yen")
    for t in tuition_texts(F):
        for sentence in re.split(r"[\u3002\n|]|\.\s", t):
            if SAVINGS.search(sentence) and FIGURE.search(sentence):
                bad.append("tuition: a figure beside a word for savings「" + sentence[:30] + "」")
    return bad



# ------------------------------------------------------------------ the doctorate: University at Buffalo, PhD in Applied Ontology

# The pages of www.buffalo.edu could not be opened on 2026-11-20: Akamai answered every automated request with Access Denied
# (HTTP 403), and nothing was bypassed. Facts from them come only from search-result summaries; these are the pages that the
# search results named as their sources. The only page opened and read for the doctorate is the Daily Nous article.
PHD_REQ = "data/phd-requirements.json"
PHD_ASSETS = "data/phd-assets.json"
UB_SEARCH = {
    "https://www.buffalo.edu/grad/programs/applied-ontology-phd.html",
    "https://www.buffalo.edu/news/releases/2026/05/ontology-phd.html",
    "https://www.buffalo.edu/cas/philosophy/graduate/admissions.html",
    "https://www.buffalo.edu/cas/philosophy/graduate/phd-ontology.html",
    "https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/"
    "winter-tuition-and-fees-for-online-academic-programs.non-resident-online.html",
    "https://www.buffalo.edu/studentaccounts/tuition-and-fees/tuition-for-online-academic-programs/"
    "spring-tuition-online-academic-programs.non-resident-online-full-time.html",
}
DN = "https://dailynous.com/2026/05/13/new-doctoral-program-in-applied-ontology/"
PHD_URLS = UB_SEARCH | {DN}
# The sentences of the Daily Nous article, word for word, as read on 2026-11-20 (the article writes Master’s with U+2019).
DN_QUOTES = {
    "The University at Buffalo Department of Philosophy is launching what will be the first PhD program in applied ontology.",
    "It will be a fully online, asynchronous program, and it will enroll students starting this fall.",
    "The department introduced an online Master’s degree in applied ontology last year.",
}
# The philosophy papers that cpsbvbng26-dotcom's README.md lists (read on 2026-11-20, main at 7cc1521), by title only.
PAPERS = {
    "The Nobility and Exemplarity of the Celibate Individual",
    "Manifesto of Imperial Selfhood",
    "Fragmentarian Spiritual Individualism",
    "Machine-mediated Rediscovery: A Case Study in Novelty, Priority, and Self-correction",
}
PHD_COURSES = {"記号論理", "集合と論理"}
PHD_ITEMS = {"bachelors", "ontology-competence", "tuition", "masters", "english-test", "recommendations", "statement"}
PHD_HEADS = ("## 博士課程の準備（University at Buffalo、応用オントロジー）",
             "## Doctoral preparation (University at Buffalo, Applied Ontology)")
PHD_DECISION_HEADS = ("### 2026-11-20 に決めた博士課程の目標", "### The doctoral decision of 2026-11-20")
PHD_UNREACHABLE = ("www.buffalo.edu の頁は、この作業の環境から開けませんでした。",
                   "The pages of www.buffalo.edu could not be opened from the environment of this record.")
PHD_TABLE_HEADS = (("| 行 | 要件 | 状態 | 出典 |", "| 項目 | 何か | 状態 | 要件 | 要件の扱い | 要件の行 |",
                    "| 事実 | 種類 | 出典 |", "| 見積もり | 計算 | 合計 |"),
                   ("| Row | Requirement | Status | Source |", "| Item | What | Status | Requirement | How the sources treat it | Rows |",
                    "| Fact | Kind | Source |", "| Estimate | Computation | Total |"))
CLAIM = re.compile(r"世界で唯一|world[’']s only|only university", re.I)
CLAIM_MARK = ("大学自身の主張", "the university's own claim")
CLAIM_NOTE = ("独立の確認は", "no independent confirmation was found")
CLAIM_PROSE = ("独立の確認は、見つけていません。", "No independent confirmation was found.")
PHONE = re.compile(r"\(?\b\d{3}\)?[\s.\-]\d{3}[\s.\-]\d{4}\b|\+\d[\d\s\-]{7,}\d|\btel:", re.I)
CONTACT_KEYS = re.compile(r"^(contact|e-?mail|mail|phone|telephone|tel|fax|person|people)$", re.I)
# Words for a person's title or post, and the names of the people who appear on the Daily Nous page (its author and a person
# named in its comments), kept in base64 like rules.SCHOOL so that this file does not carry them.
PERSON = re.compile(r"\bprof(?:essor)?\b|\bdr\.|\bdirector\b|\bcoordinator\b|\bmr\.|\bms\.|\bmrs\.|教授|先生|担当者|氏名|"
                    + rules.dec("V2VpbmJlcmc=") + "|" + rules.dec("QmFycnkgU21pdGg="), re.I)
SAVINGS_KEYS = re.compile(r"saving|balance|deposit|貯|預金|資産|所持", re.I)


def phd_load(F):
    return jload(F, PHD_REQ), jload(F, PHD_ASSETS)


def phd_rows(F):
    return {r.get("id"): r for r in ((jload(F, PHD_REQ) or {}).get("rows", []))}


def phd_entry(F):
    P = jload(F, "data/progress.json") or {"entries": []}
    return [e for e in P["entries"] if e.get("topic") == "doctorate"]


def strings(x):
    """Every string in a JSON value, keys left out."""
    if isinstance(x, str):
        return [x]
    if isinstance(x, dict):
        return [s for v in x.values() for s in strings(v)]
    if isinstance(x, list):
        return [s for v in x for s in strings(v)]
    return []


def keys(x):
    if isinstance(x, dict):
        return list(x) + [k for v in x.values() for k in keys(v)]
    if isinstance(x, list):
        return [k for v in x for k in keys(v)]
    return []


def phd_texts(F):
    """The doctoral record: both data files, the decision in progress.json, and the doctoral section of each README.
    Each is a list of strings: the strings of the JSON, or the lines of the section."""
    out = []
    for p in (PHD_REQ, PHD_ASSETS):
        out.append((p, strings(jload(F, p) or {})))
    out.append(("data/progress.json", strings(phd_entry(F))))
    for f, head in (("README.md", PHD_HEADS[0]), ("README.en.md", PHD_HEADS[1])):
        out.append((f, section(F.get(f, ""), head).split("\n")))
    return out


def phd_requirements(F):
    R = jload(F, PHD_REQ)
    if not R:
        return [PHD_REQ + " cannot be read"]
    bad = []
    O = jload(F, "data/requirements.json") or {}
    if R.get("statuses") != O.get("statuses"):
        bad.append("the statuses are not the four of data/requirements.json, in the same words")
    if set(R.get("pages_read", {})) != {DN}:
        bad.append("the pages read are not the one Daily Nous article")
    ids = [r.get("id") for r in R.get("rows", [])]
    if not ids or len(ids) != len(set(ids)):
        bad.append("no row, or an id twice")
    for r in R.get("rows", []):
        k = str(r.get("id", "?"))
        if not re.fullmatch(r"[a-z][a-z0-9-]+", k):
            bad.append(k + ": the id")
        for field in ("requirement", "requirement_en", "read_on", "status", "how"):
            if not str(r.get(field, "")).strip():
                bad.append(k + ": no " + field)
        if "source" not in r:
            bad.append(k + ": no source")
        st, src = r.get("status"), r.get("source")
        if st not in R.get("statuses", {}):
            bad.append(k + ": the status " + str(st))
        if r.get("read_on") != READ_ON or r.get("read_on", "") > today():
            bad.append(k + ": the date read is not 2026-11-20")
        # No page of the university was opened, so no row is confirmed on the official page.
        if st == "confirmed":
            bad.append(k + ": confirmed on the official page, but no page of www.buffalo.edu was opened")
        if src in UB_SEARCH and st != "search":
            bad.append(k + ": a page known only from search results, but the status is " + str(st))
        if st == "search":
            if src not in UB_SEARCH:
                bad.append(k + ": from search results, but the source is not a page that the search results named")
            if "検索" not in r.get("how", "") or "開けなかった" not in r.get("how", ""):
                bad.append(k + ": from search results, but how it was read does not say so, or that the page could not be opened")
            if "quotes" in r:
                bad.append(k + ": from search results, but it carries quotes as if the page had been read")
        if "search_words" in r and (st != "search" or not all(isinstance(x, str) and x.strip() for x in r["search_words"])):
            bad.append(k + ": search words on a row that is not from search results")
        if st == "third-party":
            if src != DN:
                bad.append(k + ": from a third-party page, but not the Daily Nous article")
            q = r.get("quotes")
            if not isinstance(q, list) or not q or not set(q) <= DN_QUOTES:
                bad.append(k + ": the quotes are not the article's sentences, word for word")
        if src == DN and st != "third-party":
            bad.append(k + ": the Daily Nous article, but not from a third-party page")
        if st == "unconfirmed" and src is not None:
            bad.append(k + ": not confirmed, but with a source")
        if st != "unconfirmed" and src is None:
            bad.append(k + ": no source, but not marked as not confirmed")
        am = r.get("amounts")
        if am is not None:
            try:
                ok = Decimal(am["tuition"]) + Decimal(am["fees"]) == Decimal(am["total"])
            except Exception:
                ok = False
            if not ok or am.get("per") not in ("credit-hour", "semester"):
                bad.append(k + ": tuition and fees do not add up to the total")
            for v in (am.get("tuition"), am.get("fees"), am.get("total")):
                if str(v) not in r.get("requirement", "") or str(v) not in r.get("requirement_en", ""):
                    bad.append(k + ": the text does not carry the amount " + str(v))
    rows = phd_rows(F)
    dl = rows.get("deadlines", {})
    if dl.get("may_be_stale") is not True or "古いかもしれない" not in dl.get("requirement", "") \
            or "may be out of date" not in dl.get("requirement_en", ""):
        bad.append("deadlines: the row does not say that the deadlines may be out of date")
    ch = rows.get("credit-hours", {})
    n = (ch.get("figures") or {}).get("credit_hours")
    if not isinstance(n, int) or str(n) not in ch.get("requirement", "") or str(n) not in ch.get("requirement_en", ""):
        bad.append("credit-hours: the number of credit hours is not in the row's text")
    return bad


def phd_assets(F):
    R, A = phd_load(F)
    if not A:
        return [PHD_ASSETS + " cannot be read"]
    bad = []
    O = jload(F, "data/assets.json") or {}
    if A.get("statuses") != O.get("statuses"):
        bad.append("the statuses are not the three of data/assets.json, in the same words")
    K = A.get("requirement_kinds", {})
    if set(K) != {"stated", "not-stated", "not-found"} or not all(len(v) == 2 and all(v) for v in K.values()):
        bad.append("the three kinds of requirement")
    rows = phd_rows(F)
    items = A.get("items", [])
    ids = [a.get("id") for a in items]
    if len(ids) != len(set(ids)) or set(ids) != PHD_ITEMS:
        bad.append("the items are not the seven recorded, once each")
    for a in items:
        k = str(a.get("id", "?"))
        for field in ("what", "what_en", "note", "note_en"):
            if not str(a.get(field, "")).strip():
                bad.append(k + ": no " + field)
        if a.get("status") not in A.get("statuses", {}):
            bad.append(k + ": the status " + str(a.get("status")))
        if a.get("requirement") not in K:
            bad.append(k + ": the kind of requirement " + str(a.get("requirement")))
        if a.get("evidence") is not None and a.get("evidence") not in EVIDENCE:
            bad.append(k + ": evidence that is not already in the operator's repositories")
        if a.get("status") == "met" and a.get("evidence") is None:
            bad.append(k + ": held, but no evidence")
        rr = a.get("requirement_rows")
        if not isinstance(rr, list) or not rr or not all(x in rows for x in rr):
            bad.append(k + ": the rows of requirements it rests on")
            rr = []
        sts = [rows[x].get("status") for x in rr]
        if a.get("requirement") == "stated" and not any(s in ("search", "third-party") for s in sts):
            bad.append(k + ": stated as a requirement, but on no row that a source gave")
        if a.get("requirement") == "not-found" and any(s != "unconfirmed" for s in sts):
            bad.append(k + ": the requirement not found, but a row with a source is named")
        for key in ("what", "what_en", "note", "note_en"):
            if RECORD_VALUES.search(str(a.get(key, ""))):
                bad.append(k + ": a personal academic record (" + key + ")")
        for key in keys(a):
            if RECORD_KEYS.search(key):
                bad.append(k + ": a field for a personal academic record (" + key + ")")
    by = {a.get("id"): a for a in items}
    b = by.get("bachelors", {})
    if b.get("status") != "partly" or b.get("requirement") != "stated":
        bad.append("bachelors: in progress, and stated as a requirement")
    m = by.get("masters", {})
    if m.get("requirement") != "not-stated" or "OMSCS" not in m.get("what", "") or "OMSCS" not in m.get("what_en", ""):
        bad.append("masters: not stated as a requirement, with OMSCS as the separate earlier aim")
    t = by.get("tuition", {})
    if t.get("status") != "not-yet" or "貯え" not in t.get("what", "") or "savings" not in t.get("what_en", ""):
        bad.append("tuition: not yet, paid from savings once saved")
    c = by.get("ontology-competence", {})
    if c.get("status") != "not-yet" or "要件を満たすとはしない" not in c.get("what", "") \
            or "not claimed to meet the requirement" not in c.get("what_en", ""):
        bad.append("ontology-competence: not yet, and the related facts are not claimed to meet the requirement")
    RK = c.get("related_kinds", {})
    if set(RK) != {"paper", "course"} or not all(len(v) == 4 and all(v) for v in RK.values()):
        bad.append("ontology-competence: the two kinds of related fact")
    rel = c.get("related", [])
    papers = {x.get("title") for x in rel if x.get("kind") == "paper"}
    courses = {x.get("title") for x in rel if x.get("kind") == "course"}
    if papers != PAPERS or courses != PHD_COURSES or len(rel) != len(PAPERS) + len(PHD_COURSES) \
            or any(set(x) != {"kind", "title"} for x in rel):
        bad.append("ontology-competence: the related facts are not the four papers and the two planned courses, by title only")
    plan = {r.get("title"): r.get("status") for r in (plan_load(F) or {}).get("rows", [])}
    for x in courses:
        if plan.get(x) != "planned":
            bad.append("ontology-competence: " + str(x) + " is not a planned course of data/course-plan.json")
    return bad


def money(x):
    return Decimal(x).quantize(Decimal("0.01"))


def phd_tuition(F):
    rows = phd_rows(F)
    t = {a.get("id"): a for a in (jload(F, PHD_ASSETS) or {}).get("items", [])}.get("tuition")
    if not t or not rows:
        return ["no doctoral tuition item, or no rows"]
    bad = []
    E = t.get("estimate", {})
    if E.get("by") != "Claude" or E.get("currency") != "USD":
        bad.append("the estimate is Claude's own, in dollars")
    n = (rows.get(E.get("credit_hours_row"), {}).get("figures") or {}).get("credit_hours")
    plans = {p.get("id"): p for p in E.get("plans", [])}
    if set(plans) != {"per-credit-hour", "per-credit-hour-tuition-only", "full-time-semesters"}:
        bad.append("the three plans of the estimate")
    for k, p in plans.items():
        am = rows.get(p.get("row"), {}).get("amounts") or {}
        try:
            if money(p["rate"]) != money(am[p["part"]]) or p["rate"] != am[p["part"]]:
                bad.append(k + ": the rate is not the row's " + str(p.get("part")))
            if p["total"] != str(money(Decimal(p["units"]) * Decimal(p["rate"]))):
                bad.append(k + ": the total is not units times rate")
        except Exception as e:
            bad.append(k + ": the plan cannot be computed (" + str(e) + ")")
        per = am.get("per")
        if per == "credit-hour" and p.get("units") != n:
            bad.append(k + ": the credit hours are not those of the row " + str(E.get("credit_hours_row")))
        if per == "semester" and (p.get("units_assumed_by") != "Claude" or "Claude の仮定" not in p.get("label", "")
                                  or "Claude's assumption" not in p.get("label_en", "")):
            bad.append(k + ": the number of semesters is not marked as Claude's assumption")
        if per not in ("credit-hour", "semester"):
            bad.append(k + ": the row has no rate per credit hour or per semester")
    if plans.get("per-credit-hour-tuition-only", {}).get("part") != "tuition" or \
            any(plans.get(x, {}).get("part") != "total" for x in ("per-credit-hour", "full-time-semesters")):
        bad.append("the parts of the rates used")
    note, note_en = E.get("note", ""), E.get("note_en", "")
    if not all(w in note for w in ("Claude", "仮定", "改定", "出願料", "為替", "円", "Comprehensive Fee")) or \
            not all(w in note_en for w in ("Claude", "assuming", "revised", "application fee", "exchange rate", "yen",
                                           "Comprehensive Fee")):
        bad.append("the estimate does not say it is Claude's, what it assumes and leaves out, and why no yen")
    for f, head in (("README.md", PHD_EST_HEADS[0]), ("README.en.md", PHD_EST_HEADS[1])):
        if not section(F.get(f, ""), head).strip():
            bad.append(f + ": no section " + head)
    return bad


PHD_EST_HEADS = ("### 博士課程の学費の見積もり", "### Estimate of doctoral tuition")


def phd_money(F):
    """No amount of the owner's money: no figure in a sentence that names savings, no field for savings, no amount in yen."""
    bad = []
    for f, texts in phd_texts(F):
        for t in texts:
            if YEN.search(rules.norm(t)):
                bad.append(f + ": an amount in yen")
            for s in re.split(r"[。|]|\.\s|\.$", t):
                if SAVINGS.search(s) and FIGURE.search(s):
                    bad.append(f + ": a figure beside a word for savings「" + s.strip()[:30] + "」")
    for p, x in ((PHD_ASSETS, jload(F, PHD_ASSETS)), (PHD_REQ, jload(F, PHD_REQ)), ("data/progress.json", phd_entry(F))):
        for k in keys(x or {}):
            if SAVINGS_KEYS.search(k):
                bad.append(p + ": a field for the owner's money (" + k + ")")
    t = {a.get("id"): a for a in (jload(F, PHD_ASSETS) or {}).get("items", [])}.get("tuition", {})
    if set(t) - {"id", "what", "what_en", "status", "requirement", "requirement_rows", "evidence", "note", "note_en", "estimate"}:
        bad.append("tuition: a field other than those recorded")
    return bad


def phd_contact(F):
    """No e-mail address, telephone number, contact field or person's name or title in the doctoral record."""
    bad = []
    for f, texts in phd_texts(F):
        for t in texts:
            if rules.EMAIL.search(t) or rules.MAILTO.search(t):
                bad.append(f + ": an e-mail address")
            if PHONE.search(t):
                bad.append(f + ": a telephone number")
            m = PERSON.search(rules.norm(t))
            if m:
                bad.append(f + ": a person's name or title: " + m.group(0))
    for p, x in ((PHD_ASSETS, jload(F, PHD_ASSETS)), (PHD_REQ, jload(F, PHD_REQ)), ("data/progress.json", phd_entry(F))):
        for k in keys(x or {}):
            if CONTACT_KEYS.search(k):
                bad.append(p + ": a field for a contact (" + k + ")")
    return bad


def phd_claim(F):
    """UB's description of itself as the world's only university with graduate degrees in applied ontology is marked, wherever it
    appears, as the university's own claim, without independent confirmation."""
    bad = []
    rows = [r for r in (jload(F, PHD_REQ) or {}).get("rows", []) if CLAIM.search(r.get("requirement", "") + r.get("requirement_en", ""))]
    if not rows:
        bad.append("no row carries the claim")
    for r in rows:
        if r.get("claim") != {"by": "university", "independently_confirmed": False} or r.get("status") != "search":
            bad.append(str(r.get("id")) + ": the claim is not marked as the university's, unconfirmed, from search results")
        if CLAIM_MARK[0] not in r.get("requirement", "") or CLAIM_NOTE[0] + "見つけていない" not in r.get("requirement", ""):
            bad.append(str(r.get("id")) + ": the Japanese text does not say it is the university's own claim, not confirmed")
        if CLAIM_MARK[1] not in r.get("requirement_en", "") or CLAIM_NOTE[1] not in r.get("requirement_en", ""):
            bad.append(str(r.get("id")) + ": the English text does not say it is the university's own claim, not confirmed")
    for f in sorted(F):
        if f in rules.SELF or f == "verification/check.py":
            continue
        lang = 1 if f.endswith(".en.md") else 0
        for n, line in enumerate(F[f].split("\n"), 1):
            if CLAIM.search(line) and not any(m in line for m in CLAIM_MARK):
                bad.append("%s %d: the claim without the mark of the university's own claim" % (f, n))
        if f.startswith("README") and CLAIM.search(F[f]):
            prose_ = [x for x in section(F[f], PHD_HEADS[lang]).split("\n") if not x.startswith("|")]
            if any(CLAIM.search(x) for x in prose_) and CLAIM_PROSE[lang] not in prose_:
                bad.append(f + ": the claim without the sentence that no independent confirmation was found")
            if not any(CLAIM.search(x) for x in prose_):
                bad.append(f + ": the doctoral section does not say in prose that the claim is the university's own")
    return bad


def phd_lines(F, lang):
    """The lines that each README's doctoral section must show, made from the data."""
    R, A = phd_load(F)
    sfx = "" if lang == 0 else "_en"
    sep, none = ("、", "なし") if lang == 0 else (", ", "none")
    req = ["| %s | %s | %s | %s |" % (r["id"], r["requirement" + sfx], R["statuses"][r["status"]][lang], r["source"] or none)
           for r in R["rows"]]
    items = ["| %s | %s | %s | %s | %s | %s |" % (a["id"], a["what" + sfx], A["statuses"][a["status"]][lang],
                                                   A["requirement_kinds"][a["requirement"]][lang], a["note" + sfx],
                                                   sep.join(a["requirement_rows"])) for a in A["items"]]
    c = next(a for a in A["items"] if a["id"] == "ontology-competence")
    rel = ["| %s | %s | %s |" % (x["title"], c["related_kinds"][x["kind"]][lang], c["related_kinds"][x["kind"]][2 + lang])
           for x in c["related"]]
    t = next(a for a in A["items"] if a["id"] == "tuition")
    est = ["| %s | %d × %s | %s %s |" % (p["label" + sfx], p["units"], p["rate"], p["total"], "ドル" if lang == 0 else "dollars")
           for p in t["estimate"]["plans"]]
    return req, items, rel, est


def phd_readme(F):
    bad = []
    E = phd_entry(F)
    for f, lang in (("README.md", 0), ("README.en.md", 1)):
        sec = section(F.get(f, ""), PHD_HEADS[lang])
        if not sec:
            bad.append(f + ": no section " + PHD_HEADS[lang])
            continue
        try:
            req, items, rel, est = phd_lines(F, lang)
        except Exception as e:
            bad.append(f + ": the tables of the doctoral data cannot be made (" + str(e) + ")")
            continue
        H = PHD_TABLE_HEADS[lang]
        want = [H[0]] + req + [H[1]] + items + [H[2]] + rel + [H[3]] + est
        if table_lines(sec) != want:
            bad.append(f + ": the doctoral tables differ from the data")
        if not E or bullets(sec, PHD_DECISION_HEADS[lang]) != E[0].get("items" if lang == 0 else "items_en"):
            bad.append(f + ": the doctoral decision differs from data/progress.json")
        if PHD_UNREACHABLE[lang] not in sec:
            bad.append(f + ": no note that www.buffalo.edu could not be opened")
    return bad


def phd_urls(F):
    bad = []
    for f, texts in phd_texts(F):
        for t in texts:
            for u in URL.findall(t):
                if u not in PHD_URLS:
                    bad.append(f + ": a URL that is neither a page named by the search results nor the article read " + u)
    return bad


def phd_decision(F):
    bad = []
    E = phd_entry(F)
    if len(E) != 1:
        return ["the doctoral decision is not one entry of data/progress.json"]
    e = E[0]
    if e.get("date") != READ_ON or e.get("kind") != "decision" or e.get("done") is not True:
        bad.append("the doctoral decision is a decision of 2026-11-20")
    ja, en = " ".join(e.get("items", [])), " ".join(e.get("items_en", []))
    if not all(w in ja for w in ("University at Buffalo", "PhD in Applied Ontology", "貯え")) or \
            not all(w in en for w in ("University at Buffalo", "PhD in Applied Ontology", "savings")):
        bad.append("the doctoral decision does not name the programme and its funding from savings")
    if any(re.search(r"\d", s) for s in e.get("items", []) + e.get("items_en", [])):
        bad.append("a figure in the items of the doctoral decision")
    # The check of the recommendation slots leaves this entry out; it must then carry nothing about the slots.
    if re.search(r"推薦|枠|recommend|slot", json.dumps(e, ensure_ascii=False), re.I):
        bad.append("the doctoral decision carries something about the recommendation slots")
    return bad


def phd_parity(F):
    """The doctoral record says the same in Japanese and English: in the data, and in the two README sections."""
    bad = []
    R, A = phd_load(F)
    for r in (R or {}).get("rows", []):
        if not str(r.get("requirement", "")).strip() or not str(r.get("requirement_en", "")).strip():
            bad.append(str(r.get("id")) + ": a row without its text in both languages")
    for a in (A or {}).get("items", []):
        for x, y in (("what", "what_en"), ("note", "note_en")):
            if not str(a.get(x, "")).strip() or not str(a.get(y, "")).strip():
                bad.append(str(a.get("id")) + ": an item without %s in both languages" % x)
        for p in a.get("estimate", {}).get("plans", []):
            if not p.get("label") or not p.get("label_en"):
                bad.append(str(p.get("id")) + ": a plan without its label in both languages")
    for e in phd_entry(F):
        if len(e.get("items", [])) != len(e.get("items_en", [])):
            bad.append("the doctoral decision: the items in Japanese and English")
    secs = [section(F.get(f, ""), h) for f, h in (("README.md", PHD_HEADS[0]), ("README.en.md", PHD_HEADS[1]))]
    ids = [[line.split(" | ")[0][2:] for line in table_lines(s) if re.match(r"^\| [a-z][a-z0-9-]+ \| ", line)] for s in secs]
    if ids[0] != ids[1] or not ids[0]:
        bad.append("the two README sections do not show the same rows in the same order")
    heads = [re.findall(r"^### .*$", s, re.M) for s in secs]
    if len(heads[0]) != len(heads[1]):
        bad.append("the two README sections do not have the same subsections")
    if len(table_lines(secs[0])) != len(table_lines(secs[1])):
        bad.append("the two README sections do not have the same number of table rows")
    N = jload(F, "verification/numbers.json") or {"counts": []}
    for name in sorted({c["count"] for c in N["counts"] if c["count"].startswith("phd_")}):
        res = [c["re"] for c in N["counts"] if c["count"] == name]
        for s, lang in zip(secs, ("README.md", "README.en.md")):
            if not any(re.search(x, line) for x in res for line in rules.bare(s).split("\n")):
                bad.append(lang + ": the doctoral count %s is not given" % name)
    if len({c["count"] for c in N["counts"] if c["count"].startswith("phd_")}) == 0:
        bad.append("no doctoral count in verification/numbers.json")
    return bad


def _phd_count(key, val):
    return lambda F: sum(1 for a in (jload(F, PHD_ASSETS) or {}).get("items", []) if a.get(key) == val)


def _phd_status(val):
    return lambda F: sum(1 for r in (jload(F, PHD_REQ) or {}).get("rows", []) if r.get("status") == val)


COUNTERS = {
    "requirements": lambda F: len((jload(F, "data/requirements.json") or {"rows": []})["rows"]),
    "courses": lambda F: len((jload(F, "data/courses.json") or {"courses": []})["courses"]),
    "confirmed": lambda F: sum(r.get("status") == "confirmed" for r in (jload(F, "data/requirements.json") or {"rows": []})["rows"]),
    "pages_read": lambda F: len((jload(F, "data/requirements.json") or {}).get("pages_read", {})),
    "assets": lambda F: len((jload(F, "data/assets.json") or {"items": []})["items"]),
    "plan_rows": lambda F: len((plan_load(F) or {"rows": []})["rows"]),
    "syllabus_information": lambda F: len((plan_load(F) or {}).get("syllabus", {}).get("information", {}).get("title_sha256", [])),
    "syllabus_mathematics": lambda F: len((plan_load(F) or {}).get("syllabus", {}).get("mathematics", {}).get("title_sha256", [])),
}
COUNTERS.update({
    "phd_rows": lambda F: len((jload(F, PHD_REQ) or {}).get("rows", [])),
    "phd_confirmed": _phd_status("confirmed"),
    "phd_search": _phd_status("search"),
    "phd_third": _phd_status("third-party"),
    "phd_unconfirmed": _phd_status("unconfirmed"),
    "phd_pages_read": lambda F: len((jload(F, PHD_REQ) or {}).get("pages_read", {})),
    "phd_items": lambda F: len((jload(F, PHD_ASSETS) or {}).get("items", [])),
    "phd_met": _phd_count("status", "met"),
    "phd_partly": _phd_count("status", "partly"),
    "phd_notyet": _phd_count("status", "not-yet"),
    "phd_stated": _phd_count("requirement", "stated"),
})
for _k in ("rate", "fee_small", "fee_large", "hours", "tuition", "semesters_1", "total_1", "semesters_2", "total_2"):
    COUNTERS["tuition_" + _k] = (lambda k: lambda F: (tuition_rates(F) or {}).get(k))(_k)


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
    ("The course plan: every title is a syllabus title, the status is planned, each competency is an item of the preparation page", course_plan),
    ("Both READMEs show the course plan, its competencies and its gaps as the data has them", plan_readme),
    ("No name or domain of the owner's university, word of the plan's forbidden list or instructor's name in any file", plan_words),
    ("Tuition: held on the owner's report, the rates as the pages give them, Claude's estimate recomputed, no amount in yen or of savings", tuition),
    ("Doctorate: every row has a status of the four, a search-result row is never confirmed, the article's sentences word for word", phd_requirements),
    ("Doctorate: every asset has a status of the three and the rows it rests on; the related facts are not claimed to meet the requirement", phd_assets),
    ("Doctorate: Claude's estimate of tuition recomputed from the rates of the rows", phd_tuition),
    ("Doctorate: no amount of the owner's money, no figure beside savings", phd_money),
    ("Doctorate: no e-mail address, telephone number, contact field or person's name or title", phd_contact),
    ("Doctorate: the claim of being the world's only university is marked as the university's own, not confirmed", phd_claim),
    ("Doctorate: both READMEs show the decision, the requirements, the assets and the estimate as the data has them", phd_readme),
    ("Doctorate: every URL is a page named by the search results or the article read", phd_urls),
    ("Doctorate: the decision of 2026-11-20 is one entry, names the programme and its funding, and carries no figure", phd_decision),
    ("Doctorate: Japanese and English say the same, in the data and in the README sections", phd_parity),
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


def _plan(G, fn):
    D = json.loads(G["data/course-plan.json"])
    fn(D)
    G["data/course-plan.json"] = json.dumps(D, ensure_ascii=False)


def _tuition(G, fn):
    A = json.loads(G["data/assets.json"])
    fn(next(a for a in A["items"] if a["id"] == "tuition"))
    G["data/assets.json"] = json.dumps(A, ensure_ascii=False)


def _fake_instructor(G):
    # A made-up name, hashed and added as the real names were; the break then writes the name in README.md with a space.
    import unicodedata
    N = json.loads(G["verification/excluded-names.json"])
    N["sha256"].append(rules.sha(re.sub(r"\s+", "", unicodedata.normalize("NFKC", "\u5c71\u7530 \u592a\u90ce").casefold())))
    N["sha256"].pop(0)
    G["verification/excluded-names.json"] = json.dumps(N, ensure_ascii=False)
    G["README.md"] += "\n\u5c71\u7530　\u592a\u90ce\n"


def _drop_name(G):
    N = json.loads(G["verification/excluded-names.json"])
    N["sha256"].pop()
    G["verification/excluded-names.json"] = json.dumps(N, ensure_ascii=False)


def _plan_row_status(D):
    D["rows"][3]["status"] = "履修済み"


def _plan_row_title(D):
    D["rows"][0]["title"] = "Pythonプログラミング2"


def _plan_row_category(D):
    D["rows"][0]["category"] = "mathematics"


def _plan_competency_outside(D):
    D["rows"][5]["competency"] = "systems-programming"


def _plan_competency_quote(D):
    D["competencies"]["oop"]["quote"] = "Object-oriented design principles."


def _plan_extra_competency(D):
    D["competencies"]["networking"] = {"ja": "x", "en": "x", "source": PREP, "quote": "x"}


def _plan_algorithms_row(D):
    D["groups"]["dsa"]["competency"] = "algorithms"
    D["rows"][1]["competency"] = "algorithms"


def _plan_drop_hash(D):
    h = rules.sha(D["rows"][0]["title"])
    D["syllabus"][D["rows"][0]["category"]]["title_sha256"].remove(h)


def _plan_grade(D):
    D["rows"][0]["grade"] = "A"


def _plan_second_status(D):
    D["statuses"]["taken"] = ["履修済み", "taken"]


def _plan_url(D):
    D["rows"][0]["source"] = "https://omscs.gatech.edu/summary"


def _tuition_no_self_report(a):
    del a["self_report"]


def _tuition_yen(a):
    a["evidence_note"] += "\u8caf\u3048\u306f 300 \u4e07\u5186\u3002"


def _tuition_savings_figure(a):
    a["what_en"] += ". Current savings are 20000 dollars"


def _tuition_estimate(a):
    a["estimate"]["plans"][1]["total"] = 10094


def _tuition_rate(a):
    a["official_quotes"][0]["quote"] = a["official_quotes"][0]["quote"].replace("$248", "$250")


def _tuition_official_number(a):
    a["official"] = a["official"].replace("9560", "9650")


def _self_report_elsewhere(G):
    A = json.loads(G["data/assets.json"])
    A["items"][0]["self_report"] = {"by": "owner", "reported_on": "2026-11-20"}
    G["data/assets.json"] = json.dumps(A, ensure_ascii=False)


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
    (C[11], "a count of assets that differs from the data", sub("README.md", "項目は 11 件です。", "項目は 12 件です。")),
    (C[11], "a count of pages read that differs from the data", sub("README.md", "開いて読んだ頁は 7 つです。", "開いて読んだ頁は 6 つです。")),
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
    (C[16], "a planned course with a status other than 履修計画中", lambda G: _plan(G, _plan_row_status)),
    (C[16], "a planned title that is not a syllabus title", lambda G: _plan(G, _plan_row_title)),
    (C[16], "a planned title in the wrong category of the syllabus", lambda G: _plan(G, _plan_row_category)),
    (C[16], "the syllabus title's hash removed", lambda G: _plan(G, _plan_drop_hash)),
    (C[16], "a competency outside the page's items", lambda G: _plan(G, _plan_competency_outside)),
    (C[16], "a competency whose quote is not the page's sentence", lambda G: _plan(G, _plan_competency_quote)),
    (C[16], "a competency added that the page does not name", lambda G: _plan(G, _plan_extra_competency)),
    (C[16], "a row serves algorithms while the gap says none does", lambda G: _plan(G, _plan_algorithms_row)),
    (C[16], "a grade in a planned course", lambda G: _plan(G, _plan_grade)),
    (C[16], "a second status", lambda G: _plan(G, _plan_second_status)),
    (C[16], "a competency given with a URL other than the preparation page", lambda G: _plan(G, _plan_url)),
    (C[16], "the source described otherwise", sub("data/course-plan.json", "大学の名とアドレスは決めごと 5 により書かない", "大学の名は書かない")),
    (C[16], "the decision of 2026-11-20 names another number of courses", sub("data/progress.json", "に挙げた 25 科目を", "に挙げた 24 科目を")),
    (C[17], "README.md changes the reason of a course", sub("README.md", "| 統計学入門 | 2026年度開講 |", "| 統計学入門 | 2027年度開講 |")),
    (C[17], "README.en.md drops a planned course", lambda G: G.__setitem__("README.en.md", "\n".join(x for x in G["README.en.md"].split("\n") if not x.startswith("| 数理統計 | ")))),
    (C[17], "README.md adds a course that is not in the data", sub("README.md", "| 数理統計 | ", "| 群論 | 2026年度開講 | 理論 | body-of-knowledge | x | 履修計画中 |\n| 数理統計 | ")),
    (C[17], "README.en.md changes a competency's label", sub("README.en.md", "| programming | The fundamentals of programming |", "| programming | Programming |")),
    (C[17], "README.md changes a gap", sub("README.md", "- 科目ごとの履修想定年次は、確かめていません。", "- 科目ごとの履修想定年次は、一年次です。")),
    (C[17], "README.en.md drops the description of the source", sub("README.en.md", ", by rule 5)", ")")),
    (C[18], "the university's name in the course plan", lambda G: G.__setitem__("data/course-plan.json", G["data/course-plan.json"] + rules.dec("WkVO") + rules.dec("5aSn5a2m"))),
    (C[18], "the university's domain in README.en.md", add("README.en.md", "\n" + rules.dec("c3lsbGFidXMuemVu") + ".ac.jp\n")),
    (C[18], "the company behind a course", add("README.md", "\n" + PLAN_WORDS[0] + "\n")),
    (C[18], "a partner in Latin letters", add("data/course-plan.json", PLAN_WORDS[2].upper())),
    (C[18], "a partner in katakana", add("README.md", "\n" + PLAN_WORDS[3] + "\n")),
    (C[18], "the laboratory", add("README.en.md", "\n" + PLAN_WORDS[5] + "\n")),
    (C[18], "the unique course's name", add("data/course-plan.json", PLAN_WORDS[8] + PLAN_WORDS[6])),
    (C[18], "an instructor's name, hashed as the real ones are", _fake_instructor),
    (C[18], "a hashed name removed", _drop_name),
    (C[18], "a hashed name that is not a sha256", sub("verification/excluded-names.json", '"sha256": [\n    "', '"sha256": [\n    "0')),
    (C[19], "tuition held without the owner's report", lambda G: _tuition(G, _tuition_no_self_report)),
    (C[19], "an amount in yen in the tuition item", lambda G: _tuition(G, _tuition_yen)),
    (C[19], "a figure beside savings in the tuition item", lambda G: _tuition(G, _tuition_savings_figure)),
    (C[19], "an amount in yen in README.md", add("README.md", "\n\u5b66\u8cbb\u306f 150 \u4e07\u5186\u3067\u3059\u3002\n")),
    (C[19], "a figure beside savings in the README row", sub("README.en.md", "current savings cover the estimated total", "current savings of 12000 dollars cover the estimated total")),
    (C[19], "a total of the estimate that is not the computation", lambda G: _tuition(G, _tuition_estimate)),
    (C[19], "a rate of the page changed", lambda G: _tuition(G, _tuition_rate)),
    (C[19], "a number of the official text changed", lambda G: _tuition(G, _tuition_official_number)),
    (C[19], "README.en.md loses the estimate", sub("README.en.md", "### Estimate of tuition\n", "### Tuition\n")),
    (C[13], "an item other than tuition held on a self-report", _self_report_elsewhere),
    (C[0], "the Bursar's page dropped from the pages read", lambda G: G.__setitem__("data/requirements.json", G["data/requirements.json"].replace('"https://bursar.gatech.edu/tuition-fees":', '"https://bursar.gatech.edu/fees":', 1))),
    (C[11], "a tuition total in prose that differs from the computation", sub("README.md", "費用を含めて 10095 ドル", "費用を含めて 10059 ドル")),
    (C[11], "a rate in English prose that differs from the page", sub("README.en.md", "Out-of-Country tuition is 248 dollars", "Out-of-Country tuition is 247 dollars")),
    (C[11], "a count of planned rows that differs from the data", sub("README.md", "計画の行は 25 行です。", "計画の行は 26 行です。")),
    (C[11], "a count of the syllabus that differs from the data", sub("README.en.md", "has 65 courses", "has 66 courses")),
]


def _phd(G, path, fn):
    D = json.loads(G[path])
    fn(D)
    G[path] = json.dumps(D, ensure_ascii=False, indent=2)


def _req_row(i, fn):
    return lambda G: _phd(G, PHD_REQ, lambda D: fn(next(r for r in D["rows"] if r["id"] == i)))


def _asset(i, fn):
    return lambda G: _phd(G, PHD_ASSETS, lambda D: fn(next(a for a in D["items"] if a["id"] == i)))


def _plan_of(i, fn):
    return _asset("tuition", lambda a: fn(next(p for p in a["estimate"]["plans"] if p["id"] == i)))


def _doctorate(fn):
    def mut(G):
        P = json.loads(G["data/progress.json"])
        fn(P)
        G["data/progress.json"] = json.dumps(P, ensure_ascii=False, indent=2)
    return mut


def _phd_entry(P):
    return next(e for e in P["entries"] if e.get("topic") == "doctorate")


def _slot_entry(P):
    return next(e for e in P["entries"] if e.get("date") == "2026-11-20" and e.get("kind") == "other")


def _set(d, k, v):
    d[k] = v


PHD_BREAKS = [
    ("phd_requirements", "a search-result row claims 公式の頁で確かめた", _req_row("credit-hours", lambda r: _set(r, "status", "confirmed"))),
    ("phd_requirements", "a row with a status outside the four", _req_row("format", lambda r: _set(r, "status", "probably"))),
    ("phd_requirements", "a search-result row given as from a third-party page", _req_row("online", lambda r: _set(r, "status", "third-party"))),
    ("phd_requirements", "a search-result row with quotes, as if the page had been read",
     _req_row("f1-visa", lambda r: _set(r, "quotes", ["The program is fully online and does not meet the requirements."]))),
    ("phd_requirements", "a search-result row whose way of reading does not name the search",
     _req_row("format", lambda r: _set(r, "how", "頁を読んだ。"))),
    ("phd_requirements", "a Daily Nous quote with the apostrophe changed (Master’s to Master's)",
     _req_row("dn-masters", lambda r: _set(r, "quotes", [r["quotes"][0].replace("’", "'")]))),
    ("phd_requirements", "a Daily Nous quote shortened",
     _req_row("dn-first-phd", lambda r: _set(r, "quotes", ["The University at Buffalo Department of Philosophy is launching a PhD program."]))),
    ("phd_requirements", "a page of www.buffalo.edu added to the pages read",
     lambda G: _phd(G, PHD_REQ, lambda D: D["pages_read"].__setitem__(sorted(UB_SEARCH)[0], "x"))),
    ("phd_requirements", "a row not confirmed, but with a source", _req_row("funding", lambda r: _set(r, "source", DN))),
    ("phd_requirements", "a search-result row whose source is a page the search did not name",
     _req_row("qualifying-paper", lambda r: _set(r, "source", "https://www.buffalo.edu/cas/philosophy.html"))),
    ("phd_requirements", "a row read on another day", _req_row("time-to-degree", lambda r: _set(r, "read_on", "2026-11-19"))),
    ("phd_requirements", "tuition and fees that do not add up", _req_row("rate-spring-2027", lambda r: r["amounts"].__setitem__("fees", "1003.29"))),
    ("phd_requirements", "the deadlines no longer said to be possibly out of date", _req_row("deadlines", lambda r: r.pop("may_be_stale"))),
    ("phd_requirements", "statuses in words other than those of data/requirements.json",
     lambda G: _phd(G, PHD_REQ, lambda D: D["statuses"].__setitem__("search", ["検索から", "from search"]))),
    ("phd_assets", "an asset with a status outside the three", _asset("english-test", lambda a: _set(a, "status", "maybe"))),
    ("phd_assets", "the bachelor's degree marked as held, without evidence", _asset("bachelors", lambda a: _set(a, "status", "met"))),
    ("phd_assets", "the competence item no longer says the related facts do not meet the requirement",
     _asset("ontology-competence", lambda a: _set(a, "what", a["what"].replace("それが要件を満たすとはしない", "それで要件を満たす")))),
    ("phd_assets", "a related course that is not a planned course",
     _asset("ontology-competence", lambda a: a["related"].__setitem__(4, {"kind": "course", "title": "形式存在論"}))),
    ("phd_assets", "a related paper that is not on the list",
     _asset("ontology-competence", lambda a: a["related"].__setitem__(0, {"kind": "paper", "title": "An Ontology of Everything"}))),
    ("phd_assets", "a requirement not found, resting on a row that has a source",
     _asset("statement", lambda a: _set(a, "requirement_rows", ["competence"]))),
    ("phd_assets", "a grade in a doctoral asset", _asset("bachelors", lambda a: _set(a, "grade", "A"))),
    ("phd_assets", "the master's degree no longer names OMSCS", _asset("masters", lambda a: _set(a, "what", "修士号。持っていない"))),
    ("phd_assets", "an item dropped", lambda G: _phd(G, PHD_ASSETS, lambda D: D["items"].pop())),
    ("phd_tuition", "a total of the estimate that is not units times rate", _plan_of("per-credit-hour", lambda p: _set(p, "total", "46163.25"))),
    ("phd_tuition", "credit hours other than those of the row", _plan_of("per-credit-hour-tuition-only", lambda p: p.update(units=70, total="39550.00"))),
    ("phd_tuition", "a rate that is not the row's", _plan_of("full-time-semesters", lambda p: _set(p, "rate", "6785.00"))),
    ("phd_tuition", "the number of semesters no longer marked as Claude's assumption", _plan_of("full-time-semesters", lambda p: p.pop("units_assumed_by"))),
    ("phd_tuition", "the note no longer says why there is no yen",
     _asset("tuition", lambda a: _set(a["estimate"], "note", a["estimate"]["note"].replace("為替の率を出典から読んでいないので、円には換算しない", "")))),
    ("phd_tuition", "README.en.md loses the doctoral estimate", sub("README.en.md", "### Estimate of doctoral tuition\n", "### Doctoral tuition\n")),
    ("phd_money", "a figure beside savings in the tuition item", _asset("tuition", lambda a: _set(a, "what", a["what"] + "。貯えは 5000 ドル"))),
    ("phd_money", "a figure beside savings in README.en.md",
     sub("README.en.md", "The amount of the owner's savings is not written.", "The owner's savings are 30000 dollars.")),
    ("phd_money", "a field for savings in the tuition item", _asset("tuition", lambda a: _set(a, "savings_level", "half"))),
    ("phd_money", "an amount in yen in the doctoral decision", _doctorate(lambda P: _phd_entry(P)["items"].append("学費は 600 " + chr(0x4e07) + chr(0x5186) + "。"))),
    ("phd_contact", "an e-mail address in a doctoral row", _req_row("contact-listed", lambda r: _set(r, "how", r["how"] + " ontology" + "@" + "example.edu"))),
    ("phd_contact", "a telephone number in a doctoral row", _req_row("contact-listed", lambda r: _set(r, "how", r["how"] + " 716-555-0100"))),
    ("phd_contact", "a contact's title and name in README.md",
     sub("README.md", "頁に載っている問い合わせ先の名・メールアドレス・電話番号は、写していません。", "問い合わせ先は Professor Example です。")),
    ("phd_contact", "a field for a contact", _req_row("contact-listed", lambda r: _set(r, "contact", "x"))),
    ("phd_contact", "the name of the Daily Nous article's author", _req_row("dn-first-phd", lambda r: _set(r, "how", r["how"] + rules.dec("SnVzdGluIFdlaW5iZXJn")))),
    ("phd_claim", "the claim row no longer says it is the university's own claim",
     _req_row("worlds-only-claim", lambda r: _set(r, "requirement", r["requirement"].replace("これは大学自身の主張で、", "")))),
    ("phd_claim", "the claim marked as independently confirmed",
     _req_row("worlds-only-claim", lambda r: r["claim"].__setitem__("independently_confirmed", True))),
    ("phd_claim", "the claim in README.en.md without the mark", add("README.en.md", "\nUB is the world's only university with these degrees.\n")),
    ("phd_claim", "README.md loses the note that no independent confirmation was found",
     sub("README.md", "独立の確認は、見つけていません。\n", "")),
    ("phd_readme", "README.md changes the status of a doctoral row",
     sub("README.md", "| competence | 博士課程の出願者は、応用オントロジーのどこかの領域での力を示す必要がある | 公式の頁の検索結果から |",
         "| competence | 博士課程の出願者は、応用オントロジーのどこかの領域での力を示す必要がある | 公式の頁で確かめた |")),
    ("phd_readme", "README.en.md changes the status of a doctoral asset",
     sub("README.en.md", "| english-test | An English test, not yet taken | not yet |", "| english-test | An English test, not yet taken | has it |")),
    ("phd_readme", "README.md changes a total of the estimate", sub("README.md", "| 6 × 7788.92 | 46733.52 ドル |", "| 6 × 7788.92 | 46733.25 ドル |")),
    ("phd_readme", "README.md changes an item of the decision", sub("README.md", "- 学費の分が貯まってから、この課程に進みます。", "- すぐにこの課程に進みます。")),
    ("phd_readme", "README.en.md loses the note that www.buffalo.edu could not be opened",
     sub("README.en.md", "The pages of www.buffalo.edu could not be opened from the environment of this record.\n", "")),
    ("phd_readme", "README.md adds a doctoral row that is not in the data",
     sub("README.md", "| funding | ", "| gre | GRE が要る | 確かめていない | なし |\n| funding | ")),
    ("phd_urls", "a URL in the doctoral assets that is neither named by the search results nor read",
     _asset("statement", lambda a: _set(a, "note", a["note"] + " https://example.org/sop"))),
    ("phd_urls", "an extra URL in the doctoral section of README.en.md",
     sub("README.en.md", "The Comprehensive Fee waiver is not subtracted.\n",
         "The Comprehensive Fee waiver is not subtracted (https://www.buffalo.edu/tuition.html).\n")),
    ("phd_decision", "a figure in the doctoral decision", _doctorate(lambda P: _phd_entry(P)["items_en"].append("Tuition is 46000 dollars."))),
    ("phd_decision", "the slot record tagged as the doctoral decision, to escape the check of the slots",
     _doctorate(lambda P: _slot_entry(P).__setitem__("topic", "doctorate"))),
    ("phd_decision", "the doctoral decision carries something about the recommendation slots",
     _doctorate(lambda P: _phd_entry(P)["items"].append("推薦の枠は決めていません。"))),
    ("phd_decision", "the doctoral decision no longer names savings",
     _doctorate(lambda P: _phd_entry(P).__setitem__("items", [x.replace("貯え", "収入") for x in _phd_entry(P)["items"]]))),
    ("phd_decision", "the doctoral decision dropped", _doctorate(lambda P: P["entries"].remove(_phd_entry(P)))),
    ("phd_parity", "an English text of a doctoral row emptied", _req_row("funding", lambda r: _set(r, "requirement_en", ""))),
    ("phd_parity", "README.en.md drops a doctoral row",
     lambda G: G.__setitem__("README.en.md", "\n".join(x for x in G["README.en.md"].split("\n") if not x.startswith("| qualifying-paper | ")))),
    ("phd_parity", "README.en.md drops the count of rows from a third-party page",
     sub("README.en.md", "3 rows come from a third-party page.\n", "")),
    ("phd_parity", "the doctoral decision has one more item in Japanese than in English",
     _doctorate(lambda P: _phd_entry(P)["items"].append("x。"))),
    ("Every number in prose is in the ledger of numbers, and every count matches the data",
     "a doctoral count of not-yet items that differs from the data", sub("README.md", "まだ無いものは 6 件です。", "まだ無いものは 5 件です。")),
    ("Every number in prose is in the ledger of numbers, and every count matches the data",
     "a doctoral count in English that differs from the data", sub("README.en.md", "The doctoral table of requirements has 27 rows.", "The doctoral table of requirements has 26 rows.")),
    ("Every number in prose is in the ledger of numbers, and every count matches the data",
     "a doctoral asset's status changed, so the count no longer matches", _asset("english-test", lambda a: _set(a, "status", "partly"))),
    ("The recommendation slots hold only their number and state, and nothing about a person",
     "a university in the slot record of 2026-11-20 (the doctoral entry left out does not open a gap)",
     _doctorate(lambda P: _slot_entry(P)["items"].append("候補は University の人です。"))),
]
_BYFN = {fn.__name__: name for name, fn in CHECKS}
BREAKS += [(_BYFN.get(k, k), d, m) for k, d, m in PHD_BREAKS]


if __name__ == "__main__":
    sys.exit(rules.run(CHECKS, BREAKS, rules.load(), sys.argv))
