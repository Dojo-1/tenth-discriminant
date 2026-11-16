"""Phase334 exact conductor-two controls on quadratic-order coordinate rings.

All arithmetic is over integer pairs. Binary reductions are taken only
after multiplication, not by replacing the source lattice or sample set.
"""
import unittest


def source_mul(d, a, b):
    x, y = a
    u, v = b
    return x*u-d*y*v, x*v+y*u


def maximal_mul(d, a, b):
    assert d % 4 == 3
    x, y = a
    u, v = b
    return x*u-((d+1)//4)*y*v, x*v+y*u+y*v


def source_to_maximal(a):
    return a[0]-a[1], 2*a[1]


def pow_pair(mul, d, a, n):
    out = (1,0)
    for _ in range(n):
        out = mul(d, out, a)
    return out


def sub(a,b):
    return a[0]-b[0], a[1]-b[1]


def mod2(a):
    return a[0]%2, a[1]%2


def all_pairs():
    return tuple((x,y) for x in (0,1) for y in (0,1))


class ConductorTwoTests(unittest.TestCase):
    def test_ring_inclusion_exact_for_small_source_pairs(self):
        samples = [(x,y) for x in range(-5,6) for y in range(-5,6)]
        for d in (3,7,11,19,43,163):
            for a in samples:
                for b in samples:
                    self.assertEqual(
                        source_to_maximal(source_mul(d,a,b)),
                        maximal_mul(d,source_to_maximal(a),source_to_maximal(b)))

    def test_source_mod_two_nonzero_nilpotent(self):
        epsilon = (1,1)
        self.assertNotEqual(mod2(epsilon),(0,0))
        for d in (3,7,11,19,43,163):
            self.assertEqual(mod2(source_mul(d,epsilon,epsilon)),(0,0))

    def test_every_source_value_satisfies_fourth_minus_square(self):
        for d in (3,7,11,19,43,163):
            for a in all_pairs():
                f = sub(pow_pair(source_mul,d,a,4),
                        pow_pair(source_mul,d,a,2))
                self.assertEqual(mod2(f),(0,0))

    def test_maximal_order_163_fails_source_polynomial(self):
        w=(0,1)
        f=sub(pow_pair(maximal_mul,163,w,4),
              pow_pair(maximal_mul,163,w,2))
        self.assertEqual(f,(1681,-82))
        self.assertEqual(mod2(f),(1,0))

    def test_maximal_163_residue_ring_is_a_field(self):
        # All three nonzero elements have multiplicative order dividing 3.
        for a in all_pairs():
            if a != (0,0):
                self.assertEqual(mod2(pow_pair(maximal_mul,163,a,3)),(1,0))

    def test_maximal_7_has_nontrivial_idempotent_but_no_nilpotents(self):
        w=(0,1)
        f=sub(pow_pair(maximal_mul,7,w,4),
              pow_pair(maximal_mul,7,w,2))
        self.assertEqual(f,(4,-4))
        self.assertEqual(mod2(f),(0,0))
        self.assertEqual(mod2(maximal_mul(7,w,w)),w)
        for a in all_pairs():
            if a!=(0,0):
                self.assertNotEqual(mod2(pow_pair(maximal_mul,7,a,2)),(0,0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
