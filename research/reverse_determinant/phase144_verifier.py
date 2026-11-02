#!/usr/bin/env python3
"""Phase144: original ordinary-jet cokernel, Smith factors, and metric strata.

Finite exact test only; no new field-discriminant bound. Run from the repository
with SymPy: python3 research/reverse_determinant/phase144_verifier.py
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
from math import prod, log
from pathlib import Path
import sys
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ellipsoid_trimming'))
from phase140_exact_trim import D, R, S, J, ORIGINAL, NESTED, jets
assert (D,R,S,J)==(19,8,4,4)
FOUR=[(-2,-1),(-1,-1),(0,-1),(1,-1)]
FULL=sorted(ORIGINAL)
THIN=sorted(NESTED)
assert len(FULL)==21 and len(THIN)==19 and set(FULL)-set(THIN)=={(-5,0),(5,0)}

def evaluation(Q):
    columns=[]
    for q in Q:
        rows=jets(q)
        for j in range(J):
            for coordinate in (0,1):
                columns.append([rows[i][j][coordinate] for i in range(R*S)])
    return Matrix(R*S,len(columns),lambda i,j:columns[j][i])

def val(n,p):
    count=0
    while n%p==0 and n:
        count+=1;n//=p
    return count

def smith(H):
    M=smith_normal_form(H,domain=ZZ)
    diag=[abs(int(M[i,i])) for i in range(M.rows)]
    assert all(diag[i]>0 for i in range(len(diag)))
    assert all(diag[i+1]%diag[i]==0 for i in range(len(diag)-1))
    return diag

def lattice(E,det_witness):
    assert det_witness>0
    H=hermite_normal_form(E,D=det_witness)
    assert H.shape==(R*S,R*S)
    d=abs(int(H.det(method='domain-ge')))
    return H,d

def square_witness(Q):
    reals=sorted((q for q in Q if q[1]==0),key=lambda q:(abs(q[0]),q[0]))
    if len(reals)>=R:
        ER=evaluation(reals[:R])
        X=ER[:,list(range(0,ER.cols,2))]
        assert X.shape==(R*S,R*S)
        det=abs(int(X.det(method='domain-ge')))
        assert det>0
        return det
    for y in (-1,1):
        points=sorted(q for q in Q if q[1]==y)
        if len(points)>=4:
            det=abs(int(evaluation(points[:4]).det(method='domain-ge')))
            if det>0:return det
    raise ValueError('No certified full-rank square witness for this Q')

def rank_mod(E,p):
    a=[[int(E[i,j])%p for j in range(E.cols)] for i in range(E.rows)]
    k=0
    for j in range(E.cols):
        pivot=next((i for i in range(k,E.rows) if a[i][j]),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        inverse=pow(a[k][j],-1,p)
        a[k][j:]=[(inverse*x)%p for x in a[k][j:]]
        for i in range(k+1,E.rows):
            t=a[i][j]
            if t:a[i][j:]=[(x-t*y)%p for x,y in zip(a[i][j:],a[k][j:])]
        k+=1
        if k==E.rows:break
    return k

def gram_det(E):
    B=Matrix.diag(*([2,2*D]*(E.cols//2)))
    return int((E*B*E.T).det(method='domain-ge'))

def main():
    fourdet=abs(int(evaluation(FOUR).det(method='domain-ge')))
    assert fourdet>0 and set(FOUR).issubset(THIN)
    E0=evaluation(FULL);E1=evaluation(THIN)
    H0,d0=lattice(E0,fourdet);H1,d1=lattice(E1,fourdet)
    assert H0==H1 and d0==d1==2**56*3**19
    smith0=smith(H0)
    assert smith0==smith(H1)
    assert smith0==[1]*8+[2]*8+[4]+[12]*3+[24]*8+[144]*4
    g0=gram_det(E0);g1=gram_det(E1)
    assert 0<g1<g0 and g0%(d0*d0)==0 and g1%(d1*d1)==0
    assert (val(g0,3),val(g1,3))==(39,38)
    assert (rank_mod(E0,2),rank_mod(E1,2))==(8,8)
    assert (rank_mod(E0,3),rank_mod(E1,3))==(17,17)
    print('full/thin index:',d0,'factorization 2^56*3^19')
    print('Smith factors:',smith0)
    print('logdet full/thin:',f'{log(g0):.9f}',f'{log(g1):.9f}')
    print('v3(det G) full/thin:',val(g0,3),val(g1,3),'v3(primitive):',val(g0,3)-38,val(g1,3)-38)
    pairs=sorted((q for q in FULL if q[0]>0 or q[0]==0 and q[1]>0))
    assert len(pairs)==10
    for k, expected in [(1,{1:10}),(2,{1:44,1024:1}),(3,{1:111,1024:6,4096:1,16384:1,67108864:1})]:
        counts=Counter()
        for omitted_pairs in combinations(pairs,k):
            removed={v for q in omitted_pairs for v in (q,(-q[0],-q[1]))}
            Q=sorted(q for q in FULL if q not in removed)
            E=evaluation(Q)
            H,d=lattice(E,square_witness(Q))
            assert d%d0==0
            ratio=d//d0
            counts[ratio]+=1
            if k==2 and ratio>1:
                assert set(omitted_pairs)=={(1,-1),(1,1)}
                relative=H0.inv()*H
                assert all(x.q==1 for x in relative)
                assert [v for v in smith(relative) if v!=1]==[2]*6+[4]*2
                assert rank_mod(E,2)==6 and rank_mod(E,3)==17
                assert val(gram_det(E),3)==43
        assert dict(counts)==expected,(k,counts)
        print('removed pairs',k,'remaining points',21-2*k,'index-ratio histogram',dict(sorted(counts.items())))
    print('PASS: exact ordinary jets, Hermite/Smith and rank checks, 175 antipodal configurations')

if __name__=='__main__':main()
