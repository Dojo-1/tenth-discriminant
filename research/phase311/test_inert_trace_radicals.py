#!/usr/bin/env python3
"""Phase311: hostile inert-source, Hermitian trace and class-one controls."""
import sys
import unittest
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import inert_trace_radicals as m


class InertTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q203,cls.e203,cls.p203=m.d203_full_source()
        cls.q163,cls.e163,cls.p163=m.matched_full_source(163)
        cls.q187,cls.e187,cls.p187=m.matched_full_source(187)
        cls.p163=m.matched_primitive(cls.e163)
        cls.p187=m.matched_primitive(cls.e187)

    def test_small_field_rank_not_f5_linear_rank(self):
        # [omega]*row1 is a distinct F5 row but not a new F25 row.
        e=np.array([[1,0,0,1],[0,1,4,1]],dtype=np.int64)
        self.assertEqual(m.rank_f25(e,203),1)
        self.assertEqual(m.rank_f5(e),2)
        self.assertEqual(m.realification_rank(e,203),2)

    def test_all_nonzero_f25_elements_invertible_and_frobenius_conjugates(self):
        for d in (163,187,203):
            self.assertTrue(m.field_checks(d))
        with self.assertRaises(ValueError):
            m.field_checks(211)

    def test_actual_native_d203_source_and_primitive_defects(self):
        c=m.analyze_arm(203,self.q203,self.e203,self.p203,2,[50,38,100,63])
        self.assertEqual(c["original_evaluation_kernel_dimension"],50)
        self.assertEqual(c["original_additional_restricted_trace_radical_dimension"],12)
        self.assertEqual(c["primitive_source_kernel_dimension"],0)
        self.assertEqual(c["primitive_restricted_trace_radical_dimension"],37)
        self.assertEqual(c["same_original_Gram_valuation_floor_from_disjoint_steps"],137)
        self.assertEqual(c["full_original_or_primitive_Gram_cells_checked"],20000)

    def test_h1_and_nonh1_matched_crosscontrols(self):
        for d,q,E,prim in ((163,self.q163,self.e163,self.p163),
                           (187,self.q187,self.e187,self.p187)):
            with self.subTest(d=d):
                c=m.analyze_arm(d,q,E,prim,1,[25,25,40,40])
                self.assertEqual(c["primitive_restricted_trace_radical_dimension"],0)
                self.assertEqual(c["same_original_Gram_valuation_floor_from_disjoint_steps"],30)

    def test_original_trace_conjugation_is_an_actual_observation_permutation(self):
        perm=m.conjugation_permutation(self.q203,2)
        self.assertEqual(len(perm),526)
        self.assertTrue(all(perm[perm[i]]==i for i in range(len(perm))))
        self.assertEqual(len(set(perm)),526)
        c=m.inert_cross_trace_certificate(self.e203,self.q203,2,203)
        self.assertEqual(c["full_Gram_cells_checked"],10000)
        self.assertTrue(c["conjugation_fixed_moment"])

    def test_original_Q_missing_one_conjugate_refuses_permutation(self):
        q=tuple(z for z in self.q203 if z!=(0,1))
        self.assertIn((1,-1),q)
        with self.assertRaisesRegex(ValueError,"not conjugation-closed"):
            m.conjugation_permutation(q,2)

    def test_nonunimodular_source_transformation_can_change_rank(self):
        e=self.e203.copy()%5
        e[0,:]=e[1,:]
        self.assertLess(m.rank_f25(e,203),m.rank_f25(self.e203,203))

    def test_invertible_source_frame_preserves_gram_rank(self):
        E=self.p203.copy()%5
        g=m.trace_gram_from_original(E,203)
        a=m.rank_f25(E,203)
        b=m.rank_f5(g)
        E[0,:]=(E[0,:]+2*E[1,:])%5
        gnew=m.trace_gram_from_original(E,203)
        self.assertEqual(m.rank_f25(E,203),a)
        self.assertEqual(m.rank_f5(gnew),b)
        self.assertFalse(np.array_equal(g,gnew))

    def test_wrong_bilinear_coefficient_or_trace_formula_is_caught(self):
        e=np.array([[0,1]],dtype=np.int64)  # omega coordinate
        a,b=e[:,0::2],e[:,1::2]
        d=203
        original=m.trace_gram_from_original(e,d)[0,0]
        # Independent norm identity: Tr(omega*bar omega)=2*m,
        # whereas the incorrect same-side contraction gives
        # Tr(omega²)=Tr(omega-m)=1-2*m.
        mm=(d+1)//4
        self.assertEqual(original,2*mm%5)
        self.assertNotEqual((1-2*mm)%5,original)


if __name__=="__main__":
    unittest.main(verbosity=2)
