import TenthDiscriminant.ResidueMaskCore

/-! A bit at k records a possible quotient in d=r+M*k. Natural-number
bitsets have no machine-word cutoff. Literal patterns need separate proofs. -/
namespace TenthDiscriminant
set_option autoImplicit false

structure QuotientPattern where
  modulus : Nat
  inverse : Nat
  wide : Nat
  deriving DecidableEq, Repr

def scaledNegativeMask (p a : Nat) : Nat :=
  residueBits ((List.range p).map (fun t => (p-(a*(t*t))%p)%p))

def scaledAllowedMask (p a : Nat) : Nat :=
  (2^p-1) ^^^ scaledNegativeMask p a

def periodicBits (p mask width : Nat) : Nat :=
  residueBits ((List.range width).filter (fun k => mask.testBit (k%p)))

def quotientWidePattern (p a : Nat) : Nat :=
  periodicBits p (scaledAllowedMask p a) (785+p)

def quotientBand (lo hi : Nat) : Nat := (2^(hi-lo)-1) <<< lo

def quotientInitial (r : Nat) : Nat :=
  quotientBand (if r<1000000 then 1 else 0) (if r<380759680 then 785 else 784)

def quotientFilter (r : Nat) : Nat → List QuotientPattern → Nat
  | current, [] => current
  | current, e::es =>
    if current=0 then 0
    else quotientFilter r (current &&& (e.wide >>> ((e.inverse*r)%e.modulus))) es

def quotientPatternCheck (M : Nat) (e : QuotientPattern) : Bool :=
  decide (0<e.modulus) && (M*e.inverse%e.modulus==1) &&
    (e.wide==quotientWidePattern e.modulus e.inverse)

def quotientPatternsCheck (M : Nat) (es : List QuotientPattern) : Bool :=
  es.all (quotientPatternCheck M)

end TenthDiscriminant
