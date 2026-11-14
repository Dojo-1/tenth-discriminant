#!/usr/bin/env python3
"""Phase316-B: small norm form and class-one ideal rigidity controls."""
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import small_norm_rigidity as x


class SmallNormRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=x.all_controls()

    def test_every_h1_ideal_shell_below_m_is_exactly_rational_square(self):
        c=self.data["h1_small_norm_ideal_rigidity"]
        self.assertEqual([v["D"] for v in c],[43,163])
        self.assertEqual([v["maximal_order_m"] for v in c],[11,41])
        self.assertEqual([v["all_independent_ideal_shells_n_less_m_checked"] for v in c],[10,40])
        self.assertEqual([v["number_of_rational_square_ideal_shells"] for v in c],[3,6])
        self.assertTrue(all(v["all_ideal_shells_iff_rational_squares"] for v in c))

    def test_real_global_h1_exact_low_norm_rays_survive_twist(self):
        c=self.data["h1_small_norm_ideal_rigidity"][1]
        self.assertEqual(c["synthetic_41prime_wild_twist_small_norm_shells_unchanged"],6)
        self.assertEqual(c["signed_conductor250_eligible_low_norm_shells_unchanged"],2)
        self.assertTrue(c["small_prime_ideal_norm_obstruction_implies_inertness_under_h1"])

    def test_actual_h2_D187_counterworld_has_nonprincipal_small_norm_ideals(self):
        n=self.data["h2_nonprincipal_ideal_counterworld"]
        self.assertEqual(n["D"],187)
        self.assertEqual(n["class_number"],2)
        self.assertEqual(n["maximal_order_m"],47)
        self.assertTrue(n["same_small_norm_element_rational_square_rule_as_h1"])
        witness={x["norm"]:x for x in n["explicit_nonprincipal_ideal_norm_failures"]}
        self.assertEqual(witness[11]["all_integral_ideals"],1)
        self.assertEqual(witness[17]["all_integral_ideals"],1)
        self.assertEqual(witness[11]["principal_ideals"],0)
        self.assertEqual(witness[17]["principal_ideals"],0)

    def test_original_order_conductor2_delays_first_active_generator_to_164(self):
        x=self.data["native_original_integer_order_threshold"]
        self.assertEqual(x["smallest_nonrational_original_order_element_norm"],163)
        self.assertEqual(x["smallest_norm_original_order_element_affected_by_wild_twist"],164)
        self.assertEqual(x["first_wild_gauge_active_integer_point"],[1,1])
        self.assertEqual(x["maximal_order_omega_first_nonrational_norm"],41)
        self.assertTrue(x["original_integer_point_not_replaced_by_maximal_order"])

    def test_second_depth_gauge_countermodel_still_changes_original_gram(self):
        self.assertTrue(self.data["second_depth_twist_preserves_all_h1_rational_square_shells_below_m"])
        self.assertTrue(self.data["but_h1_original_integer_Gram_mod25_changes_above_m"])
        self.assertEqual(self.data["native_source_Q"],109)
        self.assertEqual(self.data["synthetic_original_Gram_changed_cells_mod25"],363)
        self.assertTrue(self.data["small_norm_criterion_classical_not_novel"])
        self.assertTrue(self.data["no_uniform_cutoff_change"])

if __name__=="__main__":
    unittest.main(verbosity=2)
