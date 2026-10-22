#!/usr/bin/env python3
"""Matched local multiplicity controls. Reject setup errors, not just nonzero exits."""
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
HEADER = 'import TenthDiscriminant\nopen Polynomial TenthDiscriminant\n'
F = '(Polynomial.X^2 - Polynomial.C Polynomial.X : Polynomial (Polynomial Rat))'
pairs = {
    'taylor_det_one': (
        'example : (taylorCoefficientMatrix 4 (3 : Rat)).det = 1 := taylorCoefficientMatrix_det 4 3',
        'example : (taylorCoefficientMatrix 4 (3 : Rat)).det = 0 := by rw [taylorCoefficientMatrix_det]; norm_num'),
    'sharp_exponent': (
        f'example : ((fixedSylvesterMatrix {F} {F}.derivative 2 1).det).coeff 1 = -4 := quadratic_fixedSylvester_linear_coefficient',
        f'example : ((fixedSylvesterMatrix {F} {F}.derivative 2 1).det).coeff 1 = 0 := by rw [quadratic_fixedSylvester_linear_coefficient]; norm_num'),
    'repeated_factor': (
        'example : (fixedSylvesterMatrix (Polynomial.X^2 : Polynomial (Polynomial Rat)) (Polynomial.X^2 : Polynomial (Polynomial Rat)).derivative 2 1).det = 0 := repeated_fixedSylvester_det',
        'example : (fixedSylvesterMatrix (Polynomial.X^2 : Polynomial (Polynomial Rat)) (Polynomial.X^2 : Polynomial (Polynomial Rat)).derivative 2 1).det = 1 := by rw [repeated_fixedSylvester_det]; norm_num'),
    'translated_root': (
        'example : (Polynomial.taylor (3 : Rat) ((Polynomial.X - Polynomial.C 3)^2)).coeff 1 = 0 := taylor_coeff_zero_of_root_power _ 3 2 1 (dvd_refl _) (by decide)',
        'example : (Polynomial.taylor (3 : Rat) ((Polynomial.X - Polynomial.C 3)^2)).coeff 1 = 1 := by rw [taylor_coeff_zero_of_root_power _ 3 2 1 (dvd_refl _) (by decide)]; norm_num'),
}
with tempfile.TemporaryDirectory() as directory:
    for label,(good,bad) in pairs.items():
        for positive,source in [(True,good),(False,bad)]:
            path = pathlib.Path(directory)/(label+('_good' if positive else '_bad')+'.lean')
            path.write_text(HEADER+source+'\n',encoding='utf-8')
            result = subprocess.run(['lake','env','lean',str(path)],cwd=ROOT,
                                    capture_output=True,text=True,timeout=120)
            output = result.stdout+result.stderr
            if positive and result.returncode:
                raise SystemExit(f'Positive control failed: {label}\n{output}')
            if not positive:
                if result.returncode == 0 or 'error:' not in output or 'False' not in output:
                    raise SystemExit(f'False control did not reach arithmetic contradiction: {label}\n{output}')
                if any(x in output for x in ['unknown identifier','unknown constant','unexpected token',
                                             'failed to synthesize','type mismatch']):
                    raise SystemExit(f'Unintended negative-control failure: {label}\n{output}')
        print(f'PASS: multiplicity {label}; valid accepted, false rejected',flush=True)
subprocess.run([sys.executable,str(ROOT/'multiplicity_exact_controls.py')],cwd=ROOT,
               check=True,timeout=120)
