"""Phase341: exact integer/rational threshold-307 feasibility and kill controls.

NOT a 307^4 field theorem, NOR a Lean proof of an analytic upper at 307.
It deliberately tests the false reuse of the 313-domain 78*cuberoot
lower bound and 521/78000 radius ratio.
"""
import unittest
from fractions import Fraction as F


def endpoint(n):
    d=n**4
    R=d//4
    S=R//25
    rho=(13*n**3+24)//25
    thin=(11*n**3+24)//25
    return d,R,S,rho,thin


def hypothetical_307_gap():
    # This substitutes an UNPROVED-for-307 certified-log candidate:
    # 4 * (5726/1000) = 22904/1000. Constants otherwise identical
    # to the verified 313 scalar theorem. No original Gram inference.
    log_floor=F(22904,1000)
    log2_floor=F(6931,10000)
    return (
        (F(999997,1000000)-F(4,5))*log_floor
        - F(57193,10000) + F(1923,2000)
        + log2_floor/4 + F(4659,625000)
        + F(6931,1000000) + F(873747,250000000)
        - F(1,100000) - F(1,1000000)
    )


class Threshold307Controls(unittest.TestCase):
    def test_original_cell_criterion_crosses_at_307(self):
        # (11/25 - (1001/1000)*(407/1000))*n - 10 >= 0
        # iff 32593*n >= 10_000_000.
        self.assertEqual(32593*306-10_000_000, -26542)
        self.assertEqual(32593*307-10_000_000, 6051)
        self.assertTrue(32593*307>=10_000_000)
        self.assertFalse(32593*306>=10_000_000)

    def test_exact_endpoint_original_dimensions(self):
        d,R,S,rho,thin=endpoint(307)
        self.assertEqual((d,R,S,rho,thin),
                         (8882874001,2220718500,88828740,15045911,12731155))
        self.assertGreater(rho,thin)
        self.assertGreater(R,25*S-1)
        self.assertLessEqual(25*S,R)

    def test_313_cubic_guard_is_FALSE_at_307(self):
        # Critical negative control: do not copy a valid 313 lemma.
        _,R,_,rho,_=endpoint(307)
        n=307
        self.assertEqual(R-78*n**3, -36168054)
        self.assertLess(R,78*n**3)
        self.assertEqual(R-76*n**3, 21700832)
        self.assertGreaterEqual(R,76*n**3)

    def test_old_313_radius_ratio_is_FALSE_at_307(self):
        _,R,_,rho,_=endpoint(307)
        # Expected rho/R <= 521/78000 at 313, but not at 307.
        self.assertEqual(521*R-78000*rho, -16586719500)
        self.assertGreater(78000*rho,521*R)
        # A weaker candidate from 76*cuberoot would succeed here.
        self.assertEqual(521*R-76000*rho, 13505102500)
        self.assertLessEqual(76000*rho,521*R)

    def test_scalar_margin_is_only_conditional(self):
        gap=hypothetical_307_gap()
        self.assertGreater(gap,F(14,1000))
        self.assertLess(gap,F(15,1000))
        old_radius_saving=gap-F(7,200)
        self.assertLess(old_radius_saving,0)
        self.assertGreater(old_radius_saving,-F(22,1000))


if __name__=="__main__":
    unittest.main(verbosity=2)
