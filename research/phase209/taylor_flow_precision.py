#!/usr/bin/env python3
"""Exact Phase209 Taylor-flow/ordinary-jet checks, preregistered Issue #154.

Independent integral delta recurrence, rational formal Taylor flow and
original monic Frobenius source row. stdlib; no Hasse derivatives.
"""
from fractions import Fraction
from math import comb, factorial
from collections import defaultdict

def delta(poly,p):
    out=defaultdict(int)
    for (a,b,k),c in poly.items():
        if a:out[a-1,b,k]+=c*a
        if k:out[a+p-1,b,k-1]+=c*k
    return {e:c for e,c in out.items() if c}

def iterate(poly,p,j):
    for _ in range(j):poly=delta(poly,p)
    return poly

def evalpoly(poly,z,w,t):
    return sum(c*z**a*w**b*t**k for (a,b,k),c in poly.items())

def mulh(a,b,J):
    out=defaultdict(Fraction)
    for i,x in a.items():
        for j,y in b.items():
            if i+j<=J:out[i+j]+=x*y
    return {i:x for i,x in out.items() if x}

def taylor_coefficient(p,a,b,k,z,w,t,j):
    Z={0:Fraction(z),1:Fraction(1)}
    T={0:Fraction(t)}
    for i in range(1,p):
        T[i]=Fraction(comb(p,i),p)*z**(p-i)
    T[p]=Fraction(1,p)
    P={0:Fraction(1)}
    for _ in range(a):P=mulh(P,Z,j)
    for _ in range(k):P=mulh(P,T,j)
    return P.get(j,Fraction(0))*w**b

def valuation(n,p):
    if n==0:return None
    out=0
    while n%p==0:
        out+=1;n//=p
    return out

def guaranteed(j,p):
    n=j;v=0
    while n:
        n//=p;v+=n
    return v-j//p

def pairmul(A,B,D):
    a,b=A;c,d=B
    return (a*c-D*b*d,a*d+b*c)

def pairpow(A,k,D):
    out=(1,0)
    while k:
        if k&1:out=pairmul(out,A,D)
        A=pairmul(A,A,D)
        k//=2
    return out

def ordinary_row(D,p,r,s,k,j,z):
    w=(z[0],-z[1]);a=b=0
    for h in range(k+1):
        n=r-p*h
        if n<j:continue
        c=(-1)**h*comb(k,h)*factorial(n)//factorial(n-j)
        v=pairmul(pairpow(z,n-j,D),pairpow(w,s+h,D),D)
        a+=c*v[0];b+=c*v[1]
    den=p**k
    assert a%den==b%den==0
    return a//den,b//den

def run():
    cases=0
    for p in (3,5):
        orders=sorted(set([0,1,p-1,p,p*p-1,p*p,p*p+1,
                           p**3-1,p**3,p**3+1,2*p**3]))
        for j in orders:
            k,a=divmod(j,p)
            f={(a,0,k):1}
            direct=evalpoly(iterate(f,p,j),0,1,0)
            formal=factorial(j)*taylor_coefficient(p,a,0,k,0,1,0,j)
            assert direct==formal==factorial(j)//p**k,(p,j,direct,formal)
            assert valuation(direct,p)==guaranteed(j,p)
            assert guaranteed(j,p)>=j//(p*p)
            cases+=1
        for a,k,b,z,w,t in [(7,2,1,2,3,1),
                            (3,6,0,-1,1,2),(0,5,2,1,2,-1)]:
            f={(a,b,k):1}
            for j in range(a+p*k+2):
                expected=factorial(j)*taylor_coefficient(
                    p,a,b,k,z,w,t,j)
                observed=evalpoly(iterate(f,p,j),z,w,t)
                assert expected==observed,(p,a,k,j,expected,observed)
                assert observed%(p**guaranteed(j,p))==0,(p,a,k,j)
                cases+=1
        D=19 if p==3 else 23
        assert all((-D)%p!=(x*x)%p for x in range(p))
        for j in [p*p,p**3,2*p**3]:
            k,a=divmod(j,p)
            for z in [(1,1),(2,-1),(0,0)]:
                expected=factorial(j)//p**k
                assert ordinary_row(D,p,j,0,k,j,z)==(expected,0)
                assert valuation(expected,p)==guaranteed(j,p)
                cases+=1
    assert cases==176
    print("PHASE209_TAYLOR_FLOW",{"exact_cases":cases,
        "p3_original_sharp_j":[9,27,54],
        "p5_original_sharp_j":[25,125,250],
        "integer_delta_vs_rational_flow":True,
        "original_ordinary_jet_sharp":True},flush=True)
    print("PASS optimal integral Taylor-flow p-adic depth controls")

if __name__=="__main__":run()
