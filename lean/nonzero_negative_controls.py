#!/usr/bin/env python3
"""Matched controls for the actual nonvanishing bridge; fail on setup errors."""
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
PRE = 'import TenthDiscriminant\nopen Polynomial Matrix TenthDiscriminant\n'
PUBLIC = r'''
example (K : Type*) [Field K] [CharZero K]
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (hdeg : F.natDegree = a) (hi : Irreducible F) :
    (fixedSylvesterMatrix F F.derivative a (a-1)).det != 0 :=
  fixedDerivativeSylvester_ne_zero_of_irreducible F a ha hdeg hi

example (K : Type*) [Field K] (F : Polynomial (Polynomial K))
    (hp : F.IsPrimitive) (w : K) : F.map (Polynomial.evalRingHom w) != 0 :=
  primitive_specialization_ne_zero F hp w

example (K : Type*) [Field K] [CharZero K]
    (F : Polynomial (Polynomial K)) (a b : Nat) (ha : 1 <= a) (hb : 0 < b)
    (hdeg : F.natDegree = a) (hi : Irreducible F)
    (hw : forall i, (F.coeff i).natDegree <= b)
    (s : Finset K) (z : K -> K) (m : K -> Nat)
    (hroot : forall w, w IN s ->
      (Polynomial.X - Polynomial.C (z w))^(m w) DIV F.map (Polynomial.evalRingHom w))
    (hc : forall w, w IN s -> b < m w) : s.card <= 2*a-1 :=
  irreducible_fixedDerivativeSylvester_excessive_contact_card F a b ha hb hdeg hi hw s z m hroot hc
'''.replace('!=','\u2260').replace(' IN ',' \u2208 ').replace(' DIV ',' \u2223 ')
# Explicit lets avoid parsing projection notation on compound expressions.
POINT = '''let F : Polynomial (Polynomial Rat) := Polynomial.X^2 - Polynomial.C Polynomial.X
((fixedSylvesterMatrix F F.derivative 2 1).det).eval 0'''
PAD = '''let F : Polynomial (Polynomial Rat) := Polynomial.X^2 - Polynomial.C Polynomial.X
(fixedSylvesterMatrix F F.derivative 3 2).det'''
FIBER = '''let F : Polynomial (Polynomial Rat) := Polynomial.C Polynomial.X * (Polynomial.X + 1)
F.map (Polynomial.evalRingHom 0)'''
DROP = '''let F : Polynomial (Polynomial Rat) := Polynomial.C Polynomial.X * Polynomial.X + 1
F.map (Polynomial.evalRingHom 0)'''
CHAR3 = '''(Polynomial.X^3 - Polynomial.C Polynomial.X :
Polynomial (Polynomial (ZMod 3))).derivative'''
PAIRS = {
    'characteristic_zero_not_optional': (
        'example : '+CHAR3+' = 0 := comparatorR1_characteristic_three',
        'example : '+CHAR3+' != 0 := by rw [comparatorR1_characteristic_three]; norm_num'),
    'exact_degree_not_upper_bound': (
        'example : '+PAD+' = 0 := comparatorR1_overpadding',
        'example : '+PAD+' != 0 := by\n  dsimp only\n  rw [comparatorR1_overpadding]\n  norm_num'),
    'nonzero_polynomial_not_every_value': (
        'example : '+POINT+' = 0 := by\n  dsimp only\n  rw [quadratic_fixedSylvester_det]\n  norm_num',
        'example : '+POINT+' != 0 := by\n  dsimp only\n  rw [quadratic_fixedSylvester_det]\n  norm_num'),
    'nonprimitive_zero_fiber': (
        'example : '+FIBER+' = 0 := by simp',
        'example : '+FIBER+' != 0 := by simp'),
    'degree_loss_not_zero_fiber': (
        'example : '+DROP+' = 1 := by simp',
        'example : '+DROP+' = 0 := by simp'),
    'coprimality_not_optional': (
        'example : (fixedSylvesterMatrix (Polynomial.X^2 : Polynomial (Polynomial Rat)) (Polynomial.X^2 : Polynomial (Polynomial Rat)).derivative 2 1).det = 0 := repeated_fixedSylvester_det',
        'example : (fixedSylvesterMatrix (Polynomial.X^2 : Polynomial (Polynomial Rat)) (Polynomial.X^2 : Polynomial (Polynomial Rat)).derivative 2 1).det != 0 := by rw [repeated_fixedSylvester_det]; norm_num'),
}

def run(path, source):
    path.write_text(PRE+source.replace('!=','\u2260')+'\n',encoding='utf-8')
    return subprocess.run(['lake','env','lean',str(path)],cwd=ROOT,text=True,
                          capture_output=True,timeout=120)

with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    p = run(td/'public_api.lean',PUBLIC)
    if p.returncode:
        raise SystemExit('Public universal instantiation failed:\n'+p.stdout+p.stderr)
    print('PASS: three public nonvanishing/specialization/contact instantiations',flush=True)
    for name,(good,bad) in PAIRS.items():
        yes = run(td/(name+'_good.lean'),good)
        if yes.returncode:
            raise SystemExit(name+' good case failed:\n'+yes.stdout+yes.stderr)
        no = run(td/(name+'_bad.lean'),bad)
        text = no.stdout+no.stderr
        if no.returncode == 0 or 'error:' not in text:
            raise SystemExit(name+' false strengthening was not rejected')
        if any(x in text for x in ['unknown identifier','unknown constant','unexpected token',
                                   'failed to synthesize','application type mismatch',
                                   'maximum recursion depth','maximum number of heartbeats']):
            raise SystemExit(name+' failed for a setup/type/resource error:\n'+text)
        print('PASS: '+name+'; true accepted, false rejected',flush=True)
        print(text.strip(),flush=True)
print('PASS: all nonvanishing matched controls')
