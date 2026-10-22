#!/usr/bin/env python3
"""Exact finite controls for the proposed J>=S criterion. Not its universal proof.

Standard library only. Full rank modulo the checked prime proves full rank for
these particular characteristic-zero Q(i) matrices. A modular rank defect would
require a characteristic-zero check, not automatic rejection of the conjecture.
"""
import itertools
import json
import math
import random
from fractions import Fraction

MOD, ROOT_I, SEED = 1000000009, 430477711, 20261022

def rank_mod(matrix):
    a = [[v % MOD for v in row] for row in matrix]
    if not a:
        return 0
    k = 0
    for j in range(len(a[0])):
        found = next((i for i in range(k, len(a)) if a[i][j]), None)
        if found is None:
            continue
        a[k], a[found] = a[found], a[k]
        inv = pow(a[k][j], -1, MOD)
        a[k] = [(v * inv) % MOD for v in a[k]]
        for i in range(k+1, len(a)):
            factor = a[i][j]
            if factor:
                a[i] = [(v-factor*w) % MOD for v,w in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k

def jet_rows(P,R,S,J):
    return [[0 if j>r else math.perm(r,j)*pow(z,r-j,MOD)*pow(w,s,MOD) % MOD
             for z,w in P for j in range(J)]
            for r in range(R) for s in range(S)]

def gaussian(x,y):
    return ((x+ROOT_I*y) % MOD, (x-ROOT_I*y) % MOD)

def circle(t):
    den = pow(1+t*t,-1,MOD)
    return ((1-t*t+2*t*ROOT_I)*den % MOD, (1-t*t-2*t*ROOT_I)*den % MOD)

def determinant(matrix):
    """Integer Bareiss determinant with exact divisions and row pivoting."""
    a=[list(row) for row in matrix]
    n=len(a)
    if n==0:
        return 1
    sign, previous=1,1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        pk=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=pk*a[i][j]-a[i][k]*a[k][j]
                quotient,remainder=divmod(numerator,previous)
                if remainder:
                    raise AssertionError('Bareiss division was not exact')
                a[i][j]=quotient
            a[i][k]=0
        previous=pk
    return sign*a[-1][-1]

def specialization_resultant(a,w):
    """Fixed-size Sylvester matrix of H=w*z^a+z^2+w and H_z."""
    f=[0]*(a+1)
    f[0],f[a-2],f[a]=w,1,w
    g=[(a-i)*f[i] for i in range(a)]
    rows=[]
    for i in range(a-1):
        rows.append([0]*i+f+[0]*(a-2-i))
    for i in range(a):
        rows.append([0]*i+g+[0]*(a-1-i))
    return determinant(rows)

def interpolate_integer_values(values):
    """Newton forward differences; coefficients in ascending monomial order."""
    answer=[Fraction(0) for _ in values]
    basis=[Fraction(1)]
    differences=[Fraction(v) for v in values]
    for k in range(len(values)):
        factor=differences[0]/math.factorial(k)
        for i,b in enumerate(basis):
            answer[i] += factor*b
        differences=[y-x for x,y in zip(differences,differences[1:])]
        nxt=[Fraction(0)]*(len(basis)+1)
        for i,b in enumerate(basis):
            nxt[i] -= k*b
            nxt[i+1] += b
        basis=nxt
    return answer

def run():
    if any(MOD%d==0 for d in range(2,math.isqrt(MOD)+1)) or ROOT_I*ROOT_I%MOD!=MOD-1:
        raise AssertionError('invalid reduction field')
    rng=random.Random(SEED)
    cases=[]
    for R,S,family in itertools.product(range(1,9),range(1,5),['real','irregular','circle']):
        n,J=2*(R-1)+(S-1)+1,S
        if family=='real':
            P=[gaussian(t-n//2,0) for t in range(n)]
        elif family=='circle':
            P=[circle(t) for t in range(n)]
        else:
            P=[gaussian(x,y) for x,y in rng.sample(list(itertools.product(range(-12,13),repeat=2)),n)]
        if len({z for z,w in P})!=n or len({w for z,w in P})!=n:
            raise AssertionError('projection collision after reduction')
        matrix=jet_rows(P,R,S,J)
        rank=rank_mod(matrix)
        if rank!=R*S:
            raise AssertionError(f'Exact follow-up required for modular rank defect: {R,S,family,rank}')
        if rank_mod([row[::-1] for row in matrix[::-1]])!=rank:
            raise AssertionError('permutation drift')
        cases.append(dict(R=R,S=S,J=J,points=n,family=family,rank=rank))
    dropped=[]
    for J in range(1,5):
        R=S=J+1
        n=3*J+2
        matrix=jet_rows([circle(t) for t in range(n)],R,S,J)
        coeff=[(-1)**(J-r)*math.comb(J,r) if r==s else 0 for r in range(R) for s in range(S)]
        if any(sum(coeff[i]*matrix[i][k] for i in range(R*S))%MOD for k in range(n*J)):
            raise AssertionError('circle null polynomial failed')
        rank=rank_mod(matrix)
        if rank==R*S:
            raise AssertionError('missing-jet control failed')
        dropped.append(dict(J=J,R=R,S=S,points=n,rank=rank,rows=R*S))
    expected={3:{2:4,5:27},4:{3:16,5:-128,7:256},5:{4:108,9:3125},6:{5:1024,8:13824,11:46656}}
    resultants=[]
    for a in range(3,7):
        # Each determinant entry has w-degree <=1, so 2a samples determine it.
        coeff=interpolate_integer_values([specialization_resultant(a,w) for w in range(2*a)])
        if any(c.denominator!=1 for c in coeff):
            raise AssertionError('nonintegral resultant interpolation')
        nonzero={i:int(c) for i,c in enumerate(coeff) if c}
        if nonzero!=expected[a]:
            raise AssertionError('fixed-size resultant differs from symbolic reference')
        order,degree=min(nonzero),max(nonzero)
        if order<1 or degree>2*a-1:
            raise AssertionError('specialization multiplicity/degree budget failed')
        resultants.append(dict(a=a,b=1,order=order,degree=degree,coefficients=nonzero))
    if determinant([[2,0],[0,2]])!=4:
        raise AssertionError('real-complex distinction control failed')
    return dict(status='PASS',seed=SEED,modulus=MOD,sqrt_minus_one=ROOT_I,
                rank_cases=len(cases),cases=cases,dropped_jet_controls=dropped,
                fixed_size_resultants=resultants,
                real_complex_control=dict(complex_row_rank=1,real_gram_determinant=4),
                scope='Finite exact controls only; universal criterion not proved by this script.')

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
