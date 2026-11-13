#!/usr/bin/env python3
"""Phase311-C: adversarial original residue-bucket Gram compression tests."""
import sys
from pathlib import Path
import unittest

import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import residue_multiplicity as m
from inert_trace_radicals import matched_full_source,full_omega_q


class ResidueMultiplicityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q163,cls.e163,_=matched_full_source(163)
        cls.G163,cls.meta163=m.compressed_original_gram(cls.q163,163,40,1,1)

    def test_original_d163_nonh1_controls_and_all_Gram_entries(self):
        c=m.original_arms()
        self.assertEqual(len(c),3)
        self.assertEqual([(x["source_rank_F25"],
                           x["original_Gram_rank_F5"]) for x in c],
                         [(25,25),(25,25),(50,38)])
        self.assertEqual(c[-1]["independent_exact_original_Gram_cells_checked"],10000)
        self.assertEqual(c[0]["independent_exact_original_Gram_cells_checked"],1600)
        self.assertEqual(c[1]["independent_exact_original_Gram_cells_checked"],1600)

    def test_source_rank_and_trace_rank_bounds_are_distinct(self):
        self.assertEqual(self.meta163["source_rank_F25"],25)
        self.assertEqual(self.meta163["original_Gram_rank_F5"],25)
        self.assertLessEqual(self.meta163["original_Gram_rank_F5"],
                             self.meta163["rank_upper_bound_from_weights"])
        self.assertEqual(self.meta163["observed_distinct_F25_residue_classes"],25)

    def test_larger_original_parameter_D427_is_an_explicit_nonh1_control(self):
        c=m.larger_native_D427()
        self.assertEqual(c["original_R_S_J"],[106,4,4])
        self.assertEqual(c["source_rows"],424)
        self.assertEqual(c["observed_distinct_F25_residue_classes"],25)
        self.assertEqual(c["ten_by_ten_direct_actual_original_Gram_cells_checked"],100)
        self.assertLessEqual(c["original_Gram_rank_F5"],
                             c["rank_upper_bound_from_weights"])
        self.assertTrue(c["D427_non_h1_norm7_ramified_obstruction"])

    def test_synthetic_five_duplicate_source_observations_mod5_neutral(self):
        q=tuple(self.q163)
        g1,_=m.compressed_original_gram(q+((0,0),)*5,163,40,1,1)
        self.assertTrue(np.array_equal(g1,self.G163))
        # Adding ONE extra zero observation changes the constant-row trace.
        g2,_=m.compressed_original_gram(q+((0,0),),163,40,1,1)
        self.assertNotEqual(int(self.G163[0,0]),int(g2[0,0]))

    def test_incorrect_residue_multiplicity_changes_Gram(self):
        q=self.q163
        C=m.full_original_residue_evaluator(((0,0),),163,40,1,1)
        g=m.weighted_gram_from_residue_representatives(C,[1],163)
        self.assertEqual(int(g[0,0]),2)
        g_wrong=m.weighted_gram_from_residue_representatives(C,[2],163)
        self.assertEqual(int(g_wrong[0,0]),4)

    def test_missing_conjugation_rejected_before_as_if_original(self):
        q=tuple(z for z in self.q163 if z!=(0,1))
        self.assertIn((1,-1),q)
        with self.assertRaises(AssertionError):
            m.residue_census(q,163)

    def test_order_five_and_higher_ordinary_derivatives_vanish_mod5(self):
        q=((0,0),(1,0),(0,1))
        E=m.full_original_residue_evaluator(q,203,8,2,6)
        n=len(q)
        for jet in (5,):
            cols=E[:,2*jet*n:2*(jet+1)*n]
            self.assertTrue(np.all(cols==0))


if __name__=="__main__":
    unittest.main(verbosity=2)
