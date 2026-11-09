#!/usr/bin/env python3
"""Phase202 same-prime residue-count factorization; preregistered in Issue #130.

G(Q) mod p depends on the multiplicities of reduced integer-pair residues.
Unlike the original jet_matrix, the grouped oracle below never sees full Q.
It does not identify places, real positivity, external minors or field cutoffs.
"""
from collections import Counter
from hashlib import sha256
from math import prod
from placewise_jet_probe import jets, points, trace_gram, rank_p


def residue_counts(Q, p):
    return Counter((x % p, y % p) for x, y in Q)


def independent_jet(D, r, s, j, x, y, p):
    if j > r:
        return 0, 0
    f = prod(range(r - j + 1, r + 1)) % p

    def times(a, b):
        return ((a[0]*b[0] - D*a[1]*b[1]) % p,
                (a[0]*b[1] + a[1]*b[0]) % p)

    def power(z, n):
        q = (1, 0)
        for _ in range(n):
            q = times(q, z)
        return q

    a,b = times(power((x,y),r-j), power((x,-y),s))
    return a*f%p, b*f%p


def residue_gram(D, R, S, J, p, counts):
    """Construct full trace Gram from only Fp-valued residue multiplicities."""
    N=R*S
    G=[[0]*N for _ in range(N)]
    for (x,y),c in counts.items():
        weight=c%p
        if not weight:
            continue
        for j in range(J):
            values=[independent_jet(D,r,s,j,x,y,p)
                    for r in range(R) for s in range(S)]
            for i,(a,b) in enumerate(values):
                if not (a or b):
                    continue
                for k,(aa,bb) in enumerate(values[:i+1]):
                    G[i][k]=(G[i][k]+2*weight*(a*aa+D*b*bb))%p
    for i in range(N):
        for k in range(i):
            G[k][i]=G[i][k]
    return G


def test(D,R,S,J,rho,p):
    Q,_,_,A=jets(D,R,S,J,rho,p)
    direct=trace_gram(A,D,p)
    counts=residue_counts(Q,p)
    grouped=residue_gram(D,R,S,J,p,counts)
    assert direct==grouped, "FAIL source entry vs independent residue grouping"
    copy=counts.copy()
    copy[next(iter(copy))]+=p
    assert residue_gram(D,R,S,J,p,copy)==grouped
    rank=rank_p(grouped,p)
    digest=sha256(bytes(v%p for row in grouped for v in row)).hexdigest()[:16]
    print("RESIDUE",{"D":D,"p":p,"rho":rho,"points":len(Q),
          "occupied":len(counts),
          "nonzero_weight":sum(c%p!=0 for c in counts.values()),
          "zero_weight":sum(c%p==0 for c in counts.values()),
          "rankG":rank,"sha256_prefix":digest,
          "pfold_duplicate_preserves_modular_gram":True})
    return counts,rank


def main():
    result={}
    for p in (7,11):
        c0,r0=test(215,53,2,2,16,p)
        c1,r1=test(215,53,2,2,25,p)
        delta={z:(c1[z]-c0[z])%p for z in set(c0)|set(c1)}
        changed={z:v for z,v in delta.items() if v}
        assert sum(delta.values())%p==(133-59)%p and changed
        print("SUPPORT_DELTA",{"p":p,"changed_residue_classes":len(changed),
            "added_points":74,"rank_change":r1-r0,
            "first_changes":sorted(changed.items())[:12]})
        result[p]=(r0,r1)
    assert result=={7:(28,26),11:(44,44)},result
    print("PASS exact same-place residue-count factorization")


if __name__=="__main__":
    main()
