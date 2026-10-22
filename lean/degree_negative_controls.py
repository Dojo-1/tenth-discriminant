#!/usr/bin/env python3
"""Matched degree-budget controls; malformed proof scripts do not count as rejection."""
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
PRELUDE = 'import TenthDiscriminant\nopen Polynomial Matrix TenthDiscriminant\n'
SHARP = '''
let F : Polynomial (Polynomial Rat) :=
  Polynomial.C Polynomial.X * (Polynomial.X^2 + Polynomial.X + 1)
((fixedSylvesterMatrix F F.derivative 2 1).det).coeff 3
'''
PAIRS = {
    'sharp_degree_coefficient': (
        'example : '+SHARP+' = 3 := by\n  dsimp only\n  rw [fixedDerivativeSylvester_degree_sharp_control]\n  norm_num',
        'example : '+SHARP+' = 0 := by\n  dsimp only\n  rw [fixedDerivativeSylvester_degree_sharp_control]\n  norm_num'),
    'zero_is_not_positive_degree': (
        'example : (0 : Polynomial Rat).natDegree = 0 := by simp',
        'example : 1 <= (0 : Polynomial Rat).natDegree := by norm_num'),
    'distinct_parameters_not_duplicate_list': (
        'example : ({(0 : Rat),0} : Finset Rat).card = 1 := by norm_num',
        'example : ({(0 : Rat),0} : Finset Rat).card = 2 := by norm_num'),
    'root_degree_sharpness': (
        'example : (Polynomial.X^2 : Polynomial Rat).natDegree = 2 := by simp',
        'example : (Polynomial.X^2 : Polynomial Rat).natDegree <= 1 := by norm_num'),
}
SINGLE_ROOT = '''
example (E : Polynomial Rat) (hE : E != 0) (a : Rat) (m : Nat)
    (h : (Polynomial.X - Polynomial.C a)^m | E) : m <= E.natDegree := by
  have hh := polynomial_distinct_root_power_budget E hE {a} (fun _ => m)
    (by intro w hw; have he : w = a := Finset.mem_singleton.mp hw; subst w; exact h)
  simpa using hh
'''.replace('!=', '\u2260').replace(' | E', ' \u2223 E')

def run(path, text):
    path.write_text(PRELUDE+text+'\n', encoding='utf-8')
    return subprocess.run(['lake','env','lean',str(path)], cwd=ROOT,
                          text=True, capture_output=True, timeout=120)

with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    result = run(tmp/'single_root.lean', SINGLE_ROOT)
    if result.returncode:
        raise SystemExit('Universal root-budget instantiation failed:\n'+result.stdout+result.stderr)
    print('PASS: universal root-budget single-point instantiation', flush=True)
    for name, (good,bad) in PAIRS.items():
        positive = run(tmp/(name+'_good.lean'),good)
        if positive.returncode:
            raise SystemExit(name+' positive control failed:\n'+positive.stdout+positive.stderr)
        negative = run(tmp/(name+'_bad.lean'),bad)
        output = negative.stdout+negative.stderr
        if negative.returncode == 0 or 'error:' not in output:
            raise SystemExit(name+' accepted a false statement')
        if any(x in output for x in ('unknown identifier','unknown constant','unexpected token',
                                    'failed to synthesize','application type mismatch',
                                    'maximum recursion depth','maximum number of heartbeats')):
            raise SystemExit(name+' rejected for a setup/type/resource error:\n'+output)
        print('PASS: '+name+'; true accepted, false arithmetic strengthening rejected', flush=True)
        print(output.strip(), flush=True)
print('PASS: all degree-budget mathematical controls')
