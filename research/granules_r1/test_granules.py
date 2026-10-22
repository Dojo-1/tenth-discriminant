import random
import unittest
from fractions import Fraction as Q
import sympy as sp
from granules import *

class TestGranules(unittest.TestCase):
    def test_exact_degree_boundary(self):
        with self.assertRaises(ValueError): Target.of(Z**2-W,3)
        for e in [Q(1,10**12),Q(-1,10**12)]: Target.of(sp.Rational(e)*Z**3+Z**2-W,3)
    def test_zero_not_confidence(self):
        f=Z**2-W; t=Target.of(f,2)
        self.assertFalse(verify_nonzero_witness(f,Witness(t,Q(0),Q(0),'very-high-membership')))
    def test_good_and_forged_witness(self):
        f=Z**2-W; t=Target.of(f,2)
        self.assertTrue(verify_nonzero_witness(f,Witness(t,Q(1),Q(-4),'actual')))
        self.assertFalse(verify_nonzero_witness(f,Witness(t,Q(1),Q(4),'wrong-sign')))
    def test_target_mismatch(self):
        with self.assertRaises(ValueError):
            verify_nonzero_witness(Z**2-W,Witness(Target.of(Z**2+W,2),Q(1),Q(4),'wrong'))
    def test_repeated_factor(self):
        f=(Z**2-W)**2
        self.assertFalse(verify_nonzero_witness(f,Witness(Target.of(f,4),Q(1),Q(0),'repeated')))
    def test_zero_specialization(self):
        f=W*(Z**2-1)
        self.assertFalse(verify_nonzero_witness(f,Witness(Target.of(f,2),Q(0),Q(0),'vertical')))
    def test_negative_weights(self):
        with self.assertRaises(ValueError): blend_enclosures([Enclosure('t',Q(0),Q(1),'a')],[Q(-1)])
    def test_zero_total_hole(self):
        with self.assertRaises(ValueError): blend_enclosures([Enclosure('t',Q(0),Q(1),'a')],[Q(0)])
    def test_different_units_or_witnesses(self):
        with self.assertRaises(ValueError): blend_enclosures([Enclosure('t',Q(0),Q(1),'a'),Enclosure('u',Q(0),Q(1),'b')],[Q(1),Q(1)])
    def test_reversed(self):
        with self.assertRaises(ValueError): blend_enclosures([Enclosure('t',Q(2),Q(1),'a')],[Q(1)])
    def test_inconsistent_overlap(self):
        with self.assertRaises(ValueError): intersect_enclosures([Enclosure('t',Q(0),Q(1),'a'),Enclosure('t',Q(2),Q(3),'b')])
    def test_duplicate_provenance_not_extra_evidence(self):
        r=Enclosure('t',Q(1),Q(3),'same-source')
        out=intersect_enclosures([r,r])
        self.assertEqual((out.lower,out.upper),(r.lower,r.upper))
        self.assertEqual(out.provenance,'intersection:same-source')
    def test_distribution_not_membership(self):
        p=empirical_zplus([1,1,2,8],7)
        self.assertEqual(p['pmf'],{'1':'1/2','2':'1/4','8':'1/4'})
        self.assertEqual(p['fuzzy_event_mass'],'2/3')
    def test_empty_empirical_model_rejected(self):
        with self.assertRaises(ValueError): EmpiricalLocalModel.fit([],'unknown')
    def test_membership_rescaling(self):
        self.assertEqual(memberships([Q(0),Q(2),Q(1,1000)]),memberships([Q(0),Q(-6),Q(-3,1000)]))
    def test_uncertified_inputs_remain_conditional(self):
        # This algebraic API cannot know whether its caller proved the input bounds.
        out=blend_enclosures([Enclosure('t',Q(1),Q(2),'unverified')],[Q(1)])
        self.assertTrue(out.provenance.startswith('conditional-blend:'))
    def test_finite_property_and_metamorphic_campaign(self):
        rng=random.Random(2026102203)
        for _ in range(512):
            value=Q(rng.randint(-30,30),rng.randint(1,9))
            n=rng.randint(1,8)
            records=[Enclosure('t',value-Q(rng.randint(0,20),7),value+Q(rng.randint(0,20),11),str(i)) for i in range(n)]
            weights=[Q(rng.randint(1,20),13) for _ in records]
            b=blend_enclosures(records,weights); c=intersect_enclosures(records)
            self.assertLessEqual(b.lower,value); self.assertLessEqual(value,b.upper)
            self.assertLessEqual(b.lower,c.lower); self.assertLessEqual(c.upper,b.upper)
            rev=blend_enclosures(records[::-1],weights[::-1]); self.assertEqual(b,rev)
            scaled=blend_enclosures(records,[Q(7,3)*w for w in weights]); self.assertEqual(b,scaled)

if __name__=='__main__': unittest.main()
