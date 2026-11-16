#!/usr/bin/env python3
"""Phase330: cyclic H1 and Tate H0 bridge to actual Frobenius square fibers.

For finite abelian ray group G with involution sigma:
  N = 1 + sigma, D = 1 - sigma,
  H1(C2,G) = ker(N) / D(G),
  Tate H0(C2,G) = G^sigma / N(G).

Rational inert Frobenius classes in G*sigma are G/D(G).
Their squares map to N(G), and a fixed square has exactly
|H1(C2,G)| possible conjugacy classes. This is a STANDARD cyclic
group cohomology identity, now explicitly checked against the exact
Phase325 groups, not a new global prime estimate.

In D163,D187,D203, both groups have cardinalities 2,4,4.
These are TWO DIFFERENT cohomology groups with equal orders
for finite cyclic modules, not canonically the same group.
They share the 2-primary transfer obstruction pattern with
the additive sign-module H1(C2,Z_sign)=Z/2.

No assertion that the finite Frobenius candidates determine which
one belongs to a given inert rational p without additional labels.
"""
from __future__ import annotations
from pathlib import Path
import json
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase321"))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase322"))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase324"))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase325"))

from exact_ray_characters import ray_context,build_ray_coordinates  # noqa: E402
from semidirect_ray_representations import (  # noqa: E402
    conjugation_coordinates,coord_add,coord_neg,
)
from frobenius_conjugacy import frobenius_coset_classes  # noqa: E402


def cohomology_of_ray_group(D:int)->dict:
    if D not in (163,187,203):
        raise ValueError("Only the three exact Phase325 ray groups")
    (_, forms, ideals, identity, table, alpha, inverses,
     units, local_alpha, _) = ray_context(D)
    context=(forms,identity,table,alpha,inverses,units,local_alpha)
    model=build_ray_coordinates(D,context)
    sigma=conjugation_coordinates(D,model,ideals)
    classes=frobenius_coset_classes(model,sigma)
    n1,n2=model["n1"],model["n2"]
    identity_coord=(0,0)
    assert identity_coord in sigma
    assert sigma[identity_coord]==identity_coord

    def add(x,y):return coord_add(x,y,n1,n2)
    def neg(x):return coord_neg(x,n1,n2)
    def difference(x):return add(x,neg(sigma[x]))
    def norm(x):return add(x,sigma[x])
    N_image={norm(g) for g in sigma}
    D_image={difference(g) for g in sigma}
    fixed={g for g in sigma if sigma[g]==g}
    ker_N={g for g in sigma if norm(g)==identity_coord}
    assert N_image <= fixed
    assert D_image <= ker_N
    assert len(sigma)==len(model["all_elements"])
    assert len(D_image)==classes["difference_image_order"]
    assert len(N_image)==classes["norm_image_order"]==50

    # True cyclic H1 quotient size, computed from exact finite sets.
    assert len(ker_N)%len(D_image)==0
    H1_order=len(ker_N)//len(D_image)
    Tate0_order=len(fixed)//len(N_image)

    # Independent conjugacy-class square-fiber count.
    square_fiber=classes["classes_by_square"][identity_coord]
    assert len(square_fiber)==H1_order
    assert H1_order==classes["classes_per_squared_frobenius"]
    assert H1_order==Tate0_order

    # Both C2 cohomology groups are killed by 2. For ker(N),
    # sigma(g)=-g => 2g=(1-sigma)g lies in D(G).
    for x in ker_N:
        assert add(x,x) == difference(x)
        assert add(x,x) in D_image

    # The square class of an inert Frobenius, by definition,
    # lands in N(G). For all group elements in G, quotient class
    # of x has N(x) independent of representative x+D(G).
    for x in sigma:
        assert norm(add(x,difference((1%n1,0))))==norm(x)

    return {
        "D":D,
        "G_order":len(sigma),
        "G_fixed_order":len(fixed),
        "norm_image_order":len(N_image),
        "difference_image_order":len(D_image),
        "ker_norm_order":len(ker_N),
        "H1_C2_ray_order":H1_order,
        "Tate_H0_C2_ray_order":Tate0_order,
        "squared_frob_class_ambiguity":len(square_fiber),
        "inert_rational_coset_class_count":len(classes["square_by_class"]),
        "cohomology_two_torsion_verified":True,
        "source":"Phase321-325 exact ray-class cocycle arithmetic",
        "does_not_establish_global_prime_inequality":True,
        "does_not_establish_original_jet_intertwiner":True,
    }


def main():
    rows=[cohomology_of_ray_group(D) for D in (163,187,203)]
    print("PHASE330_FROBENIUS_COHOMOLOGY",json.dumps(rows,sort_keys=True))


if __name__=="__main__":
    main()
