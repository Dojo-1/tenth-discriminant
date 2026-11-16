#!/usr/bin/env python3
"""Phase324: exact ray-class characters and semidirect representations.

Finite, arithmetic-only. No floating roots, L-values, Euler products,
zero-free estimates, or extrapolation to a discriminant cutoff.

The ray class group G=Cl_125(K) is abelian. Complex conjugation acts
on G by sigma(g)=nu(g)*g^(-1), where nu(g) is the rational principal
ray class of the ideal norm. At conductor 125 this is NOT generally
inversion: the norm class need not be ray-trivial.

The semidirect group G rtimes_sigma C2 has 1D and 2D irreducibles.
Exact character exponents are retained; no complex approximations
are used as certificates.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase321"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase322"))

from ideal_aware_ray_class import (  # noqa: E402
    conjugate,
    ideal_norm,
    norm_mod,
    prime_ideal_catalog,
)
from exact_ray_characters import (  # noqa: E402
    MOD,
    build_ray_coordinates,
    canonical_signed_mod,
    character_conductors,
    conductor_kernels,
    exponent_numerator,
    ray_context,
)


def coord_add(x: tuple[int, int], y: tuple[int, int],
              n1: int, n2: int) -> tuple[int, int]:
    return ((x[0] + y[0]) % n1, (x[1] + y[1]) % n2)


def coord_neg(x: tuple[int, int], n1: int, n2: int) -> tuple[int, int]:
    return ((-x[0]) % n1, (-x[1]) % n2)


def conjugation_coordinates(D: int, model: dict, ideals: tuple) -> dict:
    """Compute sigma from actual ideal norms and explicit ray coordinates.

    If g corresponds to (class c, signed residue u), its representative
    ideal is (u) * I_c. Therefore N(g) is the rational ray class of
    N(I_c)*N(u), modulo 125. This is independent of cocycle coordinates.
    """
    n1, n2 = model["n1"], model["n2"]
    coordinates = model["coordinate_map"]
    identity_class = model["identity"][0]
    out = {}
    for element, x in coordinates.items():
        c, u = element
        nu = (ideal_norm(ideals[c]) * norm_mod(u, D, MOD)) % MOD
        rational_norm_class = (identity_class,
                               canonical_signed_mod((nu, 0), MOD))
        assert rational_norm_class in coordinates
        norm_x = coordinates[rational_norm_class]
        out[x] = coord_add(norm_x, coord_neg(x, n1, n2), n1, n2)
    assert len(out) == n1 * n2
    return out


def verify_conjugation(D: int, model: dict, ideals: tuple,
                       sigma: dict) -> dict:
    """Exhaustive finite tests of automorphism and true conjugate ideals."""
    n1, n2 = model["n1"], model["n2"]
    coordinates = model["coordinate_map"]
    id_class = model["identity"][0]
    e1, e2 = (1 % n1, 0), (0, 1 % n2)
    for x, sx in sigma.items():
        assert sigma[sx] == x, ("sigma^2 != 1", D, x)
        for e in (e1, e2):
            lhs = sigma[coord_add(x, e, n1, n2)]
            rhs = coord_add(sx, sigma[e], n1, n2)
            assert lhs == rhs, ("sigma not a homomorphism", D, x, e)
    assert len(set(sigma.values())) == len(sigma)

    # On the principal local subgroup, conjugation must agree with the
    # explicit quadratic-order conjugation of signed residue coordinates.
    principal_checks = 0
    for u in model["units"]:
        g = (id_class, u)
        ug = (id_class, canonical_signed_mod(conjugate(u), MOD))
        assert sigma[coordinates[g]] == coordinates[ug]
        principal_checks += 1

    # The catalog checks the nonprincipal component through actual
    # split ideal pairs, and checks inert and ramified fixed ideal classes.
    catalog = prime_ideal_catalog(D, ideals, model["table"], model["alpha"])
    pairs = {}
    for rec in catalog["records"]:
        pairs.setdefault(rec["p"], []).append(rec)
    ideal_checks = 0
    for p, rows in pairs.items():
        if rows[0]["type"] == "split":
            assert len(rows) == 2
            x, y = (coordinates[tuple(r["ray_class"])] for r in rows)
            assert sigma[x] == y and sigma[y] == x
            ideal_checks += 2
        else:
            assert len(rows) == 1
            x = coordinates[tuple(rows[0]["ray_class"])]
            assert sigma[x] == x, (D, p, rows[0]["type"])
            ideal_checks += 1

    # Rational (2) is conjugation-fixed but not its own inverse.
    rational_two = (id_class, canonical_signed_mod((2, 0), MOD))
    witness = coordinates[rational_two]
    assert sigma[witness] == witness
    assert witness != coord_neg(witness, n1, n2)
    return {"principal_checks": principal_checks,
            "prime_ideal_checks": ideal_checks,
            "non_inversion_witness": "rational principal ideal (2)"}


def dual_sigma(chi: tuple[int, int], sigma_generators: tuple,
               n1: int, n2: int) -> tuple[int, int]:
    """Dual character action, using integer rational phase numerators."""
    i, j = chi
    sg1, sg2 = sigma_generators
    denominator = n1 * n2
    num1 = exponent_numerator(i, j, sg1, n1, n2)
    num2 = exponent_numerator(i, j, sg2, n1, n2)
    assert num1 % n2 == 0, ("sigma(e1) has incompatible order", sg1)
    assert num2 % n1 == 0, ("sigma(e2) has incompatible order", sg2)
    return ((num1 // n2) % n1, (num2 // n1) % n2)


def sample_matrix_representation_relation(
    chi: tuple[int, int], g: tuple[int, int],
    sigma: dict, n1: int, n2: int
) -> bool:
    """Verify tau*pi(g)*tau^-1=pi(sigma(g)) as exact phase fractions.

    pi(g) has diagonal exponents chi(g), chi(sigma(g)) modulo 1.
    tau swaps the two basis vectors. We compare exponents only.
    """
    q0 = exponent_numerator(*chi, g, n1, n2)
    q1 = exponent_numerator(*chi, sigma[g], n1, n2)
    s0 = exponent_numerator(*chi, sigma[g], n1, n2)
    s1 = exponent_numerator(*chi, sigma[sigma[g]], n1, n2)
    return (q1, q0) == (s0, s1)


def run_field(D: int) -> dict:
    (_, forms, ideals, identity, table, alpha, inverses,
     units, local_alpha, _) = ray_context(D)
    context = (forms, identity, table, alpha, inverses, units, local_alpha)
    model = build_ray_coordinates(D, context)
    kernels, reduction_orders = conductor_kernels(D, model)
    conductors, expected_count = character_conductors(D, model, kernels)
    sigma = conjugation_coordinates(D, model, ideals)
    controls = verify_conjugation(D, model, ideals, sigma)
    n1, n2 = model["n1"], model["n2"]
    N = n1 * n2
    sigma_gen = (sigma[(1, 0)], sigma[(0, 1)])
    by_conductor = Counter()
    fixed_by_conductor = Counter()
    dual_fixed = 0
    for i in range(n1):
        for j in range(n2):
            chi = (i, j)
            image = dual_sigma(chi, sigma_gen, n1, n2)
            assert dual_sigma(image, sigma_gen, n1, n2) == chi
            assert conductors[image] == conductors[chi]
            by_conductor[conductors[chi]] += 1
            if image == chi:
                dual_fixed += 1
                fixed_by_conductor[conductors[chi]] += 1

    fixed_G = sum(sigma[g] == g for g in sigma)
    assert fixed_G == dual_fixed, ("duality fixed-space mismatch", D)
    assert dict(by_conductor) == expected_count
    assert (N - dual_fixed) % 2 == 0
    # A 1D character fixed by sigma extends with tau=+1 or -1.
    irreps_1d = 2 * dual_fixed
    # A two-element orbit induces one irreducible 2D representation.
    irreps_2d = (N - dual_fixed) // 2
    assert irreps_1d + 4 * irreps_2d == 2 * N

    sample_g = tuple(sorted(sigma))[:8]
    sample_chars = ((0, 0), (1, 0), (0, 1),
                    (n1 - 1, n2 - 1))
    for chi in sample_chars:
        for g in sample_g:
            assert sample_matrix_representation_relation(chi, g, sigma, n1, n2)

    conductor_rows = {}
    for modulus in (1, 5, 25, 125):
        count = by_conductor[modulus]
        fixed = fixed_by_conductor[modulus]
        assert (count - fixed) % 2 == 0
        conductor_rows[str(modulus)] = {
            "characters": count,
            "sigma_fixed_characters": fixed,
            "one_dimensional_extensions": 2 * fixed,
            "two_dimensional_induced_irreps": (count - fixed) // 2,
        }

    return {
        "D": D,
        "ordinary_class_number": len(forms),
        "ray_group_order": N,
        "semidirect_group_order": 2 * N,
        "ray_invariant_factors": [n1, n2],
        "conductor_image_orders": {str(k): v for k, v in reduction_orders.items()},
        "conjugation_fixed_ray_classes": fixed_G,
        "conjugation_fixed_characters": dual_fixed,
        "one_dimensional_irreducibles": irreps_1d,
        "two_dimensional_irreducibles": irreps_2d,
        "sum_of_squares": irreps_1d + 4 * irreps_2d,
        "by_conductor": conductor_rows,
        "controls": controls,
        "boundaries": {
            "no_global_character_sum_bound": True,
            "no_euler_product_or_L_values": True,
            "no_integral_source_gram_action_claim": True,
            "no_new_discriminant_bound": True,
        },
    }


def main():
    import json
    results = [run_field(D) for D in (163, 187, 203)]
    print("PHASE324_EXACT_RAY_REPRESENTATION_PASS",
          json.dumps(results, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
