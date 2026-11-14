#!/usr/bin/env python3
"""Phase322: exact dual characters, conductors and bounded prime-ideal values."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, lcm
import hashlib
import json
import struct

from ideal_aware_ray_class import (
    FIELDS,
    alpha_mod,
    class_group_element_orders,
    local_mul,
    local_unit_representatives,
    norm_mod,
    prime_ideal_catalog,
    ray_group_certificate,
)
from ray_invariant_factors import (
    cyclic_section_test,
    local_element_order,
    ray_pow,
    fast_ray_mul,
)


MOD = 125
EXPECTED_LOCAL_ORDERS = (25, 300)
EXPECTED_RAY_ORDERS = {163: 7500, 187: 15000, 203: 30000}
EXPECTED_CONDUCTORS = {
    163: {1: 1, 5: 11, 25: 288, 125: 7200},
    187: {1: 2, 5: 22, 25: 576, 125: 14400},
    203: {1: 4, 5: 44, 25: 1152, 125: 28800},
}
EXPECTED_KERNEL_ORDERS = {1: 7500, 5: 625, 25: 25, 125: 1}


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


def canonical_signed_mod(z, modulus):
    if modulus == 1:
        return (0, 0)
    a, b = z
    residue = (a % modulus, b % modulus)
    negative = ((-residue[0]) % modulus, (-residue[1]) % modulus)
    return min(residue, negative)


def local_units_mod(D, modulus):
    if modulus == 1:
        return ((0, 0),)
    units = []
    for a, b in product(range(modulus), repeat=2):
        z = (a, b)
        if norm_mod(z, D, 5) == 0:
            continue
        negative = ((-a) % modulus, (-b) % modulus)
        if z < negative:
            units.append(z)
    return tuple(sorted(units))


def local_mul_mod(x, y, D, modulus):
    if modulus == 1:
        return (0, 0)
    a, b = x
    c, d = y
    m = (D + 1) // 4
    z = (a * c - m * b * d, a * d + b * c + b * d)
    residue = (z[0] % modulus, z[1] % modulus)
    negative = ((-residue[0]) % modulus, (-residue[1]) % modulus)
    return min(residue, negative)


def local_group_generators(D, units):
    orders = {u: local_element_order(u, D) for u in units}
    candidates_300 = [u for u in units if orders[u] == 300]
    candidates_25 = [u for u in units if orders[u] == 25]
    assert candidates_300 and candidates_25
    for u300 in candidates_300:
        subgroup_300 = {local_pow(u300, b, D) for b in range(300)}
        assert len(subgroup_300) == 300
        for u25 in candidates_25:
            # The unique order-five subgroup of <u25> must not meet <u300>.
            if local_pow(u25, 5, D) in subgroup_300:
                continue
            generated = {
                local_mul(local_pow(u25, a, D), local_pow(u300, b, D), D)
                for a in range(25) for b in range(300)
            }
            if len(generated) == 7500:
                return u25, u300, generated
    raise AssertionError(("no C25 x C300 local generator pair", D))


def coordinate_add(x, y, n1, n2):
    return ((x[0] + y[0]) % n1, (x[1] + y[1]) % n2)


def coordinate_order(x, n1, n2):
    return lcm(n1 // gcd(n1, x[0]), n2 // gcd(n2, x[1]))


def generated_coordinate_subgroup(generators, n1, n2):
    subgroup = {(0, 0)}
    for generator in generators:
        order = coordinate_order(generator, n1, n2)
        powers = {
            ((k * generator[0]) % n1, (k * generator[1]) % n2)
            for k in range(order)
        }
        subgroup = {
            coordinate_add(x, y, n1, n2)
            for x in subgroup for y in powers
        }
    return subgroup


def subgroup_generators(coordinates, n1, n2):
    target = set(coordinates)
    generators = []
    current = {(0, 0)}
    for element in sorted(target):
        if element not in current:
            generators.append(element)
            current = generated_coordinate_subgroup(generators, n1, n2)
            if current == target:
                break
    assert current == target, ("failed to generate conductor kernel", len(current), len(target))
    assert len(generators) <= 2
    return tuple(generators)


def ray_context(D):
    cert, forms, ideals, identity_class, table, alpha, inverses = ray_group_certificate(D)
    units = local_unit_representatives(D)
    local_alpha = [[alpha_mod(alpha[c][d], D) for d in range(len(forms))]
                   for c in range(len(forms))]
    context = (forms, identity_class, table, alpha, inverses, units, local_alpha)
    section = cyclic_section_test(D, context)
    return cert, forms, ideals, identity_class, table, alpha, inverses, units, local_alpha, section


def build_ray_coordinates(D, context):
    forms, identity_class, table, alpha, inverses, units, local_alpha = context
    h = len(forms)
    n1, n2 = 25 * h, 300
    identity = (identity_class, (1, 0))
    u25, u300, local_generated = local_group_generators(D, units)

    # The first explicit section lift has exact order h; D163 is trivial.
    section = (identity_class, (1, 0))
    if h > 1:
        section_class = next(i for i, order in enumerate(
            class_group_element_orders(table, identity_class)) if order == h)
        section_local = {
            187: (7, 103),
            203: (34, 23)
        }[D]
        section = (section_class, section_local)
        assert ray_pow(section, h, D, table, local_alpha, identity) == identity

    local25 = (identity_class, u25)
    g_small = fast_ray_mul(section, local25, D, table, local_alpha)
    g_large = (identity_class, u300)
    assert ray_pow(g_small, n1, D, table, local_alpha, identity) == identity
    assert ray_pow(g_large, n2, D, table, local_alpha, identity) == identity

    for p in (2, 5):
        if n1 % p == 0:
            assert ray_pow(g_small, n1 // p, D, table, local_alpha, identity) != identity
        if n2 % p == 0:
            assert ray_pow(g_large, n2 // p, D, table, local_alpha, identity) != identity
    assert fast_ray_mul(g_small, g_large, D, table, local_alpha) == fast_ray_mul(
        g_large, g_small, D, table, local_alpha
    )

    small_powers = [ray_pow(g_small, a, D, table, local_alpha, identity)
                    for a in range(n1)]
    large_powers = [ray_pow(g_large, b, D, table, local_alpha, identity)
                    for b in range(n2)]
    coordinate_map = {}
    for a, x in enumerate(small_powers):
        for b, y in enumerate(large_powers):
            element = fast_ray_mul(x, y, D, table, local_alpha)
            assert element not in coordinate_map, ("duplicate ray coordinate", D, a, b)
            coordinate_map[element] = (a, b)

    group_order = h * len(units)
    assert len(local_generated) == 7500
    assert len(coordinate_map) == group_order == n1 * n2
    all_elements = tuple((c, u) for c in range(h) for u in units)
    assert set(coordinate_map) == set(all_elements)

    # Check that the coordinate map respects multiplication by both generators
    # at every group element. This proves the full coordinate law from generators.
    for element, (a, b) in coordinate_map.items():
        next_small = fast_ray_mul(element, g_small, D, table, local_alpha)
        next_large = fast_ray_mul(element, g_large, D, table, local_alpha)
        assert coordinate_map[next_small] == ((a + 1) % n1, b)
        assert coordinate_map[next_large] == (a, (b + 1) % n2)

    return {
        "D": D,
        "h": h,
        "n1": n1,
        "n2": n2,
        "identity": identity,
        "table": table,
        "alpha": alpha,
        "local_alpha": local_alpha,
        "units": units,
        "g_small": g_small,
        "g_large": g_large,
        "u25": u25,
        "u300": u300,
        "section": section,
        "coordinate_map": coordinate_map,
        "all_elements": all_elements
    }


def reduce_ray_element(element, D, modulus):
    c, u = element
    return (c, canonical_signed_mod(u, modulus))


def ray_mul_at_modulus(x, y, D, table, alpha_at_modulus, modulus):
    c, u = x
    d, v = y
    e = table[c][d]
    uv = local_mul_mod(u, v, D, modulus)
    return (e, local_mul_mod(uv, alpha_at_modulus[c][d], D, modulus))


def conductor_kernels(D, model):
    n1, n2 = model["n1"], model["n2"]
    units = model["units"]
    identity_class = model["identity"][0]
    coordinate_map = model["coordinate_map"]
    alpha = model["alpha"]
    table = model["table"]
    g_small, g_large = model["g_small"], model["g_large"]
    all_elements = model["all_elements"]

    kernel_data = {}
    reduction_orders = {}
    for modulus in (1, 5, 25, 125):
        target_units = local_units_mod(D, modulus)
        image = {canonical_signed_mod(u, modulus) for u in units}
        assert image == set(target_units)
        kernel_units = tuple(
            u for u in units
            if canonical_signed_mod(u, modulus) == ((0, 0) if modulus == 1 else (1, 0))
        )
        expected = EXPECTED_KERNEL_ORDERS[modulus]
        assert len(kernel_units) == expected
        coordinates = {
            coordinate_map[(identity_class, u)]
            for u in kernel_units
        }
        assert len(coordinates) == expected
        generators = subgroup_generators(coordinates, n1, n2)
        assert generated_coordinate_subgroup(generators, n1, n2) == coordinates

        # Reduction is a homomorphism: check on every source element times
        # each of the two ray generators. The modulus-1 target is Cl(K).
        if modulus == 1:
            for element in all_elements:
                for generator in (g_small, g_large):
                    lhs = reduce_ray_element(
                        fast_ray_mul(element, generator, D, table, model["local_alpha"]),
                        D, modulus
                    )
                    rhs_class = table[element[0]][generator[0]]
                    assert lhs == (rhs_class, (0, 0))
        else:
            alpha_m = [[alpha_mod(alpha[c][d], D, modulus)
                        for d in range(len(table))] for c in range(len(table))]
            for element in all_elements:
                for generator in (g_small, g_large):
                    lhs = reduce_ray_element(
                        fast_ray_mul(element, generator, D, table, model["local_alpha"]),
                        D, modulus
                    )
                    rhs = ray_mul_at_modulus(
                        reduce_ray_element(element, D, modulus),
                        reduce_ray_element(generator, D, modulus),
                        D, table, alpha_m, modulus
                    )
                    assert lhs == rhs

        kernel_data[modulus] = {
            "order": len(coordinates),
            "generators": generators,
            "coordinate_elements": coordinates
        }
        reduction_orders[modulus] = len(target_units) * len(table)

    assert reduction_orders == {1: model["h"], 5: model["h"] * 12,
                                25: model["h"] * 300, 125: model["h"] * 7500}
    return kernel_data, reduction_orders


def character_trivial_on_kernel(i, j, generators, n1, n2):
    denominator = n1 * n2
    for a, b in generators:
        numerator = (i * a * n2 + j * b * n1) % denominator
        if numerator != 0:
            return False
    return True


def character_conductors(D, model, kernels):
    n1, n2 = model["n1"], model["n2"]
    conductor_by_character = {}
    counts = Counter()
    moduli = (1, 5, 25, 125)
    for i in range(n1):
        for j in range(n2):
            conductor = None
            for modulus in moduli:
                generators = kernels[modulus]["generators"]
                if character_trivial_on_kernel(i, j, generators, n1, n2):
                    conductor = modulus
                    break
            assert conductor is not None
            conductor_by_character[(i, j)] = conductor
            counts[conductor] += 1
    assert dict(counts) == EXPECTED_CONDUCTORS[D], (D, dict(counts))
    assert sum(counts.values()) == n1 * n2
    return conductor_by_character, dict(counts)


def exponent_numerator(i, j, coordinates, n1, n2):
    a, b = coordinates
    return (i * a * n2 + j * b * n1) % (n1 * n2)


def reduced_fraction_from_numerator(numerator, denominator):
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)


def evaluate_bounded_prime_ideals(D, model, catalog):
    n1, n2 = model["n1"], model["n2"]
    coordinate_map = model["coordinate_map"]
    records = catalog["records"]
    record_coordinates = [
        coordinate_map[tuple(record["ray_class"])]
        for record in records
    ]
    assert len(record_coordinates) == len(records)

    grouped = defaultdict(list)
    for index, record in enumerate(records):
        grouped[record["p"]].append((index, record, record_coordinates[index]))

    digest = hashlib.sha256()
    digest.update(json.dumps(
        [{k: v for k, v in record.items() if k != "ray_class"} for record in records],
        sort_keys=True, separators=(",", ":")
    ).encode())
    digest.update(struct.pack(">HH", n1, n2))

    relation_checks = 0
    character_count = n1 * n2
    denominator = n1 * n2
    sample_indices = ((0, 0), (1, 0), (0, 1), (n1 // 2, n2 // 2))
    samples = {}

    for i in range(n1):
        for j in range(n2):
            numerators = [
                exponent_numerator(i, j, coordinates, n1, n2)
                for coordinates in record_coordinates
            ]
            for record_index, (record, numerator) in enumerate(zip(records, numerators)):
                num, den = reduced_fraction_from_numerator(numerator, denominator)
                digest.update(struct.pack(">HHHHHH", i, j, record_index,
                                          record["p"], num, den))

            # Every prime-ideal relation is checked for every character:
            # inert (p), split conjugate product (p), ramified P^2=(p).
            for p, entries in grouped.items():
                principal = (model["identity"][0],
                            canonical_signed_mod((p, 0), MOD))
                principal_coordinates = coordinate_map[principal]
                principal_num = exponent_numerator(
                    i, j, principal_coordinates, n1, n2
                )
                if entries[0][1]["type"] == "split":
                    assert len(entries) == 2
                    nsum = sum(exponent_numerator(
                        i, j, entry[2], n1, n2) for entry in entries) % denominator
                    assert nsum == principal_num
                elif entries[0][1]["type"] == "inert":
                    assert len(entries) == 1
                    assert exponent_numerator(i, j, entries[0][2], n1, n2) == principal_num
                else:
                    assert entries[0][1]["type"] == "ramified"
                    assert len(entries) == 1
                    value = exponent_numerator(i, j, entries[0][2], n1, n2)
                    assert (2 * value) % denominator == principal_num
                relation_checks += 1

            if (i, j) in sample_indices:
                samples[f"{i},{j}"] = [
                    {
                        "p": record["p"],
                        "type": record["type"],
                        "root": record.get("root"),
                        "exponent": reduced_fraction_from_numerator(
                            numerators[index], denominator
                        )
                    }
                    for index, record in enumerate(records[:8])
                ]

    return {
        "catalog_sha256": catalog["catalog_sha256"],
        "prime_ideal_records": len(records),
        "character_count": character_count,
        "character_prime_ideal_evaluations": character_count * len(records),
        "prime_ideal_relation_checks": relation_checks,
        "evaluation_matrix_sha256": digest.hexdigest(),
        "sample_character_values_first_eight_prime_ideals": samples
    }


def run_phase322():
    results = []
    for D in FIELDS:
        cert, forms, ideals, identity_class, table, alpha, inverses, units, local_alpha, section = ray_context(D)
        context = (forms, identity_class, table, alpha, inverses, units, local_alpha)
        model = build_ray_coordinates(D, context)
        kernels, reduction_orders = conductor_kernels(D, model)
        conductors, conductor_counts = character_conductors(D, model, kernels)
        catalog = prime_ideal_catalog(D, ideals, table, alpha)
        evaluations = evaluate_bounded_prime_ideals(D, model, catalog)

        results.append({
            "D": D,
            "class_number": len(forms),
            "ray_group_order": len(model["all_elements"]),
            "ray_invariant_factors": [model["n1"], model["n2"]],
            "local_generators": {"order_25": model["u25"], "order_300": model["u300"]},
            "ray_generators": {"order_25h": model["g_small"], "order_300": model["g_large"]},
            "section_lift": model["section"],
            "coordinate_bijection_size": len(model["coordinate_map"]),
            "coordinate_generator_step_checks": 2 * len(model["coordinate_map"]),
            "local_reduction_orders": {
                str(k): len(local_units_mod(D, k)) for k in (1, 5, 25, 125)
            },
            "ray_reduction_orders": {str(k): v for k, v in reduction_orders.items()},
            "conductor_kernel_orders": {
                str(k): data["order"] for k, data in kernels.items()
            },
            "conductor_kernel_generators": {
                str(k): data["generators"] for k, data in kernels.items()
            },
            "character_count": len(conductors),
            "conductor_counts": {str(k): v for k, v in conductor_counts.items()},
            "prime_ideal_catalog": {
                "records": catalog["prime_ideal_records"],
                "split_rational_primes": catalog["split_rational_primes"],
                "ramified_rational_primes": catalog["ramified_rational_primes"],
                "nonprincipal_prime_ideal_records": catalog["nonprincipal_prime_ideal_records"],
                "sha256": catalog["catalog_sha256"]
            },
            "character_evaluations": evaluations
        })
    return {"phase": "Phase322", "modulus": 125, "fields": results}


def main():
    print("PHASE322_EXACT_RAY_CHARACTER_GROUP_PASS",
          json.dumps(run_phase322(), sort_keys=True, separators=(",", ":")),
          flush=True)


if __name__ == "__main__":
    main()
