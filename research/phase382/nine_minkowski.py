#!/usr/bin/env python3
"""Finite arithmetic for the classical imaginary-quadratic Minkowski criterion.

External theorem NOT proved by code: every ideal class of a quadratic
imaginary field of discriminant -d contains an integral ideal of norm
<= (2/pi)*sqrt(d). Since pi>3, this is < (2/3)*sqrt(d).
If all primes below that bound are inert, every such ideal is a
product of principal inert prime ideals (p), hence class number one.
"""
from math import isqrt
from three_prime_199 import TARGET, symbol

def norm_cap(d):
    return max(n for n in range(1,10) if 9*n*n < 4*d)

def is_prime(n):
    return n>=2 and all(n%k for k in range(2,isqrt(n)+1))

def main():
    expected={3:1,4:1,7:1,8:1,11:2,19:2,43:4,67:5,163:8}
    assert {d:norm_cap(d) for d in TARGET}==expected
    for d in TARGET:
        c=norm_cap(d)
        assert 9*c*c < 4*d <= 9*(c+1)**2
        for p in range(2,c+1):
            if not is_prime(p):
                continue
            assert p in (2,3,5,7)
            if p==5:
                # Independent residue table, not a reused witness from sieve.
                residue=(-d)%5
                chi=0 if residue==0 else (1 if residue in (1,4) else -1)
            else:
                chi=symbol(d,p)
            assert chi==-1,(d,p,chi)
    print("PASS: classical Minkowski norm caps and required inert primes")
    print("caps:",expected)
    return expected

if __name__=="__main__":
    main()
