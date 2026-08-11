#!/usr/bin/env python3
"""Verify (and optionally correct) the per-project commit counts in the daily blog.

Every entry in `profile/README.md` carries a header like

    **[aowlsem](https://…) — 43 commits.** <theme>

and that number is the single most checkable claim on the page. It is also the
easiest one to get wrong, because it is written DURING the day it describes: any
commit landing after the entry is written makes the recorded figure too low, and
nothing ever revisits it.

This counts commits by AUTHOR DATE in local time — `git log --date=format:%F`
grouped by day — which is the only definition that matches "what we did on that
day" and is stable regardless of when it is re-run. `--since=midnight` is NOT
that: it is relative to now, so it silently answers a different question on any
later day.

A multi-project header (`[a](…) · [b](…) — N commits.`) is summed across its
repos, which is how those sections were written.

Usage:
    python3 tools/commit-audit.py                 # audit, report a table
    python3 tools/commit-audit.py --fix           # rewrite the counts in place
    python3 tools/commit-audit.py --day 2026-08-11 --repo aowlsem   # one lookup
"""
import argparse
import os
import re
import subprocess
import sys

README = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      '..', 'profile', 'README.md')
REPO_ROOT = os.path.expanduser('~')

# A blog project name does not reliably match a directory name: the CSS work is
# in `aoughwl-css`, the parser repo is `aifparser`, and the plugin lives under
# the Claude marketplace. Rather than hard-code a mapping that rots, try every
# plausible checkout and pick the one that actually has commits on the day in
# question — resolution by EVIDENCE. `~/serve` exists, has one commit ever, and
# is NOT the `serve` the blog means; a name-only mapping "corrected" that entry
# from 25 to 0.
CANDIDATES = [
    '{n}', 'aoughwl-{n}', 'aowl{n}', 'aif{n}', 'aowl-{n}', 'aoughwl{n}',
    os.path.join('.claude', 'plugins', 'marketplaces', '{n}'),
]

ENTRY_RE = re.compile(r'^## (\d+) (\d{4}-\d{2}-\d{2})', re.M)
SECTION_RE = re.compile(
    r'^\*\*(?P<names>\[[^\]]+\]\([^)]*\)(?:\s*·\s*\[[^\]]+\]\([^)]*\))*)'
    r'\s*—\s*(?P<n>\d+)\s+commits?\.', re.M)
NAME_RE = re.compile(r'\[([^\]]+)\]')


def candidate_dirs(project):
    out = []
    for pat in CANDIDATES:
        d = os.path.join(REPO_ROOT, pat.format(n=project))
        if os.path.isdir(os.path.join(d, '.git')):
            out.append(d)
    return out


def best_count(project, day):
    """Commits on `day` in the most plausible checkout, or None if none has any.

    Counted on HEAD including merges — the same question the entries were
    written with (`git log --since=midnight | wc -l`), verified to agree with
    an all-refs no-merges count on the two days that were spot-checked.
    """
    best = None
    for d in candidate_dirs(project):
        n = commits_on(d, day)
        if n and (best is None or n > best):
            best = n
    return best


def commits_on(repo, day):
    """Commits authored on `day` (local time). None if the repo is missing."""
    if repo is None:
        return None
    out = subprocess.run(
        ['git', '-C', repo, 'log', '--date=format:%Y-%m-%d', '--pretty=%ad'],
        capture_output=True, text=True)
    if out.returncode != 0:
        return None
    return sum(1 for line in out.stdout.splitlines() if line.strip() == day)


def audit(text):
    """-> [(entry_no, day, [projects], recorded, actual_or_None, span)]"""
    rows = []
    entries = list(ENTRY_RE.finditer(text))
    for i, m in enumerate(entries):
        day = m.group(2)
        end = entries[i + 1].start() if i + 1 < len(entries) else len(text)
        body = text[m.start():end]
        for s in SECTION_RE.finditer(body):
            projects = NAME_RE.findall(s.group('names'))
            recorded = int(s.group('n'))
            counts = [best_count(p, day) for p in projects]
            # ONE unresolved project makes the whole section unresolved: a
            # partial sum silently under-reports a merged section.
            actual = None if any(c is None for c in counts) else sum(counts)
            rows.append((m.group(1), day, projects, recorded, actual,
                         (m.start() + s.start('n'), m.start() + s.end('n'))))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fix', action='store_true')
    ap.add_argument('--day')
    ap.add_argument('--repo')
    a = ap.parse_args()

    if a.day and a.repo:
        n = best_count(a.repo, a.day)
        print(f'{a.repo} {a.day}: {n if n is not None else "repo not found"}')
        return 0

    text = open(README, encoding='utf-8').read()
    rows = audit(text)
    bad = [r for r in rows if r[4] is not None and r[3] != r[4]]
    miss = [r for r in rows if r[4] is None]

    print(f'{"entry":6} {"day":12} {"project(s)":34} {"said":>5} {"actual":>7}')
    for no, day, projects, rec, act, _ in rows:
        flag = '' if act is None or act == rec else '  ← WRONG'
        shown = '?' if act is None else act
        print(f'{no:6} {day:12} {" · ".join(projects)[:34]:34} {rec:>5} '
              f'{shown:>7}{flag}')
    print(f'\n{len(rows)} sections, {len(bad)} wrong, {len(miss)} unresolvable')

    if a.fix and bad:
        # rewrite right-to-left so earlier spans stay valid
        for no, day, projects, rec, act, (s, e) in sorted(bad, key=lambda r: -r[5][0]):
            text = text[:s] + str(act) + text[e:]
        open(README, 'w', encoding='utf-8').write(text)
        print(f'corrected {len(bad)} count(s)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
