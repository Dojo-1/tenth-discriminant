#!/usr/bin/env python3
"""Phase313-F: third exact-integer determinant and parity block audit."""
import unittest
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import exact_integer_determinant as e


class ExactIntegerDeterminantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=e.independent_integer_determinant_certificate()

    def test_unmodified_109_original_integer_observations_and_40rows(self):
        c=self.cert
        self.assertEqual(c["original_integer_Q"],109)
        self.assertEqual(c["original_integer_Gram_order"],40)
        self.assertTrue(c["true_40x40_unmodified_original_IntegerTraceGram"])
        self.assertTrue(c["all_odd_even_cross_entries_EXACTLY_zero"])

    def test_direct_integer_determinant_matches_77_without_smith(self):
        c=self.cert
        self.assertEqual(c["full_40x40_determinant_exact_v5"],77)
        self.assertEqual(c["full_40x40_determinant_unit_mod5"],2)
        self.assertTrue(c["independent_sympy_domain_ge_det_without_modular_Smith"])

    def test_exact_even_odd_block_valuations_and_units(self):
        c=self.cert
        blocks=c["even_odd_exact_blocks"]
        self.assertEqual([b["block_size"] for b in blocks],[20,20])
        self.assertEqual([b["exact_determinant_v5"] for b in blocks],[37,40])
        self.assertEqual([b["exact_determinant_unit_mod5"] for b in blocks],[4,3])
        self.assertEqual([b["exact_decimal_digit_count"] for b in blocks],[980,1029])

    def test_exact_determinant_and_smith_are_distinct_implementations(self):
        from d163_deep_smith import exact_D163_smith_certificate
        d=exact_D163_smith_certificate()
        c=self.cert
        self.assertEqual(d["same_original_exact_v5_if_uncensored"],
                         c["full_40x40_determinant_exact_v5"])
        self.assertTrue(c["not_a_uniform_class_number_one_field_theorem"])


if __name__=="__main__":
    unittest.main(verbosity=2)
