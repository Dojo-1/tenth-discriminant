import unittest
from dataclasses import replace
from fractions import Fraction as Q
import random
import sympy as sp
from transport import Poly,Frame,Record,admit,transport,canonicalize,oracle_value,Z,W,distance,ball_feature,Runner

class TransportTests(unittest.TestCase):
    def setUp(self):
        self.f=Poly.make([(2,0,1),(0,1,-1)])
        self.root=Record(self.f,2,((Q(1),Q(-4)),))
    def test_invalid_input_shapes(self):
        for terms in ([(-1,0,1)],[(0,0,0.1)],[(0,0,True)]):
            with self.assertRaises(ValueError):Poly.make(terms)
        for capacity in (0,-1,1.5):
            with self.assertRaises(ValueError):Runner('canonical_lru',None,capacity)
    def test_root_admission(self):
        self.assertEqual(admit(self.root),1)
    def test_general_scaling_formula(self):
        t=Frame(Q(-2),Q(3),Q(4),Q(2),Q(-5));g=t.apply(self.f)
        samples=transport(self.root,g,t)
        self.assertEqual(samples[0][1],oracle_value(g,samples[0][0]))
        self.assertEqual(t.factor(2),Q(-648))
    def test_noncommutation(self):
        scale=Frame(u=Q(2));shift=Frame(h=Q(1))
        self.assertNotEqual(scale.then(shift).apply(self.f),shift.then(scale).apply(self.f))
    def test_composition_and_inverse(self):
        rng=random.Random(3701)
        for _ in range(60):
            make=lambda: Frame(Q(rng.choice((-2,-1,1,3)),2),Q(rng.choice((-2,1,2))),Q(rng.randint(-3,3),2),Q(rng.choice((-1,1,3))),Q(rng.randint(-3,3)))
            x,y,z=make(),make(),make()
            self.assertEqual(y.apply(x.apply(self.f)),x.then(y).apply(self.f))
            self.assertEqual(x.inverse().apply(x.apply(self.f)),self.f)
            self.assertEqual(x.then(y).then(z),x.then(y.then(z)))
    def test_canonical_orbits(self):
        rng=random.Random(3702)
        for i in range(80):
            a,b=2+i%3,1+i%2
            f=Poly.make([(a,b,1),(a,0,2),(1,0,3),(0,0,rng.randint(1,19))])
            t=Frame(Q(rng.choice((-3,1,2)),3),h=Q(rng.randint(-5,5),2),b=Q(rng.randint(-5,5),3))
            n,back,s=canonicalize(f);m,back2,s2=canonicalize(t.apply(f))
            self.assertTrue(s and s2);self.assertEqual(n,m)
            self.assertEqual(back.apply(n),f);self.assertEqual(back2.apply(m),t.apply(f))
    def test_unsupported_is_not_invented(self):
        n,t,s=canonicalize(self.f)
        self.assertFalse(s);self.assertEqual(n,self.f);self.assertEqual(t,Frame())
    def test_zero_scale(self):
        for kw in ({'scale':Q(0)},{'u':Q(0)},{'v':Q(0)}):
            with self.assertRaises(ValueError):Frame(**kw)
    def test_tiny_nonzero(self):
        t=Frame(scale=Q(1,10**30));g=t.apply(self.f)
        sample=transport(self.root,g,t)[0]
        self.assertNotEqual(sample[1],0);self.assertEqual(oracle_value(g,sample[0]),sample[1])
    def test_forged_witness(self):
        with self.assertRaises(ValueError):admit(replace(self.root,samples=((Q(1),Q(1)),)))
    def test_padded_degree(self):
        with self.assertRaises(ValueError):admit(replace(self.root,degree=3))
    def test_wrong_regime(self):
        for kw in ({'field':'F3'},{'derivative':'hasse'}):
            with self.assertRaises(ValueError):admit(replace(self.root,**kw))
    def test_wrong_target(self):
        changed=Poly.make(self.f.terms+((0,0,Q(1)),))
        with self.assertRaises(ValueError):transport(self.root,changed,Frame())
    def test_source_change(self):
        bad=replace(self.root,source=Poly.make([(2,0,1),(0,1,-2)]))
        with self.assertRaises(ValueError):admit(bad)
    def test_zero_record_not_nonzero(self):
        repeated=Poly.make([(2,0,1)]);r=Record(repeated,2,((Q(1),Q(0)),))
        self.assertEqual(admit(r),1)
        t=Frame(h=Q(3));self.assertEqual(transport(r,t.apply(repeated),t)[0][1],0)
    def test_degree_loss_keeps_fixed_size(self):
        f=Poly.make([(2,1,1),(1,0,1),(0,0,1)])
        self.assertEqual(oracle_value(f,Q(0)),0)
        self.assertEqual(sp.resultant(Z+1,sp.S.One,Z),1)
    def test_empty_and_duplicate_samples(self):
        for samples in ((),((Q(1),Q(0)),(Q(1),Q(0)))):
            with self.assertRaises(ValueError):admit(replace(self.root,samples=samples))
    def test_exact_general_transport_fuzz(self):
        rng=random.Random(3703)
        for i in range(36):
            a=2+i%3
            p=Poly.make([(a,1,1),(a,0,2),(1,0,rng.randint(1,5)),(0,1,-1),(0,0,3)])
            t=Frame(Q(rng.choice((-2,1,3)),2),Q(rng.choice((-1,1,2))),Q(rng.randint(-2,2)),Q(rng.choice((-2,1,3))),Q(rng.randint(-2,2)))
            w=Q(rng.randint(-3,3),2)
            self.assertEqual(oracle_value(t.apply(p),t.map_point(w)),t.factor(a)*oracle_value(p,w))
    def test_geometry_has_no_certificate_authority(self):
        x=ball_feature(self.f);y=ball_feature(Poly.make([(3,0,1),(0,1,-1)]))
        self.assertEqual(distance(x,x,True),0)
        self.assertGreaterEqual(distance(x,y,True),0)
        with self.assertRaises(ValueError):transport(replace(self.root,field='unknown'),self.f,Frame())
    def test_nontrivial_rescaling_order(self):
        t=Frame(scale=Q(2),u=Q(3));bad=replace(self.root,samples=((Q(1),Q(0)),))
        with self.assertRaises(ValueError):admit(bad)
        self.assertNotEqual(t.factor(2),t.scale**3)

if __name__=='__main__':unittest.main()
