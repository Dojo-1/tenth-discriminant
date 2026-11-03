#!/usr/bin/env python3
"""Phase179: exact typed transport counterworlds, no new discriminant bound.

Two layers:
  * A standalone exact 2x2 reference oracle (not dependent on the jet source).
  * A source-matched D=19, R=8, S=J=4 original ordinary-Z-jet gauge test.
Do NOT treat a det-one rational frame as an integer unimodular gauge.
"""
from __future__ import annotations

from sympy import Matrix, Rational, ZZ, eye
from sympy.matrices.normalforms import smith_normal_form
from phase144_verifier import D, R, S, J, FULL, evaluation
from phase144_minimum_support import SIX
from phase145_ortho_anti_ambig import P, gram
from phase146_translation_newton import transport
from phase147_prime_adequacy import original_eval

assert (D, R, S, J) == (19, 8, 4, 4)


def det(X):
    return int(X.det(method="domain-ge"))


def pinch(G, grading):
    assert grading * grading == eye(G.rows)
    return (G + grading * G * grading.T) / 2


def ratio(G, grading):
    assert det(G) > 0
    return Rational(det(pinch(G, grading)), det(G))


def toy_oracle():
    G = Matrix([[2, 1], [1, 2]])
    P2 = Matrix([[1, 0], [0, -1]])
    U = Matrix([[1, 1], [0, 1]])
    Ui = Matrix([[1, -1], [0, 1]])
    assert U * Ui == eye(2) and det(U) == 1 and det(G) == 3
    Gt = U * G * U.T
    Pt = U * P2 * Ui
    assert Gt == Matrix([[6, 3], [3, 2]]) and Pt * Pt == eye(2)
    assert det(Gt) == det(G) == 3
    assert pinch(Gt, Pt) == U * pinch(G, P2) * U.T
    assert ratio(G, P2) == ratio(Gt, Pt) == Rational(4, 3)
    assert ratio(Gt, P2) == Rational(4, 1)
    assert ratio(Gt, P2) != ratio(Gt, Pt)

    # A det-one *rational* shear is NOT GL(2,Z). Determinant and every
    # determinant prime valuation agree, yet integral images differ.
    H = Matrix([[1, Rational(1, 2)], [0, 1]])
    assert det(H) == 1 and H.inv() == Matrix([[1, -Rational(1, 2)], [0, 1]])
    assert det(H * G * H.T) == det(G)
    assert H != Matrix([[1, 0], [0, 1]])
    assert H[0, 1].q == 2
    # A STRONGER false positive: two INTEGRAL positive Grams, the same
    # determinant and every determinant valuation, but DIFFERENT Smith
    # factors. A rational det-one gauge is not an integral isometry.
    G_integral = Matrix.diag(4, 4)
    G_integral_new = H * G_integral * H.T
    assert G_integral_new == Matrix([[5, 2], [2, 4]])
    assert det(G_integral) == det(G_integral_new) == 16
    assert all(z.q == 1 for z in G_integral_new)
    smith_old = smith_normal_form(G_integral, domain=ZZ)
    smith_new = smith_normal_form(G_integral_new, domain=ZZ)
    assert [abs(int(smith_old[i, i])) for i in range(2)] == [4, 4]
    assert [abs(int(smith_new[i, i])) for i in range(2)] == [1, 16]
    # Mod-2 ranks are 0 versus 1, so even GL_2(Z)-congruence is impossible.
    assert (G_integral.applyfunc(lambda z: z % 2)).rank() == 0
    assert (G_integral_new.applyfunc(lambda z: z % 2)).rank() == 1
    # For an integer lattice point (x,y), H^-1(x,y) is integral iff y even.
    for x in range(-7, 8):
        for y in range(-7, 8):
            coordinates = H.inv() * Matrix([x, y])
            assert all(z.q == 1 for z in coordinates) == (y % 2 == 0)
    C = Matrix([[1, 0], [0, 2]])  # basis for Z^2 intersection H Z^2
    assert all(z.q == 1 for z in H.inv() * C)
    assert Rational(det(C), det(eye(2))) == 2
    assert Rational(det(C), det(H)) == 2
    # Both quotients have index two: same covolume does NOT recover lattice.

    F = Matrix([[1, 1], [1, -1]])
    assert det(F) == -2 and F.inv() * F == eye(2)
    assert (F.applyfunc(lambda z: z % 2)).rank() == 1
    factor = smith_normal_form(F, domain=ZZ)
    assert sorted(abs(int(factor[i, i])) for i in range(2)) == [1, 2]
    B = Matrix.diag(2, 38)  # original channel metric at D=19
    assert det(F * B * F.T) == 4 * det(B)
    # If the metric is itself transported contravariantly, the Gram
    # reconstructs exactly over Q; the Z-lattice still changes.
    transported_metric = F.inv() * B * F.inv().T
    assert F * transported_metric * F.T == B
    assert transported_metric == Matrix([[10, -9], [-9, 10]])
    # Integrality of the compensated metric still does NOT make F a Z-unit.
    print("TOY PASS: integral gauge chi 4/3 vs fixed grading chi 4; "
          "SL2(Q) half shear det=1 but two 2-torsion relative quotients; "
          "Fourier index=2 and fixed-metric det factor=4; "
          "equal integral Gram det=16 but Smith profiles (4,4) vs (1,16)", flush=True)


def original_jet_control():
    assert original_eval(SIX, D) == evaluation(SIX)
    E = evaluation(SIX)
    assert E.shape == (R*S, 2*J*len(SIX))
    T = transport(2)
    translated = [(x + 2, y) for x, y in SIX]
    Es = evaluation(translated)
    assert Es == T * E and det(T) == 1
    G = gram(E)
    Gs = gram(Es)
    assert Gs == T * G * T.T
    assert det(G) == det(Gs) > 0
    # Exact, no floating log comparisons. The translation here is
    # deliberately OUTSIDE the original ellipse: gauge null only.
    assert not set(translated).issubset(set(FULL))
    Pmoved = T * P * transport(-2)
    assert Pmoved * Pmoved == eye(R*S)
    assert pinch(Gs, Pmoved) == T * pinch(G, P) * T.T
    exact_ratio = ratio(G, P)
    assert exact_ratio == ratio(Gs, Pmoved)
    assert ratio(Gs, P) != exact_ratio
    assert det(Gs) == det(G)
    # Another certificate proxy can change while det remains unchanged.
    diag_old = 1
    diag_new = 1
    for i in range(R*S):
        diag_old *= int(G[i, i])
        diag_new *= int(Gs[i, i])
    assert diag_old != diag_new and diag_old >= det(G) and diag_new >= det(Gs)
    print("D19 SOURCE PASS: original ordinary-Z jets; exact determinant, "
          "moving parity ratio, changing fixed parity ratio and diagonal "
          "Hadamard majorant", flush=True)


if __name__ == "__main__":
    toy_oracle()
    original_jet_control()
    print("PHASE179_PASS: exact transport identity and typed obstruction "
          "controls (not a hardness invariant or field theorem)", flush=True)
