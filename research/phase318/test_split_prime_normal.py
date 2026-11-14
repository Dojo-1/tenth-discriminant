#!/usr/bin/env python3
"""Phase318-B: exact principal split-prime characters are not all h1 theorems."""
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import split_prime_normal as s


class SplitPrimeWildNormalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=s.global_split_prime_normal_certificate()

    def test_exact_maximal_order_source_and_split_prime_generator_list(self):
        a=self.data
        self.assertEqual(a["D"],163)
        self.assertEqual(a["original_integer_order_Q"],109)
        self.assertEqual(a["maximal_order_radius21_Q"],225)
        self.assertIn(163,a["ramified_prime_excluded_from_antisymmetric_character"])
        self.assertGreater(a["distinct_split_principal_prime_characters_tested"],1)
        self.assertGreater(a["active_native_original_characters"],1)
        self.assertEqual(a["active_prime_list"][0],41)
        self.assertGreater(a["exact_nonmodular_prime_valuation_multiplication_checks"],1000)

    def test_original_source_normal_map_not_guessed_from_convolution(self):
        a=self.data
        self.assertGreaterEqual(a["normal_image_span_rank_among_active_global_characters"],0)
        self.assertLessEqual(
            a["normal_image_span_rank_among_active_global_characters"],
            a["active_native_original_characters"])
        self.assertTrue(all(x["global_normal_equals_linear_combination_all_local_site_normals"]
                            for x in a["per_character_source_and_radical_records"]))
        self.assertTrue(all(x["signed_wild_log_shift_preserves_norm_mod125"]
                            for x in a["per_character_source_and_radical_records"]))

    def test_original_41_prime_gauge_is_recovered_without_residue_fake_valuation(self):
        a=self.data
        p41=next(x for x in a["per_character_source_and_radical_records"]
                 if x["prime"]==41)
        self.assertEqual(p41["changed_original_Gram_cells_mod25"],363)
        self.assertEqual(p41["normal_restriction_rank"],0)
        self.assertEqual(p41["original_first_two_smith_layers"],[23,7,10])
        self.assertTrue(a["native_41_character_is_tangent_recovered"])

    def test_all_selected_global_conductor250_h1_shell_products(self):
        rows=self.data["replayed_full_250_ray_h1_convolution_selected_characters"]
        self.assertEqual(len(rows),3)
        self.assertEqual(rows[0]["prime"],41)
        for a in rows:
            self.assertEqual(a["all_independent_h1_ideal_norm_shells"],177)
            self.assertEqual(a["full_22500_conductor250_coprime_products"],270)

    def test_global_character_smith_and_first_radical_lift_are_reported_not_assumed(self):
        a=self.data
        primes=set(x["prime"] for x in a["per_character_source_and_radical_records"])
        for p in a["nonzero_radical_normal_global_characters"]:
            self.assertIn(p,primes)
        for p in a["characters_changing_first_two_smith_layers"]:
            self.assertIn(p,primes)
        for row in a["per_character_source_and_radical_records"]:
            self.assertEqual(row["changed_original_Gram_cells_mod5"],0)
            self.assertEqual(row["original_first_two_smith_layers"][0],23)
            self.assertEqual(
                sum(row["original_first_two_smith_layers"]),40)
            self.assertEqual(row["first_radical_form_equal_original"],
                             row["normal_restriction_rank"]==0)
        self.assertTrue(a["all_characters_are_synthetic_not_real_new_field_generators"])
        self.assertTrue(a["no_improvement_to_uniform_discriminant_cutoff"])

    def test_nonprime_wrong_or_zero_division_handled(self):
        p=(0,1)
        self.assertIsNone(s.divide_by_prime_generator((1,0),p))
        self.assertEqual(s.divide_by_prime_generator(p,p),(1,0))
        self.assertEqual(s.split_prime_character((0,1),p),1)
        self.assertEqual(s.split_prime_character((1,-1),p),-1)
        with self.assertRaises(ValueError):
            s.valuation_at_pi((0,0),p)


if __name__=="__main__":
    unittest.main(verbosity=2)
