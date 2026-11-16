#!/usr/bin/env python3
"""Phase325: explicit Frobenius labels in the maximal abelian quotient.

This implements only the congruence labels for INERT unramified
rational primes. The theorem that these labels distinguish full
conjugacy classes additionally uses standard global class field
theory and quadratic genus theory, not just the finite checks here.

D163:  Q(zeta_125)*Q(sqrt(-163)), maximal abelian quotient degree 200.
D187:  Q(zeta_125)*Q(sqrt(-11),sqrt(17)), degree 400.
D203:  Q(zeta_125)*Q(sqrt(-7),sqrt(29)), degree 400.

For an inert p, the K quadratic sign is -1, and the remaining label
is (p mod 125) or (p mod 125, (genus_real_discriminant/p)).
Do not apply this simplified labeling to SPLIT Frobenius classes.
"""
from __future__ import annotations
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase321"))
from ideal_aware_ray_class import is_prime  # noqa: E402

REAL_GENUS = {163: None, 187: 17, 203: 29}
GROUP_FIXED_COUNTS = {163: 100, 187: 200, 203: 200}
GENUS_FIELDS = {
    163: ("-163",),
    187: ("-11", "17"),
    203: ("-7", "29"),
}


def kronecker_for_prime(a: int, p: int) -> int:
    """Exact (a/p) for p an odd prime or p=2."""
    if not is_prime(p):
        raise ValueError(f"{p} is not prime")
    if p == 2:
        if a % 2 == 0:
            return 0
        r = a % 8
        return 1 if r in (1, 7) else -1
    if a % p == 0:
        return 0
    e = pow(a % p, (p - 1)//2, p)
    assert e in (1, p - 1)
    return 1 if e == 1 else -1


def inert_frobenius_label(D: int, p: int) -> tuple:
    """Complete class label in the abelianized quotient, for inert p."""
    if D not in REAL_GENUS:
        raise ValueError("Only the three verified imaginary quadratic fields")
    if not is_prime(p) or gcd(p, 5*D) != 1:
        raise ValueError("Only unramified rational primes coprime to 5D")
    if kronecker_for_prime(-D, p) != -1:
        raise ValueError("Requires inert p; split primes need ideal-aware ray classes")
    genus = REAL_GENUS[D]
    if genus is None:
        return (p % 125,)
    return (p % 125, kronecker_for_prime(genus, p))


def abelianization_dimension_control(D: int) -> dict:
    if D not in GROUP_FIXED_COUNTS:
        raise ValueError(D)
    real = REAL_GENUS[D]
    genus_field_degree = 2 if real is None else 4
    cyclo_degree = 100  # Euler phi(125)
    predicted = cyclo_degree * genus_field_degree
    finite_group_abelianization = 2 * GROUP_FIXED_COUNTS[D]
    assert predicted == finite_group_abelianization
    # Inert Frobenius classes correspond 1:1 to the half of the
    # abelian quotient with quadratic sign -1.
    inert_label_count = cyclo_degree * (genus_field_degree // 2)
    assert inert_label_count == GROUP_FIXED_COUNTS[D]
    return {
        "D": D,
        "cyclotomic_degree": cyclo_degree,
        "genus_field_degree_over_Q": genus_field_degree,
        "max_abelian_subfield_degree": predicted,
        "semidirect_abelianization_order": finite_group_abelianization,
        "inert_rational_frobenius_class_count": inert_label_count,
        "genus_field_factors": GENUS_FIELDS[D],
    }


def main():
    import json
    p_pairs = {163: (2, 127), 187: (2, 2377), 203: (2, 3877)}
    result = [abelianization_dimension_control(D) for D in (163,187,203)]
    witnesses = {
        str(D): {
            "primes": [p,q],
            "label_p": inert_frobenius_label(D,p),
            "label_q": inert_frobenius_label(D,q),
            "same_class_predicted_by_abelianization":
                inert_frobenius_label(D,p)==inert_frobenius_label(D,q),
        } for D,(p,q) in p_pairs.items()
    }
    print("PHASE325_ABELIAN_FROBENIUS_LABELS",
          json.dumps({"degree_controls":result,"witnesses":witnesses},
                     sort_keys=True),flush=True)


if __name__ == "__main__":
    main()
