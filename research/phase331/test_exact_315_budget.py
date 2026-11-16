"""Phase331 independent exact-rational endpoint and source-mass audit.

No use of class number one classification and NO claim to prove
the field theorem. Computes integer floor masses in closed form
at the declared original 315^4 rectangle. Lean must prove the
quantified source-to-normalization bridge separately.

Source constants are copied from explicitly named checked Lean
certificates; these finite tests are M evidence, not a replacement.
"""
from __future__ import annotations
from fractions import Fraction as F
import unittest

PRIMES_10=(7,11,13,17,19,23,29,31,37,41)
ENDPOINT=315**4
R=ENDPOINT//4
S=R//25
LOG2_LOWER=F(6931,10000)
LOG3_LOWER=F(1098,1000)
LOG5_LOWER=F(1609,1000)
LOG_TEN_LOWER=F(189,100)
NEW_BINARY_TARGET=F(6931,1000000)
NEW_ODD_TARGET=F(873747,250000000)


def floor_mass(q:int,s:int)->int:
    """Sum_{t=0}^{s-1} floor(t/q), exact quotient-remainder formula."""
    if q<1 or s<0:
        raise ValueError((q,s))
    n,t=divmod(s,q)
    return q*n*(n-1)//2+n*t


def binary_gain_lower(R:int,S:int)->F:
    """Certified by joint original-source exponent, log 2 lower."""
    return F(2*floor_mass(4,S),R*S)*LOG2_LOWER


def odd_ten_gain_lower(R:int,S:int)->F:
    """Use ten selected local Frobenius masses, each with log p>=1.89."""
    return F(2*sum(floor_mass(p*p,S) for p in PRIMES_10),R*S)*LOG_TEN_LOWER


def three_five_gain_lower(R:int,S:int)->F:
    return F(2*(1098*floor_mass(9,S)+1609*floor_mass(25,S)),1000*R*S)


def full_endpoint_exact_margin()->F:
    return ((F(999997,1000000)-F(4,5))*F(230096,10000)
            -F(57193,10000)+F(1853,2000)+LOG2_LOWER/4
            +three_five_gain_lower(R,S)
            +binary_gain_lower(R,S)
            +odd_ten_gain_lower(R,S))


class SourceExactEndpointTests(unittest.TestCase):
    def test_original_endpoint_dimensions(self):
        self.assertEqual(ENDPOINT,9845600625)
        self.assertEqual(R,2461400156)
        self.assertEqual(S,98456006)
        self.assertEqual(R-25*S,6)
        self.assertEqual(len(PRIMES_10),10)

    def test_floor_mass_closed_form_against_direct_small_sum(self):
        for q in (1,2,4,9,25,49,121,1681):
            for n in range(0,300):
                self.assertEqual(floor_mass(q,n),
                                 sum(t//q for t in range(n)))

    def test_floor_mass_lemma_all_ten_primes_at_endpoint(self):
        for p in PRIMES_10:
            q=p*p
            f=floor_mass(q,S)
            self.assertLessEqual(S*S,2*q*f+(2*q-1)*S)
        self.assertLessEqual(R*S,200*floor_mass(4,S)+200*S)

    def test_conservative_normalized_binary_gain(self):
        self.assertGreaterEqual(
            binary_gain_lower(R,S),
            NEW_BINARY_TARGET-F(2,R))
        self.assertLess(
            binary_gain_lower(R,S),F(7,1000))

    def test_conservative_normalized_ten_odd_prime_gain(self):
        self.assertGreaterEqual(
            odd_ten_gain_lower(R,S),
            NEW_ODD_TARGET-F(40,R))
        self.assertGreater(odd_ten_gain_lower(R,S),F(3497,1000000))

    def test_existing_three_five_mass_certificate_at_endpoint(self):
        self.assertGreaterEqual(
            three_five_gain_lower(R,S),
            F(4659,625000)-F(16895455,625000*ENDPOINT))

    def test_published_conditional_scalar_margin_exact(self):
        published=((F(999997,1000000)-F(4,5))*F(230096,10000)
                   -F(57193,10000)+F(1853,2000)+F(6931,40000)
                   +F(4659,625000)-F(16895455,625000*ENDPOINT)
                   +NEW_BINARY_TARGET+NEW_ODD_TARGET-F(450,R))
        self.assertEqual(
            published,
            F(2498202070590058939787,12116981457144348750000000))
        self.assertGreater(published,F(1,5000))

    def test_exact_endpoint_mass_margin_is_positive(self):
        # A pointwise rational pilot; the all-D Lean field theorem
        # still requires monotonized floor rounding, source positivity,
        # finite-prime log transport and the exact analytic upper.
        gap=full_endpoint_exact_margin()
        self.assertGreater(gap,F(1,5000))

    def test_negative_no_gains_does_not_close(self):
        baseline=((F(999997,1000000)-F(4,5))*F(230096,10000)
                  -F(57193,10000)+F(1853,2000)+LOG2_LOWER/4)
        self.assertLess(baseline,0)
        self.assertLess(baseline+three_five_gain_lower(R,S),0)


if __name__=="__main__":
    unittest.main(verbosity=2)
