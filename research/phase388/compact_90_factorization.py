#!/usr/bin/env python3
"""Phase388: exact rank-90 source matrix factorization, no rank black box.

Select 81 lower-jet scalar coordinates by conjugation and 9 fourth-jet
coordinates, one conjugation-compatible F9 representative each.
Check a FROZEN 90x90 unit minor and reconstruct all 400x216 entries.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase386"))
from source_jet_histogram import exact_ellipse_histogram,production_row_jet

D,P,R,S,J,RHO=403,3,100,4,4,40
PIVOT_ROWS=(*range(72),73,74,77,78,81,82,85,86,89,90,93,94,97,101,105,109,113,117)
assert len(PIVOT_ROWS)==90 and len(set(PIVOT_ROWS))==90

def original_and_selected_columns():
    classes=sorted(exact_ellipse_histogram(D,RHO,9))
    idx={z:c for c,z in enumerate(classes)}
    cols=[]
    for c,(x,y) in enumerate(classes):
        if y in (0,1):
            for j in range(3):
                cols.extend(2*(J*c+j)+t for t in ((0,) if y==0 else (0,1)))
    assert len(cols)==81
    for x in range(3):
        cols.append(2*(J*idx[(x,0)]+3))
        cols.extend(2*(J*idx[(x,1)]+3)+t for t in (0,1))
    assert len(cols)==90 and len(set(cols))==90
    A=[]
    for r in range(R):
        for s in range(S):
            row=[]
            for z in classes:
                for x,y in production_row_jet(D,P,r,s,S,J,z,1):
                    row.extend((x,y))
            A.append(row)
    return A,cols

def inverse_mod3(A):
    n=len(A)
    T=[[x%3 for x in row]+[int(i==j) for j in range(n)]
       for i,row in enumerate(A)]
    determinant=1
    for j in range(n):
        k=next((i for i in range(j,n) if T[i][j]),None)
        assert k is not None,("singular frozen source minor",j)
        if k!=j:T[k],T[j]=T[j],T[k];determinant=-determinant
        z=T[j][j]%3;determinant=determinant*z%3
        inv=pow(z,-1,3);T[j]=[x*inv%3 for x in T[j]]
        for i in range(n):
            if i!=j and T[i][j]:
                f=T[i][j]
                T[i]=[(x-f*y)%3 for x,y in zip(T[i],T[j])]
    return [row[n:] for row in T],determinant%3

def main():
    A,selected=original_and_selected_columns()
    M=[[A[i][j] for j in selected] for i in PIVOT_ROWS]
    inverse,det=inverse_mod3(M)
    assert det==2
    supports=[]
    for target in range(len(A[0])):
        v=[A[i][target] for i in PIVOT_ROWS]
        alpha=[sum(inverse[k][i]*v[i] for i in range(90))%3
               for k in range(90)]
        supports.append(sum(x!=0 for x in alpha))
        assert all(sum(A[i][selected[k]]*alpha[k] for k in range(90))%3
                   ==A[i][target] for i in range(400)),target
    assert max(supports)<=4
    print("PASS frozen original-source 90x90 determinant=2 mod3")
    print("PASS exact factorization A400x216 = 90 geometric columns x coefficient matrix")
    print("PASS every source channel uses at most four basis columns")
    print("CONCLUSION full source rank exactly90; no new p-adic valuation claimed")

if __name__=="__main__":main()
