#!/usr/bin/env python3
"""Phase275: two-sided original-source tube, split/inert/negative controls.

Uses the repository's ORIGINAL integer-pair ordinary-Z-jet oracle from
Phase204 (not a Hasse rewrite) and a separately implemented translation
action. An M finite regression, not a field theorem or an external review.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase204"))
from ordinary_jet_filtration import jet

P, MOD, R, S, J = 3, 9, 4, 3, 3


def original(D, z):
    return {(r, s, j): tuple(v % MOD for v in jet(D, r, s, j, z))
            for r in range(R) for s in range(S) for j in range(J)}


def action(A, delta):
    B = {}
    for r in range(R):
        for s in range(S):
            for j in range(J):
                x = A[(r, s, j)]
                dz = A[(r, s, j+1)] if j+1 < J else (0,0)
                dw = A[(r, s-1, j)] if s else (0,0)
                B[(r, s, j)] = tuple(
                    (x[k] + delta*(dz[k] + s*dw[k])) % MOD
                    for k in (0,1))
    return B


def quadratic_w(j,z,D=7):
    # F(Z,W)=(Z-1)^2*W, a linear combination of the ORIGINAL r=0,1,2
    # source rows, not a new observation convention.
    a=jet(D,2,1,j,z)
    b=jet(D,1,1,j,z)
    c=jet(D,0,1,j,z)
    return tuple((a[k]-2*b[k]+c[k]) % MOD for k in (0,1))


def main():
    cases = 0
    assert (-7) % P == 2  # inert prime for Q(sqrt(-7))
    assert (-11) % P == 1 # split prime for Q(sqrt(-11))
    for D in (7,11):
        for z in ((1,1),(0,1),(-1,1)):
            src = original(D,z)
            for delta in (3,-3,6):
                translated=original(D,(z[0]+delta,z[1]))
                got=action(src,delta)
                assert got==translated,(D,z,delta,
                    next((k,got[k],translated[k]) for k in got
                         if got[k]!=translated[k]))
                cases += len(src)*2
            assert action(action(src,3),-3)==src
            assert action(action(src,3),3)==action(src,6)
            cases+=2*len(src)*2

    # Invalid J=2 descent: F=(Z-1)^2 W and zero have identical 2-jets
    # at z=(1,0), but different moved first derivatives at z=(4,0).
    assert quadratic_w(0,(1,0)) == (0,0)
    assert quadratic_w(1,(1,0)) == (0,0)
    assert quadratic_w(1,(4,0)) == (6,0)
    cases += 3
    print("PASS source-pair-entry controls",cases,
          "inert D7 and split D11; two-sided W shift; mod9;",
          "J=2 negative descent; additive and inverse controls")


if __name__ == "__main__":
    main()
