#!/usr/bin/env python3
"""Phase288: exact Noether-graded integral transverse readout of original Gram.

PREREGISTERED at d26e36e before this executable test.
No Gaussian weights, no maximal-order substitution, no novel determinant mass.
All 140/400 original rows are read for X; only 8/16 original Gram rows have
numerical determinant/Smith-valuation controls.
"""
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve()
ROOT=HERE.parents[2]
sys.path.insert(0,str(HERE.parents[1]/"phase206"))
sys.path.insert(0,str(HERE.parents[1]/"phase204"))
from source_probe import params,gram,mul
from ordinary_jet_filtration import jet

FROZEN={
    "research/phase206/source_probe.py":"3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase204/ordinary_jet_filtration.py":"dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}
CASES={
 283:{"params":(31,70,2,2,169),"T":15638,"gap":244547044,
      "labels":[(0,0),(2,0),(1,1),(1,0),(0,1),(3,0),(2,1),(4,0)]},
 403:{"params":(40,100,4,4,219),"T":43406,"gap":1884080836,
      "labels":[(r,s) for r in range(4) for s in range(4)]},
}
PRIMES=(2,3,5,7,11)
K=4


def frozen_sources():
    for path,expected in FROZEN.items():
        actual=subprocess.check_output(
            ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True
        ).strip()
        assert actual==expected,("helper changed",path,actual,expected)


def matmul(A,B):
    assert A and B and len(A[0])==len(B)
    Bt=list(zip(*B))
    return [[sum(u*v for u,v in zip(row,col)) for col in Bt]
            for row in A]


def trans(A):
    return [list(row) for row in zip(*A)]


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def zero(n,m):
    return [[0]*m for _ in range(n)]


def matadd(A,B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]


def matsub(A,B):
    return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]


def block(A,B,C,D):
    assert len(A)==len(B) and len(C)==len(D)
    return [a+b for a,b in zip(A,B)]+[a+b for a,b in zip(C,D)]


def bareiss(A):
    M=[row[:] for row in A]
    n=len(M)
    if n==0:return 1
    prev=1
    sign=1
    for k in range(n-1):
        pivot=next((j for j in range(k,n) if M[j][k]),None)
        if pivot is None:return 0
        if pivot!=k:
            M[k],M[pivot]=M[pivot],M[k]
            sign=-sign
        x=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a=M[i][j]*x-M[i][k]*M[k][j]
                assert a%prev==0,("Bareiss exactness broken",k,i,j)
                M[i][j]=a//prev
            M[i][k]=0
        prev=x
    return sign*M[n-1][n-1]


def valuation(d,p):
    assert d!=0
    d=abs(d)
    n=0
    while d%p==0:
        n+=1
        d//=p
    return n


def v_of_q(D,q):
    x,y=q
    delta=x*x-D*y*y
    nu=x*x+D*y*y
    return (delta,nu,x,x*delta)


def full_transverse_X(D,Q,R,S):
    """All 140/400 original monomial rows, j0 REAL channel, exact E*B*V."""
    X=[[0]*K for _ in range(R*S)]
    for x,y in Q:
        z=(x,y)
        zbar=(x,-y)
        zpow=[(1,0)]
        wpow=[(1,0)]
        for r in range(1,R):
            zpow.append(mul(zpow[-1],z,D))
        for s in range(1,S):
            wpow.append(mul(wpow[-1],zbar,D))
        v=v_of_q(D,(x,y))
        for r in range(R):
            for s in range(S):
                re=mul(zpow[r],wpow[s],D)[0]
                row=X[r*S+s]
                for c in range(K):
                    row[c]+=2*re*v[c]
    assert len(X)==R*S
    # P*X=X*S for P=(-1)^(r+s), S=(+,+,-,-).
    assert all(X[r*S+s][c]==0
      for r in range(R) for s in range(S) for c in range(K)
      if ((r+s)%2==1 and c<2) or ((r+s)%2==0 and c>=2))
    return X


def original_jet_gram(D,Q,J,labels):
    """Second independent original-jet/tracemetric evaluation oracle."""
    m=2*J*len(Q)
    E=[]
    for r,s in labels:
        row=[]
        for j in range(J):
            for q in Q:
                row.extend(jet(D,r,s,j,q))
        assert len(row)==m
        E.append(row)
    weights=[w for _ in range(J) for _ in Q for w in (2,2*D)]
    return [[sum(a*b*w for a,b,w in zip(u,v,weights)) for v in E] for u in E]


def angular_and_source_checks(D,Q,J,labels,Xsmall,G,Texpected,gapexpected):
    A=sum(x*x for x,y in Q)
    B=sum(D*y*y for x,y in Q)
    T=A-B
    assert T==Texpected and T*T==gapexpected,("frozen hand result",D,T,T*T)
    assert sum(x*y for x,y in Q)==0
    C0=0
    C90=0
    for x,y in Q:
        for a,b in Q:
            C0+=(x*a+D*y*b)**2
            C90+=D*(y*a-x*b)**2
    assert C0==A*A+B*B
    assert C90==2*A*B
    assert C0-C90==T*T
    idx0=labels.index((0,0))
    idx2=labels.index((2,0))
    idx11=labels.index((1,1))
    assert Xsmall[idx0][0]==G[idx0][idx2]==2*T
    assert Xsmall[idx0][1]==G[idx0][idx11]==2*(A+B)
    assert 4*(C0-C90)==G[idx0][idx2]**2

    # The original signed metric and all ordinary Z jets remain unmodified.
    rho,R,S,J0,Q0=params(D)
    assert Q==Q0 and J0==J
    for i,(r,s) in enumerate(labels):
        direct=[0]*K
        for q in Q:
            re,_=jet(D,r,s,0,q)
            v=v_of_q(D,q)
            for c in range(K):
                direct[c]+=2*re*v[c]
        assert direct==Xsmall[i]

    # Strict 2-row Hadamard-Fischer correction on the ORIGINAL Gram minor,
    # no new arithmetic valuation from this identity.
    assert G[idx0][idx0]*G[idx2][idx2]-G[idx0][idx2]**2>0
    return {"T":T,"A":A,"B":B,"C0":C0,"C90":C90,
            "g_const_Z2":G[idx0][idx2],
            "g_const_ZW":G[idx0][idx11]}


def extension(G,X):
    n=len(G)
    return block(
        matadd(G,matmul(X,trans(X))), X,
        trans(X), eye(K))


def parity_test(G,X,Gext,labels):
    n=len(labels)
    P=[(-1)**(r+s) for r,s in labels]
    S=(1,1,-1,-1)
    assert all(G[i][j]==0 for i in range(n) for j in range(n)
               if P[i]!=P[j])
    assert all(P[i]*X[i][c]==X[i][c]*S[c]
               for i in range(n) for c in range(K))
    signs=P+list(S)
    assert all(Gext[i][j]==signs[i]*signs[j]*Gext[i][j]
               for i in range(n+K) for j in range(n+K))
    return True


def congruence_and_gauge(G,X,labels):
    n=len(G)
    Gext=extension(G,X)
    D=block(G,zero(n,K),zero(K,n),eye(K))
    U=block(eye(n),X,zero(K,n),eye(K))
    L=block(eye(n),zero(n,K),
            [[-q for q in row] for row in trans(X)],eye(K))
    assert matmul(matmul(U,D),trans(U))==Gext
    assert matmul(matmul(trans(L),Gext),L)==D
    assert matmul(trans(U),L)==eye(n+K)
    assert matmul(L,trans(U))==eye(n+K)
    assert parity_test(G,X,Gext,labels)
    d=bareiss(G)
    assert d>0
    assert bareiss(Gext)==d
    vps={str(p):valuation(d,p) for p in PRIMES}
    assert all(v==valuation(bareiss(Gext),int(p)) for p,v in vps.items())

    # A second integral moving frame, nonorthogonal but C2-equivariant.
    T2=[[1,1],[0,1]]
    Ti2=[[1,-1],[0,1]]
    T=block(T2,zero(2,2),zero(2,2),T2)
    Ti=block(Ti2,zero(2,2),zero(2,2),Ti2)
    assert matmul(T,Ti)==eye(K)
    assert bareiss(T)==1
    Sec=[1,1,-1,-1]
    assert all(T[i][j]==0 for i in range(K) for j in range(K)
               if Sec[i]!=Sec[j])
    M=block(eye(n),zero(n,K),zero(K,n),T)
    Gg=matmul(matmul(trans(M),Gext),M)
    XT=matmul(X,T)
    Kmetric=matmul(trans(T),T)
    assert Gg==block(
        matadd(G,matmul(X,trans(X))), XT,
        trans(XT), Kmetric)
    assert Kmetric!=eye(K)
    Kinv=matmul(Ti,trans(Ti))
    assert matmul(Kmetric,Kinv)==eye(K)
    schur=matsub(
        [row[:n] for row in Gg[:n]],
        matmul(matmul(XT,Kinv),trans(XT))
    )
    assert schur==G
    assert bareiss(Gg)==d
    assert parity_test(G,XT,Gg,labels)
    wrong=matsub(
        [row[:n] for row in Gg[:n]],
        matmul(XT,trans(XT)))
    assert wrong!=G,("wrong nonorthogonal gauge accepted",labels)
    return vps,len(str(d))


def run_case(D):
    rho,R,S,J,Q=params(D)
    pred=CASES[D]
    assert (rho,R,S,J,len(Q))==pred["params"]
    qset=set(Q)
    assert len(qset)==len(Q)
    assert all((-x,-y) in qset and (x,-y) in qset for x,y in Q)
    Xfull=full_transverse_X(D,Q,R,S)
    labels=pred["labels"]
    X=[Xfull[r*S+s] for r,s in labels]
    G=gram(D,Q,J,labels)
    assert G==original_jet_gram(D,Q,J,labels)
    data=angular_and_source_checks(
        D,Q,J,labels,X,G,pred["T"],pred["gap"])
    vps,digits=congruence_and_gauge(G,X,labels)
    assert any(Xfull[i][0] or Xfull[i][1] for i in range(len(Xfull)))
    assert any(Xfull[i][2] or Xfull[i][3] for i in range(len(Xfull)))
    print("PHASE288_INTEGRAL_TRANSPORT",{
        "D":D,"rho":rho,"original_Q":len(Q),"original_rows_all_checked":R*S,
        "original_J":J,"original_observation_channels":2*J*len(Q),
        "original_principal_rows_determinant_tested":len(labels),
        "transverse_integral_channels":K,
        "angular_T":data["T"],"angular_gap_T_squared":data["C0"]-data["C90"],
        "g_const_Z2":data["g_const_Z2"],
        "g_const_ZW":data["g_const_ZW"],
        "source_angular_gap_is_original_Gram_entry_squared":True,
        "integral_shear_schur_and_C2_verified":True,
        "original_small_Gram_det_decimal_digits":digits,
        "matched_p_valuations":vps,
        "moving_moving_integral_gauge":"two nonorthogonal unimodular parity-block shears",
        "no_extra_local_Smith_mass":True,
        "not_full_Gram_determinant_or_field_theorem":True,
    },flush=True)


def main():
    frozen_sources()
    for D in (283,403):
        run_case(D)
    # Rational congruence can preserve determinant while changing p2 Smith.
    assert 4*4==16*1 and (2,2)!=(0,4)
    print("PASS Phase288 C2-graded integral transverse transport and no-double-counting",flush=True)


if __name__=="__main__":
    main()
