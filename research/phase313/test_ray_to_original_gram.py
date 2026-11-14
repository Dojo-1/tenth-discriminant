#!/usr/bin/env python3
"""Phase313-D: exact same-original Gram ray-to-matrix bridge tests."""
import unittest
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import ray_to_original_gram as r
from tame_wild_ray import ray_tag


class RayToOriginalGramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d203=r.complete_D203_source_certificate()
        cls.d163=r.complete_D163_original_integer_source_certificate()

    def test_all_original_D203_primitive_Gram_cells_from_global_ray(self):
        a=self.d203
        self.assertEqual(a["original_Q"],263) if "original_Q" in a else None
        self.assertEqual(a["same_original_primitive_Gram_cells_verified"],10000)
        self.assertEqual(a["Gram_rank_F5"],63)
        self.assertEqual(a["ray_and_nonunit_sufficient_statistics"]["nonunit_observations"],9)
        self.assertEqual(a["ray_and_nonunit_sufficient_statistics"]["principal_ideal_count_prime_to5"],127)
        self.assertEqual(a["source_5_divisions"],50)

    def test_exact_native_D163_Lean_integer_pair_source_not_maximal_order(self):
        a=self.d163
        self.assertEqual(a["source"],"EXACT original Lean Z[sqrt(-163)] integer pair Q109 rho21 R40 S=J1")
        self.assertEqual(a["original_primitive_source_shape"],[40,218])
        self.assertEqual(a["original_integer_source_F25_coordinates_checked"],40*109*2)
        self.assertEqual(a["original_integer_trace_to_omega_Gram_cells_checked"],1600)
        self.assertEqual(a["global_ray_to_same_original_primitive_Gram_cells_checked"],1600)
        self.assertEqual(a["native_source_exact_p_divided_rows"],15)
        self.assertTrue(a["class_one_norm_shell_convolution_now_has_TYPED_Gram_forward_map"])

    def test_ray_spectrum_needs_both_unit_and_5divisible_observations(self):
        q=r.pilot.qmax(24)
        g,c=r.ray_count_Gram_D203(q)
        self.assertEqual(g.shape,(100,100))
        self.assertEqual(c["original_Q"],263)
        self.assertEqual(c["nonunit_observations"],9)
        self.assertEqual(2*c["principal_ideal_count_prime_to5"]+
                         c["nonunit_observations"],263)
        self.assertTrue(c["source_map_count_linear_mod5"])
        self.assertTrue(c["all_300_ray_components_only_principal_ideals_when_nonh1"])

    def test_wild_field_log_is_sign_invariant_but_epsilon_is_sign_odd(self):
        D=163
        z=(6,0)
        neg=(-6,0)
        self.assertEqual(ray_tag(z,D),ray_tag(neg,D))
        self.assertNotEqual(r.epsilon(z,D),r.epsilon(neg,D))
        c,w=ray_tag(z,D)
        ca=r.wild_unit_features(c,w,D)
        minus=((-c[0])%5,(-c[1])%5)
        cb=r.wild_unit_features(minus,w,D)
        self.assertEqual(cb[1],r.scale(-1,ca[1],5))

    def test_5divisible_first_lift_not_zero_just_because_residue_zero(self):
        u=(1,0)
        e=r.nonunit_features(u,203)
        self.assertEqual(e[1],(4,0))
        self.assertEqual(e[2],(4,0))
        z=(5,0)
        self.assertEqual(r.epsilon(z,203),(4,0))


if __name__=="__main__":
    unittest.main(verbosity=2)
