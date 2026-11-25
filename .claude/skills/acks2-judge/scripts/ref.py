#!/usr/bin/env python3
"""ref.py NAME [SECTION ...] : one section of a reference, not the whole file (every Read stays in the chat).

NAME is a file in references/ (`judge-screen`, `combat-totm`, ...; `.md` optional). With no SECTION: the file's
headings with their line counts. A SECTION is a heading's number (`11` matches `## 11. Routine`, `9a` matches
`## 9a. Domains`) or words from it (`scrolls`, `wards and auras`); each section printed runs to the next heading of
the same or a higher level.
"""
import os
import re
import sys

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references")


def load(name):
    p = os.path.join(R, name if name.endswith(".md") else name + ".md")
    if not os.path.exists(p):
        sys.exit(f"ref.py: no reference {name} (have: {', '.join(sorted(f[:-3] for f in os.listdir(R)))})")
    return open(p, encoding="utf-8").read().splitlines()


def headings(lines):
    out, fence = [], False
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"^(#{2,4}) (.*)$", ln)
        if m:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def find(hs, want):
    w = want.strip().lower()
    for k, (i, lvl, title) in enumerate(hs):
        t = title.lower()
        if re.match(re.escape(w) + r"[.)]?(\s|$)", t) or (not w[:1].isdigit() and w in t):
            return k
    return None


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    lines = load(argv[0])
    hs = headings(lines)
    if len(argv) == 1:
        for k, (i, lvl, title) in enumerate(hs):
            end = next((j for j, l2, _ in hs[k + 1:] if l2 <= lvl), len(lines))
            print(f"{'  ' * (lvl - 2)}{title}  ({end - i} lines)")
        return 0
    code = 0
    for want in argv[1:]:
        k = find(hs, want)
        if k is None:
            print(f"ref.py: no section '{want}' in {argv[0]} (run `ref.py {argv[0]}` for the headings)")
            code = 1
            continue
        i, lvl, _ = hs[k]
        end = next((j for j, l2, _ in hs[k + 1:] if l2 <= lvl), len(lines))
        print("\n".join(lines[i:end]).rstrip())
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
