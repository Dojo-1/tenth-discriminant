#!/usr/bin/env python3
"""Phase306-C exact controls: quantum-mathematical states only, no device."""
import unittest
from fractions import Fraction

import arithmetic_fabric as a
import quantum_sandbox as q


class QuantumSandboxControls(unittest.TestCase):
    def test_bell_schmidt_entanglement_vs_product(self):
        bell = q.bell_like(5)
        product = q.product_state(5)
        self.assertEqual(q.schmidt_rank(bell), 5)
        self.assertEqual(q.schmidt_rank(product), 1)
        self.assertEqual(q.reduced_purity(bell), Fraction(1, 5))
        self.assertEqual(q.reduced_purity(product), Fraction(1, 1))

    def test_local_permutation_preserves_bipartite_entanglement(self):
        bell = q.bell_like(5)
        # Local unitary: a permutation on just the first factor.
        permuted = (bell[1], bell[0], bell[2], bell[3], bell[4])
        self.assertEqual(q.schmidt_rank(permuted), 5)
        self.assertEqual(q.reduced_purity(permuted), Fraction(1, 5))
        # A noninvertible local map is NOT unitary: it may destroy entanglement.
        projected = ((1, 0, 0, 0, 0),) + ((0, 0, 0, 0, 0),) * 4
        self.assertEqual(q.schmidt_rank(projected), 1)

    def test_barrier_mediated_second_order_witness_and_no_coupling(self):
        coupled = q.tight_binding_barrier(g=1, barrier=7)
        blocked = q.tight_binding_barrier(g=0, barrier=7)
        self.assertEqual(q.transition_second_order_coefficient(coupled),
                         Fraction(-1, 2))
        self.assertEqual(q.transition_second_order_coefficient(blocked), 0)
        # Second-order coefficient by itself is independent of barrier energy:
        # it CANNOT be promoted into a tunneling-rate comparison.
        self.assertEqual(q.transition_second_order_coefficient(coupled),
                         q.transition_second_order_coefficient(
                             q.tight_binding_barrier(g=1, barrier=100)))

    def test_adiabatic_avoided_crossing_gap_and_hostile_closed_gap(self):
        eps = Fraction(1, 10)
        self.assertEqual(q.avoided_crossing_gap_squared(0, eps),
                         Fraction(1, 25))
        for s in (Fraction(-1), Fraction(-1, 2), Fraction(0),
                  Fraction(1, 2), Fraction(1)):
            self.assertGreaterEqual(q.avoided_crossing_gap_squared(s, eps),
                                    q.avoided_crossing_gap_squared(0, eps))
        self.assertEqual(q.avoided_crossing_gap_squared(0, 0), 0)
        with self.assertRaises(ValueError):
            q.adiabatic_scale_proxy(0, 100)
        self.assertEqual(q.adiabatic_scale_proxy(eps, 100),
                         Fraction(1, 4))

    def test_quantum_module_does_not_change_original_field_gram(self):
        e = a.exact_original_jet_rows(a.actual_d203_points(),
                                       degrees=(0, 1, 2), jets=2, d=203)
        g_before = a.trace_gram(e, 203)
        _ = (q.bell_like(5), q.reduced_purity(q.bell_like(5)),
             q.tight_binding_barrier(1, 7),
             q.adiabatic_scale_proxy(Fraction(1, 10), 100))
        self.assertEqual(a.trace_gram(e, 203), g_before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
