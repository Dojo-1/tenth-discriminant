#!/usr/bin/env python3
"""Phase388: fixed original-source 81x81 lower-jet unit minor.

D=403,p=3,rho=40,R=100,S=J=4. The row list is frozen; the
verifier does not select pivots adaptively to manufacture a minor.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase386"))
from source_jet_histogram import exact_ellipse_histogram, production_row_jet

D,P,R,S,J,RHO=403,3,100,4,4,40
ROWS=(
 *range(0,51),52,53,54,56,57,58,61,62,65,66,69,70,
 73,74,77,78,81,82,85,86,89,90,93,94,97,101,105,109,113,117
)
assert len(ROWS)==81 and len(set(ROWS))==81

def determinant_mod3(B):
    A=[[x%3 for x in row] for row in B]
    n=len(A);ans=1
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:return 0
        if k!=j:A[k],A[j]=A[j],A[k];ans=-ans
        z=A[j][j];ans=ans*z%3;inv=pow(z,-1,3)
        for i in range(j+1,n):
            c=A[i][j]*inv%3
            if c:A[i][j:]=[(x-c*y)%3 for x,y in zip(A[i][j:],A[j][j:])]
    return ans%3

def main():
    classes=sorted(exact_ellipse_histogram(D,RHO,9))
    assert len(classes)==27 and {y for x,y in classes}=={0,1,8}
    cols=[]
    for c,(x,y) in enumerate(classes):
        if y in (0,1):
            for j in range(3):
                cols.extend((c,j,k) for k in ((0,) if y==0 else (0,1)))
    assert len(cols)==81
    # Verify conjugation on ALL 400 original rows and j=0,1,2.
    for r in range(R):
        for s in range(S):
            for x in range(9):
                a=production_row_jet(D,P,r,s,S,J,(x,1),1)
                b=production_row_jet(D,P,r,s,S,J,(x,8),1)
                fixed=production_row_jet(D,P,r,s,S,J,(x,0),1)
                for j in range(3):
                    assert a[j][0]==b[j][0] and (a[j][1]+b[j][1])%3==0
                    assert fixed[j][1]==0
    # Nine fixed y=0 classes require one channel; nine conjugate pairs
    # require two. For 3 orders there are 3*(9+2*9)=81 independent
    # scalar coordinates, so the lower-jet rank is AT MOST 81.
    minor=[]
    for label in ROWS:
        r,s=divmod(label,S)
        jets={z:production_row_jet(D,P,r,s,S,J,z,1) for z in classes}
        minor.append([jets[classes[c]][j][k] for c,j,k in cols])
    assert determinant_mod3(minor)==1
    print("PASS conjugation upper bound 81 on all original source rows")
    print("PASS frozen 81x81 determinant is 1 modulo 3")
    print("CONCLUSION lower-jet rank=81; full rank90 remains separate")

if __name__=="__main__":main()
