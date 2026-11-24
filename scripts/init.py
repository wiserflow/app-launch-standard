#!/usr/bin/env python3
"""Copy the App Launch Standard into the current repo and create docs/launch/STATUS.md.

Run from the root of the app repo:  python3 /path/to/skill/scripts/init.py
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["SKILL.md", "RUNBOOK.md", "TOOLING.md", "REFERENCES.md"]
QUESTIONS = [
    "Track and stack: greenfield (new app), pre-launch (code exists, not in production) or brownfield (in production)? Stack already chosen?",
    "Goal now: full launch audit / prepare a launch / improve one part / review a screen's UX?",
    "Paid product? Billing model?",
    "Accounts: one person per account, team accounts (members, roles), or both?",
    "Target surfaces (web, PWA, iOS, Android, desktop, CLI, extension, bot, API/MCP)?",
    "Languages and countries served?",
    "Biggest pain right now?",
    "Deadline (launch date or next milestone)?",
]
HEADING = re.compile(r"^#\s+.*\(([^)]+)\)\s*$")
ITEM = re.compile(r"^\|\s*([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\s*\|\s*([123])\s*\|")


def parse_area(path):
    """Return (prefix, [(id, level), ...]) for one area file."""
    prefix, items = "", []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not prefix:
            m = HEADING.match(line)
            if m:
                prefix = m.group(1).strip()
        m = ITEM.match(line)
        if m:
            items.append((m.group(1), m.group(2)))
    return prefix, items


def build_status(areas_dir):
    areas = [(p, *parse_area(p)) for p in sorted(areas_dir.glob("*.md"))]
    out = ["# Launch status", "", "## Kickoff", "",
           "Answer once; the agent reads this instead of asking again.", "",
           "| # | Question | Answer |", "| --- | --- | --- |"]
    out += [f"| {i} | {q} |  |" for i, q in enumerate(QUESTIONS, 1)]
    out += ["", "## Areas", "",
            "| Area file | Prefix | Applies (yes / no / partial) | Reason |", "| --- | --- | --- | --- |"]
    out += [f"| `areas/{p.name}` | {pre} | yes |  |" for p, pre, _ in areas]
    out += ["", "## Items", "",
            "Status: `todo` / `ok` / `missing` / `diverges` (partly met: say which part fails) / `n/a (reason)`. "
            "Evidence: test name, screenshot path, URL, ADR link; `→ ID` when it fails only because that item fails.", ""]
    for p, pre, items in areas:
        out += [f"### {pre} (`areas/{p.name}`)", "", "| ID | L | Status | Evidence |", "| --- | --- | --- | --- |"]
        out += [f"| {i} | {lv} | todo |  |" for i, lv in items]
        out.append("")
    return "\n".join(out)


def add_missing_rows(text, areas_dir):
    """Insert `todo` rows for items in areas/ that STATUS.md lacks (after an upgrade). Return (text, added ids)."""
    lines = text.split("\n")
    have = {m.group(1) for m in map(ITEM.match, lines) if m}
    added = []
    for p in sorted(areas_dir.glob("*.md")):
        pre, items = parse_area(p)
        heading = f"### {pre} (`areas/{p.name}`)"
        prev = None
        for iid, lv in items:
            if iid not in have:
                row = f"| {iid} | {lv} | todo |  |"
                if heading not in lines:
                    lines += ["", heading, "", "| ID | L | Status | Evidence |", "| --- | --- | --- | --- |"]
                if prev:
                    at = next(i for i, l in enumerate(lines) if l.startswith(f"| {prev} |")) + 1
                else:
                    at = lines.index(heading) + 4  # after heading, blank, header, separator
                lines.insert(at, row)
                have.add(iid)
                added.append(iid)
            prev = iid
    return "\n".join(lines), added


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--target", default="docs/launch", help="target dir, relative to the current directory (default: docs/launch)")
    ap.add_argument("--force", action="store_true", help="overwrite existing copied files (STATUS.md is kept; rows for new items are added as todo)")
    args = ap.parse_args()

    target = Path.cwd() / args.target
    if target.exists() and any(target.iterdir()) and not args.force:
        print(f"error: {target} already exists and is not empty; use --force to refresh the copies (STATUS.md is kept)", file=sys.stderr)
        return 1
    target.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        shutil.copy2(ROOT / name, target / name)
    for name in ("areas", "scripts", "templates"):
        shutil.copytree(ROOT / name, target / name, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__", "check.py"))  # check.py is for maintainers

    status = target / "STATUS.md"
    if status.exists():
        text, added = add_missing_rows(status.read_text(encoding="utf-8"), ROOT / "areas")
        if added:
            status.write_text(text, encoding="utf-8")
        print(f"kept existing {status}" + (f"; added {len(added)} new item row(s) as todo: {', '.join(added)}" if added else ""))
    else:
        status.write_text(build_status(ROOT / "areas"), encoding="utf-8")
        print(f"created {status}")
    print(f"\nCopied the standard into {target}\n\nNext steps:\n"
          f"  1. Ask the agent to follow {args.target}/SKILL.md (it asks the kickoff questions first).\n"
          f"  2. Answers go in the Kickoff block of {args.target}/STATUS.md; set Applies=no (with a reason) for n/a areas.\n"
          f"  3. Mark items ok / missing / diverges / n/a with evidence (scripts/setrows.py writes rows from TSV); start it with `→ ID` when an item fails only because that item fails.\n"
          f"  4. Report progress: python3 {args.target}/scripts/status.py --file {args.target}/STATUS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
