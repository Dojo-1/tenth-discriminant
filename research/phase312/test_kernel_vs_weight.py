#!/usr/bin/env python3
"""Phase312-D: exact modular jet-kernel and weight-comparison hostile tests."""
import unittest
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import kernel_vs_weight as k


class KernelWeightTests(unittest.TestCase):
    def test_original_full_F25_grid_jets_reconstruct_from_basis(self):
        for R,S,J in ((40,1,1),(50,2,2),(75,3,3)):
            with self.subTest(arm=(R,S,J)):
                c=k.original_residue_jet_oracle(R,S,J)
                self.assertEqual(c["actual_GF25_evaluation_rank"],25*J)
                self.assertEqual(c["modular_source_kernel"],R*S-25*J)
                self.assertEqual(c["pivot_remainder_coordinate_checks"],
                                 c["exact_original_residue_source_field_coordinates_checked"])

    def test_old_weight_formula_closed_and_small_S_thresholds(self):
        self.assertEqual(k.weight(40,1),0)
        self.assertEqual(k.weight(50,2),45)
        self.assertEqual(k.native_comparator(40,1)["first_level_GF25_kernel_h"],15)
        self.assertEqual(k.native_comparator(50,2)["first_level_GF25_kernel_h"],50)
        self.assertEqual(k.native_comparator(50,2)["existing_valuationWeight_formula_w"],45)
        self.assertTrue(k.native_comparator(74,2)["first_level_kernel_exceeds_old_weight"])

    def test_at_S_three_old_weight_strictly_wins(self):
        d=k.native_comparator(75,3)
        self.assertEqual(d["first_level_GF25_kernel_h"],150)
        self.assertEqual(d["existing_valuationWeight_formula_w"],205)
        self.assertFalse(d["first_level_kernel_exceeds_old_weight"])
        self.assertTrue(d["old_weight_meets_or_exceeds_first_level_for_S_ge3"])

    def test_large_native_cases_never_claim_independent_extra_mass(self):
        for S in (3,4,5,6,20,50):
            for R in (25*S,25*S+1,25*S+24):
                with self.subTest(native=(R,S)):
                    d=k.native_comparator(R,S)
                    self.assertLessEqual(d["first_level_GF25_kernel_h"],
                                         d["existing_valuationWeight_formula_w"])
                    self.assertTrue(d["first_level_not_additive_to_old_weight"])

    def test_J_above_five_clamps_active_ordinary_jet_order(self):
        f=k.modulus_polynomial(6)
        self.assertEqual(len(f)-1,125)
        self.assertEqual(f[5],4)
        self.assertEqual(f[125],1)
        self.assertEqual(sum(bool(c) for c in f),2)

    def test_R_short_source_does_not_get_full_rank_imputed(self):
        A,rank=k.quotient_rectangular_matrix(8,1,1)
        self.assertEqual(A.shape,(8,25))
        self.assertEqual(rank,8)
        with self.assertRaises(ValueError):
            k.original_residue_jet_oracle(8,1,1)

    def test_full_crossover_certificate_has_no_uniform_field_bound(self):
        result=k.controls()
        self.assertEqual(len(result["independent_real_F25_original_ordinary_jet_oracles"]),3)
        self.assertTrue(result["for_target_large_S_first_level_kernel_does_not_beat_old_weight"])
        self.assertTrue(result["higher_padic_primitive_remainder_or_ray_class_bound_still_open"])


if __name__=="__main__":
    unittest.main(verbosity=2)
