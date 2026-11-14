#!/usr/bin/env python3
"""Adversarial tests for Phase322 exact ray characters and conductors."""
import unittest

from exact_ray_characters import (
    EXPECTED_CONDUCTORS,
    EXPECTED_KERNEL_ORDERS,
    EXPECTED_RAY_ORDERS,
    run_phase322,
)


class Phase322ExactRayCharacterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = run_phase322()
        cls.fields = {row["D"]: row for row in cls.data["fields"]}

    def test_full_character_group_orders_and_invariant_factors(self):
        expected = {
            163: (7500, [25, 300]),
            187: (15000, [50, 300]),
            203: (30000, [100, 300]),
        }
        for D, (order, factors) in expected.items():
            row = self.fields[D]
            self.assertEqual(row["ray_group_order"], order)
            self.assertEqual(row["character_count"], order)
            self.assertEqual(row["ray_invariant_factors"], factors)
            self.assertEqual(row["coordinate_bijection_size"], order)

    def test_local_generators_have_exact_orders_and_full_product(self):
        for D, row in self.fields.items():
            self.assertEqual(row["local_generator_orders"],
                             {"order_25": 25, "order_300": 300})
            h = {163: 1, 187: 2, 203: 4}[D]
            self.assertEqual(row["ray_generator_orders"],
                             {"order_25h": 25 * h, "order_300": 300})
            self.assertEqual(row["coordinate_generator_step_checks"],
                             2 * EXPECTED_RAY_ORDERS[D])
            self.assertEqual(row["coordinate_bijection_size"],
                             EXPECTED_RAY_ORDERS[D])

    def test_reduction_maps_and_conductor_kernels(self):
        expected_local_orders = {"1": 1, "5": 12, "25": 300, "125": 7500}
        for D, row in self.fields.items():
            self.assertEqual(row["local_reduction_orders"], expected_local_orders)
            h = {163: 1, 187: 2, 203: 4}[D]
            self.assertEqual(row["ray_reduction_orders"],
                             {"1": h, "5": h * 12, "25": h * 300, "125": h * 7500})
            self.assertEqual(row["conductor_kernel_orders"],
                             {str(k): v for k, v in EXPECTED_KERNEL_ORDERS.items()})
            self.assertTrue(all(len(gens) <= 2
                                for gens in row["conductor_kernel_generators"].values()))

    def test_exact_character_conductor_distributions(self):
        for D, row in self.fields.items():
            self.assertEqual(row["conductor_counts"],
                             {str(k): v for k, v in EXPECTED_CONDUCTORS[D].items()})
            self.assertEqual(sum(row["conductor_counts"].values()),
                             row["character_count"])

    def test_all_bounded_prime_ideal_character_values_are_hashed(self):
        for D, row in self.fields.items():
            ev = row["character_evaluations"]
            expected_records = {163: 118, 187: 128, 203: 125}[D]
            self.assertEqual(ev["prime_ideal_records"], expected_records)
            self.assertEqual(ev["character_count"], EXPECTED_RAY_ORDERS[D])
            self.assertEqual(ev["character_prime_ideal_evaluations"],
                             EXPECTED_RAY_ORDERS[D] * expected_records)
            self.assertEqual(len(ev["evaluation_matrix_sha256"]), 64)
            self.assertGreater(ev["prime_ideal_relation_checks"], 0)
            self.assertEqual(len(ev["sample_character_values_first_eight_prime_ideals"]), 4)

    def test_phase321_prime_ideal_catalog_controls_are_retained(self):
        expected = {
            163: (34, 1, 0),
            187: (44, 2, 50),
            203: (41, 2, 70)
        }
        for D, row in self.fields.items():
            cat = row["prime_ideal_catalog"]
            split, ramified, nonprincipal = expected[D]
            self.assertEqual(cat["split_rational_primes"], split)
            self.assertEqual(cat["ramified_rational_primes"], ramified)
            self.assertEqual(cat["nonprincipal_prime_ideal_records"], nonprincipal)
            self.assertEqual(len(cat["sha256"]), 64)

    def test_exact_character_values_are_rational_exponents(self):
        for row in self.fields.values():
            samples = row["character_evaluations"]["sample_character_values_first_eight_prime_ideals"]
            self.assertEqual(len(samples), 4)
            for values in samples.values():
                self.assertEqual(len(values), 8)
                for entry in values:
                    num, den = entry["exponent"]
                    self.assertGreaterEqual(num, 0)
                    self.assertGreater(den, 0)
                    self.assertLess(num, den)

    def test_total_character_counts_are_complete(self):
        self.assertEqual(sum(row["character_count"] for row in self.fields.values()),
                         7500 + 15000 + 30000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
