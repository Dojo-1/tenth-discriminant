#!/usr/bin/env python3
"""Phase308-B: adversarial principalization and representation-collapse tests."""
import unittest

from adaptive_torsion_family import (
    complete_norm_shell, independent_reduced_forms, principalization_scanner,
    source_family, flattening_adversary, InvalidTransport,
)


class AdaptiveIdealTorsionTests(unittest.TestCase):
    def test_complete_norm_shell_exactness_without_heuristic_bounds(self):
        self.assertIn((-2,7),complete_norm_shell(167,2048))
        self.assertIn((-6,1),complete_norm_shell(203,81))
        self.assertIn((-2,1),complete_norm_shell(187,49))
        self.assertIn((0,1),complete_norm_shell(163,41))
        self.assertEqual(complete_norm_shell(203,3),())

    def test_all_four_local_to_global_principalization_orders(self):
        for d,p,r,k,a in (
          (163,41,0,1,(0,1)),
          (187,7,2,2,(-2,1)),
          (203,3,0,4,(-6,1)),
          (167,2,0,11,(-2,7))
        ):
            with self.subTest(d=d):
                data=principalization_scanner(d,p,r,k)
                self.assertEqual(data["first_principal_power"],k)
                self.assertIn(a,data["principal_generators"])
                self.assertEqual(len(data["full_bounded_depth_ledger"]),k)
                self.assertTrue(all(not x["in_ideal_power"]
                                    for x in data["full_bounded_depth_ledger"][:-1]))
                self.assertTrue(data["full_bounded_depth_ledger"][-1]["in_ideal_power"])

    def test_d167_long_memory_padic_root_and_class11(self):
        data=principalization_scanner(167,2,0,11)
        self.assertEqual(data["full_bounded_depth_ledger"][-1]["hensel_root"],878)
        self.assertEqual(data["first_principal_power"],11)
        with self.assertRaises(InvalidTransport):
            principalization_scanner(167,2,0,10)

    def test_class_number_form_count_cross_control(self):
        for d,h in ((163,1),(187,2),(203,4),(167,11)):
            self.assertEqual(len(independent_reduced_forms(d)),h)

    def test_real_tendril_better_than_naive_scalar_collapse_on_fixed_cases(self):
        result=flattening_adversary()
        self.assertEqual(result["naive_scalar_only_false_positives_D"],[187,203])
        self.assertEqual(result["naive_scalar_only_accuracy_on_this_in_sample_family"],"2/4")
        self.assertEqual(result["structured_named_line_class_accuracy_on_this_in_sample_family"],"4/4")
        self.assertTrue(result["NOT_independent_or_out_of_sample_cognition_benchmark"])
        fields={x["field_D"]:x for x in result["cases"]}
        self.assertTrue(fields[203]["rank100_determinant_trivial"])
        self.assertTrue(fields[187]["rank100_determinant_trivial"])
        self.assertFalse(fields[167]["rank100_determinant_trivial"])

    def test_inert_root_and_wrong_precision_refused(self):
        with self.assertRaises(InvalidTransport):
            principalization_scanner(163,3,0,3)
        with self.assertRaises(InvalidTransport):
            principalization_scanner(203,3,0,0)
        with self.assertRaises(InvalidTransport):
            complete_norm_shell(203,-1)


if __name__=="__main__":
    unittest.main(verbosity=2)
