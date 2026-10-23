#!/usr/bin/env python3
"""Finite exact controls for the fixed-Sylvester nonzero bridge.

No proof of the universal Lean theorem; separate implementations share authorship.
Run with --source PATH to the blob-pinned production rational helper.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import random
import sys
import sympy as sp

Z, W = sp.symbols('Z W')
SOURCE_BLOB = '0c4ccb8f2dab99a5317f80345eae7920390fcbc0'
SEED = 20261023

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def load_source(path: Path):
    data = path.read_bytes()
    digest = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    require(digest == SOURCE_BLOB, 'production source drift')
    spec = importlib.util.spec_from_file_location('pinned_multiplicity', path)
    require(spec is not None and spec.loader is not None, 'module specification missing')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def matrix(f, g, a: int, b: int):
    require(a >= 0 and b >= 0, 'negative matrix bound')
    n = a + b
    cols = [sp.Poly(Z**j*f, Z) for j in range(b)]
    cols += [sp.Poly(Z**j*g, Z) for j in range(a)]
    return sp.Matrix(n, n, lambda i,j: cols[j].nth(i))

def poly_degree(f, var):
    return None if sp.expand(f) == 0 else int(sp.degree(f, var))

def primitive(f):
    coeffs = sp.Poly(f, Z).all_coeffs()
    content = sp.gcd_list(coeffs)
    return sp.degree(content, W) == 0

def run(source: Path):
    prod = load_source(source)
    rng = random.Random(SEED)
    pairs = []
    for case in range(48):
        a, b = 1 + case % 5, (case // 5) % 4
        f = sum(rng.randint(-3,3)*Z**i for i in range(a)) + rng.choice([-2,-1,1,2])*Z**a
        g = sum(rng.randint(-3,3)*Z**i for i in range(b+1))
        if case % 8 == 0:
            g = 0
        if case % 8 == 1 and b >= 1:
            f = sp.expand((Z-1)*(Z**(a-1)+1))
            g = sp.expand((Z-1)*(Z**(b-1)+1))
        M = matrix(f,g,a,b)
        d = M.det(method='domain-ge')
        dprod = sp.Rational(prod.det(M.tolist()))
        coprime = sp.degree(sp.gcd(f,g), Z) == 0
        require((d != 0) == coprime, 'field coprimality/determinant disagreement')
        require(d == dprod, 'fraction-elimination comparator mismatch')
        require((M*sp.zeros(a+b,1)) == sp.zeros(a+b,1), 'zero kernel control')
        for v in M.nullspace():
            A = sum(v[j]*Z**j for j in range(b))
            B = sum(v[b+j]*Z**j for j in range(a))
            require(sp.expand(A*f+B*g)==0, 'matrix kernel did not map to syzygy')
        reverse = M[::-1,::-1]
        require(reverse.det(method='domain-ge') == d, 'reindexing changed determinant')
        pairs.append({'f':str(f),'g':str(g),'a':a,'b':b,'gcd':str(sp.gcd(f,g)),
                      'determinant':str(d),'nullity':len(M.nullspace())})
    specs=[]
    for a in range(1,7):
        for k in range(4):
            c=rng.randint(-3,3)
            r=[rng.choice([-3,-2,-1,1,2,3])]+[rng.randint(-3,3) for _ in range(a-1)]
            specs.append(('eisenstein',sp.expand(Z**a+(W-c)*sum(r[j]*Z**j for j in range(a))),a,c,True))
    for a in range(2,6):
        for c in [-2,0,3]:
            specs.append(('leading_degree_loss',sp.expand((W-c)*Z**a+Z+1),a,c,True))
    for c in [-2,0,3,5]:
        specs.append(('repeated',sp.expand((Z-W-c)**2),2,c,False))
        specs.append(('separable_reducible',sp.expand((Z-W-c)*(Z-W-c-1)),2,c,False))
        specs.append(('nonprimitive',sp.expand((W-c)*(Z**2+Z+1)),2,c,False))
    polys=[]
    for family,f,a,c,intended_irreducible in specs:
        p=sp.Poly(f,Z,domain=sp.QQ.poly_ring(W))
        require(int(p.degree())==a, 'global degree drift')
        df=sp.diff(f,Z)
        E=sp.expand(sp.resultant(f,df,Z))
        g=sp.gcd(sp.Poly(f,Z,domain=sp.QQ.frac_field(W)),sp.Poly(df,Z,domain=sp.QQ.frac_field(W)))
        require((E!=0)==(g.degree()==0),'fraction-field bridge mismatch')
        factors=sp.factor_list(f,Z,W)[1]
        irreducible=(len(factors)==1 and factors[0][1]==1)
        require(irreducible==intended_irreducible,'unexpected factorization in declared stratum')
        if irreducible:
            require(E!=0 and primitive(f),'irreducibility bridge failed')
        evaluations=[]
        for w in [sp.Rational(c),sp.Rational(1,2),sp.Rational(c+2)]:
            fw=sp.expand(f.subs(W,w))
            M=matrix(fw,sp.diff(fw,Z),a,a-1)
            d=M.det(method='domain-ge')
            coeffs=[p.nth(i).subs(W,w) for i in range(a+1)]
            pm=prod.fixed_sylvester(coeffs,a)
            require(sp.Matrix(pm)==M,'actual matrix correspondence mismatch')
            require(sp.Rational(prod.det(pm))==d==E.subs(W,w),'specialization/resultant mismatch')
            if primitive(f):
                require(fw!=0,'primitive polynomial had zero fiber')
            padded=matrix(fw,sp.diff(fw,Z),a+1,a)
            require(padded.det(method='domain-ge')==0,'overpadding control failed')
            evaluations.append({'w':str(w),'specialization':str(fw),
                                'specialized_degree':poly_degree(fw,Z),'value':str(d)})
        polys.append({'family':family,'F':str(f),'a':a,'primitive':bool(primitive(f)),
                      'irreducible_reference':irreducible,'E':str(E),'evaluations':evaluations})
    controls={}
    controls['exact_degree_required']=matrix(Z**2-W,2*Z,3,2).det()==0 and sp.resultant(Z**2-W,2*Z,Z)!=0
    controls['nonzero_polynomial_not_everywhere_nonzero']=sp.resultant(Z**2-W,2*Z,Z)==-4*W
    controls['repeated_factor']=sp.resultant((Z-W)**2,2*(Z-W),Z)==0
    controls['nonprimitive_zero_fiber']=sp.expand((W*(Z+1)).subs(W,0))==0 and sp.resultant(W*(Z+1),W,Z)==W
    controls['degree_zero_zero_fiber']=W.subs(W,0)==0
    c3=matrix(Z**3-W,3*Z**2,3,2)
    controls['positive_characteristic']=all(sp.Poly(x,Z,W,modulus=3).is_zero for x in c3[:,2:])
    for name,ok in controls.items():
        require(bool(ok),'nondiscriminating control '+name)
    boundary={'empty':str(matrix(1,0,0,0).det()),'unit_F':str(matrix(2,Z,0,2).det())}
    require(boundary=={'empty':'1','unit_F':'4'},'constant/empty boundary mismatch')
    return {'status':'PASS','seed':SEED,'production_blob':SOURCE_BLOB,'python':sys.version.split()[0],
            'sympy':sp.__version__,'general_pairs':pairs,'polynomial_cases':polys,
            'controls':{k:bool(v) for k,v in controls.items()},'boundary':boundary,
            'counts':{'general_pairs':len(pairs),'singular_general':sum(x['determinant']=='0' for x in pairs),
                      'polynomial_cases':len(polys),'irreducible_cases':sum(x['irreducible_reference'] for x in polys),
                      'production_specializations':sum(len(x['evaluations']) for x in polys),
                      'zero_polynomial_determinants':sum(x['E']=='0' for x in polys),
                      'negative_controls':len(controls)},
            'scope':'finite same-author controls; exact algebraic paths, not independent semantic review or universal Python/Lean equivalence'}

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    result=run(args.source)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['counts'],sort_keys=True))
