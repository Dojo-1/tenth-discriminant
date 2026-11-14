#!/usr/bin/env python3
"""Phase314-A: test every original Gram coefficient wild class and J³ blindness."""
from pathlib import Path
import sys
import unittest
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import wild_quadratic_gram as m
from inert_trace_radicals import rank_f5


class WildSecondJetGramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={x["D"]:x for x in m.full_original_certificates()}

    def test_all_300_signed_ray_and_25_nonunit_gram_values_not_just_samples(self):
        for D,expected in ((203,100),(163,40)):
            a=self.data[D]
            self.assertEqual(a["source_rows"],expected)
            self.assertEqual(a["full_signed_unit_ray_classes_checked"],300)
            self.assertEqual(a["first_nonunit_lift_classes_checked"],25)
            self.assertEqual(a["exact_direct_unit_Gram_matrix_cells_checked"],
                             300*expected*expected)
            self.assertEqual(a["exact_direct_nonunit_Gram_matrix_cells_checked"],
                             25*expected*expected)
            self.assertEqual(a["total_second_jet_features_at_most"],78)

    def test_full_original_primitive_Gram_and_rank_unchanged(self):
        for D,(points,entries,rank) in {
            203:(263,10000,63),
            163:(109,1600,23)
        }.items():
            a=self.data[D]
            self.assertEqual(a["full_actual_original_Q"],points)
            self.assertEqual(a["same_original_primitive_Gram_cells_preserved"],entries)
            self.assertEqual(a["same_original_primitive_Gram_rank_F5"],rank)
            self.assertTrue(a["independent_original_source_Gram_matches"])

    def test_all_cubic_finite_differences_zero_but_second_order_visible(self):
        for D in (203,163):
            a=self.data[D]
            # 12 tame classes *25 wild starts*4 symmetrized triples
            # plus nonunit 25*4 triples.
            self.assertEqual(a["all_third_difference_Gram_matrices_zero"],
                             12*25*4+25*4)
            self.assertIsNotNone(a["second_augmentation_layer_nonzero"])
            self.assertIn(a["second_augmentation_layer_nonzero"][
                "nonzero_second_difference"],(1,2,3,4))

    def test_explicit_distinct_nonnegative_histograms_same_J_cubed_image(self):
        for D in (203,163):
            c=self.data[D]["abstract_J_cube_null_counterworld"]
            self.assertEqual(c["abstract_nonnegative_histogram_A"],[3,3,3,3])
            self.assertEqual(c["abstract_nonnegative_histogram_B"],[2,6,0,4])
            self.assertTrue(c["same_z0_z1_z2_wild_moments"])
            self.assertTrue(c["same_original_primitive_Gram_mod5"])
            self.assertTrue(c["not_claimed_as_real_number_field_ray_counts"])

    def test_six_quadratic_moments_independent_on_all_wild_points(self):
        A=np.asarray([m.monomials(w) for w in m.WILD],dtype=np.int64)
        self.assertEqual(A.shape,(25,6))
        self.assertEqual(rank_f5(A),6)
        self.assertEqual(m.monomials((0,0)),(1,0,0,0,0,0))

    def test_quadratic_moment_contributions_not_fourier_character_recovery(self):
        for D in (203,163):
            x=self.data[D]
            self.assertEqual(x["full_wild_group_algebra_dimension"],25)
            self.assertEqual(
                x["quotient_F5_C5_squared_by_J_cubed_dimension"],6)
            self.assertTrue(x["no_higher_5adic_valuation_from_mod5_compression"])


if __name__=="__main__":
    unittest.main(verbosity=2)
