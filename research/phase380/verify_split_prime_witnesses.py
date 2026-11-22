#!/usr/bin/env python3
"""Independent finite certificate verifier (no producer imports or data file).

Checks split-prime witnesses by direct modular-square enumeration, derives
negative fundamental discriminants by trial factorization, and independently
enumerates primitive reduced binary quadratic forms. Standard arithmetic
interpretation theorems are external, not established by this script.
"""
from math import gcd, isqrt

def factor(n):
    n=abs(n)
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p
                e+=1
            out.append((p,e))
        p+=1
    if n>1:
        out.append((n,1))
    return out

def fundamental(d):
    D=-d
    if D%4==1:
        return all(e==1 for _,e in factor(d))
    if D%4==0:
        m=D//4
        return m%4 in (2,3) and all(e==1 for _,e in factor(m))
    return False

def prime(p):
    return p>=2 and factor(p)==[(p,1)]

def split(D,p):
    if p==2:
        return D%8==1
    return D%p!=0 and (D%p in {k*k%p for k in range(p)})

def reduced_forms(D):
    d=-D
    forms=[]
    for a in range(1,isqrt(d//3)+1):
        for b in range(-a,a+1):
            if (b*b+d)%(4*a):
                continue
            c=(b*b+d)//(4*a)
            if c<a or ((abs(b)==a or a==c) and b<0):
                continue
            if gcd(a,b,c)==1:
                forms.append((a,b,c))
    return forms

def main():
    fundamental_ds=[d for d in range(1,653) if fundamental(d)]
    witnesses={}
    for d in fundamental_ds:
        bound=d+1 if d%2 else d
        candidates=(p for p in range(2,(bound-1)//4+1) if prime(p))
        p=next((p for p in candidates if 4*p<bound and split(-d,p)),None)
        if p is not None:
            witnesses[d]=p
    survivors=sorted(set(fundamental_ds)-set(witnesses))
    expected=[3,4,7,8,11,19,43,67,163]
    assert len(fundamental_ds)==199
    assert len(witnesses)==190
    assert max(witnesses.values())==31
    assert survivors==expected
    assert [d for d in fundamental_ds if len(reduced_forms(-d))==1]==expected
    assert reduced_forms(-163)==[(1,1,41)]
    print('INDEPENDENT VERIFIER PASS: 199 fundamental / 190 split obstructions / 9 survivors')

if __name__=='__main__':
    main()
