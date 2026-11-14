#!/usr/bin/env python3
"""Phase318-A complete local norm-preserving second-wild site controls."""
import unittest
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import local_wild_normal as q


class CompleteNativeWildNormalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=q.local_normal_certificate()

    def test_same_original_109_source_and_all_5unit_nonunit_strata(self):
        d=self.data
        self.assertEqual(d["native_original_integer_order_Q"],109)
        self.assertEqual(d["native_original_primitive_rows"],40)
        self.assertEqual(d["native_original_mod25_Gram_cells"],1600)
        self.assertEqual(d["signed_5unit_sites"],50)
        self.assertEqual(d["separate_5nonunit_observations"],9)
        self.assertEqual(d["complete_admissible_lifts_per_5unit_site"],5)
        self.assertEqual(d["complete_local_site_5unit_lifts_checked"],250)

    def test_exact_trace_norm_line_and_source_first_wild_digit_preserved(self):
        d=self.data
        self.assertTrue(d["local_norm_functional_is_nonzero_and_kernel_line"])
        self.assertTrue(d["all_original_primitive_mod5_matrices_unchanged"])
        self.assertEqual(d["mod5_radical_dimension"],17)
        self.assertEqual(d["original_first_radical_lift_rank"],7)

    def test_normal_image_and_conjugation_covariant_subspace_report_no_invented_gain(self):
        d=self.data
        rank=d["all_50_site_normal_image_rank"]
        cov=d["conjugation_covariant_normal_image_rank"]
        self.assertGreaterEqual(rank,cov)
        self.assertLessEqual(rank,50)
        self.assertGreaterEqual(cov,0)
        counts=d["conjugation_covariant_local_parameter_controls"]
        self.assertEqual(
            2*counts["conjugate_pairs"]+
            counts["self_conjugate_allowed_norm_directions"]+
            counts["self_conjugate_forbidden_norm_directions"],50)
        self.assertLessEqual(cov,counts[
            "conjugation_covariant_independent_local_parameters"])
        self.assertTrue(d["does_not_impose_full_global_ideal_convolution"])
        self.assertTrue(d["does_not_claim_new_field_or_valuation"])

    def test_hostile_trace_nonzero_perturbation_rejected_by_local_norm125(self):
        Qint,Qomega,G,meta=q.original_integer_source_oracle()
        sites,non=q.signed_unit_sites(Qomega)
        z=sites[0]
        h=next((u,v) for u in range(5) for v in range(5)
               if q.trace_norm_differential((u,v),z)!=0)
        shifted=(z[0]+25*h[0],z[1]+25*h[1])
        self.assertNotEqual(q.norm(shifted,q.D,q.TOP),q.norm(z,q.D,q.TOP))
        good,_=q.entire_norm_line(z)
        self.assertEqual(q.trace_norm_differential(good,z),0)

    def test_nonunit_cannot_occupy_p5_unit_ray_lift(self):
        with self.assertRaises(ValueError):
            q.entire_norm_line((0,0))
        with self.assertRaises(ValueError):
            q.entire_norm_line((5,0))
        with self.assertRaises(ValueError):
            q.entire_norm_line((0,5))

    def test_original_source_radical_witness_semantically_correct(self):
        d=self.data
        i=d["first_normal_site_witness_if_any"]
        if d["sites_with_nonzero_normal_restriction"]:
            self.assertIsNotNone(i)
            self.assertGreater(i["single_site_normal_rank"],0)
            self.assertIn(i["first_nonzero_radical_entry"][2],(1,2,3,4))
        else:
            self.assertEqual(d["all_50_site_normal_image_rank"],0)
            self.assertIsNone(i)


if __name__=="__main__":
    unittest.main(verbosity=2)
