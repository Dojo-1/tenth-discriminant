#!/usr/bin/env python3
"""Phase156: transported Archimedean jet budget for the ORIGINAL integer Gram.
Finite checks are evidence, NOT a proved 6-billion number-field endpoint.
"""
from fractions import Fraction as F
from mpmath import mp
from sympy import Matrix, Rational
from phase153_bertrand_budget import normalized, radius, source_correspondence
from phase147_prime_adequacy import original_eval
from phase144_verifier import FULL
from phase144_minimum_support import SIX

mp.dps=75
M=mp.mpf

def valuation(n,q):
    n=abs(int(n))
    assert n>0
    v=0
    while n%q==0:
        n//=q;v+=1
    return v

def vf(j,q):
    v=0
    while j:
        j//=q;v+=j
    return v

def capacity(Q,D,R,S,q=2,fold=False):
    costs=[]
    for x,y in Q:
        w=2 if fold and y!=0 else 1
        for j in range(S):
            costs.append(2*vf(j,q)+valuation(2*w,q))
            if y!=0: costs.append(2*vf(j,q)+valuation(2*D*w,q))
    assert len(costs)>=R*S
    return sum(sorted(costs)[:R*S])

def gram(Q,D,R,S,fold=False):
    E=original_eval(Q,D)
    assert E.rows==R*S
    weights=[]
    for x,y in Q:
        w=2 if fold and y!=0 else 1
        for j in range(S): weights.extend((2*w,2*D*w))
    assert len(weights)==E.cols
    return E*Matrix.diag(*weights)*E.T

def exact_cases():
    D,R,S=19,8,4
    Q=list(FULL);Qplus=[q for q in Q if q[1]>=0]
    assert len(Q)==21 and len(Qplus)==16
    full=gram(Q,D,R,S)
    assert full==gram(Qplus,D,R,S,fold=True)
    for tag,pts,fold,G,beta,v2 in (
        ("6",SIX,False,gram(SIX,D,R,S),56,166),
        ("21",Q,False,full,32,172),
        ("fold16",Qplus,True,full,42,172)):
        v=valuation(abs(int(G.det(method="domain-ge"))),2)
        assert (capacity(pts,D,R,S,2,fold),v)==(beta,v2)
        print("PHASE156_D19",tag,"beta2",beta,"actual_v2",v,flush=True)
    D,R,S=163,30,5
    a=[(x,1) for x in range(-7,8)]
    b=[(x,1) for x in range(-7,9)]
    assert (capacity(a,D,R,S,2),capacity(a,D,R,S,3),
            capacity(a,D,R,S,163),capacity(b,D,R,S,2))==(450,120,75,410)
    print("PHASE156_D163_CAPACITY_PASS",flush=True)

def transport_controls():
    for k in (0,1,3,10,30):
        U=Matrix([[1,k],[0,1]])
        G=U*U.T
        assert U.det()==G.det()==1 and G[0,0]==1+k*k
        # Against transported unit U I U^T, the order cost is ONE.
        assert G==U*Matrix.eye(2)*U.T
        print("PHASE156_FIXED_REFERENCE",k,"cost_at_least",1+k*k,
              "transported_reference_cost",1,flush=True)
    T=Matrix([[Rational(1,2),0],[0,Rational(1,3)]])
    assert T.det()==Rational(1,6) and (T*T.T).det()==Rational(1,36)
    assert valuation(6,2)==valuation(6,3)==1
    assert abs(mp.log(M(1)/36)+2*mp.log(2)+2*mp.log(3))<M("1e-65")
    print("PHASE156_RATIONAL_PRODUCT_FORMULA_PASS",flush=True)

def v2_prefix(n):
    # Sum_{j<n} v2(j!) by interchanging Legendre floors.
    result=0;pow2=2
    while pow2<n:
        full,rem=divmod(n,pow2)
        result+=pow2*full*(full-1)//2+full*rem
        pow2*=2
    return result

def min_t2(m,N,S):
    assert 0<m<=N*S
    j,left=divmod(m,N)
    assert j<=S
    return N*v2_prefix(j)+left*vf(j,2)

def uniform_gates():
    assert 278**4<6_000_000_000
    assert F(22,21)*(1+F(19,5*278)+F(4,278**3))**2<F(27,25)
    assert F(27,25)*(1+F(1,10**9))<F(11,10)
    assert F(19,10*278)+F(4,278**3)<F(1,140)
    a=F(15,16)*F(10,11)*(F(1,25)-F(1,10**9))-F(127,16*10**9)
    assert F(69,100)*a>F(235,10000)
    assert mp.log(2)>M(".69") and mp.log(6_000_000_000)>M("22.5")
    assert mp.log(M(24)/5)<M("1.57")
    gap=F(1,5)*F(225,10)-F(44,100)*F(157,100)-F(3817,1000)-F(1,10**6)+F(235,10000)
    assert gap>F(15,1000)
    print("PHASE156_RATIONAL_ENVELOPE_PASS",float(gap),flush=True)

def source_parameter_tests():
    for D in (5_000_000_003,5_500_000_003,6_000_000_003,
              8_000_000_003,25_000_000_003,100_000_000_003):
        m=(D+1)//4
        for ratio in (M(5)/6+M("1e-9"),M(".9"),M(".99999999")):
            p=int(mp.floor(M(m)*ratio))+1 # analytic ONLY, not necessarily prime
            R=p-1;S=R//25;rho=radius(D,p)
            L,U=normalized(R,S,rho,4*D)
            Nupper=int(mp.ceil(M(27)*p/25))
            beta=R*S+2*min_t2(R*S,Nupper,S)
            extra=M(beta)*mp.log(2)/(M(R)**2*S)
            if D>=6_000_000_000:
                assert L>=mp.log(R)-M("4.411")
                assert U<=M(".24")*mp.log(D)+M(".56")*mp.log(R)-M(".594")
                assert extra>M(".0235") and L+extra>U
            if ratio<M(".834"):
                print("PHASE156_ENDPOINT",D,"rho",rho,
                      "odd_gap",mp.nstr(L-U,12),
                      "jet2",mp.nstr(extra,12),
                      "combined",mp.nstr(L+extra-U,12),flush=True)

def main():
    source_correspondence()
    exact_cases()
    transport_controls()
    uniform_gates()
    source_parameter_tests()
    print("PHASE156_TRANSPORT_ARCH_JETS_PASS: candidate only",flush=True)

if __name__=="__main__":main()
