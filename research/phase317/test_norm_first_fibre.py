#!/usr/bin/env python3
"""Phase317 exact norm-D+1 generator fibres, including hostile nonh1 cases."""
import unittest
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import norm_first_fibre as f


class NormFirstFibreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows={x["D"]:x for x in
                  f.full_fibre_certificate()["all_fundamental_field_controls"]}

    def test_six_class_one_fields_have_prime_m_and_exactly_four_generators(self):
        for D in (7,11,19,43,67,163):
            x=self.rows[D]
            self.assertEqual(x["class_number_by_reduced_forms"],1)
            self.assertTrue(x["m_prime"])
            self.assertFalse(x["m_square"])
            self.assertEqual(len(x["integer_solutions"]),4)
            self.assertEqual(x["signed_generator_classes"],2)

    def test_higher_class_number_prime_m_is_not_a_class_one_detector(self):
        x=self.rows[187]
        self.assertGreater(x["class_number_by_reduced_forms"],1)
        self.assertEqual(x["m"],47)
        self.assertTrue(x["m_prime"])
        self.assertEqual(len(x["integer_solutions"]),4)

    def test_square_m_requires_two_extra_rational_norm_fibre_generators(self):
        x=self.rows[35]
        self.assertTrue(x["m_square"])
        self.assertEqual(x["m"],9)
        self.assertEqual(len(x["integer_solutions"]),6)
        self.assertIn((6,0),x["integer_solutions"])
        self.assertIn((-6,0),x["integer_solutions"])
        self.assertEqual(x["signed_generator_classes"],3)

    def test_composite_nonsquare_m_also_has_four(self):
        x=self.rows[203]
        self.assertEqual(x["m"],51)
        self.assertTrue(x["m_composite_nonsquare"])
        self.assertGreater(x["class_number_by_reduced_forms"],1)
        self.assertEqual(len(x["integer_solutions"]),4)

    def test_wrong_domain_and_hypotheses_rejected(self):
        for D in (0,1,3,4,5,6):
            with self.assertRaises(ValueError):
                f.original_norm_fibre(D)


if __name__=="__main__":
    unittest.main(verbosity=2)
