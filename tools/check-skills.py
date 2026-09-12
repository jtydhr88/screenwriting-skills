# -*- coding: utf-8 -*-
"""Structural checks every skill must pass before a commit.

    python tools/check-skills.py            # check all plugins
    python tools/check-skills.py --strict   # also fail on warnings

Checks, per plugins/*/skills/<dir>/SKILL.md:
  - frontmatter present, with `name:` and `description:`
  - name == directory name
  - description <= 1024 code points (the agentskills.io limit; Codex refuses longer)
    warning at > 1000 so there is headroom for edits
  - description ends with a "Use when" clause
  - every relative markdown link in SKILL.md and reference*.md resolves to a file

Exit code 1 on any error (or on warnings with --strict). No dependencies beyond the stdlib.
"""
import glob, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRICT = "--strict" in sys.argv
LIMIT, SOFT = 1024, 1000
errors, warnings = [], []

LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')

def check_links(md_path):
    d = os.path.dirname(md_path)
    text = io.open(md_path, encoding='utf-8').read()
    for target in LINK.findall(text):
        if re.match(r'^[a-z]+:', target):          # http:, mailto: ...
            continue
        if not os.path.exists(os.path.normpath(os.path.join(d, target))):
            errors.append(f"{rel(md_path)}: dead link -> {target}")

def rel(p): return os.path.relpath(p, ROOT).replace('\\', '/')

for skill_md in sorted(glob.glob(os.path.join(ROOT, 'plugins', '*', 'skills', '*', 'SKILL.md'))):
    skill_dir = os.path.dirname(skill_md)
    dirname = os.path.basename(skill_dir)
    text = io.open(skill_md, encoding='utf-8').read()

    fm = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not fm:
        errors.append(f"{rel(skill_md)}: no frontmatter"); continue
    name = re.search(r'^name:\s*(.+)$', fm.group(1), re.M)
    desc = re.search(r'^description:\s*(.+)$', fm.group(1), re.M)
    if not name: errors.append(f"{rel(skill_md)}: frontmatter has no name")
    if not desc: errors.append(f"{rel(skill_md)}: frontmatter has no description")
    if not (name and desc): continue

    name, desc = name.group(1).strip(), desc.group(1).strip()
    if name != dirname:
        errors.append(f"{rel(skill_md)}: name '{name}' != directory '{dirname}'")
    n = len(desc)
    if n > LIMIT:
        errors.append(f"{dirname}: description is {n} code points (limit {LIMIT})")
    elif n > SOFT:
        warnings.append(f"{dirname}: description is {n} code points (soft limit {SOFT})")
    if 'Use when' not in desc:
        warnings.append(f"{dirname}: description has no 'Use when' clause")

    for md in glob.glob(os.path.join(skill_dir, '*.md')):
        check_links(md)

for w in warnings: print("WARN ", w)
for e in errors:   print("ERROR", e)
total = len(glob.glob(os.path.join(ROOT, 'plugins', '*', 'skills', '*', 'SKILL.md')))
print(f"\n{total} skills checked: {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors or (STRICT and warnings) else 0)
