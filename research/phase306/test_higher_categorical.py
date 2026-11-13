#!/usr/bin/env python3
"""Phase306-B: actual original-source Hom and a separate topological 2-class."""
import unittest

import arithmetic_fabric as a
import higher_categorical as h


U = ((1, 2, 0), (0, 1, -1), (0, 0, 1))
V = ((1, 0, 0), (1, 1, 0), (0, 0, 1))


class Phase306HigherCategoricalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.points = a.actual_d203_points()
        cls.e = a.exact_original_jet_rows(cls.points, (0, 1, 2), 2, 203)
        cls.g = a.trace_gram(cls.e)

    def test_hom_profunctor_exact_composition_and_arithmetic_trace(self):
        f1, f2 = a.transpose(U), a.transpose(V)
        g1 = h.swap_complete_observation_points(p0=0, p1=1)
        g2 = h.swap_complete_observation_points(p0=2, p1=3)
        z = h.HomProfunctorElement(3, 24, a.transpose(self.e))
        sequential = z.pull_push(f1, g1).pull_push(f2, g2)
        composed = z.pull_push(a.mmul(f1, f2), a.mmul(g2, g1))
        self.assertEqual(sequential, composed)
        self.assertEqual(z.pull_push(a.eye(3), a.eye(24)), z)
        # Source frame U acts on rows; target-isometric point swap acts on columns.
        moved_source_rows = a.transpose(z.pull_push(f1, g1).linear_map)
        self.assertEqual(moved_source_rows, a.mmul(a.mmul(U, self.e), a.transpose(g1)))
        self.assertEqual(a.trace_gram(moved_source_rows),
                         a.mmul(a.mmul(U, self.g), a.transpose(U)))
        self.assertEqual(a.det(a.trace_gram(moved_source_rows)), a.det(self.g))

    def test_wrong_observation_map_and_wrong_arrow_types_fail(self):
        z = h.HomProfunctorElement(3, 24, a.transpose(self.e))
        with self.assertRaises(a.TransportError):
            z.pull_push(a.eye(4), a.eye(24))
        with self.assertRaises(a.TransportError):
            z.pull_push(a.eye(3), a.eye(23))
        wrong = h.wrong_half_fiber_swap()
        wrongly_moved_source_rows = a.transpose(z.pull_push(a.eye(3), wrong).linear_map)
        self.assertNotEqual(a.trace_gram(wrongly_moved_source_rows), self.g)

    def test_nontrivial_H2_on_separate_tetrahedral_sphere_nerve(self):
        sphere = h.tetrahedral_sphere_nerve()
        cycle = h.fundamental_sphere_cycle()
        self.assertEqual(h.boundary_of_two_chain(cycle), {})
        cocycle = {(1, 2, 3): 1}
        self.assertEqual(h.delta_two(cocycle, sphere), {})
        self.assertEqual(h.pair_cycle_cocycle(cycle, cocycle), 1)
        self.assertTrue(h.nontrivial_H2_certificate(cocycle, sphere))
        self.assertFalse(h.nontrivial_H2_certificate({}, sphere))

    def test_coboundary_null_and_filled_tetrahedron_counterworld(self):
        sphere = h.tetrahedral_sphere_nerve()
        edge_one = {(0, 1): 2, (0, 2): 3, (1, 3): 4}
        exact_two = h.delta_one(edge_one, sphere)
        self.assertEqual(h.pair_cycle_cocycle(h.fundamental_sphere_cycle(),
                                              exact_two), 0)
        self.assertFalse(h.nontrivial_H2_certificate(exact_two, sphere))
        filled = h.tetrahedral_sphere_nerve(fill_interior=True)
        bad = h.delta_two({(1, 2, 3): 1}, filled)
        self.assertEqual(bad, {(0, 1, 2, 3): 1})
        with self.assertRaises(a.TransportError):
            h.nontrivial_H2_certificate({(1, 2, 3): 1}, filled)

    def test_quaternion_noncommutative_but_associative_optional_fiber(self):
        i = h.Quaternion(0, 1, 0, 0)
        j = h.Quaternion(0, 0, 1, 0)
        k = h.Quaternion(0, 0, 0, 1)
        self.assertEqual(i.mul(j), k)
        self.assertEqual(j.mul(i), h.Quaternion(0, 0, 0, 4))
        one = h.Quaternion(1, 0, 0, 0)
        x = h.Quaternion(1, 2, 3, 4)
        y = h.Quaternion(3, 1, 0, 2)
        z = h.Quaternion(2, 0, 1, 1)
        self.assertEqual(x.mul(one).coords(), x.coords())
        self.assertEqual(x.mul(y).mul(z), x.mul(y.mul(z)))
        self.assertEqual(x.mul(x.conj()).coords(), (x.norm(), 0, 0, 0))
        self.assertEqual(x.mul(y).norm(), (x.norm() * y.norm()) % 5)
        # Matched arithmetic ablation: adding quaternion labels cannot affect G.
        self.assertEqual(a.trace_gram(self.e), self.g)


if __name__ == "__main__":
    unittest.main(verbosity=2)
