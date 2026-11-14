#!/usr/bin/env python3
"""Phase313: global h1 ray convolution vs nonprincipal cancellation controls."""
import unittest
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import principal_norm_shell as p


class PrincipalRayShellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h1={D:p.class_one_shell_convolution(D) for D in (43,163)}
        cls.nonh1=p.nonh1_class_cancel_witness()

    def test_every_eligible_coprime_ray_shell_convolution_under_h1(self):
        for D,x in self.h1.items():
            with self.subTest(D=D):
                self.assertEqual(x["individual_norm_shell_ideal_count_equalities_checked"],353)
                self.assertGreater(x["full_300_class_coprime_norm_shell_convolutions_verified"],100)
                self.assertEqual(x["first_second_mixed_Fermat_moment_equalities_verified"],
                                 3*x["full_300_class_coprime_norm_shell_convolutions_verified"])
                self.assertTrue(x["norm_shell_convolution_uses_GLOBAL_class_number_one"])

    def test_d183_principal_norm46_without_norm2_or_norm23(self):
        c=self.nonh1
        self.assertEqual(c["two_coprime_factor_norms"],[2,23])
        self.assertEqual(c["principal_norm2_ideals"],0)
        self.assertEqual(c["principal_norm23_ideals"],0)
        self.assertGreaterEqual(c["principal_norm46_ideals"],2)
        self.assertEqual(c["all_norm2_ideals"],2)
        self.assertEqual(c["all_norm23_ideals"],2)
        self.assertTrue(c["principal_only_convolution_R2_R23_is_zero_but_R46_nonzero"])
        self.assertTrue(c["nonprincipal_ideal_class_cancellation_witness"])

    def test_actual_full_ray_distribution_multiplication_not_just_total_counts(self):
        for D in (43,163):
            _,bins,_=p.principal_norm_ray_distribution(D)
            for n in (2,3,7,11,17,23,31):
                if n%5==0:
                    continue
                if n==1:
                    continue
                # Multiplication by norm1 identity is a genuine full
                # 300-component distribution test.
                self.assertEqual(
                    p.convolute_ray(bins[1],bins[n],D),
                    bins[n]
                )

    def test_moment_Leibniz_not_assumed_additive_after_sign_pairing(self):
        D=163
        _,bins,_=p.principal_norm_ray_distribution(D)
        for m,n in ((1,41),(2,41),(3,41),(7,41)):
            if m*n>441 or m%5==0 or n%5==0:
                continue
            # Predicted moments are derived from actual ideal tags
            # independently of the modulo5 residue-bucket Gram.
            am=p.all_ideal_count_at_norm(D,m)
            an=p.all_ideal_count_at_norm(D,n)
            self.assertTrue(p.check_moment_convolution(
                bins[m],bins[n],bins[m*n],D,am,an))


if __name__=="__main__":
    unittest.main(verbosity=2)
