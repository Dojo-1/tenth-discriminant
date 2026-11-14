#!/usr/bin/env python3
"""Phase318-E: synthetic resonance cannot pass exact native norm fibres."""
import unittest
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import exact_resonant_fibres as f


class ResonantRealizationFibreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=f.exact_resonant_global_fibre_certificate()
        cls.byprime={x["split_prime"]:x for x in
                     cls.data["first_original_norm_fibres_for_3_characters"]}

    def test_exact_original_norm_fibres_at_164_212_227_all_four_solutions(self):
        expected={41:(164,1),53:(212,7),227:(227,8)}
        for p,(n,a) in expected.items():
            x=self.byprime[p]
            self.assertEqual(x["first_changed_original_integer_norm_shell"],n)
            self.assertEqual(set(x["exact_integer_fibre_solutions"]),
                             {(s*a,t) for s in (-1,1) for t in (-1,1)})
            self.assertEqual(x["exact_original_signed_norm_fibre_count"],2)
            self.assertEqual(x["synthetic_signed_norm_fibre_count"],2)

    def test_all_synthetic_local_ray_norm_classes_have_no_real_integral_solution(self):
        for p,x in self.byprime.items():
            n=x["first_changed_original_integer_norm_shell"]
            self.assertTrue(
                x["synthetic_tag_support_disjoint_from_actual_exact_norm_fibre"])
            rows=x["synthetic_classes_locally_norm125_and_conductor2_admissible"]
            self.assertEqual(len(rows),2)
            for r in rows:
                self.assertEqual(r["norm_mod125"],n%125)
                self.assertEqual(r["CRT_original_suborder_lift"][0]%2,n%2)
                self.assertEqual(r["CRT_original_suborder_lift"][1]%2,0)
                self.assertFalse(r["globally_integral_exact_norm_generator_exists"])

    def test_whole_original_Gram_changes_concentrated_in_one_exact_norm_fibre(self):
        assert self.data["original_integer_order_Q"]==109
        for p,x in self.byprime.items():
            self.assertTrue(x["all_other_original_norm_shell_spectra_identical"])
            self.assertTrue(x["all_original_Gram_changes_only_from_this_exact_norm_fibre"])
            self.assertEqual(x["same_original_Gram_entries_compared_mod25"],1600)
            self.assertEqual(x["synthetic_changed_primitive_Gram_cells_mod25"],
                             {41:363,53:363,227:250}[p])

    def test_synthetic_Smith_resonance_excluded_by_actual_generator_support(self):
        self.assertEqual(self.byprime[41]["normal_pencil_lambda_mod5"],0)
        self.assertEqual(self.byprime[41]["synthetic_first_two_smith_layers"],[23,7,10])
        for p in (53,227):
            self.assertEqual(self.byprime[p]["normal_pencil_lambda_mod5"],3)
            self.assertEqual(self.byprime[p]["synthetic_first_two_smith_layers"],
                             [23,3,14])
        self.assertTrue(
            self.data["all_synthetic_resonant_rays_fail_exact_global_norm_fibre_test"])
        self.assertTrue(self.data["h2_D187_global_ideal_class_negative_control"])
        self.assertTrue(
            self.data["no_alternate_real_quadratic_field_or_field_uniform_valuation_claim"])

    def test_hostile_different_norm_solutions_excluded(self):
        self.assertEqual(f.exact_integer_norm_fibre(212),
                         ((-7,-1),(-7,1),(7,-1),(7,1)))
        self.assertEqual(f.exact_integer_norm_fibre(227),
                         ((-8,-1),(-8,1),(8,-1),(8,1)))
        self.assertEqual(f.exact_integer_norm_fibre(163),
                         ((0,-1),(0,1)))


if __name__=="__main__":
    unittest.main(verbosity=2)
