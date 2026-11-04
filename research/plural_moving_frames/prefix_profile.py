#!/usr/bin/env python3
"""Exact prefix valuation profile from the original rectangular exponent weights.

No matrices of size R*S are allocated. Research only, not a discriminant proof.
"""
from fractions import Fraction


def weight_count(R, S, p, j):
    if j <= 0:
        return R*S
    return max(R - p*j, 0)*max(S - j, 0)


def tau_prefix(R, S, p, k):
    """Sum of the k smallest e(r,s)=min(r//p,S-1-s)."""
    n = R*S
    assert p > 0 and R >= 0 and S >= 1 and 0 <= k <= n
    m = n-k
    lo, hi = 0, min(S-1, (R-1)//p if R else 0)
    while lo < hi:
        mid = (lo+hi+1)//2
        if weight_count(R, S, p, mid) > m:
            lo = mid
        else:
            hi = mid-1
    t = lo
    if t == 0:
        return 0, 0
    # On j <= t the terms are nonzero and the sum is a polynomial.
    assert R >= p*t
    partial = t*R*S - (R+p*S)*t*(t+1)//2 + p*t*(t+1)*(2*t+1)//6
    return partial-m*t, t


def total_weight(R, S, p):
    """Only used when R >= p*(S-1)."""
    assert R >= p*(S-1) and S >= 1
    return R*S*(S-1)//2 - p*S*(S-1)*(S+1)//6


def test_small_enumeration():
    count = 0
    for R in range(10, 44):
        for S in range(2, 7):
            for p in (2, 3, 5):
                e = sorted(min(r//p, S-1-s)
                           for r in range(R) for s in range(S))
                for k in range(R*S+1):
                    observed, _ = tau_prefix(R, S, p, k)
                    assert observed == sum(e[:k]), (R, S, p, k)
                    count += 1
                if R >= p*(S-1):
                    assert total_weight(R, S, p) == sum(e)
    return count


def large_parameter_summary():
    D = 322**4
    R = D//4
    S = R//25
    n = R*S
    data = {"D": D, "R": R, "S": S, "rows": n, "primes": {}}
    for p in (3, 5):
        Fp = total_weight(R, S, p)
        rows = []
        for a, b in ((1, 4), (1, 2), (3, 4), (1, 1)):
            k = n*a//b
            tau, t = tau_prefix(R, S, p, k)
            rows.append({"fraction": f"{a}/{b}", "k": k,
                         "tau": tau, "last_threshold": t,
                         "tau_over_F_exact": str(Fraction(tau, Fp))})
        data["primes"][str(p)] = {"total_F": Fp, "prefixes": rows}
    return data


if __name__ == "__main__":
    import json
    checked = test_small_enumeration()
    print("SMALL_EXACT_COMPARISONS", checked)
    print(json.dumps(large_parameter_summary(), indent=2))
    print("PASS: closed-form prefix profile agrees with exhaustive small cases")
