#!/usr/bin/env python3
"""Phase317-C: exact first radical-lift vs gauge-congruence tangent controls."""
import unittest
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import radical_tangent as t


class RadicalFirstLiftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=t.radical_tangent_certificate()

    def test_original_radical_is_17_and_independent_e1_equals_7(self):
        a=self.data
        self.assertEqual(a["original_Q"],109)
        self.assertEqual(a["original_source_Gram_dimension"],40)
        self.assertEqual(a["original_Gram_mod5_rank"],23)
        self.assertEqual(a["original_Gram_mod5_radical_dimension"],17)
        self.assertEqual(a["independent_radical_first_lift_original_rank"],7)
        self.assertEqual(a["independent_Smith_unit_pivot_e1"],7)

    def test_all_five_gauge_perturbations_same_smith_but_tangent_status_measured(self):
        rows=self.data["synthetic_five_gauge_first_lift_profiles"]
        self.assertEqual(len(rows),5)
        self.assertEqual([a["actual_original_Gram_entries_changed_mod25"]
                          for a in rows],[0,363,363,363,363])
        for r in rows:
            self.assertEqual(r["Smith_e0_e1_ege2"],[23,7,10])
            self.assertEqual(r["first_radical_form_rank"],7)
            self.assertEqual(r["radical_dim"],17)
            tangent=r["tangent_result"]["is_tangent_to_mod5_congruence_orbit"]
            self.assertEqual(tangent,
                             r["difference_restricted_to_radical_rank"]==0)
            self.assertEqual(r["first_radical_form_equal_original"],
                             r["difference_restricted_to_radical_rank"]==0)

    def test_positive_I_plus_5X_congruence_has_zero_radical_normal_component(self):
        pos=self.data["positive_explicit_U_equal_I_plus_5X_congruence"]
        self.assertTrue(pos["is_tangent_to_mod5_congruence_orbit"])
        self.assertTrue(pos["independent_solvability_witness"])
        self.assertEqual(pos["radical_restriction_rank"],0)

    def test_deliberate_nontangent_symmetric_radical_deformation_rejected(self):
        neg=self.data["negative_rank_one_radical_non_tangent_control"]
        self.assertFalse(neg["is_tangent_to_mod5_congruence_orbit"])
        self.assertFalse(neg["independent_solvability_witness"])
        self.assertEqual(neg["radical_restriction_rank"],1)

    def test_first_lift_form_independent_of_integral_lift_of_radical_basis(self):
        g=np.asarray([[1,0,0],[0,5,0],[0,0,0]],dtype=np.int64)
        K,_,_=t.kernel_basis_mod5(g%5)
        self.assertEqual(K.shape,(3,2))
        B=t.first_radical_form(g,K)
        lift=K+5*np.asarray([[1,2],[2,3],[4,1]],dtype=np.int64)
        self.assertTrue(np.array_equal(B,t.first_radical_form(g,lift)))
        self.assertEqual(t.rank_f5(B),1)

    def test_tangent_iff_radical_restriction_with_small_hand_checkable_matrix(self):
        g0=np.asarray([[1,0],[0,0]],dtype=np.int64)
        K,_,_=t.kernel_basis_mod5(g0)
        self.assertEqual(K.shape,(2,1))
        Ht=np.asarray([[2,1],[1,0]],dtype=np.int64)
        Hn=np.asarray([[2,1],[1,1]],dtype=np.int64)
        self.assertTrue(t.tangent_witness_or_obstruction(
            g0,Ht,K)["independent_solvability_witness"])
        self.assertFalse(t.tangent_witness_or_obstruction(
            g0,Hn,K)["is_tangent_to_mod5_congruence_orbit"])

    def test_no_novel_field_theorem_from_synthetic_tangency(self):
        self.assertTrue(self.data["no_full_Smith_or_new_determinant_claim"])
        self.assertTrue(self.data["no_real_alternative_quadratic_field"])


if __name__=="__main__":
    unittest.main(verbosity=2)
