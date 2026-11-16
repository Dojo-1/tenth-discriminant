"""Phase335 independent exact-integer controls for conductor-sensitive jet filtrations.

The observation set and derivative operator are unchanged:
  ∂^j_Z Z^r W^s evaluated at z=x+y*sqrt(-D), w=conj(z),
with W held constant while differentiating. Maximal-order coordinates
are used only as a representation of the SAME computed source values.

No field bound, original-Gram determinant improvement or additional
2-adic factor is inferred from these finite controls.
"""
import math
import unittest


def pair_mul(d,a,b):
    return a[0]*b[0]-d*a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def pair_pow(d,a,n):
    out=(1,0)
    while n:
        if n&1:
            out=pair_mul(d,out,a)
        a=pair_mul(d,a,a)
        n//=2
    return out


def pair_sub(a,b):
    return a[0]-b[0], a[1]-b[1]


def original_ordinary_jet(d,r,s,j,a):
    if j>r:
        return (0,0)
    f=math.factorial(r)//math.factorial(r-j)
    z=pair_pow(d,a,r-j)
    w=pair_pow(d,(a[0],-a[1]),s)
    z=pair_mul(d,z,w)
    return (f*z[0],f*z[1])


def integer_polynomial_jet(d, terms, j, a):
    """Original finite linear combination of Z^r W^s ordinary jets.

    terms holds triples (r,s,integer coefficient); W is held fixed
    throughout the derivative. No change of samples or metric.
    """
    re=im=0
    for r,s,c in terms:
        v=original_ordinary_jet(d,r,s,j,a)
        re+=c*v[0]
        im+=c*v[1]
    return re,im


def source_h_jet(d,j,a):
    return pair_sub(original_ordinary_jet(d,2,0,j,a),
                    original_ordinary_jet(d,0,2,j,a))


def to_maximal(a):
    return a[0]-a[1],2*a[1]


def maximal_mul(d,a,b):
    assert d%4==3
    return a[0]*b[0]-((d+1)//4)*a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1]


def maximal_pow(d,a,n):
    out=(1,0)
    for _ in range(n):
        out=maximal_mul(d,out,a)
    return out


def maximal_h_omega(d):
    w=(0,1)
    bar_w=(1,-1)
    return pair_sub(maximal_pow(d,w,2),maximal_pow(d,bar_w,2))


def divisible(q,a):
    return a[0]%q==0 and a[1]%q==0


class ConductorSensitiveJets(unittest.TestCase):
    def test_exact_H_value_and_ordinary_jets(self):
        count=0
        for d in (3,7,11,19,43,163):
            for x in range(-5,6):
                for y in range(-5,6):
                    a=(x,y)
                    self.assertEqual(source_h_jet(d,0,a),(0,4*x*y))
                    self.assertEqual(source_h_jet(d,1,a),(2*x,2*y))
                    self.assertEqual(source_h_jet(d,2,a),(2,0))
                    for j in range(3,8):
                        self.assertEqual(source_h_jet(d,j,a),(0,0))
                    self.assertTrue(divisible(4,source_h_jet(d,0,a)))
                    for j in range(8):
                        self.assertTrue(divisible(2,source_h_jet(d,j,a)))
                    count+=1
        self.assertEqual(count,726)

    def test_sharp_first_and_second_jet_counterexamples(self):
        for j in (1,2):
            self.assertEqual(source_h_jet(3,j,(1,0)),(2,0))
            self.assertFalse(divisible(4,source_h_jet(3,j,(1,0))))
        # Correct row/derivative semantics are essential. Hasse
        # coefficients would not supply these j! factors.
        self.assertEqual(original_ordinary_jet(3,2,0,2,(1,0)),(2,0))

    def test_maximal_omega_binary_H_negative_all_D(self):
        for d in (3,7,11,19,43,163,203):
            self.assertEqual(maximal_h_omega(d),(-1,2))
            self.assertFalse(divisible(2,maximal_h_omega(d)))

    def test_nonzero_polynomial_H_in_source_two_filtration_not_four(self):
        # Coefficient vector (Z^2 - W^2) is NOT termwise even.
        # Its actual original evaluated jets nevertheless lie in 2L.
        h=((2,0,1),(0,2,-1))
        samples=((0,0),(1,0),(0,1),(1,1),(-1,2),(3,-1))
        for d in (3,7,163):
            for a in samples:
                for j in range(3):
                    v=integer_polynomial_jet(d,h,j,a)
                    self.assertEqual(v,source_h_jet(d,j,a))
                    self.assertTrue(divisible(2,v))
        self.assertFalse(divisible(
            4,integer_polynomial_jet(3,h,1,(1,0))))

    def test_coefficient_level_odd_and_binary_filters(self):
        # Test integer POLYNOMIALS, not the vacuous statement that
        # all original monomial rows are divisible by an odd modulus.
        coeffs=(
            ((2,0,1),(0,2,-1)),
            ((3,1,2),(1,2,-3),(0,0,1)),
            ((4,0,-2),(2,1,5),(0,2,-7),(1,0,3)),
            ((0,0,6),),
        )
        samples=((0,0),(1,0),(0,1),(1,1),(-1,2),(3,-1))
        for d in (3,7,163):
            for terms in coeffs:
                for j in range(4):
                    for a in samples:
                        v=integer_polynomial_jet(d,terms,j,a)
                        for q in (1,3,5,9,25,27,49,125):
                            self.assertEqual(
                                divisible(q,v),divisible(q,to_maximal(v)))
                        for k in range(1,6):
                            q=2**k
                            if divisible(2*q,to_maximal(v)):
                                self.assertTrue(divisible(q,v))
                            if divisible(2*q,v):
                                self.assertTrue(divisible(2*q,to_maximal(v)))
        for k in range(0,6):
            q=2**k
            # Polynomial P(Z,W)=Z at the singleton original source
            # sample (q,q), with J=1: this is a genuine coefficient-
            # vector filtration counterexample at level 2*q.
            v=integer_polynomial_jet(3,((1,0,1),),0,(q,q))
            self.assertEqual(v,(q,q))
            self.assertTrue(divisible(2*q,to_maximal(v)))
            self.assertFalse(divisible(2*q,v))

    def test_odd_local_filtrations_and_binary_loss(self):
        samples=((0,0),(1,0),(0,1),(1,1),(-1,2),(3,-1))
        rows=tuple((r,s) for r in range(5) for s in range(3))
        jets=[original_ordinary_jet(d,r,s,j,a)
              for d in (3,7,163)
              for r,s in rows
              for a in samples for j in range(3)]
        for q in (1,3,5,7,9,25,27,49,125):
            for a in jets:
                self.assertEqual(divisible(q,a),divisible(q,to_maximal(a)))
        for k in range(1,7):
            q=2**k
            for a in jets:
                if divisible(2*q,to_maximal(a)):
                    self.assertTrue(divisible(q,a))
                if divisible(2*q,a):
                    self.assertTrue(divisible(2*q,to_maximal(a)))
            # Sharpness for every k, independent of any specific jet:
            # (q,q) is not divisible by 2q, but its image (0,2q) is.
            witness=(q,q)
            self.assertFalse(divisible(2*q,witness))
            self.assertTrue(divisible(2*q,to_maximal(witness)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
