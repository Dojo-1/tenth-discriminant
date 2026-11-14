#!/usr/bin/env python3
"""Phase312-C: global ideal-vs-principal shell and misleading moment null tests."""
import unittest
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import norm_shell_bridge as m


class GlobalNormShellTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={d:m.actual_shell_and_orbit_certificate(d,h)
                  for d,h in m.FIELDS}

    def test_h1_both_fields_have_full_principal_ideal_shell_equality(self):
        for d in (43,163):
            x=self.data[d]
            self.assertEqual(x["all_positive_norm_shells_checked"],441)
            self.assertIsNone(x["first_nonprincipal_shell_if_any"])
            self.assertEqual(x["total_nonprincipal_ideals_norm_at_most_rho_squared"],0)

    def test_nonh1_d183_first_failure_is_split_ideal_of_norm_two(self):
        x=self.data[183]
        f=x["first_nonprincipal_shell_if_any"]
        self.assertEqual(f["n"],2)
        self.assertEqual(f["all_ideals_norm_n"],2)
        self.assertEqual(f["principal_norm_n_element_count"],0)
        self.assertGreater(x["total_nonprincipal_ideals_norm_at_most_rho_squared"],0)
        self.assertEqual(m.quadratic_character_at_prime(183,2),1)
        self.assertEqual(m.quadratic_character_at_prime(183,3),0)

    def test_twice_ideal_count_and_kronecker_character_known_cases(self):
        for d in (43,163,183):
            self.assertEqual(m.all_ideal_count_at_norm(d,1),1)
            self.assertEqual(m.kronecker_character(d,1),1)
        self.assertEqual(m.quadratic_character_at_prime(43,2),-1)
        self.assertEqual(m.quadratic_character_at_prime(163,2),-1)
        self.assertEqual(m.all_ideal_count_at_norm(163,2),0)
        with self.assertRaises(ValueError):
            m.kronecker_character(163,0)

    def test_unweighted_first_Fermat_moment_zero_even_when_h8(self):
        for d in (43,163,183):
            x=self.data[d]
            self.assertEqual(x["total_unweighted_first_Fermat_moment_mod5"],(0,0))
            self.assertTrue(x["vanishing_first_moment_is_sign_symmetry_NOT_h1"])

    def test_ray_class_residue_orbits_are_principal_only(self):
        for d in (43,163,183):
            groups=self.data[d]["twelve_principal_unit_orbit_counts"]
            self.assertEqual(len(groups),12)
            self.assertTrue(all(c>=0 for c in groups.values()))
            self.assertTrue(self.data[d]["global_h1_necessary_norm_shell_identity_no_congruence_moment_theorem"])

    def test_local_five_divisibility_is_not_global_ideal_class(self):
        self.assertIsNone(m.unit_orbit((0,0)))
        self.assertIsNone(m.unit_orbit((5,-5)))
        self.assertEqual(m.unit_orbit((1,2)),m.unit_orbit((-1,-2)))


if __name__=="__main__":
    unittest.main(verbosity=2)
