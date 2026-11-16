#!/usr/bin/env python3
"""Phase325 exact congruence controls for inert Frobenius class labels."""
import unittest

from abelian_frobenius_labels import (
    abelianization_dimension_control,
    inert_frobenius_label,
    kronecker_for_prime,
)


class AbelianFrobeniusLabelTests(unittest.TestCase):
    def test_quadratic_field_and_genus_degree_match(self):
        for D, target in ((163, 200),(187, 400),(203, 400)):
            v=abelianization_dimension_control(D)
            self.assertEqual(v["max_abelian_subfield_degree"], target)
            self.assertEqual(v["semidirect_abelianization_order"], target)
            self.assertEqual(v["inert_rational_frobenius_class_count"],
                             target//2)

    def test_D163_two_and_127_same_inert_class_label(self):
        self.assertEqual(inert_frobenius_label(163,2),(2,))
        self.assertEqual(inert_frobenius_label(163,127),(2,))

    def test_D187_genus_sign_separates_same_norm_square(self):
        self.assertEqual(inert_frobenius_label(187,2),(2,1))
        self.assertEqual(inert_frobenius_label(187,2377),(2,-1))
        self.assertNotEqual(inert_frobenius_label(187,2),
                            inert_frobenius_label(187,2377))

    def test_D203_genus_sign_separates_same_norm_square(self):
        self.assertEqual(inert_frobenius_label(203,2),(2,-1))
        self.assertEqual(inert_frobenius_label(203,3877),(2,1))
        self.assertNotEqual(inert_frobenius_label(203,2),
                            inert_frobenius_label(203,3877))

    def test_bad_input_split_ramified_and_conductor_rejected(self):
        # An inert-only label cannot be used to classify split primes.
        with self.assertRaises(ValueError):
            inert_frobenius_label(163, 5)
        with self.assertRaises(ValueError):
            inert_frobenius_label(163, 163)
        with self.assertRaises(ValueError):
            inert_frobenius_label(163, 4)
        with self.assertRaises(ValueError):
            inert_frobenius_label(163, 41) if kronecker_for_prime(-163,41)==1 else inert_frobenius_label(163, 1)

    def test_prime_two_kronecker_and_real_genus_signs(self):
        for D in (163,187,203):
            self.assertEqual(kronecker_for_prime(-D,2),-1)
        self.assertEqual(kronecker_for_prime(17,2),1)
        self.assertEqual(kronecker_for_prime(29,2),-1)


if __name__=="__main__":
    unittest.main(verbosity=2)
