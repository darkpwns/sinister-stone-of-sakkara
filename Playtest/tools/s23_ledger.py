#!/usr/bin/env python3
"""Append rows to the end of a Ledger section's table: s23_ledger.py "<section heading>" "<row>" ["<row>" ...]"""
import sys
p = "Campaign/Ledger.md"; sec = sys.argv[1]; rows = sys.argv[2:]
L = open(p).read().split("\n")
i = next(k for k, l in enumerate(L) if l.strip() == "## " + sec)
j = next((k for k in range(i + 1, len(L)) if L[k].startswith("## ")), len(L))
k = j
while k > i and not L[k - 1].startswith("|"): k -= 1
L[k:k] = rows
open(p, "w").write("\n".join(L)); print(f"{len(rows)} rows -> {sec}")
