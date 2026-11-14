#!/usr/bin/env python3
"""Adversarial tests for the exact Phase321 ideal-aware ray groups."""
import unittest

import ideal_aware_ray_class as phase


class Phase321IdealAwareRayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = phase.run_phase321()
        cls.groups = {x["D"]: x for x in cls.data["ray_groups"]}
        cls.catalogs = {x["D"]: x for x in cls.data["prime_ideal_catalogs"]}

    def test_exact_reduced_form_class_numbers(self):
        self.assertEqual([self.groups[D]["class_number"] for D in (163, 187, 203)],
                         [1, 2, 4])
        self.assertEqual(self.groups[187]["ordinary_class_group_element_orders"],
                         (1, 2))
        self.assertEqual(self.groups[203]["ordinary_class_group_element_orders"],
                         (1, 4, 4, 2))

    def test_ray_group_orders_and_local_kernel(self):
        expected = {163: 7500, 187: 15000, 203: 30000}
        for D, order in expected.items():
            row = self.groups[D]
            self.assertEqual(row["local_unit_count_mod125"], 15000)
            self.assertEqual(row["signed_local_ray_kernel_order"], 7500)
            self.assertEqual(row["ray_class_group_order"], order)
            self.assertEqual(row["expected_ray_class_group_order"], order)
            self.assertEqual(row["full_ray_group_inverse_checks"], order)
            self.assertTrue(row["full_ray_group_identity_and_inverse_verified"])

    def test_exact_ideal_product_and_cocycle_associativity(self):
        for D in (163, 187, 203):
            row = self.groups[D]
            h = row["class_number"]
            self.assertEqual(row["exact_ideal_product_scalings"], h * h)
            self.assertEqual(row["ordinary_class_group_associativity_checks"], h ** 3)
            self.assertEqual(row["exact_cocycle_associativity_checks"], h ** 3)
            self.assertEqual(row["exact_cocycle_commutativity_checks"], h * h)

    def test_nonprincipal_classes_are_present_and_not_replaced_by_elements(self):
        for D in (187, 203):
            row = self.catalogs[D]
            self.assertGreater(row["nonprincipal_prime_ideal_records"], 0)
            self.assertTrue(row["every_prime_ideal_mapped_into_full_ray_group"])
            self.assertTrue(row["all_split_conjugate_products_verified"])
            self.assertTrue(row["all_ramified_squares_verified"])

    def test_bounded_prime_ideal_catalog(self):
        for D in (163, 187, 203):
            row = self.catalogs[D]
            self.assertEqual(row["rational_prime_bound"], 441)
            self.assertTrue(row["prime_5_excluded_from_ray_group"])
            self.assertGreater(row["split_rational_primes"], 0)
            self.assertGreater(row["ramified_rational_primes"], 0)
            self.assertEqual(len(row["catalog_sha256"]), 64)

    def test_D163_reduces_to_phase315_local_group(self):
        row = self.groups[163]
        self.assertTrue(row["D163_reduces_to_Phase315_local_signed_unit_group"])
        self.assertEqual(row["ray_class_group_order"], 7500)
        self.assertEqual(row["ray_cocycle_residues_mod125"], (((1, 0),),))

    def test_nontrivial_cocycles_are_recorded_not_assumed_away(self):
        d187 = self.groups[187]["ray_cocycle_residues_mod125"]
        d203 = self.groups[203]["ray_cocycle_residues_mod125"]
        self.assertNotEqual(d187[1][1], (1, 0))
        self.assertNotEqual(d203[1][1], (1, 0))
        for D in (163, 187, 203):
            self.assertTrue(self.groups[D]["extension_not_assumed_split"])

    def test_hnf_is_canonical_and_ideal_norm_multiplicative(self):
        for D in (163, 187, 203):
            forms = phase.reduced_forms(D)
            ideals = [phase.form_ideal(f) for f in forms]
            for I in ideals:
                self.assertEqual(phase.hnf(list(phase.ideal_basis(I))), I)
                self.assertEqual(phase.ideal_norm(I), I[0] * I[2])
            for I in ideals:
                for J in ideals:
                    product = phase.ideal_product(I, J, D)
                    self.assertEqual(product, phase.ideal_product(J, I, D))
                    self.assertEqual(phase.ideal_norm(product),
                                     phase.ideal_norm(I) * phase.ideal_norm(J))


if __name__ == "__main__":
    unittest.main(verbosity=2)
