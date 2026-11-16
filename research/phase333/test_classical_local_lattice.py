"""Phase333: exact lattice/index-two and unchanged ordinary-jet controls.

Independent integer computation, not a universal proof or field theorem.
The source sample nodes, derivative direction, original rank and positive
trace metric are held fixed. Odd moduli include composite prime powers;
the even counterexample is required to fail the false equivalence.
"""
import math
import unittest


def to_maximal(a):
    x, y = a
    return x - y, 2*y


def original_trace(d, a, b):
    return 2*(a[0]*b[0] + d*a[1]*b[1])


def maximal_trace(d, a, b):
    assert d % 2 == 1
    return (2*a[0]*b[0] + a[0]*b[1] + a[1]*b[0]
            + ((d+1)//2)*a[1]*b[1])


def divides_pair(q, a):
    return a[0] % q == 0 and a[1] % q == 0


def pair_mul(d, a, b):
    x, y = a
    u, v = b
    return x*u - d*y*v, x*v + y*u


def pair_pow(d, a, n):
    t = (1, 0)
    for _ in range(n):
        t = pair_mul(d, t, a)
    return t


def jet(d, r, s, j, a):
    if j > r:
        return (0, 0)
    falling = math.factorial(r)//math.factorial(r-j)
    b = pair_mul(d, pair_pow(d, a, r-j),
                 pair_pow(d, (a[0], -a[1]), s))
    return (falling*b[0], falling*b[1])


def gram_entry(d, q, jmax, left, right, metric):
    total = 0
    for j in range(jmax):
        for a in q:
            v = jet(d, *left, j, a)
            w = jet(d, *right, j, a)
            if metric is maximal_trace:
                v, w = to_maximal(v), to_maximal(w)
            total += metric(d, v, w)
    return total


class ClassicalLocalLatticeTests(unittest.TestCase):
    def test_inclusion_has_exact_parity_image(self):
        for x in range(-12, 13):
            for b in range(-12, 13):
                # The maximal coordinate (x,b) is in the image iff b is even.
                self.assertEqual(b % 2 == 0,
                                 to_maximal((x+b//2, b//2)) == (x,b))

    def test_trace_pairing_for_all_small_values(self):
        for d in (3, 7, 11, 19, 43, 163):
            nodes = [(x, y) for x in range(-4, 5) for y in range(-4, 5)]
            for a in nodes:
                for b in nodes:
                    self.assertEqual(original_trace(d, a, b),
                                     maximal_trace(d, to_maximal(a), to_maximal(b)))

    def test_odd_moduli_preserve_coordinate_divisibility(self):
        for q in (1, 3, 5, 7, 9, 11, 25, 27, 49, 81, 125):
            for x in range(-150, 151):
                for y in (-125,-81,-27,-13,-9,-3,-1,0,1,3,9,13,27,81,125):
                    a = (x, y)
                    self.assertEqual(divides_pair(q, a),
                                     divides_pair(q, to_maximal(a)))

    def test_binary_non_equivalence_and_one_step_loss(self):
        a = (1,1)
        self.assertTrue(divides_pair(2, to_maximal(a)))
        self.assertFalse(divides_pair(2, a))
        for q in (2,4,8,16,32,64):
            for x in range(-65, 66):
                for y in range(-65, 66):
                    a = (x,y)
                    if divides_pair(q, to_maximal(a)):
                        self.assertTrue(divides_pair(q//2, a))
        # A false claim that 2O-divisibility implies 2L-divisibility
        # must never become a valid test expectation.
        self.assertNotEqual(divides_pair(2, (1,1)),
                            divides_pair(2, to_maximal((1,1))))

    def test_original_jet_gram_unchanged_after_coordinate_transport(self):
        nodes = ((0,1), (1,1), (2,-1))
        rows = ((0,0), (0,1), (1,0), (1,1), (2,0), (2,1))
        for d in (3,7,163):
            for left in rows:
                for right in rows:
                    self.assertEqual(
                        gram_entry(d,nodes,2,left,right,original_trace),
                        gram_entry(d,nodes,2,left,right,maximal_trace))


if __name__ == "__main__":
    unittest.main(verbosity=2)
