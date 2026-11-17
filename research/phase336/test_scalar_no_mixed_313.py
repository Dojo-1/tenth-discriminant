"""Phase336 exact controls: stronger 313^4 radius and scalar separation.

No floating-point approximations are accepted as proof. Conservative
rational log/error bounds are identical to the Lean proof target.
The numerical test checks formulas, not the missing actual-source
Hadamard upper or prime lower at the 313 domain.

Critical counterfactual: with NO mixed source H factor and the OLD
1/10 Hadamard saving, the conservative 313 scalar gap is negative.
"""
from fractions import Fraction as F
import unittest

def conservative_no_mixed_gap():
    logD = F(22984,1000)              # proven lower log(313^4)
    log2 = F(6931,10000)             # proven lower log 2
    discrepancy = F(999997,1000000) - F(4,5)
    return (discrepancy*logD
            -F(57193,10000)
            +F(1923,2000)           # stronger original upper constant
            +log2/4
            +F(4659,625000)
            +F(6931,1000000)
            +F(873747,250000000)
            -F(1,100000)            # D denominator bound
            -F(1,1000000))          # 42/R denominator bound

def radii_exact_at_fourth_power(n):
    t=n**3
    thin=(11*t+24)//25
    padded=(13*t+24)//25
    return thin,padded

class Strong313WithoutMixedTests(unittest.TestCase):
    def test_conservative_gap_is_positive_without_H(self):
        gap=conservative_no_mixed_gap()
        self.assertGreater(gap,F(29,1000))
        self.assertLess(gap,F(31,1000))

    def test_old_radius_saving_does_not_separate(self):
        # Without mixed H, changing -1923/2000 to -1853/2000
        # costs 70/2000 = 0.035, killing the 313 scalar separation.
        old_gap=conservative_no_mixed_gap()-F(70,2000)
        self.assertLess(old_gap,0)
        self.assertGreater(old_gap,-F(1,100))

    def test_exact_integer_ceiling_radius_ratio(self):
        for n in list(range(313,352))+[375,450,1000,2026]:
            thin,padded=radii_exact_at_fourth_power(n)
            self.assertGreater(thin,0)
            self.assertLess(thin,padded)
            self.assertLessEqual(20*thin,17*padded)

    def test_313_endpoint_root_and_dimensions(self):
        d=313**4
        self.assertEqual(d,9597924961)
        r=d//4
        s=r//25
        self.assertGreaterEqual(r,100000000)
        self.assertGreaterEqual(s,500000)
        self.assertLessEqual(25*s,r)
        self.assertLessEqual(r,26*s)

if __name__=="__main__":
    unittest.main(verbosity=2)
