#!/usr/bin/env python3
"""Reject local proof escapes and audit compiled theorem dependencies in Lean."""
import pathlib
import re
import subprocess

root = pathlib.Path(__file__).resolve().parent
for path in sorted((root / 'TenthDiscriminant').rglob('*.lean')):
    text = path.read_text()
    code = re.sub(r'/\-.*?\-/', '', text, flags=re.S)
    code = re.sub(r'--[^\n]*', '', code)
    bad = re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b', code)
    if bad:
        raise SystemExit(f'{path.name}: forbidden proof escape: {bad.group(0)}')
run = subprocess.run(['lake','env','lean','Audit.lean'], cwd=root, text=True, capture_output=True)
print(run.stdout, end='')
print(run.stderr, end='')
if run.returncode:
    raise SystemExit(run.returncode)
if 'AUDIT_OK TenthDiscriminant:' not in run.stdout:
    raise SystemExit('No completed Lean environment audit')
print('PASS: compiled declarations audited; only propext, Classical.choice, Quot.sound allowed.')
