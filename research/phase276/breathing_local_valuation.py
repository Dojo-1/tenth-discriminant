#!/usr/bin/env python3
"""Exact negative control: Loewner support growth need not raise p-adic mass.

Uses the existing ordinary-Z source evaluator from Phase204 and an
independently implemented lattice-ellipse/cardinality computation.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase204"))
from ordinary_jet_filtration import gramstep

D = 163
P = (3, 5)


def ellipse(rho):
    return [(x,y) for x in range(-rho,rho+1)
             for y in range(-rho,rho+1)
             if x*x+D*y*y<=rho*rho]


def valuation(n,p):
    assert n > 0
    k=0
    while n%p==0:
        k+=1
        n//=p
    return k


def main():
    source_sets = [set(ellipse(rho)) for rho in (1,2,3)]
    assert source_sets[0]<source_sets[1]<source_sets[2]
    results=[]
    for rho,Q in zip((1,2,3),source_sets):
        source=gramstep(sorted(Q),D,1,1,0)
        assert len(source)==1 and len(source[0])==1
        det=source[0][0]
        assert det==2*len(Q)  # independent algebraic source expectation
        results.append((rho,len(Q),det,valuation(det,3),valuation(det,5)))
    assert results==[(1,3,6,1,0),(2,5,10,0,1),(3,7,14,0,0)]
    assert (-D)%3==2 and (-D)%5==2
    assert all(p < D/4 for p in P)
    assert results[0][2]<results[1][2]<results[2][2]
    assert results[0][3]>results[1][3] # p3 falls
    assert results[0][4]<results[1][4] # p5 rises
    assert results[1][4]>results[2][4] # p5 falls
    for row in results:
        print("rho,count,det,v3,v5 =",*row,sep=" ")
    print("PASS: same-original-source breathing has opposite inert p-depth changes")


if __name__=="__main__":
    main()
