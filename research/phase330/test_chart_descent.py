#!/usr/bin/env python3
"""Phase330 exact modular/intertwiner obstruction and hostile controls."""
from __future__ import annotations
from math import prod,gcd
import unittest

from chart_descent import (
    identity,swap,diagonal,first_return,add,scale,mul,mod,
    two_chart_norm,two_chart_difference,
    symmetric_return_mod,verify_chart_obstruction,
    single_chart_gram_pullback,quotient_invariants_c2,
)
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase329"))
from stabilized_return import original_integer_trace_gram,determinant
from braid_frobenius import S3_GROUP,hurwitz_positive


class IntegralConjugateChartDescent(unittest.TestCase):
    def test_exact_integer_first_return_is_not_equivariant(self):
        for n in range(1,6):
            S,D,F=swap(n),diagonal(n),first_return(n)
            self.assertEqual(mul(S,D),D)
            self.assertEqual(mul(F,D),identity(n))
            self.assertNotEqual(mul(F,S),F)

    def test_nonexistence_mod_two_and_even_characteristics(self):
        for n in (1,2,3,4,5):
            for m in (2,4,6,8,10,14,16,18):
                d=verify_chart_obstruction(n,m)
                self.assertFalse(d["two_is_unit"])
                self.assertFalse(d["symmetric_return_exists"])
                self.assertIsNone(symmetric_return_mod(n,m))

    def test_unique_symmetric_retraction_scalar_mod_m(self):
        for m in range(2,26):
            valid=[a for a in range(m) if (2*a)%m==1]
            expected=[] if m%2==0 else [pow(2,-1,m)]
            self.assertEqual(valid,expected)
            self.assertEqual(symmetric_return_mod(1,m) is not None,m%2==1)

    def test_odd_prime_and_crt_fibers(self):
        for n in (1,2,3,4):
            for ell in (3,5,7,11,13):
                result=verify_chart_obstruction(n,ell)
                self.assertTrue(result["symmetric_return_exists"])
                self.assertEqual((2*result["inverse_two"])%ell,1)
        # R/14 is a product of char-2 and char-7 fibers. It is not a
        # field and does NOT inherit the F7 chart retraction.
        self.assertIsNone(symmetric_return_mod(2,14))
        self.assertIsNotNone(symmetric_return_mod(2,7))
        self.assertIsNone(symmetric_return_mod(2,2))

    def test_norm_differential_and_nonnormalized_projectors(self):
        for n in (1,2,3,4):
            N,D=two_chart_norm(n),two_chart_difference(n)
            S=swap(n);I=identity(2*n)
            self.assertEqual(mul(N,N),scale(N,2))
            self.assertEqual(mul(D,D),scale(D,2))
            self.assertEqual(mul(N,D),scale(I,0))
            self.assertEqual(mul(D,N),scale(I,0))
            N2=mod(N,2)
            self.assertNotEqual(N2,mod(scale(I,0),2))
            self.assertEqual(mul(N2,N2,2),mod(scale(I,0),2))
            N7=mod(scale(N,4),7)
            D7=mod(scale(D,4),7)
            self.assertEqual(mul(N7,N7,7),N7)
            self.assertEqual(mul(D7,D7,7),D7)
            self.assertEqual(mul(N7,D7,7),mod(scale(I,0),7))
            self.assertEqual(mod(add(N7,D7),7),mod(I,7))

    def test_actual_ordinary_z_source_gram_no_new_binary_val(self):
        cases=[
            (7,((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1)),2,2,2),
            (11,((1,0),(0,1),(2,1),(-1,1)),2,3,1),
            (19,((0,0),(1,0),(0,1),(-1,2)),3,2,2),
        ]
        for D,Q,J,R,S in cases:
            B=original_integer_trace_gram(Q,D,J,R,S)
            pulled=single_chart_gram_pullback(B)
            self.assertEqual(pulled,scale(B,2))
            n=len(B)
            self.assertEqual(determinant(pulled),2**n*determinant(B))
            self.assertEqual(len(pulled),n)
            self.assertNotEqual(B,pulled)

    def test_nontrivial_integral_gram_evenness_does_not_repair_return(self):
        B=((2,0),(0,6))
        self.assertEqual(single_chart_gram_pullback(B),((4,0),(0,12)))
        self.assertIsNone(symmetric_return_mod(2,2))
        # Even Gram entries DO NOT give an integral 1/2 linear return.

    def test_sign_module_cohomology_parity_obstruction(self):
        outcome=quotient_invariants_c2()
        self.assertEqual(outcome["H1_sign_C2"],"Z/2Z")
        # The underlying extension can split as Z modules (first
        # projection), but not as Z[C2] modules (no equivariant return).
        self.assertEqual(mul(first_return(1),diagonal(1)),identity(1))
        self.assertNotEqual(mul(first_return(1),swap(1)),first_return(1))


class BraidVersusChartExchangeControls(unittest.TestCase):
    def test_actual_hurwitz_crossing_is_not_always_plain_swap(self):
        G=S3_GROUP
        differing=[
            (x,y) for x in G.members for y in G.members
            if hurwitz_positive(x,y,G)!=(y,x)
        ]
        self.assertGreater(len(differing),0)
        # The phase330 swap no-go is a C2-chart symmetry theorem,
        # not a theorem that every nonabelian braid admits no action.

    def test_abelian_or_commuting_braid_specialization_equals_swap(self):
        G=S3_GROUP
        for x in G.members:
            for y in G.members:
                if G.mul(x,y)==G.mul(y,x):
                    self.assertEqual(hurwitz_positive(x,y,G),(y,x))


if __name__=="__main__":
    unittest.main(verbosity=2)
