#!/usr/bin/env python3
"""Phase328 tapestry controls; no inferred new bound or field theory."""
import random
import unittest

from tapestry import (
    G,H,HE,NODES,EDGES,REQUIRED_315,
    g_add,sigma,h_mul,h_conjugate,
    tensor_multiply,frobenius_square_from_inert_lift,
    validate_tapestry,eligible_to_claim_315,sample_tapestry,
    H_ONE,H_NEG_ONE,Q8,
)


class TapestryExactAlgebraTests(unittest.TestCase):
    def test_toy_norm_twist_not_equivalent_to_inversion(self):
        g=(1,1)
        self.assertEqual(sigma(g),(3,1))
        self.assertNotEqual(sigma(g),(3,5))
        square=frobenius_square_from_inert_lift(g)
        self.assertEqual(square,((0,2),0))
        self.assertNotEqual(square,HE)
        self.assertEqual(h_mul((g,1),(g,1)),square)

    def test_h_finite_semidirect_group_exact_associativity(self):
        self.assertEqual(len(G),24)
        self.assertEqual(len(H),48)
        self.assertEqual(len(set(H)),48)
        for a in H:
            self.assertEqual(h_mul(a,HE),a)
            self.assertEqual(h_mul(HE,a),a)
            for b in H:
                for c in H:
                    self.assertEqual(h_mul(h_mul(a,b),c),
                                     h_mul(a,h_mul(b,c)))

    def test_frobenius_square_central_without_frob_being_central(self):
        for g in G:
            f=(g,1)
            square=h_mul(f,f)
            self.assertEqual(square,(g_add(g,sigma(g)),0))
            for h in H:
                self.assertEqual(h_conjugate(h,square),square)
        self.assertNotEqual(
            h_conjugate(((1,0),0),((1,1),1)),((1,1),1))

    def test_external_quaternion_and_frobenius_actions_commute(self):
        for u in Q8:
            for h in H:
                self.assertEqual(
                    tensor_multiply((u,HE),(H_ONE,h)),
                    tensor_multiply((H_ONE,h),(u,HE)))
                self.assertEqual(
                    tensor_multiply((u,HE),(H_NEG_ONE,h)),
                    tensor_multiply((H_NEG_ONE,h),(u,HE)))
        # This commuting product does NOT give an action on the
        # unchanged integer jet lattice.

    def test_tensor_product_associativity_under_random_words(self):
        rng=random.Random(328328)
        for _ in range(2048):
            a=(Q8[rng.randrange(8)],H[rng.randrange(48)])
            b=(Q8[rng.randrange(8)],H[rng.randrange(48)])
            c=(Q8[rng.randrange(8)],H[rng.randrange(48)])
            self.assertEqual(
                tensor_multiply(tensor_multiply(a,b),c),
                tensor_multiply(a,tensor_multiply(b,c)))

    def test_sample_tapestry_returns_exact_original_determinant(self):
        x=sample_tapestry()
        self.assertEqual(x["toy_semidirect_order"],48)
        self.assertEqual(x["toy_inert_frob_square"],((0,2),0))
        self.assertEqual(x["source_D"],7)
        self.assertEqual(x["source_dimension"],4)
        self.assertEqual(x["original_determinant"],
                         x["stabilized_moving_determinant"])
        self.assertTrue(x["tensor_actions_commute"])
        self.assertFalse(x["claimed_315_bound"])


class TapestryEvidenceGateTests(unittest.TestCase):
    def test_typed_graph_no_dangling_edges(self):
        validate_tapestry()
        names={node.name for node in NODES}
        self.assertEqual(len(names),len(NODES))
        self.assertGreaterEqual(len(EDGES),15)
        self.assertIn("integral_moving_gram_return",names)
        self.assertIn("315_field_uniform_bound",names)
        self.assertIn("global_one_element_gluing",names)

    def test_exact_return_does_not_remove_315_obligations(self):
        # No amount of finite test success on the stabilized frame
        # discharges the existing original-jet or field theorem gates.
        self.assertFalse(eligible_to_claim_315({}))
        self.assertFalse(eligible_to_claim_315({
            "integral_moving_gram_return":True,
            "rational_frobenius_classes":True,
            "exact_conductor_characters":True,
        }))
        for missing in REQUIRED_315:
            other={name:True for name in REQUIRED_315 if name!=missing}
            self.assertFalse(eligible_to_claim_315(other))
        # Logical sufficiency of booleans is NOT independent evidence
        # that the corresponding mathematical statements are proved.
        self.assertTrue(eligible_to_claim_315(
            {name:True for name in REQUIRED_315}))

    def test_parity_glued_weave_is_typed_not_an_unproved_ray_action(self):
        nodes={node.name:node.status for node in NODES}
        edges={(e.source,e.target):e.kind for e in EDGES}
        self.assertEqual(nodes["parity_glued_two_chart_weave"],"finite")
        self.assertEqual(nodes["q8_integral_woven_intertwiner"],"finite")
        self.assertEqual(nodes["symmetric_integral_one_chart_descent"],"rejected")
        self.assertEqual(
            edges[("stabilized_quaternionic_jet","parity_glued_two_chart_weave")],"exact")
        self.assertEqual(
            edges[("parity_glued_two_chart_weave","q8_integral_woven_intertwiner")],"exact")
        self.assertEqual(
            edges[("parity_glued_two_chart_weave","symmetric_integral_one_chart_descent")],"blocked")
        self.assertEqual(
            edges[("coefficient_characteristic_2","parity_glued_two_chart_weave")],"forgetful")
        self.assertEqual(nodes["integral_ray_action_original_jet"],"open")
        self.assertFalse(eligible_to_claim_315({
            "q8_integral_woven_intertwiner":True,
            "parity_glued_two_chart_weave":True,
        }))

    def test_no_fake_prime_field_or_invented_jet_equivariance(self):
        edge_classes={(e.source,e.target):e.kind for e in EDGES}
        self.assertEqual(edge_classes[
            ("coefficient_characteristic_2","original_integer_jet_gram")],
            "blocked")
        self.assertEqual(edge_classes[
            ("norm_twisted_representations","integral_ray_action_original_jet")],
            "blocked")
        self.assertEqual(edge_classes[
            ("integral_moving_gram_return","315_field_uniform_bound")],
            "blocked")
        self.assertEqual(edge_classes[
            ("stabilized_quaternionic_jet","integral_moving_gram_return")],
            "exact")
        self.assertEqual(next(n.status for n in NODES
                             if n.name=="F1_signed_monoid"),"semantic")


if __name__=="__main__":
    unittest.main(verbosity=2)
