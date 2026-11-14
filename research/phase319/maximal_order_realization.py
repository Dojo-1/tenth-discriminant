#!/usr/bin/env python3
"""Phase319: maximal-order completion of Phase318's wild-ray realization test.

This experiment keeps the original integer-order Q109 and the genuine
maximal-order Q225 as different supports. It tests all 34 exact split-prime
characters on Q225, exhausts exact maximal-order norm fibres for every
changed shell, replays the full conductor-250 convolution, and measures
the complete local norm-preserving second-wild lift family.

No field-uniform valuation or new discriminant bound is inferred.
"""
from collections import Counter, defaultdict
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
for folder in (
    "phase311", "phase312", "phase313", "phase314",
    "phase315", "phase316", "phase317", "phase318"
):
    sys.path.insert(0, str(ROOT / "research" / folder))

from inert_trace_radicals import full_omega_q, rank_f5
from norm_shell_bridge import quadratic_norm
from fermat_lift import conjugate
from wild_gauge import integer_mul
from wild_log125 import (
    exhaustive_lift_table, is_unit, norm, signed_ray125_tag
)
from conductor250_original_mod25 import (
    gram_from_unit_rays_and_nonunit_lifts, gram_of_observations,
    unit_and_nonunit_counts
)
from radical_tangent import kernel_basis_mod5
from two_digit_smith import two_smith_slices
from split_prime_normal import (
    global_ray_replay_one_prime, signed_wild_character_tag,
    split_principal_prime_generators, verify_exact_ideal_valuation_character
)

D = 163
RHO = 21
R = 40
P = 5
MOD = 25
TOP = 125


def exact_maximal_order_norm_fibre(n):
    """All (a,b) with a^2+a*b+41*b^2=n, without a source-support filter."""
    assert n >= 0
    out = set()
    for b in range(-3, 4):
        t2 = 4 * n - 163 * b * b
        if t2 < 0:
            continue
        t = isqrt(t2)
        if t * t != t2:
            continue
        for signed_t in {t, -t}:
            if (signed_t - b) % 2 == 0:
                a = (signed_t - b) // 2
                z = (a, b)
                assert quadratic_norm(z, D) == n
                out.add(z)
    return tuple(sorted(out))


def signed_representatives(points):
    points = set(points)
    out = []
    for z in points:
        opposite = (-z[0], -z[1])
        assert opposite in points
        if z < opposite:
            out.append(z)
    return tuple(sorted(out))


def source_sites(Q):
    sites = []
    nonunits = []
    for z in Q:
        opposite = (-z[0], -z[1])
        if is_unit(z, D):
            if z < opposite:
                sites.append(z)
        else:
            nonunits.append(z)
    return tuple(sorted(sites)), tuple(sorted(nonunits))


def trace_norm_differential(h, z):
    product_z = integer_mul(h, conjugate(z, None))
    return (2 * product_z[0] + product_z[1]) % P


def complete_local_lift_line(z):
    candidates = tuple(
        (a, b)
        for a, b in product(range(P), repeat=2)
        if trace_norm_differential((a, b), z) == 0
    )
    assert len(candidates) == P
    assert (0, 0) in candidates
    base = next(h for h in candidates if h != (0, 0))
    generated = {
        ((k * base[0]) % P, (k * base[1]) % P)
        for k in range(P)
    }
    assert generated == set(candidates)
    return base, candidates


def local_differential_certificate(sites, Gactual):
    """Enumerate all 5 lifts/site and compare full and radical-normal spans."""
    K, pivots, free = kernel_basis_mod5(Gactual % P)
    assert K.shape[0] == R
    assert rank_f5(Gactual % P) == R
    assert K.shape == (R, 0), ("maximal-order primitive radical is nonzero", K.shape)

    normal_matrices = []
    full_matrices = []
    lift_count = 0
    for z in sites:
        base, candidates = complete_local_lift_line(z)
        assert len(candidates) == 5
        baseline = gram_of_observations((z, (-z[0], -z[1])))
        first = None
        for k in range(P):
            lifted = (
                z[0] + 25 * k * base[0],
                z[1] + 25 * k * base[1]
            )
            assert norm(lifted, D, TOP) == norm(z, D, TOP)
            old_tag = signed_ray125_tag(z, D)
            new_tag = signed_ray125_tag(lifted, D)
            assert old_tag[0] == new_tag[0]
            assert tuple(x % P for x in old_tag[1]) == tuple(
                x % P for x in new_tag[1]
            )
            shifted = gram_of_observations(
                (lifted, (-lifted[0], -lifted[1]))
            )
            diff = (shifted - baseline) % MOD
            assert np.array_equal(diff, diff.T)
            assert not np.any(diff % P)
            H = (diff // P) % P
            if k == 0:
                assert not np.any(H)
            elif k == 1:
                first = H
            else:
                assert np.array_equal(H, (k * first) % P)
            lift_count += 1
        assert first is not None
        full_matrices.append(first)
        # K has zero columns, so every restriction is the empty 0x0 form.
        normal = (K.T @ first @ K) % P
        assert normal.shape == (0, 0)
        normal_matrices.append(normal)

    tri = np.triu_indices(R)
    full_vectors = np.column_stack([H[tri] for H in full_matrices]) % P
    full_span_rank = rank_f5(full_vectors)
    assert lift_count == 5 * len(sites)
    return {
        "signed_5unit_sites": len(sites),
        "nonunit_stratum_separate": True,
        "local_norm125_lifts_per_site": 5,
        "all_local_lifts_checked": lift_count,
        "local_differentials_linear_in_F5_lift_parameter": True,
        "all_primitive_Gram_differentials_symmetric": True,
        "maximal_order_primitive_Gram_rank_mod5": R,
        "maximal_order_primitive_radical_dimension": K.shape[1],
        "radical_normal_image_dimension": 0,
        "full_symmetric_40x40_local_differential_span_rank": full_span_rank,
        "no_local_norm_or_first_wild_digit_failure": True
    }


def exact_shell_realization(Q, sites, pi):
    """Compare synthetic ray tags with every exact maximal-order generator."""
    actual = defaultdict(Counter)
    synthetic = defaultdict(Counter)
    for z in sites:
        n = quadratic_norm(z, D)
        actual[n][signed_ray125_tag(z, D)] += 1
        synthetic[n][signed_wild_character_tag(z, pi)] += 1

    changed = sorted(
        n for n in set(actual) | set(synthetic)
        if actual[n] != synthetic[n]
    )
    Qset = set(Q)
    records = []
    for n in changed:
        fibre = exact_maximal_order_norm_fibre(n)
        assert fibre, ("occupied source norm has no exact maximal-order fibre", n)
        assert set(fibre).issubset(Qset), (
            "norm-shell generator lies outside complete radius-21 support", n
        )
        fibre_sites = signed_representatives(fibre)
        assert all(is_unit(z, D) for z in fibre_sites)
        fibre_tags = Counter(signed_ray125_tag(z, D) for z in fibre_sites)
        assert fibre_tags == actual[n], (
            "source ray support disagrees with exhaustive maximal-order norm fibre",
            n, fibre_tags, actual[n]
        )
        synthetic_support = set(synthetic[n])
        actual_support = set(fibre_tags)
        missing = sorted(synthetic_support - actual_support)
        overlap = sorted(synthetic_support & actual_support)
        records.append({
            "norm": n,
            "exact_maximal_order_generators": len(fibre),
            "exact_signed_generator_classes": len(fibre_sites),
            "actual_signed_ray_classes": len(actual_support),
            "synthetic_signed_ray_classes": len(synthetic_support),
            "synthetic_classes_realized_at_exact_norm": len(overlap),
            "synthetic_classes_unrealized_at_exact_norm": len(missing),
            "all_synthetic_classes_globally_realized": not missing,
            "synthetic_support_disjoint": not overlap and bool(missing),
            "synthetic_only_tags": missing,
            "actual_only_tags": sorted(actual_support - synthetic_support),
            "ray_multiplicity_counter_unchanged": actual[n] == synthetic[n]
        })
    return changed, records


def determinant_mod25(matrix):
    """Determinant modulo 25 using only unit pivots (valid if rank mod5 is full)."""
    a = np.asarray(matrix, dtype=np.int64).copy() % MOD
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError("square matrix required")
    n = a.shape[0]
    det = 1
    for k in range(n):
        pivot = next(
            (i for i in range(k, n) if int(a[i, k]) % P != 0),
            None
        )
        if pivot is None:
            return 0
        if pivot != k:
            a[[k, pivot], :] = a[[pivot, k], :]
            det = (-det) % MOD
        value = int(a[k, k]) % MOD
        det = (det * value) % MOD
        inv = pow(value, -1, MOD)
        for i in range(k + 1, n):
            factor = int(a[i, k]) * inv % MOD
            if factor:
                a[i, k:] = (a[i, k:] - factor * a[k, k:]) % MOD
    return det % MOD


def full_maximal_order_certificate():
    Q, prime_generators, ramified = split_principal_prime_generators()
    Q = tuple(Q)
    assert len(Q) == 225
    Q_even = tuple(z for z in Q if z[1] % 2 == 0)
    assert len(Q_even) == 109
    assert len({(a % P, b % P) for a, b in Q}) == 25

    sites, nonunits = source_sites(Q)
    even_sites, even_nonunits = source_sites(Q_even)
    assert len(sites) == 108
    assert len(nonunits) == 9
    assert len(even_sites) == 50
    assert len(even_nonunits) == 9

    actual_counts, actual_nonunit_counts = unit_and_nonunit_counts(Q)
    assert sum(actual_counts.values()) == len(sites)
    assert sum(actual_nonunit_counts.values()) == len(nonunits)
    lookup, _ = exhaustive_lift_table(D)
    Gactual = gram_from_unit_rays_and_nonunit_lifts(
        actual_counts, actual_nonunit_counts, lookup
    )
    direct = np.zeros((R, R), dtype=np.int64)
    for z in sites:
        direct = (direct + gram_of_observations((z, (-z[0], -z[1])))) % MOD
    for z in nonunits:
        direct = (direct + gram_of_observations((z,))) % MOD
    assert np.array_equal(Gactual, direct)
    assert rank_f5(Gactual % P) == 40
    actual_profile = two_smith_slices(Gactual)
    profile_actual = [
        actual_profile["e0_unit_smith_factors"],
        actual_profile["e1_exactly_one_five"],
        actual_profile["e_at_least_2"]
    ]
    assert profile_actual == [40, 0, 0]
    det_actual = determinant_mod25(Gactual)

    local = local_differential_certificate(sites, Gactual)
    results = []
    all_replays = []
    active_even = []
    active_full = []
    total_exact_valuation_checks = 0
    total_shell_checks = 0
    total_convolution_checks = 0

    for prime, pi in sorted(prime_generators.items()):
        checks = verify_exact_ideal_valuation_character(pi, Q)
        total_exact_valuation_checks += checks
        replay = global_ray_replay_one_prime(pi, Q)
        all_replays.append(replay)
        total_shell_checks += replay["all_independent_h1_ideal_norm_shells"]
        total_convolution_checks += replay[
            "full_22500_conductor250_coprime_products"
        ]

        even_active = any(
            signed_wild_character_tag(z, pi) != signed_ray125_tag(z, D)
            for z in even_sites
        )
        full_active = any(
            signed_wild_character_tag(z, pi) != signed_ray125_tag(z, D)
            for z in sites
        )
        if even_active:
            active_even.append(prime)
        if full_active:
            active_full.append(prime)

        changed, shell_records = exact_shell_realization(Q, sites, pi)
        assert all(
            x["synthetic_classes_unrealized_at_exact_norm"] == 2
            for x in shell_records
        ), ("changed maximal-order norm shell has an unexpected ray realization", prime)
        fake_counts = Counter(
            signed_wild_character_tag(z, pi) for z in sites
        )
        Gfake = gram_from_unit_rays_and_nonunit_lifts(
            fake_counts, actual_nonunit_counts, lookup
        )
        assert np.array_equal(Gfake % P, Gactual % P), (
            "wild shift changed the original first digit", prime
        )
        fake_profile = two_smith_slices(Gfake)
        profile_fake = [
            fake_profile["e0_unit_smith_factors"],
            fake_profile["e1_exactly_one_five"],
            fake_profile["e_at_least_2"]
        ]
        assert profile_fake == [40, 0, 0]
        det_fake = determinant_mod25(Gfake)
        results.append({
            "split_prime": prime,
            "principal_generator": pi,
            "exact_valuation_product_checks": checks,
            "full_ray250_norm_shell_checks": replay[
                "all_independent_h1_ideal_norm_shells"
            ],
            "full_ray250_coprime_products": replay[
                "full_22500_conductor250_coprime_products"
            ],
            "active_on_old_even_support": even_active,
            "active_on_full_maximal_support": full_active,
            "changed_exact_norm_shells": len(changed),
            "changed_norms": changed,
            "exact_norm_fibre_records": shell_records,
            "synthetic_classes_unrealized_over_full_maximal_order": sum(
                x["synthetic_classes_unrealized_at_exact_norm"]
                for x in shell_records
            ),
            "all_changed_shells_have_full_exact_fibre_audit": True,
            "maximal_order_first_two_smith_layers": profile_fake,
            "determinant_residue_mod25_actual": det_actual,
            "determinant_residue_mod25_synthetic": det_fake,
            "determinant_residue_changed_mod25": det_actual != det_fake,
            "no_5adic_valuation_claim_from_residue_change": True
        })

    assert len(prime_generators) == 34
    byprime = {x["split_prime"]: x for x in results}
    required = {41: 164, 53: 212, 227: 227}
    required_fibres = {}
    for p, n in required.items():
        assert n in byprime[p]["changed_norms"]
        rec = next(x for x in byprime[p]["exact_norm_fibre_records"]
                   if x["norm"] == n)
        fibre = exact_maximal_order_norm_fibre(n)
        required_fibres[p] = {
            "norm": n,
            "all_maximal_order_generators": fibre,
            "signed_generator_classes": len(signed_representatives(fibre)),
            "synthetic_classes_unrealized": rec[
                "synthetic_classes_unrealized_at_exact_norm"
            ],
            "synthetic_support_disjoint": rec["synthetic_support_disjoint"]
        }
        assert len(fibre) == 4
        assert rec["synthetic_support_disjoint"], (
            "Phase318 resonance became realized in the full maximal order", p, rec
        )

    assert set(active_even).issubset(set(active_full))
    assert len(active_even) == 16
    assert len(active_full) == 34
    total_changed_shells = sum(x["changed_exact_norm_shells"] for x in results)
    total_unrealized = sum(
        x["synthetic_classes_unrealized_over_full_maximal_order"]
        for x in results
    )
    residue_changes = sum(x["determinant_residue_changed_mod25"] for x in results)
    assert total_changed_shells == 44
    assert total_unrealized == 88
    assert residue_changes == 21
    assert byprime[197]["changed_exact_norm_shells"] == 0
    return {
        "D": D,
        "maximal_order_norm_cutoff": RHO * RHO,
        "full_maximal_order_Q": len(Q),
        "old_integer_order_Q": len(Q_even),
        "new_odd_omega_coordinate_points": len(Q) - len(Q_even),
        "F25_residue_support": 25,
        "signed_5unit_sites": len(sites),
        "nonunit_observations": len(nonunits),
        "actual_primitive_Gram_rank_mod5": rank_f5(Gactual % P),
        "actual_primitive_Gram_first_two_Smith_layers": profile_actual,
        "actual_primitive_Gram_determinant_residue_mod25": det_actual,
        "local_norm_preserving_second_wild_map": local,
        "split_prime_characters_tested": len(results),
        "active_on_old_even_support": len(active_even),
        "active_on_full_maximal_support": len(active_full),
        "newly_active_on_odd_coordinate_completion": sorted(
            set(active_full) - set(active_even)
        ),
        "exact_ideal_valuation_product_checks": total_exact_valuation_checks,
        "full_ray250_ideal_shell_replays": total_shell_checks,
        "full_ray250_coprime_products": total_convolution_checks,
        "total_changed_exact_norm_shells": total_changed_shells,
        "total_unrealized_synthetic_ray_classes": total_unrealized,
        "characters_changing_determinant_residue_mod25": residue_changes,
        "p197_per_shell_ray_spectrum_unchanged": True,
        "mandatory_exact_norm_fibres": required_fibres,
        "per_character_records": results,
        "all_full_support_synthetic_grams_keep_unit_mod5": True,
        "no_uniform_field_valuation_or_cutoff_claim": True
    }


def main():
    data = full_maximal_order_certificate()
    print("PHASE319_MAXIMAL_ORDER_WILD_RAY_REALIZATION_PASS", data, flush=True)


if __name__ == "__main__":
    main()
