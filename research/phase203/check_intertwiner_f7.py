#!/usr/bin/env python3
"""Phase203-B: explicit single-prime parity intertwiner, Issues #134 and #131.

Exact, standard-library-only finite certificate; NO uniform theorem in p/D/R,
NO identification with an external selected minor or the field discriminant.
The two arithmetic oracles are independent:
(1) original integer-pair jets/trace formula;
(2) split embeddings sqrt(-215) -> +/-3 over F7.
"""
from math import prod

D, P, R, S, J = 215, 7, 14, 2, 2
ROWS = [(r, s) for r in range(R) for s in range(S)]
EVEN = [i for i, (r,s) in enumerate(ROWS) if (r+s)%2 == 0]
ODD = [i for i, (r,s) in enumerate(ROWS) if (r+s)%2 == 1]
assert len(EVEN) == len(ODD) == 14

# Sparse 14x14 matrix U, indices 0-based, coefficients in F7.
# Det U = 1; it works for ALL 25 inversion orbits of F7^2.
U_TERMS = (
    (0,1,1), (1,0,6),
    (2,1,6), (2,3,4), (2,7,6), (2,9,5), (2,13,6),
    (3,2,6), (3,4,6), (3,8,6), (3,10,1),
    (4,3,6), (4,5,6), (4,9,6), (4,11,2),
    (5,4,6), (5,6,4), (5,10,6), (5,12,1),
    (6,5,6), (6,11,6), (6,13,5),
    (7,0,1), (7,2,2), (7,6,6), (7,8,1), (7,12,6),
    (8,1,1), (8,3,6), (8,7,1), (8,9,4), (8,13,1),
    (9,2,1), (9,4,5), (9,8,1), (9,10,2),
    (10,3,1), (10,5,6), (10,9,1), (10,11,2),
    (11,4,1), (11,6,2), (11,10,1), (11,12,4),
    (12,5,1), (12,11,1), (12,13,1),
    (13,6,1), (13,12,1),
)
assert len(U_TERMS) == 49


def U_at(p):
    U = [[0]*14 for _ in range(14)]
    for i,j,z in U_TERMS:
        U[i][j] = (z if z<=3 else z-7) % p
    return U


def matmul(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) % p
             for j in range(len(B[0]))] for i in range(len(A))]


def trans(A):
    return list(map(list,zip(*A)))


def congruent(E,O,U,p):
    return matmul(trans(U),matmul(E,U,p),p) == O


def det_mod(A,p):
    a = [list(row) for row in A]
    n = len(a); d = 1
    for j in range(n):
        k = next((i for i in range(j,n) if a[i][j]%p),None)
        if k is None: return 0
        if k!=j: a[j],a[k]=a[k],a[j];d=-d
        d = d*a[j][j]%p
        inv = pow(a[j][j],-1,p)
        for i in range(j+1,n):
            c = a[i][j]*inv%p
            for h in range(j+1,n):a[i][h]=(a[i][h]-c*a[j][h])%p
            a[i][j] = 0
    return d%p


def plus_minus_jets(x,y,j,p,root):
    z,w=(x+root*y)%p,(x-root*y)%p
    plus=[];minus=[]
    for r,s in ROWS:
        if j>r:
            plus.append(0);minus.append(0)
        else:
            f=prod(range(r-j+1,r+1))%p
            plus.append(f*pow(z,r-j,p)*pow(w,s,p)%p)
            minus.append(f*pow(w,r-j,p)*pow(z,s,p)%p)
    return plus,minus


def gram_split(Q,p,root):
    """Independent split Fp x Fp field-trace calculation."""
    g=[[0]*28 for _ in range(28)]
    for x,y in Q:
        for j in range(J):
            plus,minus=plus_minus_jets(x,y,j,p,root)
            for i in range(28):
                for k in range(i+1):
                    g[i][k]=(g[i][k]+plus[i]*minus[k]+minus[i]*plus[k])%p
    for i in range(28):
        for k in range(i):g[k][i]=g[i][k]
    return g


def pairmul(z,w,p):
    a,b=z;c,d=w
    return ((a*c-D*b*d)%p,(a*d+b*c)%p)


def pairpow(z,n,p):
    a=(1,0)
    for _ in range(n):a=pairmul(a,z,p)
    return a


def gram_pairs(Q,p):
    """Original integer-jet coordinate path; independent from split oracle."""
    g=[[0]*28 for _ in range(28)]
    for x,y in Q:
        z=(x%p,y%p)
        for j in range(J):
            vals=[]
            for r,s in ROWS:
                if j>r: vals.append((0,0))
                else:
                    v=pairmul(pairpow(z,r-j,p),pairpow((x%p,-y%p),s,p),p)
                    f=prod(range(r-j+1,r+1))
                    vals.append((f*v[0]%p,f*v[1]%p))
            for i in range(28):
                a,b=vals[i]
                for k in range(i+1):
                    c,d=vals[k]
                    g[i][k]=(g[i][k]+2*(a*c+D*b*d))%p
    for i in range(28):
        for k in range(i):g[k][i]=g[i][k]
    return g


def block(G,I):
    return [[G[i][j] for j in I] for i in I]


def orbits(p):
    available={(x,y) for x in range(p) for y in range(p)}
    out=[]
    while available:
        z=min(available);rev=((-z[0])%p,(-z[1])%p)
        o=tuple(sorted({z,rev}))
        available.difference_update(o)
        out.append(o)
    return out


def ellipse_points(rho):
    return [(x,y) for y in range(-rho,rho+1)
            for x in range(-rho,rho+1) if x*x+D*y*y<=rho*rho]


def centered(z,p):
    return z if z<=p//2 else z-p


def main():
    assert (-D)%P == 3*3%P
    U=U_at(P)
    assert det_mod(U,P)==1
    O=orbits(P)
    assert len(O)==25 and sorted(map(len,O))==[1]+[2]*24
    for orbit in O:
        G=gram_split(orbit,P,3)
        assert G==gram_pairs(orbit,P), ("two source oracles differ",orbit)
        assert all(G[i][j]==0 for i in EVEN for j in ODD)
        assert congruent(block(G,EVEN),block(G,ODD),U,P),orbit
    print("ALL_RESIDUE_ORBITS",{"D":D,"p":P,"orbits":25,"total_residues":49,
          "row_space":28,"parity_dimensions":[14,14],
          "nonzero_entries_of_U":49,"detU":1,
          "two_independent_arithmetic_oracles":True,
          "one_U_congruent_for_every_orbit":True})
    for rho,n,expected in [(16,59,2),(25,133,0)]:
        Q=ellipse_points(rho)
        assert len(Q)==n
        G=gram_pairs(Q,P)
        assert G==gram_split(Q,P,3)
        even,odd=block(G,EVEN),block(G,ODD)
        assert congruent(even,odd,U,P)
        assert det_mod(even,P)==det_mod(odd,P)==expected
        print("ACTUAL_SUPPORT",{"rho":rho,"points":n,
              "det_even":expected,"det_odd":expected})
    # Separate arithmetic place: same centered U is NOT automatically an isometry.
    assert (-D)%11 == 4*4%11
    failed=0
    for orbit in orbits(7):
        if all(y in (0,1,6) for x,y in orbit):
            integer_o=[(centered(x,7),centered(y,7)) for x,y in orbit]
            G=gram_split(integer_o,11,4)
            if not congruent(block(G,EVEN),block(G,ODD),U_at(11),11):
                failed+=1
    assert failed>=1
    print("PRIME_BOUNDARY",{"p":11,
          "same_centered_integer_lift_failed_orbits":failed,
          "det_lift_mod11":det_mod(U_at(11),11)})
    G=gram_pairs([(1,0)],P)
    assert any(G[i][j] for i in EVEN for j in ODD)
    print("NEGATIVE_CONTROL",{"unpaired_point_cross_parity_nonzero":True})
    print("PASS: exact source-constrained, place-specific intertwiner certificate")


if __name__=="__main__":
    main()
