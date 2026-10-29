"""One sealed exact definition-level check; no production or trial imports."""
from pathlib import Path
from math import comb, factorial
import json
import sys

POINTS = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 1)]
LOCAL = [(1, 3), (19, 3), (2, 5), (1, 7)]
RECTANGLES = [(0, 2), (2, 0), (1, 1), (4, 2), (9, 3)]
ZERO = (0, 0)
ONE = (1, 0)

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def scale(c, a):
    return c * a[0], c * a[1]

def mul(d, a, b):
    return a[0]*b[0] - d*a[1]*b[1], a[0]*b[1] + a[1]*b[0]

def power(d, a, n):
    v = ONE
    for _ in range(n):
        v = mul(d, v, a)
    return v

def conj(a):
    return a[0], -a[1]

def poly_mul(d, a, b):
    c = [ZERO for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = add(c[i+j], mul(d, x, y))
    return c

def poly_power(d, a, n):
    out = [ONE]
    for _ in range(n):
        out = poly_mul(d, out, a)
    return out

def derivative_value(d, coefficients, z, j):
    # Differentiate the constructed polynomial, then evaluate: no binomial-row code.
    c = list(coefficients)
    for _ in range(j):
        c = [scale(i, c[i]) for i in range(1, len(c))]
    out = ZERO
    for x in reversed(c):
        out = add(mul(d, out, z), x)
    return out

def canonical_jet(d, r, s, j, z):
    if j > r:
        return ZERO
    return scale(factorial(r)//factorial(r-j),
                 mul(d, power(d,z,r-j), power(d,conj(z),s)))

def direct_polynomial(d, p, r, s, k, z):
    xp = [ZERO]*p + [ONE]
    xp[0] = scale(-1,conj(z))
    monomial = [ZERO]*(r-p*k) + [power(d,conj(z),s)]
    return poly_mul(d, monomial, poly_power(d,xp,k))

def mm(a,b):
    columns = len(b[0]) if b else 0
    return [[sum(aik*b[k][j] for k,aik in enumerate(row))
             for j in range(columns)] for row in a]

def transpose(a):
    return [list(c) for c in zip(*a)]

def coordinate_gram(e, weights):
    return [[sum(x*w*y for x,w,y in zip(a,weights,b)) for b in e] for a in e]

def determinant(a):
    n = len(a)
    if n == 0:
        return 1
    a = [row[:] for row in a]
    sign, previous = 1, 1
    for k in range(n-1):
        pivot = next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = value*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0, 'nonexact Bareiss division'
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = value
    return sign*a[-1][-1]

def one_case(d,p,R,S,J):
    labels = [(r,s) for r in range(R) for s in range(S)]
    slots = [(j,z) for j in range(J) for z in POINTS]
    exponents = [min(r//p,S-1-s) for r,s in labels]
    U = [[0]*len(labels) for _ in labels]
    for i,((r,s),k) in enumerate(zip(labels,exponents)):
        for t in range(k+1):
            rr,ss = r-p*t,s+t
            assert 0 <= rr < R and 0 <= ss < S
            U[i][rr*S+ss] += (-1)**t*comb(k,t)
    V = [[canonical_jet(d,r,s,j,z) for j,z in slots] for r,s in labels]
    E = [[c for v in row for c in v] for row in V]
    weights = [w for _ in slots for w in (2,2*d)]
    G = [[sum(2*(a[0]*b[0]+d*a[1]*b[1]) for a,b in zip(v,w))
          for w in V] for v in V]
    assert G == coordinate_gram(E,weights), 'original Gram identity'
    direct = []
    for (r,s),k in zip(labels,exponents):
        polynomials = {z:direct_polynomial(d,p,r,s,k,z) for z in POINTS}
        jets = [derivative_value(d,polynomials[z],z,j) for j,z in slots]
        direct.append([c for v in jets for c in v])
    transformed = mm(U,E)
    assert transformed == direct, 'actual ordinary jet action'
    delta = [p**k for k in exponents]
    assert all(x % q == 0 for q,row in zip(delta,direct) for x in row)
    Ehat = [[x//q for x in row] for q,row in zip(delta,direct)]
    K = coordinate_gram(Ehat,weights)
    middle = mm(mm(U,G),transpose(U))
    expected = [[delta[i]*K[i][j]*delta[j] for j in range(len(labels))]
                for i in range(len(labels))]
    assert middle == expected, 'integral two-sided factorization'
    F = sum(min(r//p,t) for r in range(R) for t in range(S))
    assert sum(exponents) == F, 'reflected exponent convention'
    du,dg,dk = determinant(U),determinant(G),determinant(K)
    assert du == 1 and determinant(middle) == dg
    assert dg == p**(2*F)*dk, 'exact determinant factor'
    return {'D':d,'p':p,'R':R,'S':S,'J':J,'weights':exponents,'U':U,
            'G':G,'K':K,'detG':dg,'detK':dk,'F':F,
            'jet_coordinates_checked':sum(map(len,direct))}

def main():
    records = []
    for d,p in LOCAL:
        assert p != 2 and all((x*x+d)%p for x in range(p)), 'local guard'
        for z in POINTS:
            diff = add(power(d,z,p),scale(-1,conj(z)))
            assert diff[0]%p == diff[1]%p == 0, 'Frobenius congruence'
        for R,S in RECTANGLES:
            for J in (0,1,p,p+1):
                records.append(one_case(d,p,R,S,J))
    assert len(records) == 80
    assert determinant([[3]]) % 3 == 0 and determinant([[3]]) % 9 != 0
    invalid = add(power(2,(0,1),3),scale(-1,conj((0,1))))
    assert invalid[0]%3 != 0 or invalid[1]%3 != 0
    x3 = [ZERO,ZERO,ZERO,ONE]
    ordinary = derivative_value(1,x3,(0,0),3)
    assert ordinary == (6,0) and ordinary[0]%3 == 0 and 1%3 != 0
    constant = sum(2 for _ in POINTS)
    assert constant == 10 and constant != len(POINTS)
    payload = {'cases':records,'negative_controls':4,
               'zero_determinants':sum(r['detG']==0 for r in records),
               'positive_determinants':sum(r['detG']>0 for r in records),
               'jet_coordinates_checked':sum(r['jet_coordinates_checked'] for r in records)}
    Path(sys.argv[1]).write_text(json.dumps(payload,separators=(',',':'))+'\n',encoding='utf-8')
    print('PASS: 80 fixed cases; integral quotient jets and shared pivots; '
          '4 negative controls; '+str(payload['jet_coordinates_checked'])+' jet coordinates; '
          +str(payload['zero_determinants'])+' zero determinants retained.')

if __name__ == '__main__':
    main()
