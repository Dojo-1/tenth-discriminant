#!/usr/bin/env python3
"""Phase142 second instrument: 4 nonreal nodes exactly span 32 original jets.

D=19, R=8, S=J=4. All samples are from the ORIGINAL ellipse Q_5,
and their ordinary-Z derivatives keep W fixed, with the same paired
trace weights (2,2D). A four-sample support offers 4*2*J=32 integer
columns, equal to the 32 polynomial rows. This is an exact *finite*
witness, not a production rank theorem or an improved field cutoff.

Run: python3 research/ellipsoid_trimming/phase142_complex_minimal.py
"""
from __future__ import annotations
from itertools import combinations
from math import log, isqrt
from phase140_exact_trim import D,R,S,J,DIM,ORIGINAL,jets
from phase142_leverage import det_general,sum_gram

P=1_000_003
assert all(P%d for d in range(2,isqrt(P)+1)), "modular rank requires prime P"

def eval_matrix(points):
    out=[]
    for row in range(DIM):
        vals=[]
        for q in points:
            jv=jets(q)[row]
            for jj in range(J):
                vals.extend(jv[jj])
        out.append(vals)
    return out

def rank_modp(points):
    a=[[v%P for v in row] for row in eval_matrix(points)]
    n=len(a); m=len(a[0]); rr=0
    for col in range(m):
        if rr==n:break
        pivot=next((i for i in range(rr,n) if a[i][col]),None)
        if pivot is None:continue
        a[pivot],a[rr]=a[rr],a[pivot]
        inv=pow(a[rr][col],P-2,P)
        for j in range(col,m):
            a[rr][j]=a[rr][j]*inv%P
        for i in range(rr+1,n):
            if not a[i][col]:continue
            mul=a[i][col]
            for j in range(col,m):
                a[i][j]=(a[i][j]-mul*a[rr][j])%P
        rr+=1
    return rr

def main():
    points=sorted(q for q in ORIGINAL if q[1]!=0)
    assert len(points)==10 and len(ORIGINAL)==21
    assert all(y in (-1,1) for _,y in points)
    histogram={}
    for qs in combinations(points,4):
        rank=rank_modp(qs)
        histogram[rank]=histogram.get(rank,0)+1
        # Every unique real abscissa contributes two complex-conjugate
        # embeddings and 2*J independent ordinary-jet columns in this
        # FROZEN model. At a repeated abscissa, the conjugate rows are
        # copies: extra samples do not increase rank.
        expected=2*J*len({x for x,y in qs})
        assert rank==expected,(qs,rank,expected)
    assert histogram=={16:10,24:120,32:80},histogram

    witness=[(-2,-1),(-1,-1),(0,-1),(1,-1)]
    M=eval_matrix(witness)
    assert len(M)==DIM and all(len(row)==DIM for row in M)
    dE=det_general(M)
    assert dE!=0 and dE%P!=0
    detB=(4*D)**(len(witness)*J)
    G=sum_gram(witness)
    dG=det_general(G)
    assert dG==detB*dE*dE
    assert dG>0 and dG%(3**38)==0
    assert len(witness)*2*J==DIM
    assert not 2*(R-1)+(S-1)<len(witness)
    assert max(x*x+D*y*y for x,y in witness)==23

    conjugate=[(-2,-1),(-2,1),(-1,-1),(0,-1)]
    assert rank_modp(conjugate)==24
    three=[(-2,-1),(-1,-1),(0,-1)]
    assert rank_modp(three)==24
    assert len(three)*2*J<DIM
    # Geometric efficiency in node COUNT does not force radius or
    # Hadamard improvement; compare the 8-real-node witness on x=+/-1..4.
    real8=[(x,0) for x in (-4,-3,-2,-1,1,2,3,4)]
    real_G=sum_gram(real8)
    real_det=det_general(real_G)
    assert real_det>0
    assert dG>real_det # these four complex nodes have larger Gram volume
    print(f"Four nonreal nodes {witness}: det(E)={dE}")
    print(f"det(G)=(4D)^16*det(E)^2; logdet={log(dG):.9f}")
    print(f"8 real-axis nodes logdet={log(real_det):.9f}")
    print("All C(10,4)=210 nonreal sample sets, modular ranks:",histogram)
    print("3-node channel-count and conjugate-duplicate controls passed.")
    print("At original D=19 only: four nodes achieve rank32, "
          "with no new production theorem or cutoff.")

if __name__=="__main__":
    main()
