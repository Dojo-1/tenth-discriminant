#!/usr/bin/env python3
"""Audit every project theorem using Lean's transitive axiom reporting."""
import pathlib
import re
import subprocess
import tempfile

root = pathlib.Path(__file__).resolve().parent
names = []
for path in sorted((root / 'TenthDiscriminant').glob('*.lean')):
    text = path.read_text()
    code = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    code = re.sub(r'/\-.*?\-/', '', code, flags=re.S)
    code = re.sub(r'--[^\n]*', '', code)
    bad = re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b', code)
    if bad:
        raise SystemExit(f'{path.name}: forbidden proof escape: {bad.group(0)}')
    names.extend('TenthDiscriminant.' + n for n in re.findall(r'^theorem\s+(\w+)', code, flags=re.M))
if not names:
    raise SystemExit('No theorem declarations found')
with tempfile.TemporaryDirectory() as tmp:
    probe = pathlib.Path(tmp) / 'Audit.lean'
    probe.write_text('import TenthDiscriminant\n' + ''.join(f'#print axioms {n}\n' for n in names))
    run = subprocess.run(['lake','env','lean',str(probe)], cwd=root, text=True, capture_output=True)
    print(run.stdout, end='')
    print(run.stderr, end='')
    if run.returncode:
        raise SystemExit(run.returncode)
    output = run.stdout
    allowed = {'propext', 'Classical.choice', 'Quot.sound'}
    for n in names:
        matches = re.findall(r"'"+re.escape(n)+r"' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", output)
        if len(matches) != 1:
            raise SystemExit(f'Missing or ambiguous axiom report for {n}')
        used = {x.strip() for x in matches[0].split(',') if x.strip()}
        if used - allowed:
            raise SystemExit(f'{n}: nonstandard axioms {used-allowed}')
print(f'PASS: {len(names)} theorem declarations; only standard axioms allowed.')
