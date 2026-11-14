#!/usr/bin/env python3
"""Phase313: hostile local tame/wild unit and nonsemisimple algebra tests."""
import unittest
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import tame_wild_ray as t
sys.path.insert(0,str(HERE.parent/"phase312"))
from fermat_lift import local_ring_transport,conjugate


class WildRayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fields={D:t.ring_unit_orbits(D) for D in (43,163,183,203)}

    def test_exhaustive_600_unit_300_signed_ray_bijection(self):
        for D,x in self.fields.items():
            with self.subTest(D=D):
                self.assertEqual(x["units_mod25"],600)
                self.assertEqual(x["sign_quotient_classes"],300)
                self.assertEqual(x["tame_orbits"],12)
                self.assertEqual(x["wild_additive_classes"],25)
                self.assertTrue(x["principal_unit_wild_isomorphism"])
                self.assertTrue(x["all_24_tame_residues_have_25_wild_lifts"])

    def test_normalized_log_escapes_odd_raw_epsilon_null(self):
        D=163
        self.assertEqual(t.normalized_delta((1,0),D),(0,0))
        self.assertEqual(t.normalized_delta((6,0),D),(4,0))
        self.assertEqual(t.normalized_delta((-6,0),D),(4,0))
        self.assertEqual(t.ray_tag((6,0),D),t.ray_tag((-6,0),D))
        self.assertNotEqual(t.ray_tag((1,0),D),t.ray_tag((6,0),D))

    def test_raw_cross_field_omega_not_a_transport_but_hensel_delta_is(self):
        phi,data=local_ring_transport(163,183)
        self.assertNotEqual(phi((0,1)),(0,1))
        for z in ((1,0),(6,0),(0,1),(1,2),(-4,3)):
            if not t.norm_mod5(z,163):
                continue
            self.assertEqual(t.normalized_delta(z,163),
                             t.normalized_delta(phi(z),183))

    def test_nonunits_are_not_divided_inside_quadratic_field(self):
        for D in (43,163,183):
            for z in ((0,0),(5,0),(0,5)):
                with self.subTest(D=D,z=z):
                    with self.assertRaises(ZeroDivisionError):
                        t.normalized_delta(z,D)
                    with self.assertRaises(ValueError):
                        t.tame_orbit(z,D)

    def test_wild_group_algebra_nilpotent_not_ordinary_fourier(self):
        data=t.wild_augmentation_certificate()
        self.assertEqual(data["wild_group_algebra_F5_dimension"],25)
        self.assertEqual(data["graded_dimensions"],[1,2,3,4,5,4,3,2,1])
        self.assertTrue(data["augmentation_J9_zero_J8_nonzero"])
        self.assertTrue(data["nonsemisimple_wild_p_part_not_captured_by_F25_Fourier"])

    def test_wild_tame_product_is_direct_product(self):
        D=203
        z=(6,0)
        w=(0,1)
        self.assertEqual(t.ray_tag(t.mul(z,w,D,25),D),
                         t.tag_mul(t.ray_tag(z,D),t.ray_tag(w,D),D))
        self.assertEqual(t.ray_tag(z,D),t.ray_tag((-6,0),D))
        self.assertEqual(t.normalized_delta(t.conjugate(w),D),
                         conjugate(t.normalized_delta(w,D),5))


if __name__=="__main__":
    unittest.main(verbosity=2)
