#!/usr/bin/env python3
"""Phase307-E: exact finite Smith depths and coherent precision transports.

This is a computational shadow of p-adic completion, NOT aleph_omega or
a construction of a genuinely transfinite arithmetic obstruction.
"""
from dataclasses import dataclass


class TransportRemainder(ValueError):
    pass


@dataclass(frozen=True)
class SmithDepth:
    elementary_exponents: tuple

    def __post_init__(self):
        if any(not isinstance(v,int) or v<0 for v in self.elementary_exponents):
            raise TransportRemainder("Smith exponents must be finite nonnegative integers")

    def kernel_log_at(self, n):
        if not isinstance(n,int) or n<0:
            raise TransportRemainder("finite precision n must be nonnegative")
        return sum(min(n, b) for b in self.elementary_exponents)

    def layer_at(self, n):
        if not isinstance(n,int) or n<1:
            raise TransportRemainder("layer starts at 1")
        return sum(b >= n for b in self.elementary_exponents)

    def finite_length(self):
        return sum(self.elementary_exponents)

    def verify_telescope(self):
        max_n=max(self.elementary_exponents,default=0)+2
        assert self.kernel_log_at(0)==0
        for n in range(1,max_n+1):
            assert self.kernel_log_at(n)-self.kernel_log_at(n-1)==self.layer_at(n)
        assert self.kernel_log_at(max_n)==self.finite_length()
        assert self.layer_at(max_n)==0
        return True


@dataclass(frozen=True)
class PrecisionWorldlet:
    """Typed residue of ONE original integer under one named source."""
    field_d: int
    prime: int
    level: int
    source_id: str
    residue: int

    def __post_init__(self):
        if self.field_d<=0 or self.prime<2 or self.level<1 or not self.source_id:
            raise TransportRemainder("invalid precision worldlet")
        if not 0<=self.residue<self.prime**self.level:
            raise TransportRemainder("residue not canonical")

    @classmethod
    def from_int(cls, field_d, prime, level, source_id, x):
        return cls(field_d,prime,level,source_id,x%(prime**level))

    def reduce(self, lower_level):
        if not 1<=lower_level<=self.level:
            raise TransportRemainder("cannot invert loss of higher p-adic digits")
        return PrecisionWorldlet(self.field_d,self.prime,lower_level,
                                 self.source_id,self.residue%(self.prime**lower_level))

    def compatible(self, finer):
        if (self.field_d,self.prime,self.source_id)!=(
            finer.field_d,finer.prime,finer.source_id):
            raise TransportRemainder("transport across unrelated source/field/prime")
        small=min(self.level,finer.level)
        return self.residue%(self.prime**small)==finer.residue%(self.prime**small)

    def roundtrip_integer_remainder(self, x):
        """No value of x can be recovered from residue alone."""
        if x%(self.prime**self.level)!=self.residue:
            raise TransportRemainder("integer not in the recorded residue class")
        return {"canonical_reconstruction":self.residue,
                "unrecovered_integer_multiple":(x-self.residue)//(self.prime**self.level),
                "typed_loss":"integer-multiple-of-prime-power",
                "hidden_without_integer_source":True}


@dataclass(frozen=True)
class GovernanceClock:
    """Finite source operation clock; independent review is a separate clock."""
    computational_step: int
    review_epoch: int

    def tick_source(self):
        return GovernanceClock(self.computational_step+1,self.review_epoch)

    def tick_review(self, verified_external_receipt=False):
        # A self-authored boolean is not evidence of an external peer witness.
        if not verified_external_receipt:
            return self
        raise TransportRemainder("external checker API not integrated; no automatic promotion")


def main():
    f=SmithDepth((0,)*50+(1,)*50)
    assert f.verify_telescope()
    assert f.kernel_log_at(1)==f.kernel_log_at(2)==50
    assert f.layer_at(1)==50 and f.layer_at(2)==0
    z=PrecisionWorldlet.from_int(203,5,5,"original-100-row",123456)
    for n in range(1,5):
        assert z.reduce(n)==PrecisionWorldlet.from_int(203,5,n,"original-100-row",123456)
        assert z.reduce(n).compatible(z)
    assert GovernanceClock(2,0).tick_source()==GovernanceClock(3,0)
    print("PHASE307_PRECISION_TOWER_PASS",{
        "finite_D203_source_smith_depth":50,
        "depth1":50,"depth2":0,
        "coherent_five_level_reductions":True,
        "aleph_omega_not_computed":True,"field_bound_not_improved":True
    },flush=True)


if __name__=="__main__":
    main()
