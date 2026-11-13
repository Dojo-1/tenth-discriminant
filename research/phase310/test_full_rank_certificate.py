#!/usr/bin/env python3
"""Phase310-C: hostile modular minor and fixed-source index-square tests."""
import sys
import unittest
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import full_rank_certificate as c


class FullRankCertificateTests(unittest.TestCase):
    def test_known_answer_finite_field_determinant_and_rank(self):
        r=c.independent_minor_known_controls()
        self.assertEqual(r["known_triangular_det_mod101"],27)
        self.assertEqual(r["rectangular_minor_and_wrong_duplicate_rank"],[3,2])

    def test_wrong_root_rejected_by_defining_equation(self):
        self.assertEqual(c.simple_roots(203,101),(46,56))
        self.assertNotIn(0,c.simple_roots(203,101))
        self.assertEqual(c.simple_roots(203,5),())

    def test_original_good_prime_full_rank_minor_source(self):
        q=tuple(c.original.original_q()) if hasattr(c.original,"original_q") else tuple(c.original.qmax(24))
        x=c.rank_minor_good_prime(q,101)
        self.assertEqual(x["original_source_all_coordinates_checked"],105200)
        # This assert is the preregistered prediction; a failure must
        # NOT be repaired by silently choosing a different good prime.
        self.assertTrue(x["any_full_rank_witness"])
        for witness in x["rank_minor_witnesses"]:
            self.assertEqual(witness["Fell_rank"],100)
            self.assertNotEqual(witness["100x100_minor_det_modell_if_full"],0)
            self.assertEqual(len(witness["pivot_observation_jet_columns_if_full"]),100)

    def test_duplicate_row_destroys_nonzero_original_minor(self):
        q=tuple(c.original.qmax(24))
        E=c.original_evaluation_at_good_prime(q,101)
        X=(E[:,0::2]+46*E[:,1::2])%101
        r,cols=c.row_rank_and_pivot_columns(X,101)
        self.assertEqual(r,100)
        dup=X.copy()
        dup[1,:]=dup[0,:]
        self.assertEqual(c.row_rank_and_pivot_columns(dup,101)[0],99)
        self.assertEqual(c.determinant_mod_p(dup[:,list(cols)],101),0)

    def test_derived_p3_bound_provenance_and_no_uniform_promotion(self):
        cert=c.source_index_square_lower_bound()
        self.assertGreaterEqual(cert["p3_split_local_source_Smith_lower_bound"],658)
        self.assertGreaterEqual(cert["derived_certified_original_Gram_v3_lower_bound"],1316)
        self.assertEqual(cert["derived_certified_original_Gram_v3_lower_bound"],
                         2*cert["p3_split_local_source_Smith_lower_bound"])
        self.assertTrue(cert["real_Hermitian_trace_Gram_positive_definite_by_full_row_rank"])
        self.assertTrue(cert["D203_is_class_number_four"])
        self.assertTrue(cert["no_new_uniform_h1_or_tenth_discriminant_bound"])


if __name__=="__main__":
    unittest.main(verbosity=2)
