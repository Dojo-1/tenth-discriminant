#!/usr/bin/env python3
"""Phase327 exact two-360 ACAF/anti-ambiguity harness.

This tests a concrete signed quaternionic coefficient shadow.
It DOES NOT simulate all rational rotations or construct the full
ray-class field, integral jet action, or discriminant theorem.
"""
import random
import unittest

from interleaved_f1_prime import (
    ONE, ZERO, NEG_ONE, I, J, K, BASIS, Q8,
    FrobeniusPrime, CoefficientPrime, RayConductor,
    add, scale, product, conjugate, norm, scalar_inner,
    reduce_mod, product_mod, power, moving_frame,
    quaternion_basis_product, small_group_algebra_product,
    crt_2_7, semisimple_group_algebra_characteristic,
    typed_prime_context, two_full_turn_spin_signs,
    orthogonal_half_turn_word_counts,
)


class Phase327Two360AndSignedOne(unittest.TestCase):
    def test_exact_two_full_turns(self):
        self.assertEqual(two_full_turn_spin_signs(),
                         (NEG_ONE, NEG_ONE, ONE, ONE))
        self.assertEqual(product(NEG_ONE, NEG_ONE), ONE)
        self.assertEqual(product(NEG_ONE, I), product(I, NEG_ONE))

    def test_orthogonal_half_turns_and_spin_commutator(self):
        self.assertEqual(norm(I), 1)
        self.assertEqual(norm(J), 1)
        self.assertEqual(scalar_inner(I, J), 0)
        self.assertEqual(product(I, J), K)
        self.assertEqual(product(J, I), scale(-1, K))
        commutator = product(
            product(product(I, J), conjugate(I)), conjugate(J))
        self.assertEqual(commutator, NEG_ONE)
        self.assertNotEqual(commutator, ONE)

    def test_full_360_by_360_exact_orthogonal_anti_ambiguity(self):
        result = orthogonal_half_turn_word_counts()
        self.assertEqual(result["pairs"], 129600)
        self.assertEqual(result["anticommuting_pairs"], 32400)
        self.assertEqual(result["commuting_pairs"], 97200)
        print("PHASE327_360_BY_360_SWEEP", result, flush=True)

    def test_double_moving_frame_preserves_order_but_adjoint_loses_spin_sign(self):
        rng = random.Random(720327)
        for _ in range(256):
            a = tuple(rng.randint(-6, 6) for _ in range(4))
            u, v = Q8[rng.randrange(8)], Q8[rng.randrange(8)]
            self.assertEqual(
                moving_frame(u, moving_frame(v, a)),
                moving_frame(product(u, v), a))
            self.assertEqual(moving_frame(NEG_ONE, a), a)
            self.assertEqual(product(NEG_ONE, a), scale(-1, a))
        # A 360-degree lift is -1 in the spinor module, but its
        # SO3/adjoint-frame action is the identity. They are not the
        # same representation even in characteristic zero.
        self.assertEqual(moving_frame(NEG_ONE, I), I)
        self.assertNotEqual(product(NEG_ONE, I), I)

    def test_orthogonal_random_imaginary_vectors_anticommute(self):
        rng = random.Random(360360)
        examined = 0
        for _ in range(2048):
            x, y, z = (rng.randint(-9, 9) for _ in range(3))
            if x == y == 0:
                continue
            a, b = (0, x, y, z), (0, -y, x, 0)
            self.assertEqual(scalar_inner(a, b), 0)
            self.assertEqual(product(a, b), scale(-1, product(b, a)))
            self.assertEqual(
                reduce_mod(product(a, b), 2),
                reduce_mod(product(b, a), 2))
            examined += 1
        self.assertGreater(examined, 2000)

    def test_characteristic_two_kills_scalar_sign_and_has_nilpotents(self):
        self.assertNotEqual(product(I, J), product(J, I))
        self.assertEqual(product_mod(I, J, 2), product_mod(J, I, 2))
        self.assertNotEqual(product_mod(I, J, 7), product_mod(J, I, 7))
        # (1+i)^2=2i over Z; it becomes a genuine zero-product in F2.
        e = add(ONE, I)
        self.assertNotEqual(reduce_mod(e, 2), ZERO)
        self.assertEqual(product_mod(e, e, 2), ZERO)
        self.assertNotEqual(product_mod(e, e, 7), ZERO)
        self.assertEqual(reduce_mod(NEG_ONE, 2), reduce_mod(ONE, 2))
        self.assertNotEqual(reduce_mod(NEG_ONE, 7), reduce_mod(ONE, 7))

    def test_moving_frame_covariance_and_prime_reduction(self):
        rng = random.Random(327360)
        cases = 0
        for _ in range(512):
            a = tuple(rng.randint(-7, 7) for _ in range(4))
            b = tuple(rng.randint(-7, 7) for _ in range(4))
            u = Q8[rng.randrange(len(Q8))]
            ua, ub = moving_frame(u, a), moving_frame(u, b)
            self.assertEqual(norm(ua), norm(a))
            self.assertEqual(scalar_inner(ua, ub), scalar_inner(a, b))
            self.assertEqual(
                moving_frame(u, product(a, b)),
                product(ua, ub))
            for ell in (2, 3, 5, 7, 11):
                self.assertEqual(
                    reduce_mod(product(a, b), ell),
                    product_mod(reduce_mod(a, ell),
                                reduce_mod(b, ell), ell))
                self.assertEqual(
                    reduce_mod(moving_frame(u, a), ell),
                    product_mod(
                        product_mod(reduce_mod(u, ell),
                                    reduce_mod(a, ell), ell),
                        reduce_mod(conjugate(u), ell), ell))
            cases += 1
        self.assertEqual(cases, 512)

    def test_crt_interleaving_is_product_ring_not_field(self):
        for value in range(-100, 101):
            x = crt_2_7(value, value)
            self.assertEqual(x, value % 14)
            self.assertEqual(x % 2, value % 2)
            self.assertEqual(x % 7, value % 7)
        # Z/14 is not a field: nonzero 7 and 8 multiply to zero.
        self.assertNotEqual(7 % 14, 0)
        self.assertNotEqual(8 % 14, 0)
        self.assertEqual((7 * 8) % 14, 0)
        rng = random.Random(147)
        for _ in range(512):
            a = tuple(rng.randint(-20, 20) for _ in range(4))
            b = tuple(rng.randint(-20, 20) for _ in range(4))
            ab = product(a, b)
            self.assertEqual(
                tuple(crt_2_7(x, x) for x in ab),
                tuple(x % 14 for x in ab))
            for ell in (2, 7):
                self.assertEqual(product_mod(a, b, ell),
                                 reduce_mod(ab, ell))

    def test_cyclic_one_generator_over_toy_group_shadow(self):
        for n in (2, 3, 5):
            omega = {(0, 0): 1}
            for a in range(4):
                for g in range(n):
                    basis_vector = {(a, g): 1}
                    self.assertEqual(
                        small_group_algebra_product(
                            basis_vector, omega, n), basis_vector)
                    self.assertEqual(
                        small_group_algebra_product(
                            omega, basis_vector, n), basis_vector)
            # Exact associative multiplication on randomly selected
            # sums; this is the C_n shadow, not the actual H_D.
            rng = random.Random(360 + n)
            for _ in range(128):
                terms = []
                for _j in range(3):
                    v = {}
                    for _k in range(3):
                        label = (rng.randrange(4), rng.randrange(n))
                        v[label] = v.get(label, 0) + rng.choice([-2, -1, 1, 2])
                    terms.append(v)
                a, b, c = terms
                xy = small_group_algebra_product(a, b, n)
                yz = small_group_algebra_product(b, c, n)
                self.assertEqual(
                    small_group_algebra_product(xy, c, n),
                    small_group_algebra_product(a, yz, n))
                for ell in (2, 7):
                    a7 = small_group_algebra_product(a, b, n, ell)
                    reduced = {k: v % ell for k, v in xy.items()
                               if v % ell}
                    self.assertEqual(a7, reduced)

    def test_maschke_regime_controls_not_new_fields(self):
        expected = {2: False, 3: False, 5: False,
                    7: True, 11: True}
        for D in (163, 187, 203):
            for ell, good in expected.items():
                self.assertEqual(
                    semisimple_group_algebra_characteristic(
                        D, CoefficientPrime(ell)), good)

    def test_three_distinct_prime_roles_are_typed(self):
        m = RayConductor(125)
        self.assertEqual(
            typed_prime_context(
                FrobeniusPrime(2), CoefficientPrime(7), m, 163),
            (2, 7, 125))
        # ell=2 does NOT change the arithmetic rational prime p=7.
        self.assertEqual(
            typed_prime_context(
                FrobeniusPrime(7), CoefficientPrime(2), m, 163),
            (7, 2, 125))
        self.assertNotEqual(FrobeniusPrime(2), CoefficientPrime(2))
        with self.assertRaises(ValueError):
            typed_prime_context(
                FrobeniusPrime(5), CoefficientPrime(7), m, 163)
        with self.assertRaises(ValueError):
            typed_prime_context(
                FrobeniusPrime(163), CoefficientPrime(7), m, 163)
        with self.assertRaises(TypeError):
            typed_prime_context(CoefficientPrime(2),
                                FrobeniusPrime(7), m, 163)
        with self.assertRaises(ValueError):
            CoefficientPrime(1)

    def test_frobenius_two_signed_order_is_separate_from_coefficient_two(self):
        residue = 1
        order = None
        for t in range(1, 126):
            residue = (residue * 2) % 125
            if residue in (1, 124):
                order = t
                break
        self.assertEqual(order, 50)
        self.assertEqual(residue, 124)  # -1 in ray conductor 125
        # In coefficient characteristic two the scalar -1 equals +1;
        # neither this fact nor CRT changes the signed ray-class order.
        self.assertEqual(-1 % 2, 1 % 2)
        self.assertNotEqual(-1 % 7, 1 % 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
