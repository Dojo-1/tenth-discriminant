#!/usr/bin/env python3
"""Phase313-E: depth-six exact original h1 D163 Smith hostile controls."""
import unittest
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import d163_deep_smith as m
from secondary_trace_radical import staged_trace_radical


class D163ExactDepthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=m.exact_D163_smith_certificate()

    def test_unmodified_original_integer_source_and_exact_row_factorization(self):
        c=self.data["source"]
        self.assertEqual(c["D"],163)
        self.assertEqual(c["original_native_rho_R_S_J"],[21,40,1,1])
        self.assertEqual(c["original_integer_Q"],109)
        self.assertEqual(c["original_integer_E_mod5pow7_shape"],[40,218])
        self.assertEqual(c["same_original_1600_Gram_factorization_cells_verified"],1600)
        self.assertEqual(c["exact_divided_rows"],15)
        self.assertTrue(c["original_nonsingular_from_43_integer_points"])

    def test_precise_primitive_rank_and_residual_floor(self):
        c=self.data
        self.assertEqual(c["staged_primitive_unit_ranks"][0],23)
        self.assertEqual(c["staged_primitive_residual_dimensions"][:2],[40,17])
        self.assertGreaterEqual(c["primitive_determinant_v5_lower_bound"],17)
        self.assertGreaterEqual(c["same_original_determinant_v5_lower_bound"],47)
        self.assertTrue(c["independent_rectangular_DVR_Smith_matches"])

    def test_exact_if_and_only_if_no_censored_factors(self):
        c=self.data
        if c["censored_factors_at_or_above_depth6"]==0:
            self.assertIsInstance(c["same_original_exact_v5_if_uncensored"],int)
            self.assertEqual(c["same_original_exact_v5_if_uncensored"],
                             c["same_original_determinant_v5_lower_bound"])
        else:
            self.assertIsNone(c["same_original_exact_v5_if_uncensored"])
        self.assertTrue(c["no_large_field_bound_improvement"])

    def test_zero_block_never_gets_fabricated_exact_determinant(self):
        c=staged_trace_radical(np.zeros((2,2),dtype=np.int64),5,6)
        self.assertEqual(c["censored_factors_at_depth"],2)
        self.assertIsNone(c["exact_det_valuation_if_all_resolved"])


if __name__=="__main__":
    unittest.main(verbosity=2)
