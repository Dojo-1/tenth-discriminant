#!/usr/bin/env python3
"""Phase204 p^3 layers, preregistered before testing in Issues #136 and #137.

Original ordinary-Z integer-pair source. Hasse jets appear ONLY as quotients
of a forced factorial, not as replacements for the production derivative.
Integral Gamma_k are coefficients of Phase146's already-known T_a action.
"""
from math import factorial,comb
from ordinary_jet_filtration import mul as pairmul,powpair,jet
from source_translation_junction import mul as matmul,transpose,E,T
from truncated_smith_profiles import gram

def hjet(D,r,s,j,z):
    if j>r:return (0,0)
    x=pairmul(powpair(z,r-j,D),powpair((z[0],-z[1]),s,D),D)
    return comb(r,j)*x[0],comb(r,j)*x[1]

def hstep(D,R,S,j,Q):
    A=[[c for z in Q for c in hjet(D,r,s,j,z)]
       for r in range(R) for s in range(S)]
    weights=[2 if k%2==0 else 2*D for k in range(len(A[0]))]
    return [[sum(x*y*w for x,y,w in zip(a,b,weights)) for b in A] for a in A]

def grade(D,p,R,S,J,Q):
    A=gram(Q,D,R,S,J);B=gram(Q,D,R,S,p);n=R*S
    assert all((A[i][k]-B[i][k])%(p*p)==0 for i in range(n) for k in range(n))
    result=[[(A[i][k]-B[i][k])//(p*p)%p for k in range(n)] for i in range(n)]
    target=[[0]*n for _ in range(n)]
    for j in range(p,J):
        assert j<2*p and factorial(j)%p==0
        H=hstep(D,R,S,j,Q);factor=(factorial(j)//p)**2
        for i in range(n):
            for k in range(n):target[i][k]=(target[i][k]+factor*H[i][k])%p
    assert target==result
    return result

def gammat(R,S,t):
    return [[comb(r,u)*comb(s,v) if u<=r and v<=s and (r-u)+(s-v)==t else 0
             for u in range(R) for v in range(S)]
            for r in range(R) for s in range(S)]

def check_grade(D,p):
    R,S,J=p+2,2,p+2;Q=[(0,0),(1,0),(1,1)]
    H=grade(D,p,R,S,J,Q)
    assert H==grade(D,p,R,S,J,[(x+p,y) for x,y in Q])
    Gp=gram(Q,D,R,S,p);Gj=gram(Q,D,R,S,J)
    assert any((a-b)%(p**3)!=0 for x,y in zip(Gp,Gj) for a,b in zip(x,y))
    sharp=grade(D,p,R,S,J,[(0,0)])[p*S][p*S]
    assert sharp==2%p
    print("GRADE_P2",{"p":p,"D":D,"rows":R*S,
        "nonzero_entries":sum(bool(x) for row in H for x in row),
        "sharp_diagonal":sharp,"invariant_under_full_p_shift":True,
        "tail_not_zero_mod_p3":True})

def check_divided(D,p):
    R,S,J=p+2,3,p+2;a=p;mod=p**3;n=R*S;Q=[(0,0),(1,0),(1,1)]
    G0=gammat(R,S,0);G1=gammat(R,S,1);G2=gammat(R,S,2)
    assert matmul(G1,G1)==[[2*x for x in row] for row in G2]
    Ma=T(R,S,a)
    assert all((Ma[i][j]-G0[i][j]-a*G1[i][j]-a*a*G2[i][j])%mod==0
               for i in range(n) for j in range(n))
    Qshift=[(x+a,y) for x,y in Q]
    assert E(D,R,S,J,Qshift)==matmul(Ma,E(D,R,S,J,Q))
    A=gram(Q,D,R,S,J);B=gram(Qshift,D,R,S,J)
    assert B==matmul(matmul(Ma,A),transpose(Ma))
    assert G2[2*S][0]==1 and a*a%mod!=0
    assert (Ma[2*S][0]-G0[2*S][0]-a*G1[2*S][0])%mod==a*a%mod
    print("INTEGRAL_DIVIDED_POWER",{"p":p,"D":D,"modulus":mod,
        "rows":n,"quadratic_correction":a*a%mod,
        "nonunit_factorial_safe":True,"exact_original_gram":True})

if __name__=="__main__":
    for p,D in ((3,7),(5,3),(7,215)):check_grade(D,p)
    for p,D in ((2,3),(3,7),(5,3)):check_divided(D,p)
    print("PASS two graded source tests")
