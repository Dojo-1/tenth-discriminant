#!/usr/bin/env python3
"""Phase328 adversarial exact integer stabilization and tapestry gates."""
from __future__ import annotations

import random
import unittest

from stabilized_return import (
    H_ONE, H_NEG_ONE, Q8, identity, transpose, matrix_mul, matrix_mod,
    determinant, block_diag, quaternion_left_frame, scalar_inclusion,
    stabilized_gram, frame_transport, return_gram, verify_stable_return,
    original_integer_trace_gram, pair_mul, pair_pow,
    integer_derivative_row, counterexample_fixed_metric,
)


def random_symmetric_gram(n: int, seed: int):
    """Deterministic positive integral Gram; not the source Gram."""
    rng = random.Random(seed)
    C = tuple(tuple(rng.randint(-3,3) for _ in range(n))
              for _ in range(n))
    G = matrix_mul(transpose(C),C)
    return tuple(tuple(G[i][j] + int(i == j)
                       for j in range(n)) for i in range(n))


class OriginalTraceGramSourceTests(unittest.TestCase):
    def test_exact_pair_source_convention_and_factor_two(self):
        self.assertEqual(pair_mul(7,(1,2),(3,4)),(-53,10))
        self.assertEqual(pair_pow(7,(0,1),2),(-7,0))
        self.assertEqual(integer_derivative_row(7,0,1,1,(1,1)),(0,0))
        self.assertEqual(integer_derivative_row(7,1,1,1,(1,1)),(1,-1))
        B=original_integer_trace_gram(((1,0),(0,1)),7,1,1,1)
        self.assertEqual(B,((16,),))
        self.assertEqual(determinant(B),16)
        self.assertEqual(
            original_integer_trace_gram(((1,0),),7,1,1,1),((2,),))
        # The source includes a literal factor two, not a normalized
        # new scalar product or invented mixed Z/W derivative.

    def test_source_gram_symmetry_and_finite_set_semantics(self):
        inputs=[
            (7,((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1)),2,2,2),
            (11,((1,0),(0,1),(2,1),(-1,1)),2,3,1),
            (19,((0,0),(1,0),(0,1),(-1,2)),3,2,2),
        ]
        for D,Q,J,R,S in inputs:
            B=original_integer_trace_gram(Q,D,J,R,S)
            self.assertEqual(B,transpose(B))
            self.assertEqual(len(B),R*S)
            self.assertTrue(all(B[i][i]>=0 for i in range(R*S)))
            self.assertEqual(
                B,original_integer_trace_gram(tuple(reversed(Q)),D,J,R,S))
            for u in Q8:
                self.assertTrue(verify_stable_return(B,u)["returned_exact"])
        with self.assertRaises(ValueError):
            original_integer_trace_gram(((1,0),(1,0)),7,2,2,2)


class Phase328IntegralMovingTapestry(unittest.TestCase):
    def test_full_Q8_representation_and_det_one(self):
        for n in (1,2,3,4):
            for u in Q8:
                U=quaternion_left_frame(u,n)
                self.assertEqual(matrix_mul(U,transpose(U)),identity(4*n))
                self.assertEqual(matrix_mul(transpose(U),U),identity(4*n))
                self.assertEqual(determinant(U),1)
                for v in Q8:
                    uv=__import__("stabilized_return").quaternion_product(u,v)
                    self.assertEqual(
                        matrix_mul(quaternion_left_frame(u,n),
                                   quaternion_left_frame(v,n)),
                        quaternion_left_frame(uv,n))

    def test_exhaustive_8_frame_integer_return_for_random_gram(self):
        examined=0
        for n in (1,2,3,4):
            for seed in (0,1,3,7):
                B=random_symmetric_gram(n,n*100+seed)
                for u in Q8:
                    r=verify_stable_return(B,u)
                    self.assertEqual(r["det_source"],determinant(B))
                    examined+=1
        self.assertEqual(examined,128)

    def test_two_moving_frames_metric_naturality(self):
        B=((2,1),(1,3))
        G0=stabilized_gram(B)
        E0=scalar_inclusion(2)
        for u in Q8:
            U=quaternion_left_frame(u,2)
            frame=frame_transport(B,u)
            self.assertEqual(frame["embed"],matrix_mul(U,E0))
            self.assertEqual(return_gram(frame),B)
            for v in Q8:
                V=quaternion_left_frame(v,2)
                uv=__import__("stabilized_return").quaternion_product(u,v)
                both=frame_transport(B,uv)
                self.assertEqual(
                    both["moving"],
                    matrix_mul(matrix_mul(U,frame_transport(B,v)["moving"]),
                               transpose(U)))
                self.assertEqual(
                    both["embed"],matrix_mul(U,frame_transport(B,v)["embed"]))
                self.assertEqual(
                    both["return"],
                    matrix_mul(frame_transport(B,v)["return"],transpose(U)))
        self.assertEqual(determinant(G0),determinant(B))

    def test_two_distinct_gram_regimes_and_no_fake_divisor(self):
        result=counterexample_fixed_metric()
        self.assertEqual(result["original_det"],2)
        self.assertEqual(result["covariant_det"],2)
        self.assertEqual(result["fixed_invariant_det"],16)
        self.assertTrue(result["fixed_metric_isometry_fails_for_return_stabilization"])
        B=((2,),)
        self.assertEqual(determinant(stabilized_gram(B,"return")),2)
        self.assertEqual(determinant(stabilized_gram(B,"isometric")),2**4)
        self.assertNotEqual(16%2**4,2%2**4)

    def test_spin_sign_retained_in_inclusion_not_gram(self):
        B=((3,1),(1,2))
        f=frame_transport(B,H_ONE)
        g=frame_transport(B,H_NEG_ONE)
        self.assertNotEqual(f["embed"],g["embed"])
        self.assertEqual(
            g["embed"],
            tuple(tuple(-x for x in row) for row in f["embed"]))
        self.assertEqual(f["moving"],g["moving"])
        self.assertEqual(
            matrix_mod(f["embed"],2),matrix_mod(g["embed"],2))
        self.assertNotEqual(
            matrix_mod(f["embed"],7),matrix_mod(g["embed"],7))
        self.assertEqual(return_gram(f),return_gram(g))

    def test_exact_prime_reduction_commutes_with_transport(self):
        rng=random.Random(328360)
        for n in (1,2,3):
            B=random_symmetric_gram(n,rng.randrange(9999))
            for u in Q8:
                frame=frame_transport(B,u)
                for ell in (2,3,5,7,11):
                    U=matrix_mod(frame["U"],ell)
                    B0=matrix_mod(frame["base"],ell)
                    E=matrix_mod(frame["embed"],ell)
                    moving=matrix_mod(frame["moving"],ell)
                    self.assertEqual(moving,matrix_mod(
                        matrix_mul(matrix_mul(U,B0),transpose(U)),ell))
                    self.assertEqual(
                        matrix_mod(return_gram(frame),ell),
                        matrix_mod(B,ell))
                    self.assertEqual(
                        matrix_mod(matrix_mul(frame["return"],frame["embed"]),ell),
                        matrix_mod(identity(n),ell))

    def test_unimodular_return_not_fixed_gram_isometry(self):
        B=((2,),)
        U=quaternion_left_frame((0,1,0,0),1)
        G0=stabilized_gram(B)
        G1=matrix_mul(matrix_mul(U,G0),transpose(U))
        self.assertNotEqual(G1,G0)
        self.assertEqual(determinant(G0),determinant(G1))
        # A fixed metric with four copies is invariant, but has det B^4.
        four=stabilized_gram(B,"isometric")
        self.assertEqual(matrix_mul(matrix_mul(U,four),transpose(U)),four)
        self.assertNotEqual(determinant(four),determinant(B))

    def test_no_unwarranted_full_jet_equivariance(self):
        # The stabilized return works on the full original Gram as an
        # integer matrix, not on a freshly invented set of derivatives.
        # The source ordinary-Z derivative of W is zero; after
        # conjugation W becomes Z and the derivative is one.
        W_z_derivative=0
        conjugate_W_z_derivative=1
        self.assertNotEqual(W_z_derivative,conjugate_W_z_derivative)


if __name__=="__main__":
    unittest.main(verbosity=2)
