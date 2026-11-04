#!/usr/bin/env python3
"""Exact *original-source* ordinary-jet Gram pilot (not a field proof).

D=19, J=S=3, R=4, source observation supports are ellipsePairs D rho.
Integer pair arithmetic, W=conjugate Z held fixed in each Z derivative,
trace=2*(ac+Dbd). Uses no NumPy, floating point, or substituted Gram.
"""
from itertools import combinations
from math import factorial, gcd

D, R, S, J, P = 19, 4, 3, 3, 3


def mul(a, b):
    return (a[0]*b[0]-D*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def power(a, k):
    v = (1, 0)
    for _ in range(k):
        v = mul(v, a)
    return v


def ordinary_jet(a, r, s, j):
    if j > r:
        return 0, 0
    w = (a[0], -a[1])
    v = mul(power(a, r-j), power(w, s))
    factor = factorial(r)//factorial(r-j)
    return factor*v[0], factor*v[1]


def ellipse(rho):
    return [(x, y)
            for x in range(-rho, rho+1)
            for y in range(-rho, rho+1)
            if x*x+D*y*y <= rho*rho]


def gram(Q):
    rows = [(r, s) for r in range(R) for s in range(S)]
    n = len(rows)
    g = [[0]*n for _ in range(n)]
    for point in Q:
        for j in range(J):
            v = [ordinary_jet(point, r, s, j) for r, s in rows]
            for i in range(n):
                for h in range(i, n):
                    g[i][h] += 2*(v[i][0]*v[h][0]+D*v[i][1]*v[h][1])
    for i in range(n):
        for h in range(i):
            g[i][h] = g[h][i]
    return g


def determinant(a):
    n = len(a)
    if n == 0:
        return 1
    a = [list(row) for row in a]
    sign, prev = 1, 1
    for j in range(n-1):
        if a[j][j] == 0:
            pivot = next((i for i in range(j+1,n) if a[i][j]), None)
            if pivot is None:
                return 0
            a[j], a[pivot] = a[pivot], a[j]
            sign *= -1
        v = a[j][j]
        for i in range(j+1, n):
            for h in range(j+1,n):
                num = a[i][h]*v - a[i][j]*a[j][h]
                assert num % prev == 0
                a[i][h] = num//prev
        for i in range(j+1,n):
            a[i][j] = 0
        prev = v
    return sign*a[-1][-1]


def divisor(a, k):
    n = len(a)
    d = 0
    for iset in combinations(range(n),k):
        for jset in combinations(range(n),k):
            d = gcd(d,abs(determinant([[a[i][j] for j in jset] for i in iset])))
    return d


def valuation(n,p):
    assert n
    count = 0
    while n%p==0:
        count+=1
        n//=p
    return count


def test_original_source():
    assert (-D)%P == 2  # 2 is nonsquare modulo 3: Frobenius is conjugation.
    # R=4,S=3,p=3: exponents 1 at (3,0),(3,1), zero elsewhere.
    exponents = [min(r//P,S-1-s) for r in range(R) for s in range(S)]
    assert exponents.count(1) == 2 and exponents.count(0) == 10
    expected_k11, expected_k12 = 2, 4
    outputs=[]
    for radius, count, v3minor11, v3det in [(5,21,3,6),(6,31,5,8)]:
        Q=ellipse(radius)
        G=gram(Q)
        detG=determinant(G)
        assert len(Q)==count and len(G)==R*S and detG>0
        d10=divisor(G,10)
        d11=divisor(G,11)
        d12=divisor(G,12)
        assert d12==detG
        assert valuation(d11,3)==v3minor11 and valuation(detG,3)==v3det
        assert d11 % 3**expected_k11 == 0
        assert detG % 3**expected_k12 == 0
        outputs.append({"radius":radius,"observations":len(Q),"det_bits":detG.bit_length(),
                        "v3_delta10":valuation(d10,3),
                        "v3_delta11":valuation(d11,3),
                        "v3_det":valuation(detG,3)})
    return outputs


if __name__=="__main__":
    import json
    print(json.dumps(test_original_source(),indent=2))
    print("PASS: original ordinary-jet finite source and partial-minor factors")
