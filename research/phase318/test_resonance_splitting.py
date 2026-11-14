#!/usr/bin/env python3
"""Phase318-D: exact simultaneous rank 3+4+10 resonance splitting."""
from pathlib import Path
import sys
import unittest
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import resonance_splitting as r


class ResonanceSplitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=r.resonance_common_splitting()

    def test_rank_additive_hypotheses_and_common_radical(self):
        x=self.data
        self.assertEqual(x["same_native_original_integer_order_Q"],109)
        self.assertEqual(x["same_native_original_Gram_mod5_radical_dim"],17)
        self.assertEqual(x["rank_B_original"],7)
        self.assertEqual(x["rank_B_resonant_lambda3"],3)
        self.assertEqual(x["rank_N"],4)
        self.assertTrue(x["rank_sum_exactly_additive"])
        self.assertEqual(x["common_kernel_dimension"],10)

    def test_exact_17d_invertible_simultaneous_block_splitting(self):
        x=self.data
        self.assertEqual(x["simultaneous_split_basis_dimensions"],[3,4,10])
        self.assertEqual(x["nondegenerate_complement_dimensions"],[3,4])
        self.assertTrue(x["common_GL17_F5_basis_invertible"])
        self.assertTrue(all(v in (1,2,3,4) for v in
                             x["nondegenerate_block_determinants_mod5"]))
        self.assertTrue(x["all_289_block_entries_verified_per_lambda"])

    def test_quartic_minor_exactly_explains_single_resonance(self):
        rows=self.data["exact_5_lambda_split_and_quartic_minors"]
        self.assertEqual(len(rows),5)
        self.assertEqual([a["exact_split_rank"] for a in rows],[7,7,7,3,7])
        self.assertEqual(
            [a["old_fixed_original_7x7_minor_determinant"] for a in rows],
            [4,4,4,0,4])
        c=self.data["nonzero_quartic_block_minor_leading_constant_mod5"]
        for row in rows:
            lam=row["lambda"]
            self.assertEqual(row["upper_7x7_block_determinant"],
                             c*pow((lam-3)%5,4,5)%5)
            self.assertTrue(row["all_289_entries_of_split_pencil_verified"])

    def test_hostile_overlapping_image_operators_rejected(self):
        self.assertTrue(self.data["noncomplementary_symmetric_pair_hostile_rejected"])
        hostile=np.asarray([[1,0],[0,0]],dtype=np.int64)
        with self.assertRaises(ValueError):
            r.require_rank_additive(hostile,hostile,(2*hostile)%5)

    def test_no_field_uniform_val_promotion(self):
        self.assertTrue(self.data["no_universal_class_number_or_full_valuation_claim"])


if __name__=="__main__":
    unittest.main(verbosity=2)
