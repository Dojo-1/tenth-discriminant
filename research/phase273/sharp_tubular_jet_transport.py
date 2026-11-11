#!/usr/bin/env python3
"""Phase273 preregistered integer-only finite controls, not a universal proof.

Primary: first-J ordinary derivative vector transforms by I+delta*N modulo
p^2 when J>=p and delta divisible by p.
Negative: for J<p, X^J is invisible at zero but visible after a p-shift.
Metamorphic: group action and inverse on the full ambient jet module.
"""
from math import factorial

PRIMES = (2, 3, 5, 7)


def jet(coeffs, a, depth):
    return [
        sum(
            c * (factorial(k) // factorial(k-j)) * a**(k-j)
            for k, c in enumerate(coeffs) if j <= k
        )
        for j in range(depth)
    ]


def step(v, u, modulus):
    return [
        (v[i] + (u * v[i+1] if i + 1 < len(v) else 0)) % modulus
        for i in range(len(v))
    ]


def main():
    checked = 0
    for p in PRIMES:
        modulus = p*p
        for depth in (p, p+1, p+3):
            for a in (-2, 0, 1):
                for t in (-1, 1, 2):
                    delta = p*t
                    for degree in range(2*p+5):
                        coeffs = [0] * (degree+1)
                        coeffs[degree] = 1
                        before = [x % modulus for x in jet(coeffs,a,depth)]
                        actual = [x % modulus for x in jet(coeffs,a+delta,depth)]
                        assert step(before,delta,modulus) == actual, (
                            "positive control", p, depth, a, delta, degree)
                        checked += 1
        for depth in range(1,p):
            coeffs = [0] * (depth+1)
            coeffs[depth] = 1
            before = [x % modulus for x in jet(coeffs,0,depth)]
            after = [x % modulus for x in jet(coeffs,p,depth)]
            assert before == [0]*depth
            assert after[depth-1] == (factorial(depth)*p)%modulus != 0
            checked += 1
        for depth in (p,p+3):
            v = [(7*i*i + 3*i + 1) % modulus for i in range(depth)]
            assert step(step(v,p,modulus),-p,modulus) == v
            assert step(step(v,p,modulus),p,modulus) == step(v,2*p,modulus)
            checked += 2
        print("PRIME_OK",p,"positive_min_J",p,"negative_max_J",p-1)
    assert checked == 1487
    print("PASS finite checks:",checked)


if __name__ == "__main__":
    main()
