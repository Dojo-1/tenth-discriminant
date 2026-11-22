#!/usr/bin/env python3
"""Exact p-adic precision transport for normalized ordinary source jets.

Tests source-specific congruences at D=43, p=3, R=7, S=J=3.
The universal polynomial congruence implication is a paper proof.
"""
from math import comb

D,p,R,S,J=43,3,7,3,3

def mul(a,b):
    x,y=a; u,v=b
    return (x*u-D*y*v, x*v+y*u)
def power(a,n):
    ans=(1,0)
    for _ in range(n):ans=mul(ans,a)
    return ans
def ordinary_jet(r,s,j,a):
    if j>r:return (0,0)
    x,y=a
    z=mul(power(a,r-j),power((x,-y),s))
    coeff=1
    for t in range(j): coeff*=r-t
    return tuple(coeff*t for t in z)

def samples(rho):
    return [(x,y) for x in range(-rho,rho+1) for y in range(-rho,rho+1)
            if x*x+D*y*y<=rho*rho]

def normal_jet(r,s,j,a):
    k=min(r//p,S-1-s)
    vals=[0,0]
    for t in range(k+1):
        v=ordinary_jet(r-p*t,s+t,j,a)
        for ax in (0,1):vals[ax]+=(-1)**t*comb(k,t)*v[ax]
    assert all(x%p**k==0 for x in vals)
    return k,tuple(x//p**k for x in vals)

def main():
    Q=samples(9)
    assert len(Q)==45
    assert max(min(r//p,S-1-s) for r in range(R) for s in range(S))==2
    total=0
    for a in Q:
        for shift in ((27,0),(0,27),(-27,0),(0,-27)):
            b=(a[0]+shift[0],a[1]+shift[1])
            for r in range(R):
                for s in range(S):
                    for j in range(J):
                        k,va=normal_jet(r,s,j,a)
                        kb,vb=normal_jet(r,s,j,b)
                        assert k==kb and all((x-y)%3==0 for x,y in zip(va,vb))
                        total+=1
    assert total==11340
    for a in Q[:10]:
        b=(a[0]+81,a[1])
        for r in range(R):
            for s in range(S):
                for j in range(J):
                    _,va=normal_jet(r,s,j,a)
                    _,vb=normal_jet(r,s,j,b)
                    assert all((x-y)%9==0 for x,y in zip(va,vb))
    assert [normal_jet(3,0,0,(x,0))[1][0]%3 for x in (0,3,6)]==[0,2,1]
    assert [normal_jet(3,0,0,(x,0))[1][0]%9 for x in (0,9)]==[0,6]
    print('PASS',total,'p^3-shift normalized original jets modulo 3')
    print('PASS p^4-shift jets modulo 9, plus lower-precision hostile controls')

if __name__=='__main__':main()
