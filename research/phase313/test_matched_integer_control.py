#!/usr/bin/env python3
"""Phase313-G identical original Q109 h1/nonh1 matched source controls."""
import unittest
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import matched_integer_control as m


class MatchedIntegerControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=m.matched_controls()

    def test_identical_actual_integer_pair_points_under_h1_and_h8(self):
        self.assertEqual(m.integer_Q(163),m.integer_Q(183))
        self.assertEqual(len(m.integer_Q(163)),109)
        self.assertTrue(self.result["identical_actual_original_pair_observation_support"])
        self.assertTrue(self.result["original_Gram_matched_mod5"])

    def test_same_exact_D163_and_D183_original_valuation(self):
        c=self.result
        a=c["h1_D163"]
        b=c["h8_D183"]
        self.assertEqual(a["h_by_standard_reduced_forms"],1)
        self.assertEqual(b["h_by_standard_reduced_forms"],8)
        self.assertEqual(a["exact_full_determinant_v5"],77)
        self.assertEqual(b["exact_full_determinant_v5"],77)
        self.assertEqual(a["exact_parity_block_v5"],[37,40])
        self.assertEqual(b["exact_parity_block_v5"],[37,40])
        self.assertTrue(c["same_exact_v5_measured_not_assumed_before_protocol"])

    def test_source_exact_divisions_and_matched_primitive_profiles(self):
        c=self.result
        for arm in (c["h1_D163"],c["h8_D183"]):
            self.assertEqual(arm["source_exact_5_divisions"],15)
            self.assertEqual(arm["matched_not_native_R_S_J"],[40,1,1])
            self.assertGreater(arm["primitive_Gram_rank_F5"],0)
            self.assertTrue(arm["not_class_number_one_diagnostic"])
        self.assertTrue(c["no_uniform_h1_rank_or_val_inference"])

    def test_field_mod5_identification_not_automatic_higher_lift(self):
        # Source p5 field algebra is the same, but the field discriminant
        # coefficient differs at p5^2 (163 vs183). Do not infer that
        # the higher primitive moments must be equal from mod5 alone.
        self.assertEqual(163%5,183%5)
        self.assertNotEqual(163%25,183%25)
        self.assertTrue(self.result["matched_fields_have_different_global_class_number"])


if __name__=="__main__":
    unittest.main(verbosity=2)
