#!/usr/bin/env python3
"""Matched controls for the real/complex and fixed-parameter jet boundaries."""
import pathlib
import subprocess
import tempfile

root=pathlib.Path(__file__).resolve().parent
pairs={
    'real_vs_complex': (
        'example : (TenthDiscriminant.traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det = 4 := TenthDiscriminant.traceGramMatrix_real_complex_control',
        'example : (TenthDiscriminant.traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det = 0 := by rw [TenthDiscriminant.traceGramMatrix_real_complex_control]; norm_num'),
    'fixed_w_derivative': (
        'example : ((Polynomial.derivative^[1]) (TenthDiscriminant.rowSection (fun _ : Fin 1 => (0,1)) (fun _ => (1 : Complex)) 1)).eval 1 = 0 := by norm_num [TenthDiscriminant.rowSection]',
        'example : ((Polynomial.derivative^[1]) (TenthDiscriminant.rowSection (fun _ : Fin 1 => (0,1)) (fun _ => (1 : Complex)) 1)).eval 1 = 1 := by norm_num [TenthDiscriminant.rowSection]'),
    'jet_order_boundary': (
        'example : ((Polynomial.derivative^[2]) ((Polynomial.C (1 : Complex)*Polynomial.X-1)^2)).eval 1 = 2 := by norm_num [Function.iterate_succ_apply, Polynomial.derivative_pow]',
        'example : ((Polynomial.derivative^[2]) ((Polynomial.C (1 : Complex)*Polynomial.X-1)^2)).eval 1 = 0 := by norm_num [Function.iterate_succ_apply, Polynomial.derivative_pow]'),
}
with tempfile.TemporaryDirectory() as tmp:
    for label,(good,bad) in pairs.items():
        for positive,source in [(True,good),(False,bad)]:
            p=pathlib.Path(tmp)/(label+('_positive' if positive else '_negative')+'.lean')
            p.write_text('import TenthDiscriminant\n'+source+'\n',encoding='utf-8')
            r=subprocess.run(['lake','env','lean',str(p)],cwd=root,capture_output=True,text=True,timeout=120)
            output=r.stdout+r.stderr
            if positive:
                if r.returncode:
                    raise SystemExit(f'Positive jet control failed: {label}\n{output}')
            else:
                if r.returncode==0 or 'error:' not in output:
                    raise SystemExit(f'Known-false jet control accepted: {label}')
                if any(t in output for t in ['unknown identifier','unknown constant','unexpected token','failed to synthesize','application type mismatch']):
                    raise SystemExit(f'Negative jet control failed for a setup error: {label}\n{output}')
                print(output.strip(),flush=True)
        print(f'PASS: jet control {label}: true accepted, false rejected',flush=True)
