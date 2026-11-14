#!/usr/bin/env python3
"""Phase318-C: 1d normal pencil and all 16 h1 global ray controls."""
from pathlib import Path
import sys
import unittest
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import normal_pencil as p


class NormalPencilAndHeldoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=p.normal_pencil_certificate()

    def test_full_site_image_is_one_dimensional_not_one_normal_matrix_rank(self):
        a=self.data
        self.assertEqual(a["D"],163)
        self.assertEqual(a["original_native_integer_order_Q"],109)
        self.assertEqual(a["original_mod5_Gram_radical_dim"],17)
        self.assertEqual(a["original_first_lift_rank"],7)
        self.assertEqual(a["complete_local_sites"],50)
        self.assertEqual(a["nonzero_local_site_normals"],8)
        self.assertEqual(a["normal_image_dim"],1)
        self.assertEqual(len(a["all_50_local_normal_coefficients_mod5"]),50)
        self.assertEqual(sum(c!=0 for c in
                             a["all_50_local_normal_coefficients_mod5"]),8)
        self.assertGreater(a["first_nonzero_normal_matrix_rank"],0)

    def test_every_of_five_lambda_has_computed_first_lift_rank(self):
        ranks=self.data["exact_F5_normal_pencil_lambda_to_rank"]
        self.assertEqual(len(ranks),5)
        self.assertEqual(ranks[0],7)
        self.assertTrue(self.data["pencil_rank_drop_resonance_scalars"])
        for lam in self.data["pencil_rank_drop_resonance_scalars"]:
            self.assertIn(lam,(1,2,3,4))
            self.assertLess(ranks[lam],7)

    def test_exact_nonsingular_7x7_minor_and_vandermonde_degree_bound(self):
        a=self.data
        self.assertEqual(len(a["specific_nonzero_original_7x7_minor_rows"]),7)
        self.assertEqual(len(a["specific_nonzero_original_7x7_minor_cols"]),7)
        dets=a["minor_determinants_at_lambda_0_1_2_3_4"]
        self.assertEqual(len(dets),5)
        self.assertNotEqual(dets[0],0)
        coef=a["degree_at_most_rankN_minor_polynomial_coefficients_mod5"]
        self.assertEqual(len(coef),5)
        for lam in range(5):
            self.assertEqual(dets[lam],
                             sum(coef[j]*pow(lam,j,5) for j in range(5))%5)
        for lam in a["pencil_rank_drop_resonance_scalars"]:
            self.assertEqual(dets[lam],0)

    def test_both_observed_synthetic_e1_changers_fit_frozen_normal_pencil(self):
        a=self.data
        rec={x["prime"]:x for x in
             a["per_character_normal_pencil_scales_and_smith"]}
        self.assertEqual(len(rec),16)
        self.assertEqual(rec[41]["original_synthetic_first_two_smith"],[23,7,10])
        for prime in (53,227):
            x=rec[prime]
            self.assertEqual(x["original_synthetic_first_two_smith"],[23,3,14])
            self.assertTrue(x["normal_pencil_predicts_smith_e1"])
            self.assertGreater(x["normal_restriction_rank"],0)
            self.assertIn(prime,
                          a["globally_multiplicative_synthetic_characters_changing_e1"])

    def test_full_native_global_250_convolution_for_all_16_active(self):
        rows=self.data["complete_16_character_native_conductor250_replay"]
        self.assertEqual(len(rows),16)
        for row in rows:
            self.assertEqual(row["all_independent_h1_ideal_norm_shells"],177)
            self.assertEqual(row["full_22500_conductor250_coprime_products"],270)

    def test_heldout_p53_p227_original_ideal_counts_and_all_59_products(self):
        rows=self.data["heldout_radius60_p53_p227_full_ray250_convolutions"]
        self.assertEqual([r["prime"] for r in rows],[53,227])
        for row in rows:
            self.assertEqual(row["heldout_radius"],60)
            self.assertEqual(row["heldout_maximal_order_Q"],1785)
            self.assertEqual(row["all_independent_prime_to10_ideal_shells"],1440)
            self.assertEqual(row["genuine_nonidentity_coprime_full_ray250_products"],59)
            self.assertGreater(row["exact_ideal_character_multiplication_checks"],10000)
            self.assertTrue(row["original_integer_order_Q109_NOT_replaced"])

    def test_h2_D187_principal_convolution_counterworld_is_retained(self):
        self.assertTrue(self.data["nonh1_D187_principal_ray_failure_control"])
        self.assertTrue(self.data["no_new_field_or_discriminant_cutoff_improvement"])

    def test_modular_determinant_hostile_controls(self):
        self.assertEqual(p.determinant_mod5(np.asarray([[0,1],[1,0]])),4)
        self.assertEqual(p.determinant_mod5(np.diag([1,2,3])),1)
        self.assertEqual(p.determinant_mod5(np.asarray([[5,1],[0,5]])),0)
        with self.assertRaises(ValueError):
            p.determinant_mod5(np.zeros((2,3),dtype=np.int64))


if __name__=="__main__":
    unittest.main(verbosity=2)
