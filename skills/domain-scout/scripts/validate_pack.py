#!/usr/bin/env python3
"""Validate one or more domain packs against the pack format.

Usage:
  python3 validate_pack.py domains/creative-direction-film
  python3 validate_pack.py domains/*          # several packs
  python3 validate_pack.py .agent-architect/domains/<name>   # a project overlay
  add --strict to treat warnings as errors

Exit code 1 when errors are found. Rules: references/pack-format.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"
    r"|AKIA[0-9A-Z]{16}|xox[abp]-[A-Za-z0-9-]{10,}|Bearer\s+[A-Za-z0-9._-]{20,})"
)

DOMAIN_SECTIONS = [
    "Scope",
    "Roles",
    "Workflows",
    "Vocabulary",
    "What good looks like",
    "Risks and compliance",
    "Where agents help",
    "References",
]
BRANCHES = [
    "Outcome",
    "Trigger and inputs",
    "Decomposition",
    "Roles",
    "Knowledge",
    "Tools and data",
    "Risk and permissions",
    "Verification",
    "Environment",
]
TOOL_COLUMNS = ["Tool", "Used for", "Integration", "Auth", "Checked"]
REFERENCE_FILES = ["references/questions.md", "references/tools.md", "references/patterns.md"]
REQUIRED_FIELDS = ["name", "title", "description", "keywords", "status", "checked"]
OVERLAY_SECTIONS = ["Team", "Clients and approvals", "Tools in use", "House terms", "House rules"]
OVERLAY_FIELDS = ["extends", "title", "checked"]

LIMITS = {"DOMAIN.md": 200, "reference": 300, "contents_after": 100}
MIN_SOURCES = 8
MIN_QUESTIONS = 10
STALE_DAYS = 180


class Report:
    def __init__(self, pack: Path):
        self.pack = pack
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.status = "unknown"

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def split_frontmatter(text: str) -> tuple[dict | None, str, str | None]:
    if not text.startswith("---"):
        return None, text, "missing YAML frontmatter"
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return None, text, "frontmatter is not closed with ---"
    body = parts[1].split("\n", 1)[1] if "\n" in parts[1] else ""
    try:
        data = yaml.safe_load(parts[0][3:]) or {}
    except yaml.YAMLError as exc:
        return None, body, f"invalid YAML frontmatter: {exc}"
    if not isinstance(data, dict):
        return None, body, "frontmatter must be a mapping"
    return data, body, None


def as_date(value) -> dt.date | None:
    if isinstance(value, dt.date):
        return value
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        return None


def h2_headings(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^## (.+)$", text, re.M)]


def check_size(r: Report, rel: str, text: str, limit: int) -> None:
    lines = text.count("\n") + 1
    if lines > limit:
        r.error(rel, f"{lines} lines, limit is {limit}.")
    if rel != "DOMAIN.md" and lines > LIMITS["contents_after"] and "## Contents" not in text:
        r.warn(rel, f"{lines} lines without a '## Contents' list.")


def check_domain(r: Report, today: dt.date) -> None:
    path = r.pack / "DOMAIN.md"
    if not path.is_file():
        r.error("DOMAIN.md", "missing.")
        return
    text = path.read_text(encoding="utf-8")
    check_size(r, "DOMAIN.md", text, LIMITS["DOMAIN.md"])
    fm, body, err = split_frontmatter(text)
    if err:
        r.error("DOMAIN.md", err)
        return
    for field in REQUIRED_FIELDS:
        if not fm.get(field):
            r.error("DOMAIN.md", f"frontmatter field '{field}' is missing or empty.")
    name = fm.get("name")
    if name and name != r.pack.name:
        r.error("DOMAIN.md", f"name '{name}' does not match folder '{r.pack.name}'.")
    if name and not NAME_RE.match(str(name)):
        r.error("DOMAIN.md", f"name '{name}' must be lowercase kebab-case.")
    if fm.get("keywords") is not None and not isinstance(fm["keywords"], list):
        r.error("DOMAIN.md", "keywords must be a list.")
    status = fm.get("status")
    if status and status not in ("draft", "reviewed"):
        r.error("DOMAIN.md", "status must be 'draft' or 'reviewed'.")
    checked = as_date(fm.get("checked")) if fm.get("checked") else None
    if fm.get("checked") and checked is None:
        r.error("DOMAIN.md", "checked must be an ISO date (YYYY-MM-DD).")
    if checked and (today - checked).days > STALE_DAYS:
        r.warn("DOMAIN.md", f"checked {checked} is over {STALE_DAYS} days old; refresh the pack.")
    if status == "reviewed" and not as_date(fm.get("reviewed", "")):
        r.error("DOMAIN.md", "status 'reviewed' needs a 'reviewed: YYYY-MM-DD' date.")
    r.status = str(status or "unknown")

    found = h2_headings(body)
    missing = [s for s in DOMAIN_SECTIONS if s not in found]
    if missing:
        r.error("DOMAIN.md", f"missing sections: {', '.join(missing)}.")
    elif [s for s in found if s in DOMAIN_SECTIONS] != DOMAIN_SECTIONS:
        r.warn("DOMAIN.md", f"sections are out of order; expected {', '.join(DOMAIN_SECTIONS)}.")
    links = set(LINK_RE.findall(body))
    for target in REFERENCE_FILES + ["sources.md"]:
        if target not in links:
            r.error("DOMAIN.md", f"does not link to {target}.")


def check_reference_common(r: Report, rel: str) -> str | None:
    path = r.pack / rel
    if not path.is_file():
        r.error(rel, "missing.")
        return None
    text = path.read_text(encoding="utf-8")
    check_size(r, rel, text, LIMITS["reference"])
    for target in LINK_RE.findall(text):
        if not target.startswith(("http://", "https://")) and target.endswith(".md"):
            r.error(rel, f"links to '{target}'; references never link to other files in the pack.")
    return text


def check_questions(r: Report) -> None:
    rel = "references/questions.md"
    text = check_reference_common(r, rel)
    if text is None:
        return
    for heading in h2_headings(text):
        if heading not in BRANCHES and heading != "Contents":
            r.error(rel, f"heading '{heading}' is not a design-tree branch ({', '.join(BRANCHES)}).")
    # A question is a bullet starting with bold text; it continues on indented lines.
    blocks = re.findall(r"^- \*\*.*(?:\n  .*)*", text, re.M)
    if len(blocks) < MIN_QUESTIONS:
        r.error(rel, f"{len(blocks)} questions, need at least {MIN_QUESTIONS}.")
    for block in blocks:
        flat = " ".join(line.strip() for line in block.splitlines())
        m = re.match(r"- \*\*(.+?)\*\*(.*)$", flat)
        if not m:
            r.error(rel, f"question '{flat[:60]}' has unclosed bold text.")
        elif "Recommended:" not in m.group(2):
            r.error(rel, f"question '{m.group(1)[:60]}' has no 'Recommended:' answer.")


def parse_tables(text: str) -> list[list[list[str]]]:
    tables, current = [], []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            current.append(cells)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    return tables


def check_tools(r: Report) -> None:
    rel = "references/tools.md"
    text = check_reference_common(r, rel)
    if text is None:
        return
    tables = parse_tables(text)
    if not tables:
        r.error(rel, "no tool tables found.")
    rows = 0
    for table in tables:
        if table[0] != TOOL_COLUMNS:
            r.error(rel, f"table header must be | {' | '.join(TOOL_COLUMNS)} |, got | {' | '.join(table[0])} |.")
            continue
        for row in table[2:]:
            rows += 1
            if len(row) != len(TOOL_COLUMNS):
                r.error(rel, f"row '{row[0]}' has {len(row)} cells, expected {len(TOOL_COLUMNS)}.")
                continue
            if not row[2]:
                r.error(rel, f"tool '{row[0]}' has no Integration; write 'none found'.")
            if not row[4]:
                r.error(rel, f"tool '{row[0]}' has no Checked value; write 'unverified' if unknown.")
    if tables and rows == 0:
        r.error(rel, "tool tables have no rows.")


def check_patterns(r: Report) -> None:
    rel = "references/patterns.md"
    text = check_reference_common(r, rel)
    if text is None:
        return
    found = h2_headings(text)
    for section in ("Teams", "Expert roles", "Anti-patterns"):
        if section not in found:
            r.error(rel, f"missing section '## {section}'.")


def check_sources(r: Report) -> None:
    rel = "sources.md"
    path = r.pack / rel
    if not path.is_file():
        r.error(rel, "missing.")
        return
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^checked:\s*\d{4}-\d{2}-\d{2}", text, re.M):
        r.error(rel, "needs a 'checked: YYYY-MM-DD' line.")
    urls = {u.rstrip(".,;") for u in URL_RE.findall(text)}
    if len(urls) < MIN_SOURCES:
        r.error(rel, f"{len(urls)} distinct sources, need at least {MIN_SOURCES}.")


def check_secrets(r: Report) -> None:
    for path in sorted(r.pack.rglob("*.md")):
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if SECRET_RE.search(line):
                r.error(str(path.relative_to(r.pack)), f"line {n} looks like a literal credential; use ${{VAR}}.")


def check_overlay(r: Report) -> None:
    rel = "OVERLAY.md"
    text = (r.pack / rel).read_text(encoding="utf-8")
    check_size(r, rel, text, LIMITS["DOMAIN.md"])
    fm, body, err = split_frontmatter(text)
    if err:
        r.error(rel, err)
        return
    for field in OVERLAY_FIELDS:
        if not fm.get(field):
            r.error(rel, f"frontmatter field '{field}' is missing or empty.")
    extends = fm.get("extends")
    if extends and extends != r.pack.name:
        r.error(rel, f"extends '{extends}' does not match folder '{r.pack.name}'.")
    if fm.get("checked") and as_date(fm.get("checked")) is None:
        r.error(rel, "checked must be an ISO date (YYYY-MM-DD).")
    found = h2_headings(body)
    if not found:
        r.error(rel, f"has no sections; use any of {', '.join(OVERLAY_SECTIONS)}.")
    for heading in found:
        if heading not in OVERLAY_SECTIONS:
            r.error(rel, f"section '{heading}' is not one of {', '.join(OVERLAY_SECTIONS)}.")
    r.status = "overlay"


def validate(pack: Path, today: dt.date | None = None) -> Report:
    r = Report(pack)
    today = today or dt.date.today()
    if not pack.is_dir():
        r.error(str(pack), "not a directory.")
        return r
    if not NAME_RE.match(pack.name):
        r.error(str(pack), "folder name must be lowercase kebab-case.")
    if (pack / "OVERLAY.md").is_file() and not (pack / "DOMAIN.md").is_file():
        check_overlay(r)
        check_secrets(r)
        return r
    check_domain(r, today)
    check_questions(r)
    check_tools(r)
    check_patterns(r)
    check_sources(r)
    check_secrets(r)
    return r


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("packs", nargs="+", type=Path, help="pack folder(s), e.g. domains/<name>")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args(argv)

    failed = False
    for pack in args.packs:
        r = validate(pack)
        for e in r.errors:
            print(f"ERROR   {pack.name}/{e}")
        for w in r.warnings:
            print(f"WARNING {pack.name}/{w}")
        bad = bool(r.errors) or (args.strict and bool(r.warnings))
        failed |= bad
        print(f"{'FAIL' if bad else 'OK'}    {pack.name} ({r.status}): {len(r.errors)} errors, {len(r.warnings)} warnings")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
