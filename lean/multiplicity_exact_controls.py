#!/usr/bin/env python3
"""Finite exact controls for fixed-size Sylvester multiplicity; not a universal proof."""
from fractions import Fraction
from math import comb, factorial
import json
import random

SEED = 20261022

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def det(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    n = len(a)
    require(all(len(row) == n for row in a), 'matrix is not square')
    value = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            value = -value
        p = a[k][k]
        value *= p
        for i in range(k+1, n):
            f = a[i][k] / p
            for j in range(k+1, n):
                a[i][j] -= f * a[k][j]
    return value

def shift_power(root, k):
    return [comb(k, i) * (-root)**(k-i) for i in range(k+1)]

def pmul(f, g):
    out = [0] * (len(f)+len(g)-1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i+j] += a*b
    return out

def fixed_sylvester(f, a):
    # Columns: Z^j F for j<a-1, then Z^j F_Z for j<a.
    require(len(f) == a+1, 'retain original degree bound and zero leading entries')
    g = [(i+1)*f[i+1] for i in range(a)]
    n = 2*a-1
    columns = [[0]*j + f + [0]*(a-2-j) for j in range(a-1)]
    columns += [[0]*j + g + [0]*(a-1-j) for j in range(a)]
    return [list(row) for row in zip(*columns)] if n else []

def interpolate(values):
    coefficients = [Fraction(0)] * len(values)
    basis, differences = [Fraction(1)], [Fraction(v) for v in values]
    for k in range(len(values)):
        factor = differences[0] / factorial(k)
        for i, b in enumerate(basis):
            coefficients[i] += factor*b
        differences = [b-a for a,b in zip(differences,differences[1:])]
        basis = pmul(basis, [-k,1])
    return coefficients

def eval_poly(f,x):
    out = Fraction(0)
    for c in reversed(f):
        out = out*x+c
    return out

def taylor_coefficients(f,center):
    return [sum(f[j]*comb(j,i)*center**(j-i) for j in range(i,len(f)))
            for i in range(len(f))]

def run():
    rng = random.Random(SEED)
    known = []
    for a,f,expected in [
        (2,lambda w:[-w,0,1],{1:-4}),
        (3,lambda w:[w,0,1,w],{2:4,5:27}),
        (2,lambda w:[0,0,1],{}),
    ]:
        c = interpolate([det(fixed_sylvester(f(w),a)) for w in range(2*a)])
        actual = {i:int(v) for i,v in enumerate(c) if v}
        require(actual == expected,f'known-answer mismatch {a}: {actual}')
        known.append({'a':a,'coefficients':actual,'order':min(actual) if actual else None})
    cases = []
    for case in range(48):
        a = 2+case%4
        drop = bool((case//4)%2)
        m = rng.randint(1,a-1 if drop else a)
        w0,z0 = rng.randint(-3,3),rng.randint(-3,3)
        k = a-m-(1 if drop else 0)
        h = shift_power(z0,k)
        h[0] += 1
        f0 = pmul(shift_power(z0,m),h)
        f0 += [0]*(a+1-len(f0))
        g = [rng.randint(-3,3) for _ in range(a)]+[rng.choice([-2,-1,1,2])]
        def f(w):
            return [x+(w-w0)*y for x,y in zip(f0,g)]
        c = interpolate([det(fixed_sylvester(f(w),a)) for w in range(2*a)])
        require(all(v.denominator == 1 for v in c),'noninteger determinant coefficients')
        tc = taylor_coefficients(c,w0)
        require(all(tc[i] == 0 for i in range(m-1)),'multiplicity bound failed')
        for w in [-7,2*a+3]:
            require(eval_poly(c,w) == det(fixed_sylvester(f(w),a)),'interpolation degree mismatch')
        n = 2*a-1
        T = [[comb(j,i)*z0**(j-i) if i<=j else 0 for j in range(n)] for i in range(n)]
        require(det(T) == 1,'Taylor determinant normalization failed')
        M = fixed_sylvester(f(w0),a)
        TM = [[sum(T[i][k]*M[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        require(all(v == 0 for row in TM[:m-1] for v in row),'low Taylor rows did not vanish')
        test = fixed_sylvester(f(w0+1),a)
        d = det(test)
        require(det([row[::-1] for row in test[::-1]]) == d,'basis-reordering drift')
        swapped = [row[:] for row in test]
        swapped[0],swapped[1] = swapped[1],swapped[0]
        require(det(swapped) == -d,'row swap sign lost')
        nonzero = [i for i,v in enumerate(tc) if v]
        cases.append({'a':a,'m':m,'w0':w0,'z0':z0,'leading_degree_drop':drop,
                      'det_order':nonzero[0] if nonzero else None,
                      'det_coefficients':[int(v) for v in c]})
    require(known[0]['order'] == 1,'sharp bound control did not discriminate')
    require(det([[1,0],[0,1]]) == 1 and det([[0,0],[0,1]]) == 0,
            'singular-transform control failed')
    return {'status':'PASS','seed':SEED,'known_cases':known,'planted_cases':cases,
            'count':len(cases),'degree_drop_cases':sum(c['leading_degree_drop'] for c in cases),
            'scope':'finite exact controls; shared authorship, not independent semantic review'}

if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
