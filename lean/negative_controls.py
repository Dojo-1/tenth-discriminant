#!/usr/bin/env python3
"""Require Lean to reject known-false strengthening attempts."""
import pathlib
import subprocess
import tempfile

root = pathlib.Path(__file__).resolve().parent
cases = {
    'split_endpoint_included': 'example : 4*(41 : Nat) < 163+1 := by decide',
    'gap_accepted': 'example : TenthDiscriminant.checkChain 0 4 [(0,2),(3,4)] = true := by decide',
    'unbounded_multiplier': 'example : (100 : Rat)*10099-199^2 <= (9/25 : Rat)*(100*10099) := by norm_num',
}
with tempfile.TemporaryDirectory() as tmp:
    for label, statement in cases.items():
        p = pathlib.Path(tmp) / (label + '.lean')
        p.write_text('import TenthDiscriminant\n' + statement + '\n')
        r = subprocess.run(['lake','env','lean',str(p)], cwd=root, text=True, capture_output=True)
        if r.returncode == 0 or 'error:' not in r.stdout + r.stderr:
            raise SystemExit(f'FAIL: {label} was not rejected with a Lean error')
        print(f'PASS: rejected {label}')
        print(r.stdout.strip())
print('PASS: all three known-false statements rejected; this is not a universal mutation claim.')
