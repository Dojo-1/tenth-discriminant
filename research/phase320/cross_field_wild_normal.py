#!/usr/bin/env python3
"""Phase320: cross-field maximal-order second-wild normal-map experiment.

Fields: D=163 (h=1), 187 (h=2), 203 (h=4), all with 5 inert.
The experiment separates:
  (i) a common R=40,J=1,norm<=441 diagnostic,
  (ii) the D163 even-suborder legacy control,
  (iii) native D187 R46,J1 and D203 R50,J2 sources.

All source Grams use the genuine maximal order and the original trace metric.
The Frobenius row frame is unimodular; division of the designated rows by 5
is separately recorded as an evaluation superlattice. Local lifts are only
performed at 5-units; nonunits remain separate.

This is a finite local/source experiment, not a global ray-character or
class-number-one valuation theorem.
"""
from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "phase315"))
from wild_log125 import exhaustive_lift_table, is_unit, norm, signed_ray125_tag

P = 5
MOD = 25
TOP = 125
FIELDS = (163, 187, 203)
EXPECTED_CLASS_NUMBERS = {163: 1, 187: 2, 203: 4}


def m_parameter(D):
    assert D > 3 and D % 4 == 3
    return (D + 1) // 4


def mul(x, y, D, mod=None):
    a, b = x
    c, d = y
    m = m_parameter(D)
    z = (a * c - m * b * d, a * d + b * c + b * d)
    if mod is None:
        return z
    return (z[0] % mod, z[1] % mod)


def conjugate(z, mod=None):
    a, b = z
    out = (a + b, -b)
    if mod is None:
        return out
    return (out[0] % mod, out[1] % mod)


def norm_int(z, D):
    a, b = z
    return a * a + a * b + m_parameter(D) * b * b


def norm_mod(z, D, mod):
    return norm_int(z, D) % mod


def trace(z):
    return 2 * z[0] + z[1]


def trace_pairing(x, y, D):
    return trace(mul(x, conjugate(y), D))


def trace_matrix(D):
    m = m_parameter(D)
    return np.asarray([[2, 1], [1, 2 * m]], dtype=np.int64)


def exact_rho(D):
    rho = 0
    while 25**4 * rho**4 < 11**4 * D**3:
        rho += 1
    return rho


def maximal_order_source(D, rho):
    """Exhaust N(a+b*omega)<=rho^2 with a proved finite b/a box."""
    m = m_parameter(D)
    bmax = isqrt((4 * rho * rho) // D)
    Q = []
    for b in range(-bmax, bmax + 1):
        abound = rho + abs(b) + 2
        for a in range(-abound, abound + 1):
            if a * a + a * b + m * b * b <= rho * rho:
                Q.append((a, b))
        assert norm_int((abound, b), D) > rho * rho
        assert norm_int((-abound, b), D) > rho * rho
    Q = tuple(sorted(set(Q)))
    assert len(Q) == len(set(Q))
    assert all(norm_int(z, D) <= rho * rho for z in Q)
    Qset = set(Q)
    assert all((-a, -b) in Qset for a, b in Q)
    return Q


def old_integer_order_source_D163(rho=21):
    Q = []
    for y in range(-isqrt((rho * rho) // 163),
                   isqrt((rho * rho) // 163) + 1):
        xbound = isqrt(rho * rho - 163 * y * y)
        for x in range(-xbound, xbound + 1):
            Q.append((x - y, 2 * y))
    return tuple(sorted(set(Q)))


def reduced_forms(D):
    """Exact reduced primitive positive forms of discriminant -D."""
    forms = []
    for a in range(1, isqrt(D // 3) + 2):
        for b in range(-a, a + 1):
            numerator = b * b + D
            if numerator % (4 * a):
                continue
            c = numerator // (4 * a)
            if a > c:
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            forms.append((a, b, c))
    return tuple(forms)


def class_number_certificate(D):
    forms = reduced_forms(D)
    h = len(forms)
    assert h == EXPECTED_CLASS_NUMBERS[D], (D, forms, h)
    return {"D": D, "discriminant": -D, "reduced_forms": forms,
            "class_number": h, "exact_reduced_form_count": True}


def field_certificate(D):
    assert D % 4 == 3
    # D is squarefree, so -D is a fundamental quadratic discriminant.
    for p in range(2, isqrt(D) + 1):
        assert D % (p * p) != 0
    minus_D_mod5 = (-D) % 5
    assert minus_D_mod5 in (2, 3)
    assert minus_D_mod5 not in {x * x % 5 for x in range(5)}
    return {
        "D": D,
        "fundamental_discriminant": -D,
        "minus_D_mod5": minus_D_mod5,
        "five_inert": True,
        "residue_algebra": "F25",
        "trace_matrix": trace_matrix(D).tolist(),
        "trace_matrix_determinant": D,
        "class_number": class_number_certificate(D)
    }


def row_frame(R, J):
    """Original-row unitriangular Frobenius frame and divided row indices."""
    n = R * J
    U = np.eye(n, dtype=np.int64)
    divided = []
    if J == 1:
        for r in range(25, R):
            U[r, r - 24] = -1
            divided.append(r)
    elif J == 2:
        for r in range(5, R):
            i = r * J
            prev = (r - 5) * J + 1
            U[i, prev] = -1
            divided.append(i)
    else:
        raise ValueError("Phase320 freezes only J=1 or J=2")
    return U, tuple(divided)


def raw_rows(z, D, R, J):
    """Rows Z^r W^s, W=conjugate(Z), modulo 125."""
    z = (z[0] % TOP, z[1] % TOP)
    w = conjugate(z, TOP)
    zp = [(1, 0)]
    wp = [(1, 0)]
    for _ in range(1, R):
        zp.append(mul(zp[-1], z, D, TOP))
    for _ in range(1, J):
        wp.append(mul(wp[-1], w, D, TOP))
    E = np.zeros((R * J, 2), dtype=np.int64)
    for r in range(R):
        for s in range(J):
            E[r * J + s, :] = mul(zp[r], wp[s], D, TOP)
    return E


def primitive_rows(z, D, R, J, U=None, divided=None):
    if U is None:
        U, divided = row_frame(R, J)
    raw = raw_rows(z, D, R, J)
    transformed = (U @ raw) % TOP
    primitive = np.zeros_like(transformed)
    divset = set(divided)
    for i in range(R * J):
        if i in divset:
            assert not np.any(transformed[i, :] % P), (
                "Frobenius row failed exact /5 divisibility", D, R, J, i, z)
            primitive[i, :] = (transformed[i, :] // P) % MOD
        else:
            primitive[i, :] = transformed[i, :] % MOD
    return raw, transformed, primitive


def point_gram(E, D, modulus):
    B = trace_matrix(D)
    return (E @ B @ E.T) % modulus


def pair_gram(z, D, R, J, U, divided):
    _, _, E1 = primitive_rows(z, D, R, J, U, divided)
    neg = ((-z[0]) % TOP, (-z[1]) % TOP)
    _, _, E2 = primitive_rows(neg, D, R, J, U, divided)
    return (point_gram(E1, D, MOD) + point_gram(E2, D, MOD)) % MOD


def source_gram_certificate(Q, D, R, J):
    U, divided = row_frame(R, J)
    n = R * J
    Gorig = np.zeros((n, n), dtype=np.int64)
    Gprim = np.zeros((n, n), dtype=np.int64)
    units = []
    nonunits = []
    for z in Q:
        raw, transformed, Eprim = primitive_rows(z, D, R, J, U, divided)
        Gorig = (Gorig + point_gram(raw, D, TOP)) % TOP
        Gprim = (Gprim + point_gram(Eprim, D, MOD)) % MOD
        if norm_mod(z, D, P) == 0:
            nonunits.append(z)
        else:
            units.append(z)

    Gtrans = (U @ Gorig @ U.T) % TOP
    divset = set(divided)
    for i in range(n):
        for j in range(n):
            if i in divset and j in divset:
                expected = (P * P * int(Gprim[i, j])) % TOP
            elif i in divset or j in divset:
                expected = (P * int(Gprim[i, j])) % TOP
            else:
                expected = int(Gprim[i, j]) % MOD
            actual = int(Gtrans[i, j])
            if i in divset or j in divset:
                assert actual == expected, (
                    "original-to-primitive Frobenius Gram identity failed",
                    D, R, J, i, j, actual, expected)
            else:
                assert actual % MOD == expected, (
                    "undivided original Gram block mismatch",
                    D, R, J, i, j, actual, expected)

    Qset = set(Q)
    sites = []
    for z in units:
        neg = (-z[0], -z[1])
        assert neg in Qset
        if z < neg:
            sites.append(z)
    assert 2 * len(sites) + len(nonunits) == len(Q)
    # Direct signed-pair plus separate nonunit reconstruction.
    Gpair = np.zeros((n, n), dtype=np.int64)
    for z in sites:
        Gpair = (Gpair + pair_gram(z, D, R, J, U, divided)) % MOD
    for z in nonunits:
        _, _, E = primitive_rows(z, D, R, J, U, divided)
        Gpair = (Gpair + point_gram(E, D, MOD)) % MOD
    assert np.array_equal(Gpair, Gprim)
    return {
        "U": U, "divided_rows": divided, "Gorig_mod125": Gorig,
        "Gprim_mod25": Gprim, "sites": tuple(sorted(sites)),
        "nonunits": tuple(sorted(nonunits)),
        "units": tuple(sorted(units)),
        "support_metadata": {
            "points": len(Q),
            "signed_5unit_sites": len(sites),
            "unit_points": len(units),
            "nonunit_points": len(nonunits),
            "residue_classes_F25": len({(a % 5, b % 5) for a, b in Q}),
            "b_layer_counts": dict(sorted(Counter(b for a, b in Q).items())),
            "original_rows": n,
            "jet_layers": J,
            "frobenius_divided_rows": len(divided),
            "all_divided_rows_exactly_divisible_by5": True,
            "original_to_primitive_gram_identity_checked": True,
            "nonunit_stratum_separate": True
        }
    }


def rank_mod5(matrix):
    A = np.asarray(matrix, dtype=np.int64) % P
    if A.ndim != 2 or A.size == 0:
        return 0
    rows, cols = A.shape
    rank = 0
    for col in range(cols):
        if rank >= rows:
            break
        candidates = np.flatnonzero(A[rank:, col])
        if not len(candidates):
            continue
        pivot = rank + int(candidates[0])
        if pivot != rank:
            A[[rank, pivot], :] = A[[pivot, rank], :]
        inv = pow(int(A[rank, col]), -1, P)
        A[rank, col:] = (A[rank, col:] * inv) % P
        factors = A[rank + 1:, col].copy()
        mask = factors != 0
        if np.any(mask):
            indices = np.flatnonzero(mask) + rank + 1
            A[indices, col:] = (
                A[indices, col:]
                - factors[mask, None] * A[rank, col:][None, :]
            ) % P
        rank += 1
    return rank


def kernel_basis_mod5(matrix):
    A = np.asarray(matrix, dtype=np.int64).copy() % P
    rows, cols = A.shape
    pivots = []
    r = 0
    for j in range(cols):
        if r >= rows:
            break
        candidates = np.flatnonzero(A[r:, j])
        if not len(candidates):
            continue
        k = r + int(candidates[0])
        if k != r:
            A[[r, k], :] = A[[k, r], :]
        A[r, :] = (A[r, :] * pow(int(A[r, j]), -1, P)) % P
        for i in range(rows):
            if i != r and A[i, j]:
                A[i, :] = (A[i, :] - A[i, j] * A[r, :]) % P
        pivots.append(j)
        r += 1
    free = [j for j in range(cols) if j not in set(pivots)]
    K = np.zeros((cols, len(free)), dtype=np.int64)
    for k, f in enumerate(free):
        K[f, k] = 1
        for i, j in enumerate(pivots):
            K[j, k] = (-A[i, f]) % P
    assert rank_mod5(K) == len(free) if free else K.shape[1] == 0
    assert not np.any((np.asarray(matrix, dtype=np.int64) @ K) % P)
    return K


def first_radical_form(G):
    K = kernel_basis_mod5(G % P)
    if K.shape[1] == 0:
        return K, np.zeros((0, 0), dtype=np.int64), 0
    lifted = (K.T @ (np.asarray(G, dtype=np.int64) % MOD) @ K) % MOD
    assert not np.any(lifted % P), "radical lift not divisible by five"
    B = (lifted // P) % P
    assert np.array_equal(B, B.T)
    return K, B, rank_mod5(B)


def local_norm_line(z, D):
    candidates = []
    for u in range(P):
        for v in range(P):
            h = (u, v)
            product = mul(h, conjugate(z), D, P)
            if (2 * product[0] + product[1]) % P == 0:
                candidates.append(h)
    assert len(candidates) == P, (D, z, candidates)
    assert (0, 0) in candidates
    base = next(h for h in candidates if h != (0, 0))
    generated = {((k * base[0]) % P, (k * base[1]) % P)
                 for k in range(P)}
    assert generated == set(candidates)
    return base, tuple(candidates)


def upper_vectors(matrices, dimension):
    if dimension == 0:
        return np.zeros((0, len(matrices)), dtype=np.int64)
    tri = np.triu_indices(dimension)
    return np.column_stack([H[tri] for H in matrices]) % P


def local_normal_certificate(D, R, J, Q, source):
    G = source["Gprim_mod25"]
    K, first_form, e1 = first_radical_form(G)
    e0 = rank_mod5(G % P)
    ege2 = R * J - e0 - e1
    sites = source["sites"]
    U = source["U"]
    divided = source["divided_rows"]
    full_differentials = []
    normal_differentials = []
    local_site_records = []
    lifts_checked = 0
    for z in sites:
        base, candidates = local_norm_line(z, D)
        baseline = pair_gram(z, D, R, J, U, divided)
        H1 = None
        site_record = {"site": z, "lift_count": len(candidates)}
        old_tag = signed_ray125_tag(z, D)
        for k in range(P):
            lifted = ((z[0] + 25 * k * base[0]) % TOP,
                      (z[1] + 25 * k * base[1]) % TOP)
            assert norm(lifted, D, TOP) == norm(z, D, TOP), (
                "local lift changed norm mod125", D, z, k)
            new_tag = signed_ray125_tag(lifted, D)
            assert old_tag[0] == new_tag[0], (
                "local lift changed tame signed ray tag", D, z, k)
            assert tuple(x % P for x in old_tag[1]) == tuple(
                x % P for x in new_tag[1]), (
                "local lift changed first wild digit", D, z, k)
            shifted = pair_gram(lifted, D, R, J, U, divided)
            diff = (shifted - baseline) % MOD
            assert np.array_equal(diff, diff.T)
            assert not np.any(diff % P)
            Hk = (diff // P) % P
            if k == 0:
                assert not np.any(Hk)
            elif k == 1:
                H1 = Hk
            else:
                assert H1 is not None
                assert np.array_equal(Hk, (k * H1) % P), (
                    "local Gram differential not F5-linear", D, z, k)
            if K.shape[1]:
                N = (K.T @ Hk @ K) % P
                assert np.array_equal(N, N.T)
                if k == 1:
                    normal_differentials.append(N)
            lifts_checked += 1
        assert H1 is not None
        full_differentials.append(H1)
        local_site_records.append(site_record)

    full_span = upper_vectors(full_differentials, R * J)
    full_span_rank = rank_mod5(full_span)
    normal_span = upper_vectors(normal_differentials, K.shape[1])
    normal_span_rank = rank_mod5(normal_span)
    return {
        "D": D, "R": R, "J": J,
        "primitive_Gram_rank_mod5": e0,
        "primitive_radical_dimension": K.shape[1],
        "primitive_first_radical_form_rank_e1": e1,
        "primitive_first_two_Smith_layers_mod25": [e0, e1, ege2],
        "local_norm_preserving_lifts_per_signed_site": P,
        "signed_5unit_sites": len(sites),
        "all_local_lifts_checked": lifts_checked,
        "all_local_norms_preserved_mod125": True,
        "all_first_wild_digits_preserved": True,
        "all_local_differentials_symmetric": True,
        "all_local_differentials_linear_in_F5_parameter": True,
        "full_symmetric_primitive_Gram_differential_span_rank": full_span_rank,
        "radical_normal_image_dimension": normal_span_rank,
        "radical_normal_image_is_zero": normal_span_rank == 0,
        "no_determinant_valuation_inferred": True
    }


def build_arm(name, D, rho, R, J, Q):
    src = source_gram_certificate(Q, D, R, J)
    local = local_normal_certificate(D, R, J, Q, src)
    return {
        "name": name,
        "field": field_certificate(D),
        "source_order": "maximal-order",
        "rho": rho,
        "norm_cutoff": rho * rho,
        "source": src["support_metadata"],
        "local_normal": local
    }


def run_cross_field_certificate():
    field_data = {D: field_certificate(D) for D in FIELDS}
    ray_data = {}
    for D in FIELDS:
        _, meta = exhaustive_lift_table(D)
        assert meta["unit_mod125_count"] == 15000
        assert meta["signed_unit_ray125_count"] == 7500
        assert meta["p_adic_two_digit_wild_values_per_exact_residue"] == 625
        ray_data[D] = {
            "unit_mod125_count": meta["unit_mod125_count"],
            "signed_unit_ray125_count": meta["signed_unit_ray125_count"],
            "p_adic_two_digit_wild_values_per_exact_residue":
                meta["p_adic_two_digit_wild_values_per_exact_residue"],
            "twisted_defect_and_corrected_log_product_tests":
                meta["twisted_defect_and_corrected_log_product_tests"],
            "conjugation_and_signed_invariance_all_units_checked":
                meta["conjugation_and_signed_invariance_all_units_checked"]
        }

    arms = []
    # D163 source-completion control: old even suborder vs full maximal order.
    Q163 = maximal_order_source(163, 21)
    Q163_even = tuple(z for z in Q163 if z[1] % 2 == 0)
    Q163_old = old_integer_order_source_D163(21)
    assert len(Q163) == 225 and len(Q163_even) == 109
    assert set(Q163_even) == set(Q163_old)
    arms.append(build_arm("D163-even-legacy-control", 163, 21, 40, 1, Q163_even))
    arms.append(build_arm("D163-full-maximal", 163, 21, 40, 1, Q163))

    # Matched diagnostic: same norm cutoff, 40 original monomial rows, J=1.
    for D in (187, 203):
        Q = maximal_order_source(D, 21)
        assert len({(a % P, b % P) for a, b in Q}) == 25
        arms.append(build_arm(f"D{D}-matched-R40-J1", D, 21, 40, 1, Q))

    # Native original-source geometry, derived from the frozen parameter rule.
    for D in (187, 203):
        rho = exact_rho(D)
        R = D // 4
        J = R // 25
        assert (rho, R, J) == ({187: (23, 46, 1), 203: (24, 50, 2)}[D])
        Q = maximal_order_source(D, rho)
        arms.append(build_arm(f"D{D}-native-R{R}-J{J}", D, rho, R, J, Q))

    byname = {a["name"]: a for a in arms}
    # Required D163 regressions from Phase318/319.
    old = byname["D163-even-legacy-control"]["local_normal"]
    full = byname["D163-full-maximal"]["local_normal"]
    assert old["primitive_Gram_rank_mod5"] == 23
    assert old["primitive_radical_dimension"] == 17
    assert old["primitive_first_radical_form_rank_e1"] == 7
    assert old["radical_normal_image_dimension"] == 1
    assert full["primitive_Gram_rank_mod5"] == 40
    assert full["primitive_radical_dimension"] == 0
    assert full["radical_normal_image_dimension"] == 0
    assert full["full_symmetric_primitive_Gram_differential_span_rank"] == 10

    # The D203 R50,J2 arm here uses the full maximal-order norm ball.
    # It is deliberately NOT identified with any earlier integer-order
    # D203 experiment; source completion is one of the variables under test.
    d203_native = byname["D203-native-R50-J2"]["local_normal"]
    assert d203_native["R"] * d203_native["J"] == 100
    assert (d203_native["primitive_Gram_rank_mod5"]
            + d203_native["primitive_radical_dimension"]) == 100

    return {
        "fields": field_data,
        "local_conductor125_unit_group_replays": ray_data,
        "arms": arms,
        "D163_source_completion_regression": {
            "even_order_points": 109,
            "full_maximal_order_points": 225,
            "even_primitive_radical_dimension": 17,
            "full_primitive_radical_dimension": 0,
            "even_radical_normal_image_dimension": 1,
            "full_radical_normal_image_dimension": 0
        },
        "D203_native_maximal_order_geometry": {
            "R": 50, "J": 2, "rows": 100,
            "primitive_rank_mod5": d203_native["primitive_Gram_rank_mod5"],
            "primitive_radical_dimension": d203_native["primitive_radical_dimension"],
            "source_is_full_maximal_order_not_original_integer_order": True
        },
        "global_class_group_boundary": {
            "D163_class_number": 1,
            "D187_class_number": 2,
            "D203_class_number": 4,
            "D163_global_split_prime_character_family_not_transferred": True,
            "nonprincipal_ideal_classes_require_ideal_aware_global_ray_model": True
        },
        "no_field_uniform_valuation_or_cutoff_claim": True
    }


def main():
    data = run_cross_field_certificate()
    print("PHASE320_CROSS_FIELD_MAXIMAL_ORDER_WILD_NORMAL_PASS", data, flush=True)


if __name__ == "__main__":
    main()
