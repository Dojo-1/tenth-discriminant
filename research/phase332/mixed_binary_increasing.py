"""Phase332 — guarded mixed binary source-basis pilot (exact integers).

Candidate polynomial at original monomial (r,s):
    Z^(r-4k-2b) W^(s-4c)
      (Z^4-Z^2)^k (Z^2-W^2)^b (W^4-W^2)^c

where b=min(r//2,(S-1-s)//2), k=(r-2b)//4, c=s//4.
W is held fixed for ALL ordinary Z derivatives.

Facts checked here:
  * every monomial stays in the original R by S rectangle;
  * the coefficient matrix is integral, lower triangular, diagonal 1;
  * every source ordinary jet has 2^(k+b+c) in both integer coordinates;
  * row exponents improve on the Phase331 bidirectional basis;
  * for R>=S-1, new row mass exceeds old by at least
      (R-S+1)*sum_{t<S} floor(t/4).

All tests are bounded M evidence, NOT a universal Lean proof or
the claimed 313^4 field bound. No Work or external computation.
"""
from __future__ import annotations

from functools import lru_cache
from math import factorial
from typing import Dict
import unittest

Pair = tuple[int,int]
Mono = tuple[int,int]


def add(a:Pair,b:Pair)->Pair:
    return a[0]+b[0],a[1]+b[1]


def mul(D:int,a:Pair,b:Pair)->Pair:
    return a[0]*b[0]-D*a[1]*b[1],a[0]*b[1]+a[1]*b[0]


@lru_cache(maxsize=None)
def power(D:int,a:Pair,n:int)->Pair:
    assert n>=0
    acc=(1,0)
    while n:
        if n&1:acc=mul(D,acc,a)
        a=mul(D,a,a)
        n//=2
    return acc


def falling(r:int,j:int)->int:
    return factorial(r)//factorial(r-j) if j<=r else 0


def exponents(r:int,s:int,S:int)->tuple[int,int,int]:
    if r<0 or s<0 or not 0<=s<S:raise ValueError((r,s,S))
    b=min(r//2,(S-1-s)//2)
    k=(r-2*b)//4
    c=s//4
    return k,b,c


def multiply_factor(poly:Dict[Mono,int],
                    terms:tuple[tuple[int,int,int],...])->Dict[Mono,int]:
    nxt:Dict[Mono,int]={}
    for (r,s),coefficient in poly.items():
        for dr,ds,m in terms:
            key=(r+dr,s+ds)
            nxt[key]=nxt.get(key,0)+coefficient*m
    return {k:v for k,v in nxt.items() if v}


@lru_cache(maxsize=None)
def polynomial(r:int,s:int,S:int)->tuple[tuple[Mono,int],...]:
    k,b,c=exponents(r,s,S)
    poly:Dict[Mono,int]={(r-4*k-2*b,s-4*c):1}
    assert r-4*k-2*b>=0 and s-4*c>=0
    for _ in range(k):
        poly=multiply_factor(poly,((4,0,1),(2,0,-1)))
    for _ in range(b):
        poly=multiply_factor(poly,((2,0,1),(0,2,-1)))
    for _ in range(c):
        poly=multiply_factor(poly,((0,4,1),(0,2,-1)))
    return tuple(sorted(poly.items()))


def source_jet(D:int,z:Pair,w:Pair,poly:tuple[tuple[Mono,int],...],
               j:int)->Pair:
    total=(0,0)
    for (r,s),coefficient in poly:
        if r<j:continue
        term=mul(D,power(D,z,r-j),power(D,w,s))
        total=add(total,(coefficient*falling(r,j)*term[0],
                         coefficient*falling(r,j)*term[1]))
    return total


def floor_mass(q:int,S:int)->int:
    a,b=divmod(S,q)
    return q*a*(a-1)//2+a*b


class GuardedMixedBinaryTests(unittest.TestCase):
    def test_unimodular_lower_triangular_rows(self):
        for R in range(1,17):
            for S in range(1,17):
                for r in range(R):
                    for s in range(S):
                        values=dict(polynomial(r,s,S))
                        self.assertEqual(values.get((r,s)),1)
                        self.assertTrue(all(0<=u<R and 0<=v<S
                                            for u,v in values))
                        self.assertTrue(all(u*S+v<=r*S+s
                                            for u,v in values))
                        self.assertTrue(all((u,v)==(r,s) or
                                            u*S+v<r*S+s
                                            for u,v in values))

    def test_joint_all_original_ordinary_jets(self):
        count=0
        for D in (1,2,3,163):
            for x in range(-2,3):
                for y in range(-2,3):
                    z,w=(x,y),(x,-y)
                    for r in range(10):
                        for s in range(10):
                            poly=polynomial(r,s,10)
                            k,b,c=exponents(r,s,10)
                            for j in range(8):
                                a=source_jet(D,z,w,poly,j)
                                f=1<<(k+b+c)
                                self.assertEqual(a[0]%f,0,(D,x,y,r,s,j))
                                self.assertEqual(a[1]%f,0,(D,x,y,r,s,j))
                                count+=1
        self.assertEqual(count,80000)

    def test_new_exponent_dominates_previous_source_basis(self):
        for R in range(1,30):
            for S in range(1,26):
                for r in range(R):
                    for s in range(S):
                        k,b,c=exponents(r,s,S)
                        self.assertGreaterEqual(k+b+c,r//4+s//4)

    def test_new_mass_has_positive_second_horizontal_scale(self):
        for S in range(1,22):
            for R in range(max(1,S-1),40):
                extra=sum(exponents(r,s,S)[0]+
                          exponents(r,s,S)[1]+
                          exponents(r,s,S)[2]-(r//4+s//4)
                          for r in range(R) for s in range(S))
                self.assertGreaterEqual(extra,
                    (R-S+1)*floor_mass(4,S),(R,S,extra))
        # Large-endpoint asymptotic check, not a proof for all D.
        R=315**4//4
        S=R//25
        self.assertGreaterEqual(R-S+1,0)
        self.assertGreater(floor_mass(4,S),0)

    def test_negative_naive_W_square_minus_W(self):
        # Universal W-only quadratic W²-W is invalid at non-real
        # source samples in the dual-number residue order mod 2.
        D=3
        w=(0,-1)
        w2=power(D,w,2)
        wrong=(w2[0]-w[0],w2[1]-w[1])
        self.assertNotEqual(wrong[1]%2,0)

if __name__=="__main__":
    unittest.main(verbosity=2)
