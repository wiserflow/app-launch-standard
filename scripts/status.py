#!/usr/bin/env python3
"""Report progress from docs/launch/STATUS.md: per-area counts, totals, open items.

Always exits 0 (it is a report). Areas with Applies = no or n/a (...) are skipped.
Only items up to --level are counted. Open items whose evidence starts with "→ ID" are
listed apart as blocked by another item, so one root cause does not read as many gaps; a pointer to
an item that is closed, above --level, unknown or in a skipped area does not block, so the item stays a root.
"""
import argparse
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from init import parse_area

STATUSES = ["ok", "missing", "diverges", "todo", "n/a"]
ITEM_ID = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
POINTER = re.compile(r"^→\s*([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse(text):
    """Return (applies, items): applies {prefix: bool}; items [(prefix, id, level, status, evidence)]."""
    applies, items, section, prefix, seen = {}, [], "", "", {}
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if line.startswith("### "):
            prefix = line[4:].split("(")[0].strip()
            continue
        if not line.startswith("|") or set(line) <= set("|- :"):
            continue
        c = cells(line)
        if section == "Areas" and len(c) >= 3 and c[0].startswith("`areas/"):
            v = c[2].lower()
            if v == "no" or v.startswith("n/a"):
                applies[c[1]] = False
            else:
                applies[c[1]] = True
                if v not in ("yes", "applies", "") and not v.startswith("partial"):
                    print(f"warning: line {n}: unknown Applies value '{c[2]}' for {c[1]}, treated as applicable", file=sys.stderr)
        elif section == "Items" and c[0] != "ID":
            if len(c) < 3 or not ITEM_ID.match(c[0]) or c[1] not in ("1", "2", "3"):
                print(f"warning: line {n}: malformed row, skipped: {line[:80]}", file=sys.stderr)
                continue
            status = c[2].lower().split()[0] if c[2] else ""
            if status not in STATUSES:
                print(f"warning: line {n}: unknown status '{c[2]}' for {c[0]}, skipped", file=sys.stderr)
                continue
            if c[0] in seen:
                print(f"warning: line {n}: duplicate {c[0]} (first at line {seen[c[0]]}), skipped", file=sys.stderr)
                continue
            seen[c[0]] = n
            evidence = c[3] if len(c) > 3 else ""
            if status == "ok" and not evidence:
                print(f"warning: line {n}: {c[0]} is ok with empty Evidence", file=sys.stderr)
            items.append((prefix, c[0], int(c[1]), status, evidence))
    return applies, items


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--file", default="docs/launch/STATUS.md", help="STATUS.md path (default: docs/launch/STATUS.md)")
    ap.add_argument("--level", type=int, default=1, choices=[1, 2, 3], help="count and list items up to this level (default: 1 = L1 launch blockers only)")
    args = ap.parse_args()

    path = Path(args.file)
    if not path.is_file():
        print(f"error: {path} not found (run scripts/init.py first)")
        return 0
    applies, items = parse(path.read_text(encoding="utf-8"))
    areas_dir = path.parent / "areas"
    if areas_dir.is_dir():
        known = {i[1] for i in items}
        missing = [iid for f in sorted(areas_dir.glob("*.md")) for pre, its in [parse_area(f)]
                   if applies.get(pre, True) for iid, _ in its if iid not in known]
        if missing:
            print(f"warning: {len(missing)} item(s) in areas/ missing from {path.name}: {', '.join(missing)} "
                  "(upgrade drift; add rows with status todo)", file=sys.stderr)
    skipped = sorted(p for p, a in applies.items() if not a)
    items = [i for i in items if applies.get(i[0], True) and i[2] <= args.level]
    open_ids = {i[1] for i in items if i[3] not in ("ok", "n/a")}
    print(f"Items up to L{args.level}\n")

    by_area = {}
    for item in items:
        by_area.setdefault(item[0], dict.fromkeys(STATUSES, 0))[item[3]] += 1
    head = f"{'Area':<14}" + "".join(f"{s:>10}" for s in STATUSES)
    print(head + "\n" + "-" * len(head))
    total = dict.fromkeys(STATUSES, 0)
    for prefix, counts in by_area.items():
        print(f"{prefix:<14}" + "".join(f"{counts[s]:>10}" for s in STATUSES))
        for s in STATUSES:
            total[s] += counts[s]
    print("-" * len(head))
    print(f"{'TOTAL':<14}" + "".join(f"{total[s]:>10}" for s in STATUSES))
    counted = sum(total.values()) - total["n/a"]
    if counted:
        print(f"\nDone: {total['ok']}/{counted} applicable items ok ({100 * total['ok'] // counted}%)")
    if skipped:
        print(f"Skipped areas (Applies = no / n/a): {', '.join(skipped)}")

    open_items = [i for i in items if i[3] not in ("ok", "n/a")]
    def blocker(ev):
        m = POINTER.match(ev)
        return m.group(1) if m and m.group(1) in open_ids else None
    blocked = [i for i in open_items if blocker(i[4])]
    roots = [i for i in open_items if not blocker(i[4])]
    for title, group in ((f"Open items up to L{args.level}", roots), ("Blocked by another item", blocked)):
        if group or title.startswith("Open"):
            print(f"\n{title}: {len(group)}")
        for _, iid, lv, status, ev in group:
            print(f"  {iid:<12} L{lv} {status}" + (f"  {ev}" if ev else ""))
    return 0


if __name__ == "__main__":
    try:
        main()
        sys.stdout.flush()
    except BrokenPipeError:  # reader closed early (e.g. `| head`, an output filter): still a report, exit 0
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
    sys.exit(0)
