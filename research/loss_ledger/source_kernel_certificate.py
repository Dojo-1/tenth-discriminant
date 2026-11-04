#!/usr/bin/env python3
"""Round201 post-preregistered exact modular-kernel witness for original jet Grams.

Produces canonical mod-3 nullspaces by deterministic RREF. Do not mistake
their bases for basis-independent matrices or infer a uniform field bound.
"""
import json
from pathlib import Path
import sys


def rref(a, p):
    r = [[int(x) % p for x in row] for row in a]
    nrows = len(r)
    ncols = len(r[0]) if r else 0
    pivots = []
    pivotrow = 0
    for col in range(ncols):
        cand = next((i for i in range(pivotrow, nrows) if r[i][col] % p), None)
        if cand is None:
            continue
        r[pivotrow], r[cand] = r[cand], r[pivotrow]
        inv = pow(r[pivotrow][col], -1, p)
        r[pivotrow] = [(x*inv)%p for x in r[pivotrow]]
        for i in range(nrows):
            if i != pivotrow:
                c = r[i][col]
                if c:
                    r[i] = [(x-c*y)%p for x,y in zip(r[i],r[pivotrow])]
        pivots.append(col)
        pivotrow += 1
        if pivotrow == nrows:
            break
    return r, pivots


def nullspace(a,p):
    rows,pivots=rref(a,p)
    ncols=len(a[0])
    free=[i for i in range(ncols) if i not in pivots]
    vectors=[]
    for j in free:
        v=[0]*ncols
        v[j]=1
        for pivotrow, pivotcol in enumerate(pivots):
            v[pivotcol]=(-rows[pivotrow][j])%p
        assert not any(sum(a[i][k]*v[k] for k in range(ncols))%p
                       for i in range(len(a)))
        vectors.append(v)
    return pivots,free,vectors


def outside_kernel(a,v,p):
    return [sum(a[i][j]*v[j] for j in range(len(v)))%p
            for i in range(len(a))]


def source_test():
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"plural_moving_frames"))
    from original_source_small_pilot import gram, ellipse, determinant, D, R, S, J
    assert (D,R,S,J)==(19,4,3,3)
    g5=gram(ellipse(5));g6=gram(ellipse(6))
    assert determinant(g5)>0 and determinant(g6)>0
    piv5,free5,k5=nullspace(g5,3)
    piv6,free6,k6=nullspace(g6,3)
    assert (len(piv5),len(piv6))==(10,9)
    assert (len(k5),len(k6))==(2,3)
    # A particular relation belongs to the added-observation Gram kernel,
    # but fails on the smaller support. Not an invariance or inclusion theorem.
    extra=next((v for v in k6 if any(outside_kernel(g5,v,3))),None)
    assert extra is not None
    assert all(x==0 for x in outside_kernel(g6,extra,3))
    y5=outside_kernel(g5,extra,3)
    assert any(y5)
    # Verify the kernel dimension via an independent check from nonzero minors
    # only in dimension 2? Here rely on the deterministic RREF rank certificate:
    # exact modular row operations, explicit pivot columns and null vectors.
    return {
        "parameter":{"D":D,"R":R,"S":S,"J":J,"p":3},
        "radii":[5,6],
        "pivot_indices_zero_based":{"radius5":piv5,"radius6":piv6},
        "free_indices_zero_based":{"radius5":free5,"radius6":free6},
        "nullspace_basis":{"radius5":k5,"radius6":k6},
        "witness_kernel_radius6_not_radius5":extra,
        "witness_G5_product_mod3":y5,
        "witness_G6_product_mod3":outside_kernel(g6,extra,3)
    }


if __name__=="__main__":
    print(json.dumps(source_test(),indent=2))
    print("ROUND201_EXACT_SOURCE_NULLSPACE_PASS")
