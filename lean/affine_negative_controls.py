#!/usr/bin/env python3
"""Matched accepted/rejected Lean statements; no compiler failure counts as proof."""
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
EXPR = ('(fixedDerivativeDeterminant '
        '(affineTransportPolynomial affineControlPolynomial 3 2 5 7 (-2)) 2).eval (3/7)')
SCALAR = ('(fixedDerivativeDeterminant '
          '(affineTransportPolynomial affineControlPolynomial 3 1 0 1 0) 2).eval 1')
ZERO = ('(fixedDerivativeDeterminant '
        '(affineTransportPolynomial affineControlPolynomial 0 1 0 1 0) 2).eval 1')
PAIRS = {
    'combined_frame': (
        f'example : {EXPR} = -1728 := affine_control_combined_value',
        f'example : {EXPR} = -432 := by rw [affine_control_combined_value]; norm_num'),
    'scalar_exponent': (
        f'example : {SCALAR} = -108 := affine_control_scalar_value',
        f'example : {SCALAR} = -324 := by rw [affine_control_scalar_value]; norm_num'),
    'singular_scale': (
        f'example : {ZERO} = 0 := affine_control_zero_scale',
        f'example : {ZERO} != 0 := by rw [affine_control_zero_scale]; norm_num'),
    'inverse_parameter': (
        'example : (7 : Rat)*((1-(-2))/7)+(-2) = 1 := by norm_num',
        'example : (7 : Rat)*(7*1+(-2))+(-2) = 1 := by norm_num'),
}
BAD_SETUP = ('unknown identifier', 'unknown constant', 'unexpected token',
             'failed to synthesize', 'type mismatch', 'maximum recursion depth',
             'maximum number of heartbeats')
with tempfile.TemporaryDirectory() as temp:
    for name, pair in PAIRS.items():
        for expected, source in zip((True, False), pair):
            file = pathlib.Path(temp) / f'{name}_{expected}.lean'
            file.write_text('import TenthDiscriminant\nopen TenthDiscriminant\n'+source+'\n')
            result = subprocess.run(['lake', 'env', 'lean', str(file)], cwd=ROOT,
                                    text=True, capture_output=True, timeout=120)
            output = result.stdout + result.stderr
            if expected:
                if result.returncode:
                    raise SystemExit(f'Positive control failed: {name}\n{output}')
            elif result.returncode == 0 or 'error:' not in output or any(x in output for x in BAD_SETUP):
                raise SystemExit(f'Negative control failed incorrectly: {name}\n{output}')
            print(f'PASS {name}: {"accepted" if expected else "rejected"}', flush=True)
            print(output.strip(), flush=True)
print('PASS: four matched affine-transport controls.')
