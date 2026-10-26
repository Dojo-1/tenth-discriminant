import TenthDiscriminant.FiniteSieveBridge

/-! A wheel is a finite list of allowed remainders, not a claim that a
saved output is complete. Each lift and the interval enumeration below
carry a universal coverage proof. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem modularRootTest_congr (a b p : Nat) (h : a%p=b%p) :
    modularRootTest a p=modularRootTest b p := by
  unfold modularRootTest
  apply congrArg ((List.range p).any)
  funext r
  rw [Nat.add_mod (r*r) a p, Nat.add_mod (r*r) b p, h]

def wheelLift (m : Nat) (rs : List Nat) (p : Nat) : List Nat :=
  ((List.range p).flatMap (fun k => rs.map (fun r => r+m*k))).filter
    (fun n => !modularRootTest n p)

theorem wheelLift_covers (m p d : Nat) (rs : List Nat)
    (hm : 0 < m) (hp : 0 < p) (hr : d%m ∈ rs)
    (hroot : modularRootTest d p=false) : d%(m*p) ∈ wheelLift m rs p := by
  let z := d%(m*p)
  have hzm : z%m=d%m := Nat.mod_mod_of_dvd d (dvd_mul_right m p)
  have hzp : z%p=d%p := Nat.mod_mod_of_dvd d (dvd_mul_left p m)
  have hk : z/m<p := by
    apply (Nat.div_lt_iff_lt_mul hm).mpr
    simpa [z, Nat.mul_comm] using Nat.mod_lt d (Nat.mul_pos hm hp)
  have heq : d%m+m*(z/m)=z := by
    simpa only [hzm] using Nat.mod_add_div z m
  apply List.mem_filter.mpr
  constructor
  · apply List.mem_flatMap.mpr
    refine ⟨z/m, List.mem_range.mpr hk, ?_⟩
    exact List.mem_map.mpr ⟨d%m, hr, heq⟩
  · have hz := modularRootTest_congr z d p hzp
    change (!modularRootTest z p)=true
    rw [hz, hroot]
    rfl

def wheelMod : List Nat → Nat
  | [] => 8
  | p::ps => wheelMod ps*p

def wheelResidues : List Nat → List Nat
  | [] => [3]
  | p::ps => wheelLift (wheelMod ps) (wheelResidues ps) p

theorem wheelMod_pos (ps : List Nat) (hp : ∀ p ∈ ps, 0<p) : 0<wheelMod ps := by
  induction ps with
  | nil => decide
  | cons p ps ih =>
    exact Nat.mul_pos (ih (fun q hq => hp q (List.mem_cons_of_mem p hq)))
      (hp p (List.mem_cons_self))

/-- Every integer satisfying the specified nonsquare conditions is retained.
The list order affects enumeration only, not coverage. -/
theorem wheelResidues_cover (ps : List Nat) (hp : ∀ p ∈ ps, 0<p)
    (d : Nat) (hmod : d%8=3)
    (hn : ∀ p ∈ ps, modularRootTest d p=false) : d%wheelMod ps ∈ wheelResidues ps := by
  induction ps with
  | nil => simpa [wheelMod, wheelResidues, hmod]
  | cons p ps ih =>
    have htail : ∀ q ∈ ps, 0<q := fun q hq => hp q (List.mem_cons_of_mem p hq)
    apply wheelLift_covers _ _ _ _ (wheelMod_pos ps htail) (hp p List.mem_cons_self)
    · exact ih htail (fun q hq => hn q (List.mem_cons_of_mem p hq))
    · exact hn p List.mem_cons_self

def intervalWheel (m : Nat) (rs : List Nat) (lo hi : Nat) : List Nat :=
  ((List.range (hi/m+1)).flatMap (fun k => rs.map (fun r => r+m*k))).filter
    (fun d => decide (lo≤d ∧ d<hi))

/-- Quotient and remainder supply a witness for every interval point.
The quotient range is deliberately padded; the exact half-open filter
removes padding. Missing quotient or residue coverage cannot be assumed. -/
theorem intervalWheel_covers (m d lo hi : Nat) (rs : List Nat)
    (hr : d%m ∈ rs) (hlo : lo≤d) (hhi : d<hi) : d ∈ intervalWheel m rs lo hi := by
  have hk : d/m<hi/m+1 := by
    have hle : d/m ≤ hi/m := Nat.div_le_div_right (Nat.le_of_lt hhi)
    omega
  apply List.mem_filter.mpr
  constructor
  · apply List.mem_flatMap.mpr
    refine ⟨d/m, List.mem_range.mpr hk, ?_⟩
    exact List.mem_map.mpr ⟨d%m, hr, Nat.mod_add_div d m⟩
  · simpa only [decide_eq_true_eq] using And.intro hlo hhi

def millionWheelPrimes : List Nat := [3,5,7,11]
def millionExtraPrimes : List Nat :=
  [13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127]

theorem millionWheelPrimes_checked : checkedOddPrimes millionWheelPrimes=true := by decide +kernel
theorem millionExtraPrimes_checked : checkedOddPrimes millionExtraPrimes=true := by decide +kernel
theorem millionWheelPrimes_bounded :
    millionWheelPrimes.all (fun p => decide (p≤11))=true := by decide +kernel
theorem millionWheelMod : wheelMod millionWheelPrimes=9240 := by decide +kernel
theorem millionWheelResidue_count : (wheelResidues millionWheelPrimes).length=30 := by decide +kernel

theorem classNumber_one_mem_millionWheel (d hi : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hlo : 92≤d) (hhi : d<hi) :
    d ∈ intervalWheel (wheelMod millionWheelPrimes) (wheelResidues millionWheelPrimes) 92 hi := by
  have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
  apply intervalWheel_covers _ _ _ _ _ (hlo := hlo) (hhi := hhi)
  apply wheelResidues_cover (d := d) (hmod := hmod)
  · intro p hp
    have hpair : p.Prime ∧ p≠2 :=
      of_decide_eq_true ((List.all_eq_true.mp millionWheelPrimes_checked) p hp)
    exact hpair.1.pos
  · intro p hp
    have hpair : p.Prime ∧ p≠2 :=
      of_decide_eq_true ((List.all_eq_true.mp millionWheelPrimes_checked) p hp)
    have hbound : p≤11 :=
      of_decide_eq_true ((List.all_eq_true.mp millionWheelPrimes_bounded) p hp)
    have htest := guardedPrimeTest_of_classNumber_one d p hsq hc hmod hpair.1 hpair.2
    simpa [guardedPrimeTest, show 4*p≤d by omega] using htest

end TenthDiscriminant
