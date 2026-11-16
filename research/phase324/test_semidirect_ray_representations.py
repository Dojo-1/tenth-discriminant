#!/usr/bin/env python3
"""Phase324 adversarial exact tests: ray characters and representations.

The heavy D163/D187/D203 group contexts are each reconstructed once,
not via the full six-million-entry Phase322 evaluation matrix.
"""
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase321"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase322"))
from ideal_aware_ray_class import (  # noqa: E402
    conjugate,
    local_mul,
    local_unit_representatives,
    norm_mod,
)
from exact_ray_characters import canonical_signed_mod  # noqa: E402
from semidirect_ray_representations import (  # noqa: E402
    coord_add,
    run_field,
)


def sparse_projector(f, kernel, n1, n2):
    """Exact subgroup averaging on the regular representation."""
    out = defaultdict(Fraction)
    m = len(kernel)
    assert m
    for g, a in f.items():
        for k in kernel:
            out[coord_add(g, k, n1, n2)] += a / m
    return {g: a for g, a in out.items() if a}


def sub_vectors(x, y):
    out = defaultdict(Fraction)
    for g, a in x.items():
        out[g] += a
    for g, a in y.items():
        out[g] -= a
    return {g: a for g, a in out.items() if a}


class Phase324ToyProjectors(unittest.TestCase):
    def test_orthogonal_idempotent_conductor_shells_over_Q(self):
        n1, n2 = 4, 6
        kernels = [
            [(a, b) for a in range(4) for b in range(6)],
            [(0, b) for b in range(6)],
            [(0, 0), (0, 3)],
            [(0, 0)],
        ]
        f = {(0, 0): Fraction(1), (1, 2): Fraction(3, 2),
             (2, 4): Fraction(-2, 3)}
        P = lambda k, v: sparse_projector(v, kernels[k], n1, n2)
        for k in range(4):
            self.assertEqual(P(k, P(k, f)), P(k, f))
            for j in range(4):
                self.assertEqual(P(k, P(j, f)), P(min(k, j), f))
        E = [lambda v, k=k:
             sub_vectors(P(k, v), P(k - 1, v) if k else {})
             for k in range(4)]
        for k in range(4):
            self.assertEqual(E[k](E[k](f)), E[k](f))
            for j in range(4):
                if j != k:
                    self.assertEqual(E[k](E[j](f)), {})
        reconstructed = {}
        for op in E:
            reconstructed = sub_vectors(reconstructed,
                                         {g: -v for g, v in op(f).items()})
        self.assertEqual(reconstructed, f)
        self.assertEqual([24 // len(K) for K in kernels], [1, 4, 12, 24])
        self.assertEqual([1, 4 - 1, 12 - 4, 24 - 12], [1, 3, 8, 12])

    def test_fourier_change_is_not_integer_unimodular(self):
        """An integral Fourier matrix cannot be used to invent 2-adic mass.

        H diagonalizes the C2 regular representation but det(H)=-2.
        For original Gram I, the transformed Gram is 2I. Its new factor
        2^2 comes solely from det(H)^2, not from the original determinant.
        """
        H = ((1, 1), (1, -1))
        A = ((1, 0), (0, 1))
        mul = lambda X, Y: tuple(tuple(sum(X[r][k] * Y[k][c]
            for k in range(2)) for c in range(2)) for r in range(2))
        transpose = lambda X: tuple(tuple(X[c][r] for c in range(2))
                                     for r in range(2))
        det = lambda X: X[0][0] * X[1][1] - X[0][1] * X[1][0]
        transformed = mul(mul(H, A), transpose(H))
        self.assertEqual(det(H), -2)
        self.assertEqual(transformed, ((2, 0), (0, 2)))
        self.assertEqual(det(A), 1)
        self.assertEqual(det(transformed), 4)
        self.assertEqual(det(transformed), det(H) ** 2 * det(A))

    def test_concentration_counterexample(self):
        """No lower bound on the principal class from group theory alone."""
        n1, n2 = 4, 6
        mass_on_nonprincipal = {(1, 1): Fraction(100)}
        mass_on_principal = {(0, 0): Fraction(100)}
        self.assertEqual(mass_on_nonprincipal.get((0, 0), 0), 0)
        self.assertEqual(mass_on_principal.get((0, 0), 0), 100)
        self.assertEqual(sum(mass_on_nonprincipal.values()),
                         sum(mass_on_principal.values()))


class Phase324RayRepresentations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = {D: run_field(D) for D in (163, 187, 203)}
        print("PHASE324_EXACT_REPRESENTATION_SUMMARY " + json.dumps({
            str(D): {
                "fixed": row["conjugation_fixed_ray_classes"],
                "irreps_1d": row["one_dimensional_irreducibles"],
                "irreps_2d": row["two_dimensional_irreducibles"],
                "principal_ideal_counts": row["controls"]["principal_prime_ideal_counts"],
                "conductor_shells": row["by_conductor"],
            } for D, row in cls.rows.items()}, sort_keys=True), flush=True)

    def test_exact_group_orders_and_irrep_dimension_squares(self):
        for D, h in ((163, 1), (187, 2), (203, 4)):
            row = self.rows[D]
            self.assertEqual(row["ray_group_order"], 7500 * h)
            self.assertEqual(row["semidirect_group_order"], 15000 * h)
            self.assertEqual(row["sum_of_squares"], 15000 * h)
            self.assertEqual(row["conjugation_fixed_ray_classes"],
                             row["conjugation_fixed_characters"])
            self.assertTrue(row["conjugation_fixed_ray_classes"] > 0)
            self.assertEqual(row["one_dimensional_irreducibles"] % 2, 0)

    def test_D163_non_dihedral_two_dimensional_irreps(self):
        row = self.rows[163]
        self.assertEqual(row["conjugation_fixed_ray_classes"], 100)
        self.assertEqual(row["conjugation_fixed_characters"], 100)
        self.assertEqual(row["one_dimensional_irreducibles"], 200)
        self.assertEqual(row["two_dimensional_irreducibles"], 3700)
        self.assertEqual(row["sum_of_squares"], 15000)
        self.assertEqual(row["controls"]["principal_checks"], 7500)

    def test_conductor_shells_preserved_by_sigma(self):
        for D, h in ((163, 1), (187, 2), (203, 4)):
            shells = self.rows[D]["by_conductor"]
            self.assertEqual([shells[str(m)]["characters"]
                              for m in (1, 5, 25, 125)],
                             [h, 11*h, 288*h, 7200*h])
            for entry in shells.values():
                self.assertEqual(
                    entry["one_dimensional_extensions"] +
                    4*entry["two_dimensional_induced_irreps"],
                    2*entry["characters"])

    def test_catalog_galois_action_is_source_aware(self):
        for D, expected in ((163, 118), (187, 128), (203, 125)):
            row = self.rows[D]
            self.assertEqual(row["controls"]["principal_checks"], 7500)
            self.assertEqual(row["controls"]["prime_ideal_checks"], expected)
            self.assertEqual(row["controls"]["non_inversion_witness"],
                             "rational principal ideal (2)")

    def test_bounded_principal_nonprincipal_separation(self):
        expected = {163: (118, 0), 187: (78, 50), 203: (55, 70)}
        for D, (ordinary_principal, nonprincipal) in expected.items():
            row = self.rows[D]
            counts = row["controls"]["principal_prime_ideal_counts"]
            self.assertEqual(counts["1"], ordinary_principal)
            self.assertEqual(
                row["controls"]["ordinary_nonprincipal_prime_ideal_count"],
                nonprincipal)
            self.assertGreaterEqual(counts["1"], counts["5"])
            self.assertGreaterEqual(counts["5"], counts["25"])
            self.assertGreaterEqual(counts["25"], counts["125"])

    def test_local_conjugate_norm_exact_all_7500_D163_units(self):
        D = 163
        units = local_unit_representatives(D)
        self.assertEqual(len(units), 7500)
        for u in units:
            conjugated = canonical_signed_mod(conjugate(u), 125)
            product = local_mul(u, conjugated, D)
            rational_norm = canonical_signed_mod((norm_mod(u, D, 125), 0), 125)
            self.assertEqual(product, rational_norm)
            self.assertEqual(
                canonical_signed_mod(conjugate(conjugated), 125), u)

    def test_rational_two_fixed_but_not_inverted(self):
        D = 163
        identity = canonical_signed_mod((1, 0), 125)
        two = canonical_signed_mod((2, 0), 125)
        self.assertEqual(canonical_signed_mod(conjugate(two), 125), two)
        g = identity
        order = None
        for n in range(1, 101):
            g = local_mul(g, two, D)
            if g == identity:
                order = n
                break
        self.assertEqual(order, 50)
        self.assertNotEqual(local_mul(two, two, D), identity)


if __name__ == "__main__":
    unittest.main(verbosity=2)
