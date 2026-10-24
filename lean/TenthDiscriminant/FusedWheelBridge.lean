import TenthDiscriminant.ResidueMaskBridge
import TenthDiscriminant.FusedWheelParameters

/-! Fusion and a complete seed partition preserve ALL predicates, not just
one list length or one observed successful run. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem maskWheelLift_all (m : Nat) (rs : List Nat) (e : Nat×Nat) (f : Nat→Bool) :
    (maskWheelLift m rs e).all f = rs.all (fun r =>
      (List.range e.1).all (fun k =>
        if maskRootTest (r+m*k) e.1 e.2 then true else f (r+m*k))) := by
  apply Bool.eq_iff_iff.mpr
  rw [List.all_eq_true, List.all_eq_true]
  constructor
  · intro h r hr
    apply List.all_eq_true.mpr
    intro k hk
    by_cases hz : maskRootTest (r+m*k) e.1 e.2=true
    · simp only [hz, ↓reduceIte]
    · have hm : r+m*k ∈ maskWheelLift m rs e := by
        apply List.mem_filter.mpr
        refine ⟨List.mem_flatMap.mpr ⟨k, hk, List.mem_map.mpr ⟨r, hr, rfl⟩⟩, ?_⟩
        simp [hz]
      simpa only [hz, Bool.false_eq_true, ↓reduceIte] using h _ hm
  · intro h n hn
    obtain ⟨hn, hz⟩ := List.mem_filter.mp hn
    obtain ⟨k, hk, hn⟩ := List.mem_flatMap.mp hn
    obtain ⟨r, hr, rfl⟩ := List.mem_map.mp hn
    have hf := List.all_eq_true.mp (h r hr) k hk
    have hfalse : maskRootTest (r+m*k) e.1 e.2=false := by simpa using hz
    simpa only [hfalse, Bool.false_eq_true, ↓reduceIte] using hf

theorem maskWheelVisit_all (es : List (Nat×Nat)) (m : Nat) (rs : List Nat) (f : Nat→Bool) :
    rs.all (fun r => maskWheelVisit es m r f)=(maskWheelFromList es m rs).all f := by
  induction es generalizing f with
  | nil => rfl
  | cons e es ih =>
    rw [maskWheelFromList, maskWheelLift_all, ←ih]
    rfl

/-- The eleven blocks are a complete partition for every leaf predicate.
No sampled runtime or cardinality agreement is used in this equality. -/
theorem phase35_partition (f : Nat→Bool) :
    phase35Seeds.all (fun r => maskWheelVisit phase35Prefix 184 r f)=
      (maskWheelResidues phase34Base).all f := by
  rw [maskWheelVisit_all]
  rfl

theorem phase35_seed_count : phase35Seeds.length=11 := by decide +kernel

theorem phase35_translate_of_blocks (k : Nat)
    (hc : phase35Seeds.all (phase35Block k)=true) :
    maskTranslateClear (maskWheelResidues phase34Base)
      892371480 1000000 700000000000 k phase34Extra=true := by
  change phase35Seeds.all (fun r => maskWheelVisit phase35Prefix 184 r (phase35Leaf k))=true at hc
  rw [phase35_partition] at hc
  exact hc

theorem fused_false_leaf_control :
    maskWheelVisit [(3,negativeSquareMask 3)] 8 3 (fun _ => false)=false := by decide +kernel

theorem fused_omitted_seed_control :
    ([] : List Nat).all (fun _ => false)=true ∧
      phase35Seeds.all (fun _ => false)=false := by decide +kernel

/-- The base wheel repeats after one period, but an extra prime need not.
Thus one checked translate cannot certify all the others by translation. -/
theorem fused_extra_translation_control :
    maskRootTest 163 29 (negativeSquareMask 29)=false ∧
      maskRootTest (163+892371480) 29 (negativeSquareMask 29)=true := by decide +kernel

end TenthDiscriminant
