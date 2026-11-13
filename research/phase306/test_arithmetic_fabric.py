#!/usr/bin/env python3
"""Phase306 exact bounded tests, including deliberately hostile controls."""
import json
import unittest
from pathlib import Path

import arithmetic_fabric as f


U = ((1, 2, 0), (0, 1, -1), (0, 0, 1))
V = ((1, 0, 0), (1, 1, 0), (0, 0, 1))


class Phase306ArithmeticFabricTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.points = f.actual_d203_points()
        cls.E = f.exact_original_jet_rows(cls.points, degrees=(0, 1, 2), jets=2, d=203)
        cls.G = f.trace_gram(cls.E, 203)

    def test_actual_original_source_not_fabricated(self):
        self.assertEqual((len(self.points), len(self.E), len(self.E[0])), (6, 3, 24))
        self.assertEqual(self.G, f.transpose(self.G))
        self.assertGreater(f.det(self.G), 0)
        self.assertEqual(self.E[0][:12], (1, 0) * 6)
        self.assertEqual(self.E[0][12:], (0, 0) * 6)
        self.assertTrue(all(f.omega_norm(z, 203) <= 576 for z in self.points))

    def test_integral_gauge_source_and_gram(self):
        for u in (U, V, f.mmul(U, V), f.mmul(V, U)):
            with self.subTest(u=u):
                self.assertEqual(f.det(u), 1)
                inv = f.inverse_unimodular(u)
                self.assertEqual(f.mmul(u, inv), f.eye(3))
                moved, predicted, d0, d1 = f.gram_covariance(u, self.E)
                self.assertEqual(moved, predicted)
                self.assertEqual(d0, d1)
        # Noncommuting moving frames: composition order is observable.
        self.assertNotEqual(f.mmul(U, V), f.mmul(V, U))
        self.assertEqual(f.mmul(f.mmul(U, V), f.inverse_unimodular(f.mmul(U, V))), f.eye(3))
        self.assertNotEqual(f.mmul(f.mmul(U, V), f.inverse_unimodular(f.mmul(V, U))), f.eye(3))

    def test_bad_gauge_rejected_not_decorative(self):
        bad = ((2, 0, 0), (0, 1, 0), (0, 0, 1))
        with self.assertRaises(f.TransportError):
            f.gram_covariance(bad, self.E)
        moved, _, _, _ = f.gram_covariance(U, self.E)
        self.assertNotEqual(moved, self.G)  # Covariance is not entrywise invariance.

    def test_padic_basechange_functor_and_type_boundary(self):
        for k in (1, 2):
            c = f.Cage(203, 5, k, "original.D203.Zr.j01")
            a, b = f.transport_functor(U, self.E, c)
            self.assertEqual(a, b)
        with self.assertRaises(f.TransportError):
            f.transport_functor(U, self.E, f.Cage(203, 5, 2, "source"),
                                f.Cage(203, 5, 1, "source"))
        with self.assertRaises(f.TransportError):
            f.transport_functor(U, self.E, f.Cage(203, 5, 2, "source"),
                                f.Cage(187, 5, 2, "source"))

    def test_high_dimensional_symplectic_lift_and_hamiltonian_pairing(self):
        lift = f.cotangent_lift(U)
        self.assertEqual(len(lift), 6)
        self.assertEqual(f.symplectic_defect(lift, 25), f.mod_matrix(f.eye(6), 25)
                         if False else f.matrix([[0] * 6 for _ in range(6)]))
        q, pi = (2, 3, 1), (1, 0, 4)
        transported = f.matvec(lift, q + pi)
        self.assertEqual(f.dual_pair(q, pi, 25),
                         f.dual_pair(transported[:3], transported[3:], 25))
        self.assertNotEqual(f.symplectic_defect(f.block_diag(U, U), 25),
                            f.matrix([[0] * 6 for _ in range(6)]))

    def test_heisenberg_central_2cocycle_not_fake_quantum(self):
        x = (1, 0, 0, 0, 0, 0)
        y = (0, 0, 0, 1, 0, 0)
        z = (1, 1, 0, 0, 0, 1)
        self.assertNotEqual(f.phase_cocycle(x, y), f.phase_cocycle(y, x))
        self.assertEqual(f.cocycle_defect(x, y, z), 0)
        a, b, c = (x, 2), (y, 3), (z, 4)
        self.assertEqual(f.heisenberg_product(f.heisenberg_product(a, b), c),
                         f.heisenberg_product(a, f.heisenberg_product(b, c)))
        self.assertNotEqual(f.heisenberg_product(a, b), f.heisenberg_product(b, a))
        # Nonbilinear fake phase fails the cocycle identity.
        def wrong_cocycle(t, u):
            return t[0] * u[0] * u[0] % 5
        t = (1, 0, 0, 0, 0, 0)
        bad = (wrong_cocycle(t, t) + wrong_cocycle(f.phase_add(t, t), t)
               - wrong_cocycle(t, t) - wrong_cocycle(t, f.phase_add(t, t))) % 5
        self.assertNotEqual(bad, 0)

    def test_sheaf_glue_on_actual_observation_cover_and_hostile_overlap(self):
        universe = [f"q{i}" for i in range(len(self.points))]
        values = dict(zip(universe, (a % 25 for a, _ in self.points)))
        def section(ids):
            return f.LocalSection(25, tuple((k, values[k]) for k in ids))
        a = section(("q0", "q1", "q2"))
        b = section(("q2", "q3", "q4"))
        c = section(("q4", "q5", "q0"))
        self.assertEqual(f.glue_sections((a, b, c), universe), values)
        changed_b = f.LocalSection(25, (("q2", (values["q2"] + 1) % 25),
                                         ("q3", values["q3"]), ("q4", values["q4"])))
        with self.assertRaises(f.GluingObstruction):
            f.glue_sections((a, changed_b, c), universe)
        with self.assertRaises(f.GluingObstruction):
            f.glue_sections((a, f.LocalSection(5, (("q2", values["q2"] % 5),)), c), universe)
        with self.assertRaises(f.GluingObstruction):
            f.glue_sections((a, b), universe)

    def test_holoportive_crt_has_real_information_remainder(self):
        integer = 123456
        r = f.crt_pair(integer % 25, 25, integer % 49, 49)
        self.assertEqual(r.modulus, 1225)
        self.assertEqual(r.residue, integer % 1225)
        self.assertEqual(r.residue % 25, integer % 25)
        self.assertEqual(r.residue % 49, integer % 49)
        self.assertNotEqual(r.residue, integer)
        self.assertEqual(f.crt_pair((integer+1225) % 25, 25,
                                    (integer+1225) % 49, 49), r)
        self.assertEqual(r.remainder_type, "unknown-integer-multiple-of-modulus")
        with self.assertRaises(f.TransportError):
            f.crt_pair(1, 25, 2, 5)

    def test_godelian_open_reminder_not_self_certification(self):
        claim = f.Claim("D203_source_v5", "crgs-author", "M", "source_measurement", "pinned_sha")
        forged = f.Attestation("crgs-author", "formal_kernel", "fake-link")
        with self.assertRaises(f.PromotionDenied):
            f.promote_proved(claim, forged)
        forged_other = f.Attestation("other-model", "formal_kernel", "fake-link")
        with self.assertRaises(f.PromotionDenied):
            f.promote_proved(claim, forged_other)
        theorem = f.Claim("open_field_bridge", "crgs-author", "H", "formal_theorem", "pinned_sha")
        with self.assertRaises(f.PromotionDenied):
            f.promote_proved(theorem, forged)
        with self.assertRaises(f.PromotionDenied):
            f.promote_proved(theorem, f.Attestation("reviewer", "self_test", "fake-link"))

    def test_hyperbolic_context_tree_zero_four_point_defect(self):
        t = f.fixed_context_tree()
        self.assertTrue(f.all_tree_quadruples_zero(t))
        self.assertGreater(t.distance("source.jets", "field.D163"), 0)
        self.assertNotEqual(t.distance("source.jets", "precision.k1"), 0)
        with self.assertRaises(f.TransportError):
            f.ContextTree({"a": "b", "b": "a"})

    def test_manifest_nonflat_honest_evidence_governance(self):
        j = json.loads((Path(__file__).parent / "worldlet_manifest.json").read_text())
        self.assertGreaterEqual(len(j["worldlets"]), 5)
        self.assertEqual(len(j["qualities"]), 16)
        self.assertGreaterEqual(len(j["clocks"]), 2)
        self.assertGreaterEqual(len(j["identity"]["local_holonomies"]), 2)
        self.assertTrue(all("return_transport" in t and "remainder" in t
                            for t in j["tendrils"]))
        self.assertIn("performance-and-field-bridge",
                      {x["claim_id"] for x in j["evidence"] if x["status"] == "H"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
