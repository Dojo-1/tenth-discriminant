#!/usr/bin/env python3
"""Phase388: exact original-source fourth-jet/Bockstein subspace certificate.

D=403, p=3, rho=40, R=100, S=J=4, original W-held ordinary jets.
Two independent implementations check ALL 219 original ellipse points.
No new p-adic valuation, class number theorem, or human proof review.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase386"))
from source_jet_histogram import (
    exact_ellipse_histogram, ellipse_points, production_row_jet, pair_pow, rank_mod)
from direct_integer_oracle import normal_jet

D,P,R,S,J,RHO=403,3,100,4,4,40

# Source row labels (r,s, coefficient mod3), not abstract auxiliary forms.
# Frozen sparse witnesses: each has 4 or 6 original normalized rows.
WITNESSES=(
 ((3,0,1),(9,0,2),(21,2,2),(33,0,1)),
 ((2,3,1),(3,0,2),(6,3,2),(9,0,1),(10,3,2),(12,3,1)),
 ((3,3,1),(4,0,2),(7,3,2),(10,0,1),(11,3,2),(13,3,1)),
 ((0,3,2),(2,1,1),(4,3,2),(6,3,1),(15,2,2),(27,0,1)),
 ((0,2,1),(1,3,2),(5,3,2),(7,3,1),(16,2,2),(28,0,1)),
 ((1,2,1),(2,3,2),(6,3,2),(8,3,1),(17,2,2),(29,0,1)),
 ((2,2,1),(3,3,2),(7,3,2),(9,3,1),(18,2,2),(30,0,1)),
 ((0,3,1),(4,3,2),(8,3,2),(10,3,1),(19,2,2),(31,0,1)),
 ((1,3,1),(5,3,2),(9,3,2),(11,3,1),(20,2,2),(32,0,1)),
)

def witness_jets(d,z,i,direct=False):
    out=[[0,0] for j in range(J)]
    for r,s,c in WITNESSES[i]:
        jets=([normal_jet(d,P,S,r,s,j,z) for j in range(J)]
              if direct else production_row_jet(d,P,r,s,S,J,z,1))
        for j in range(J):
            for k in (0,1):
                out[j][k]=(out[j][k]+c*jets[j][k])%P
    return [tuple(v) for v in out]

def bockstein_fourth(d,z,i):
    # Same space as Phase284: B_a(z)=2*z^a, 0<=a<=8.
    # Our concrete basis is 2*(1-z^8), 1,z,...,z^7.
    if i==0:
        z8=pair_pow(z,8,d,3)
        return ((2*(1-z8[0]))%3,(-2*z8[1])%3)
    return pair_pow(z,i-1,d,3)

def row_rank(A):
    """Independent column-pivot modular row reducer, not rank_mod."""
    piv={}
    for row in A:
        v=[x%3 for x in row]
        while True:
            j=next((i for i,x in enumerate(v) if x),None)
            if j is None: break
            if j not in piv:
                u=pow(v[j],-1,3)
                piv[j]=[x*u%3 for x in v]
                break
            c=v[j]; b=piv[j]
            v=[(x-c*y)%3 for x,y in zip(v,b)]
    return len(piv)

def source_matrix(classes):
    A=[]
    for r in range(R):
        for s in range(S):
            row=[]
            for z in classes:
                for x,y in production_row_jet(D,P,r,s,S,J,z,1):
                    row.extend((x,y))
            A.append(row)
    return A

def main():
    Q=list(ellipse_points(D,RHO))
    hist=exact_ellipse_histogram(D,RHO,9)
    classes=sorted(hist)
    assert len(Q)==219 and len(classes)==27
    assert {y for x,y in classes}=={0,1,8}
    assert len({(x%3,y%3) for x,y in classes})==9

    for z in Q:
        for i in range(9):
            factored=witness_jets(D,z,i)
            exact=witness_jets(D,z,i,direct=True)
            assert factored==exact,("source oracle",z,i)
            assert exact[:3]==[(0,0)]*3,("lower jet failure",z,i)
            assert exact[3]==bockstein_fourth(D,z,i),("fourth jet",z,i)

    A=source_matrix(classes)
    low=[2*(J*c+j)+k for c in range(27) for j in range(3) for k in (0,1)]
    high=[2*(J*c+3)+k for c in range(27) for k in (0,1)]
    lower=[[row[t] for t in low] for row in A]
    assert rank_mod(lower,3)==row_rank(lower)==81
    assert rank_mod(A,3)==row_rank(A)==90

    K=[]
    for i in range(9):
        row=[]
        for z in classes:
            assert witness_jets(D,z,i)[:3]==[(0,0)]*3
            row.extend(witness_jets(D,z,i)[3])
        K.append(row)
    assert rank_mod(K,3)==row_rank(K)==9
    assert rank_mod(A,3)-rank_mod(lower,3)==9

    phase284=[]
    for a in range(9):
        row=[]
        for z in classes:
            row.extend(tuple(2*x%3 for x in pair_pow(z,a,D,3)))
        phase284.append(row)
    assert rank_mod(phase284,3)==9
    assert rank_mod(K+phase284,3)==9

    original284=[A[(a%3+3)*S+a//3] for a in range(9)]
    assert rank_mod([[row[t] for t in low] for row in original284],3)==9
    assert [[row[t] for t in high] for row in original284]==phase284
    omitted={(a%3+3)*S+a//3 for a in range(9)}
    assert rank_mod([row for k,row in enumerate(A) if k not in omitted],3)==89

    # Crucial kill conditions: neither an arbitrary y mod9 nor merely
    # D mod3 suffices. The identities require the exact frozen source.
    assert witness_jets(D,(0,2),1)[:3] != [(0,0)]*3
    for d in (19,283):
        assert d%3==D%3 and d%9!=D%9
        assert witness_jets(d,(0,1),1)[:3] != [(0,0)]*3
    assert normal_jet(D,3,S,3,0,3,(0,0))==(2,0)
    print("PASS 219 original points x 9 sparse combinations x 4 ordinary jets")
    print("PASS lower rank81, total90, kernel fourth-jet image rank9")
    print("PASS equality with Phase284 span B_a(z)=2*z^a, a=0..8")
    print("PASS direct integer vs factored polynomial oracles; negative controls")
    print("CAUTION: original nine Phase284 rows are NOT lower-jet-null")
    print("CAUTION: no additional determinant valuation and no universal D/y claim")

if __name__=="__main__":main()
