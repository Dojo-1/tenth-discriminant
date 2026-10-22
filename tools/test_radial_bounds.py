"""Adversarial exact controls for moment identities and the annulus lemma."""
import math
import unittest
from fractions import Fraction

from flint import ctx, fmpz_mat

from determinant_lifts import ellipse_points
from radial_bounds import (
    annulus_points, certify_radial, correlation_ratio_bound, cross,
    diagonal, radial_moments, radial_partition,
)
from verify_exact import gram, square


class RadialControls(unittest.TestCase):
    def test_moment_entries_match_full_gram(self):
        for D in (7, 19):
            for points in (square(3), ellipse_points(D), [(0, 0), (2, 1), (-1, 2)]):
                for R, S, J in ((4, 3, 1), (4, 3, 2), (4, 3, 6)):
                    moments = radial_moments(D, points, R + S - 2)
                    G = gram(points, R, S, J, D)
                    for r in range(R):
                        for s in range(S):
                            i = r * S + s
                            self.assertEqual(diagonal(moments, r, s, J), G[i][i])
                            if r + 1 < R and s + 1 < S:
                                self.assertEqual(cross(moments, r, s, J),
                                                 G[i][(r + 1) * S + s + 1])

    def test_extra_derivative_term_cannot_be_dropped(self):
        moments = radial_moments(7, [(1, 0), (2, 0)], 2)
        self.assertEqual(diagonal(moments, 1, 1, 2),
                         diagonal(moments, 1, 1, 1) + 2 * moments[1])
        self.assertEqual(cross(moments, 0, 0, 2), 2 * moments[1])
        self.assertNotEqual(cross(moments, 0, 0, 2), 2 * moments[0])
        unit = radial_moments(7, [(-1, 0), (1, 0)], 2)
        product = diagonal(unit, 0, 0, 2) * diagonal(unit, 1, 1, 2)
        self.assertGreater(Fraction(product - cross(unit, 0, 0, 2) ** 2, product),
                           Fraction(9, 25))

    def test_partition_is_disjoint_and_safe(self):
        for R, S, J in ((6, 3, 1), (12, 4, 3), (3, 2, 8)):
            pairs, singles = radial_partition(R, S, J)
            rows = [row for pair in pairs for row in pair] + singles
            self.assertEqual(len(rows), R * S)
            self.assertEqual(len(set(rows)), R * S)
            for (r, s), second in pairs:
                self.assertGreaterEqual(r, 2 * (J - 1))
                self.assertEqual(second, (r + 1, s + 1))

    def test_safe_range_and_annulus_are_required(self):
        for a, b, r, J in ((0, 2, 4, 2), (3, 2, 4, 2), (1, 2, 0, 2)):
            with self.assertRaises(ValueError):
                correlation_ratio_bound(a, b, r, J)
        for points in ([(0, 0), (1, 0)], [(1, 0), (3, 0)]):
            with self.assertRaises(ValueError):
                certify_radial(7, points, 4, 2, 2)

    def test_no_certificate_is_not_a_rank_claim(self):
        result = certify_radial(7, [(3, 0), (3, 1)], 40, 2, 1)
        self.assertFalse(result["independence_sufficient"])
        self.assertNotIn("normalized_gaps", result)
        self.assertNotIn("singular", result["status"])

    def test_analytic_ratio_and_strengthening_mutation(self):
        # J=1, r=s=0: two nonzero real points, squared radii 1 and 4.
        points = [(1, 0), (2, 0)]
        moments = radial_moments(7, points, 2)
        product = diagonal(moments, 0, 0, 1) * diagonal(moments, 1, 1, 1)
        minor = product - cross(moments, 0, 0, 1) ** 2
        ratio = Fraction(minor, product)
        self.assertEqual(ratio, Fraction(9, 34))
        self.assertLessEqual(ratio, correlation_ratio_bound(1, 4, 0, 1))
        self.assertGreater(ratio, Fraction(1, 4))
        self.assertEqual(correlation_ratio_bound(1, 2, 2, 2), Fraction(1, 4))
        self.assertLessEqual(correlation_ratio_bound(1, 2, 20, 11), Fraction(9, 25))
        self.assertGreater(correlation_ratio_bound(1, 2, 2, 3), Fraction(9, 25))

    def test_bound_against_small_full_determinants(self):
        for D in (7, 19):
            points = annulus_points(D)
            lines = {}
            for x, y in points:
                lines[y] = lines.get(y, 0) + 1
            J = max(lines.values()) + len(lines)
            # R=4 has no uniform-safe pairs; this also checks the zero-gain path.
            result = certify_radial(D, points, 4, 2, J)
            self.assertTrue(result["independence_sufficient"])
            G = gram(points, 4, 2, J, D)
            self.assertGreater(int(fmpz_mat(G).det()), 0)
            self.assertEqual(result["pairs"], 0)
        # J=1 permits pairs at small R. Direct rank replaces the sufficient test here.
        points, R, S, J, D = [(1, 0), (2, 0), (1, 1), (2, 1)], 3, 2, 1, 7
        G = gram(points, R, S, J, D)
        moments = radial_moments(D, points, R + S - 2)
        pairs, singles = radial_partition(R, S, J)
        product = math.prod(diagonal(moments, r, s, J) for r, s in singles)
        for (r, s), (u, v) in pairs:
            product *= diagonal(moments, r, s, J) * diagonal(moments, u, v, J) - cross(moments, r, s, J) ** 2
        self.assertGreater(int(fmpz_mat(G).det()), 0)
        self.assertLessEqual(int(fmpz_mat(G).det()), product)

    def test_certified_nontrivial_pair_against_full_determinant(self):
        # D=1 is an algebraic control, not a new fundamental-discriminant case.
        D, R, S, J = 1, 40, 2, 20
        points = annulus_points(D)
        result = certify_radial(D, points, R, S, J)
        self.assertTrue(result["independence_sufficient"])
        self.assertGreater(result["pairs"], 0)
        moments = radial_moments(D, points, R + S - 2)
        pairs, singles = radial_partition(R, S, J)
        block = math.prod(diagonal(moments, r, s, J) for r, s in singles)
        for (r, s), (u, v) in pairs:
            block *= diagonal(moments, r, s, J) * diagonal(moments, u, v, J) - cross(moments, r, s, J) ** 2
        determinant = int(fmpz_mat(gram(points, R, S, J, D)).det())
        self.assertGreater(determinant, 0)
        self.assertLessEqual(determinant, block)

    def test_annulus_enumeration(self):
        for D in (7, 19):
            points = annulus_points(D)
            self.assertEqual(len(points), len(set(points)))
            self.assertTrue(all(18 * D <= x * x + D * y * y <= 36 * D for x, y in points))
            self.assertEqual(points, [(x, y) for y in range(-7, 8)
                                     for x in range(-math.isqrt(36 * D), math.isqrt(36 * D) + 1)
                                     if 18 * D <= x * x + D * y * y <= 36 * D])


if __name__ == "__main__":
    ctx.prec = 160
    unittest.main()
