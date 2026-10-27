import TenthDiscriminant
import Mathlib.NumberTheory.Harmonic.Bounds

/-! A positive finite Abel operator keeps the axis constant separate. -/
open scoped BigOperators NumberField nonZeroDivisors Classical
namespace TenthDiscriminant.ClosedKernel
open ExcludedPrime SplitPrimeBudget
set_option autoImplicit false
noncomputable section

def linearSlope (d M : Real) : Real := Real.pi/Real.sqrt d+2*Real.sqrt (M/(3*d))
def closedCost (d M : Real) (L : Nat) : Real :=
  linearSlope d M*(Real.log 3+Real.log L*(1+Real.log L))+Real.log 3/6

theorem kernel_mono (L : Nat) (hL : 3≤L) (B C : Nat → Real)
    (hBC : ∀ n, 3≤n → n≤L → B n≤C n) :
    kernelCost L primeKernel B ≤ kernelCost L primeKernel C := by
  unfold kernelCost
  apply add_le_add
  · exact mul_le_mul_of_nonneg_left (hBC L hL le_rfl) (primeKernel_nonneg L)
  · apply Finset.sum_le_sum
    intro n hn
    have hh := Finset.mem_Ico.mp hn
    have hc : 0≤primeKernel n-primeKernel (n+1) := by
      exact sub_nonneg.mpr (primeKernel_antitone L ⟨hh.1,by omega⟩
        ⟨by omega,by omega⟩ (by omega))
    exact mul_le_mul_of_nonneg_left (hBC n hh.1 (by omega)) hc

theorem affine_identity (L : Nat) (hL : 3≤L) (f : Nat → Real) (a b : Real) :
    kernelCost L f (fun n => a*n+b) =
      a*(3*f 3+∑ n ∈ Finset.Ico 4 (L+1), f n)+b*f 3 := by
  induction L, hL using Nat.le_induction with
  | base => simp [kernelCost]; ring
  | succ L hL ih =>
    have hs : kernelCost (L+1) f (fun n => a*n+b) =
        kernelCost L f (fun n => a*n+b)+f (L+1)*a := by
      simp only [kernelCost,Finset.sum_Ico_succ_top hL,Nat.cast_add,Nat.cast_one]
      ring
    rw [hs,ih,Finset.sum_Ico_succ_top (by omega : 4≤L+1)]
    ring

theorem prime_sum_bound (L : Nat) (hL : 3≤L) :
    (∑ n ∈ Finset.Ico 4 (L+1), primeKernel n) ≤
      Real.log L*(1+Real.log L) := by
  have hlog : 0≤Real.log (L : Real) := Real.log_nonneg (by exact_mod_cast (by omega : 1≤L))
  have hinv : (∑ n ∈ Finset.Ico 4 (L+1), (n : Real)⁻¹) ≤ (harmonic L : Real) := by
    simp only [harmonic_eq_sum_Icc,Rat.cast_sum,Rat.cast_inv,Rat.cast_natCast]
    apply Finset.sum_le_sum_of_subset_of_nonneg
    · intro n hn
      have hh := Finset.mem_Ico.mp hn
      exact Finset.mem_Icc.mpr ⟨by omega,by omega⟩
    · intro n hn hnot
      positivity
  calc
    _ ≤ ∑ n ∈ Finset.Ico 4 (L+1), Real.log L*(n : Real)⁻¹ := by
      apply Finset.sum_le_sum
      intro n hn
      have hh := Finset.mem_Ico.mp hn
      have hn0 : (0 : Real)<n := by exact_mod_cast (by omega : 0<n)
      have hnL : (n : Real)≤L := by exact_mod_cast (by omega : n≤L)
      simpa only [primeKernel,div_eq_mul_inv] using
        mul_le_mul_of_nonneg_right (Real.log_le_log hn0 hnL) (by positivity : 0≤(n : Real)⁻¹)
    _ = Real.log L*∑ n ∈ Finset.Ico 4 (L+1), (n : Real)⁻¹ := (Finset.mul_sum ..).symm
    _ ≤ Real.log L*(harmonic L : Real) := mul_le_mul_of_nonneg_left hinv hlog
    _ ≤ _ := mul_le_mul_of_nonneg_left (harmonic_le_one_add_log L) hlog

theorem sqrt_majorant (d M x : Real) (hd : 0<d) (hM : 0≤M) (hx : 3≤x) :
    Real.sqrt (M*x/d) ≤ x*Real.sqrt (M/(3*d)) := by
  have hq : 0≤M/(3*d) := by positivity
  apply Real.sqrt_le_iff.mpr
  refine ⟨by positivity,?_⟩
  calc
    M*x/d = 3*x*(M/(3*d)) := by field_simp; ring
    _ ≤ x^2*(M/(3*d)) := mul_le_mul_of_nonneg_right (by nlinarith) hq
    _ = (x*Real.sqrt (M/(3*d)))^2 := by rw [mul_pow,Real.sq_sqrt hq]

theorem actual_majorant (D : Nat) [Fact ((D : Int)%4=3)] (n : Nat) (hn : 3≤n) :
    countBound D n ≤ linearSlope D (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)))*n+1/2 := by
  have hD : 0<D := by have hm := (Fact.out : (D : Int)%4=3); omega
  have hM : 0≤ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)) := by
    unfold ClassFiber.normBound
    positivity
  have hs := sqrt_majorant (D : Real) (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)))
    (n : Real) (by exact_mod_cast hD) hM (by exact_mod_cast hn)
  unfold countBound linearSlope
  simp only [div_eq_mul_inv] at hs ⊢
  nlinarith

theorem closed_count_kernel (D : Nat) [Fact ((D : Int)%4=3)] (L : Nat) (hL : 3≤L) :
    kernelCost L primeKernel (countBound D) ≤
      closedCost D (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))) L := by
  let a := linearSlope D (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4)))
  have ha : 0≤a := by dsimp [a,linearSlope]; positivity
  calc
    _ ≤ kernelCost L primeKernel (fun n => a*n+1/2) :=
      kernel_mono L hL _ _ (fun n hn hnL => actual_majorant D n hn)
    _ = a*(Real.log 3+∑ n ∈ Finset.Ico 4 (L+1), primeKernel n)+Real.log 3/6 := by
      rw [affine_identity L hL]
      norm_num [primeKernel]
      ring
    _ ≤ a*(Real.log 3+Real.log L*(1+Real.log L))+Real.log 3/6 := by
      exact add_le_add_right (mul_le_mul_of_nonneg_left (add_le_add_left (prime_sum_bound L hL) _) ha) _
    _ = _ := rfl

theorem closed_actual_gram_budget (D : Nat) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (h : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≤2)
    (P : Finset Nat) (D2 rho R S L : Nat)
    (hD2 : D≤D2) (hR : 1≤R) (hS : 1≤S) (hL : 3≤L)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p≠2) (hmax : ∀ p ∈ P, p≤L)
    (hradius : (1001/1000 : Real)*
      Real.sqrt (((3*R+S : Nat) : Real)*Real.sqrt D2/Real.pi)+
      10*Real.sqrt D2 ≤ (rho : Real)) :
    mass P R S ≤ Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i))+
      lossScale R S*closedCost D (ClassFiber.normBound (QuadraticField (((D : Int)+1)/4))) L+
      ((R*S*(S-1) : Nat) : Real)*Real.log (D : Real) := by
  have old := actual_gram_budget D hsq h P D2 rho R S L hD2 hR hS hL hprime hodd hmax hradius
  have hk := mul_le_mul_of_nonneg_left (closed_count_kernel D L hL)
    (by unfold lossScale; positivity : 0≤lossScale R S)
  linarith

theorem endpoint_control (f : Nat → Real) (a b : Real) :
    kernelCost 3 f (fun n => a*n+b)=(3*a+b)*f 3 := by simp [kernelCost]; ring

theorem zero_slope_control (L : Nat) (hL : 3≤L) (b : Real) :
    kernelCost L primeKernel (fun n => (0 : Real)*n+b)=b*primeKernel 3 := by
  rw [affine_identity L hL]; ring

theorem constant_control (L : Nat) (hL : 3≤L) :
    kernelCost L primeKernel (fun _ => (1 : Real))=primeKernel 3 := by
  simpa using zero_slope_control L hL 1

theorem closed_endpoint_nonneg (d M : Real) (hd : 0≤d) (hM : 0≤M) :
    0≤closedCost d M 3 := by
  unfold closedCost linearSlope
  positivity
end
end TenthDiscriminant.ClosedKernel

#check TenthDiscriminant.ClosedKernel.kernel_mono
#check TenthDiscriminant.ClosedKernel.affine_identity
#check TenthDiscriminant.ClosedKernel.prime_sum_bound
#check TenthDiscriminant.ClosedKernel.sqrt_majorant
#check TenthDiscriminant.ClosedKernel.actual_majorant
#check TenthDiscriminant.ClosedKernel.closed_count_kernel
#check TenthDiscriminant.ClosedKernel.closed_actual_gram_budget
#check TenthDiscriminant.ClosedKernel.endpoint_control
#check TenthDiscriminant.ClosedKernel.zero_slope_control
#check TenthDiscriminant.ClosedKernel.constant_control
#check TenthDiscriminant.ClosedKernel.closed_endpoint_nonneg
#print TenthDiscriminant.ClosedKernel.linearSlope
#print TenthDiscriminant.ClosedKernel.closedCost
#print TenthDiscriminant.ExcludedPrime.primeKernel
#print TenthDiscriminant.ExcludedPrime.kernelCost
#print axioms TenthDiscriminant.ClosedKernel.closed_actual_gram_budget
#audit_namespace TenthDiscriminant.ClosedKernel

open Lean Elab Command

elab "#phase83_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE83_ROOT_MISSING {target}"
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
      throwError "PHASE83_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE83_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE83_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE83_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE83_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"




#phase83_inputs TenthDiscriminant.ClosedKernel.closed_actual_gram_budget
