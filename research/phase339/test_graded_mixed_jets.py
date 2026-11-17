"""Finite exact controls for Phase339 graded original ordinary-Z jets.
The universal statement is proved on paper, NOT in Lean here.
"""
import math
import unittest

def pairmul(d,a,b):
    return (a[0]*b[0]-d*a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def pairpow(d,a,n):
    z=(1,0)
    while n:
        if n&1: z=pairmul(d,z,a)
        a=pairmul(d,a,a)
        n//=2
    return z

def polynomial_mul(p,q):
    v={}
    for (r,s),x in p.items():
        for (t,u),y in q.items():
            k=(r+t,s+u)
            v[k]=v.get(k,0)+x*y
    return {k:x for k,x in v.items() if x}

def h_power_times_monomial(b,r,s):
    h={(2,0):1,(0,2):-1}
    p={(r,s):1}
    for _ in range(b): p=polynomial_mul(p,h)
    return p

def original_ordinary_jet(d,p,j,z):
    w=z[0],-z[1]
    acc=(0,0)
    for (r,s),c in p.items():
        if j>r: continue
        falling=math.factorial(r)//math.factorial(r-j)
        a=pairmul(d,pairpow(d,z,r-j),pairpow(d,w,s))
        acc=(acc[0]+c*falling*a[0],acc[1]+c*falling*a[1])
    return acc

def pairdivisible(m,z):
    return z[0]%m==0 and z[1]%m==0

class GradedOrdinaryJetTests(unittest.TestCase):
    def test_general_monomial_quotient(self):
        count=0
        for d in (3,7,163):
            for z in ((-2,1),(-1,-1),(0,0),(1,0),(1,1)):
                for b in range(6):
                    for r in range(4):
                        for s in range(3):
                            p=h_power_times_monomial(b,r,s)
                            for j in range(2*b+r+3):
                                v=original_ordinary_jet(d,p,j,z)
                                required=math.factorial(j)*2**max(0,2*b-j)
                                self.assertTrue(pairdivisible(required,v),
                                    (d,z,b,r,s,j,required,v))
                                count+=1
        self.assertGreater(count,5000)

    def test_exact_sharpness_witnesses(self):
        d=163
        self.assertEqual(original_ordinary_jet(d,h_power_times_monomial(1,0,0),0,(1,1)),(0,4))
        self.assertEqual(original_ordinary_jet(d,h_power_times_monomial(1,0,0),1,(1,0)),(2,0))
        self.assertEqual(original_ordinary_jet(d,h_power_times_monomial(1,0,0),2,(1,0)),(2,0))
        self.assertEqual(original_ordinary_jet(d,h_power_times_monomial(2,0,0),2,(1,0)),(8,0))
        self.assertFalse(pairdivisible(8,original_ordinary_jet(d,h_power_times_monomial(1,0,0),0,(1,1))))
        self.assertFalse(pairdivisible(4,original_ordinary_jet(d,h_power_times_monomial(1,0,0),1,(1,0))))

if __name__=='__main__':
    unittest.main(verbosity=2)
