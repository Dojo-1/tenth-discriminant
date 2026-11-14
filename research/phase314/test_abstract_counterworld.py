#!/usr/bin/env python3
"""Phase314-C hostile: abstract h1-convolution is not a wild Gram bound."""
import unittest
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import abstract_counterworld as x


class AbstractWildCounterworldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=x.abstract_counterworld()

    def test_same_actual_zeroth_shell_counts_but_different_wild_data(self):
        c=self.data
        self.assertEqual(tuple(c["frozen_formal_shell_norms"]),(1,9,49,441))
        self.assertEqual(len(c["two_models"]),2)
        self.assertTrue(c["both_preserve_actual_zeroth_ideal_counts_ON_THE_FOUR_SHELLS"])
        self.assertNotEqual(c["two_models"][0]["norm9_wild"],
                            c["two_models"][1]["norm9_wild"])

    def test_coprime_convolution_internal_to_shell_family_satisfied_in_both(self):
        c=self.data
        for model in c["two_models"]:
            self.assertTrue(model["all_coprime_convolution_relations_internal_to_four_shells"])
        self.assertTrue(c["both_preserve_conductor2_and_tame_residues"])
        self.assertTrue(c["full_coprime_convolution_constraints_for_all_other_shells_NOT_claimed"])

    def test_same_original_Gram_function_can_separate_formal_ray_assignments(self):
        c=self.data
        d=c["different_original_primitive_Gram_entry"]
        self.assertIn(d["difference_mod5"],(1,2,3,4))
        self.assertGreaterEqual(d["row_i"],0)
        self.assertLess(d["row_j"],40)
        self.assertTrue(c["conv_plus_totals_alone_cannot_force_a_wild_Gram_value"])

    def test_not_a_fake_real_number_field_counterexample(self):
        c=self.data
        self.assertTrue(c["alternate_wild_assignments_not_realizable_as_actual_D163_elements"])
        self.assertTrue(c["extra_number_field_residue_reciprocity_constraints_still_required"])
        self.assertTrue(c["does_not_refute_uniform_h1_discriminant_theorem"])


if __name__=="__main__":
    unittest.main(verbosity=2)
