import Std

/-! Pure natural-number checker. No number-field imports or machine-word
arithmetic: a bit at t records that t is a negative square residue. -/
namespace TenthDiscriminant
set_option autoImplicit false

def residueBits : List Nat → Nat
  | [] => 0
  | r::rs => (2^r) ||| residueBits rs

def negativeSquareMask (p : Nat) : Nat :=
  residueBits ((List.range p).map (fun r => (p-(r*r)%p)%p))

def maskRootTest (d p mask : Nat) : Bool := mask.testBit (d%p)

def maskGuardedTest (d p mask : Nat) : Bool :=
  if 4*p≤d then !maskRootTest d p mask else true

def maskTests (d : Nat) (entries : List (Nat×Nat)) : Bool :=
  entries.all (fun e => maskGuardedTest d e.1 e.2)

def maskWheelMod : List (Nat×Nat) → Nat
  | [] => 8
  | e::es => maskWheelMod es*e.1

def maskWheelResidues : List (Nat×Nat) → List Nat
  | [] => [3]
  | e::es =>
    ((List.range e.1).flatMap (fun k =>
      (maskWheelResidues es).map (fun r => r+maskWheelMod es*k))).filter
      (fun d => !maskRootTest d e.1 e.2)

/-- A single wheel translate, filtered against the original global bounds.
True is only a finite checker result, not a coverage assertion. -/
def maskTranslateClear (rs : List Nat) (period lo hi k : Nat)
    (entries : List (Nat×Nat)) : Bool :=
  rs.all (fun r =>
    let d := r+period*k
    if lo≤d ∧ d<hi then !maskTests d entries else true)

end TenthDiscriminant
