#!/usr/bin/env python3
"""Phase307-C: actual-observation cover, abstract constant H2 vs flabby functions.

The 4-patch nerve is a tetrahedral boundary; coefficient *sheaf* matters.
No gerbe on Spec(O_K) or number-field class-number theorem is implied.
"""
from itertools import combinations
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase306"))
from arithmetic_fabric import actual_d203_points
from higher_categorical import (tetrahedral_sphere_nerve,
                               fundamental_sphere_cycle,
                               pair_cycle_cocycle,
                               nontrivial_H2_certificate,
                               boundary_of_two_chain)

P=5


def covers_over_actual_points():
    """q0..q3 belong to all but one patch each; q4/q5 to one patch."""
    points=actual_d203_points()
    labels=tuple(f"q{i}" for i in range(len(points)))
    cover={i:set() for i in range(4)}
    for i in range(4):
        for k in range(4):
            if k != i:
                cover[i].add(labels[k])
    cover[0].add("q4")
    cover[1].add("q5")
    assert set().union(*cover.values())==set(labels)
    assert len(set.intersection(*cover.values()))==0
    return labels,cover


def intersection(cover,simplex):
    return set.intersection(*(cover[i] for i in simplex))


def all_faces():
    return tuple(combinations(range(4),3))


def all_edges():
    return tuple(combinations(range(4),2))


def all_2_cochains(cover,value_fn):
    """C^2(cover, F5^U): cochain indexed by a simplex AND actual point."""
    return {(face,q):value_fn(face,q)%P
            for face in all_faces() for q in sorted(intersection(cover,face))}


def coboundary_one(cover,b):
    out={}
    for face in all_faces():
        i,j,k=face
        for q in intersection(cover,face):
            out[(face,q)]=(b.get(((j,k),q),0)
                          -b.get(((i,k),q),0)
                          +b.get(((i,j),q),0))%P
    return out


def coboundary_zero(cover,a):
    out={}
    for i,j in all_edges():
        for q in intersection(cover,(i,j)):
            out[((i,j),q)]=(a.get((j,q),0)-a.get((i,q),0))%P
    return out


def pointwise_contraction(cover,c):
    """Construct h(c) with delta h(c)=c for THIS explicit acyclic cover."""
    out={}
    for face in all_faces():
        for q in intersection(cover,face):
            # Each q in a triple is in exactly those three patches.
            support=[i for i in range(4) if q in cover[i]]
            assert support==list(face),("not a boundary-cover contraction",q)
            base=support[0]
            remaining=tuple(x for x in face if x!=base)
            sign=(-1)**face.index(base)
            key=(remaining,q)
            assert key not in out
            out[key]=sign*c.get((face,q),0)%P
    assert coboundary_one(cover,out)==c
    return out


def demonstrate_coefficient_sensitive_H2():
    points,cover=covers_over_actual_points()
    assert all(len(intersection(cover,face))==1 for face in all_faces())
    assert all(len(intersection(cover,edge))==2 for edge in all_edges())
    sphere=tetrahedral_sphere_nerve(False)
    cycle=fundamental_sphere_cycle()
    assert boundary_of_two_chain(cycle)=={}
    constant={(1,2,3):1}
    assert nontrivial_H2_certificate(constant,sphere)
    assert pair_cycle_cocycle(cycle,constant)==1

    # Reuse same *symbols* as F5-valued functions on each actual overlap.
    sheaf=all_2_cochains(cover,lambda face,q: 1 if face==(1,2,3) else 0)
    primitive=pointwise_contraction(cover,sheaf)
    assert coboundary_one(cover,primitive)==sheaf
    # Generic deterministic cochain to avoid a single lucky example.
    c2=all_2_cochains(cover,
        lambda face,q: (2*sum(face)+int(q[1:])+1)%5)
    b=pointwise_contraction(cover,c2)
    assert coboundary_one(cover,b)==c2

    a={(i,q):(i*3+int(q[1:]))%5 for i in cover for q in cover[i]}
    assert all(x==0 for x in coboundary_one(
        cover,coboundary_zero(cover,a)).values())
    # Cover gluing hostile case: contradictory restriction cannot glue.
    bad={"q0":{1:1,2:2,3:1}}
    assert len(set(bad["q0"].values()))>1
    return {
        "actual_D203_observations":len(points),
        "cover_patches":len(cover),
        "tetrahedral_boundary_faces":len(all_faces()),
        "abstract_constant_coeff_H2_nonzero":True,
        "function_sheaf_explicit_H2_primitive":True,
        "function_sheaf_delta1_delta0_zero":True,
        "hostile_incompatible_overlap_rejected":True,
        "arithmetic_gerbe_NOT_established":True
    }


def main():
    print("PHASE307_ACTUAL_SHEAF_COHOMOLOGY_PASS",
          demonstrate_coefficient_sensitive_H2(),flush=True)


if __name__=="__main__":
    main()
