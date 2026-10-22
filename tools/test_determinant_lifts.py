"""Exact adversarial controls for the finite lift experiment."""
import math
import unittest
from itertools import product

from flint import ctx, fmpz_mat

from determinant_lifts import (
    analyze, ellipse_points, pair_partition, principal_product,
    smith_layers, valuation,
)
from verify_exact import gram, square


class LiftControls(unittest.TestCase):
    def test_nested_layers_not_independent(self):
        factors = [1, 3, 27, 81]
        layers = smith_layers(factors, 3)
        self.assertEqual(layers, [3, 2, 2, 1])
        self.assertEqual(sum(layers), valuation(math.prod(factors), 3))
        self.assertNotEqual(sum(k * c for k, c in enumerate(layers, 1)),
                            valuation(math.prod(factors), 3))
        self.assertEqual(smith_layers(factors, 5), [])

    def test_zero_and_composite_valuation_rejected(self):
        for n, p in ((0, 3), (12, 4), (12, 1)):
            with self.assertRaises(ValueError):
                valuation(n, p)
        with self.assertRaises(ValueError):
            smith_layers([1, 0], 3)

    def test_layers_against_modular_kernels(self):
        G = [[6, 3], [3, 6]]
        smith = fmpz_mat(G).snf()
        factors = [abs(int(smith[i, i])) for i in range(2)]
        layers = smith_layers(factors, 3)
        previous = 1
        for k in range(1, 4):
            modulus = 3 ** k
            kernel = sum(all(sum(a * b for a, b in zip(row, vector)) % modulus == 0
                             for row in G)
                         for vector in product(range(modulus), repeat=2))
            increment = layers[k - 1] if k <= len(layers) else 0
            self.assertEqual(kernel, previous * 3 ** increment)
            previous = kernel

    def test_correlations_and_upper_bound_mutation(self):
        G = [[10, 9, 0], [9, 10, 0], [0, 0, 2]]
        blocks = pair_partition(G)
        bound = principal_product(G, blocks)
        diagonal = math.prod(G[i][i] for i in range(3))
        d = int(fmpz_mat(G).det())
        self.assertEqual(d, 38)
        self.assertEqual(bound, d)
        self.assertLess(bound, diagonal)
        # A proposed extra factor of two saving is false, even in this example.
        self.assertGreater(d, bound // 2)
        self.assertEqual(principal_product(G, [(0,), (1,), (2,)]), diagonal)

    def test_block_partitions_reject_double_counting(self):
        G = [[2, 1, 0], [1, 2, 0], [0, 0, 2]]
        for blocks in ([(0, 1), (1, 2)], [(0,)], [(0, 1, 2)], [(), (0, 1), (2,)]):
            with self.assertRaises(ValueError):
                principal_product(G, blocks)

    def test_exact_ellipse(self):
        for D in (7, 19, 163):
            points = ellipse_points(D)
            direct = [(x, y) for y in range(-3, 4) for x in range(-30, 31)
                      if 4 * (x * x + D * y * y) <= 9 * D]
            self.assertEqual(points, direct)

    def test_singular_is_not_an_infinite_valuation(self):
        result = analyze(7, square(2), 9, 3, 1)
        self.assertLess(result["rank"], result["rows"])
        self.assertNotIn("prime_layers", result)
        self.assertFalse(result["independence_sufficient"])

    def test_sufficient_is_not_necessary(self):
        result = analyze(7, square(3), 4, 2, 2)
        self.assertEqual(result["status"], "positive")
        self.assertFalse(result["independence_sufficient"])

    def test_derivative_saturation(self):
        points = square(3)
        self.assertEqual(gram(points, 4, 2, 4, 7), gram(points, 4, 2, 5, 7))

    def test_known_fields_and_valuation_mutation(self):
        for D in (7, 19, 43, 67, 163):
            result = analyze(D, ellipse_points(D), 6, 2, 20)
            self.assertEqual(result["status"], "positive")
            self.assertTrue(result["prime_layers"])
            self.assertTrue(all(p["p"] != 2 for p in result["prime_layers"]))
            for prime in result["prime_layers"]:
                self.assertGreaterEqual(prime["valuation"], prime["green"])
                # Measured valuation is exact: one extra unit is already false.
                self.assertLess(sum(prime["layers"]), prime["valuation"] + 1)

    def test_strengthened_green_bound_is_false(self):
        result = analyze(19, ellipse_points(19), 4, 2, 16)
        self.assertEqual(result["status"], "positive")
        self.assertTrue(result["independence_sufficient"])
        self.assertTrue(result["strict_cutoff"])
        for prime in result["prime_layers"]:
            self.assertEqual(prime["valuation"], prime["green"])
            self.assertLess(prime["valuation"], prime["green"] + 2)

    def test_invalid_inputs(self):
        for points, R, S, J in (([], 2, 2, 2), ([(0, 0)] * 2, 2, 2, 2),
                                (square(2), 0, 2, 2), (square(2), 2, 2, 0)):
            with self.assertRaises(ValueError):
                analyze(7, points, R, S, J)


if __name__ == "__main__":
    ctx.prec = 160
    unittest.main()
