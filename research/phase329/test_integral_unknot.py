#!/usr/bin/env python3
"""Phase329 exact hostile controls for source Gram handle-slide knots."""
from __future__ import annotations

import random
import unittest

from integral_unknot import (
    shear, shear_inverse, coupled_gram, coupled_formula,
    coupled_source_embedding, coupled_source_return,
    frame_coupled_gram, verify_coupled_return, source_dependent_coupling,
    vp,
)
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))
from stabilized_return import (
    Q8, identity, transpose, matrix_mul, determinant, block_diag,
    original_integer_trace_gram, quaternion_left_frame,
)


def symmetric_gram(n:int,seed:int):
    rng=random.Random(seed)
    A=tuple(tuple(rng.randrange(-4,5) for _ in range(n))
            for _ in range(n))
    return matrix_mul(transpose(A),A)


class GramHandleSlideTests(unittest.TestCase):
    def test_small_nonzero_coupling_identity_and_det(self):
        B=((2,1),(1,3))
        C=((1,2),(-3,1),(0,2),(4,0),(1,-1),(-2,1))
        r=verify_coupled_return(B,C,Q8[2])
        self.assertEqual(r["source_det"],5)
        self.assertEqual(r["coupled_det"],5)
        self.assertEqual(r["shear_det"],1)
        self.assertEqual(
            tuple(tuple(x for x in row) for row in coupled_gram(B,C)),
            coupled_formula(B,C))

    def test_unimodular_shear_and_inverse_for_random_couplings(self):
        rng=random.Random(329329)
        tested=0
        for n in range(1,5):
            for m in range(1,3*n+1):
                for _ in range(5):
                    C=tuple(tuple(rng.randint(-7,7) for _ in range(n))
                            for _ in range(m))
                    T=shear(C)
                    self.assertEqual(matrix_mul(T,shear_inverse(C)),
                                     identity(n+m))
                    self.assertEqual(determinant(T),1)
                    self.assertEqual(determinant(shear_inverse(C)),1)
                    tested+=1
        self.assertEqual(tested,150)

    def test_actual_original_ordinary_z_gram_from_phase328_source(self):
        cases=[
            (7,((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1)),2,2,2),
            (11,((1,0),(0,1),(2,1),(-1,1)),2,3,1),
            (19,((0,0),(1,0),(0,1),(-1,2)),3,2,2),
        ]
        verified=0
        for D,Q,J,R,S in cases:
            B=original_integer_trace_gram(Q,D,J,R,S)
            C=source_dependent_coupling(B)
            self.assertEqual(len(C),3*R*S)
            self.assertTrue(any(v for row in C for v in row))
            for u in Q8:
                r=verify_coupled_return(B,C,u)
                self.assertEqual(r["source_det"],determinant(B))
                verified+=1
        self.assertEqual(verified,24)

    def test_noninvertible_and_negative_gram_preserve_det_exactly(self):
        for B in (((0,),),((-7,),),((1,1),(1,1)),
                  ((0,1),(1,0)),((2,-4),(-4,8))):
            n=len(B)
            C=tuple(tuple((r+2*c)%3-1 for c in range(n))
                    for r in range(3*n))
            for u in Q8:
                result=verify_coupled_return(B,C,u)
                self.assertEqual(result["coupled_det"],determinant(B))

    def test_no_new_prime_valuation_from_unimodular_resolution(self):
        B=((14,7),(7,14))
        C=source_dependent_coupling(B)
        detB=determinant(B)
        detC=determinant(coupled_gram(B,C))
        self.assertEqual(detB,147)
        for p in (2,3,5,7,11,13):
            self.assertEqual(vp(detB,p),vp(detC,p))
        self.assertEqual(vp(detB,3),1)
        self.assertEqual(vp(detB,7),2)

    def test_counterexample_nonunimodular_auxiliary_metric(self):
        # A stabilization with H=[2] would yield det=2*det B;
        # it cannot be treated as a new divisor of det B itself.
        B=((3,),)
        H=((2,),)
        self.assertEqual(determinant(block_diag(B,H)),6)
        self.assertNotEqual(determinant(block_diag(B,H)),
                            determinant(B))
        with self.assertRaises(ValueError):
            coupled_gram(B,((1,2),))
        with self.assertRaises(ValueError):
            shear(())
        with self.assertRaises(ValueError):
            frame_coupled_gram(B,((1,),),Q8[2])

    def test_two_moving_frames_intertwine_coupled_metric_and_source(self):
        B=((3,1),(1,3))
        C=source_dependent_coupling(B)
        for u in Q8:
            F=frame_coupled_gram(B,C,u)
            for v in Q8:
                U=quaternion_left_frame(v,2)
                # Applying v to the already-u-coupled metric is
                # equivalent to one frame vu by the Phase328 group law.
                from stabilized_return import quaternion_product
                W=frame_coupled_gram(B,C,quaternion_product(v,u))
                self.assertEqual(
                    W["moving"],
                    matrix_mul(matrix_mul(U,F["moving"]),transpose(U)))
                self.assertEqual(
                    W["inclusion"],matrix_mul(U,F["inclusion"]))
                self.assertEqual(
                    W["return"],matrix_mul(F["return"],transpose(U)))


if __name__=="__main__":
    unittest.main(verbosity=2)
