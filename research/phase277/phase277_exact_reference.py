#!/usr/bin/env python3
"""Phase277: independent small exact-det oracle for the local Smith pipeline.

Historical Phase205 source: D=19, R=8, S=J=4, rho=5, complete Q21.
Construct original ordinary-Z jets with pure Python integer pairs,
compute the exact 32x32 trace-Gram determinant by Bareiss, then recover
its p-adic valuations independently from local Smith decomposition.
p3 inert, p5 split, p7 split; no field classification assumption.
"""
from functools import lru_cache
from collections import Counter
from math import factorial
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from phase277_saturate import local_smith_with_U,gram_mod_power

D,R,S,J,RHO=19,8,4,4,5
Q=tuple((x,y) for x in range(-RHO,RHO+1)
        for y in range(-RHO,RHO+1) if x*x+D*y*y<=RHO*RHO)
assert len(Q)==21

def mult(v,w):
    a,b=v;c,d=w
    return (a*c-D*b*d,a*d+b*c)

@lru_cache(None)
def power(z,n):
    a=(1,0)
    for _ in range(n):a=mult(a,z)
    return a

def jet(r,s,j,z):
    if j>r:return (0,0)
    a,b=mult(power(z,r-j),power((z[0],-z[1]),s))
    factor=factorial(r)//factorial(r-j)
    return (factor*a,factor*b)

def exact_det(a):
    x=[list(row) for row in a]
    n=len(x)
    sign=1;prev=1
    for i in range(n-1):
        if x[i][i]==0:
            j=next((j for j in range(i+1,n) if x[j][i]),None)
            if j is None:return 0
            x[i],x[j]=x[j],x[i]
            sign=-sign
        pivot=x[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                v=x[j][k]*pivot-x[j][i]*x[i][k]
                assert v%prev==0
                x[j][k]=v//prev
            x[j][i]=0
        prev=pivot
    return sign*x[-1][-1]

def vp(v,p):
    assert v!=0
    k=0
    while v%p==0:
        v//=p;k+=1
    return k

def original_gram(E):
    weights=[w for j in range(J) for q in Q for w in (2,2*D)]
    return [[sum(a*b*w for a,b,w in zip(E[i],E[k],weights))
             for k in range(len(E))] for i in range(len(E))]

def run():
    E=[[v for j in range(J) for q in Q for v in jet(r,s,j,q)]
       for r in range(R) for s in range(S)]
    assert len(E)==32 and len(E[0])==168
    G=original_gram(E)
    det=exact_det(G)
    assert det>0
    assert G[0][0]==42 and G[0][8]==-120
    expected=[
        (3,{0:17,1:11,2:4},{0:31,1:1},39),
        (5,{0:32},{0:29,1:2,2:1},4),
        (7,{0:32},{0:32},0)
    ]
    for p,exps_expected,resid_expected,v_expected in expected:
        precision=6 if p!=7 else 4
        E_mod=np.asarray(E,dtype=np.int64)%(p**precision)
        exps,primitive=local_smith_with_U(E_mod,p,precision,
                                            prim_precision=3,log=False)
        assert primitive is not None
        assert dict(Counter(exps))==exps_expected,(p,Counter(exps))
        H=gram_mod_power(primitive,p,3,weight_D=D)
        rexp,_=local_smith_with_U(H,p,3,prim_precision=1,log=False)
        assert dict(Counter(rexp))==resid_expected,(p,Counter(rexp))
        computed=2*sum(exps)+sum(rexp)
        actual=vp(det,p)
        assert computed==actual==v_expected,(p,computed,actual)
        print('EXACT_REFERENCE',dict(D=D,p=p,source_smith=exps_expected,
              residual_smith=resid_expected,det_vp=actual),flush=True)
    print('PASS pure-Python Bareiss original Gram matches modular Smith',flush=True)

if __name__=='__main__':
    run()
