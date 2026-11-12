#!/usr/bin/env python3
"""Phase288-B exact weighted full-order transverse remainder in original Gram.

Preregistered at e5b8fe8 AFTER Phase288-A success and BEFORE this program.
The weighted half-coset remainder is EXTERNAL DATA in an integral source
register, NOT an additional arithmetic invariant of the original Gram.
"""
from fractions import Fraction as F
from math import isqrt

from integral_transverse_transport import (
    frozen_sources, params, gram, jet, CASES, full_transverse_X,
    eye, matmul, trans, matadd, block, zero, bareiss
)

HALF_EXPECTED={283:192,403:260}
PRIMES=(2,3,5,7,11)


def integer_coset(D,Q):
    return [(2*x,2*y) for x,y in Q]


def half_coset(D,rho):
    bound=4*rho*rho
    out=[]
    for b in range(-isqrt(bound//D),isqrt(bound//D)+1):
        if b%2==0:continue
        remain=bound-D*b*b
        if remain<0:continue
        t=isqrt(remain)
        for a in range(-t,t+1):
            if a%2:
                out.append((a,b))
    return out


def squared_norm(D,z):
    a,b=z
    v=a*a+D*b*b
    assert v%4==0
    return v//4


def trace_squared(D,z):
    a,b=z
    v=a*a-D*b*b
    assert v%2==0
    return v//2


def finite_weighted_curvature(D,rho,full):
    scale=1<<(rho*rho)
    records=[]
    anum=bnum=xy=trace_num=0
    for a,b in full:
        n=squared_norm(D,(a,b))
        assert n<=rho*rho
        w=1<<(rho*rho-n)
        records.append((a,b,w))
        anum+=a*a*w
        bnum+=D*b*b*w
        xy+=a*b*w
        trace_num+=trace_squared(D,(a,b))*w
    assert xy==0
    A=F(anum,4*scale)
    B=F(bnum,4*scale)
    T=A-B
    assert trace_num%2==0
    assert T==F(trace_num,2*scale)

    c0numerator=0
    c90numerator=0
    for a,b,wa in records:
        for c,d,wc in records:
            w=wa*wc
            c0numerator+=(a*c+D*b*d)**2*w
            c90numerator+=D*(b*c-a*d)**2*w
    den=16*scale*scale
    c0=F(c0numerator,den)
    c90=F(c90numerator,den)
    assert c0==A*A+B*B
    assert c90==2*A*B
    assert c0-c90==T*T
    return A,B,T,trace_num,scale


def exact_tail(rho):
    k=4
    q=F((rho+3)**k,(rho+2)**k*(1<<(2*rho+1)))
    assert 0<q<1
    upper=F(8*(rho+2)**k,1<<(rho*rho))/(1-q)
    return upper


def stable_integral_certificate(G,Xplus,labels):
    n=len(G)
    k=len(Xplus[0])
    assert k==5
    Xtranspose=trans(Xplus)
    H=block(matadd(G,matmul(Xplus,Xtranspose)),Xplus,
            Xtranspose,eye(k))
    base=block(G,zero(n,k),zero(k,n),eye(k))
    U=block(eye(n),Xplus,zero(k,n),eye(k))
    L=block(eye(n),zero(n,k),
            [[-v for v in row] for row in Xtranspose],eye(k))
    assert matmul(matmul(U,base),trans(U))==H
    assert matmul(matmul(trans(L),H),L)==base
    assert matmul(trans(U),L)==eye(n+k)
    # Inversion symmetry matches the four original channels and fifth even R.
    signs=[(-1)**(r+s) for r,s in labels]+[1,1,-1,-1,1]
    assert all(H[i][j]==signs[i]*signs[j]*H[i][j]
        for i in range(n+k) for j in range(n+k))
    olddet=bareiss(G)
    assert olddet>0
    assert bareiss(H)==olddet
    return len(str(olddet))


def run_case(D):
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==CASES[D]["params"]
    integer=integer_coset(D,Q)
    half=half_coset(D,rho)
    assert len(half)==HALF_EXPECTED[D]
    full=integer+half
    allpoints=set(full)
    assert len(allpoints)==len(full)
    assert all((-a,-b) in allpoints and (a,-b) in allpoints for a,b in full)
    assert all((a,-b) in allpoints for a,b in full)
    assert set(integer).isdisjoint(half)
    assert all(squared_norm(D,z)<=rho*rho for z in full)
    assert any((z[0]*z[0]-D*z[1]*z[1])%4!=0 for z in half),(
        "wrong assumption: half-coset Re(z^2) always integral",D
    )
    A,B,Tweighted,num,scale=finite_weighted_curvature(D,rho,full)
    assert A>B>0
    labels=CASES[D]["labels"]
    G=gram(D,Q,J,labels)
    g=G[labels.index((0,0))][labels.index((2,0))]
    assert g==2*CASES[D]["T"]

    original_weight_correction=sum(
        trace_squared(D,z)*((1<<(rho*rho-squared_norm(D,z)))-scale)
        for z in integer)
    half_correction=sum(
        trace_squared(D,z)*(1<<(rho*rho-squared_norm(D,z)))
        for z in half)
    rnum=num-scale*g
    assert rnum==original_weight_correction+half_correction
    assert rnum%2==0
    assert Tweighted==F(g,2)+F(rnum,2*scale)
    assert rnum!=0
    assert half_correction!=0
    assert original_weight_correction!=0
    assert Tweighted!=F(g,2),("weighted full order was conflated with original Gram")

    # The ORIGIN is the unique inversion fixed original source point:
    assert Q.count((0,0))==1
    # A fifth original integer co-vector supported at the original j0 REAL
    # observation channel at q0 has value rnum/2.
    v_at_zero=rnum//2
    Xall=full_transverse_X(D,Q,R,S)
    fifth=[]
    for r in range(R):
        for s in range(S):
            coeff=jet(D,r,s,0,(0,0))[0]
            val=2*coeff*v_at_zero
            assert val==(rnum if (r,s)==(0,0) else 0)
            fifth.append(val)
    X5=[row+[fifth[i]] for i,row in enumerate(Xall)]
    assert all(X5[r*S+s][4]==0 for r in range(R) for s in range(S)
               if (r+s)%2==1)
    Xsel=[X5[r*S+s] for r,s in labels]
    digits=stable_integral_certificate(G,Xsel,labels)

    Btail=exact_tail(rho)
    limit=930 if D==283 else 1560
    assert Btail<F(1,1<<limit)
    error_radius=2*abs(Tweighted)*Btail+Btail*Btail
    assert error_radius>0
    print("PHASE288_WEIGHTED_REMAINDER",{
      "D":D,"rho":rho,
      "original_integer_points":len(integer),
      "finite_maximal_order_half_coset_points":len(half),
      "finite_maximal_order_total_points":len(full),
      "original_gram_g_1_Z2":g,
      "weighted_four_dimensional_curvature_gap":"(g/2+R/2^(rho^2+1))^2",
      "weighted_source_remainder_nonzero":rnum!=0,
      "separate_original_weight_and_half_coset_corrections":True,
      "integer_remainder_even":rnum%2==0,
      "remainder_numerator_bit_length":abs(rnum).bit_length(),
      "direct_pairwise_full_order_angular_identities":True,
      "fifth_integer_channel_recovers_exact_remainder_at_origin":True,
      "selected_original_gram_rows":len(labels),
      "selected_gram_det_decimal_digits":digits,
      "local_Smith_mass_added":0,
      "two_coset_degree2_tail_upper_lt_2_pow_minus":limit,
      "infinite_curvature_error_bounded_exactly":True,
      "not_an_improvement_to_original_field_theorem":True,
    },flush=True)


def main():
    frozen_sources()
    for D in (283,403):
        run_case(D)
    print("PASS Phase288-B full-order weighted remainder through integral original-source anchor",flush=True)


if __name__=="__main__":
    main()
