#!/usr/bin/env python3
"""Phase307-D: optional nonassociative octonion fiber over F5.

A verified algebraic associator adds a distinction absent in quaternions.
It is NOT an arithmetic class-group operator, AI mind quality, or physics.
"""
from dataclasses import dataclass
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase306"))
from higher_categorical import Quaternion

P=5
Z=Quaternion(0,0,0,0)
ONE=Quaternion(1,0,0,0)
I=Quaternion(0,1,0,0)
J=Quaternion(0,0,1,0)
K=Quaternion(0,0,0,1)


def qadd(a,b):
    return Quaternion(*((x+y)%P for x,y in zip(a.coords(),b.coords())))


def qneg(a):
    return Quaternion(*((-x)%P for x in a.coords()))


def qsub(a,b):
    return qadd(a,qneg(b))


@dataclass(frozen=True)
class Octonion:
    a: Quaternion
    b: Quaternion

    def mul(self,other):
        # (a,b)(c,d)=(ac-conj(d)b, da+b conj(c)).
        c,d=other.a,other.b
        return Octonion(qsub(self.a.mul(c),d.conj().mul(self.b)),
                        qadd(d.mul(self.a),self.b.mul(c.conj())))

    def add(self,other):
        return Octonion(qadd(self.a,other.a),qadd(self.b,other.b))

    def sub(self,other):
        return Octonion(qsub(self.a,other.a),qsub(self.b,other.b))

    def norm(self):
        return (self.a.norm()+self.b.norm())%P

    def coords(self):
        return self.a.coords()+self.b.coords()


def associator(x,y,z):
    return x.mul(y).mul(z).sub(x.mul(y.mul(z)))


def main():
    e1=Octonion(I,Z)
    e2=Octonion(J,Z)
    e4=Octonion(Z,ONE)
    witness=associator(e1,e2,e4)
    assert witness.coords()!=(0,)*8
    assert associator(e1,e1,e4).coords()==(0,)*8
    x=Octonion(Quaternion(1,2,3,4),Quaternion(0,1,1,3))
    y=Octonion(Quaternion(3,1,0,2),Quaternion(2,4,0,1))
    assert x.mul(y).norm()==(x.norm()*y.norm())%5
    print("PHASE307_OCTONION_OBSERVABLE_PASS",{
        "associator_e1_e2_e4":witness.coords(),
        "nonassociativity_detected":True,"alternative_control":True,
        "norm_multiplicative_control":True,
        "not_used_by_original_field_gram":True,
        "no_cognitive_or_physical_claim":True
    },flush=True)


if __name__=="__main__":
    main()
