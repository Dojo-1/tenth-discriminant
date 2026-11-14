#!/usr/bin/env python3
"""Phase309-B hostile checks for conjugate-embedding and Hermitian trace transport."""
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))

import split_embedding_transport as s
import original_source_picard as source


class Phase309SplitEmbeddingTests(unittest.TestCase):
    def test_both_embedded_residue_worlds_and_trace_agree(self):
        for d,p,r,g,det in (
          (203,3,0,((6,7),(7,120)),671),
          (187,7,2,((6,11),(11,196)),1055),
          (167,2,0,((6,5),(5,92)),527)):
            with self.subTest(field=d):
                c=s.certify(d,p,r,g,det)
                self.assertEqual((c["rank_first_embedding"],
                                  c["rank_second_embedding"]),(1,2))
                self.assertEqual(c["all_hermitian_trace_pairs_compared"],2401)
                self.assertNotEqual(c["original_det_mod_p"],0)
                self.assertTrue(c["same_side_dot_pairing_is_wrong"])

    def test_heterogeneous_local_rank_and_nonzero_cross_gram(self):
        (r1,r2),ps=s.split_embeddings(203,3,0)
        a=source.exact_patch_matrix(ps)
        x,y=s.residue_eval(a,r1,3),s.residue_eval(a,r2,3)
        self.assertEqual(s.mod_rank(x,3),1)
        self.assertEqual(s.mod_rank(y,3),2)
        cross=s.cross_trace_gram(x,y,3)
        self.assertEqual(cross,((0,1),(1,0)))
        self.assertEqual(s.mod_rank(cross,3),2)
        wrong=s.same_embedding_fallacy(x,y,3)
        self.assertNotEqual(wrong,cross)

    def test_wrong_embedding_or_wrong_field_is_rejected(self):
        with self.assertRaises(ValueError):
            s.split_embeddings(203,5,0)
        with self.assertRaises(ValueError):
            s.split_embeddings(203,3,2)
        with self.assertRaises(ValueError):
            s.split_embeddings(163,41,0) # outside actual original source

    def test_residue_pairing_is_symmetric_but_not_euclidean_same_side(self):
        (r1,r2),ps=s.split_embeddings(187,7,2)
        a=source.exact_patch_matrix(ps)
        x,y=s.residue_eval(a,r1,7),s.residue_eval(a,r2,7)
        b=s.cross_trace_gram(x,y,7)
        self.assertEqual(b,((6,4),(4,0)))
        self.assertEqual(b[0][1],b[1][0])
        self.assertNotEqual(s.same_embedding_fallacy(x,y,7),b)


if __name__=="__main__":
    unittest.main(verbosity=2)
