#!/usr/bin/env python3
"""Finite same-author checks of affine covariance; separate from the Lean proof.
Run: python lean/affine_exact_controls.py --source lean/multiplicity_exact_controls.py
Requires SymPy. The matrix remains fixed at the source's exact global Z degree.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as sp

EXPECTED = '0c4ccb8f2dab99a5317f80345eae7920390fcbc0'
Z, W = sp.symbols('Z W')

def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)

def load_source(path: Path):
    content = path.read_bytes()
    sha = hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
    require(sha == EXPECTED, 'production source drift')
    spec = importlib.util.spec_from_file_location('pinned_multiplicity', path)
    require(spec is not None and spec.loader is not None, 'cannot import pinned source')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def rat(value) -> Fraction:
    x = sp.Rational(value)
    return Fraction(int(x.p), int(x.q))

def run(source: Path) -> dict:
    impl = load_source(source)
    frames = [(sp.Rational(3),sp.Rational(2),sp.Rational(5),sp.Rational(7),sp.Rational(-2)),
              (sp.Rational(-2,3),sp.Rational(-3,2),sp.Rational(1,3),sp.Rational(2,5),sp.Rational(7,4)),
              (sp.Rational(1),sp.Rational(1),sp.Rational(0),sp.Rational(1),sp.Rational(0))]
    cases=[]
    evaluations=0
    zero_evaluations=0
    degree_drops=0
    for a in range(1,5):
        families=[Z**a-W, (W-1)*Z**a+Z**(a-1)+W+1,
                  (Z-2)**a, Z**a+(W**2+2)*Z+W+3]
        for family,F in enumerate(families):
            require(sp.degree(F,Z)==a, 'wrong declared degree')
            E=sp.Poly(sp.resultant(F,sp.diff(F,Z),Z),W)
            for lam,u,h,v,b in frames:
                G=sp.expand(lam*F.subs({Z:u*Z+h,W:v*W+b}, simultaneous=True))
                E2=sp.Poly(sp.resultant(G,sp.diff(G,Z),Z),W)
                factor=lam**(2*a-1)*u**(a*a)
                expected=sp.Poly(factor*E.as_expr().subs(W,v*W+b),W)
                require(E2==expected, 'whole polynomial transport mismatch')
                values=[]
                for t in [sp.Rational(0),sp.Rational(1),sp.Rational(3,2)]:
                    target=(t-b)/v
                    def fixed_value(P,point):
                        coeffs=[rat(sp.expand(P).coeff(Z,i).subs(W,point)) for i in range(a+1)]
                        return impl.det(impl.fixed_sylvester(coeffs,a))
                    d=fixed_value(F,t); new=fixed_value(G,target)
                    require(new==rat(factor)*d, 'fixed matrix value mismatch')
                    require(d==rat(E.eval(t)) and new==rat(E2.eval(target)), 'resultant comparator mismatch')
                    degree_drops += int(sp.Poly(F.subs(W,t),Z).degree()<a)
                    zero_evaluations += int(d==0)
                    evaluations += 1
                    values.append({'source_point':str(t),'target_point':str(target),
                                   'source_value':str(d),'target_value':str(new)})
                cases.append({'degree':a,'family':family,'polynomial':str(F),
                              'frame':[str(x) for x in (lam,u,h,v,b)],'factor':str(factor),
                              'source_resultant':str(E.as_expr()),'values':values})
    F=Z**2-W
    G=3*F.subs({Z:2*Z+5,W:7*W-2},simultaneous=True)
    E=sp.resultant(G,sp.diff(G,Z),Z)
    correct=E.subs(W,sp.Rational(3,7))
    require(correct==-1728, 'known combined transport value')
    require(correct != 3**3*2**2*(-4), 'missing derivative slope mutant survived')
    require(correct != 3**4*2**4*(-4), 'wrong scalar exponent mutant survived')
    require(E.subs(W,5) != correct, 'forward-point mutant survived')
    H=W*Z**2+Z+1
    require(sp.resultant(H,sp.diff(H,Z),Z).subs(W,0)==0, 'fixed degree-loss reference')
    require(sp.resultant(H.subs(W,0),sp.diff(H,Z).subs(W,0),Z)==1, 'smaller rebuilt resultant reference')
    return {'status':'PASS','sympy':sp.__version__,'source_blob':EXPECTED,
            'whole_polynomial_cases':len(cases),'fixed_matrix_evaluation_pairs':evaluations,
            'zero_evaluation_controls':zero_evaluations,'degree_loss_evaluations':degree_drops,
            'incorrect_shortcuts_rejected':3,'degree_loss_object_change_control':True,
            'scope':'finite same-author exact controls; not a universal implementation equivalence proof',
            'cases':cases}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,default=Path(__file__).with_name('multiplicity_exact_controls.py'))
    args=parser.parse_args()
    print(json.dumps(run(args.source),indent=2))
