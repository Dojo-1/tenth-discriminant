#!/usr/bin/env python3
"""Phase310 hostile controls: full original D203 split-embedding mirror geometry."""
import sys
from pathlib import Path
import unittest

import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import full_source_split_mirror as a


class FullSourceSplitMirrorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q=a.original_q()
        cls.E=a.original.evaluate_original_jets(cls.q,a.R,a.S,a.J,a.MOD)
        cls.X0=a.residue_field_projection(cls.E,0,3)
        cls.X1=a.residue_field_projection(cls.E,1,3)

    def test_full_original_263_point_and_all_100_rows(self):
        c=a.actual_source_certificate()
        self.assertEqual(c["source_evaluation_shape"],[100,1052])
        self.assertEqual(c["entire_original_omega_coordinate_checks"],105200)
        self.assertEqual(c["full_original_integer_Gram_cells_checked"],10000)
        self.assertEqual(c["whole_source_split_embedding_ranks_F3"],[12,12])
        self.assertLessEqual(c["actual_full_source_Gram_rank_F3"],12)
        self.assertEqual(c["distinct_actual_residue_pairs"],9)

    def test_conjugation_mirror_survives_reordering_actual_observations(self):
        full=a.original.original_trace_gram(self.E,len(self.q),a.J,3)
        reverse=tuple(reversed(self.q))
        Er=a.original.evaluate_original_jets(reverse,a.R,a.S,a.J,a.MOD)
        xr=a.residue_field_projection(Er,0,3)
        yr=a.residue_field_projection(Er,1,3)
        moved,ids=a.two_jet_column_permutation(xr,reverse)
        self.assertTrue(np.array_equal(moved,yr))
        self.assertTrue(all(ids[ids[i]]==i for i in range(len(ids))))
        inverted_gram=a.original.original_trace_gram(Er,len(reverse),a.J,3)
        self.assertTrue(np.array_equal(inverted_gram,full))
        self.assertTrue(np.array_equal(
            (xr@yr.T+yr@xr.T)%3,full))

    def test_unimodular_moving_source_frame_preserves_cross_gram_covariance(self):
        g=(self.X0@self.X1.T+self.X1@self.X0.T)%3
        x=self.X0.copy()
        y=self.X1.copy()
        x[0,:]=(self.X0[0,:]+2*self.X0[11,:])%3
        y[0,:]=(self.X1[0,:]+2*self.X1[11,:])%3
        moved=(x@y.T+y@x.T)%3
        expected=g.copy()
        expected[0,:]=(g[0,:]+2*g[11,:])%3
        expected[:,0]=(expected[:,0]+2*expected[:,11])%3
        self.assertTrue(np.array_equal(expected,moved))
        self.assertEqual(a.f_rank(g,3),a.f_rank(moved,3))
        self.assertEqual(a.f_rank(x,3),a.f_rank(self.X0,3))
        self.assertNotEqual(int(np.sum(np.abs(g-moved))),0)

    def test_wrong_same_embedded_dot_pairing_on_original_ring(self):
        # x=y=omega, embeddings0,1; original Hermitian trace is zero mod3,
        # incorrectly pairing each view with itself gives one.
        x0,x1=a.residue_field_projection(np.asarray([[0,1]]),0,3)[0,0],\
               a.residue_field_projection(np.asarray([[0,1]]),1,3)[0,0]
        self.assertEqual((x0*x1+x1*x0)%3,0)
        self.assertEqual((x0*x0+x1*x1)%3,1)

    def test_source_truncation_breaks_permutation_while_actual_pairing_stays_defined(self):
        culprit=(0,1)
        cut=tuple(z for z in self.q if z!=culprit)
        with self.assertRaisesRegex(ValueError,"not conjugation-invariant"):
            a.conjugation_permutation(cut)
        self.assertIn((1,-1),cut)
        self.assertNotIn(culprit,cut)

    def test_non_split_prime_and_wrong_source_types(self):
        with self.assertRaisesRegex(ValueError,"not a simple split"):
            a.split_roots(203,5)
        with self.assertRaises(ValueError):
            a.residue_field_projection(np.zeros((2,3)),0,3)

    def test_real_jet_quotient_spans_every_original_row(self):
        c0=a.check_symbolic_jet_span(self.X0)
        c1=a.check_symbolic_jet_span(self.X1)
        self.assertEqual(c0["basis_rank_F3"],12)
        self.assertEqual(c1["basis_rank_F3"],12)
        self.assertEqual(c0["source_coordinate_comparisons"],52600)
        self.assertEqual(c1["source_coordinate_comparisons"],52600)


if __name__=="__main__":
    unittest.main(verbosity=2)
