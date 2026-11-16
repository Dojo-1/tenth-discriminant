#!/usr/bin/env python3
"""Phase330 exact H1/Tate H0 bridge to Phase325 ray arithmetic."""
import unittest

from frobenius_cohomology import cohomology_of_ray_group


class FrobeniusSquareCohomologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows={D:cohomology_of_ray_group(D) for D in (163,187,203)}
        import json
        print("PHASE330_FROB_H1_TATE_H0",
              json.dumps(cls.rows,sort_keys=True),flush=True)

    def test_actual_ray_group_H1_orders_and_square_fibers(self):
        for D,expected in ((163,2),(187,4),(203,4)):
            r=self.rows[D]
            self.assertEqual(r["H1_C2_ray_order"],expected)
            self.assertEqual(r["Tate_H0_C2_ray_order"],expected)
            self.assertEqual(r["squared_frob_class_ambiguity"],expected)
            self.assertTrue(r["cohomology_two_torsion_verified"])

    def test_exact_kernel_image_and_fixed_order_quotients(self):
        for D,r in self.rows.items():
            self.assertEqual(r["norm_image_order"],50)
            self.assertEqual(
                r["ker_norm_order"]*r["norm_image_order"],
                r["G_order"])
            self.assertEqual(
                r["ker_norm_order"]//r["difference_image_order"],
                r["H1_C2_ray_order"])
            self.assertEqual(
                r["G_fixed_order"]//r["norm_image_order"],
                r["Tate_H0_C2_ray_order"])

    def test_frobenius_ambiguity_is_not_a_prime_distribution_bound(self):
        for r in self.rows.values():
            self.assertTrue(r["does_not_establish_global_prime_inequality"])
            self.assertTrue(r["does_not_establish_original_jet_intertwiner"])

    def test_matched_distinct_coefficient_modules_do_not_claim_identity(self):
        # H1(C2,Z_sign)=Z/2, whereas the ray-group H1 is a
        # finite abelian 2-group of order 2 or 4. Equal patterns
        # of 2-torsion do not identify their coefficient modules.
        self.assertEqual(self.rows[163]["H1_C2_ray_order"],2)
        self.assertEqual(self.rows[187]["H1_C2_ray_order"],4)
        self.assertEqual(self.rows[203]["H1_C2_ray_order"],4)
        self.assertNotEqual(self.rows[187]["H1_C2_ray_order"],2)


if __name__=="__main__":
    unittest.main(verbosity=2)
