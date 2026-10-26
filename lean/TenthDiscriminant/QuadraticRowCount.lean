import Mathlib
import TenthDiscriminant.AxiomAudit
import Mathlib.Analysis.SumIntegralComparisons

/-! Frozen Phase63 row-count proof transported to production.
The closed area evaluation is in QuadraticAreaCount. -/

open scoped BigOperators
open MeasureTheory
namespace TenthDiscriminant.QuadraticRows
set_option autoImplicit false
noncomputable section

def quad (a b c : Real) (p : Int × Int) : Real :=
  a*(p.1 : Real)^2+b*(p.1 : Real)*(p.2 : Real)+c*(p.2 : Real)^2

def width (a D t s : Real) : Real := Real.sqrt (4*a*t-D*s^2)/a
def height (a D t : Real) : Real := Real.sqrt (4*a*t/D)
def nonzeroBudget (a D t : Real) : Real :=
  2*(∫ s in (0 : Real)..height a D t, width a D t s)+2*height a D t

theorem integer_interval_card (A : Finset Int) (l u : Real) (hlu : l ≤ u)
    (hA : ∀ x ∈ A, l ≤ (x : Real) ∧ (x : Real) ≤ u) :
    (A.card : Real) ≤ u-l+1 := by
  classical
  by_cases hn : A.Nonempty
  · have hsub : A ⊆ Finset.Icc (A.min' hn) (A.max' hn) := by
      intro x hx
      exact Finset.mem_Icc.mpr ⟨A.min'_le x hx, A.le_max' x hx⟩
    have hcard := Finset.card_le_card hsub
    have hminmax : A.min' hn ≤ A.max' hn := A.min'_le _ (A.max'_mem hn)
    have hc : (A.card : Int) ≤ A.max' hn+1-A.min' hn := by
      calc
        _ ≤ ((Finset.Icc (A.min' hn) (A.max' hn)).card : Int) := by exact_mod_cast hcard
        _ = _ := Int.card_Icc_of_le (A.min' hn) (A.max' hn) (by omega)
    have hr : (A.card : Real) ≤ (A.max' hn : Real)+1-(A.min' hn : Real) := by
      exact_mod_cast hc
    have hl := (hA _ (A.min'_mem hn)).1
    have hu := (hA _ (A.max'_mem hn)).2
    linarith
  · have he : A=∅ := by
      apply Finset.eq_empty_iff_forall_not_mem.mpr
      intro x hx
      exact hn ⟨x,hx⟩
    rw [he]
    simp only [Finset.card_empty, Nat.cast_zero]
    linarith

theorem complete_square (a b c : Real) (p : Int × Int) :
    4*a*quad a b c p = (2*a*(p.1 : Real)+b*(p.2 : Real))^2+
      (4*a*c-b^2)*(p.2 : Real)^2 := by unfold quad; ring

theorem point_height (a b c t : Real) (p : Int × Int) (ha : 0 < a)
    (hD : 0 < 4*a*c-b^2) (hq : quad a b c p ≤ t) :
    (p.2 : Real) ≤ height a (4*a*c-b^2) t := by
  unfold height
  apply Real.le_sqrt_of_sq_le
  apply (le_div_iff₀ hD).mpr
  have hc := complete_square a b c p
  have hm := mul_le_mul_of_nonneg_left hq (by positivity : 0 ≤ 4*a)
  nlinarith [sq_nonneg (2*a*(p.1 : Real)+b*(p.2 : Real))]

theorem width_nonneg (a D t s : Real) (ha : 0 < a) : 0 ≤ width a D t s :=
  div_nonneg (Real.sqrt_nonneg _) ha.le

theorem width_continuous (a D t : Real) : Continuous (width a D t) := by
  unfold width
  fun_prop

theorem width_antitone (a D t : Real) (ha : 0 < a) (hD : 0 < D) :
    AntitoneOn (width a D t) (Set.Ici 0) := by
  intro x hx y hy hxy
  have hs : x^2 ≤ y^2 := (sq_le_sq₀ hx hy).mpr hxy
  have hm := mul_le_mul_of_nonneg_left hs hD.le
  apply div_le_div_of_nonneg_right _ ha.le
  apply Real.sqrt_le_sqrt
  linarith

theorem row_card (U : Finset (Int × Int)) (a b c t : Real) (n : Nat)
    (ha : 0 < a) (hQ : ∀ p ∈ U, quad a b c p ≤ t) :
    ((U.filter (fun p => p.2=(n : Int))).card : Real) ≤
      width a (4*a*c-b^2) t (n : Real)+1 := by
  classical
  let F := U.filter (fun p => p.2=(n : Int))
  let X := F.image Prod.fst
  let v := Real.sqrt (4*a*t-(4*a*c-b^2)*(n : Real)^2)
  let l := (-b*(n : Real)-v)/(2*a)
  let u := (-b*(n : Real)+v)/(2*a)
  have hv : 0 ≤ v := Real.sqrt_nonneg _
  have h2a : 0 < 2*a := by positivity
  have hlu : l ≤ u := by
    apply (div_le_div_iff_of_pos_right h2a).mpr
    linarith
  have hcard : X.card=F.card := by
    apply Finset.card_image_iff.mpr
    intro p hp q hq he
    apply Prod.ext he
    have hp' := (Finset.mem_filter.mp hp).2
    have hq' := (Finset.mem_filter.mp hq).2
    exact hp'.trans hq'.symm
  have hX : ∀ x ∈ X, l ≤ (x : Real) ∧ (x : Real) ≤ u := by
    intro x hx
    obtain ⟨p,hp,rfl⟩ := Finset.mem_image.mp hx
    have hpU := (Finset.mem_filter.mp hp).1
    have hy : p.2=(n : Int) := (Finset.mem_filter.mp hp).2
    have hyr : (p.2 : Real)=(n : Real) := by exact_mod_cast hy
    have hc := complete_square a b c p
    rw [hyr] at hc
    have hm := mul_le_mul_of_nonneg_left (hQ p hpU) (by positivity : 0 ≤ 4*a)
    have hs : (2*a*(p.1 : Real)+b*(n : Real))^2 ≤
        4*a*t-(4*a*c-b^2)*(n : Real)^2 := by nlinarith
    have hb := abs_le.mp (Real.abs_le_sqrt hs)
    constructor
    · apply (div_le_iff₀ h2a).mpr
      linarith [hb.1]
    · apply (le_div_iff₀ h2a).mpr
      linarith [hb.2]
  have hh := integer_interval_card X l u hlu hX
  rw [hcard] at hh
  have he : u-l+1=width a (4*a*c-b^2) t (n : Real)+1 := by
    dsimp [l,u,v,width]
    field_simp [ne_of_gt ha]
    ring
  exact hh.trans_eq he

theorem positive_rows (U : Finset (Int × Int)) (a b c t : Real)
    (ha : 0 < a) (hD : 0 < 4*a*c-b^2) (ht : 0 ≤ t)
    (hpos : ∀ p ∈ U, 0 < p.2) (hQ : ∀ p ∈ U, quad a b c p ≤ t) :
    (U.card : Real) ≤
      (∫ s in (0 : Real)..height a (4*a*c-b^2) t, width a (4*a*c-b^2) t s)+
        height a (4*a*c-b^2) t := by
  classical
  let Y := height a (4*a*c-b^2) t
  let M : Nat := ⌊Y⌋₊
  have hY : 0 ≤ Y := Real.sqrt_nonneg _
  have hMY : (M : Real) ≤ Y := Nat.floor_le hY
  have hmap : U.toSet.MapsTo (fun p => p.2.toNat-1) (Finset.range M) := by
    intro p hp
    have hy := hpos p hp
    have hycast : (p.2.toNat : Real)=(p.2 : Real) := by
      exact_mod_cast Int.toNat_of_nonneg hy.le
    have hyn : p.2.toNat ≤ M := by
      apply (Nat.le_floor_iff hY).mpr
      rw [hycast]
      exact point_height a b c t p ha hD (hQ p hp)
    have hypos : 0 < p.2.toNat := by omega
    apply Finset.mem_range.mpr
    change p.2.toNat-1 < M
    omega
  have hc : U.card=∑ n ∈ Finset.range M,
      (U.filter (fun p => p.2.toNat-1=n)).card :=
    Finset.card_eq_sum_card_fiberwise hmap
  have hfiber (n : Nat) : U.filter (fun p => p.2.toNat-1=n)=
      U.filter (fun p => p.2=((n+1 : Nat) : Int)) := by
    ext p
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨hp,hn⟩
      have hy := hpos p hp
      have hycast := Int.toNat_of_nonneg hy.le
      exact ⟨hp,by omega⟩
    · rintro ⟨hp,hn⟩
      have hy := hpos p hp
      have hycast := Int.toNat_of_nonneg hy.le
      exact ⟨hp,by omega⟩
  simp_rw [hfiber] at hc
  have hcr : (U.card : Real)=∑ n ∈ Finset.range M,
      ((U.filter (fun p => p.2=((n+1 : Nat) : Int))).card : Real) := by
    exact_mod_cast hc
  have hanti : AntitoneOn (width a (4*a*c-b^2) t) (Set.Icc (0 : Real) (0+M)) :=
    (width_antitone a (4*a*c-b^2) t ha hD).mono (by intro x hx; exact hx.1)
  have hsum : (∑ n ∈ Finset.range M, width a (4*a*c-b^2) t ((n+1 : Nat) : Real)) ≤
      ∫ s in (0 : Real)..(M : Real), width a (4*a*c-b^2) t s := by
    simpa only [zero_add] using hanti.sum_le_integral
  have hcont := width_continuous a (4*a*c-b^2) t
  have hadd : (∫ s in (0 : Real)..(M : Real), width a (4*a*c-b^2) t s)+
      (∫ s in (M : Real)..Y, width a (4*a*c-b^2) t s)=
      ∫ s in (0 : Real)..Y, width a (4*a*c-b^2) t s :=
    intervalIntegral.integral_add_adjacent_intervals
      (hcont.intervalIntegrable (0 : Real) (M : Real)) (hcont.intervalIntegrable (M : Real) Y)
  have htail : 0 ≤ ∫ s in (M : Real)..Y, width a (4*a*c-b^2) t s :=
    intervalIntegral.integral_nonneg_of_forall hMY (fun s => width_nonneg a _ t s ha)
  have hint : (∫ s in (0 : Real)..(M : Real), width a (4*a*c-b^2) t s) ≤
      ∫ s in (0 : Real)..Y, width a (4*a*c-b^2) t s := by linarith
  calc
    _ = ∑ n ∈ Finset.range M,
        ((U.filter (fun p => p.2=((n+1 : Nat) : Int))).card : Real) := hcr
    _ ≤ ∑ n ∈ Finset.range M, (width a (4*a*c-b^2) t ((n+1 : Nat) : Real)+1) :=
      Finset.sum_le_sum (fun n hn => row_card U a b c t (n+1) ha hQ)
    _ = (∑ n ∈ Finset.range M, width a (4*a*c-b^2) t ((n+1 : Nat) : Real))+(M : Real) := by
      rw [Finset.sum_add_distrib]
      simp
    _ ≤ (∫ s in (0 : Real)..(M : Real), width a (4*a*c-b^2) t s)+(M : Real) :=
      add_le_add_right hsum _
    _ ≤ _ := add_le_add hint hMY

def reflect (p : Int × Int) : Int × Int := (-p.1,-p.2)

theorem reflect_injective : Function.Injective reflect := by
  intro p q he
  apply Prod.ext
  · simpa [reflect] using congrArg Prod.fst he
  · simpa [reflect] using congrArg Prod.snd he

theorem quad_reflect (a b c : Real) (p : Int × Int) :
    quad a b c (reflect p)=quad a b c p := by simp [quad,reflect]

theorem off_axis_count (U : Finset (Int × Int)) (a b c t : Real)
    (ha : 0 < a) (hD : 0 < 4*a*c-b^2) (ht : 0 ≤ t)
    (hQ : ∀ p ∈ U, quad a b c p ≤ t) (hy : ∀ p ∈ U, p.2 ≠ 0) :
    (U.card : Real) ≤ nonzeroBudget a (4*a*c-b^2) t := by
  classical
  let V := U.filter (fun p => 0 < p.2)
  let W := U.filter (fun p => ¬ 0 < p.2)
  have hc : V.card+W.card=U.card :=
    Finset.filter_card_add_filter_neg_card_eq_card (s:=U) (fun p => 0 < p.2)
  have hv := positive_rows V a b c t ha hD ht
    (fun p hp => (Finset.mem_filter.mp hp).2)
    (fun p hp => hQ p (Finset.mem_filter.mp hp).1)
  have hwpos : ∀ q ∈ W.image reflect, 0 < q.2 := by
    intro q hq
    obtain ⟨p,hp,rfl⟩ := Finset.mem_image.mp hq
    have hn := (Finset.mem_filter.mp hp).2
    have hz := hy p (Finset.mem_filter.mp hp).1
    dsimp [reflect]
    omega
  have hwQ : ∀ q ∈ W.image reflect, quad a b c q ≤ t := by
    intro q hq
    obtain ⟨p,hp,rfl⟩ := Finset.mem_image.mp hq
    rw [quad_reflect]
    exact hQ p (Finset.mem_filter.mp hp).1
  have hw := positive_rows (W.image reflect) a b c t ha hD ht hwpos hwQ
  have hwcard : (W.image reflect).card=W.card :=
    Finset.card_image_iff.mpr (fun p hp q hq he => reflect_injective he)
  rw [hwcard] at hw
  have hcr : (V.card : Real)+(W.card : Real)=(U.card : Real) := by exact_mod_cast hc
  unfold nonzeroBudget
  linarith

theorem circle_control : (2 : Real) ≤ nonzeroBudget 1 4 1 := by
  let U : Finset (Int × Int) := {(0,1),(0,-1)}
  have hQ : ∀ p ∈ U, quad 1 0 1 p ≤ 1 := by
    intro p hp
    simp only [U,Finset.mem_insert,Finset.mem_singleton] at hp
    rcases hp with rfl | rfl <;> norm_num [quad]
  have hy : ∀ p ∈ U, p.2 ≠ 0 := by
    intro p hp
    simp only [U,Finset.mem_insert,Finset.mem_singleton] at hp
    rcases hp with rfl | rfl <;> norm_num
  have hc := off_axis_count U 1 0 1 1 (by norm_num) (by norm_num) (by norm_num) hQ hy
  norm_num [U] at hc
  exact hc

theorem empty_control (a D t : Real) (ha : 0 < a) :
    ((∅ : Finset (Int × Int)).card : Real) ≤ nonzeroBudget a D t := by
  have hY : 0 ≤ height a D t := Real.sqrt_nonneg _
  have hi : 0 ≤ ∫ s in (0 : Real)..height a D t, width a D t s :=
    intervalIntegral.integral_nonneg_of_forall hY (fun s => width_nonneg a D t s ha)
  simp only [Finset.card_empty,Nat.cast_zero]
  unfold nonzeroBudget
  linarith

theorem zero_row_guard_control : quad 1 0 1 (0,0) ≤ 0 ∧
    ¬ (1 : Real) ≤ nonzeroBudget 1 4 0 := by
  norm_num [quad,nonzeroBudget,height]

end
end TenthDiscriminant.QuadraticRows

#audit_namespace TenthDiscriminant.QuadraticRows
#print axioms TenthDiscriminant.QuadraticRows.off_axis_count
