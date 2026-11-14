#!/usr/bin/env python3
"""Phase316 adversarial global ideal-character wild gauge controls.

Checks EXACT principal-ideal valuation identities and true local norm125
residue invariance, then compares full 22500-ray h1 convolution and the
same ORIGINAL integer-order Gram mod25 under a synthetic second-depth
trace-zero twist. No claim the modified tags are actual generators.
"""
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import wild_gauge as g

class GlobalWildGaugeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=g.full_gauge_countercertificate()

    def test_norm41_primes_factor_and_valuation_anti_involution(self):
        self.assertEqual(g.integer_mul((0,1),(1,-1)),(41,0))
        self.assertEqual(g.prime_divisibility((0,1)),(1,0))
        self.assertEqual(g.prime_divisibility((1,-1)),(0,1))
        self.assertEqual(g.prime_divisibility((41,0)),(1,1))
        self.assertEqual(g.antisymmetric_valuation((0,1)),1)
        self.assertEqual(g.antisymmetric_valuation((1,-1)),-1)
        self.assertEqual(g.antisymmetric_valuation((41,0)),0)

    def test_all_global_h1_norm_shell_counts_full_250_ray_convolutions(self):
        c=self.data["global_h1_full_signed_ray250_heldout"]
        self.assertEqual(c["radius_heldout_or_native"],60)
        self.assertEqual(c["independently_verified_total_ideal_shells"],1440)
        self.assertEqual(c["full_conductor250_twisted_coprime_convolutions_verified"],59)
        self.assertTrue(c["same_ideal_counts_and_full_convolution_as_actual_h1"])
        self.assertGreater(c["principal_ideals_with_nonzero_41_adic_asymmetry"],0)

    def test_original_native_source_selected_after_conductor2_gate(self):
        c=self.data
        n=c["global_h1_full_signed_ray250_native"]
        self.assertEqual(n["radius_heldout_or_native"],21)
        self.assertEqual(n["full_conductor250_twisted_coprime_convolutions_verified"],270)
        self.assertEqual(c["original_native_integer_source_Q"],109)
        self.assertEqual(c["native_original_Gram_entries_compared"],1600)
        self.assertEqual(c["original_native_primitive_modulus"],25)
        self.assertEqual(c["native_original_G_F5_rank"],23)
        self.assertEqual(c["synthetic_twisted_G_F5_rank"],23)
        self.assertTrue(c["synthetic_vs_actual_Gram_equal_mod5"])

    def test_tracezero_norm125_and_conjugation_via_exact_inverses(self):
        c=self.data
        self.assertTrue(c["shift_reduction_mod5_is_zero"])
        self.assertEqual(tuple(c["trace_zero_depth2_wild_shift"]),(20,10))
        self.assertGreater(c["unit_generator_norm_mod125_and_conjugation_checks"],1000)
        self.assertGreater(c["units_whose_second_wild_log_changed"],0)
        self.assertGreater(c["exact_principal_ideal_valuation_product_tests"],1000)

    def test_zero_twist_identity_and_traceful_twist_hostile(self):
        c=self.data
        self.assertTrue(c["zero_twist_identical_original_ray_and_Gram"])
        self.assertTrue(c["traceful_twist_breaks_norm_mod125_and_conjugation"])
        self.assertTrue(c["synthetic_tags_not_actual_global_principal_generator_rays"])
        self.assertTrue(c["no_uniform_determinant_or_discriminant_bound_inferred"])

    def test_report_not_assume_second_digit_gram_difference(self):
        c=self.data
        if c["synthetic_vs_actual_Gram_changed_mod25"]:
            self.assertGreater(c["changed_mod25_matrix_cells"],0)
            self.assertIn(c["first_changed_original_matrix_cell_if_any"][
                "synthetic_minus_actual_mod25"],(5,10,15,20))
        else:
            self.assertEqual(c["changed_mod25_matrix_cells"],0)
            self.assertIsNone(c["first_changed_original_matrix_cell_if_any"])

if __name__=="__main__":
    unittest.main(verbosity=2)
