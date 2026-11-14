#!/usr/bin/env python3
"""Phase312 class-one versus non-h1 matched-source and ray-class controls."""
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import class_one_ray_controls as c
import fermat_lift as f


class Phase312ClassOneRayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results=c.matched_field_controls()

    def test_same_inert_residue_algebra_has_different_class_numbers(self):
        data=self.results["matched_fields"]
        self.assertEqual([x["D"] for x in data],[43,163,183])
        self.assertEqual([x["class_number_from_standard_reduced_forms"] for x in data],
                         [1,1,8])
        self.assertEqual({x["omega_residue_polynomial_m_mod5"] for x in data},{1})
        self.assertEqual({x["matched_radius_not_native_field_policy"] for x in data},{21})

    def test_finite_local_units_not_ordinary_ray_class_proof(self):
        data=self.results["matched_fields"]
        self.assertEqual([x["local_mod5_unit_count"] for x in data],[24]*3)
        self.assertEqual([x["local_mod25_unit_count"] for x in data],[600]*3)
        self.assertEqual([x["ray_class_5_order_conditional_on_standard_exact_sequence"]
                          for x in data],[12,12,96])
        self.assertEqual([x["ray_class_25_order_conditional_on_standard_exact_sequence"]
                          for x in data],[300,300,2400])
        self.assertTrue(self.results["ray_class_order_uses_imported_global_exact_sequence"])

    def test_local_frobenius_comparison_requires_corrected_hensel_map(self):
        for d in self.results["local_Hensel_ring_transports"]:
            self.assertTrue(d["same_mod5_residue_algebra"])
            self.assertTrue(d["raw_omega_mapping_not_a_mod25_ring_hom_if_m_diff"])
            self.assertEqual(d["bounded_epsilon_covariance_tests"],49)

    def test_matched_residue_moments_do_not_claim_uniform_global_bound(self):
        data=self.results["matched_fields"]
        for row in data:
            self.assertEqual(row["matched_original_40row_Gram_rank_F5"],
                             row["nonzero_mod5_residue_weights"])
            self.assertTrue(row["residue_moment_record_is_not_class_number_one_theorem"])
        self.assertTrue(self.results["no_congruence_for_bounded_Hecke_sums_proved"])
        self.assertTrue(self.results["no_original_field_bound_changed"])

    def test_wrong_raw_omega_coordinate_frame_is_detected(self):
        phi,desc=f.local_ring_transport(163,183)
        w=(0,1)
        self.assertNotEqual(phi(w),(0,1))
        self.assertEqual(f.epsilon(w,163),f.epsilon(phi(w),183))
        self.assertNotEqual((163+1)//4%25,(183+1)//4%25)

    def test_d183_non_h1_has_impossible_principal_norm3(self):
        self.assertEqual(len(c.independent_reduced_forms(183)),8)
        self.assertGreater((183+1)//4,3)
        self.assertTrue(all(t*t!=3 for t in range(-3,4)))


if __name__=="__main__":
    unittest.main(verbosity=2)
