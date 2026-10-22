#!/usr/bin/env python3
"""Matched jet-assembly controls. Setup/type/resource failures are not falsifiers."""
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
PRELUDE = 'import TenthDiscriminant\nopen Polynomial Matrix TenthDiscriminant TenthDiscriminant.JetAssembly\n'
PUBLIC = r'''
example (K : Type*) [Field K] [CharZero K]
    (F : Polynomial (Polynomial K)) (s : Finset K) (z : K -> K)
    (hz : Function.Injective z) (J : Nat) (hJ : wDegree F < J)
    (hc : 2*F.natDegree+wDegree F < s.card)
    (hj : forall w, w IN s -> forall j, j < J ->
      ((Polynomial.derivative^[j]) (specialize F w)).eval (z w) = 0) : F = 0 :=
  polynomial_eq_zero_of_jet_count F s z hz J hJ hc hj

example {n : Nat} (P : Finset Complex) (J R S : Nat)
    (hR : 1 <= R) (hS : 1 <= S) (rows : Fin n -> Nat * Nat)
    (hi : Function.Injective rows) (hr : forall i, (rows i).1 < R)
    (hs : forall i, (rows i).2 < S) (hJ : S <= J)
    (hc : 2*(R-1)+(S-1) < P.card) : 0 < (traceGramMatrix P J rows).det :=
  traceGramMatrix_det_pos_of_point_count P J R S hR hS rows hi hr hs hJ hc

-- Ender's stronger count guard reaches the actual matrix theorem without a new oracle.
example {n : Nat} (P : Finset Complex) (R S : Nat)
    (hR : 1 <= R) (hS : 1 <= S) (rows : Fin n -> Nat * Nat)
    (hi : Function.Injective rows) (hr : forall i, (rows i).1 < R)
    (hs : forall i, (rows i).2 < S) (hc : 3*R+S < P.card) :
    0 < (traceGramMatrix P S rows).det := by
  apply traceGramMatrix_det_pos_of_point_count P S R S hR hS rows hi hr hs (by omega)
  omega
'''.replace(' IN ', ' \u2208 ').replace('Nat * Nat', 'Nat \u00d7 Nat')

PAIRS = {
 'coefficient_variable_degree': (
  'example : wDegree (Polynomial.C (Polynomial.X^3 : Polynomial Rat)) = 3 := by simp',
  'example : wDegree (Polynomial.C (Polynomial.X^3 : Polynomial Rat)) = 2 := by simp'),
 'zero_fiber_retained': (
  'example : specialize (Polynomial.C (Polynomial.X-1 : Polynomial Rat)) 1 = 0 := by simp',
  'example : specialize (Polynomial.C (Polynomial.X-1 : Polynomial Rat)) 1 = 1 := by simp'),
 'ordinary_not_divided_derivative': (
  'example : ((Polynomial.derivative^[3]) (Polynomial.X^3 : Polynomial Rat)).eval 0 = 6 := by norm_num [Polynomial.iterate_derivative_X_pow_eq_C_mul, Nat.descFactorial]',
  'example : ((Polynomial.derivative^[3]) (Polynomial.X^3 : Polynomial Rat)).eval 0 = 1 := by norm_num [Polynomial.iterate_derivative_X_pow_eq_C_mul, Nat.descFactorial]'),
 'duplicate_row_exclusion': (
  'example : (traceGramMatrix {0} 2 (fun _ : Fin 2 => (0,0))).det = 0 := traceGramMatrix_duplicate_control',
  'example : 0 < (traceGramMatrix {0} 2 (fun _ : Fin 2 => (0,0))).det := by rw [traceGramMatrix_duplicate_control]; norm_num'),
 'sample_count_boundary': (
  'example : (traceGramMatrix {0} 1 (fun i : Fin 2 => (i.val,0))).det = 0 := comparatorR1_complex_translation',
  'example : 0 < (traceGramMatrix {0} 1 (fun i : Fin 2 => (i.val,0))).det := by rw [comparatorR1_complex_translation]; norm_num'),
 'origin_is_not_removed': (
  'example : (traceGramMatrix {0} 2 (fun _ : Fin 1 => (0,0))).det = 2 := traceGramMatrix_single_control',
  'example : (traceGramMatrix {0} 2 (fun _ : Fin 1 => (0,0))).det = 0 := by rw [traceGramMatrix_single_control]; norm_num'),
 'real_complex_rank_distinction': (
  'example : (traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det = 4 := traceGramMatrix_real_complex_control',
  'example : (traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det = 0 := by rw [traceGramMatrix_real_complex_control]; norm_num'),
 'characteristic_three_boundary': (
  'example : (Polynomial.X^3 - Polynomial.C Polynomial.X : Polynomial (Polynomial (ZMod 3))).derivative = 0 := comparatorR1_characteristic_three',
  'example : (Polynomial.X^3 - Polynomial.C Polynomial.X : Polynomial (Polynomial (ZMod 3))).derivative = 1 := by rw [comparatorR1_characteristic_three]; norm_num'),
}

def run(path: Path, source: str):
    path.write_text(PRELUDE+source+'\n', encoding='utf-8')
    return subprocess.run(['lake','env','lean',str(path)],cwd=ROOT,text=True,
                          capture_output=True,timeout=120)

with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    result = run(tmp/'public_api.lean', PUBLIC)
    if result.returncode:
        raise SystemExit('Public theorem instantiation failed:\n'+result.stdout+result.stderr)
    print('PASS: three universal jet/Gram/Ender API instantiations',flush=True)
    for name,(good,bad) in PAIRS.items():
        pos = run(tmp/(name+'_positive.lean'),good)
        if pos.returncode:
            raise SystemExit(name+' positive control failed:\n'+pos.stdout+pos.stderr)
        neg = run(tmp/(name+'_negative.lean'),bad)
        output = neg.stdout+neg.stderr
        if neg.returncode == 0 or 'error:' not in output:
            raise SystemExit(name+' false strengthening was accepted')
        if any(x in output for x in ('unknown identifier','unknown constant','unexpected token',
            'failed to synthesize','application type mismatch','maximum recursion depth',
            'maximum number of heartbeats','invalid field notation')):
            raise SystemExit(name+' failed for setup/type/resource reasons:\n'+output)
        print('PASS: '+name+'; true accepted, false strengthening rejected',flush=True)
        print(output.strip(),flush=True)
print('PASS: all jet-assembly API and matched mathematical controls')
