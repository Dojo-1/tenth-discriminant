#!/usr/bin/env python3
"""Phase329 braid, quandle, and matched-null Frobenius controls."""
from __future__ import annotations

import random
import unittest

from braid_frobenius import (
    S3_GROUP, TOY_H48, H, S3, full_inert_coset,
    q_conjugate, q_inverse_conjugate,
    hurwitz_positive, hurwitz_negative,
    braid_generator, braid_word, group_product,
    are_conjugate, closure_coloring_count,
    two_strand_alexander, alexander_eval,
)


class ReidemeisterQuandleTests(unittest.TestCase):
    def test_finite_groups_verified(self):
        self.assertTrue(S3_GROUP.validate())
        self.assertTrue(TOY_H48.validate())

    def test_quandle_reidemeister_one_two_three(self):
        # Reidemeister I: idempotency; II: invertibility of right
        # translation; III: right self-distributivity.
        for G in (S3_GROUP,TOY_H48):
            for x in G.members:
                self.assertEqual(q_conjugate(x,x,G),x)
                for y in G.members:
                    self.assertEqual(
                        q_inverse_conjugate(q_conjugate(x,y,G),y,G),x)
                    self.assertEqual(
                        q_conjugate(q_inverse_conjugate(x,y,G),y,G),x)
                    for z in G.members:
                        self.assertEqual(
                            q_conjugate(q_conjugate(x,y,G),z,G),
                            q_conjugate(
                                q_conjugate(x,z,G),
                                q_conjugate(y,z,G),G))

    def test_hurwitz_inverse_and_product_invariance(self):
        for G in (S3_GROUP,TOY_H48):
            for x in G.members:
                for y in G.members:
                    new=hurwitz_positive(x,y,G)
                    self.assertEqual(hurwitz_negative(*new,G),(x,y))
                    self.assertEqual(
                        hurwitz_positive(*hurwitz_negative(x,y,G),G),
                        (x,y))
                    self.assertEqual(group_product((x,y),G),
                                     group_product(new,G))
                    self.assertTrue(are_conjugate(x,new[0],G) or
                                    are_conjugate(y,new[0],G))

    def test_braid_yang_baxter_for_all_H48_triples(self):
        G=TOY_H48
        n=0
        for x in G.members:
            for y in G.members:
                for z in G.members:
                    source=(x,y,z)
                    self.assertEqual(
                        braid_word(source,(1,2,1),G),
                        braid_word(source,(2,1,2),G))
                    n+=1
        self.assertEqual(n,48**3)

    def test_negative_crossing_undoes_positive(self):
        G=TOY_H48
        for x in G.members:
            for y in G.members:
                self.assertEqual(
                    braid_word((x,y),(1,-1,1),G),
                    braid_word((x,y),(1,),G))
        with self.assertRaises(ValueError):
            braid_word((G.unit,G.unit),(0,),G)


class ColoredKnotAndFrobeniusTests(unittest.TestCase):
    def test_S3_discriminates_trefoil_from_unknot(self):
        unknot=closure_coloring_count(S3_GROUP,1)
        trefoil=closure_coloring_count(S3_GROUP,3)
        self.assertEqual(unknot["fixed_colorings"],6)
        self.assertEqual(trefoil["fixed_colorings"],12)
        self.assertEqual(trefoil["nonconstant_colorings"],6)
        self.assertEqual(unknot["nonconstant_colorings"],0)

    def test_toy_ray_H48_has_blind_spot(self):
        # Critical matched null: using a larger group is NOT
        # automatically a better knot detector.
        unknot=closure_coloring_count(TOY_H48,1)
        trefoil=closure_coloring_count(TOY_H48,3)
        self.assertEqual(unknot["fixed_colorings"],48)
        self.assertEqual(trefoil["fixed_colorings"],48)
        self.assertEqual(trefoil["nonconstant_colorings"],0)
        inert=full_inert_coset()
        self.assertEqual(len(inert),24)
        self.assertEqual(
            closure_coloring_count(TOY_H48,1,inert)["fixed_colorings"],24)
        self.assertEqual(
            closure_coloring_count(TOY_H48,3,inert)["fixed_colorings"],24)

    def test_frobenius_inert_sector_stays_typed_under_braids(self):
        G=TOY_H48
        inert=full_inert_coset()
        n=0
        for x in inert:
            for y in inert:
                u,v=hurwitz_positive(x,y,G)
                self.assertEqual(u[1],1)
                self.assertEqual(v[1],1)
                self.assertEqual(group_product((x,y),G),
                                 group_product((u,v),G))
                # Inert Frobenius square is central for this H,
                # and conjugating a component preserves its square.
                self.assertEqual(G.mul(x,x),G.mul(v,v))
                self.assertEqual(G.mul(y,y),G.mul(u,u))
                n+=1
        self.assertEqual(n,24**2)

    def test_alexander_polynomial_independent_invariant(self):
        # Reduced Burau 2-braid formula for odd positive exponents.
        self.assertEqual(two_strand_alexander(1),(1,))
        self.assertEqual(two_strand_alexander(3),(1,-1,1))
        self.assertEqual(two_strand_alexander(5),(1,-1,1,-1,1))
        self.assertEqual(alexander_eval(two_strand_alexander(1),-1),1)
        self.assertEqual(alexander_eval(two_strand_alexander(3),-1),3)
        self.assertEqual(alexander_eval(two_strand_alexander(5),-1),5)
        self.assertNotEqual(two_strand_alexander(1),
                            two_strand_alexander(3))
        with self.assertRaises(ValueError):
            two_strand_alexander(2)
        with self.assertRaises(ValueError):
            closure_coloring_count(S3_GROUP,0)


if __name__=="__main__":
    unittest.main(verbosity=2)
