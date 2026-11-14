#!/usr/bin/env python3
"""Adversarial tests for Phase321-B ray group invariant factors."""
import unittest

from ray_invariant_factors import run_phase321b


class Phase321BRayInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = run_phase321b()
        cls.groups = {x["D"]: x for x in cls.data["invariant_factor_results"]}
        cls.sections = {x["D"]: x for x in cls.data["cyclic_section_tests"]}

    def test_exact_invariant_factors(self):
        self.assertEqual(self.groups[163]["invariant_factors"], (25, 300))
        self.assertEqual(self.groups[187]["invariant_factors"], (25, 600))
        self.assertEqual(self.groups[203]["invariant_factors"], (25, 1200))

    def test_exact_group_orders_and_exponents(self):
        expected = {163: (7500, 300), 187: (15000, 600), 203: (30000, 1200)}
        for D, (order, exponent) in expected.items():
            row = self.groups[D]
            self.assertEqual(row["ray_group_order"], order)
            self.assertEqual(row["group_exponent"], exponent)
            self.assertTrue(row["group_exponent_checked_on_every_element"])
            self.assertEqual(row["invariant_factors"][-1], exponent)

    def test_complete_p_primary_torsion_counts(self):
        expected = {
            163: {2: (1, 2, 4), 3: (1, 3), 5: (1, 25, 625, 625, 625)},
            187: {2: (1, 2, 4, 8), 3: (1, 3), 5: (1, 25, 625, 625, 625)},
            203: {2: (1, 2, 4, 8, 16), 3: (1, 3), 5: (1, 25, 625, 625, 625)}
        }
        for D, p_rows in expected.items():
            for p, counts in p_rows.items():
                self.assertEqual(self.groups[D]["p_primary"][p]["torsion_counts"], counts)

    def test_exact_sequence_extension_splitting(self):
        self.assertTrue(self.sections[163]["splits"])
        self.assertEqual(self.sections[163]["canonical_lift_order"], 1)
        for D, lift_order in ((187, 8), (203, 16)):
            self.assertFalse(self.sections[D]["splits"])
            self.assertEqual(self.sections[D]["section_lift_count"], 0)
            self.assertTrue(self.sections[D]["all_7500_local_lifts_exhausted"])
            self.assertEqual(self.sections[D]["canonical_lift_order"], lift_order)
            self.assertEqual(self.sections[D]["local_obstruction_order"], 4)
            self.assertTrue(self.groups[D]["ray_extension_is_nonsplit"])

    def test_actual_group_differs_from_split_direct_product(self):
        self.assertEqual(self.groups[163]["split_direct_product_invariant_factors"],
                         (25, 300))
        self.assertEqual(self.groups[187]["split_direct_product_invariant_factors"],
                         (50, 300))
        self.assertEqual(self.groups[203]["split_direct_product_invariant_factors"],
                         (100, 300))
        self.assertTrue(self.groups[187]["ray_invariant_factors_differ_from_split_product"])
        self.assertTrue(self.groups[203]["ray_invariant_factors_differ_from_split_product"])

    def test_primary_orders_reconstruct_the_full_group(self):
        for D, row in self.groups.items():
            primary_order = 1
            for p, data in row["p_primary"].items():
                primary_order *= data["p_primary_order"]
            self.assertEqual(primary_order, row["ray_group_order"])

    def test_invariant_factor_divisibility(self):
        for row in self.groups.values():
            factors = row["invariant_factors"]
            self.assertTrue(all(factors[i + 1] % factors[i] == 0
                                for i in range(len(factors) - 1)))

    def test_exponent_witnesses_exist(self):
        for row in self.groups.values():
            self.assertEqual(set(row["exponent_witnesses"]),
                             set(row["prime_factorization"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
