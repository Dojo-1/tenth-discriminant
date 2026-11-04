#!/usr/bin/env python3
"""Phase204 junction prereg #136/#137: Phase146 integral translation and p² jets.

These are SOURCE-typed matrix identities, not improved determinant lower bounds.
The exact global translation action predates Phase204 (Phase146, 31 Oct 2026).
"""
from math import comb
from ordinary_jet_filtration import jet
from truncated_smith_profiles import gram, profile

def mul(A,B):
    bt=list(zip(*B))
    return [[sum(x*y for x,y in zip(a,b)) for b in bt] for a in A]
def transpose(A):return [list(row) for row in zip(*A)]
def T(R,S,d):
    return [[comb(r,u)*comb(s,v)*d**(r+s-u-v) if u<=r and v<=s else 0
             for u in range(R) for v in range(S)]
            for r in range(R) for s in range(S)]
def N(R,S):
    return [[r if u==r-1 and v==s else s if u==r and v==s-1 else 0
             for u in range(R) for v in range(S)]
            for r in range(R) for s in range(S)]
def E(D,R,S,J,Q):
    return [[c for j in range(J) for z in Q for c in jet(D,r,s,j,z)]
            for r in range(R) for s in range(S)]
def check(D,p,R,S,J):
    Q=[(0,0),(1,0),(1,1)];m=p*p;n=R*S
    ev=E(D,R,S,J,Q);G=gram(Q,D,R,S,J);Gp=gram(Q,D,R,S,p)
    Id=[[int(i==j) for j in range(n)] for i in range(n)]
    assert all((a-b)%m==0 for u,v in zip(G,Gp) for a,b in zip(u,v))
    A=N(R,S)
    for delta in (p,2*p):
        Qshift=[(x+delta,y) for x,y in Q]
        M=T(R,S,delta)
        assert mul(M,ev)==E(D,R,S,J,Qshift)
        assert mul(M,T(R,S,-delta))==Id
        assert all((M[i][j]-Id[i][j]-delta*A[i][j])%m==0
                   for i in range(n) for j in range(n))
        GS=gram(Qshift,D,R,S,J)
        assert GS==mul(mul(M,G),transpose(M))
        L=mul(A,Gp);Rt=mul(Gp,transpose(A))
        assert all((GS[i][j]-Gp[i][j]-delta*(L[i][j]+Rt[i][j]))%m==0
                   for i in range(n) for j in range(n))
        assert profile(GS,p)==profile(Gp,p)
        assert gram([(delta,0)]+Q[1:],D,R,S,J)!=GS
    for z in Q:
        for r in range(1,R):
            for s in range(S):
                for j in range(p):
                    x=jet(D,r,s,j+1,z)
                    y=jet(D,r-1,s,j,z)
                    assert x==(r*y[0],r*y[1])
    # Wrong assumption that W is fixed BETWEEN MOVING POINTS.
    assert jet(D,0,1,0,(p,0))==(p,0)
    assert jet(D,0,1,0,(0,0))==(0,0)
    print("SOURCE_JUNCTION",{"p":p,"D":D,"rows":n,
        "shifts":[p,2*p],"smith_profile_p2":profile(Gp,p),
        "exact_integer_row_congruence":True,"mod_p2_first_variation":True,
        "single_point_countercontrol":True,"W_shift_required":True})
if __name__=="__main__":
    check(7,3,5,2,5)
    check(3,5,7,2,7)
    check(215,7,9,3,9)
    print("PASS Phase146/204 source transport junction")
