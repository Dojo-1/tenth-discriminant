#!/usr/bin/env python3
"""Phase309 hostile controls: original-source Picard minors vs integer trace Gram."""
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sys.path.insert(0,str(HERE.parent/"phase308"))
import original_source_picard as a
import picard_tendrils as ideals


class Phase309OriginalSourcePicardTests(unittest.TestCase):
    def test_original_d203_parent_source_exact_oracle_and_local_class(self):
        p=a.patch_certificate(203,3,0,4,((6,7),(7,120)),671)
        self.assertEqual(p["parent_source_faithfulness"]["entire_parent_original_matrix_shape"],
                         [100,1052])
        self.assertEqual(p["parent_source_faithfulness"]["exact_original_coordinates_compared"],16)
        self.assertEqual(p["minor_ideal_norm"],3)
        self.assertEqual(p["ideal_class_order"],4)
        self.assertEqual(p["three_original_maximal_minors"],
                         ((3,0),(0,1),(-3,1)))
        self.assertTrue(p["original_Z_source_unchanged"])

    def test_original_gram_has_p_unit_even_with_nonprincipal_Picard(self):
        for d,p,r,k,g,det in a.CASES:
            with self.subTest(d=d):
                cert=a.patch_certificate(d,p,r,k,g,det)
                self.assertEqual(cert["ideal_class_order"],k)
                self.assertGreater(k,1)
                self.assertNotEqual(det%p,0)
                self.assertEqual(det%p,(-(1-2*r)**2)%p)
                self.assertTrue(cert["local_nonprincipal_ideal_Does_NOT_force_Gram_p_mass"])
        self.assertEqual(671%3,2)
        self.assertEqual(1055%7,5)
        self.assertEqual(527%2,1)

    def test_saturation_strictly_greater_than_integer_coefficients(self):
        for d,p,r,k,g,det in a.CASES:
            cert=a.patch_certificate(d,p,r,k,g,det)
            w=cert["strict_saturation_element"]
            z=(-r,1)
            c=ideals.conjugate(z)
            self.assertEqual(w["b_numerator_O_coordinates"],c)
            self.assertEqual(w["pb_integer_coordinates"],c)
            self.assertEqual(w["zb_integer_coordinates"],(ideals.norm(z,d)//p,0))
            self.assertNotEqual(c[1]%p,0)
            self.assertTrue(w["b_not_integral"])

    def test_enlarge_actual_observation_cover_kills_selected_patch_obstruction(self):
        for d,p,r,k,g,det in a.CASES:
            ps,q=a.patch_source(d,p,r)
            self.assertIn((1,0),q)
            orig=a.exact_patch_matrix(ps)
            augmented=orig+(((1,0),(1,0)),)
            minors=a.two_by_two_minors(augmented,d)
            self.assertIn((1,0),minors)
            self.assertEqual(ideals.ideal_z_index(d,minors),1)
            self.assertEqual(a.patch_certificate(d,p,r,k,g,det)
                             ["after_z1_minor_ideal_norm"],1)

    def test_real_original_native_observation_radii_not_invented(self):
        for d,p,r,k,g,det in a.CASES:
            ps,q=a.patch_source(d,p,r)
            self.assertGreaterEqual(ps.R,2)
            self.assertGreaterEqual(ps.S,1)
            self.assertGreaterEqual(ps.J,1)
            self.assertIn((0,0),q)
            self.assertIn((p,0),q)
            self.assertIn((-r,1),q)
            self.assertIn((1,0),q)
            self.assertTrue(all(ideals.norm(z,d)<=ps.rho*ps.rho
                                for z in ps.observations))
        with self.assertRaisesRegex(ValueError,"nonexistent original observation"):
            a.patch_source(163,41,0)

    def test_wrong_root_not_a_split_patch(self):
        with self.assertRaisesRegex(ValueError,"NOT a root"):
            a.patch_source(203,5,0)
        with self.assertRaises(ValueError):
            a.patch_source(203,3,2)
        with self.assertRaises(ValueError):
            a.patch_source(203,4,0)

    def test_direct_ideal_index_not_confused_with_integer_gram_det(self):
        ps,q=a.patch_source(203,3,0)
        A=a.exact_patch_matrix(ps)
        ideal_index=ideals.ideal_z_index(203,a.two_by_two_minors(A,203))
        gram=a.original_integer_trace_gram(ps)
        gdet=gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0]
        self.assertEqual(ideal_index,3)
        self.assertEqual(gdet,671)
        self.assertEqual(gdet%ideal_index,2)
        # A scalar 3-adic mass inference would be a mathematical mistake.
        self.assertFalse(gdet%ideal_index==0)


if __name__=="__main__":
    unittest.main(verbosity=2)
