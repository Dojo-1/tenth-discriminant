#!/usr/bin/env python3
"""Phase274: exact finite controls for the sharp local precision horizon.
Preregistered claim: for u with v_p(u)=s>=1, first-J ordinary jets
over Z[X] determine moved jets modulo p^e iff e <= s+v_p(J!).
Finite tests are NOT a universal proof.
"""
from math import factorial

def vp(n, p):
    if n == 0:
        return 10**9
    n = abs(n)
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k

def monomial_jet(degree, a, depth):
    return [
        factorial(degree)//factorial(degree-i) * a**(degree-i)
        if i <= degree else 0
        for i in range(depth)
    ]

def local_coefficient(p, e, u, d):
    if d == 0:
        return 1
    if u == 0:
        return 0
    mod = p**e
    denominator = factorial(d)
    v = vp(u,p)*d - vp(denominator,p)
    assert v >= 0
    unit = (u//p**vp(u,p))**d
    denominator_unit = denominator//p**vp(denominator,p)
    return (p**v*unit*pow(denominator_unit,-1,mod)) % mod

def transport(v,p,e,u):
    mod = p**e
    return [
        sum(local_coefficient(p,e,u,k-i)*v[k]
            for k in range(i,len(v))) % mod
        for i in range(len(v))
    ]

def main():
    count = 0
    for p in (2,3,5):
        for e in range(1,6):
            for s in range(1,4):
                u = p**s
                mod = p**e
                for J in range(1,12):
                    valid = e <= s+vp(factorial(J),p)
                    if valid:
                        for a in (0,2):
                            for degree in range(J+5):
                                before = [x%mod for x in monomial_jet(degree,a,J)]
                                after = [x%mod for x in monomial_jet(degree,a+u,J)]
                                assert transport(before,p,e,u) == after, (
                                    "positive",p,e,s,J,a,degree)
                                count += 1
                        v = [(7*i+3*i*i+1)%mod for i in range(J)]
                        assert transport(transport(v,p,e,u),p,e,-u) == v
                        count += 1
                    else:
                        before = [x%mod for x in monomial_jet(J,0,J)]
                        after = [x%mod for x in monomial_jet(J,u,J)]
                        assert before == [0]*J
                        assert after[J-1] == factorial(J)*u%mod != 0
                        count += 1
        print("PRIME_PASSED",p,flush=True)
    assert count == 8839
    print("PASS",count,"exact finite controls")

if __name__ == "__main__":
    main()
