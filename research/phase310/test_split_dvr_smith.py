#!/usr/bin/env python3
"""Phase310-B: independent small DVR correctness, censorship and full-source equality."""
import sys
from pathlib import Path
import unittest

import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import split_dvr_smith as s


class SplitDVRSmithTests(unittest.TestCase):
    def test_tiny_known_answer_and_metamorphic_shear(self):
        oracle=s.tiny_known_answer_controls()
        self.assertEqual(oracle["known_diagonal_histogram"],{0:1,1:1,2:1,4:1})
        self.assertTrue(oracle["unimodular_row_column_shear_preserves"])
        self.assertEqual(oracle["zero_matrix_factors_censored"],3)

    def test_mixed_censored_resolved_levels_not_falsely_counted_exact(self):
        modulus=3**6
        sample=np.diag(np.asarray([1,3,3**6],dtype=np.int64))
        profile=s.rectangular_smith_dvr(sample,3,6)
        self.assertEqual(profile["resolved_histogram"],{0:1,1:1})
        self.assertEqual(profile["censored_at_or_above_precision"],1)
        self.assertEqual(profile["lower_bound_valuation_sum"],7)
        self.assertIsNone(profile["exact_valuation_sum_if_uncensored"])

    def test_two_nontrivial_unit_shears_preserve_rectangular_profile(self):
        x=np.asarray([[1,0,0,0],[0,3,0,0],[0,0,9,0]],dtype=np.int64)
        a=s.rectangular_smith_dvr(x,3,6)
        y=x.copy()
        y[0,:]+=7*y[1,:]
        y[2,:]-=2*y[0,:]
        y[:,2]+=5*y[:,1]
        b=s.rectangular_smith_dvr(y,3,6)
        self.assertEqual(a["levels"],b["levels"])
        self.assertEqual(a["resolved_histogram"],{0:1,1:1,2:1})

    def test_hensel_mirror_full_source_equal_smith_profiles(self):
        result=s.actual_D203_split_dvr()
        self.assertEqual(result["K_one_source_and_Gram_rank_F3"],[12,12])
        self.assertEqual(result["local_smith_hist0"],result["local_smith_hist1"])
        self.assertEqual(result["full_original_source_raw_coordinates_checked"],105200)
        self.assertEqual(result["conjugate_local_source_coordinates_checked"],52600)
        self.assertEqual(result["full_original_Gram_cells_checked"],10000)
        self.assertTrue(result["full_original_Q_conjugation_mirror"])
        self.assertTrue(result["not_computed_global_Picard_ideal"])


if __name__=="__main__":
    unittest.main(verbosity=2)
