#!/usr/bin/env python3
"""Phase315: adversarial second 5-adic wild logarithm, unit ring semantics."""
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from wild_log125 import (
    exhaustive_lift_table,wild_log_25,twisted_defect,
    signed_ray125_tag,inv
)
from tame_wild_ray import ray_tag

class WildConductor125Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local={D:exhaustive_lift_table(D)[1] for D in (163,183,187)}

    def test_all_15000_local_units_and_7500_signed_ray_classes_each_field(self):
        for D,c in self.local.items():
            with self.subTest(D=D):
                self.assertEqual(c["ring_mod125_total_elements"],15625)
                self.assertEqual(c["unit_mod125_count"],15000)
                self.assertEqual(c["signed_unit_ray125_count"],7500)
                self.assertEqual(c["tame_residue_count"],12)
                self.assertEqual(c["p_adic_two_digit_wild_values_per_exact_residue"],625)
                self.assertTrue(c["explicit_lookup_15000_residue_wild_pairs"])

    def test_raw_defect_twisted_product_nonzero_but_truncated_log_additive(self):
        for D,c in self.local.items():
            self.assertIsNotNone(c["raw_defect_is_NOT_additive_witness"])
            self.assertGreater(c["twisted_defect_and_corrected_log_product_tests"],10000)
            self.assertTrue(c["conjugation_and_signed_invariance_all_units_checked"])

    def test_first_level_collision_retains_second_wild_digit(self):
        z1,z2=(1,0),(26,0)
        for D in self.local:
            self.assertEqual(ray_tag(z1,D),ray_tag(z2,D))
            self.assertNotEqual(signed_ray125_tag(z1,D),signed_ray125_tag(z2,D))
            self.assertEqual(wild_log_25(z1,D),(0,0))
            self.assertEqual(wild_log_25(z2,D),(20,0))

    def test_residue_nonunit_division_is_explicitly_rejected(self):
        for D in self.local:
            for z in ((0,0),(5,0),(0,5),(25,0)):
                with self.assertRaises(ZeroDivisionError):
                    inv(z,D)
                with self.assertRaises(ZeroDivisionError):
                    twisted_defect(z,D)
                with self.assertRaises(ValueError):
                    signed_ray125_tag(z,D)


if __name__=="__main__":
    unittest.main(verbosity=2)
