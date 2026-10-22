#!/usr/bin/env python3
"""Exact finite checks; not a proof of the universal Lean statements.
Requires SymPy 1.14.0. The production helper is loaded only after blob checking.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
import random
from pathlib import Path
from fractions import Fraction
import sympy as s

W,Z=s.symbols('W Z')
SEED=222026
BLOB='0c4ccb8f2dab99a5317f80345eae7920390fcbc0'

def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)

def nd(p):
    p=s.Poly(p,W,domain=s.QQ)
    return 0 if p.is_zero else int(p.degree())

def encode(p):
    return str(s.expand(p))

def fixed(F,a):
    cols=[s.expand(Z**i*F) for i in range(a-1)]
    cols += [s.expand(Z**i*s.diff(F,Z)) for i in range(a)]
    return s.Matrix(2*a-1,2*a-1,lambda i,j:cols[j].coeff(Z,i))

def run(source: Path):
    data=source.read_bytes()
    digest=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(digest==BLOB,'production source drift')
    spec=importlib.util.spec_from_file_location('frozen_multiplicity',source)
    prod=importlib.util.module_from_spec(spec);spec.loader.exec_module(prod)
    rng=random.Random(SEED)
    out={'seed':SEED,'source_blob':digest,'matrices':[],'sylvester':[],'planted':[],'negative_controls':[]}
    for n in range(5):
        for trial in range(12):
            d=[rng.randrange(4) for _ in range(n)]
            A=s.Matrix(n,n,lambda i,j:sum(rng.randrange(-2,3)*W**k for k in range(d[j]+1)))
            if n and trial%4==0:
                A[n-1,:]=s.zeros(1,n)
            E=s.expand(A.det(method='domain-ge'))
            require(nd(E)<=sum(d),'column degree bound')
            if n<=3:
                lap=0
                for p in itertools.permutations(range(n)):
                    inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
                    lap += (-1)**inv*s.prod(A[p[j],j] for j in range(n))
                require(s.expand(lap-E)==0,'permutation determinant mismatch')
            require(s.expand(A.T.det(method='domain-ge')-E)==0,'transpose mismatch')
            out['matrices'].append({'n':n,'trial':trial,'column_degrees':d,'matrix':[[encode(A[i,j]) for j in range(n)] for i in range(n)],'det':encode(E),'zero':E==0,'nat_degree':nd(E)})
    for a in range(1,5):
        for b in range(3):
            for trial in range(4):
                coeff=[sum(rng.randrange(-3,4)*W**k for k in range(b+1)) for _ in range(a+1)]
                coeff[a] += (1 if s.expand(coeff[a]).coeff(W,b)==0 else 0)*W**b
                F=s.expand(sum(coeff[i]*Z**i for i in range(a+1)))
                require(s.degree(F,Z)==a,'exact degree construction')
                M=fixed(F,a)
                E=s.expand(M.det(method='domain-ge'))
                R=s.resultant(F,s.diff(F,Z),Z)
                require(s.expand(E-R)==0,'actual matrix/resultant mismatch')
                require(nd(E)<=(2*a-1)*b,'Sylvester degree bound')
                evals=[]
                for t in [s.Rational(-2),s.Rational(1,2),s.Rational(3)]:
                    f=[Fraction(s.Rational(s.expand(F).coeff(Z,i).subs(W,t))) for i in range(a+1)]
                    d=prod.det(prod.fixed_sylvester(f,a))
                    require(s.Rational(d.numerator,d.denominator)==E.subs(W,t),'production evaluation mismatch')
                    pad=prod.det(prod.fixed_sylvester(f+[Fraction(0)],a+1))
                    require(pad==0,'degree overpadding did not vanish')
                    evals.append({'t':str(t),'value':str(d),'padded_value':str(pad)})
                out['sylvester'].append({'a':a,'b':b,'trial':trial,'F':encode(F),'det':encode(E),'nat_degree':nd(E),'zero':E==0,'evals':evals})
    for trial in range(24):
        a=2+trial%3; m=rng.randint(2,a); z0=rng.randint(-2,2); w0=rng.randint(-2,2)
        H=(Z-z0)**(a-m)+1
        G=sum(rng.randint(-2,2)*Z**i for i in range(a+1))
        if G==0:G=1
        F=s.expand((Z-z0)**m*H+(W-w0)*G)
        E=s.expand(fixed(F,a).det(method='domain-ge'))
        f0=s.Poly(F.subs(W,w0),Z)
        require(not f0.is_zero,'nonzero specialization')
        require(s.rem(f0.as_expr(),(Z-z0)**m,Z)==0,'planted multiplicity')
        require(s.rem(E,(W-w0)**(m-1),W)==0,'local multiplicity mismatch')
        contacts=[]
        if E!=0:
            for w in s.polys.polytools.ground_roots(s.Poly(E,W)):
                f=s.Poly(F.subs(W,w),Z)
                if f.is_zero:continue
                rr=s.polys.polytools.ground_roots(f)
                if rr:
                    z,mult=max(rr.items(),key=lambda pair:pair[1])
                    if mult>1:contacts.append((str(w),str(z),int(mult)))
            spent=sum(k-1 for _,_,k in contacts)
            require(spent<=nd(E),'sum of distinct contact orders')
            require(len(contacts)<=2*a-1,'excessive-contact count for b=1')
        out['planted'].append({'F':encode(F),'a':a,'m':m,'w0':w0,'z0':z0,'det':encode(E),'zero':E==0,'rational_contacts':contacts})
    sharp=W*(Z**2+Z+1); E=s.expand(fixed(sharp,2).det())
    require(E==3*W**3 and nd(E)>2,'sharper universal degree mutant not rejected')
    out['negative_controls'].append({'name':'replace_2a_minus_1_by_2a_minus_2','det':encode(E),'rejected':True})
    repeated=Z**2; E=s.expand(fixed(repeated,2).det());require(E==0,'repeated determinant')
    require(all(s.rem(repeated.subs(W,w),Z**2,Z)==0 and repeated.subs(W,w)!=0 for w in range(5)), 'repeated-factor premises')
    require(2>1 and len(set(range(5)))>2*2-1, 'nonzero-determinant mutant did not contradict cardinality')
    out['negative_controls'].append({'name':'drop_nonzero_determinant','F':'Z**2','b':1,'distinct_parameters':list(range(5)),'m_each':2,'cardinality':5,'claimed_bound':3,'rejected':True})
    F=W*(Z+1);E=s.expand(fixed(F,1).det());require(E==W and F.subs(W,0)==0,'zero-specialization witness')
    require(E!=0 and s.rem(F.subs(W,0),Z**100,Z)==0 and 100-1>nd(E), 'zero-specialization mutant did not contradict root budget')
    out['negative_controls'].append({'name':'drop_nonzero_specialization','F':encode(F),'det':encode(E),'w':0,'chosen_m':100,'impossible_degree_cost':99,'rejected':True})
    E=s.expand(fixed(Z-1,1).det());require(E==1,'b-zero witness')
    require(s.rem(Z-1,Z-1,Z)==0 and 1>0 and len({0,1})>2*1-1, 'b-positive mutant did not contradict cardinality')
    out['negative_controls'].append({'name':'drop_b_positive','F':'Z-1','b':0,'distinct_parameters':[0,1],'z_each':1,'m_each':1,'rejected':True})
    E=s.expand(fixed(Z**2-W,2).det());require(E==-4*W,'duplicate witness')
    require(s.rem(E,W,W)==0 and len([0]*5)*(2-1)>nd(E) and len(set([0]*5))==1, 'duplicate-count mutant did not contradict degree budget')
    out['negative_controls'].append({'name':'count_list_duplicates_as_distinct','parameters':[0]*5,'true_set_card':1,'false_list_card':5,'rejected':True})
    out['summary']={'general_matrices':len(out['matrices']),'bivariate_cases':len(out['sylvester']),'production_values':3*len(out['sylvester']),'overpadding_checks':3*len(out['sylvester']),'planted_cases':len(out['planted']),'zero_general_determinants':sum(x['zero'] for x in out['matrices']),'zero_sylvester_determinants':sum(x['zero'] for x in out['sylvester']),'zero_planted_determinants':sum(x['zero'] for x in out['planted']),'negative_controls':len(out['negative_controls']),'status':'PASS','scope':'finite same-author checks, not an irreducible nonvanishing proof'}
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    out=run(args.source);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['summary'],indent=2))
