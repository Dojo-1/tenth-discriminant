#!/usr/bin/env python3
"""Adversarial regression suite for Phase320."""
import unittest

from cross_field_wild_normal import run_cross_field_certificate


class CrossFieldWildNormalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = run_cross_field_certificate()
        cls.arms = {x["name"]: x for x in cls.data["arms"]}

    def test_exact_class_numbers_and_inert_prime(self):
        expected = {163: 1, 187: 2, 203: 4}
        for D, h in expected.items():
            field = self.data["fields"][D]
            self.assertEqual(field["class_number"]["class_number"], h)
            self.assertTrue(field["five_inert"])
            self.assertIn(field["minus_D_mod5"], (2, 3))
            self.assertEqual(field["class_number"]["exact_reduced_form_count"], True)

    def test_phase315_local_unit_group_replays(self):
        for D in (163, 187, 203):
            row = self.data["local_conductor125_unit_group_replays"][D]
            self.assertEqual(row["unit_mod125_count"], 15000)
            self.assertEqual(row["signed_unit_ray125_count"], 7500)
            self.assertEqual(row["p_adic_two_digit_wild_values_per_exact_residue"], 625)
            self.assertGreater(row["twisted_defect_and_corrected_log_product_tests"], 0)

    def test_D163_source_completion_regressions(self):
        old = self.arms["D163-even-legacy-control"]["local_normal"]
        full = self.arms["D163-full-maximal"]["local_normal"]
        self.assertEqual(old["primitive_Gram_rank_mod5"], 23)
        self.assertEqual(old["primitive_radical_dimension"], 17)
        self.assertEqual(old["primitive_first_radical_form_rank_e1"], 7)
        self.assertEqual(old["radical_normal_image_dimension"], 1)
        self.assertEqual(full["primitive_Gram_rank_mod5"], 40)
        self.assertEqual(full["primitive_radical_dimension"], 0)
        self.assertEqual(full["radical_normal_image_dimension"], 0)
        self.assertEqual(
            full["full_symmetric_primitive_Gram_differential_span_rank"], 10
        )

    def test_matched_R40_J1_arms_keep_geometry_fixed(self):
        for name in ("D163-full-maximal", "D187-matched-R40-J1",
                     "D203-matched-R40-J1"):
            arm = self.arms[name]
            self.assertEqual(arm["local_normal"]["R"], 40)
            self.assertEqual(arm["local_normal"]["J"], 1)
            self.assertEqual(arm["norm_cutoff"], 441)
            self.assertEqual(arm["source"]["residue_classes_F25"], 25)

    def test_native_D187_and_D203_geometry(self):
        d187 = self.arms["D187-native-R46-J1"]
        d203 = self.arms["D203-native-R50-J2"]
        self.assertEqual((d187["rho"], d187["local_normal"]["R"],
                          d187["local_normal"]["J"]), (23, 46, 1))
        self.assertEqual((d203["rho"], d203["local_normal"]["R"],
                          d203["local_normal"]["J"]), (24, 50, 2))
        self.assertEqual(d203["local_normal"]["primitive_Gram_rank_mod5"], 63)
        self.assertEqual(d203["local_normal"]["primitive_radical_dimension"], 37)

    def test_all_local_norm_lines_are_complete_and_first_digit_safe(self):
        for arm in self.data["arms"]:
            local = arm["local_normal"]
            self.assertEqual(
                local["all_local_lifts_checked"],
                5 * local["signed_5unit_sites"]
            )
            self.assertTrue(local["all_local_norms_preserved_mod125"])
            self.assertTrue(local["all_first_wild_digits_preserved"])
            self.assertTrue(local["all_local_differentials_symmetric"])
            self.assertTrue(local["all_local_differentials_linear_in_F5_parameter"])
            self.assertTrue(local["no_determinant_valuation_inferred"])

    def test_nontrivial_class_groups_do_not_inherit_D163_global_characters(self):
        boundary = self.data["global_class_group_boundary"]
        self.assertEqual(boundary["D163_class_number"], 1)
        self.assertEqual(boundary["D187_class_number"], 2)
        self.assertEqual(boundary["D203_class_number"], 4)
        self.assertTrue(boundary["D163_global_split_prime_character_family_not_transferred"])
        self.assertTrue(boundary["nonprincipal_ideal_classes_require_ideal_aware_global_ray_model"])
        self.assertTrue(self.data["no_field_uniform_valuation_or_cutoff_claim"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
