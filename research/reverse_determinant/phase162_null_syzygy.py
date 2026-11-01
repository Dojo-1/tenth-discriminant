#!/usr/bin/env python3
"""Phase162: S-polynomial / leading-term completion of the binary jet-null ideal.

Finite exact original ordinary-Z-jet controls. Four-generator lower bound is
PAPER mathematics until its full row-to-Gram factor has a Lean proof.
"""
from math import comb
from sympy import Poly, Symbol, diff
from phase159_observation_continuum import ordinary_effective, powers
from phase162_binary_null_lower import triple_floor, source_correspondence


def best_factors(r,s,S):
    """Optimize within F(Z), H(Z,W), F(W), K(Z,W) generators only."""
    best=(-1,None)
    for b in range(min(r//2,(S-1-s)//2)+1):
        for d in range(min((r-2*b)//2,s//2)+1):
            a=(r-2*b-2*d)//4
            c=(s-2*d)//4
            k=a+b+c+d
            if k>best[0]:best=(k,(a,b,c,d))
    return best


def exponent(R,S):
    return R*S+2*sum(best_factors(r,s,S)[0]
                     for r in range(R) for s in range(S))


def source_exact_rows(D,R,S,Q):
    E,weights,_=ordinary_effective(Q,D,R,S)
    assert len(E)==R*S and len(E[0])==len(weights)
    for r in range(R):
        for s in range(S):
            k,(a,b,c,d)=best_factors(r,s,S)
            assert 4*a+2*b+2*d<=r and 4*c+2*d<=s and s+2*b<S
            for col in range(len(weights)):
                val=sum(
                    (-1)**(t+u+v+w)*comb(a,t)*comb(b,u)*comb(c,v)*comb(d,w)
                    * E[(r-2*t-2*u)*S+s+2*u-2*v-2*w][col]
                    for t in range(a+1) for u in range(b+1)
                    for v in range(c+1) for w in range(d+1))
                assert val%(2**k)==0,(D,r,s,col,a,b,c,d,k,val)
    return exponent(R,S)


def main():
    source_correspondence()
    Z,W=Symbol("Z"),Symbol("W")
    F=Z**4-Z**2
    H=Z**2-W**2
    K=Z**2*(W**2-1)
    assert Poly(F-Z**2*H-K,Z,W).is_zero
    for j in range(1,5):
        assert all(int(c)%2==0 for c in Poly(diff(K,Z,j),Z,W).coeffs())
    for D in (2,3,19,163):
        for x in range(-2,3):
            for y in range(-2,3):
                z=powers((x,y),2,D)
                w=powers((x,-y),2,D)
                a=x*x-D*y*y
                # K=z^2*(w^2-1): both integer coordinates even
                from phase159_observation_continuum import pairmul
                Kval=pairmul(z[2],(w[2][0]-1,w[2][1]),D)
                assert Kval==(a*(a-1)+4*D*x*x*y*y,-2*x*y)
                assert all(k%2==0 for k in Kval)
    cases=[
        (3,4,4,[(0,2),(-2,1),(0,0)],32),
        (19,8,4,[(0,2),(-2,1),(0,0),(2,-1)],96),
        (163,30,5,[(x,0) for x in range(-10,11)]
            + [(x,1) for x in range(-2,3)],1358),
        (2,10,5,[(x,y) for x in range(-2,3) for y in range(-2,3)],198),
        (4,12,9,[(0,0),(1,1),(2,-1)],652),
    ]
    for D,R,S,Q,expected in cases:
        assert source_exact_rows(D,R,S,Q)==expected
        assert expected>=triple_floor(R,S)
        print("PHASE162_SYZYGY_SOURCE",D,R,S,expected,flush=True)
    for R in range(1,30):
        for S in range(1,13):
            assert exponent(R,S)>=triple_floor(R,S)
    print("PHASE162_BINARY_NULL_SYZYGY_PASS: finite only",flush=True)


if __name__=="__main__":main()
