#!/usr/bin/env python3
"""Phase315: exact global conductor250 to ORIGINAL D163 Gram modulo25."""
import unittest
import sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import conductor250_original_mod25 as o

class Conductor250OriginalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=o.full_original_mod25_certificate()

    def test_original_109_integer_source_and_precise_mod25_oracle(self):
        c=self.data
        s=c["original_integer_source"]
        self.assertEqual(s["unchanged_original_integer_source_Q"],109)
        self.assertEqual(s["unchanged_original_source_rows"],40)
        self.assertEqual(s["original_primitive_source_coordinates_verified"],8720)
        self.assertEqual(s["original_primitive_Gram_cells_directly_verified"],1600)
        self.assertEqual(s["source_exact_divided_rows"],15)
        self.assertEqual(s["original_primitive_modulus"],25)
        self.assertTrue(s["not_the_maximal_order_source"])

    def test_full_h1_global_signed_22500_class_transport_first(self):
        c=self.data
        self.assertEqual(c["global_maximal_order_Q"],225)
        self.assertEqual(c["full_signed_ray125_unit_classes"],7500)
        self.assertEqual(c["full_signed_ray250_unit_class_capacity"],22500)
        self.assertEqual(c["all_prime_to10_norm_shell_total_ideal_checks"],177)
        self.assertEqual(c["full_22500_class_conductor250_coprime_products_checked"],270)

    def test_original_suborder_conductor2_gate_after_global_convolution(self):
        c=self.data
        self.assertEqual(c["original_odd_norm_selected_unit_ideals"],26)
        self.assertEqual(c["original_even_norm_selected_unit_ideals"],24)
        self.assertEqual(c["original_unit_ray125_principal_ideals"],50)
        self.assertEqual(c["original_nonunit_first_lift_observations"],9)
        self.assertEqual(c["same_ORIGINAL_Gram_mod25_entries_direct_and_local_and_global"],1600)
        self.assertEqual(c["same_ORIGINAL_Gram_mod5_rank"],23)

    def test_first_level_wild_class_does_not_capture_second_Gram_digit(self):
        x=self.data["strict_collision_first_digit_vs_second_digit"]
        self.assertTrue(x["same_first_level_ray_tag"])
        self.assertTrue(x["different_second_digit_wild_log"])
        self.assertTrue(x["same_signed_primitive_Gram_mod5"])
        self.assertTrue(x["different_signed_primitive_Gram_mod25"])
        self.assertIn(x["first_Gram_difference_mod25"],(5,10,15,20))
        self.assertTrue(x["NOT_claimed_two_actual_elements_of_original_norm_ball"])

    def test_same_original_direct_Gram_mod25_is_nontrivial(self):
        Q,Omega,G,c=o.original_integer_source_oracle()
        self.assertEqual(G.shape,(40,40))
        self.assertEqual(len(Omega),109)
        self.assertTrue(np.array_equal(G,G.T))
        self.assertTrue(np.any(G%25))
        self.assertEqual(int(o.rank_f5(G%5)),23)
        self.assertTrue(self.data["does_NOT_upgrade_exact_v5_77_or_bound_322pow4"])

if __name__=="__main__":
    unittest.main(verbosity=2)
