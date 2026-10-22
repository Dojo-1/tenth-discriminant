#!/usr/bin/env python3
"""Matched good/bad controls and executable tests of the transitive axiom gate."""
import pathlib
import subprocess
import sys
import tempfile

root = pathlib.Path(__file__).resolve().parent
pairs = {
    'split_endpoint': (
        'example : 4*(40 : Nat) < 163+1 := by decide',
        'example : 4*(41 : Nat) < 163+1 := by decide'),
    'coverage_gap': (
        'example : TenthDiscriminant.checkChain 0 4 [(0,2),(2,4)] = true := by decide',
        'example : TenthDiscriminant.checkChain 0 4 [(0,2),(3,4)] = true := by decide'),
    'multiplier_range': (
        'example : (5 : Rat)*20-8^2 <= (9/25 : Rat)*(5*20) := by norm_num',
        'example : (100 : Rat)*10099-199^2 <= (9/25 : Rat)*(100*10099) := by norm_num'),
    'gram_duplicate_rows': (
        'example : (TenthDiscriminant.traceGramMatrix {0} 2 (fun _ : Fin 2 => (0,0))).det = 0 := TenthDiscriminant.traceGramMatrix_duplicate_control',
        'example : 0 < (TenthDiscriminant.traceGramMatrix {0} 2 (fun _ : Fin 2 => (0,0))).det := by rw [TenthDiscriminant.traceGramMatrix_duplicate_control]; norm_num'),
    'gram_unmatched_column': (
        'example : (TenthDiscriminant.traceGramMatrix {1} 2 (fun i : Fin 2 => if i = 0 then (0,0) else (1,1))).det = 4 := TenthDiscriminant.traceGramMatrix_unmatched_control',
        'example : (TenthDiscriminant.traceGramMatrix {1} 2 (fun i : Fin 2 => if i = 0 then (0,0) else (1,1))).det = 0 := by rw [TenthDiscriminant.traceGramMatrix_unmatched_control]; norm_num'),
    'gram_trace_normalization': (
        'example : (TenthDiscriminant.traceGramMatrix {0} 2 (fun _ : Fin 1 => (0,0))).det = 2 := TenthDiscriminant.traceGramMatrix_single_control',
        'example : (TenthDiscriminant.traceGramMatrix {0} 2 (fun _ : Fin 1 => (0,0))).det = 1 := by rw [TenthDiscriminant.traceGramMatrix_single_control]; norm_num'),
}
probes = {
    'kernel_proof': (True, 'namespace ProofAuditProbe\nprivate theorem ok : 2+2=4 := by decide\nend ProofAuditProbe'),
    'transitive_incomplete_proof': (False, 'namespace ExternalProbe\ntheorem gap : False := by sorry\nend ExternalProbe\nnamespace ProofAuditProbe\nlemma bad : False := ExternalProbe.gap\nend ProofAuditProbe'),
    'transitive_custom_axiom': (False, 'namespace ExternalProbe\naxiom gap : False\nend ExternalProbe\nnamespace ProofAuditProbe\ntheorem bad : False := ExternalProbe.gap\nend ProofAuditProbe'),
    'native_evaluation': (False, 'namespace ProofAuditProbe\ntheorem native : 2+2=4 := by native_decide\nend ProofAuditProbe'),
}
with tempfile.TemporaryDirectory() as tmp:
    def run(label, source):
        p = pathlib.Path(tmp) / (label+'.lean')
        p.write_text('import TenthDiscriminant\n'+source+'\n', encoding='utf-8')
        return subprocess.run(['lake','env','lean',str(p)], cwd=root, text=True,
                              capture_output=True, timeout=120)
    for label, (good,bad) in pairs.items():
        positive = run(label+'_positive', good)
        if positive.returncode:
            raise SystemExit(f'Positive control failed: {label}\n{positive.stdout}\n{positive.stderr}')
        negative = run(label+'_negative', bad)
        output = negative.stdout + negative.stderr
        if negative.returncode == 0 or 'error:' not in output:
            raise SystemExit(f'Known-false statement was not rejected: {label}')
        if any(marker in output for marker in (
                'unknown identifier', 'unknown constant', 'unexpected token', 'failed to synthesize')):
            raise SystemExit(f'Negative control failed for an unintended setup/type error: {label}\n{output}')
        print(f'PASS: {label}, good accepted / false strengthening rejected', flush=True)
        print(output.strip(), flush=True)
    for label, (should_pass,source) in probes.items():
        result = run(label, source+'\n#audit_namespace ProofAuditProbe')
        output = result.stdout+result.stderr
        if should_pass:
            if result.returncode or 'AUDIT_OK ProofAuditProbe:' not in output:
                raise SystemExit(f'Positive audit control failed: {label}\n{output}')
        else:
            if result.returncode == 0 or 'NONSTANDARD_AXIOMS' not in output:
                raise SystemExit(f'Audit gate did not reject the intended dependency: {label}\n{output}')
        print(f'PASS: proof-audit control {label}', flush=True)
        print(output.strip(), flush=True)
subprocess.run([sys.executable, str(root / 'exact_gram_controls.py')],
               cwd=root, check=True, timeout=120)
subprocess.run([sys.executable, str(root / 'jet_uniqueness_controls.py')],
               cwd=root, check=True, timeout=120)
subprocess.run([sys.executable, str(root / 'jet_negative_controls.py')],
               cwd=root, check=True, timeout=120)
print('PASS: matched mathematical controls, proof-audit controls, exact Gram and jet controls.')
