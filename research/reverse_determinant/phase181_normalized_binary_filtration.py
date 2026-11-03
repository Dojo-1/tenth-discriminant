#!/usr/bin/env python3
"""Phase181: source-exact normalized 2-primary filtration, finite only.

The original ordinary-Z jet E and unchanged trace weights B=2C are used.
Phase162 supplies a monic integral row operation U with UE=Delta N,
Delta_ii=2^(floor(r/4)), so det(G)=2^Lambda1 det(N C N.T).
Only the residual Gram is tested for additional binary factors. The
existing valuation lower must not be counted again. No new field bound.
"""
from __future__ import annotations

from math import comb

from phase159_observation_continuum import ordinary_effective, pairmul, powers
from phase159_padic_gram import gram_mod_2_power, smith_exponents_2
from phase180_binary_hull import binary_rank


def lambda1(R: int, S: int) -> int:
    return R*S + 2*S*sum(r//4 for r in range(R))


def source_normalize(E, R: int, S: int):
    """Exactly Phase162's triangular monic F_r(Z) basis; integer quotient."""
    assert len(E) == R*S
    width = len(E[0])
    assert all(len(row) == width for row in E)
    N = []
    exponents = []
    for r in range(R):
        k = r//4
        assert all(0 <= r-2*t < r for t in range(1,k+1))
        coeff = [(-1)**t * comb(k,t) for t in range(k+1)]
        for s in range(S):
            transformed = [sum(c*E[(r-2*t)*S+s][col]
                               for t,c in enumerate(coeff))
                           for col in range(width)]
            divisor = 1<<k
            assert all(v % divisor == 0 for v in transformed), (r,s,k)
            N.append([v//divisor for v in transformed])
            exponents.append(k)
    assert R*S + 2*sum(exponents) == lambda1(R,S)
    return N, exponents


def polynomial_reference(Q, D, R, S, N):
    """Second evaluator: formal polynomial derivatives before point values.

    Checks the ordinary-jet row basis without reconstructing it by
    the same linear combinations of E rows used by source_normalize.
    """
    from sympy import Poly, Symbol
    z = Symbol("z")
    polys = [Poly(z**(r-4*(r//4)) * (z**4-z**2)**(r//4), z)
             for r in range(R)]
    column = 0
    for x,y in Q:
        zpair = (x,y)
        w_powers = powers((x,-y),S-1,D)
        for j in range(S):
            for r in range(R):
                derivative = polys[r].diff((0,j))
                coeffs = derivative.all_coeffs()
                value = (0,0)
                for c in coeffs:
                    value = pairmul(value,zpair,D)
                    value = (value[0]+int(c),value[1])
                for s in range(S):
                    i = r*S+s
                    result = pairmul(value,w_powers[s],D)
                    divisor = 1<<(r//4)
                    assert all(v % divisor == 0 for v in result)
                    assert N[i][column] == result[0]//divisor
                    if y:
                        assert N[i][column+1] == result[1]//divisor
            column += 1 + (y!=0)
    assert column == len(N[0])


def smith_profile(A, K=64):
    exponents,unknown = smith_exponents_2(A,K)
    assert unknown == 0, ("precision censored",K,unknown)
    assert len(exponents) == len(A) and max(exponents) < K
    valuation = sum(exponents)
    barcode = [sum(e>=t for e in exponents)
               for t in range(1,max(exponents)+1)]
    assert valuation == sum(barcode)
    assert barcode == sorted(barcode,reverse=True)
    return valuation,barcode,exponents


def row_shear_on_gram(H, K=64):
    """Unimodular row shear H -> UHU.T; determinant/Smith unchanged."""
    mod = 1<<K
    B = [list(row) for row in H]
    for j in range(len(B)):
        B[0][j] = (B[0][j]+B[1][j])%mod
    for i in range(len(B)):
        B[i][0] = (B[i][0]+B[i][1])%mod
    return B


def check(Q,D,R,S,expected,*,reference=False,gauge=False):
    m = R*S
    E,weights,_ = ordinary_effective(Q,D,R,S)
    assert D%2 == 1 and len(E) == m
    assert all(w in (2,2*D) for w in weights)
    N,exponents = source_normalize(E,R,S)
    if reference:
        polynomial_reference(Q,D,R,S,N)
    C = [w//2 for w in weights]
    assert all(c%2 == 1 for c in C)
    H = gram_mod_2_power(N,C,64)
    rank_N = binary_rank(N)
    rank_H = binary_rank(H)
    hull = rank_N-rank_H
    assert hull >= 0
    n1 = m-rank_H
    assert n1 == (m-rank_N)+hull
    residual,barcode,invariants = smith_profile(H)
    assert n1 == (barcode[0] if barcode else 0)
    observed = (m,lambda1(R,S),rank_N,rank_H,n1,residual)
    assert observed == expected, (Q,D,observed,expected)

    # Original and normalized Smith valuations are compared on exactly
    # the same support, unmodified metric, and original row source.
    G = gram_mod_2_power(E,weights,64)
    original,_,_ = smith_profile(G)
    assert original == lambda1(R,S)+residual, (D,R,S,original,residual)
    if gauge:
        Hg = row_shear_on_gram(H)
        assert smith_profile(Hg)[:2] == (residual,barcode)
        Ng = [row.copy() for row in N]
        Ng[0] = [a+b for a,b in zip(N[0],N[1])]
        assert binary_rank(Ng) == rank_N
        assert binary_rank(Hg) == rank_H

    print("PHASE181_RESIDUAL",dict(
        D=D,R=R,S=S,points=len(Q),channels=len(weights),
        lambda1=lambda1(R,S),original_v2=original,
        residual_v2=residual,rank_N=rank_N,rank_H=rank_H,
        hull=hull,n1=n1,top_smith=max(invariants),
        layers=len(barcode),first_layers=barcode[:8]),flush=True)
    return barcode


def main():
    # Phase180 A/B: equal full rank of original rows, unequal hulls.
    C = [(0,2)]
    check(C+[(-2,1)],3,2,2,(4,4,4,3,1,1),
          reference=True,gauge=True)
    check(C+[(-1,0)],3,2,2,(4,4,4,4,0,0),
          reference=True,gauge=True)

    # Historical six-point integer-image witness, D=19 (not a field cutoff).
    six = [(-2,-1),(-1,-1),(-1,0),(0,-1),(0,0),(1,-1)]
    check(six,19,8,4,(32,64,16,8,24,102),
          reference=True,gauge=True)

    D,R,S = 163,30,5
    full = [(x,0) for x in range(-13,14)]+[(x,1) for x in range(-2,3)]
    real = sorted((q for q in full if q[1]==0),
                  key=lambda q:(abs(q[0]),q[0]))[:21]
    nonreal = sorted((q for q in full if q[1]!=0),
                     key=lambda q:(q[0]*q[0]+D,abs(q[0]),q[0]))
    chosen = real+nonreal
    assert len(chosen) == 26
    cases = [
        (None,(150,1130,16,12,138,2057)),
        ((0,0),(150,1130,16,8,142,2070)),
        ((10,0),(150,1130,16,8,142,2046)),
    ]
    barcodes = []
    for removed,expected in cases:
        Q = [q for q in chosen if q != removed]
        barcodes.append(check(Q,D,R,S,expected))
    # Equal first-layer ranks fail to determine deeper valuations.
    assert barcodes[1][0] == barcodes[2][0] == 142
    assert sum(barcodes[1]) == 2070 and sum(barcodes[2]) == 2046
    print("PHASE181_SOURCE_NORMALIZED_FILTRATION_PASS: finite only",
          flush=True)


if __name__ == "__main__":
    main()
