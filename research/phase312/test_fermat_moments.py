#!/usr/bin/env python3
"""Phase312 hostile controls for inert Fermat-quotient features and primitive
D203 original ordinary-jet source. These tests are correlated AI-authored
verification, NOT independent mathematical peer review.
"""
import sys
from pathlib import Path
import unittest
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import fermat_lift as f
import primitive_moments as m


class Phase312FermatPrimitiveTests(unittest.TestCase):
    def test_local_fermat_product_and_addition_not_naive_derivation(self):
        for D in (43,163,183,203):
            for x in ((0,0),(1,0),(6,0),(0,1),(1,2)):
                for y in ((-2,3),(1,-1),(0,1),(6,0)):
                    self.assertTrue(f.check_fermat_laws(x,y,D))
        self.assertEqual(f.epsilon((1,0),163),(0,0))
        self.assertEqual(f.epsilon((6,0),163),(4,0))
        self.assertNotEqual(f.epsilon((2,0),163),
                            f.add(f.epsilon((1,0),163),
                                  f.epsilon((1,0),163),5))

    def test_mod25_moving_frame_required_to_compare_local_quadratic_orders(self):
        for D,E in ((43,163),(163,183),(43,183)):
            with self.subTest(pair=(D,E)):
                data=f.transport_controls(D,E)
                self.assertTrue(data["raw_omega_mapping_not_a_mod25_ring_hom_if_m_diff"])
                self.assertEqual(data["bounded_epsilon_covariance_tests"],49)
                self.assertEqual(data["bounded_multiplicativity_tests"],196)

    def test_full_100_original_primitive_rows_and_all_jets_from_epsilon(self):
        rec=m.primitive_moment_certificate()
        self.assertEqual(rec["all_primitive_value_and_ordinary_jet_omega_coordinates_reconstructed"],
                         105200)
        self.assertEqual(rec["same_original_source_shape"],[100,1052])
        self.assertEqual(rec["source_rows_p_divided"],50)
        self.assertEqual(rec["primitive_Gram_rank_F5"],63)
        self.assertEqual(rec["moment_primitive_Gram_cells_checked"],10000)
        self.assertEqual(rec["actual_F25_residue_bins"],25)
        self.assertTrue(rec["same_residue_1_and_6_distinct_primitive_F5row"])

    def test_hermitian_moment_tensor_is_not_scalar_residue_count(self):
        z=(1,0)
        e1=f.epsilon((1,0),203)
        e6=f.epsilon((6,0),203)
        self.assertEqual(e1,(0,0))
        self.assertEqual(e6,(4,0))
        M1a,M1b=m.moments_for_class(((1,0),))
        M6a,M6b=m.moments_for_class(((6,0),))
        self.assertEqual(int(M1a[0,0]),1)
        self.assertEqual(int(M6a[0,0]),1)
        self.assertFalse(np.array_equal(M1a,M6a))
        self.assertTrue(np.array_equal(M1b,np.zeros((3,3),dtype=np.int64)))
        self.assertTrue(np.array_equal(M6b,np.zeros((3,3),dtype=np.int64)))

    def test_wrong_j1_along_curve_W_equals_Z5_is_not_original_ordinary_jet(self):
        z=(6,0)
        # r5 Frobenius row: F_5=(Z^5-W)/5. Holding W fixed,
        # its ordinary j1 at Z=z is Z^4 = 1 mod5. If W were
        # incorrectly differentiated as Z^5, j1 would vanish.
        c=m.residue_jet_coefficients((1,0))
        j1=m.field_dot(c[1,10],m.feature(z))
        self.assertEqual(j1,(1,0))
        self.assertNotEqual(j1,(0,0))


if __name__=="__main__":
    unittest.main(verbosity=2)
