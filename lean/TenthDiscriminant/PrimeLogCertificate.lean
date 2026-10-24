import TenthDiscriminant.UniformPrimeMass
import TenthDiscriminant.NumericalCertificate

/-! A fixed table of four rounded prime-log constants can be reused for
arbitrary rectangle dimensions. Pairing checks prevent missing/swapped rows. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

structure ConstantRow where
  p : Nat
  a : Nat
  b : Nat
  c : Nat
  e : Nat
deriving DecidableEq, Repr

def checkConstantRow (r : Row) (t : ConstantRow) : Bool := decide (
  t.p = r.p ∧ r.hi ≤ t.a * (r.p - 1) ∧
    if 7 ≤ r.p then t.b * r.p ≤ r.lo ∧ r.hi ≤ t.c * r.p ^ 2 ∧ t.e = r.hi
    else t.b = 0 ∧ t.c = 0 ∧ t.e = 0)

def checkConstantRows : List Row → List ConstantRow → Bool
  | [], [] => true
  | r :: rs, t :: ts => checkConstantRow r t && checkConstantRows rs ts
  | _, _ => false

theorem checkConstantRows_sound (rs : List Row) (ts : List ConstantRow)
    (hc : checkConstantRows rs ts = true) :
    List.Forall₂ (fun r t => checkConstantRow r t = true) rs ts := by
  induction rs generalizing ts with
  | nil =>
    cases ts with
    | nil => exact .nil
    | cons t ts => simp [checkConstantRows] at hc
  | cons r rs ih =>
    cases ts with
    | nil => simp [checkConstantRows] at hc
    | cons t ts =>
      have hh : checkConstantRow r t = true ∧ checkConstantRows rs ts = true := by
        simpa only [checkConstantRows, Bool.and_eq_true] using hc
      exact .cons hh.1 (ih ts hh.2)

theorem checkConstantRow_sound (r : Row) (t : ConstantRow)
    (hr : checkRow r = true) (hc : checkConstantRow r t = true) :
    Real.log r.p / ((r.p : Real) - 1) ≤ (t.a : Real) / scale ∧
      (t.b : Real) / scale ≤ (if 7 ≤ r.p then Real.log r.p / (r.p : Real) else 0) ∧
      (if 7 ≤ r.p then Real.log r.p / (r.p : Real) ^ 2 else 0) ≤ (t.c : Real) / scale ∧
      (if 7 ≤ r.p then Real.log r.p else 0) ≤ (t.e : Real) / scale := by
  have hp : 2 ≤ r.p := (of_decide_eq_true hr).1
  have hl := (checkRow_sound r hr).2.1
  have hs : (0 : Real) < scale := by norm_num [scale]
  have hp0 : (0 : Real) < r.p := by exact_mod_cast (by omega : 0 < r.p)
  have hp1 : (0 : Real) < (r.p : Real) - 1 := by
    have hh : (2 : Real) ≤ r.p := by exact_mod_cast hp
    linarith
  have hlo : (r.lo : Real) ≤ Real.log r.p * scale := (div_le_iff₀ hs).mp hl.1
  have hhi : Real.log r.p * scale ≤ r.hi := (le_div_iff₀ hs).mp hl.2
  rcases of_decide_eq_true hc with ⟨hid, ha, ht⟩
  have ha' : (r.hi : Real) ≤ t.a * ((r.p : Real) - 1) := by
    have hcast : (r.hi : Real) ≤ ((t.a * (r.p - 1) : Nat) : Real) := by exact_mod_cast ha
    simpa only [Nat.cast_mul, Nat.cast_sub (by omega : 1 ≤ r.p), Nat.cast_one] using hcast
  constructor
  · exact (div_le_div_iff₀ hp1 hs).mpr (hhi.trans ha')
  · by_cases hret : 7 ≤ r.p
    · rw [if_pos hret] at ht
      rcases ht with ⟨hb, hc, he⟩
      have hb' : (t.b : Real) * r.p ≤ r.lo := by exact_mod_cast hb
      have hc' : (r.hi : Real) ≤ t.c * (r.p : Real) ^ 2 := by exact_mod_cast hc
      simp only [if_pos hret]
      refine ⟨(div_le_div_iff₀ hs hp0).mpr (hb'.trans hlo), ?_, ?_⟩
      · exact (div_le_div_iff₀ (by positivity) hs).mpr (hhi.trans hc')
      · rw [he]
        exact hl.2
    · rw [if_neg hret] at ht
      rcases ht with ⟨hb, hc, he⟩
      simp [if_neg hret, hb, hc, he]

theorem paired_upper_units (f : Row → Real) (u : ConstantRow → Nat)
    (hsound : ∀ r t, checkRow r = true → checkConstantRow r t = true → f r ≤ (u t : Real) / scale)
    (rs : List Row) (ts : List ConstantRow)
    (hc : List.Forall₂ (fun r t => checkConstantRow r t = true) rs ts) :
    (∀ r ∈ rs, checkRow r = true) →
      (rs.map f).sum ≤ ((ts.map u).sum : Nat) / (scale : Real) := by
  induction hc with
  | nil => simp
  | @cons r t rs ts hh ht ih =>
    intro hr
    have hhead := hsound r t (hr r (by simp)) hh
    have htail := ih (fun x hx => hr x (by simp [hx]))
    simp only [List.map_cons, List.sum_cons, Nat.cast_add]
    rw [add_div]
    exact add_le_add hhead htail

theorem paired_lower_units (f : Row → Real) (u : ConstantRow → Nat)
    (hsound : ∀ r t, checkRow r = true → checkConstantRow r t = true → (u t : Real) / scale ≤ f r)
    (rs : List Row) (ts : List ConstantRow)
    (hc : List.Forall₂ (fun r t => checkConstantRow r t = true) rs ts) :
    (∀ r ∈ rs, checkRow r = true) →
      ((ts.map u).sum : Nat) / (scale : Real) ≤ (rs.map f).sum := by
  induction hc with
  | nil => simp
  | @cons r t rs ts hh ht ih =>
    intro hr
    have hhead := hsound r t (hr r (by simp)) hh
    have htail := ih (fun x hx => hr x (by simp [hx]))
    simp only [List.map_cons, List.sum_cons, Nat.cast_add]
    rw [add_div]
    exact add_le_add hhead htail

theorem four_prime_log_bounds (rs : List Row) (ts : List ConstantRow)
    (hcover : rs.map Row.p = primeList) (hr : ∀ r ∈ rs, checkRow r = true)
    (hc : List.Forall₂ (fun r t => checkConstantRow r t = true) rs ts) :
    primeLogFactorialConstant 10000 ≤ ((ts.map ConstantRow.a).sum : Nat) / (scale : Real) ∧
      (((ts.map ConstantRow.b).sum : Nat) : Real) / scale ≤ primeLogLinearConstant 7 10000 ∧
      primeLogSquareConstant 7 10000 ≤ ((ts.map ConstantRow.c).sum : Nat) / (scale : Real) ∧
      primeLogErrorConstant 7 10000 ≤ ((ts.map ConstantRow.e).sum : Nat) / (scale : Real) := by
  constructor
  · rw [primeLogFactorialConstant, ← rows_sum_eq rs hcover]
    exact paired_upper_units _ ConstantRow.a (fun r t hr hc => (checkConstantRow_sound r t hr hc).1) rs ts hc hr
  constructor
  · rw [primeLogLinearConstant, retainedSmallPrimes, Finset.sum_filter, ← rows_sum_eq rs hcover]
    exact paired_lower_units _ ConstantRow.b (fun r t hr hc => (checkConstantRow_sound r t hr hc).2.1) rs ts hc hr
  constructor
  · rw [primeLogSquareConstant, retainedSmallPrimes, Finset.sum_filter, ← rows_sum_eq rs hcover]
    exact paired_upper_units _ ConstantRow.c (fun r t hr hc => (checkConstantRow_sound r t hr hc).2.2.1) rs ts hc hr
  · rw [primeLogErrorConstant, retainedSmallPrimes, Finset.sum_filter, ← rows_sum_eq rs hcover]
    exact paired_upper_units _ ConstantRow.e (fun r t hr hc => (checkConstantRow_sound r t hr hc).2.2.2) rs ts hc hr

theorem missing_constant_row_rejected :
    checkConstantRows [⟨2,1,1,1,1,0,⟨0,0,0⟩,[]⟩] [] = false := by decide

end
end TenthDiscriminant.FirstCertificate
