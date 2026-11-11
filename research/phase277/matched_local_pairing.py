#!/usr/bin/env python3
"""Phase277: source-faithful matched inert/split local pairing, finite only.

Original D=283, rho=31, R=70,S=J=2. Entire ellipse and all j<2 are used.
The field need NOT have class number one. At p=3,5 (inert) use exactly
the already-counted unimodular old Frobenius row and divide it once.
At p=7 (split) do NOT invoke the inert Frobenius row identity.

C0 is NOT p-saturated: its rank is smaller than 140 at all primes.
The radical dim(rank(C0)-rank(C0 B C0^T)) is a genuine invariant of the
UNSATURATED row image, but NOT a new primitive Smith factor/field bound.

Reproduces a recorded exploratory run; it is post-hoc regression,
not an independently preregistered discovery.
"""
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase204"))
from ordinary_jet_filtration import jet as independent_ordinary_jet

D,R,S,J,RHO = 283,70,2,2,31
Q = [(x,y) for y in range(-RHO,RHO+1) for x in range(-RHO,RHO+1)
     if x*x+D*y*y <= RHO*RHO]
assert len(Q)==169
N=R*S
ROWS=[(r,s) for r in range(R) for s in range(S)]

def pairmul(a,b,mod):
    return ((a[0]*b[0]-D*a[1]*b[1])%mod,
            (a[0]*b[1]+a[1]*b[0])%mod)

def pairpow(z,n,mod):
    assert n>=0
    out=(1,0)
    while n:
        if n&1:out=pairmul(out,z,mod)
        z=pairmul(z,z,mod)
        n//=2
    return out

def normalized_source(p,inert):
    rows=[]
    old_budget=0
    for r,s in ROWS:
        # With S=2, k is 0 or 1. Inertness is a REQUIRED guard.
        k=min(r//p,S-1-s) if inert else 0
        old_budget+=k
        mod=p**(k+1)
        row=[]
        for j in range(J):
            for x,y in Q:
                z=(x%mod,y%mod)
                w=(x%mod,(-y)%mod)
                def source_term(a,b):
                    if a<j:return (0,0)
                    v=pairmul(pairpow(z,a-j,mod),pairpow(w,b,mod),mod)
                    fall=a if j==1 else 1
                    return ((fall*v[0])%mod,(fall*v[1])%mod)
                v=source_term(r,s)
                if k:
                    sub=source_term(r-p,s+1)
                    v=((v[0]-sub[0])%mod,(v[1]-sub[1])%mod)
                    assert v[0]%p==0 and v[1]%p==0, (p,r,s,j,x,y)
                    v=(v[0]//p,v[1]//p)
                row.extend([v[0]%p,v[1]%p])
        rows.append(row)
    return np.array(rows,dtype=np.int64),old_budget

def rank_numpy(M,p):
    A=M.copy()%p
    n,m=A.shape
    k=0
    for j in range(m):
        if k==n:break
        nz=np.flatnonzero(A[k:,j])
        if not len(nz):continue
        i=k+int(nz[0])
        A[[k,i]]=A[[i,k]]
        A[k,j:]=A[k,j:]*pow(int(A[k,j]),-1,p)%p
        idx=np.flatnonzero(A[k+1:,j])+k+1
        if len(idx):
            A[idx,j:]=(A[idx,j:]-A[idx,j,None]*A[k,j:])%p
        k+=1
    return k

def rank_scalar(M,p):
    """Independent scalar row elimination (only for 140x140 Gram)."""
    A=[list(map(lambda t:int(t)%p,row)) for row in M]
    n=len(A);m=len(A[0]);k=0
    for j in range(m):
        pivot=next((i for i in range(k,n) if A[i][j]),None)
        if pivot is None:continue
        A[k],A[pivot]=A[pivot],A[k]
        inv=pow(A[k][j],-1,p)
        A[k][j:]=[(t*inv)%p for t in A[k][j:]]
        for i in range(k+1,n):
            mult=A[i][j]
            if mult:
                A[i][j:]=[(u-mult*v)%p for u,v in zip(A[i][j:],A[k][j:])]
        k+=1
        if k==n:break
    return k

def check_alternate_source(C,p,inert):
    """Compare selected rows/columns to independently imported integer jets."""
    for r,s in ((0,0),(p,0),(p+1,0),(69,0),(69,1)):
        k=min(r//p,S-1-s) if inert else 0
        i=r*S+s
        for j in range(J):
            for zi in (0,len(Q)//2,len(Q)-1):
                z=Q[zi]
                v=independent_ordinary_jet(D,r,s,j,z)
                if k:
                    q=independent_ordinary_jet(D,r-p,s+1,j,z)
                    v=(v[0]-q[0],v[1]-q[1])
                    assert all(t%p==0 for t in v)
                    v=(v[0]//p,v[1]//p)
                start=2*(j*len(Q)+zi)
                assert tuple(map(int,C[i,start:start+2])) == (v[0]%p,v[1]%p)

def main():
    assert N==140 and len(Q)*J*2==676
    results=[]
    # Split case is a genuine negative: its local source is the same D,
    # but Frobenius quotient is NOT justified for p=7.
    cases={3:{"character":-1,"budget":67,"rank":36,"gram":10,"j0":18,"flat":10},
           5:{"character":-1,"budget":65,"rank":60,"gram":32,"j0":30,"flat":32},
           7:{"character": 1,"budget":0,"rank":28,"gram":28,"j0":14,"flat":26}}
    for p,expected in cases.items():
        sq={(x*x)%p for x in range(p)}
        chi=1 if ((-D)%p) in sq else -1
        assert chi==expected["character"] and (-D)%p!=0
        inert=(chi==-1)
        C,budget=normalized_source(p,inert)
        check_alternate_source(C,p,inert)
        assert C.shape==(140,676)
        original_B=np.tile(np.array([2,2*D],dtype=np.int64),len(Q)*J)%p
        G=((C*original_B)@C.T)%p
        rankC=rank_numpy(C,p)
        rankG=rank_numpy(G,p)
        assert rankG==rank_scalar(G,p)
        assert rankG<=rankC
        assert rank_numpy(C[:,:2*len(Q)],p)==expected["j0"]
        # Null metric is NOT the original source. It must not be silently used.
        flat_B=np.tile(np.array([2,2],dtype=np.int64),len(Q)*J)%p
        flatG=((C*flat_B)@C.T)%p
        assert rank_numpy(flatG,p)==expected["flat"]
        if p==7:assert rank_numpy(flatG,p)!=rankG
        # Metamorphic independent of channel and row order.
        Cp=C[:,::-1]
        Bp=original_B[::-1]
        assert np.array_equal((Cp*Bp)@Cp.T%p,G)
        Cs=C.copy()
        Cs[0]=(Cs[0]+Cs[1])%p
        assert rank_numpy(Cs,p)==rankC
        assert rank_numpy(((Cs*original_B)@Cs.T)%p,p)==rankG
        observed={"p":p,"character":chi,"budget":budget,"rank":rankC,
                  "gram":rankG,"j0":expected["j0"],"flat":expected["flat"]}
        assert all(observed[x]==expected[x] for x in expected),observed
        results.append((p,rankC-rankG,140-rankC))
        print("MATCHED_SOURCE",observed,
              "image_pairing_radical",rankC-rankG,
              "evaluation_defect",140-rankC,flush=True)
    assert results==[(3,26,104),(5,28,80),(7,0,112)]
    print("PASS Phase277 exact original-source inert/split panel")

if __name__=="__main__":
    main()
