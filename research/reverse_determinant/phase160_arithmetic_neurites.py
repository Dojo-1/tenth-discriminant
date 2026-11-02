#!/usr/bin/env python3
"""Phase160: exact arithmetic-neurite gluing for the ORIGINAL ordinary-jet Gram.

Finite reproducible controls, not a new field bound, Spin theorem or
independent mathematical referee. Reuses the Phase159 source evaluator.
"""
from fractions import Fraction
from itertools import combinations
from math import isqrt
from random import Random
from sympy import Matrix, diag
from sympy.matrices.normalforms import hermite_normal_form
from phase159_observation_continuum import ordinary_effective


def index_and_gram(A, weights):
    assert A.rank() == A.rows
    d = abs(int(hermite_normal_form(A).det()))
    g = int((A * diag(*weights) * A.T).det())
    assert g > 0 and g % (d*d) == 0
    return d, g, g//(d*d)


def from_columns(cols, weights):
    return index_and_gram(Matrix.hstack(*(Matrix(c) for c in cols)), weights)


def from_source(Q, D=3, R=2, S=2):
    E, weights, _ = ordinary_effective(Q, D, R, S)
    return index_and_gram(Matrix(E), weights)


def vq(n, p):
    assert n != 0
    n = abs(n); v = 0
    while n % p == 0:
        n //= p; v += 1
    return v


def diamond(a, b, intersection, union):
    # Each triple is (integer-lattice index, original detG, detG/index^2).
    i, g, h = zip(intersection, a, b, union)
    assert i[0]*i[3] % (i[1]*i[2]) == 0
    rem = i[0]*i[3] // (i[1]*i[2])
    assert rem >= 1
    assert g[1]*g[2] >= g[0]*g[3]
    assert h[1]*h[2] >= h[0]*h[3]
    assert Fraction(h[1]*h[2], h[0]*h[3]) == (
        Fraction(g[1]*g[2], g[0]*g[3]) * rem*rem)
    return rem


def weighted_minors(A, weights, p=2):
    assert A.cols == len(weights)
    terms = []
    for I in combinations(range(A.cols), A.rows):
        determinant = int(A[:, list(I)].det())
        if determinant == 0:
            continue
        term = determinant*determinant
        for j in I:
            term *= weights[j]
        terms.append(term)
    assert terms
    minimum = min(vq(t,p) for t in terms)
    critical = sum(vq(t,p) == minimum for t in terms)
    determinant = int((A*diag(*weights)*A.T).det())
    assert sum(terms) == determinant
    actual = vq(determinant,p)
    assert actual >= minimum
    if p == 2:
        assert (critical % 2 == 1) == (actual == minimum)
    return minimum, critical, actual


def source_case():
    base = [(0,2)]
    left = base + [(-2,1)]
    right = base + [(-1,0)]
    both = base + [(-2,1),(-1,0)]
    values = [from_source(Q) for Q in (base,left,right,both)]
    assert values == [
        (4,2304,144),
        (1,122656,122656),
        (1,74896,74896),
        (1,622368,622368)]
    rem = diamond(values[1],values[2],values[0],values[3])
    assert rem == 4  # Z/2 x Z/2, checked by source Smith normal form
    expected = [(8,1,8),(4,6,5),(4,1,4),(4,34,5)]
    for Q,want in zip((base,left,right,both),expected):
        E,weights,_ = ordinary_effective(Q,3,2,2)
        assert weighted_minors(Matrix(E), weights) == want
    print("PHASE160_SOURCE_GLUE_PASS",dict(
        intersection=base,arms=(left,right),
        lattice_indices=[v[0] for v in values],remainder_order=rem,
        plucker_2adic=expected),flush=True)


def source_sweep():
    base=[(0,2)]
    choices=[(x,y) for x in range(-2,3) for y in range(3)
             if (x,y)!=(0,2) and x*x+3*y*y<=20]
    overlap=from_source(base)
    nontrivial=0
    for a,b in combinations(choices,2):
        rem=diamond(from_source(base+[a]),from_source(base+[b]),
                    overlap,from_source(base+[a,b]))
        nontrivial += int(rem>1)
    assert len(list(combinations(choices,2)))==91
    assert nontrivial==36
    print("PHASE160_SOURCE_DIAMONDS_PASS",
          dict(tested=91,nontrivial_gluing=nontrivial),flush=True)


def independent_controls():
    # Integral overlap R=(4Z)/(12Z)=Z/3.
    cols={"a":(12,),"b":(2,),"c":(4,)}
    def rec(labels):
        return from_columns([cols[x] for x in labels],[2]*len(labels))
    overlap,left,right,union=map(rec,("a","ab","ac","abc"))
    assert (overlap,left,right,union)==(
        (12,288,2),(2,296,74),(4,320,20),(2,328,82))
    assert diamond(left,right,overlap,union)==3
    assert Fraction(left[1]*right[1],overlap[1]*union[1])==Fraction(370,369)
    assert Fraction(left[2]*right[2],overlap[2]*union[2])==Fraction(370,41)
    assert vq(3,3)==1
    # Parity of minimal Plucker contributions, not factorial floor.
    for rows,want in [
        ([[1,0,1],[0,1,2]],(2,2,3)),
        ([[1,0,1],[0,1,1]],(2,3,2))]:
        assert weighted_minors(Matrix(rows),[2]*3)==want
    # Same cokernel does not imply rational quadratic-form isometry.
    A=Matrix([[1,0,1],[0,1,1]])
    old=index_and_gram(A[:,[0,1]],[2,2])
    new=index_and_gram(A,[2,2,2])
    assert old[:2]==(1,4) and new[:2]==(1,12)
    assert new[1]//old[1]==3 and isqrt(3)**2!=3
    print("PHASE160_TORSION_PARITY_SPIN_OBSTRUCTION_PASS",flush=True)


def diamond_sweep():
    rng=Random(160)
    passed=0
    for _ in range(100):
        vectors=[]
        while len(vectors)<4:
            v=(rng.randrange(-6,7),rng.randrange(-6,7))
            if v!=(0,0):vectors.append(v)
        if Matrix.hstack(Matrix(vectors[0]),Matrix(vectors[1])).det()==0:
            continue
        # Weights are indexed by global label. Reassigning a shared weight
        # across supports invalidates the real submodularity comparison.
        w=[2,6,2,6]
        c=from_columns(vectors[:2],w[:2])
        a=from_columns(vectors[:3],w[:3])
        b=from_columns([vectors[j] for j in (0,1,3)],
                       [w[j] for j in (0,1,3)])
        u=from_columns(vectors,w)
        diamond(a,b,c,u)
        passed+=1
    assert passed==98
    print("PHASE160_RANDOM_DIAMONDS_PASS",passed,flush=True)


if __name__=="__main__":
    source_case()
    source_sweep()
    independent_controls()
    diamond_sweep()
    print("PHASE160_ARITHMETIC_NEURITES_PASS: bounded finite only",flush=True)
