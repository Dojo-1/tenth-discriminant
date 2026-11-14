#!/usr/bin/env python3
"""Phase314 held-out rho60 genuine nontrivial 900-ray h1 stress tests."""
import unittest
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import heldout_global_ray as h


class HeldoutGlobalRayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.positive=[h.h1_heldout(D) for D in (43,163)]
        cls.negative=h.nonh1_counterworld()

    def test_two_h1_fields_all_prime_to10_ideal_shells_not_vacuous(self):
        for a in self.positive:
            self.assertEqual(a["class_number_from_independent_reduced_forms"],1)
            self.assertEqual(a["heldout_rho"],60)
            self.assertEqual(a["all_ideal_total_shell_checks"],1440)
            self.assertGreater(a["actual_prime_to10_principal_ideals"],100)
            self.assertTrue(a["native_field_theorem_source_not_substituted"])

    def test_nonidentity_convolution_more_than_earlier_four_pairs(self):
        for a in self.positive:
            self.assertGreater(a["nontrivial_nonidentity_coprime_ideal_shell_products"],4)
            self.assertGreater(a["full_ray_distribution_nonzero_cells_compared"],4)
            self.assertEqual(a["full_900_ray_class_cap"],900)
            self.assertEqual(a["closed_second_jet_cap"],216)
            self.assertTrue(a["no_new_field_Gram_or_cutoff_claim"])

    def test_inert2_and5_nonh1_D187_real_ideal_class_cancellation(self):
        d=self.negative
        self.assertEqual(d["D"],187)
        self.assertGreater(d["class_number_from_independent_reduced_forms"],1)
        self.assertEqual(d["nonprincipal_ramified_ideal_factor_norms"],[11,17])
        self.assertEqual(d["both_principal_counts_at_norm11_and_norm17"],0)
        self.assertGreater(d["principal_count_at_product_norm187"],0)
        self.assertTrue(d["principal_only_convolution_fails_despite_same_local_ray_group"])
        self.assertTrue(d["same_inert2_and5_local_group_C3_x_C12_x_C5_squared"])

    def test_wrong_local_residue_ideals_rejected(self):
        with self.assertRaises(ValueError):
            h.ray50_tag(163,(5,0))
        with self.assertRaises(ValueError):
            h.ray50_tag(163,(2,0))
        with self.assertRaises(ValueError):
            h.ray50_tag(163,(0,0))


if __name__=="__main__":
    unittest.main(verbosity=2)
