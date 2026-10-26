import TenthDiscriminant
import Mathlib.Algebra.BigOperators.Module

open scoped BigOperators
namespace TenthDiscriminant.ExcludedPrimePrototype
set_option autoImplicit false
noncomputable section

def weight (R S p : Nat) : Real :=
  (2 * valuationWeight R S p : Nat) * Real.log (p : Real)
def mass (P : Finset Nat) (R S : Nat) : Real := ∑ p ∈ P, weight R S p
def prefixCount (E : Finset Nat) (n : Nat) : Real :=
  ((E.filter (fun p => p ≤ n)).card : Real)
def kernelCost (L : Nat) (f B : Nat → Real) : Real :=
  f L * B L + ∑ n ∈ Finset.Ico 3 L, (f n-f (n+1))*B n

theorem indicator_prefix (E : Finset Nat) (n : Nat) :
    (∑ i ∈ Finset.range (n+1), if i ∈ E then (1 : Real) else 0) = prefixCount E n := by
  classical
  have hs : (Finset.range (n+1)).filter (fun i => i ∈ E) = E.filter (fun i => i ≤ n) := by
    ext i
    simp only [Finset.mem_filter, Finset.mem_range]
    constructor
    · rintro ⟨hi, he⟩
      exact ⟨he, by omega⟩
    · rintro ⟨he, hi⟩
      exact ⟨by omega, he⟩
  rw [← Finset.sum_filter]
  simp [hs, prefixCount]

theorem count_abel_identity (E : Finset Nat) (L : Nat) (f : Nat → Real)
    (hL : 3 ≤ L) (hE : ∀ p ∈ E, 3 ≤ p ∧ p ≤ L) :
    (∑ p ∈ E, f p) = kernelCost L f (prefixCount E) := by
  classical
  have hs : (Finset.Ico 3 (L+1)).filter (fun i => i ∈ E) = E := by
    ext i
    simp only [Finset.mem_filter, Finset.mem_Ico]
    constructor
    · intro h; exact h.2
    · intro h
      have hh := hE i h
      exact ⟨⟨hh.1, by omega⟩, h⟩
  have hleft : (∑ i ∈ Finset.Ico 3 (L+1),
      f i * (if i ∈ E then (1 : Real) else 0)) = ∑ p ∈ E, f p := by
    calc
      _ = ∑ i ∈ (Finset.Ico 3 (L+1)).filter (fun i => i ∈ E), f i := by
        rw [Finset.sum_filter]
        simp only [mul_ite, mul_one, mul_zero]
      _ = _ := by rw [hs]
  have hbase : (∑ i ∈ Finset.range 3, if i ∈ E then (1 : Real) else 0) = 0 := by
    apply Finset.sum_eq_zero
    intro i hi
    have hn : i ∉ E := by
      intro he
      have hh := hE i he
      have hl := Finset.mem_range.mp hi
      omega
    simp [hn]
  have hparts := Finset.sum_Ico_by_parts f
    (fun i => if i ∈ E then (1 : Real) else 0) (by omega : 3 < L+1)
  simp only [smul_eq_mul, Nat.add_sub_cancel] at hparts
  rw [hleft, hbase] at hparts
  simp_rw [indicator_prefix] at hparts
  simp only [mul_zero, sub_zero] at hparts
  have hneg : (∑ n ∈ Finset.Ico 3 L, (f n-f (n+1))*prefixCount E n) =
      -(∑ n ∈ Finset.Ico 3 L, (f (n+1)-f n)*prefixCount E n) := by
    rw [← Finset.sum_neg_distrib]
    apply Finset.sum_congr rfl
    intro n hn
    ring
  unfold kernelCost
  linarith

theorem count_transfer (E : Finset Nat) (L : Nat) (f B : Nat → Real)
    (hL : 3 ≤ L) (hE : ∀ p ∈ E, 3 ≤ p ∧ p ≤ L)
    (hanti : AntitoneOn f (Set.Icc 3 L)) (hf : 0 ≤ f L)
    (hB : ∀ n, 3 ≤ n → n ≤ L → prefixCount E n ≤ B n) :
    (∑ p ∈ E, f p) ≤ kernelCost L f B := by
  rw [count_abel_identity E L f hL hE]
  unfold kernelCost
  apply add_le_add
  · exact mul_le_mul_of_nonneg_left (hB L hL le_rfl) hf
  · apply Finset.sum_le_sum
    intro n hn
    have hh := Finset.mem_Ico.mp hn
    have hc : 0 ≤ f n-f (n+1) := by
      apply sub_nonneg.mpr
      exact hanti ⟨hh.1, by omega⟩ ⟨by omega, by omega⟩ (by omega)
    exact mul_le_mul_of_nonneg_left (hB n hh.1 (by omega)) hc

theorem good_mass_bound (G : Finset Nat) (D D2 rho R S : Nat)
    (hD : 0 < D) (hD2 : D ≤ D2) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hprime : ∀ p ∈ G, p.Prime) (hodd : ∀ p ∈ G, p ≠ 2)
    (hns : ∀ p ∈ G, ¬ IsSquare (-(D : ZMod p)))
    (hradius : (1001/1000 : Real)*
        Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
        10*Real.sqrt D2 ≤ (rho : Real)) :
    mass G R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i)) := by
  classical
  have hb := ellipseTraceGram_det_bounds_of_ender_radius D D2 rho R S hD hD2 hR hS hradius
  have hpos : 0 < (integerRectangularTraceGram (ellipsePairs D rho) D S R S).det := by
    have hh : (0 : Real) < ((integerRectangularTraceGram (ellipsePairs D rho) D S R S).det : Real) := by
      rw [ellipseIntegerTraceGram_det_cast D rho S R S hD]
      exact hb.1
    exact_mod_cast hh
  have hlocal : ∀ p ∈ G, (p : Int)^(2*valuationWeight R S p) ∣
      (integerRectangularTraceGram (ellipsePairs D rho) D S R S).det := by
    intro p hp
    letI : Fact p.Prime := ⟨hprime p hp⟩
    exact rectangularTraceGram_valuation_of_nonsquare (ellipsePairs D rho) D S R S p
      (hodd p hp) (hns p hp)
  have hp_le := primePowerProduct_le_det G (fun p => 2*valuationWeight R S p)
    (integerRectangularTraceGram (ellipsePairs D rho) D S R S).det hpos hprime hlocal
  have hi : ((∏ p ∈ G, p^(2*valuationWeight R S p) : Nat) : Int) ≤
      (integerRectangularTraceGram (ellipsePairs D rho) D S R S).det := by
    have hc : ((∏ p ∈ G, p^(2*valuationWeight R S p) : Nat) : Int) ≤
        ((integerRectangularTraceGram (ellipsePairs D rho) D S R S).det.natAbs : Int) := by
      exact_mod_cast hp_le
    simpa only [Int.natCast_natAbs, abs_of_pos hpos] using hc
  have hr : ((∏ p ∈ G, p^(2*valuationWeight R S p) : Nat) : Real) ≤
      (rectangularTraceGram (ellipsePoints D rho) S R S).det := by
    have hc : ((∏ p ∈ G, p^(2*valuationWeight R S p) : Nat) : Real) ≤
        ((integerRectangularTraceGram (ellipsePairs D rho) D S R S).det : Real) := by
      exact_mod_cast hi
    rwa [ellipseIntegerTraceGram_det_cast D rho S R S hD] at hc
  have hprod : (0 : Real) < ((∏ p ∈ G, p^(2*valuationWeight R S p) : Nat) : Real) := by
    exact_mod_cast Finset.prod_pos (fun p hp => pow_pos (hprime p hp).pos _)
  have hlog := Real.log_le_log hprod (hr.trans hb.2)
  have hm : Real.log ((∏ p ∈ G, p^(2*valuationWeight R S p) : Nat) : Real) = mass G R S := by
    simp only [Nat.cast_prod, Nat.cast_pow]
    rw [Real.log_prod]
    · simp only [Real.log_pow, mass, weight]
    · intro p hp
      exact ne_of_gt (pow_pos (by exact_mod_cast (hprime p hp).pos : 0 < (p : Real)) _)
  rw [hm] at hlog
  exact hlog

theorem excluded_prime_budget (P G : Finset Nat) (D D2 rho R S L : Nat)
    (f B : Nat → Real) (C : Real)
    (hD : 0 < D) (hD2 : D ≤ D2) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hL : 3 ≤ L) (hG : G ⊆ P)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p ≠ 2)
    (hmax : ∀ p ∈ P, p ≤ L) (hns : ∀ p ∈ G, ¬ IsSquare (-(D : ZMod p)))
    (hanti : AntitoneOn f (Set.Icc 3 L)) (hf : 0 ≤ f L) (hC : 0 ≤ C)
    (hB : ∀ n, 3 ≤ n → n ≤ L → prefixCount (P\G) n ≤ B n)
    (hw : ∀ p ∈ P\G, weight R S p ≤ C*f p)
    (hradius : (1001/1000 : Real)*
        Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
        10*Real.sqrt D2 ≤ (rho : Real)) :
    mass P R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i)) + C*kernelCost L f B := by
  classical
  have hE : ∀ p ∈ P\G, 3 ≤ p ∧ p ≤ L := by
    intro p hp
    have hh := (Finset.mem_sdiff.mp hp).1
    have h2 := (hprime p hh).two_le
    exact ⟨by have hn := hodd p hh; omega, hmax p hh⟩
  have hg := good_mass_bound G D D2 rho R S hD hD2 hR hS
    (fun p hp => hprime p (hG hp)) (fun p hp => hodd p (hG hp)) hns hradius
  have he : mass (P\G) R S ≤ C*(∑ p ∈ P\G, f p) := by
    unfold mass
    calc
      _ ≤ ∑ p ∈ P\G, C*f p := Finset.sum_le_sum (fun p hp => hw p hp)
      _ = _ := by rw [Finset.mul_sum]
  have hk := mul_le_mul_of_nonneg_left (count_transfer (P\G) L f B hL hE hanti hf hB) hC
  have hu : G ∪ (P\G)=P := by
    ext p
    simp only [Finset.mem_union, Finset.mem_sdiff]
    constructor
    · intro h
      rcases h with h | h
      · exact hG h
      · exact h.1
    · intro h
      by_cases hg : p ∈ G
      · exact Or.inl hg
      · exact Or.inr ⟨h,hg⟩
  have hd : Disjoint G (P\G) := by
    apply Finset.disjoint_left.mpr
    intro p hp he
    exact (Finset.mem_sdiff.mp he).2 hp
  have hm : mass P R S=mass G R S+mass (P\G) R S := by
    unfold mass
    rw [← Finset.sum_union hd, hu]
  rw [hm]
  exact add_le_add hg (he.trans hk)

theorem nonempty_control :
    (∑ p ∈ ({3,5} : Finset Nat), (1 : Real)/p)=8/15 ∧
    kernelCost 5 (fun n => (1 : Real)/n) (prefixCount {3,5})=8/15 := by
  have hi : Finset.Ico 3 5=({3,4} : Finset Nat) := by decide
  norm_num [kernelCost, hi, prefixCount, Finset.filter_insert, Finset.filter_singleton]

theorem empty_count_control (n : Nat) : prefixCount ∅ n=0 := by simp [prefixCount]
theorem empty_kernel_control (L : Nat) (f : Nat → Real) :
    kernelCost L f (fun _ => 0)=0 := by simp [kernelCost]

theorem increasing_kernel_rejected :
    let f := fun n : Nat => if n=3 then (0 : Real) else 1
    let B := fun n : Nat => if n=3 then (2 : Real) else 1
    (∀ n, 3 ≤ n → n ≤ 4 → prefixCount {3} n ≤ B n) ∧
      ¬ (∑ p ∈ ({3} : Finset Nat), f p) ≤ kernelCost 4 f B := by
  dsimp
  constructor
  · intro n h3 h4
    interval_cases n <;> norm_num [prefixCount, Finset.filter_insert, Finset.filter_singleton]
  · have hi : Finset.Ico 3 4=({3} : Finset Nat) := by decide
    norm_num [kernelCost, hi]

theorem negative_endpoint_rejected :
    (∀ n, 3 ≤ n → n ≤ 3 → prefixCount ∅ n ≤ 1) ∧
      ¬ (∑ p ∈ (∅ : Finset Nat), (-1 : Real)) ≤
        kernelCost 3 (fun _ => (-1 : Real)) (fun _ => 1) := by
  constructor
  · intro n hn hmax; simp [prefixCount]
  · norm_num [kernelCost]

theorem split_input_control : IsSquare (-(19 : ZMod 5)) := ⟨1, by decide⟩
end
end TenthDiscriminant.ExcludedPrimePrototype

#audit_namespace TenthDiscriminant.ExcludedPrimePrototype

open Lean Elab Command

elab "#prototype_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PROTOTYPE_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
    ``TenthDiscriminant.ellipse_primeMass_product_dvd,
    ``TenthDiscriminant.ellipse_primeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_log_le_hadamard,
    ``TenthDiscriminant.smallPrimeNormLifting_of_classNumber_one,
    ``TenthDiscriminant.smallPrime_nonsquare_of_classNumber_one,
    ``TenthDiscriminant.rectangularTraceGram_valuation_of_classNumber_one,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b,

    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff,
    ``TenthDiscriminant.known_nine_classNumber_one,
    ``TenthDiscriminant.phase36_all_fibers,
    ``TenthDiscriminant.classNumber_one_candidates_below_million,
    ``TenthDiscriminant.classNumber_one_iff_below_million,
    ``TenthDiscriminant.phase35_q0_translate,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_parameter_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b,
    ``TenthDiscriminant.FirstCertificate.rawPrimeMassLower_uniform]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PROTOTYPE_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PROTOTYPE_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PROTOTYPE_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PROTOTYPE_NONSTANDARD_AXIOM {name}"
  logInfo m!"PROTOTYPE_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"



#prototype_inputs TenthDiscriminant.ExcludedPrimePrototype.good_mass_bound
#prototype_inputs TenthDiscriminant.ExcludedPrimePrototype.count_transfer
#prototype_inputs TenthDiscriminant.ExcludedPrimePrototype.excluded_prime_budget
#print axioms TenthDiscriminant.ExcludedPrimePrototype.excluded_prime_budget
