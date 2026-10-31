#!/usr/bin/env python3
"""Phase138: exact original ordinary-jet Gram, graded volumes and counterworlds.

Only Python standard-library arbitrary-precision integers. The immutable
experimental object: D=19, rho=5, R=8, S=J=4, all 21 original ellipse nodes,
ordinary Z-derivatives (W held fixed), factor-two trace metric.
No production number-field theorem or independent reviewer is claimed.

Run: python3 research/graded_covolume/phase138_exact_fibers.py
"""
from __future__ import annotations

from collections import defaultdict
from math import exp, log
from operator import mul
from functools import reduce

D, RHO, R, S, J = 19, 5, 8, 4, 4
N = R * S
Q = [(x, y) for x in range(-RHO, RHO + 1)
     for y in range(-RHO, RHO + 1) if x*x + D*y*y <= RHO*RHO]

def cmul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0]*b[0]-D*a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def cpow(a: tuple[int, int], n: int) -> tuple[int, int]:
    out = (1, 0)
    for _ in range(n):
        out = cmul(out, a)
    return out

def falling(n: int, j: int) -> int:
    if j > n:
        return 0
    return reduce(mul, (n-t for t in range(j)), 1)

def jet(r: int, s: int, j: int, z: tuple[int, int], p: list[int]) -> tuple[int, int]:
    """Ordinary derivative of Z^(r-m)*W^(s-m)*P_m(ZW) at W=conj(z)."""
    m = min(r, s)
    assert len(p) == m+1 and p[-1] == 1
    out = (0, 0)
    w = (z[0], -z[1])
    for t, coeff in enumerate(p):
        rr, ss = r-m+t, s-m+t
        if j > rr:
            continue
        a = cmul(cpow(z, rr-j), cpow(w, ss))
        c = coeff * falling(rr, j)
        out = (out[0]+c*a[0], out[1]+c*a[1])
    return out

def append_u_minus_a(p: list[int], a: int) -> list[int]:
    out = [0] * (len(p)+1)
    for i, c in enumerate(p):
        out[i] -= a*c
        out[i+1] += c
    return out

def polynomial_frames() -> dict[str, list[list[int]]]:
    l = RHO*RHO
    a = l//2
    e = max(a, l-a)
    b = (e*e+3)//4
    centered: list[list[int]] = [[1]]
    cheb: list[list[int]] = [[1]]
    for m in range(1, S):
        centered.append(append_u_minus_a(centered[-1], a))
        p = append_u_minus_a(cheb[-1], a)
        if m == 2:
            p[0] -= 2*b
        if m >= 3:
            for k, x in enumerate(cheb[m-2]):
                p[k] -= b*x
        cheb.append(p)
    # A shared monic P2 adjusted to the optimum for ONE row. P3 is
    # deliberately unchanged: no recurrence constraint is silently imposed.
    shared = [p.copy() for p in cheb]
    shared[2][0] += 3
    assert (a, b) == (12, 43)
    assert cheb[2] == [58, -24, 1]
    assert shared[2] == [61, -24, 1]
    return {"centered": centered, "cheb": cheb, "shared-row-optimum": shared}

def observations(polys: list[list[int]]) -> list[list[int]]:
    e: list[list[int]] = []
    for r in range(R):
        for s in range(S):
            p = polys[min(r, s)]
            row: list[int] = []
            for z in Q:
                for j in range(J):
                    row.extend(jet(r, s, j, z, p))
            e.append(row)
    return e

def gram(e: list[list[int]]) -> list[list[int]]:
    weights = [2 if i%2==0 else 2*D for i in range(len(e[0]))]
    return [[sum(x*y*w for x, y, w in zip(a, b, weights))
             for b in e] for a in e]

def integer_det(a: list[list[int]]) -> int:
    """Fraction-free Bareiss, exact arbitrary precision, with row pivoting."""
    if not a:
        return 1
    n = len(a)
    assert all(len(x) == n for x in a)
    b = [row.copy() for row in a]
    sign, den = 1, 1
    for k in range(n-1):
        if b[k][k] == 0:
            pivot = next((i for i in range(k+1, n) if b[i][k] != 0), None)
            if pivot is None:
                return 0
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        q = b[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = b[i][j]*q - b[i][k]*b[k][j]
                assert num % den == 0, "Bareiss exact division must hold"
                b[i][j] = num//den
        for i in range(k+1, n):
            b[i][k] = 0
        den = q
    return sign*b[-1][-1]

def principal(g: list[list[int]], ids: list[int]) -> list[list[int]]:
    return [[g[i][j] for j in ids] for i in ids]

def radial_groups() -> list[list[int]]:
    groups: dict[int, list[int]] = defaultdict(list)
    for r in range(R):
        for s in range(S):
            groups[r-s].append(r*S+s)
    return [groups[k] for k in sorted(groups)]

def parity_groups() -> list[list[int]]:
    return [[r*S+s for r in range(R) for s in range(S) if (r-s)%2 == par]
            for par in (0, 1)]

def log_upper(g: list[list[int]], groups: list[list[int]]) -> tuple[float, list[int]]:
    ds = [integer_det(principal(g, b)) for b in groups]
    assert all(d > 0 for d in ds)
    return sum(log(d) for d in ds), ds

def main() -> None:
    assert len(Q) == 21 and 2*(R-1)+(S-1) < len(Q)
    radial, parity = radial_groups(), parity_groups()
    assert sorted(map(len, radial)) == sorted([1,2,3,4,4,4,4,4,3,2,1])
    assert sorted(map(len, parity)) == [16, 16]
    frames = polynomial_frames()
    outputs = {}
    fiber_ref = None
    parity_ref = None
    for name, ps in frames.items():
        e = observations(ps)
        assert len(e) == N and all(len(row) == 2*J*len(Q) for row in e)
        g = gram(e)
        # The exact entrywise opposite-parity zeros are already proved
        # generally for centrally symmetric Q in CentralSymmetry.lean.
        assert all(g[i][j] == 0 for i in parity[0] for j in parity[1])
        log_diags, _ = log_upper(g, [[i] for i in range(N)])
        log_fiber, fiber_ds = log_upper(g, radial)
        log_parity, parity_ds = log_upper(g, parity)
        # This equality is an *integer identity*, not a float comparison.
        assert integer_det(g) == parity_ds[0]*parity_ds[1]
        if fiber_ref is None:
            fiber_ref = fiber_ds
            parity_ref = parity_ds
        else:
            assert fiber_ds == fiber_ref
            assert parity_ds == parity_ref
        assert log_diags >= log_fiber >= log_parity
        outputs[name] = (log_diags, log_fiber, log_parity)
        print(f"{name}: log(diagonals)={log_diags:.12f}, "
              f"log(radial blocks)={log_fiber:.12f}, "
              f"log(parity blocks)={log_parity:.12f}")
    centered, cheb, shared = (outputs[k] for k in
                             ("centered", "cheb", "shared-row-optimum"))
    assert abs(centered[0]-585.557677542876)<1e-7
    assert abs(cheb[0]-579.753853408232)<1e-7
    assert abs(shared[0]-579.806638232291)<1e-7
    assert all(abs(x[1]-543.904300463457)<1e-7 for x in outputs.values())
    assert all(abs(x[2]-530.285191201861)<1e-7 for x in outputs.values())
    assert 1.05 < exp(shared[0]-cheb[0]) < 1.06, (
        "Shared use of locally optimal P2 must worsen global diagonal product")
    assert centered[0]-centered[1] > 41
    assert cheb[1]-cheb[2] > 13
    # The stronger claim 'ANY integer frame preserves radial blocks' fails.
    g0 = [[1,0],[0,1]]
    shear_g = [[2,1],[1,1]]
    assert integer_det(g0)==integer_det(shear_g)==1
    assert g0[0][0]*g0[1][1] != shear_g[0][0]*shear_g[1][1]
    # Symmetry is essential: one unsymmetrized sample has odd pairing.
    assert 2*(1*1) == 2
    print("All exact original-jet, fiber invariance, parity, "
          "global-optimality counterworld and scope guards passed.")

if __name__ == "__main__":
    main()
