#!/usr/bin/env python3
"""Phase305: standalone F_p[Z]/(Z^(p^2)-Z)^j ordinary-jet kernel census.

No repository imports, third-party dependencies, or claims about a field bound.
This is a finite F_p computation; it is not a Lean proof.
"""
from math import comb


def rank_mod_p(vectors, p):
    pivots = {}
    for raw in vectors:
        row = [int(x) % p for x in raw]
        for k in sorted(pivots):
            factor = row[k]
            if factor:
                base = pivots[k]
                for col in range(k, len(row)):
                    row[col] = (row[col] - factor * base[col]) % p
        pivot = next((j for j, x in enumerate(row) if x), None)
        if pivot is not None:
            inv = pow(row[pivot], -1, p)
            for col in range(pivot, len(row)):
                row[col] = row[col] * inv % p
            pivots[pivot] = row
    return len(pivots)


def monomial_remainders(p, j, max_degree):
    """Compute x^n mod (x^(p*p)-x)^j via a monic recurrence."""
    q = p * p
    degree = q * j
    # (x^q - x)^j = x^(q*j) + sum_(k<j) c[k]*x^(q*k+j-k)
    lower = {q * k + j - k: (comb(j, k) * (-1) ** (j - k)) % p
             for k in range(j)}
    vector = [0] * degree
    vector[0] = 1
    output = [tuple(vector)]
    for _ in range(max_degree):
        overflow = vector[-1]
        vector = [0] + vector[:-1]
        if overflow:
            for exponent, coefficient in lower.items():
                vector[exponent] = (vector[exponent] - overflow * coefficient) % p
        output.append(tuple(vector))
    return output


def valuation_weight(R, S, p):
    return sum(min(r // p, t) for r in range(R) for t in range(S))


def kernel_census(R, S, J, p):
    assert p > 1 and R > 0 and S > 0 and J > 0
    j = min(J, p)  # ordinary, NOT Hasse derivatives, vanish identically for j>=p
    quotient_dimension = p * p * j
    if R >= quotient_dimension:
        # Rows s=0 contain 1,x,...,x^(d-1), hence span the entire quotient.
        image_rank = quotient_dimension
    else:
        remainders = monomial_remainders(p, j, R - 1 + p * (S - 1))
        image_rank = rank_mod_p(
            (remainders[r + p * s] for r in range(R) for s in range(S)), p)
    n = R * S
    h = n - image_rank
    w = valuation_weight(R, S, p)
    return dict(R=R, S=S, J=J, p=p, effective_J=j,
                image_rank=image_rank, kernel_dimension=h,
                valuationWeight=w, first_level_gain=h-w,
                valid_lower_exponent=2*max(h, w))


def main():
    cases = [
        ((40, 1, 1, 5), (25, 15, 0)),
        ((50, 2, 2, 5), (50, 50, 45)),
        ((70, 2, 2, 3), (18, 122, 67)),
        ((70, 2, 2, 5), (50, 90, 65)),
        ((100, 4, 4, 5), (100, 300, 550)),
    ]
    for args, expected in cases:
        result = kernel_census(*args)
        observed = (result['image_rank'], result['kernel_dimension'],
                    result['valuationWeight'])
        assert observed == expected, (args, observed, expected)
        print(result)
    # Degenerate-derivative boundary: J>p adds no ordinary derivative constraints.
    assert kernel_census(13, 3, 17, 3)['kernel_dimension'] == kernel_census(13, 3, 3, 3)['kernel_dimension']
    print('PASS phase305 Frobenius-Hermite bounded source rank controls')


if __name__ == '__main__':
    main()
