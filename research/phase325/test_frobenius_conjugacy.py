#!/usr/bin/env python3
"""Phase325 adversarial tests for rational Frobenius conjugacy classes.

The only asserted exact field calculations are at D=163,187,203.
The full inert-prime Frobenius lift is NOT computed.
"""
import unittest

from frobenius_conjugacy import run_field


class FrobeniusConjugacyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = {D: run_field(D) for D in (163, 187, 203)}
        import json
        print("PHASE325_FROBENIUS_SUMMARY",
              json.dumps(cls.rows, sort_keys=True), flush=True)

    def test_group_coset_class_sizes(self):
        expected = {
            163: (7500, 15000, 100, 75),
            187: (15000, 30000, 200, 75),
            203: (30000, 60000, 200, 150),
        }
        for D, (g, h, classes, class_size) in expected.items():
            row = self.rows[D]
            self.assertEqual(row["ray_group_order"], g)
            self.assertEqual(row["rational_extension_order"], h)
            self.assertEqual(row["inert_frobenius_coset_class_count"], classes)
            self.assertEqual(row["each_inert_coset_class_size"], class_size)
            self.assertEqual(classes * class_size, g)

    def test_sq_frob_does_not_determine_full_class(self):
        for D, fibers in ((163, 2), (187, 4), (203, 4)):
            row = self.rows[D]
            self.assertEqual(row["squared_frobenius_norm_image_order"], 50)
            self.assertEqual(row["candidate_classes_per_squared_frobenius"], fibers)
            self.assertGreater(fibers, 1)

    def test_two_inert_and_exact_splitting_degree(self):
        for D, number in ((163, 150), (187, 300), (203, 600)):
            row = self.rows[D]
            self.assertTrue(row["two_is_inert"])
            self.assertEqual(row["two_square_frobenius_order"], 50)
            self.assertEqual(row["two_rational_frobenius_order"], 100)
            self.assertEqual(row["two_residue_degree_in_ray_class_field"], 100)
            self.assertEqual(row["two_number_of_primes_in_ray_class_field"], number)

    def test_split_and_inert_local_artin_character_polynomial_checks(self):
        for D, row in self.rows.items():
            local = row["catalog_local_polynomials"]
            self.assertGreater(local["split_rational_primes"], 0)
            self.assertGreater(local["inert_rational_primes"], 0)
            self.assertGreater(local["exact_local_polynomial_phase_checks"], 0)
            self.assertEqual(local["ramified_rational_primes"], 
                             {163: 1, 187: 2, 203: 2}[D])

    def test_no_claim_of_actual_inert_frobenius_lift_or_global_bound(self):
        for row in self.rows.values():
            self.assertTrue(
                row["bounds"]["do_not_claim_inert_full_frobenius_class_from_its_square"])
            self.assertTrue(row["bounds"]["no_global_euler_product_or_L_values"])
            self.assertTrue(row["bounds"]["no_new_discriminant_bound"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
