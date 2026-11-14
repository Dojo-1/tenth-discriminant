#!/usr/bin/env python3
"""Phase313-H: ensure GLOBAL maximal-order h1 convolution is projected
through conductor2 BEFORE reconstructing the SAME original suborder Gram.
This repairs a semantic gap without altering the proved fixed determinant.
"""
import sys
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import conductor2_order_gate as m
from tame_wild_ray import ray_tag

class Conductor2OrderGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=m.conductor2_bridge_certificate()

    def test_maximal225_vs_original109_selected_by_even_omega_coordinate(self):
        d=self.data
        self.assertEqual(d["maximal_order_radius21_observations"],225)
        self.assertEqual(d["actual_original_integer_suborder_observations"],109)
        self.assertTrue(d["all_original_observations_exactly_even_omega_coefficient"])
        self.assertEqual(d["original_suborder"],"Z[sqrt(-163)] = Z + 2 O_K")

    def test_full_ray50_is_900_components_with_global_h1_convolution(self):
        d=self.data
        self.assertEqual(d["conductor2_unit_group_C3"],3)
        self.assertEqual(d["full_signed_conductor50_unit_classes"],900)
        self.assertEqual(d["independent_total_ideal_norm_shell_checks"],177)
        self.assertGreater(d["full_900_component_coprime_norm_convolutions_checked"],100)

    def test_selected_coprime5_census_and_same_original_primitive_gram(self):
        d=self.data
        self.assertEqual(d["selected_original_5unit_ideal_count"],50)
        self.assertEqual(d["original_5divisible_observation_count"],9)
        self.assertEqual(d["projected_global_h1_to_same_original_Gram_cells_checked"],1600)
        self.assertEqual(d["original_primitive_Gram_rank_mod5"],23)
        self.assertTrue(d["projected_original_25ray_census_equal_direct"])
        self.assertEqual(
            d["selected_odd_norm_ideals_ray2_1"]+
            d["selected_even_norm_ideals_2divisible"],50)

    def test_strict_counterexample_to_wrong_suborder_convolution(self):
        d=self.data["suborder_projection_not_convolution_homomorphism"]
        self.assertEqual(d["non_suborder_factor_norms"],[41,43])
        self.assertEqual(d["product_norm"],1763)
        self.assertEqual(d["product_original_integer_coordinates"],[-40,1])
        self.assertTrue(d["no_original_suborder_norm41_or43"])
        self.assertTrue(d["original_suborder_product_norm1763_exists"])
        self.assertTrue(d["projecting_convolution_before_multiplication_is_invalid"])

    def test_conductor2_field_and_projection_are_not_interchangeable(self):
        D=163
        self.assertEqual(m.norm_mod2((0,1)),1)
        self.assertEqual(m.norm_mod2((1,1)),1)
        self.assertEqual(m.mul((0,1),(1,1),D,2),(1,0))
        with self.assertRaises(ValueError):
            m.ray50_tag((0,0))
        with self.assertRaises(ValueError):
            m.ray50_tag((5,0))
        self.assertTrue(self.data["no_uniform_extra_Gram_valuation"])

if __name__=="__main__":
    unittest.main(verbosity=2)
