#!/usr/bin/env python3
"""Phase328: a source-preserving quaternionic *stabilization and return*.

This is NOT a quaternionic action on the unchanged original jet space.
The original integer trace Gram B acts on J=Z^N.  On J^4 install:

  Bhat = diag(B, I_N, I_N, I_N)
  iu   = Uu * i0                     (inclusion, 4N by N)
  pu   = p0 * Uu.T                  (return, N by 4N)
  Bu   = Uu * Bhat * Uu.T           (moving Gram, 4N by 4N)

where Uu = L_u tensor I_N is the integral signed permutation from
u in Q8. These exact *integer* matrices obey

  pu*iu = I_N
  iu.T*Bu*iu = B
  det Bu = det B
  Buv = Uu * Bv * Uu.T

for arbitrary integer B. Spin-sign (-1) survives in iu, but cancels
in Bu. An invariant alternative diag(B,B,B,B) has det(B)^4 and MUST
NOT be mistaken for a new divisor of det B.

The exact source Gram implementation below follows the definitions
integerDerivativeRow, integerPairTrace and integerRectangularTraceGram
in lean/TenthDiscriminant/IntegerTraceGram.lean on small Q,D,J,R,S.
No new discriminant bound, field of characteristic one, or
equivariant quaternionic return to the unchanged jet lattice.
"""
from __future__ import annotations

from math import prod
from typing import Sequence

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase327"))

from interleaved_f1_prime import (  # noqa: E402
    Q8, BASIS, ONE as H_ONE, NEG_ONE as H_NEG_ONE,
    conjugate as quaternion_conj, norm as quaternion_norm,
    product as quaternion_product,
)

Matrix = tuple[tuple[int, ...], ...]
QuadraticPair = tuple[int, int]


def identity(n: int) -> Matrix:
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def transpose(a: Matrix) -> Matrix:
    if not a:
        return ()
    return tuple(zip(*a))


def matrix_mul(a: Matrix, b: Matrix) -> Matrix:
    if not a:
        return ()
    if not b:
        raise ValueError("Matrix shapes are not compatible")
    common = len(b)
    if any(len(row) != common for row in a):
        raise ValueError("Matrix shapes are not compatible")
    width = len(b[0])
    if any(len(row) != width for row in b):
        raise ValueError("Ragged right matrix")
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(common))
              for j in range(width))
        for i in range(len(a))
    )


def matrix_mod(a: Matrix, ell: int) -> Matrix:
    if ell < 2:
        raise ValueError("Reduction requires a prime characteristic >= 2")
    return tuple(tuple(x % ell for x in row) for row in a)


def block_diag(*blocks: Matrix) -> Matrix:
    sizes = [len(b) for b in blocks]
    if any(len(row) != n for b, n in zip(blocks, sizes) for row in b):
        raise ValueError("Blocks must be square")
    offsets = [sum(sizes[:j]) for j in range(len(blocks))]
    n = sum(sizes)
    out = [[0] * n for _ in range(n)]
    for block, size, off in zip(blocks, sizes, offsets):
        for i in range(size):
            for j in range(size):
                out[off + i][off + j] = block[i][j]
    return tuple(tuple(row) for row in out)


def determinant(a: Matrix) -> int:
    """Exact integer Bareiss determinant; permutations handle zero pivots."""
    n = len(a)
    if n == 0:
        return 1
    if any(len(row) != n for row in a):
        raise ValueError("Only square matrices have determinants")
    b = [list(row) for row in a]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if b[k][k] == 0:
            pivot_row = next((r for r in range(k + 1, n)
                              if b[r][k] != 0), None)
            if pivot_row is None:
                return 0
            b[k], b[pivot_row] = b[pivot_row], b[k]
            sign = -sign
        pivot = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * b[i][j] - b[i][k] * b[k][j]
                if numerator % previous != 0:
                    raise AssertionError("Bareiss exact division failed")
                b[i][j] = numerator // previous
            b[i][k] = 0
        previous = pivot
    return sign * b[-1][-1]


def quaternion_left_frame(u: tuple[int, int, int, int], n: int) -> Matrix:
    """L_u tensor I_n: exactly the signed permutation on four copies."""
    if n <= 0:
        raise ValueError("Frame requires positive source rank")
    if u not in Q8 or quaternion_norm(u) != 1:
        raise ValueError("Integral unit quaternion must belong to Q8")
    left = tuple(
        tuple(quaternion_product(u, BASIS[c])[r] for c in range(4))
        for r in range(4)
    )
    return tuple(tuple(left[i//n][j//n] if i % n == j % n else 0
                       for j in range(4*n)) for i in range(4*n))


def scalar_inclusion(n: int) -> Matrix:
    if n <= 0:
        raise ValueError("positive source rank required")
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(4*n))


def stabilized_gram(b: Matrix, mode: str = "return") -> Matrix:
    n = len(b)
    if n <= 0 or any(len(row) != n for row in b):
        raise ValueError("Gram must be nonempty square")
    if mode == "return":
        return block_diag(b, identity(n), identity(n), identity(n))
    if mode == "isometric":
        return block_diag(b, b, b, b)
    raise ValueError("Unknown stabilization mode")


def frame_transport(b: Matrix, u: tuple[int, int, int, int]) -> dict:
    """Integral transport, exact source return and moving Gram."""
    n = len(b)
    U = quaternion_left_frame(u, n)
    Uinv = transpose(U)
    embed = matrix_mul(U, scalar_inclusion(n))
    projection = matrix_mul(transpose(scalar_inclusion(n)), Uinv)
    base = stabilized_gram(b, "return")
    moving = matrix_mul(matrix_mul(U, base), Uinv)
    return {
        "U": U, "Uinv": Uinv, "embed": embed, "return": projection,
        "base": base, "moving": moving
    }


def return_gram(bundle: dict) -> Matrix:
    return matrix_mul(
        matrix_mul(transpose(bundle["embed"]), bundle["moving"]),
        bundle["embed"],
    )


def verify_stable_return(b: Matrix, u: tuple[int,int,int,int]) -> dict:
    """All exact integral bridge equalities, including determinants."""
    n = len(b)
    data = frame_transport(b, u)
    U, Ut = data["U"], data["Uinv"]
    assert matrix_mul(U, Ut) == identity(4*n)
    assert matrix_mul(Ut, U) == identity(4*n)
    assert matrix_mul(data["return"], data["embed"]) == identity(n)
    assert return_gram(data) == b
    assert determinant(U) == 1
    db = determinant(b)
    assert determinant(data["moving"]) == db
    assert determinant(data["base"]) == db
    return {"rank": n, "frame": u, "det_source": db,
            "det_moving": determinant(data["moving"]),
            "returned_exact": True, "unimodular": True}


def pair_mul(D: int, a: QuadraticPair, b: QuadraticPair) -> QuadraticPair:
    return (a[0]*b[0] - D*a[1]*b[1],
            a[0]*b[1] + a[1]*b[0])


def pair_pow(D: int, a: QuadraticPair, n: int) -> QuadraticPair:
    if n < 0:
        raise ValueError("negative exponent not present in integer jet")
    value = (1, 0)
    for _ in range(n):
        value = pair_mul(D, value, a)
    return value


def falling(r: int, j: int) -> int:
    if j > r:
        return 0
    return prod(range(r-j+1, r+1))


def integer_derivative_row(
    D: int, r: int, s: int, j: int, p: QuadraticPair
) -> QuadraticPair:
    if j > r:
        return (0, 0)
    z = pair_pow(D, p, r-j)
    w = pair_pow(D, (p[0], -p[1]), s)
    a, b = pair_mul(D, z, w)
    return (falling(r, j)*a, falling(r,j)*b)


def original_integer_trace_gram(
    Q: Sequence[QuadraticPair], D: int, J: int, R: int, S: int
) -> Matrix:
    """Literal low-dimensional source Gram; no new W derivatives."""
    if D <= 0 or J < 0 or R < 1 or S < 1:
        raise ValueError("Invalid original source parameters")
    if len(set(Q)) != len(Q):
        raise ValueError("Q is a Finset: duplicate samples are forbidden")
    rows = [(r,s) for r in range(R) for s in range(S)]
    cache = {
        (k,j,p): integer_derivative_row(D,r,s,j,p)
        for k,(r,s) in enumerate(rows)
        for j in range(J) for p in Q
    }
    return tuple(
        tuple(
            sum(
                2 * (cache[(i,j,p)][0] * cache[(k,j,p)][0] +
                     D * cache[(i,j,p)][1] * cache[(k,j,p)][1])
                for j in range(J) for p in Q
            )
            for k in range(R*S)
        )
        for i in range(R*S)
    )


def counterexample_fixed_metric() -> dict:
    """Why Q8 cannot be an isometry of B⊕I⊕I⊕I for all B."""
    b = ((2,),)
    base = stabilized_gram(b)
    U = quaternion_left_frame((0,1,0,0), 1)
    turned = matrix_mul(matrix_mul(U, base), transpose(U))
    assert turned != base
    iso = stabilized_gram(b, "isometric")
    fixed = matrix_mul(matrix_mul(U, iso), transpose(U))
    assert fixed == iso
    assert determinant(base) == determinant(turned) == 2
    assert determinant(iso) == 16
    assert determinant(iso) != determinant(b)
    return {"original_det":2,"covariant_det":2,
            "fixed_invariant_det":16,
            "fixed_metric_isometry_fails_for_return_stabilization":True}


if __name__ == "__main__":
    import json
    result = []
    for D, Q, J, R, S in (
        (7, ((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1)), 2, 2, 2),
        (11, ((1,0),(0,1),(2,1),(-1,1)), 2, 3, 1),
    ):
        b = original_integer_trace_gram(Q,D,J,R,S)
        result.append({"D":D,"J":J,"R":R,"S":S,
                       "source_det":determinant(b),
                       "frames":[verify_stable_return(b,u)
                                 for u in (H_ONE,H_NEG_ONE)]})
    print("PHASE328_STABLE_RETURN_PASS",json.dumps(result,sort_keys=True))
