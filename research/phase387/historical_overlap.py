#!/usr/bin/env python3
"""Matched-source no-double-count audit for Phase387 residue Smith floors.

The older Smith histograms are repository-published measured baselines;
this script independently recomputes ellipse residue occupancies. It does
NOT reproduce the historical Smith elimination or prove a new field bound.
"""
from math import isqrt

HISTORIES = (
    (283,31,70,2,2,3,527,{0:36,1:9,2:9,4:36,5:9,6:9,8:31,9:1}),
    (403,40,100,4,4,3,840,{0:90,1:36,2:18,3:256}),
    (403,40,100,4,4,5,435,{0:240,1:15,2:15,3:130}),
    (283,31,70,2,2,5,195,None),
)

def original_points(D,rho):
    Y=isqrt(rho*rho//D)
    return [(x,y) for y in range(-Y,Y+1)
            for x in range(-isqrt(rho*rho-D*y*y),
                           isqrt(rho*rho-D*y*y)+1)]

def count_class_by_points(Q,q):
    return len({(x%q,y%q) for x,y in Q})

def count_class_by_slices(D,rho,q):
    bins={}
    Y=isqrt(rho*rho//D)
    for y in range(-Y,Y+1):
        L=isqrt(rho*rho-D*y*y)
        for rx in range(q):
            first=-L+(rx+L)%q
            if first<=L:bins.setdefault(y%q,set()).add(rx)
    return sum(map(len,bins.values()))

def is_inert(D,p):
    return pow((-D)%p,(p-1)//2,p)==p-1

def main():
    assert is_inert(283,3) and is_inert(283,5)
    assert is_inert(403,3) and is_inert(403,5)
    assert not is_inert(403,11) # split-prime guard
    for D,rho,R,S,J,p,known,history in HISTORIES:
        Q=original_points(D,rho); n=R*S
        if history is not None:
            assert sum(history.values())==n
            assert sum(e*c for e,c in history.items())==known
        cumulative=0
        details=[]
        for depth in range(1,5):
            q=p**(depth+1)
            occupied=count_class_by_points(Q,q)
            assert occupied==count_class_by_slices(D,rho,q)
            floor=max(0,n-2*J*occupied)
            if history is not None and (depth<=3 or (D,p)==(283,3)):
                tail=sum(c for e,c in history.items() if e>=depth)
                assert tail>=floor,(D,p,depth,tail,floor)
            cumulative+=floor
            details.append((depth,occupied,floor))
        assert cumulative<=known,(D,p,cumulative,known)
        print(f"D={D} p={p} Q={len(Q)} n={n} "
              f"Phase387 index floor={cumulative} "
              f"older source index={'exact ' if D==283 else 'at least '}{known}")
        print("   depth, occupied classes, certified floor:",details)
        if p==3:
            actual_rank=history[0]
            class_cap=2*J*details[0][1]
            assert actual_rank<class_cap
            print("   exact original normalized rank mod3:",actual_rank,
                  "vs occupied-class cap:",class_cap)
    print("PASS matched-source historical replay: zero additive extra units")

if __name__=="__main__":main()
