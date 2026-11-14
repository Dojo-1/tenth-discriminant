#!/usr/bin/env python3
"""Phase321-B: exact ray-group invariant factors and cyclic-section tests."""
from math import prod

from ideal_aware_ray_class import (
    FIELDS, ray_group_certificate, local_unit_representatives,
    alpha_mod, local_mul, class_group_element_orders
)


def factor_integer(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def log_prime_power(n, p):
    k = 0
    while n > 1 and n % p == 0:
        n //= p
        k += 1
    assert n == 1, ("torsion count is not a p-power", p, n)
    return k


def ray_group_context(D):
    cert, forms, ideals, identity, table, alpha, inverses = ray_group_certificate(D)
    units = local_unit_representatives(D)
    local_alpha = [[alpha_mod(alpha[c][d], D) for d in range(len(forms))]
                   for c in range(len(forms))]
    return cert, forms, identity, table, alpha, inverses, units, local_alpha


def fast_ray_mul(x, y, D, table, local_alpha):
    c, u = x
    d, v = y
    e = table[c][d]
    uv = local_mul(u, v, D)
    return (e, local_mul(uv, local_alpha[c][d], D))


def ray_pow(x, exponent, D, table, local_alpha, identity):
    out = identity
    base = x
    n = exponent
    while n:
        if n & 1:
            out = fast_ray_mul(out, base, D, table, local_alpha)
        base = fast_ray_mul(base, base, D, table, local_alpha)
        n >>= 1
    return out


def invariant_factors_from_primary(primary):
    width = max(len(exponents) for exponents in primary.values())
    aligned = {
        p: [0] * (width - len(exponents)) + list(exponents)
        for p, exponents in primary.items()
    }
    factors = tuple(prod(p ** aligned[p][i] for p in aligned)
                    for i in range(width))
    assert all(factors[i + 1] % factors[i] == 0
               for i in range(len(factors) - 1))
    return factors


def p_torsion_counts(D):
    cert, forms, identity_class, table, alpha, inverses, units, local_alpha = ray_group_context(D)
    h = len(forms)
    identity = (identity_class, (1, 0))
    elements = tuple((c, u) for c in range(h) for u in units)
    order = len(elements)
    factors = factor_integer(order)
    result = {}
    for p, max_exp in factors.items():
        counts = [1] + [0] * max_exp
        for g in elements:
            x = g
            for k in range(1, max_exp + 1):
                x = ray_pow(x, p, D, table, local_alpha, identity)
                if x == identity:
                    counts[k] += 1
        logs = [0] + [log_prime_power(counts[k], p)
                      for k in range(1, max_exp + 1)]
        at_least = [0] * (max_exp + 2)
        for k in range(1, max_exp + 1):
            at_least[k] = logs[k] - logs[k - 1]
            assert at_least[k] >= 0
        exponents = []
        for k in range(1, max_exp + 1):
            multiplicity = at_least[k] - at_least[k + 1]
            assert multiplicity >= 0
            exponents.extend([k] * multiplicity)
        assert sum(exponents) == factors[p]
        result[p] = {
            "p": p,
            "max_exponent": max_exp,
            "torsion_counts": tuple(counts),
            "torsion_log_p": tuple(logs),
            "factors_with_exponent_at_least_k": tuple(at_least[1:max_exp + 1]),
            "primary_cyclic_exponents": tuple(sorted(exponents)),
            "p_primary_order": counts[max_exp]
        }
    primary = {p: row["primary_cyclic_exponents"] for p, row in result.items()}
    invariant_factors = invariant_factors_from_primary(primary)
    assert prod(invariant_factors) == order
    exponent = invariant_factors[-1]
    for g in elements:
        assert ray_pow(g, exponent, D, table, local_alpha, identity) == identity
    exponent_witnesses = {}
    for p in factors:
        witness = next((g for g in elements
                        if ray_pow(g, exponent // p, D, table, local_alpha, identity)
                        != identity), None)
        assert witness is not None
        exponent_witnesses[p] = witness
    return {
        "D": D,
        "ray_group_order": order,
        "prime_factorization": factors,
        "p_primary": result,
        "invariant_factors": invariant_factors,
        "group_exponent": exponent,
        "group_exponent_checked_on_every_element": True,
        "exponent_witnesses": exponent_witnesses
    }, (forms, identity_class, table, alpha, inverses, units, local_alpha)


def local_pow(x, exponent, D):
    out = (1, 0)
    base = x
    n = exponent
    while n:
        if n & 1:
            out = local_mul(out, base, D)
        base = local_mul(base, base, D)
        n >>= 1
    return out


def element_order(g, group_order, D, table, local_alpha, identity):
    order = group_order
    for p, exponent in factor_integer(group_order).items():
        for _ in range(exponent):
            if ray_pow(g, order // p, D, table, local_alpha, identity) == identity:
                order //= p
            else:
                break
    return order


def local_element_order(u, D):
    order = 7500
    for p, exponent in factor_integer(7500).items():
        for _ in range(exponent):
            if local_pow(u, order // p, D) == (1, 0):
                order //= p
            else:
                break
    return order


def cyclic_section_test(D, context):
    forms, identity_class, table, alpha, inverses, units, local_alpha = context
    h = len(forms)
    identity = (identity_class, (1, 0))
    orders = class_group_element_orders(table, identity_class)
    if h == 1:
        return {"D": D, "ordinary_class_group_order": 1,
                "splits": True, "reason": "trivial quotient",
                "section_lift_count": 1, "section_lifts": ((1, 0),),
                "first_section_lift": (1, 0),
                "canonical_lift_order": 1, "canonical_lift_power_h": identity,
                "canonical_lift_power_order": 1}
    generator = next(i for i, n in enumerate(orders) if n == h)
    lifts = []
    for u in units:
        g = (generator, u)
        if ray_pow(g, h, D, table, local_alpha, identity) == identity:
            lifts.append(u)
    canonical_lift = (generator, (1, 0))
    canonical_power = ray_pow(canonical_lift, h, D, table, local_alpha, identity)
    assert canonical_power[0] == identity_class
    return {
        "D": D,
        "ordinary_class_group_order": h,
        "generator_class_index": generator,
        "splits": bool(lifts),
        "section_lift_count": len(lifts),
        "section_lifts": tuple(lifts),
        "first_section_lift": lifts[0] if lifts else None,
        "all_7500_local_lifts_exhausted": True,
        "canonical_lift_order": element_order(
            canonical_lift, h * 7500, D, table, local_alpha, identity),
        "canonical_lift_power_h": canonical_power,
        "canonical_lift_power_order": local_element_order(canonical_power[1], D)
    }


def direct_product_invariants(local_kernel_factors, h):
    primary = {}
    for n in list(local_kernel_factors) + [h]:
        for p, e in factor_integer(n).items():
            primary.setdefault(p, []).append(e)
    normalized = {
        p: tuple(sorted(exponents)) for p, exponents in primary.items()
    }
    return invariant_factors_from_primary(normalized)


def run_phase321b():
    results = []
    sections = []
    for D in FIELDS:
        inv, context = p_torsion_counts(D)
        sections.append(cyclic_section_test(D, context))
        h = len(context[0])
        inv["split_direct_product_invariant_factors"] = direct_product_invariants((25, 300), h)
        inv["ray_extension_splits"] = sections[-1]["splits"]
        inv["ray_invariant_factors_match_split_product"] = (
            inv["invariant_factors"] == inv["split_direct_product_invariant_factors"]
        )
        results.append(inv)
    return {"invariant_factor_results": results, "cyclic_section_tests": sections}


def main():
    print("PHASE321B_RAY_INVARIANT_FACTORS_PASS", run_phase321b(), flush=True)


if __name__ == "__main__":
    main()
