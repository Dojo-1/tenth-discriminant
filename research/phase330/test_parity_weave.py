#!/usr/bin/env python3
"""Phase330 positive lift with exact parity remainder and Q8 frames."""
import random
import unittest
from fractions import Fraction
from parity_weave import (
    weave_pair,parity_compatible,deweave_pair,swap_woven_pair,
    exact_woven_matrix,four_copy_weave,woven_quaternion_action,
    woven_bilinear,verify_weave,rational_mm,
)
from chart_descent import mod,mul,identity
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))
from stabilized_return import (
    Q8,quaternion_left_frame,matrix_mul,determinant,block_diag,
    original_integer_trace_gram, transpose,
)


def mv(A,x):
    return tuple(sum(a*b for a,b in zip(row,x)) for row in A)


class IntegralParityWeaveTests(unittest.TestCase):
    def test_exact_image_index_and_inverse(self):
        for n in range(1,5):
            r=verify_weave(n)
            self.assertEqual(r["paired_index"],2**n)
            self.assertEqual(r["four_copy_index"],4**n)
            self.assertTrue(r["q8_compatible"])
            self.assertEqual(determinant(exact_woven_matrix(n)),(-2)**n)

    def test_integer_weave_deweave_random(self):
        rng=random.Random(330330)
        for n in range(1,5):
            for _ in range(128):
                x=tuple(rng.randint(-100,100) for i in range(n))
                y=tuple(rng.randint(-100,100) for i in range(n))
                woven=weave_pair(x,y)
                self.assertTrue(parity_compatible(*woven))
                self.assertEqual(deweave_pair(*woven),(x,y))
                self.assertEqual(
                    swap_woven_pair(*woven),weave_pair(y,x))

    def test_adversarial_parity_lattice_rejects_ambient_pair(self):
        for n in range(1,5):
            u=(1,)+(0,)*(n-1)
            v=(0,)*n
            self.assertFalse(parity_compatible(u,v))
            with self.assertRaises(ValueError):
                deweave_pair(u,v)
        with self.assertRaises(ValueError):
            weave_pair((1,),(1,2))

    def test_original_source_gram_bilinear_kept_on_parity_lattice(self):
        B=original_integer_trace_gram(
            ((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1)),
            D=7,J=2,R=2,S=2)
        self.assertEqual(len(B),4)
        rng=random.Random(33032)
        for _ in range(100):
            x=tuple(rng.randint(-8,8) for _ in range(4))
            y=tuple(rng.randint(-8,8) for _ in range(4))
            xp=tuple(rng.randint(-8,8) for _ in range(4))
            yp=tuple(rng.randint(-8,8) for _ in range(4))
            u,v=weave_pair(x,y)
            up,vp=weave_pair(xp,yp)
            naive=sum(x[i]*B[i][j]*xp[j]+y[i]*B[i][j]*yp[j]
                      for i in range(4) for j in range(4))
            self.assertEqual(woven_bilinear(B,u,v,up,vp),naive)

    def test_gram_two_copy_metric_requires_ambient_half(self):
        B=((3,1),(1,5))
        W=exact_woven_matrix(2)
        source=block_diag(B,B)
        ambient=tuple(tuple(Fraction(x,2) for x in row)
                      for row in source)
        preserved=rational_mm(rational_mm(transpose(W),ambient),W)
        self.assertEqual(
            preserved,
            tuple(tuple(Fraction(x) for x in row) for row in source))
        self.assertEqual(determinant(W),4)
        # Ambient half-integer entries are not an integral Gram on
        # the entire Z^4, but they define an integer pairing on
        # the index-four parity sublattice.
        self.assertEqual(ambient[0][0],Fraction(3,2))

    def test_q8_acts_integrally_on_woven_four_copy_parity_lattice(self):
        rng=random.Random(330720)
        for n in (1,2,3):
            W=four_copy_weave(n)
            for u in Q8:
                U=quaternion_left_frame(u,n)
                Uw=woven_quaternion_action(u,n)
                self.assertEqual(matrix_mul(Uw,W),matrix_mul(W,U))
                for _ in range(20):
                    original=tuple(rng.randint(-10,10) for _ in range(4*n))
                    woven=mv(W,original)
                    moved=mv(Uw,woven)
                    self.assertEqual(moved,mv(W,mv(U,original)))
                    self.assertTrue(parity_compatible(
                        moved[:n],moved[n:2*n]))
                    self.assertTrue(parity_compatible(
                        moved[2*n:3*n],moved[3*n:]))

    def test_four_copy_q8_woven_group_law(self):
        from interleaved_f1_prime import product as quaternion_product
        for n in (1,2):
            for u in Q8:
                for v in Q8:
                    uv=quaternion_product(u,v)
                    self.assertEqual(
                        matrix_mul(woven_quaternion_action(u,n),
                                   woven_quaternion_action(v,n)),
                        woven_quaternion_action(uv,n))

    def test_mod_two_loses_inverse_but_mod_seven_recovers_it(self):
        for n in (1,2,3):
            W=exact_woven_matrix(n)
            W2=mod(W,2)
            W7=mod(W,7)
            self.assertEqual(mul(W2,W2,2),mod(
                tuple(tuple(0 for _ in range(2*n)) for _ in range(2*n)),2))
            inv7=mod(tuple(tuple(4*x for x in row) for row in W),7)
            self.assertEqual(mul(W7,inv7,7),mod(identity(2*n),7))
            self.assertEqual(mul(inv7,W7,7),mod(identity(2*n),7))


if __name__=="__main__":
    unittest.main(verbosity=2)
