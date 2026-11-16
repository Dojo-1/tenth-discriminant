#!/usr/bin/env python3
"""Phase329 independent knot trace and discriminant-linking tests."""
from __future__ import annotations

from fractions import Fraction
import random
import unittest

from arithmetic_knot_invariants import (
    determinantal_divisors, smith_invariant_factors, rational_inverse,
    linking_pair, discriminant_untie, braid_permutation_cycles,
    trace_braid_power,
)
from integral_unknot import (
    coupled_gram, source_dependent_coupling, vp,
)
from braid_frobenius import (
    S3_GROUP,TOY_H48,closure_coloring_count,full_inert_coset,
    two_strand_alexander,
)
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))
from stabilized_return import (
    original_integer_trace_gram,block_diag,identity,
    determinant,transpose,
)


class ExactArithmeticKnotObstructions(unittest.TestCase):
    def test_determinantal_divisors_and_Smith_form(self):
        B=((14,7),(7,14))
        self.assertEqual(determinantal_divisors(B),(1,7,147))
        self.assertEqual(smith_invariant_factors(B),(7,21))
        self.assertEqual(abs(determinant(B)),147)
        self.assertEqual(smith_invariant_factors(((12,),)),(12,))

    def test_coupled_gram_has_identical_cokernel_plus_trivial_aux(self):
        for B in (((12,),),((14,7),(7,14))):
            C=source_dependent_coupling(B)
            M=coupled_gram(B,C)
            n=len(B);m=len(C)
            # Exact Smith factors, rather than determinant only.
            factors=smith_invariant_factors(M)
            expected=(1,)*m+smith_invariant_factors(B)
            self.assertEqual(factors,expected)
            self.assertEqual(
                abs(determinant(M)),abs(determinant(B)))
            for p in (2,3,5,7,11):
                self.assertEqual(vp(determinant(M),p),
                                 vp(determinant(B),p))

    def test_rational_linking_form_under_integral_untie(self):
        B=((14,7),(7,14))
        self.assertEqual(linking_pair(B,(1,0),(1,0)),
                         Fraction(2,21))
        self.assertEqual(linking_pair(B,(1,0),(0,1)),
                         Fraction(20,21))
        C=source_dependent_coupling(B)
        n=len(B)+len(C)
        rng=random.Random(32921)
        for _ in range(32):
            x=tuple(rng.randint(-5,5) for _ in range(n))
            y=tuple(rng.randint(-5,5) for _ in range(n))
            r=discriminant_untie(B,C,x,y)
            self.assertEqual(r["coupled_pair"],r["decoupled_pair"])

    def test_noninvertible_discriminant_form_is_not_defined(self):
        B=((1,1),(1,1))
        with self.assertRaises(ValueError):
            smith_invariant_factors(B)
        with self.assertRaises(ValueError):
            rational_inverse(B)
        with self.assertRaises(ValueError):
            linking_pair(B,(1,0),(0,1))

    def test_actual_source_gram_arithmetic_invariants(self):
        Q=((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1))
        B=original_integer_trace_gram(Q,D=7,J=2,R=2,S=2)
        self.assertEqual(B,transpose(B))
        self.assertNotEqual(determinant(B),0)
        factors=smith_invariant_factors(B)
        self.assertEqual(abs(determinant(B)),
                         __import__("math").prod(factors))
        # This test does not attempt all rank-16 minors of the
        # coupled source; its determinant equality is independently
        # established by the Phase329 shear certificate.


class BraidIntegralOperatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows={G.name:braid_permutation_cycles(G)
                  for G in (S3_GROUP,TOY_H48)}
        import json
        print("PHASE329_BRAID_PERMUTATION_CYCLES",
              json.dumps(cls.rows,sort_keys=True),flush=True)

    def test_integral_braid_representation_unimodular(self):
        self.assertEqual(self.rows[S3_GROUP.name]["rank"],36)
        self.assertEqual(self.rows[TOY_H48.name]["rank"],2304)
        for data in self.rows.values():
            self.assertTrue(data["permutation_unique"])
            self.assertIn(data["determinant"],(-1,1))
            self.assertEqual(
                sum(int(k)*v for k,v in data["cycles"].items()),
                data["rank"])

    def test_trace_equals_closed_braid_knot_coloring(self):
        for G in (S3_GROUP,TOY_H48):
            data=self.rows[G.name]
            for odd_power in (1,3,5,7):
                self.assertEqual(
                    trace_braid_power(data,odd_power),
                    closure_coloring_count(G,odd_power)["fixed_colorings"])

    def test_knot_coloring_not_complete_even_with_2304_dimensions(self):
        toy=self.rows[TOY_H48.name]
        self.assertEqual(trace_braid_power(toy,1),
                         trace_braid_power(toy,3))
        self.assertNotEqual(two_strand_alexander(1),
                            two_strand_alexander(3))
        s3=self.rows[S3_GROUP.name]
        self.assertEqual(trace_braid_power(s3,1),6)
        self.assertEqual(trace_braid_power(s3,3),12)

    def test_no_prime_bound_inference_from_braid_trace(self):
        for g in (S3_GROUP,TOY_H48):
            data=self.rows[g.name]
            self.assertEqual(trace_braid_power(data,0),data["rank"])
            with self.assertRaises(ValueError):
                trace_braid_power(data,-1)
        # No character average nor L-function estimate is represented
        # by a finite braid permutation trace.


if __name__=="__main__":
    unittest.main(verbosity=2)
