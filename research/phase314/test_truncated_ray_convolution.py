#!/usr/bin/env python3
"""Phase314-B: full conductor50 h1 product survives 216 wild jets and
projection goes ONLY after multiplication, preserving original Gram.
"""
import sys
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import truncated_ray_convolution as c
from wild_quadratic_gram import monomials


class TruncatedRayConvolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=c.full_conductor50_quadratic_certificate()

    def test_full_h1_ray50_convolution_in_216_jet_algebra(self):
        a=self.result
        self.assertEqual(a["full_signed_ray50_classes"],900)
        self.assertEqual(a["truncated_wild_second_jet_coordinates"],216)
        self.assertEqual(a["eligible_norm_shells_exactly_accounted"],177)
        self.assertEqual(a["full_900_ray_convolution_jet_pairs_verified"],270)
        self.assertTrue(a["truncated_wild_quotient_convolution_compatible"])

    def test_original_conductor2_selector_retains_correct_72plus6_moments(self):
        a=self.result
        self.assertEqual(a["maximal_order_Q"],225)
        self.assertEqual(a["original_integer_order_Q"],109)
        self.assertEqual(a["selected_odd_norm_unit_ideals"],26)
        self.assertEqual(a["selected_even_norm_unit_ideals"],24)
        self.assertEqual(a["nonunit_first_lift_observations"],9)
        self.assertEqual(a["original_selected_72plus6_moment_capacity"],78)
        self.assertTrue(a["suborder_projection_NOT_a_convolution_map"])

    def test_same_original_integer_Gram_all_entries_and_rank_preserved(self):
        a=self.result
        self.assertEqual(a["same_original_integer_Gram_cells_reconstructed"],1600)
        self.assertEqual(a["same_original_integer_primitive_Gram_rank_mod5"],23)
        self.assertEqual(a["source_coefficients_full_25wild_value_checks"],300)
        self.assertTrue(a["no_class_number_one_extra_valuation_inferred"])

    def test_six_raw_moment_convolution_formula_under_arbitrary_wild_values(self):
        for x,y in (((1,2),(3,4)),((0,0),(1,0)),((4,1),(3,3))):
            A=monomials(x)
            B=monomials(y)
            actual=c.moment_product_six(A,B)
            add=((x[0]+y[0])%5,(x[1]+y[1])%5)
            self.assertEqual(tuple(v%5 for v in actual),monomials(add))
        z=(0,0,0,0,0,0)
        A=monomials((1,2))
        self.assertEqual(c.moment_product_six(A,z),z)

    def test_mixed_moment_cross_term_cannot_be_dropped(self):
        u=monomials((1,2))
        v=monomials((2,1))
        r=c.moment_product_six(u,v)
        self.assertEqual(r[4]%5,monomials((3,3))[4])
        no_cross=(u[4]*v[0]+u[0]*v[4])%5
        self.assertNotEqual(r[4]%5,no_cross)


if __name__=="__main__":
    unittest.main(verbosity=2)
