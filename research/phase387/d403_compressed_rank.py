#!/usr/bin/env python3
"""Source-faithful D403/p3 full Frobenius-normalized residue evaluation rank.

Finite measurement only: exact original Q and all four ordinary Z jets,
W held fixed. Computes 400x216 class-compressed evaluation matrix mod3.
The source Phase386 factorization and a DIFFERENT direct integer jet oracle
must agree on selected original points. No determinant / new field bound.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase386"))
from source_jet_histogram import exact_ellipse_histogram,ellipse_points,production_row_jet,rank_mod
from direct_integer_oracle import normal_jet

D,P,R,S,J,RHO=403,3,100,4,4,40

def column_rank(A,selection=None):
    """Independent F3 column-basis elimination by earliest nonzero coordinate."""
    n=len(A);k=len(A[0])
    if selection is None:selection=range(k)
    basis={}
    for j in selection:
        v=[A[i][j]%P for i in range(n)]
        while True:
            pivot=next((i for i,x in enumerate(v) if x),None)
            if pivot is None:break
            if pivot not in basis:
                inv=pow(v[pivot],-1,P)
                basis[pivot]=[(x*inv)%P for x in v]
                break
            b=basis[pivot];c=v[pivot]
            v=[(x-c*y)%P for x,y in zip(v,b)]
    return len(basis)

def run():
    Q=list(ellipse_points(D,RHO))
    H=exact_ellipse_histogram(D,RHO,P*P)
    assert len(Q)==219 and len(H)==27
    classes=sorted(H)
    A=[[0]*(2*J*len(classes)) for _ in range(R*S)]
    for c,a in enumerate(classes):
        for r in range(R):
            for s in range(S):
                jets=production_row_jet(D,P,r,s,S,J,a,1)
                for j,(x,y) in enumerate(jets):
                    A[r*S+s][2*(J*c+j)]=x
                    A[r*S+s][2*(J*c+j)+1]=y
    assert rank_mod(A,P)==column_rank(A)==90
    # The paper eventual-row periodicity r -> r+24 after the saturated
    # threshold gives 37+34+31+28=130 original row labels (not 148).
    source_period_reduced=[A[r*S+s] for s in range(S)
        for r in range(P*(S-1-s)+J+P*(P*P-1))]
    assert len(source_period_reduced)==130
    assert rank_mod(source_period_reduced,P)==column_rank(source_period_reduced)==90
    for js,expected in (([0],27),([0,1],54),([0,1,2],81),([0,1,2,3],90)):
        ids=[2*(J*c+j)+t for c in range(len(classes)) for j in js for t in range(2)]
        assert column_rank(A,ids)==expected
    # Correct source j=0..3 is essential. The j=3-omitted alteration
    # incorrectly yields rank 81 instead of 90 (historic Phase280 kill).
    perm=[2*(J*c+j)+t for c in reversed(range(len(classes)))
          for j in range(J) for t in (1,0)]
    assert column_rank(A,perm)==90
    for a in (Q[0],Q[1],Q[36],Q[100],Q[150],Q[-1]):
        c=classes.index((a[0]%9,a[1]%9))
        for r in (0,1,2,3,9,33,50,99):
            for s in range(S):
                for j in range(J):
                    independent=normal_jet(D,P,S,r,s,j,a)
                    actual=tuple(A[r*S+s][2*(J*c+j)+t] for t in (0,1))
                    assert actual==tuple(x%P for x in independent)
    print("PASS original D403 p3, Q=219, class-compressed F=400x216, exact rank=90")
    print("PASS derivative rank profile 27,54,81,90; j3 omission negative control")
    print("PASS independent row and column ranks, integer oracle, class permutation")

if __name__=="__main__":run()
