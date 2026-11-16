#!/usr/bin/env python3
"""Phase329: Reidemeister/Hurwitz knot transport on finite conjugacy data.

For ANY group G, the quandle operation is x ▷ y = y^(-1) x y.
The positive Hurwitz generator on adjacent factors is

   R(x,y) = (x*y*x^(-1),x).

It preserves product x*y and the multiset of conjugacy classes,
satisfies the Yang–Baxter/braid relation, and has inverse
R^-1(u,v)=(v,v^(-1)*u*v).

The fixed points of R^k on G^2 count group-conjugation quandle
colorings of the closure of the two-strand braid sigma_1^k. Those
counts are knot/link invariants, NOT complete invariants.

Use S3 as a discriminating positive control (trefoil 12 colorings
vs 6 for unknot), and Phase328's toy H48 as a matched NULL
(trefoil and unknot both 48). No claim that actual H_D
distinguishes the trefoil is made.

Actual Frobenius classes are elements of a finite Galois group modulo
conjugation. These moves preserve conjugacy, not the original
ordinary-Z jet metric. The transport lives in its own fiber.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from pathlib import Path
import sys
from typing import Callable,Any

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))
from tapestry import H, HE, h_mul, sigma  # noqa: E402

S3=tuple(permutations((0,1,2)))
S3_UNIT=(0,1,2)


def perm_mul(a:tuple[int,...],b:tuple[int,...])->tuple[int,...]:
    return tuple(a[b[i]] for i in range(len(a)))


def perm_inverse(a:tuple[int,...])->tuple[int,...]:
    return tuple(a.index(i) for i in range(len(a)))


def toy_h_inverse(x):
    g,e=x
    negative=((-g[0])%4,(-g[1])%6)
    return (sigma(negative) if e else negative,e)


@dataclass(frozen=True)
class FiniteGroup:
    name: str
    members: tuple[Any,...]
    unit: Any
    mul: Callable[[Any,Any],Any]
    inv: Callable[[Any],Any]

    def validate(self):
        universe=set(self.members)
        assert self.unit in universe
        for x in self.members:
            assert self.mul(self.unit,x)==x
            assert self.mul(x,self.unit)==x
            assert self.mul(x,self.inv(x))==self.unit
            assert self.mul(self.inv(x),x)==self.unit
        return True


S3_GROUP=FiniteGroup("S3",S3,S3_UNIT,perm_mul,perm_inverse)
TOY_H48=FiniteGroup("phase328_toy_H48",H,HE,h_mul,toy_h_inverse)


def q_conjugate(x,y,G:FiniteGroup):
    """x ▷ y = y^-1 x y."""
    return G.mul(G.mul(G.inv(y),x),y)


def q_inverse_conjugate(x,y,G:FiniteGroup):
    """Inverse right action: y x y^-1."""
    return G.mul(G.mul(y,x),G.inv(y))


def hurwitz_positive(x,y,G:FiniteGroup):
    return (q_inverse_conjugate(y,x,G),x)


def hurwitz_negative(x,y,G:FiniteGroup):
    return (y,q_conjugate(x,y,G))


def braid_generator(tup:tuple, index:int, sign:int, G:FiniteGroup):
    if index<0 or index+1>=len(tup):
        raise ValueError("Invalid braid index")
    if sign not in (-1,1):
        raise ValueError("Sign must be positive or negative")
    a,b=tup[index:index+2]
    x,y=(hurwitz_positive(a,b,G) if sign==1
         else hurwitz_negative(a,b,G))
    out=list(tup)
    out[index],out[index+1]=x,y
    return tuple(out)


def braid_word(tup:tuple,word:tuple[int,...],G:FiniteGroup):
    """Signed 1-based braid indices, as in sigma_i."""
    out=tup
    for generator in word:
        if generator==0:
            raise ValueError("Braid generator cannot be zero")
        out=braid_generator(out,abs(generator)-1,
                            1 if generator>0 else -1,G)
    return out


def group_product(tup:tuple,G:FiniteGroup):
    acc=G.unit
    for x in tup:
        acc=G.mul(acc,x)
    return acc


def are_conjugate(x,y,G:FiniteGroup)->bool:
    return any(
        G.mul(G.mul(z,x),G.inv(z))==y
        for z in G.members
    )


def closure_coloring_count(G:FiniteGroup,power:int,
                           colors:tuple|None=None)->dict:
    """Fixed tuples for closure of sigma_1^power, power >= 1 odd."""
    if power<1 or power%2==0:
        raise ValueError("Only odd positive 2-strand knot closures")
    colors=G.members if colors is None else colors
    color_set=set(colors)
    assert len(color_set)==len(colors)
    count=nonconstant=0
    for x in colors:
        for y in colors:
            changed=braid_word((x,y),(1,)*power,G)
            if changed==(x,y):
                count+=1
                if x!=y:
                    nonconstant+=1
    return {"group":G.name,"power":power,
            "colors":len(colors),"fixed_colorings":count,
            "nonconstant_colorings":nonconstant}


def two_strand_alexander(power:int)->tuple[int,...]:
    """Normalized Alexander polynomial of T(2,k), k positive odd.

    Reduced Burau for B2 sends sigma_1 to -t. The ratio
      (1-(-t)^k)/(1+t) = (1+t^k)/(1+t)
    has coefficients +1,-1,+1,...,+1 for odd k.
    This is a known knot invariant for this specific family,
    *not* an algorithm computing all knot polynomials.
    """
    if power<1 or power%2==0:
        raise ValueError("Power must be odd positive for a knot")
    return tuple(1 if j%2==0 else -1 for j in range(power))


def alexander_eval(coeffs:tuple[int,...],t:int)->int:
    return sum(c*(t**i) for i,c in enumerate(coeffs))


def full_inert_coset()->tuple:
    """Rational inert Frobenius has e=1 in H48 toy semidirect group."""
    return tuple(h for h in H if h[1]==1)


if __name__=="__main__":
    import json
    rows=[closure_coloring_count(g,k)
          for g in (S3_GROUP,TOY_H48) for k in (1,3,5)]
    print("PHASE329_BRAID_KNOT_PASS",
          json.dumps(rows,sort_keys=True),flush=True)
