#!/usr/bin/env python3
"""Link the constructed Lean chain to the saved log; do not validate its margins."""
import hashlib
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[1]
p = root / 'ledger/coverage_ender.txt'
data = p.read_bytes()
expected_hash = '4e82ce50fd49436582af584d5cdc30d2449d59317582f846803d0d37da587fd8'
if hashlib.sha256(data).hexdigest() != expected_hash:
    raise SystemExit('Coverage source changed: re-audit the source/proof link before updating its digest')
actual = [tuple(map(int, m)) for m in re.findall(r'^CERTIFIED \[(\d+), (\d+)\]', data.decode(), re.M)]
x = 700000000000
expected = []
for _ in range(250):
    y = min(10**36, 5*x//4)
    expected.append((x,y))
    x = y
if actual != expected or x != 10**36:
    raise SystemExit('Recorded endpoints differ from the Lean recurrence')
print('PASS: source digest and all 250 interval pairs match the Lean recurrence.')
print('Scope: endpoint identity only; Arb inequalities are not certified by this check.')
