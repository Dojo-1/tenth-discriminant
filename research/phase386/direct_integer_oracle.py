#!/usr/bin/env python3
"""Independent original-source integer-pair ordinary derivative reference."""
from math import comb

def mul(D,a,b):
    x,y=a;u,v=b
    return (x*u-D*y*v,x*v+y*u)

def power(D,a,n):
    assert n>=0
    out=(1,0)
    for _ in range(n):out=mul(D,out,a)
    return out

def ordinary_jet(D,r,s,j,point):
    if j>r:return (0,0)
    x,y=point
    u=mul(D,power(D,point,r-j),power(D,(x,-y),s))
    f=1
    for t in range(j):f*=r-t
    return f*u[0],f*u[1]

def normal_jet(D,p,S,r,s,j,a):
    k=min(r//p,S-1-s)
    z=[0,0]
    for t in range(k+1):
        v=ordinary_jet(D,r-p*t,s+t,j,a)
        for c in (0,1):z[c]+=(-1)**t*comb(k,t)*v[c]
    assert all(n%p**k==0 for n in z)
    return tuple(n//p**k for n in z)
