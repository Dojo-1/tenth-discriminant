#!/usr/bin/env python3
"""Phase312-B: coherent complete local Z5 ring equivalence negative controls."""
import unittest
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import local_completion_no_go as l


class LocalCompletionNoGoTests(unittest.TestCase):
    def test_all_three_pairs_exact_coherent_hensel_at_depth_six(self):
        for D,E in ((43,163),(163,183),(43,183)):
            with self.subTest(pair=(D,E)):
                data=l.exact_bidirectional_controls(D,E,6)
                self.assertEqual(data["levels"],6)
                self.assertEqual(data["highest_modulus"],15625)
                self.assertTrue(data["inverse_and_conjugation_checked_at_every_level"])
                self.assertTrue(data["phase_A_mod25_reference_reproduced"])
                self.assertTrue(data["first_Fermat_quotient_covariant"])
                self.assertEqual(data["actual_multiplicativity_checks"],96)

    def test_mod25_corrected_omega_transport_has_specific_nontrivial_digit(self):
        phi,x=l.coherent_hensel_lift(163,183,3)
        self.assertEqual(x[0]["omega_image"],(0,1))
        self.assertEqual(x[1]["omega_image"],(10,6))
        self.assertNotEqual(phi((0,1),2),(0,1))
        self.assertEqual(l.quadratic_relation(phi((0,1),3),163,183,125),(0,0))

    def test_wrong_residue_chart_and_zero_precision_rejected(self):
        with self.assertRaises(ValueError):
            l.coherent_hensel_lift(163,67,6)
        with self.assertRaises(ValueError):
            l.coherent_hensel_lift(163,183,0)
        phi,_=l.coherent_hensel_lift(163,183,3)
        with self.assertRaises(ValueError):
            phi((0,1),4)

    def test_same_local_ring_does_not_identify_global_discriminant(self):
        a=l.exact_bidirectional_controls(163,183,4)
        self.assertNotEqual(a["source_D"],a["target_D"])
        self.assertTrue(a["same_local_algebra_does_not_constrain_global_class_number"])


if __name__=="__main__":
    unittest.main(verbosity=2)
