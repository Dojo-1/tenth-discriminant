#!/usr/bin/env python3
"""Phase313: exact original/primitive sign-parity Gram split hostile tests."""
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import sign_parity_gram as s


class OriginalSignParityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=s.sign_parity_gram_certificate()

    def test_original_and_primitive_50_by_50_orthogonal_blocks(self):
        d=self.data
        self.assertEqual(d["actual_Q"],263)
        self.assertEqual(d["even_row_count"],50)
        self.assertEqual(d["odd_row_count"],50)
        self.assertEqual(d["original_opposite_parity_Gram_zero_cells"],5000)
        self.assertEqual(d["primitive_opposite_parity_Gram_zero_cells"],5000)

    def test_smith_profiles_split_but_original_valuation_not_double_counted(self):
        d=self.data
        a=d["primitive_even_smith_levels"]
        b=d["primitive_odd_smith_levels"]
        self.assertEqual(a.get(0,0)+b.get(0,0),63)
        self.assertEqual(a.get(1,0)+b.get(1,0),36)
        self.assertEqual(a.get(2,0)+b.get(2,0),1)
        self.assertEqual(d["combined_primitive_exact_v5"],38)
        self.assertEqual(d["same_original_v5_after_50_5_divisions"],138)
        self.assertTrue(d["parity_split_does_not_add_new_valuation"])

    def test_remove_one_observation_destroy_same_parity_invariant(self):
        self.assertEqual(self.data["asymmetric_observation_Gram_constant_Z_cross"],123)
        self.assertTrue(self.data["sign_parity_requires_full_actual_source_support"])

    def test_original_F_and_K_shears_preserve_row_parity(self):
        par=s.source_row_parity()
        self.assertEqual(par[0],0)
        self.assertEqual(par[1],1)
        self.assertEqual(par[2],1)
        self.assertEqual(par[3],0)
        self.assertEqual(len([x for x in par if x==0]),50)


if __name__=="__main__":
    unittest.main(verbosity=2)
