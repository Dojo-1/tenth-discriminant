#!/usr/bin/env python3
"""Phase321: exact ideal-aware ray class groups modulo 125.

Constructs Cl_(125)(Q(sqrt(-D))) for D=163,187,203 using exact
rank-two ideal lattices, reduced-form representatives and the full
extension cocycle. No principal-generator shortcut is used for a
nonprincipal ideal class.
"""
from fractions import Fraction
from math import gcd, isqrt, lcm
from itertools import product
import hashlib
import json

FIELDS = (163, 187, 203)
MOD = 125
EXPECTED_H = {163: 1, 187: 2, 203: 4}


def m_parameter(D):
    assert D > 3 and D % 4 == 3
    return (D + 1) // 4


def mul(x, y, D):
    """Multiply integer coordinate pairs in O_D=Z[omega]."""
    a, b = x
    c, d = y
    m = m_parameter(D)
    return (a * c - m * b * d, a * d + b * c + b * d)


def mul_mod(x, y, D, modulus):
    z = mul(x, y, D)
    return (z[0] % modulus, z[1] % modulus)


def conjugate(z):
    a, b = z
    return (a + b, -b)


def norm(z, D):
    a, b = z
    return a * a + a * b + m_parameter(D) * b * b


def norm_mod(z, D, modulus):
    return norm(z, D) % modulus


def extended_gcd(a, b):
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if a < 0:
        old_s = -old_s
    if b < 0:
        old_t = -old_t
    return old_r, old_s, old_t


def hnf(generators):
    """Column HNF [[h,u],[0,g]], 0<=u<h, for a rank-two lattice."""
    assert len(generators) >= 2
    g = 0
    x_at_g = 0
    for x, y in generators:
        g2, s, t = extended_gcd(g, y)
        x_at_g = s * x_at_g + t * x
        g = g2
    assert g > 0, ("lattice has zero second-coordinate projection", generators)
    determinant_gcd = 0
    for i in range(len(generators)):
        x1, y1 = generators[i]
        for j in range(i + 1, len(generators)):
            x2, y2 = generators[j]
            determinant_gcd = gcd(
                determinant_gcd, abs(x1 * y2 - x2 * y1)
            )
    assert determinant_gcd > 0
    assert determinant_gcd % g == 0
    h = determinant_gcd // g
    assert h > 0
    u = x_at_g % h
    for x, y in generators:
        assert y % g == 0
        assert (x - (y // g) * u) % h == 0
    return (h, u, g)


def ideal_basis(I):
    h, u, g = I
    return ((h, 0), (u, g))


def ideal_norm(I):
    h, _, g = I
    return h * g


def reduced_forms(D):
    """All reduced primitive positive forms of discriminant -D."""
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


def form_ideal(form):
    """I=(a, omega-(b+1)/2), as column HNF."""
    a, b, _ = form
    assert (b + 1) % 2 == 0
    t = (b + 1) // 2
    return (a, (-t) % a, 1)


def ideal_product(I, J, D):
    products = [mul(x, y, D) for x in ideal_basis(I) for y in ideal_basis(J)]
    K = hnf(products)
    assert ideal_norm(K) == ideal_norm(I) * ideal_norm(J)
    return K


def alpha_times_vector(alpha_num, q, v, D):
    """((A+B*omega)/q) times an integer vector, as Fractions."""
    A, B = alpha_num
    x, y = v
    z = mul((A, B), (x, y), D)
    return (Fraction(z[0], q), Fraction(z[1], q))


def canonical_alpha(alpha):
    a, b = alpha
    if a < 0 or (a == 0 and b < 0):
        return (-a, -b)
    return (a, b)


def scaled_ideal_hnf(alpha_num, q, I, D):
    vectors = [alpha_times_vector(alpha_num, q, v, D) for v in ideal_basis(I)]
    if any(x.denominator != 1 or y.denominator != 1 for x, y in vectors):
        return None
    return hnf([(int(x), int(y)) for x, y in vectors])


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def find_scaling_alpha(source_ideal, target_ideal, D):
    """Find alpha with source_ideal=(alpha)*target_ideal, modulo +/-1."""
    source_norm = ideal_norm(source_ideal)
    target_norm = ideal_norm(target_ideal)
    found = {}
    target_h = target_ideal[0]
    for q in divisors(target_h):
        scaled_norm = Fraction(source_norm * q * q, target_norm)
        if scaled_norm.denominator != 1:
            continue
        N = int(scaled_norm)
        Bmax = isqrt((4 * N) // D)
        for B in range(-Bmax, Bmax + 1):
            Amax = isqrt(N) + abs(B) + 2
            for A in range(-Amax, Amax + 1):
                if gcd(gcd(abs(A), abs(B)), q) != 1:
                    continue
                if A * A + A * B + m_parameter(D) * B * B != N:
                    continue
                if scaled_ideal_hnf((A, B), q, target_ideal, D) != source_ideal:
                    continue
                alpha = canonical_alpha((Fraction(A, q), Fraction(B, q)))
                found[alpha] = True
    return tuple(found)


def ideal_class_data(D):
    forms = reduced_forms(D)
    assert len(forms) == EXPECTED_H[D], (D, forms)
    ideals = tuple(form_ideal(f) for f in forms)
    assert all(gcd(ideal_norm(I), MOD) == 1 for I in ideals)
    identity = forms.index((1, 1, m_parameter(D)))
    h = len(forms)
    table = [[None] * h for _ in range(h)]
    alpha = [[None] * h for _ in range(h)]
    for i in range(h):
        for j in range(h):
            product_ideal = ideal_product(ideals[i], ideals[j], D)
            matches = []
            for k in range(h):
                candidates = find_scaling_alpha(product_ideal, ideals[k], D)
                if candidates:
                    matches.append((k, candidates))
            assert len(matches) == 1, (D, i, j, product_ideal, matches)
            k, candidates = matches[0]
            assert len(candidates) == 1, (D, i, j, k, candidates)
            table[i][j] = k
            alpha[i][j] = candidates[0]
    class_associativity_checks = 0
    for i in range(h):
        assert table[identity][i] == i and table[i][identity] == i
        assert canonical_alpha(alpha[identity][i]) == (Fraction(1), Fraction(0))
        assert canonical_alpha(alpha[i][identity]) == (Fraction(1), Fraction(0))
    for i in range(h):
        for j in range(h):
            for k in range(h):
                assert table[table[i][j]][k] == table[i][table[j][k]]
                class_associativity_checks += 1
    for i in range(h):
        for j in range(h):
            assert table[i][j] == table[j][i]
            assert canonical_alpha(alpha[i][j]) == canonical_alpha(alpha[j][i])
    inverses = []
    for i in range(h):
        candidates = [j for j in range(h) if table[i][j] == identity]
        assert len(candidates) == 1
        inverses.append(candidates[0])
    return forms, ideals, identity, table, alpha, tuple(inverses), class_associativity_checks


def alpha_mul(x, y, D):
    """Exact multiplication of two rational quadratic elements."""
    a, b = x
    c, d = y
    m = m_parameter(D)
    return canonical_alpha((a * c - m * b * d, a * d + b * c + b * d))


def alpha_mod(alpha, D, modulus=MOD):
    a, b = alpha
    q = lcm(a.denominator, b.denominator)
    A = a.numerator * (q // a.denominator)
    B = b.numerator * (q // b.denominator)
    common = gcd(gcd(abs(A), abs(B)), q)
    A, B, q = A // common, B // common, q // common
    assert gcd(q, modulus) == 1
    qi = pow(q, -1, modulus)
    out = ((A * qi) % modulus,
           (B * qi) % modulus)
    assert norm_mod(out, D, 5) != 0
    neg = ((-out[0]) % modulus, (-out[1]) % modulus)
    return min(out, neg)


def local_unit_representatives(D):
    units = []
    for a, b in product(range(MOD), repeat=2):
        z = (a, b)
        if norm_mod(z, D, 5) != 0:
            neg = ((-a) % MOD, (-b) % MOD)
            if z < neg:
                units.append(z)
    units = tuple(sorted(units))
    assert len(units) == 7500
    assert len(set(units)) == 7500
    assert all(norm_mod(z, D, 5) != 0 for z in units)
    return units


def local_mul(x, y, D):
    z = mul_mod(x, y, D, MOD)
    neg = ((-z[0]) % MOD, (-z[1]) % MOD)
    return min(z, neg)


def local_inverse(x, D):
    n = norm_mod(x, D, MOD)
    assert gcd(n, MOD) == 1
    bar = conjugate(x)
    invn = pow(n, -1, MOD)
    z = ((bar[0] * invn) % MOD, (bar[1] * invn) % MOD)
    neg = ((-z[0]) % MOD, (-z[1]) % MOD)
    return min(z, neg)


def ray_multiply(x, y, D, class_table, alpha_table):
    c, u = x
    d, v = y
    e = class_table[c][d]
    cocycle = alpha_mod(alpha_table[c][d], D)
    return (e, local_mul(local_mul(u, v, D), cocycle, D))


def class_group_element_orders(table, identity):
    orders = []
    for c in range(len(table)):
        x = identity
        for n in range(1, len(table) + 1):
            x = table[x][c]
            if x == identity:
                orders.append(n)
                break
        else:
            raise AssertionError(("class element order not found", c))
    return tuple(orders)


def ray_group_certificate(D):
    forms, ideals, identity, class_table, alpha_table, inverses, class_assoc = ideal_class_data(D)
    units = local_unit_representatives(D)
    h = len(forms)
    cocycle_checks = 0
    for c in range(h):
        for d in range(h):
            for e in range(h):
                lhs = alpha_mul(alpha_table[c][d],
                                alpha_table[class_table[c][d]][e], D)
                rhs = alpha_mul(alpha_table[d][e],
                                alpha_table[c][class_table[d][e]], D)
                assert lhs == rhs, ("cocycle associativity", D, c, d, e, lhs, rhs)
                cocycle_checks += 1
    local_alpha = [[alpha_mod(alpha_table[c][d], D) for d in range(h)]
                   for c in range(h)]
    for c in range(h):
        for d in range(h):
            assert norm_mod(local_alpha[c][d], D, 5) != 0
    identity_pair = (identity, (1, 0))
    total = h * len(units)
    inverse_checks = 0
    for c in range(h):
        d = inverses[c]
        cocycle = local_alpha[c][d]
        for u in units:
            v = local_inverse(local_mul(u, cocycle, D), D)
            g = (c, u)
            inv_g = (d, v)
            assert ray_multiply(g, inv_g, D, class_table, alpha_table) == identity_pair
            assert ray_multiply(inv_g, g, D, class_table, alpha_table) == identity_pair
            inverse_checks += 1
    assert total == EXPECTED_H[D] * 7500
    assert len(units) == 7500
    # The kernel is exactly the local signed unit group; D=163 is its local-only case.
    kernel = tuple((identity, u) for u in units)
    assert len(kernel) == 7500
    if D == 163:
        assert h == 1 and all(alpha_table[0][0] == (Fraction(1), Fraction(0)) for _ in (0,))
        for u in units:
            for v in units[:17]:
                assert ray_multiply((0, u), (0, v), D, class_table, alpha_table) == (
                    0, local_mul(u, v, D)
                )
    return {
        "D": D,
        "discriminant": -D,
        "class_number": h,
        "reduced_forms": forms,
        "ordinary_class_group_table": tuple(tuple(row) for row in class_table),
        "ordinary_class_group_inverses": inverses,
        "ordinary_class_group_element_orders": class_group_element_orders(class_table, identity),
        "ordinary_class_group_associativity_checks": class_assoc,
        "ray_cocycle_residues_mod125": tuple(tuple(alpha_mod(alpha_table[c][d], D)
                                                       for d in range(h))
                                                 for c in range(h)),
        "local_unit_count_mod125": 15000,
        "signed_local_ray_kernel_order": len(units),
        "ray_class_group_order": total,
        "expected_ray_class_group_order": EXPECTED_H[D] * 7500,
        "exact_ideal_product_scalings": h * h,
        "exact_cocycle_associativity_checks": cocycle_checks,
        "exact_cocycle_commutativity_checks": h * h,
        "full_ray_group_inverse_checks": inverse_checks,
        "full_ray_group_identity_and_inverse_verified": True,
        "extension_not_assumed_split": True,
        "D163_reduces_to_Phase315_local_signed_unit_group": D == 163,
        "no_class_number_one_shortcut": True
    }, forms, ideals, identity, class_table, alpha_table, inverses


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for p in range(3, isqrt(n) + 1, 2):
        if n % p == 0:
            return False
    return True


def prime_ideal_lattices(p, D):
    """Return (type, root, ideal HNF) for primes above p."""
    m = m_parameter(D)
    roots = [r for r in range(p) if (r * r - r + m) % p == 0]
    if len(roots) == 0:
        return (("inert", None, (p, 0, p)),)
    if len(roots) == 1:
        r = roots[0]
        return (("ramified", r, (p, (-r) % p, 1)),)
    assert len(roots) == 2
    return tuple(("split", r, (p, (-r) % p, 1)) for r in roots)


def map_prime_ideal_to_ray(Ip, D, ideals, class_table, alpha_table):
    matches = []
    for c, Ic in enumerate(ideals):
        candidates = find_scaling_alpha(Ip, Ic, D)
        if candidates:
            assert len(candidates) == 1
            matches.append((c, candidates[0]))
    assert len(matches) == 1, ("prime ideal class map", D, Ip, matches)
    c, alpha = matches[0]
    residue = alpha_mod(alpha, D)
    assert norm_mod(residue, D, 5) != 0
    return (c, residue)


def prime_ideal_catalog(D, ideals, class_table, alpha_table):
    records = []
    split_pairs = 0
    ramified_squares = 0
    for p in range(2, 442):
        if not is_prime(p) or p == 5:
            continue
        primes = prime_ideal_lattices(p, D)
        if primes[0][0] == "inert":
            typ, root, I = primes[0]
            assert I == (p, 0, p)
            ray = map_prime_ideal_to_ray(I, D, ideals, class_table, alpha_table)
            records.append({"p": p, "type": typ, "root": None,
                            "ideal_hnf": I, "ray_class": ray})
        elif primes[0][0] == "ramified":
            typ, root, I = primes[0]
            square = ideal_product(I, I, D)
            assert square == (p, 0, p), ("ramified prime square", D, p, I, square)
            ray = map_prime_ideal_to_ray(I, D, ideals, class_table, alpha_table)
            records.append({"p": p, "type": typ, "root": root,
                            "ideal_hnf": I, "ray_class": ray})
            ramified_squares += 1
        else:
            (typ1, r1, I1), (typ2, r2, I2) = primes
            assert ideal_product(I1, I2, D) == (p, 0, p), (
                "split conjugate product", D, p, I1, I2,
                ideal_product(I1, I2, D)
            )
            ray1 = map_prime_ideal_to_ray(I1, D, ideals, class_table, alpha_table)
            ray2 = map_prime_ideal_to_ray(I2, D, ideals, class_table, alpha_table)
            assert class_table[ray1[0]][ray2[0]] == 0
            records.append({"p": p, "type": "split", "root": r1,
                            "ideal_hnf": I1, "ray_class": ray1})
            records.append({"p": p, "type": "split", "root": r2,
                            "ideal_hnf": I2, "ray_class": ray2})
            split_pairs += 1
    catalog_bytes = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return {
        "D": D,
        "rational_prime_bound": 441,
        "prime_5_excluded_from_ray_group": True,
        "prime_ideal_records": len(records),
        "split_rational_primes": split_pairs,
        "ramified_rational_primes": ramified_squares,
        "nonprincipal_prime_ideal_records": sum(1 for r in records if r["ray_class"][0] != 0),
        "all_split_conjugate_products_verified": True,
        "all_ramified_squares_verified": True,
        "every_prime_ideal_mapped_into_full_ray_group": True,
        "catalog_sha256": hashlib.sha256(catalog_bytes).hexdigest(),
        "records": records
    }


def run_phase321():
    output = []
    catalogs = []
    for D in FIELDS:
        cert, forms, ideals, identity, table, alpha, inverses = ray_group_certificate(D)
        catalog = prime_ideal_catalog(D, ideals, table, alpha)
        output.append(cert)
        catalogs.append(catalog)
    return {"ray_groups": output, "prime_ideal_catalogs": catalogs}


def main():
    result = run_phase321()
    summary = {
        "ray_groups": [
            {k: v for k, v in row.items() if k != "ordinary_class_group_table"}
            for row in result["ray_groups"]
        ],
        "prime_ideal_catalogs": [
            {k: v for k, v in row.items() if k != "records"}
            for row in result["prime_ideal_catalogs"]
        ]
    }
    print("PHASE321_IDEAL_AWARE_RAY_CLASS_GROUP_PASS", summary, flush=True)


if __name__ == "__main__":
    main()
