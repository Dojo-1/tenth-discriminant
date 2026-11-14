#!/usr/bin/env python3
"""Phase314-G: linear operator rank != rank of its output matrices."""
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import moment_operator_rank as m


class GramOperatorImageRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={D:m.moment_Gram_operator_certificate(D) for D in (203,163)}

    def test_original_symmetrical_source_spaces_not_replaced(self):
        for D,n,Q in ((203,100,263),(163,40,109)):
            a=self.data[D]
            self.assertEqual(a["original_source_rows"],n)
            self.assertEqual(a["actual_original_Q"],Q)
            self.assertEqual(a["full_symmetrical_Gram_coordinate_dim"],n*(n+1)//2)
            self.assertEqual(a["quadratic_second_jet_parameters"],78)
            self.assertEqual(a["raw_signed_300_plus_25_ray_lift_bins"],325)

    def test_exact_linear_map_rank_and_kernel_reconstruction(self):
        for D in (203,163):
            a=self.data[D]
            rank=a["exact_F5_rank_of_moment_to_Gram_LINEAR_MAP"]
            nullity=a["formal_moment_nullity_78_minus_operator_rank"]
            self.assertEqual(rank+nullity,78)
            self.assertGreater(rank,0)
            self.assertGreaterEqual(nullity,0)
            if nullity:
                self.assertIsNotNone(a["explicit_kernel_witness_if_any"])
                self.assertGreater(len(a["explicit_kernel_witness_if_any"]),0)
            else:
                self.assertIsNone(a["explicit_kernel_witness_if_any"])

    def test_actual_Gram_rank_is_not_confused_with_parameter_map_rank(self):
        self.assertEqual(self.data[203]["original_actual_G_matrix_rank_F5"],63)
        self.assertEqual(self.data[163]["original_actual_G_matrix_rank_F5"],23)
        self.assertEqual(self.data[203]["original_actual_Gram_cells_reconstructed_by_operator"],10000)
        self.assertEqual(self.data[163]["original_actual_Gram_cells_reconstructed_by_operator"],1600)
        self.assertTrue(self.data[203]["no_invalid_inference_matrix_rank_le_operator_rank"])
        self.assertTrue(self.data[163]["no_class_one_or_uniform_cutoff_inference"])

    def test_actual_nonunit_sign_symmetry_kills_first_moments_only_on_real_data(self):
        for D in (203,163):
            a=self.data[D]
            self.assertEqual(a["actual_nonunit_sign_odd_moments_x_y_vanish"],[0,0])


if __name__=="__main__":
    unittest.main(verbosity=2)
