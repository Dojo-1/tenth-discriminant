#!/usr/bin/env python3
"""Round201 exact post-preregistration pilots T0-T3.

No numerical floats, torch, sympy or surrogate field construction.
Protocol: research/loss_ledger/PREREGISTRATION_2026-11-04.md
Prereq frozen commit: 727381f7e9c42624d98c955e68e564e7891ef862
"""
from __future__ import annotations

from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import json
import sys


def det(a):
    n=len(a)
    if n==0:
        return 1
    # Exact Leibniz expansion; n=2,3 only in these tests.
    result=0
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=1
        for i,j in enumerate(perm):
            term*=a[i][j]
        result+=(-1 if inversions%2 else 1)*term
    return result


def vp(x,p):
    if x==0:
        return None  # infinity
    assert p>1
    x=abs(x)
    k=0
    while x%p==0:
        x//=p
        k+=1
    return k


def tropical_det(a,p):
    vals=[]
    for perm in permutations(range(len(a))):
        term=0
        for i,j in enumerate(perm):
            t=vp(a[i][j],p)
            if t is None:
                term=None
                break
            term+=t
        if term is not None:
            vals.append(term)
    return min(vals) if vals else None


def transpose(a):
    return [list(row) for row in zip(*a)]


def mmul(a,b):
    bt=transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def delta(a,k):
    n=len(a)
    g=0
    for I in combinations(range(n),k):
        for J in combinations(range(n),k):
            g=gcd(g,abs(det([[a[i][j] for j in J] for i in I])))
    return g


def rank_mod(a,p):
    """Exact modular Gaussian elimination over F_p."""
    rows=[list(map(lambda x:x%p,row)) for row in a]
    m=len(rows)
    n=len(rows[0]) if rows else 0
    r=0
    for col in range(n):
        pivot=next((i for i in range(r,m) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=pow(rows[r][col],-1,p)
        rows[r]=[(x*inv)%p for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][col]:
                t=rows[i][col]
                rows[i]=[(x-t*y)%p for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==m:
            break
    return r


def kernel_cardinality_by_enumeration(a,p,m):
    """Independent brute-force count, intended only for 3x3 and m<=3."""
    mod=p**m
    return sum(all(sum(a[i][j]*x[j] for j in range(len(x)))%mod==0
                   for i in range(len(x)))
               for x in product(range(mod),repeat=len(a)))


def test_T0():
    a=[[1,1],[1,4]]
    b=[[1,1],[1,10]]
    assert det(a)==3 and det(b)==9
    assert vp(det(a),3)==1 and vp(det(b),3)==2
    assert [[vp(x,3) for x in row] for row in a]==[[0,0],[0,0]]
    assert [[vp(x,3) for x in row] for row in b]==[[0,0],[0,0]]
    ta,tb=tropical_det(a,3),tropical_det(b,3)
    assert (ta,tb)==(0,0)
    assert (vp(det(a),3)-ta,vp(det(b),3)-tb)==(1,2)
    return {"det": [3,9], "entry_valuations": [[0,0],[0,0]],
            "tropical_det": [ta,tb], "cancellation_defects":[1,2]}


def test_T1():
    c=[[1,0,0],[0,3,0],[0,0,27]]
    e=[[1,0,0],[0,9,0],[0,0,9]]
    assert det(c)==det(e)==81 and rank_mod(c,3)==rank_mod(e,3)==1
    dc=[delta(c,k) for k in range(1,4)]
    de=[delta(e,k) for k in range(1,4)]
    assert dc==[1,3,81] and de==[1,9,81]
    observed_c=[kernel_cardinality_by_enumeration(c,3,m) for m in range(1,4)]
    observed_e=[kernel_cardinality_by_enumeration(e,3,m) for m in range(1,4)]
    assert observed_c==[9,27,81] and observed_e==[9,81,81]
    assert observed_c==[3**sum(min(x,m) for x in [0,1,3]) for m in range(1,4)]
    assert observed_e==[3**sum(min(x,m) for x in [0,2,2]) for m in range(1,4)]
    return {"det":81,"rank_mod_3":1,"determinantal_divisors":[dc,de],
            "kernel_sizes_mod_3_m":[observed_c,observed_e]}


def test_T2():
    a=[[1,1],[1,4]]
    u=[[1,-1],[0,1]]
    g=mmul(mmul(u,a),transpose(u))
    assert det(u)==1 and g==[[3,-3],[-3,4]]
    assert det(g)==det(a)==3
    assert [delta(g,k) for k in (1,2)]==[delta(a,k) for k in (1,2)]==[1,3]
    assert (vp(det(a),3)-tropical_det(a,3))==1
    assert (vp(det(g),3)-tropical_det(g,3))==0
    return {"integral_frame":u,"transformed_gram":g,
            "determinantal_divisors":[1,3],"defect_before_after":[1,0]}


def test_T3():
    source=Path(__file__).resolve().parents[1]/"plural_moving_frames"
    sys.path.insert(0,str(source))
    from original_source_small_pilot import D,R,S,J,ellipse,gram,determinant
    assert (D,R,S,J)==(19,4,3,3)
    ranks=[]
    for rho,expected_count in ((5,21),(6,31)):
        points=ellipse(rho)
        assert len(points)==expected_count
        g=gram(points)
        assert len(g)==12 and determinant(g)>0
        rank=rank_mod(g,3)
        assert rank <= R+3*(S-1)==10
        ranks.append(rank)
    assert ranks[0]==10, ("rho=5 rank",ranks[0])
    assert ranks[1]<=9, ("rho=6 rank",ranks[1])
    return {"D":D,"p":3,"R":R,"S":S,"J":J,"radii":[5,6],
            "ranks_mod_3":ranks,"upper":10,"real_Gram_determinants_positive":True}


if __name__=="__main__":
    results={"T0":test_T0(),"T1":test_T1(),"T2":test_T2(),"T3":test_T3()}
    print(json.dumps(results,indent=2,sort_keys=True))
    print("ROUND201_EXACT_PILOTS_PASS (finite only, no new discriminant bound)")
