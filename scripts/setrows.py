#!/usr/bin/env python3
"""Set Status and Evidence of item rows in docs/launch/STATUS.md without reading or rewriting it by hand.

Rows come as TSV (file or `-` for stdin), one per item: ID<TAB>status<TAB>evidence.
status: ok | missing | diverges | todo | n/a (reason). `ok` needs evidence. The Level column is kept.
The file is locked while writing, so parallel agents (one per area, with --prefixes) can update it safely.
Nothing is written if any row is invalid or any ID is not in STATUS.md.
"""
import argparse
import fcntl
import re
import sys

sys.dont_write_bytecode = True
from init import ITEM

VALID = re.compile(r"^(ok|missing|diverges|todo|n/a \(.+\))$")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("rows", help="TSV file with ID<TAB>status<TAB>evidence lines, or - for stdin")
    ap.add_argument("--file", default="docs/launch/STATUS.md", help="STATUS.md path (default: docs/launch/STATUS.md)")
    ap.add_argument("--prefixes", default="", help="comma-separated prefixes this writer may touch (e.g. SEC,DB); default: any")
    args = ap.parse_args()

    prefixes = [p for p in args.prefixes.split(",") if p]
    src = sys.stdin if args.rows == "-" else open(args.rows, encoding="utf-8")
    updates = {}
    for n, raw in enumerate(src, 1):
        raw = raw.rstrip("\n")
        if not raw.strip():
            continue
        parts = [p.strip() for p in raw.split("\t")]
        if len(parts) != 3:
            sys.exit(f"error: rows line {n}: need 3 tab-separated fields: {raw[:80]}")
        iid, st, ev = parts
        if prefixes and not any(iid.startswith(p + "-") for p in prefixes):
            sys.exit(f"error: rows line {n}: {iid} is outside --prefixes {','.join(prefixes)}")
        if not VALID.match(st):
            sys.exit(f"error: rows line {n}: bad status '{st}' (ok / missing / diverges / todo / n/a (reason))")
        if st == "ok" and not ev:
            sys.exit(f"error: rows line {n}: {iid} is ok without evidence")
        updates[iid] = (st.replace("|", "/"), ev.replace("|", "/"))

    with open(args.file, "r+", encoding="utf-8") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        lines = f.read().split("\n")
        done = set()
        for i, line in enumerate(lines):
            m = ITEM.match(line)
            if m and m.group(1) in updates:
                st, ev = updates[m.group(1)]
                lines[i] = f"| {m.group(1)} | {m.group(2)} | {st} | {ev} |"
                done.add(m.group(1))
        if set(updates) - done:
            sys.exit(f"error: IDs not in {args.file} (nothing written): {', '.join(sorted(set(updates) - done))}")
        f.seek(0)
        f.write("\n".join(lines))
        f.truncate()
    print(f"updated {len(done)} row(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
