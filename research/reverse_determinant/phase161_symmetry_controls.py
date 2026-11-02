#!/usr/bin/env python3
"""Phase161: exact symmetries of the ORIGINAL ordinary-Z jet observations.

Finite tests only. The source columns and weights come from Phase159,
which was cross-checked against the Phase147 original integer evaluator.
No Hasse substitution, new prime-mass theorem, or improved field cutoff.
"""
from sympy import Matrix, diag, eye, ZZ
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from phase159_observation_continuum import (
    ordinary_effective, rankmod, obstruction, determinant_mod,
    beta, source_correspondence,
)


def observation(Q, D, R, S, p=None):
    entries, weights, _ = ordinary_effective(Q, D, R, S, p)
    return Matrix(entries), weights


def trace_gram(E, weights):
    return E * diag(*weights) * E.T


def gauge_signs(Q, S, kind):
    """Signed channel action, in the exact original (point,j,re/im) order."""
    signs = []
    for x, y in Q:
        for j in range(S):
            signs.append(1 if kind == "conj" else (-1)**j)
            if y:
                signs.append(-1 if kind == "conj" else
                             ((-1)**j if kind == "inverse" else -(-1)**j))
    return diag(*signs)


def exact_source_symmetries():
    D, R, S = 19, 8, 4
    Q = [(-1, 1), (0, 0), (2, -1), (1, 0)]
    E, w = observation(Q, D, R, S)
    G = trace_gram(E, w)
    P = diag(*[(-1)**(r+s) for r in range(R) for s in range(S)])
    actions = (
        ("conj", lambda x, y: (x, -y)),
        ("inverse", lambda x, y: (-x, -y)),
        ("horizontal", lambda x, y: (-x, y)),
    )
    for name, f in actions:
        transformed = [f(x, y) for x, y in Q]
        Et, wt = observation(transformed, D, R, S)
        assert wt == w
        expected = (E if name == "conj" else P*E) * gauge_signs(Q, S, name)
        assert Et == expected, name
        expected_gram = G if name == "conj" else P*G*P
        assert trace_gram(Et, wt) == expected_gram, name
    print("PHASE161_SOURCE_EQUIVARIANCE_PASS")


def nontrivial_identity_action():
    # The involution fixes this singleton support, and preserves its Gram,
    # but is NOT the identity on its finite cokernel.
    E, w = observation([(0, 3)], 3, 2, 2)
    P = diag(1, -1, -1, 1)
    J = diag(1, -1, -1, 1)
    assert E == Matrix([[1, 0, 0, 0], [0, -3, 0, 0],
                        [0, 3, 1, 0], [27, 0, 0, -3]])
    assert P*E*J == E
    G = trace_gram(E, w)
    assert P*G*P == G
    smith = smith_normal_form(E, domain=ZZ)
    assert [abs(int(smith[i, i])) for i in range(4)] == [1, 1, 3, 3]
    H = hermite_normal_form(E)
    assert int(H.det()) != 0
    # In Z^4 / im(E), the second coordinate survives mod 3; P negates it.
    e2 = Matrix([0, 1, 0, 0])
    defect = H.inv()*(P-eye(4))*e2
    assert any(c.q != 1 for c in defect)
    e4 = Matrix([0, 0, 0, 1])
    assert P*e4 == e4
    print("PHASE161_COKERNEL_ACTION_PASS")


def blocks(O, S):
    ev = [j for j in range(S-1) if j % 2 == 0]
    od = [j for j in range(S-1) if j % 2 == 1]
    assert all(int(O[i,j]) == 0 for i in range(S-1)
               for j in range(S-1) if (i-j) % 2)
    return O.extract(ev, ev), O.extract(od, od)


def characteristic_examples():
    # Symmetric, 31-root characteristic subset: removing center succeeds.
    D, p, S = 163, 31, 5
    Q = [(x, 0) for x in range(-10, 11)] + [(x, 1) for x in range(-2, 3)]
    assert len(Q) == 26 and beta(Q, D, p-1, S) == 430
    assert rankmod(observation(Q, D, p-1, S, p)[0].tolist(), p) == 150
    Qm = [q for q in Q if q != (0, 0)]
    O = Matrix(obstruction(Qm, D, p, S))
    even, odd = blocks(O, S)
    assert even == Matrix([[9, 14], [8, 23]])
    assert odd == Matrix([[0, 20], [10, 28]])
    assert (determinant_mod(even.tolist(), p),
            determinant_mod(odd.tolist(), p)) == (2, 17)
    assert determinant_mod(O.tolist(), p) == 3
    assert beta(Qm, D, p-1, S) == 450
    assert rankmod(observation(Qm, D, p-1, S, p)[0].tolist(), p) == 150
    print("PHASE161_SPLIT_OBSTRUCTION_P31_PASS")

    # Falsifying control with D congruent to 3 modulo 4 and inert p=11.
    # It is NOT an admissible production prime for D=3.
    D, p, S = 3, 11, 3
    Q = [(x, 0) for x in range(-3, 4)] + [(0, 1), (0, 2)]
    assert len(Q) == 9 and all(x*x + D*y*y <= 25 for x,y in Q)
    assert pow((-D) % p, (p-1)//2, p) == p-1
    assert rankmod(observation(Q, D, p-1, S, p)[0].tolist(), p) == 30
    Qm = [q for q in Q if q != (0, 0)]
    O = Matrix(obstruction(Qm, D, p, S))
    assert O == Matrix([[0, 0], [0, 3]])
    assert rankmod(observation(Qm, D, p-1, S, p)[0].tolist(), p) == 29
    print("PHASE161_SYMMETRIC_DELETION_COUNTEREXAMPLE_PASS")


if __name__ == "__main__":
    source_correspondence()
    exact_source_symmetries()
    nontrivial_identity_action()
    characteristic_examples()
    print("PHASE161_SYMMETRIES_PASS: exact finite checks; no new bound")
