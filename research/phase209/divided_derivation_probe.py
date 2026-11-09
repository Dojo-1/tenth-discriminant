#!/usr/bin/env python3
"""Phase209-A/B prereg #154/#155: ordinary-jet integral derivation and exact
original Gram conjugation check. stdlib, independent small bounded oracles.
Not a uniform proof or a change of the mainline 322^4 field result.
"""
from math import comb,isqrt
from collections import defaultdict

def mul(a,b,D):
    return a[0]*b[0]-D*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def power(a,k,D):
    z=(1,0)
    while k:
        if k&1:z=mul(z,a,D)
        a=mul(a,a,D);k//=2
    return z
def falling(r,j):
    q=1
    for h in range(j):q*=r-h
    return q if j<=r else 0
def ordinary_source(D,p,r,s,S,j,z):
    k=min(r//p,S-1-s)
    w=z[0],-z[1];a=b=0
    for t in range(k+1):
        e=r-p*t
        if e<j:continue
        u,v=mul(power(z,e-j,D),power(w,s+t,D),D)
        c=(-1)**t*comb(k,t)*falling(e,j)
        a+=c*u;b+=c*v
    den=p**k
    assert a%den==b%den==0,("old inert divisor",D,p,r,s,j,z)
    return a//den,b//den

def delta(P,p):
    out=defaultdict(int)
    for (a,s,k),v in P.items():
        if a:out[a-1,s,k]+=a*v
        if k:out[a+p-1,s,k-1]+=k*v
    return {x:v for x,v in out.items() if v}
def iterate(P,p,j):
    for _ in range(j):P=delta(P,p)
    return P
def evaluate(P,z,T,D):
    w=z[0],-z[1];a=b=0
    for (e,s,k),c in P.items():
        q=mul(mul(power(z,e,D),power(w,s,D),D),power(T,k,D),D)
        a+=c*q[0];b+=c*q[1]
    return a,b
def quotient(D,p,z):
    w=z[0],-z[1];q=power(z,p,D)
    a,b=q[0]-w[0],q[1]-w[1]
    assert a%p==b%p==0,("noninert",D,p,z)
    return a//p,b//p

def check_operator():
    checked=0
    for p in (3,5):
        for a in range(2*p+1):
            for k in range(2*p+2):
                f={(a,2,k):1}
                got={e:v%p for e,v in iterate(f,p,p).items() if v%p}
                expected={(a,2,k-1):(-k)%p} if k%p else {}
                assert got==expected,(p,a,k,got,expected)
                assert all(v%p==0 for v in iterate(f,p,p*p).values())
                checked+=1
    cases=[(19,3,30,0,23,(1,1),(0,1,8,9,10,17,18,19)),
           (23,5,60,0,55,(1,1),(0,1,24,25,26,49,50,51)),
           (19,3,30,1,23,(2,1),(0,1,9,18)),
           (23,5,60,1,55,(2,1),(0,1,25,50))]
    for D,p,r,s,S,z,orders in cases:
        k=min(r//p,S-1-s)
        T=quotient(D,p,z)
        seed={(r-p*k,s,k):1}
        for j in orders:
            direct=ordinary_source(D,p,r,s,S,j,z)
            independent=evaluate(iterate(seed,p,j),z,T,D)
            assert direct==independent,(D,p,r,s,j,direct,independent)
            den=p**(j//(p*p))
            assert direct[0]%den==direct[1]%den==0,(D,p,j,direct)
        print("ORDINARY_JET_DEPTH",{"D":D,"p":p,"r":r,"s":s,"k":k,
            "orders":orders,"quotient":T},flush=True)
    z3=power((1,1),3,287)
    assert (z3[0]-1)%3 or (z3[1]+1)%3
    print("PASS_DELTA",{"tested_polynomial_monomials":checked,
       "ordinary_beyond_p_squared":True,"noninert_negative":True},flush=True)

def ellipse(D,rho):
    out=[]
    for y in range(-isqrt(rho*rho//D),isqrt(rho*rho//D)+1):
        x=isqrt(rho*rho-D*y*y)
        out.extend((t,y) for t in range(-x,x+1))
    return out
def metric(D,a,b):
    return 2*(a[0]*b[0]+D*a[1]*b[1])
def check_gram():
    D,p,S,J=19,3,10,10;Q=ellipse(D,6)
    assert len(Q)==31
    rows=[(0,0),(1,0),(3,0),(3,1),(10,0),(11,0),(11,1),(11,3)]
    n=len(rows);G=[[0]*n for _ in rows];F=[[0]*n for _ in rows]
    for j in range(J):
        for z in Q:
            zz=(z[0],-z[1])
            v=[ordinary_source(D,p,r,s,S,j,z) for r,s in rows]
            bv=[ordinary_source(D,p,r,s,S,j,zz) for r,s in rows]
            assert all((a,-b)==c for (a,b),c in zip(v,bv))
            for a in range(n):
                for b in range(n):G[a][b]+=metric(D,v[a],v[b])
        for z in Q:
            if z[1]<0:continue
            v=[ordinary_source(D,p,r,s,S,j,z) for r,s in rows]
            for a in range(n):
                for b in range(n):
                    F[a][b]+=(2 if z[1]>0 else 1)*metric(D,v[a],v[b])
            scale=p**(j//(p*p))
            assert all(a%scale==b%scale==0 for a,b in v)
    assert F==G
    # Removing a conjugate partner changes the original trace Gram.
    minus=(0,-1)
    assert minus in Q
    difference=0
    for j in range(J):
        v=[ordinary_source(D,p,r,s,S,j,minus) for r,s in rows]
        difference+=sum(metric(D,t,t) for t in v)
    assert difference>0
    print("PASS_ORIGINAL_GRAM_FOLD",{"D":D,"p":p,"Q":len(Q),
       "original_rows_tested":n,"matched_entries":n*n,
       "negative_missing_conjugate_changes_Gram":True},flush=True)

def _pair_sub(a,b):
    return a[0]-b[0],a[1]-b[1]

def _pair_scale(c,a):
    return c*a[0],c*a[1]

def _old_monomial_ordinary_jet(D,r,s,j,z):
    """The original integerDerivativeRow on the exact conjugate coordinate."""
    if j>r:return (0,0)
    w=(z[0],-z[1])
    return _pair_scale(falling(r,j),
        mul(power(z,r-j,D),power(w,s,D),D))

def _combined_matrix_row_jet(D,p,R,S,r,s,j,z):
    """Independent two-index old-monomial matrix expansion; no new source."""
    assert 0<=r<R and 0<=s<S and p>=2
    k=min(r//p,S-1-s)
    ell=s//(p*p)
    a=b=0
    active=0
    for t in range(k+1):
        for u in range(ell+1):
            rr=r-p*t
            ss=s+t-(p*p-1)*u
            assert 0<=rr<R and 0<=ss<S,(D,p,r,s,t,u,rr,ss)
            assert rr*S+ss<R*S
            coeff=(-1)**(t+u)*comb(k,t)*comb(ell,u)
            v=_old_monomial_ordinary_jet(D,rr,ss,j,z)
            a+=coeff*v[0];b+=coeff*v[1]
            active+=1
    return (a,b),active,k,ell

def _poly_mul(left,right,D):
    """Exact independent polynomial multiplication over Z[sqrt(-D)]."""
    out=defaultdict(lambda:(0,0))
    for a,ca in left.items():
        for b,cb in right.items():
            c=mul(ca,cb,D)
            old=out[a+b]
            out[a+b]=(old[0]+c[0],old[1]+c[1])
    return {j:v for j,v in out.items() if v!=(0,0)}

def _combined_direct_polynomial(D,p,R,S,r,s,z):
    """No binomial-row coefficients: multiply literal factors in Z."""
    k=min(r//p,S-1-s)
    ell=s//(p*p)
    w=(z[0],-z[1])
    horizontal=_pair_sub(power(w,p*p,D),w)
    constant=mul(power(w,s-p*p*ell,D),power(horizontal,ell,D),D)
    poly={r-p*k:constant}
    factor={p:(1,0),0:(-w[0],-w[1])}
    for _ in range(k):
        poly=_poly_mul(poly,factor,D)
    return poly

def _direct_polynomial_jet(D,poly,j,z):
    """Different oracle: ordinary differentiate polynomial coefficients."""
    a=b=0
    for degree,coefficient in poly.items():
        if j>degree:continue
        value=mul(coefficient,power(z,degree-j,D),D)
        factor=falling(degree,j)
        a+=factor*value[0];b+=factor*value[1]
    return (a,b)

def check_combined_original_jets():
    """Phase244 prospective issue #159: two different exact source oracles."""
    cases=[
       (19,3,9,4,11,3,9,11,1,1,59),
       (19,3,9,7,21,6,18,21,2,2,59),
       (23,5,12,6,27,5,25,27,1,1,101),
       (23,5,12,11,53,10,50,53,2,2,101)]
    observations=0
    for D,p,rho,R,S,r,s,J,k_expected,ell_expected,N in cases:
        assert all((-D)%p!=v*v%p for v in range(p))
        Q=ellipse(D,rho)
        assert len(Q)==N,(D,rho,len(Q),N)
        for z in Q:
            poly=_combined_direct_polynomial(D,p,R,S,r,s,z)
            for j in range(J):
                from_matrix,active,k,ell=_combined_matrix_row_jet(
                    D,p,R,S,r,s,j,z)
                from_direct=_direct_polynomial_jet(D,poly,j,z)
                assert k==k_expected and ell==ell_expected
                assert active==(k+1)*(ell+1)
                assert from_matrix==from_direct,(
                    "combined old-jet/source mismatch",D,p,r,s,z,j,
                    from_matrix,from_direct)
                den=p**(k+ell)
                assert all(v%den==0 for v in from_matrix),(
                    "inert combined p-adic divisor fails",D,p,r,s,z,j,
                    from_matrix,den)
                observations+=1
        print("PHASE244_COMBINED_CASE",
            {"D":D,"p":p,"rho":rho,"original_Q":N,
             "R":R,"S":S,"J":J,"k":k_expected,
             "ell":ell_expected},flush=True)

    # Hostile differential control: H=(W^9-W)/3 and T=(Z^3-W)/3
    # have the same VALUE mod3 on inert observations; substituting
    # H=T before differentiating is false for ordinary Z-jets.
    z=(1,1);D=19;p=3
    actual,_,_,_=_combined_matrix_row_jet(D,p,4,11,3,9,1,z)
    w=(z[0],-z[1])
    T=_pair_sub(power(z,3,D),w)
    wrong=_pair_scale(6,mul(power(z,2,D),T,D))
    assert all(t%9==0 for t in actual+wrong)
    assert any((actual[i]//9-wrong[i]//9)%3!=0 for i in range(2))
    # Ramified/split contexts violate the stated inert-residue assumption.
    assert any((-3)%3==v*v%3 for v in range(3))
    assert any((-19)%5==v*v%5 for v in range(5))
    print("PASS_PHASE244_COMBINED_SOURCE",
        {"exact_original_ordinary_jet_checks":observations,
         "independent_polynomial_multiplication":True,
         "noncommuting_source_matrix_not_substituted":True,
         "differentiated_h_equals_t_negative_control":True,
         "ramified_split_hypotheses_rejected":True},flush=True)

if __name__=="__main__":
    check_operator()
    check_gram()
    check_combined_original_jets()
    print("PASS PHASE209-A/B source oracles",flush=True)
