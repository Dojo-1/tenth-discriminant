#!/usr/bin/env python3
"""Phase308-C: test invariant recovery by filtered categorical Worldlets."""
import unittest

from filtered_picard import (
    PicardFlag,FilterTypeError,standard_flag,repeated_I_flag,
    inverse_tendril_pair,representation_adaptation_control,
)


class FilteredPicardTests(unittest.TestCase):
    def test_rank100_free_but_named_grades_nonprincipal(self):
        for d,m in ((187,2),(203,4)):
            x=repeated_I_flag(d,m,100)
            y=standard_flag(d,m,100)
            self.assertEqual(x.forget_filtration(),y.forget_filtration())
            self.assertTrue(x.underlying_module_free_by_steinitz)
            self.assertFalse(x.filtered_isomorphic_to(y))
            self.assertEqual(x.deweave()["first_nontrivial_grade"],1)
        x=repeated_I_flag(167,11,100)
        self.assertEqual(x.determinant_class,1)
        self.assertFalse(x.underlying_module_free_by_steinitz)

    def test_rank2_inverse_tendrils_cancel_only_after_forgetting(self):
        for d,m in ((187,2),(203,4),(167,11)):
            x=inverse_tendril_pair(d,m)
            y=standard_flag(d,m,2)
            self.assertEqual(x.determinant_class,0)
            self.assertEqual(x.forget_filtration(),y.forget_filtration())
            self.assertTrue(x.underlying_module_free_by_steinitz)
            self.assertFalse(x.filtered_isomorphic_to(y))
            self.assertEqual(x.canonical_grades,(1,m-1))

    def test_principal_control_and_correct_source_types(self):
        x=inverse_tendril_pair(163,1)
        self.assertTrue(x.filtered_isomorphic_to(standard_flag(163,1,2)))
        with self.assertRaises(FilterTypeError):
            x.filtered_isomorphic_to(standard_flag(203,4,2))
        with self.assertRaises(FilterTypeError):
            repeated_I_flag(203,4,0)

    def test_counterexample_for_flattened_classifier_triggers_type_refinement(self):
        result=representation_adaptation_control()
        self.assertEqual(result["scalar_only_false_positive_fields"],[187,203])
        self.assertEqual(len(result["pairwise_I_plus_inverse_cancellation"]),3)
        self.assertTrue(result["representation_refinement_changes_in_sample_false_positive_count"])
        self.assertTrue(result["NOT_a_general_intelligence_benchmark"])


if __name__=="__main__":
    unittest.main(verbosity=2)
