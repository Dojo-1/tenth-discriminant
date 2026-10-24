import TenthDiscriminant.ResidueMaskCore

/-! A continuation visits a leaf without retaining the full wheel list.
The materialized counterpart exists only to state the correspondence. -/
namespace TenthDiscriminant
set_option autoImplicit false

def maskPrefixMod (m : Nat) : List (Nat×Nat) → Nat
  | [] => m
  | e::es => maskPrefixMod m es*e.1

def maskWheelLift (m : Nat) (rs : List Nat) (e : Nat×Nat) : List Nat :=
  ((List.range e.1).flatMap (fun k => rs.map (fun r => r+m*k))).filter
    (fun d => !maskRootTest d e.1 e.2)

def maskWheelFromList : List (Nat×Nat) → Nat → List Nat → List Nat
  | [], _, rs => rs
  | e::es, m, rs => maskWheelLift (maskPrefixMod m es) (maskWheelFromList es m rs) e

def maskWheelVisit : List (Nat×Nat) → Nat → Nat → (Nat→Bool) → Bool
  | [], _, r, f => f r
  | e::es, m, r, f => maskWheelVisit es m r (fun z =>
      (List.range e.1).all (fun k =>
        let d := z+maskPrefixMod m es*k
        if maskRootTest d e.1 e.2 then true else f d))

end TenthDiscriminant
