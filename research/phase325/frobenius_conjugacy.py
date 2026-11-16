#!/usr/bin/env python3
"""Phase325: exact Frobenius conjugacy-class constraints over Q.

Arithmetic Frobenius for unramified rational primes p not dividing 5*D.

G=Gal(L/K)=Cl_125(K), H=G rtimes_sigma C2=Gal(L/Q).
A split rational p has conjugacy class {g, sigma(g)} in G.
For inert rational p, Frob_p lies in G*sigma and its square is
the rational ray class [(p)] in G. The square alone may leave more
than one conjugacy class: DO NOT select an unverified lift.

Only exact finite group arithmetic and rational character phases are
used. This program does not construct the ray-class field polynomial
or calculate an actual inert rational Frobenius lift, L-values, global
Euler products, prime-distribution bounds, or a discriminant endpoint.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from math import gcd
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase321"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase322"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase324"))

from exact_ray_characters import (  # noqa: E402
    MOD, build_ray_coordinates, canonical_signed_mod,
    exponent_numerator, ray_context,
)
from ideal_aware_ray_class import prime_ideal_catalog  # noqa: E402
from semidirect_ray_representations import (  # noqa: E402
    conjugation_coordinates, coord_add, coord_neg,
)


def subtract(x, y, n1, n2):
    return coord_add(x, coord_neg(y, n1, n2), n1, n2)


def order_in_product(x, n1, n2):
    """Order in the explicit C_n1 x C_n2 model, no floating roots."""
    from math import lcm
    return lcm(n1 // gcd(n1, x[0]), n2 // gcd(n2, x[1]))


def norm_class(x, sigma, n1, n2):
    return coord_add(x, sigma[x], n1, n2)


def rational_principal_coordinate(p, D, model):
    if p % 5 == 0:
        raise ValueError("prime divides conductor")
    return model["coordinate_map"][
        (model["identity"][0],
         canonical_signed_mod((p, 0), MOD))
    ]


def frobenius_coset_classes(model, sigma):
    """Classify the *entire* nontrivial coset G*sigma.

    Conjugation by a group element h sends g*sigma to
        (g + h - sigma(h))*sigma.
    Thus each nontrivial-coset conjugacy class is a coset of
    (1-sigma)G. Conjugation by sigma adds no extra class members.
    """
    n1, n2 = model["n1"], model["n2"]
    origin = (0, 0)
    assert origin in sigma and sigma[origin] == origin
    difference_image = {
        subtract(x, sx, n1, n2) for x, sx in sigma.items()
    }
    assert origin in difference_image
    for x in sigma:
        assert sigma[sigma[x]] == x
    # The full image is a subgroup. Check closure on its generators
    # and all elements, using the fact that sigma is a homomorphism.
    for x in sigma:
        for generator in ((1, 0), (0, 1)):
            lhs = sigma[coord_add(x, generator, n1, n2)]
            rhs = coord_add(sigma[x], sigma[generator], n1, n2)
            assert lhs == rhs

    class_by_element = {}
    square_by_class = {}
    class_sizes = Counter()
    for g in sigma:
        if g in class_by_element:
            continue
        conjugates = {
            coord_add(g, delta, n1, n2)
            for delta in difference_image
        }
        assert len(conjugates) == len(difference_image)
        rep = min(conjugates)
        assert rep not in square_by_class
        square = norm_class(rep, sigma, n1, n2)
        for conjugate in conjugates:
            assert conjugate not in class_by_element
            assert norm_class(conjugate, sigma, n1, n2) == square
            class_by_element[conjugate] = rep
        square_by_class[rep] = square
        class_sizes[len(conjugates)] += 1

    assert len(class_by_element) == len(sigma) == n1 * n2
    fixed_count = sum(x == sx for x, sx in sigma.items())
    assert len(difference_image) == len(sigma) // fixed_count
    assert len(square_by_class) == fixed_count

    classes_by_square = defaultdict(list)
    for rep, square in square_by_class.items():
        classes_by_square[square].append(rep)

    # For all three fields, local signed-unit norms give every
    # rational unit residue modulo 125 up to sign: exactly 50 classes.
    rational_units = {
        rational_principal_coordinate(u, None, model)
        for u in range(1, MOD) if u % 5 != 0
    }
    assert len(rational_units) == 50
    assert set(classes_by_square) == rational_units
    assert len(set(map(len, classes_by_square.values()))) == 1
    ambiguous_lifts = fixed_count // 50
    assert all(len(v) == ambiguous_lifts for v in classes_by_square.values())

    return {
        "difference_image_order": len(difference_image),
        "fixed_count": fixed_count,
        "coset_class_count": len(square_by_class),
        "coset_class_size": len(difference_image),
        "norm_image_order": len(classes_by_square),
        "classes_per_squared_frobenius": ambiguous_lifts,
        "class_by_element": class_by_element,
        "square_by_class": square_by_class,
        "classes_by_square": classes_by_square,
        "class_sizes": dict(class_sizes),
    }


def local_polynomial_phases(D, model, sigma, classes, catalog):
    """Check split and inert local Artin factor identities using phases.

    Split:
        (1 - chi(g) T)(1 - chi(sigma(g)) T).
    Inert:
        1 - chi([(p)]) T^2.

    For inert p, test all *candidate* conjugacy classes whose squares
    equal [(p)]. We NEVER assert which is the actual Frob_p class.
    """
    n1, n2 = model["n1"], model["n2"]
    den = n1 * n2
    coordinate_map = model["coordinate_map"]
    rows = defaultdict(list)
    for row in catalog["records"]:
        rows[row["p"]].append(row)
    split = inert = ramified = phase_checks = 0
    samples = ((0, 0), (1, 0), (0, 1), (n1-1, n2-1))
    for p, pair in sorted(rows.items()):
        rational_class = rational_principal_coordinate(p, D, model)
        kind = pair[0]["type"]
        if kind == "split":
            assert len(pair) == 2
            g, gbar = (
                coordinate_map[tuple(row["ray_class"])] for row in pair)
            assert sigma[g] == gbar and sigma[gbar] == g
            assert coord_add(g, gbar, n1, n2) == rational_class
            split += 1
            for chi in samples:
                a = exponent_numerator(*chi, g, n1, n2)
                b = exponent_numerator(*chi, gbar, n1, n2)
                c = exponent_numerator(*chi, rational_class, n1, n2)
                assert (a+b) % den == c
                phase_checks += 1
        elif kind == "inert":
            assert len(pair) == 1
            inert += 1
            assert (
                coordinate_map[tuple(pair[0]["ray_class"])]
                == rational_class
            )
            # Each candidate rational Frobenius has zero trace in
            # non-fixed 2D induced blocks, and the same determinant
            # -chi([(p)]). Its square is scalar chi([(p)]) I_2.
            candidates = classes["classes_by_square"][rational_class]
            assert len(candidates) == classes["classes_per_squared_frobenius"]
            for g in candidates:
                assert norm_class(g, sigma, n1, n2) == rational_class
                for chi in samples:
                    a = exponent_numerator(*chi, g, n1, n2)
                    b = exponent_numerator(*chi, sigma[g], n1, n2)
                    c = exponent_numerator(*chi, rational_class, n1, n2)
                    assert (a+b) % den == c
                    phase_checks += 1
        else:
            assert kind == "ramified" and len(pair) == 1
            ramified += 1
            # This prime ramifies over Q: do not define unramified
            # rational Frobenius element from the ray class alone.
    return {
        "split_rational_primes": split,
        "inert_rational_primes": inert,
        "ramified_rational_primes": ramified,
        "exact_local_polynomial_phase_checks": phase_checks,
    }


def run_field(D):
    if D not in (163, 187, 203):
        raise ValueError("This implementation has verified class-group data only for three fields")
    (_, forms, ideals, identity, table, alpha, inverses,
     units, local_alpha, _) = ray_context(D)
    context = (forms, identity, table, alpha, inverses, units, local_alpha)
    model = build_ray_coordinates(D, context)
    sigma = conjugation_coordinates(D, model, ideals)
    conjugacy = frobenius_coset_classes(model, sigma)
    catalog = prime_ideal_catalog(D, ideals, table, alpha)
    local = local_polynomial_phases(D, model, sigma, conjugacy, catalog)

    # D=163,187,203 are all 3 modulo 8: their negative fundamental
    # discriminants are 5 modulo 8, hence 2 is inert.
    assert (-D) % 8 == 5
    rational_two = rational_principal_coordinate(2, D, model)
    assert rational_two in conjugacy["classes_by_square"]
    square_order = order_in_product(rational_two, model["n1"], model["n2"])
    assert square_order == 50
    f2 = 2 * square_order
    h_order = 2 * len(model["all_elements"])
    assert h_order % f2 == 0

    return {
        "D": D,
        "ray_group_order": len(model["all_elements"]),
        "rational_extension_order": h_order,
        "inert_frobenius_coset_class_count": conjugacy["coset_class_count"],
        "each_inert_coset_class_size": conjugacy["coset_class_size"],
        "squared_frobenius_norm_image_order": conjugacy["norm_image_order"],
        "candidate_classes_per_squared_frobenius":
            conjugacy["classes_per_squared_frobenius"],
        "two_is_inert": True,
        "two_square_frobenius_order": square_order,
        "two_rational_frobenius_order": f2,
        "two_residue_degree_in_ray_class_field": f2,
        "two_number_of_primes_in_ray_class_field": h_order // f2,
        "catalog_local_polynomials": local,
        "bounds": {
            "arithmetic_frobenius_convention": True,
            "do_not_claim_inert_full_frobenius_class_from_its_square": True,
            "no_global_euler_product_or_L_values": True,
            "no_new_discriminant_bound": True,
        },
    }


def main():
    result = [run_field(D) for D in (163, 187, 203)]
    print("PHASE325_FROBENIUS_CONJUGACY_PASS",
          json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
