#!/usr/bin/env python3
"""Phase319 maximal-order ray-realization regression tests."""
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import maximal_order_realization as phase


class MaximalOrderRealizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = phase.full_maximal_order_certificate()
        cls.byprime = {
            x["split_prime"]: x for x in cls.data["per_character_records"]
        }

    def test_full_support_is_not_the_old_integer_order_support(self):
        d = self.data
        self.assertEqual(d["full_maximal_order_Q"], 225)
        self.assertEqual(d["old_integer_order_Q"], 109)
        self.assertEqual(d["new_odd_omega_coordinate_points"], 116)
        self.assertEqual(d["F25_residue_support"], 25)
        self.assertEqual(d["signed_5unit_sites"], 108)
        self.assertEqual(d["nonunit_observations"], 9)

    def test_full_maximal_order_primitive_gram_has_no_mod5_radical(self):
        d = self.data
        self.assertEqual(d["actual_primitive_Gram_rank_mod5"], 40)
        self.assertEqual(d["actual_primitive_Gram_first_two_Smith_layers"],
                         [40, 0, 0])
        local = d["local_norm_preserving_second_wild_map"]
        self.assertEqual(local["all_local_lifts_checked"], 540)
        self.assertEqual(local["maximal_order_primitive_radical_dimension"], 0)
        self.assertEqual(local["radical_normal_image_dimension"], 0)
        self.assertLessEqual(
            local["full_symmetric_40x40_local_differential_span_rank"], 108
        )

    def test_every_split_prime_character_has_full_global_ray_replay(self):
        d = self.data
        self.assertEqual(d["split_prime_characters_tested"], 34)
        self.assertEqual(len(self.byprime), 34)
        for p, row in self.byprime.items():
            self.assertEqual(row["full_ray250_norm_shell_checks"], 177, p)
            self.assertEqual(row["full_ray250_coprime_products"], 270, p)
            self.assertTrue(row["all_changed_shells_have_full_exact_fibre_audit"])
            self.assertEqual(row["maximal_order_first_two_smith_layers"], [40, 0, 0])
            self.assertTrue(row["no_5adic_valuation_claim_from_residue_change"])

    def test_phase318_resonance_fibres_remain_unrealized_in_maximal_order(self):
        fibres = self.data["mandatory_exact_norm_fibres"]
        self.assertEqual(set(fibres), {41, 53, 227})
        for p, row in fibres.items():
            self.assertEqual(row["signed_generator_classes"], 2)
            self.assertEqual(len(row["all_maximal_order_generators"]), 4)
            self.assertTrue(row["synthetic_support_disjoint"])
            self.assertGreater(row["synthetic_classes_unrealized"], 0)

    def test_exact_maximal_order_norm_equation(self):
        expected = {164: 4, 212: 4, 227: 4}
        for n, count in expected.items():
            fibre = phase.exact_maximal_order_norm_fibre(n)
            self.assertEqual(len(fibre), count)
            self.assertTrue(all(phase.quadratic_norm(z, phase.D) == n
                                for z in fibre))

    def test_local_and_global_claims_remain_bounded(self):
        d = self.data
        self.assertTrue(d["all_full_support_synthetic_grams_keep_unit_mod5"])
        self.assertTrue(d["no_uniform_field_valuation_or_cutoff_claim"])
        self.assertGreaterEqual(
            d["active_on_full_maximal_support"],
            d["active_on_old_even_support"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
