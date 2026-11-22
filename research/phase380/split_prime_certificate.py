#!/usr/bin/env python3
"""Phase380 exact finite exclusion of class-number-one candidates through d<=652.

No imports beyond Python's standard library. No analytic L-function, Heegner
classification, floating-point arithmetic or outside class-number oracle.

DEPENDENCIES OF THE MATHEMATICAL INTERPRETATION (not proved by this script):
  1. Standard discriminant description of an imaginary quadratic ring of
     integers and the displayed integral norm forms.
  2. For a split prime p, there is a prime ideal of norm p.
  3. Class number one makes that ideal principal.

This certifies EXCLUSION of 190 candidates, not class number one for the nine
survivors. The positive direction must be established independently.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from math import isqrt

LIMIT = 652
SURVIVORS = (3, 4, 7, 8, 11, 19, 43, 67, 163)


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def squarefree(n: int) -> bool:
    n = abs(n)
    return n > 0 and all(n % (k*k) for k in range(2, isqrt(n) + 1))


def negative_fundamental(d: int) -> bool:
    """Is -d a negative fundamental discriminant?"""
    if d <= 0:
        return False
    D = -d
    if D % 4 == 1:
        return squarefree(D)
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and squarefree(m)
    return False


def split_prime(D: int, p: int) -> bool:
    """Kronecker(D/p)=+1; p is asserted to be prime."""
    assert D < 0 and is_prime(p)
    if p == 2:
        return D % 8 == 1
    if D % p == 0:
        return False  # ramified, never split
    return pow(D % p, (p - 1) // 2, p) == 1


def split_prime_independent(D: int, p: int) -> bool:
    """Independent small-prime check by enumerating nonzero square residues."""
    if p == 2:
        return D % 8 == 1
    if D % p == 0:
        return False
    return any((a * a - D) % p == 0 for a in range(1, p))


def bound_numerator(d: int) -> int:
    """Necessary inequality for a principal split prime: 4*p >= this."""
    assert negative_fundamental(d)
    return d + 1 if d % 2 else d


def witness(d: int) -> int | None:
    """A prime p whose splitting contradicts class number one for -d."""
    b = bound_numerator(d)
    return next((p for p in range(2, (b - 1)//4 + 1)
                 if is_prime(p) and 4*p < b and split_prime(-d, p)), None)


def certificate(limit: int = LIMIT) -> dict:
    fundamentals = [d for d in range(1, limit + 1) if negative_fundamental(d)]
    excluded = {d: p for d in fundamentals if (p := witness(d)) is not None}
    survivors = sorted(set(fundamentals) - set(excluded))

    # Exact independent modular-residue cross-check for every small prime.
    primes = [p for p in range(2, max(excluded.values(), default=2) + 1)
              if is_prime(p)]
    for d in fundamentals:
        for p in primes:
            assert split_prime(-d, p) == split_prime_independent(-d, p), (d,p)
    for d,p in excluded.items():
        assert negative_fundamental(d)
        assert 4*p < bound_numerator(d)
        assert is_prime(p) and split_prime(-d, p)

    if limit == LIMIT:
        assert len(fundamentals) == 199, len(fundamentals)
        assert len(excluded) == 190, len(excluded)
        assert survivors == list(SURVIVORS), survivors
        assert max(excluded.values()) == 31
        # Boundaries: a split prime at equality does NOT prove nonprincipality.
        for d,p in [(7,2),(11,3),(19,5),(43,11),(67,17),(163,41)]:
            assert split_prime(-d,p) and 4*p == d+1
        assert not split_prime(-8,2)  # p=2 ramifies in Q(sqrt(-2))

    lines = [f'{d},{p}' for d,p in sorted(excluded.items())]
    canonical = '\n'.join(lines) + '\n'
    return dict(limit=limit, negative_fundamental=len(fundamentals),
                excluded=len(excluded), survivors=survivors,
                max_witness_prime=max(excluded.values(),default=0),
                prime_witness_frequencies=dict(sorted(Counter(excluded.values()).items())),
                sorted_witnesses=[[d,p] for d,p in sorted(excluded.items())],
                sha256_witness_csv=hashlib.sha256(canonical.encode('ascii')).hexdigest())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=LIMIT)
    parser.add_argument('--json',action='store_true',help='emit full sorted witness list')
    args = parser.parse_args()
    result = certificate(args.limit)
    if args.json:
        print(json.dumps(result,sort_keys=True,indent=2))
    else:
        for field in ('limit','negative_fundamental','excluded','survivors',
                      'max_witness_prime','prime_witness_frequencies',
                      'sha256_witness_csv'):
            print(f'{field}: {result[field]}')
        print('P=bounded integer enumeration only; no analytic or class-number proof')


if __name__ == '__main__':
    main()
