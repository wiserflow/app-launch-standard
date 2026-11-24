#!/usr/bin/env python3
"""Validate the standard: unique IDs, valid levels, ID prefixes, and the counts quoted in SKILL.md/README.md.

Run from the repo root:  python3 scripts/check.py   (exit 1 on any error)
"""
import re
import sys
from pathlib import Path

from init import ITEM, ROOT, parse_area

ID_ROW = re.compile(r"^\|\s*([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\s*\|\s*([^|]*?)\s*\|")
MAP_ROW = re.compile(r"`areas/([a-z-]+\.md)`.*\|\s*(\d+) \((\d+)\)(?: \+ (\d+) \((\d+)\)[^|]*)?\s*\|\s*$")
SUMMARY = re.compile(r"(\d+) areas, (\d+) (?:checklist )?items \((\d+) launch blockers\) plus (\d+) target-specific")


def main():
    errors = []
    areas = sorted((ROOT / "areas").glob("*.md"))
    seen = {}
    counts = {}
    for path in areas:
        prefix, items = parse_area(path)
        prefixes = [p.strip() for p in prefix.split("/") if p.strip()]
        if not prefixes:
            errors.append(f"{path.name}: heading has no '(PREFIX)'")
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ID_ROW.match(line)
            if m and not ITEM.match(line) and re.fullmatch(r"L?\d", m.group(2)):
                errors.append(f"{path.name}: {m.group(1)} has invalid level '{m.group(2)}' (use 1, 2 or 3)")
        for item_id, _ in items:
            if item_id in seen:
                errors.append(f"{path.name}: duplicate ID {item_id} (also in {seen[item_id]})")
            seen[item_id] = path.name
            if prefixes and not any(item_id.startswith(p + "-") for p in prefixes):
                errors.append(f"{path.name}: {item_id} does not match heading prefix ({prefix})")
        base = [lv for i, lv in items if i.count("-") == 1]
        target = [lv for i, lv in items if i.count("-") > 1]
        counts[path.name] = (len(base), base.count("1"), len(target), target.count("1"))

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for line in skill.splitlines():
        m = MAP_ROW.search(line)
        if not m or m.group(1) not in counts:
            continue
        quoted = tuple(int(g or 0) for g in m.groups()[1:])
        if quoted != counts[m.group(1)]:
            errors.append(f"SKILL.md map: {m.group(1)} says {quoted}, actual {counts[m.group(1)]} (items, L1, target items, target L1)")

    total = (len(areas), sum(c[0] for c in counts.values()), sum(c[1] for c in counts.values()),
             sum(c[2] for c in counts.values()))
    for name in ("SKILL.md", "README.md"):
        m = SUMMARY.search((ROOT / name).read_text(encoding="utf-8"))
        if not m:
            errors.append(f"{name}: summary line '<n> areas, <n> items (<n> launch blockers) plus <n> target-specific' not found")
        elif tuple(map(int, m.groups())) != total:
            errors.append(f"{name}: summary says {tuple(map(int, m.groups()))}, actual {total} (areas, items, L1, target items)")

    for e in errors:
        print(f"error: {e}")
    print(f"{len(areas)} areas, {len(seen)} IDs, {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
