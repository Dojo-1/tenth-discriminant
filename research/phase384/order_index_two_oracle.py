#!/usr/bin/env python3
"""Exact bounded source-order -> maximal-order chart oracle.
Python integer arithmetic is a TEST, not a proof of the analytic Gram bounds.
"""
from itertools import product
from math import isqrt

def chart(p):
    x,y=p
    return x-y,2*y

def beta_mul(D,a,b):
    x,y=a;u,v=b
    return x*u-D*y*v,x*v+y*u

def omega_mul(c,a,b):
    x,y=a;u,v=b
    return x*u-c*y*v,x*v+y*u+y*v

def beta_trace(D,a,b):
    x,y=a;u,v=b
    return 2*(x*u+D*y*v)

def omega_trace(c,a,b):
    x,y=a;u,v=b
    return 2*x*u+x*v+y*u+2*c*y*v

def squarefree(d):
    return all(d%(p*p) for p in range(2,isqrt(d)+1))

def run():
    Ds=[d for d in range(3,200) if d%4==3 and squarefree(d)]
    pts=list(product(range(-2,3),repeat=2))
    count=0
    for d in Ds:
        c=(d+1)//4
        T=((1,-1),(0,2))
        Bomega=((2,1),(1,2*c))
        Bbeta=((2,0),(0,2*d))
        mul=lambda A,B: tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
        assert mul(mul(tuple(zip(*T)),Bomega),T)==Bbeta
        assert 2*2*c-1==d and Bbeta[0][0]*Bbeta[1][1]==4*d
        for a in pts:
            for b in pts:
                assert chart(beta_mul(d,a,b))==omega_mul(c,chart(a),chart(b))
                assert beta_trace(d,a,b)==omega_trace(c,chart(a),chart(b))
                count+=1
    for p in (2,3,5,7,11,13):
        image={(chart((x,y))[0]%p,chart((x,y))[1]%p)
               for x in range(p) for y in range(p)}
        assert len(image)==(p if p==2 else p*p)
    assert not any(chart(xy)==(0,1) for xy in pts)
    assert len(Ds)==42 and count==26250
    print('PASS: 42 squarefree odd-chart radicands, 26250 pair-pair identities')
    print('PASS: trace Gram congruence and index 2 (odd local invertibility)')
    print('PASS: mod-2 kernel / omega outside source lattice')

if __name__=='__main__':run()
