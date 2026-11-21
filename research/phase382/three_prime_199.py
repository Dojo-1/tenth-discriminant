#!/usr/bin/env python3
"""Exact three-prime sieve for the conditional d<=199 theorem.

Input NOT proved by this program: if h(Q(sqrt(-d)))=1 for a negative
fundamental field discriminant -d, then every prime p<d/4 is inert.
This program checks only p=2,3,7. It does not prove GRH, the Epstein
analytic-continuation bridge or any class-number identity.
"""
from math import isqrt

TARGET=(3,4,7,8,11,19,43,67,163)
PRIMES=(2,3,7)

def squarefree(n):
    assert n>=1
    return all(n%(q*q) for q in range(2,isqrt(n)+1))

def fundamental_abs(d):
    if d<3:return False
    if d%4==3:return squarefree(d)
    if d%4==0:
        m=d//4
        return m%4 in (1,2) and squarefree(m)
    return False

def symbol(d,p):
    assert fundamental_abs(d) and p in PRIMES
    D=-d
    if p==2:
        if d%2==0:return 0
        return 1 if D%8==1 else -1
    if d%p==0:return 0
    value=pow(D%p,(p-1)//2,p)
    assert value in (1,p-1)
    return 1 if value==1 else -1

def independent_symbol(d,p):
    D=-d
    if D%p==0:return 0
    if p==2:
        return 1 if any(x%2 and (x*x-D)%8==0 for x in range(8)) else -1
    return 1 if D%p in {x*x%p for x in range(1,p)} else -1

def survives(d,primes=PRIMES):
    return all(not(4*p<d) or symbol(d,p)==-1 for p in primes)

def main():
    fundamental=[d for d in range(3,200) if fundamental_abs(d)]
    assert len(fundamental)==62
    for d in fundamental:
        for p in PRIMES:
            assert symbol(d,p)==independent_symbol(d,p),(d,p)
    survivors=tuple(d for d in fundamental if survives(d))
    assert survivors==TARGET,survivors
    missing={}
    for p in PRIMES:
        other=tuple(q for q in PRIMES if q!=p)
        missing[p]=tuple(sorted(set(d for d in fundamental if survives(d,other))-set(TARGET)))
    assert missing=={
        2:(79,88,127,148,151,184),
        3:(51,107,123,155,179),
        7:(91,115,139,187)
    },missing
    # A ramified local factor is not an inert prime.
    assert fundamental_abs(20) and 4*2<20 and symbol(20,2)==0
    assert sum(not survives(d) for d in fundamental)==53
    print("PASS: 62 fundamental negative discriminants d<=199")
    print("PASS: 53 excluded by inertness at p=2,3,7")
    print("PASS: survivors:",list(survivors))
    print("PASS: independent residue symbols, omission/ramification controls")
    return survivors

if __name__=="__main__":main()
