#!/usr/bin/env python3
"""Phase311-B: staged DVR radical algebra and original-source factorization tests."""
import sys
import unittest
from pathlib import Path

import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import secondary_trace_radical as m


class SecondaryTraceRadicalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g,cls.source=m.original_primitive_factorization()

    def test_original_same_source_and_10000_Gram_cells_factorized(self):
        self.assertEqual(self.source["unchanged_original_source_shape"],[100,1052])
        self.assertEqual(self.source["exact_divided_rows"],50)
        self.assertEqual(self.source["original_and_primitive_Gram_100x100_factorization_cells_checked"],10000)

    def test_three_radical_stages_and_exact_primitive_val38(self):
        c=m.staged_trace_radical(self.g,5,3)
        self.assertEqual(c["levels_residual_dimensions"],[100,37,1])
        self.assertEqual(c["levels_unit_ranks"],[63,36,1])
        self.assertEqual(c["smith_exponent_histogram"],{0:63,1:36,2:1})
        self.assertEqual(c["exact_det_valuation_if_all_resolved"],38)
        self.assertEqual(c["censored_factors_at_depth"],0)

    def test_independent_rectangular_dvr_smith_agrees_exactly(self):
        from split_dvr_smith import rectangular_smith_dvr
        c=rectangular_smith_dvr(self.g,5,3)
        self.assertEqual(c["resolved_histogram"],{0:63,1:36,2:1})
        self.assertEqual(c["censored_at_or_above_precision"],0)
        self.assertEqual(c["exact_valuation_sum_if_uncensored"],38)

    def test_invertible_source_changes_preserve_all_graded_ranks(self):
        a=m.staged_trace_radical(self.g,5,3)
        b=m.staged_trace_radical(m.unitriangular_congruence(self.g),5,3)
        self.assertEqual(a["levels_unit_ranks"],b["levels_unit_ranks"])
        self.assertEqual(a["smith_exponent_histogram"],b["smith_exponent_histogram"])

    def test_offdiagonal_unit_form_not_a_false_p_radical(self):
        c=m.staged_trace_radical(np.array([[0,1],[1,0]]),5,3)
        self.assertEqual(c["smith_exponent_histogram"],{0:2})
        self.assertTrue(c["unit_offdiagonal_shears_by_level"][0])

    def test_actual_censored_example_is_not_claimed_exact(self):
        c=m.staged_trace_radical(np.diag([1,5,125]).astype(np.int64),5,3)
        self.assertEqual(c["smith_exponent_histogram"],{0:1,1:1})
        self.assertEqual(c["censored_factors_at_depth"],1)
        self.assertIsNone(c["exact_det_valuation_if_all_resolved"])

    def test_expected_original_v5_138_by_exact_nonoverlap_only(self):
        c=m.certificate()
        self.assertEqual(c["primitive_exact_determinant_v5"],38)
        self.assertEqual(c["original_exact_determinant_v5"],138)
        self.assertEqual(c["first_level_lower_bound137_vs_exact138"],[137,138])
        self.assertTrue(c["no_overlap_with_valuationWeight45_asserted"])
        self.assertTrue(c["not_actual_cohomological_Bockstein"])


if __name__=="__main__":
    unittest.main(verbosity=2)
