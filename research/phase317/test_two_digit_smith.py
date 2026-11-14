#!/usr/bin/env python3
"""Phase317 hostile: two Smith digits of original vs five synthetic gauges."""
from pathlib import Path
import sys
import unittest
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import two_digit_smith as s


class OriginalGramTwoSmithSlicesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=s.actual_vs_gauge_smith_certificate()

    def test_actual_original_native_source_and_all_five_shifts(self):
        x=self.data
        self.assertEqual(x["D"],163)
        self.assertEqual(x["source_R"],40)
        self.assertEqual(x["source_original_Q"],109)
        self.assertEqual(x["original_primitive_Gram_cells"],1600)
        self.assertEqual(len(x["full_5_point_tracezero_gauge_family"]),5)

    def test_mod5_fixed_and_two_smith_layer_accounting_correct(self):
        for rec in self.data["full_5_point_tracezero_gauge_family"]:
            t=rec["exact_mod25_smith"]
            self.assertEqual(t["e0_unit_smith_factors"],23)
            self.assertEqual(
                t["e0_unit_smith_factors"]+
                t["e1_exactly_one_five"]+
                t["e_at_least_2"],40)
            self.assertEqual(
                t["mod25_kernel_log5_cardinality"],
                t["e1_exactly_one_five"]+2*t["e_at_least_2"])
            self.assertTrue(rec["original_mod5_source_unchanged"])

    def test_363_native_source_changed_cells_and_zero_twist_control(self):
        rows=self.data["full_5_point_tracezero_gauge_family"]
        self.assertEqual(rows[0]["changed_original_Gram_cells_mod25"],0)
        self.assertEqual(rows[1]["changed_original_Gram_cells_mod25"],363)
        self.assertEqual(rows[1]["first_changed_cell_if_any"],(0,26,15))
        self.assertTrue(self.data["exact_norm164_ray_source_premise_checked"])

    def test_independent_known_smith_fixtures_and_unimodular_invariance(self):
        fixtures=self.data["hostile_unit_pivot_permutation_and_shear_controls"]
        self.assertEqual(len(fixtures),7)
        self.assertTrue(all(x["row_col_unimodular_invariance"] for x in fixtures))

    def test_dense_smith_hostile_controls(self):
        unit=np.asarray([[1,3,5],[7,2,4],[5,8,1]],dtype=np.int64)
        base=s.two_smith_slices(unit)
        shear=unit.copy()%25
        shear[1,:]=(shear[1,:]+9*shear[0,:])%25
        shear[:,2]=(shear[:,2]+4*shear[:,1])%25
        perm=shear[np.ix_([2,0,1],[1,2,0])]
        other=s.two_smith_slices(perm)
        for label in ("e0_unit_smith_factors","e1_exactly_one_five","e_at_least_2"):
            self.assertEqual(base[label],other[label])

    def test_no_synthetic_field_or_unproved_full_determinant_inference(self):
        self.assertTrue(self.data["not_a_real_alternative_quadratic_field"])
        self.assertTrue(self.data["not_full_v5_det_or_uniform_valuation_bound"])
        self.assertEqual(self.data["distinct_first_two_smith_profiles_in_gauge_family"]>1,
                         self.data["some_wild_twist_changes_e1_or_ege2"])
        self.assertEqual(self.data["distinct_first_two_smith_profiles_in_gauge_family"]==1,
                         self.data["if_all_profiles_same_record_as_negative"])

    def test_reject_non_square_shapes(self):
        with self.assertRaises(ValueError):
            s.two_smith_slices(np.zeros((3,2),dtype=np.int64))


if __name__=="__main__":
    unittest.main(verbosity=2)
