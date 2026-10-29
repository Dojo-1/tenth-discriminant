import TenthDiscriminant

/-! Quantitative radial observations. The polynomial and its ordinary derivatives
are the production RadialOperator objects. No new Gram or divisor is introduced.
Phase118 preregistration: 7378fa5557d5ab13139295cf945e4d81ab4815c2.
The global determinant aggregation and actual-field cutoff are later obligations. -/
open Polynomial
open scoped BigOperators ComplexConjugate Classical
namespace TenthDiscriminant.RadialJetMajorant
set_option autoImplicit false
noncomputable section

/-- Every Leibniz term, including terms whose descending factorial is zero. -/
def coefficient (r s j : Nat) (h : Real) : Real :=
  ∑ k ∈ Finset.range (s+1),
    (s.choose k : Real) * (j.descFactorial k : Real) *
      ((r-s).descFactorial (j-k) : Real) * h^(s-k)

/-- Actual ordinary Z-derivative, holding W fixed before setting W=conjugate Z. -/
def jet (a : Int) (r s j : Nat) (z : Complex) : Complex :=
  ((derivative^[j]) (RadialOperator.polynomial a (conj z) r s)).eval z

private theorem sum_same_support {A : Type*} [AddCommMonoid A]
    (f : Nat → A) (n m : Nat)
    (hn : ∀ k, n < k → f k=0) (hm : ∀ k, m < k → f k=0) :
    ∑ k ∈ Finset.range (n+1), f k = ∑ k ∈ Finset.range (m+1), f k := by
  have extend (a b : Nat) (ha : ∀ k, a < k → f k=0) :
      ∑ k ∈ Finset.range (a+1), f k = ∑ k ∈ Finset.range (a+b+1), f k := by
    apply Finset.sum_subset (Finset.range_mono (by omega))
    intro k hk hka
    apply ha k
    have := Finset.mem_range.not.mp hka
    omega
  rw [extend n m hn, extend m n hm, Nat.add_comm m n]

private theorem choose_falling (j s k : Nat) :
    j.choose k * s.descFactorial k = s.choose k * j.descFactorial k := by
  rw [Nat.descFactorial_eq_factorial_mul_choose, Nat.descFactorial_eq_factorial_mul_choose]
  ring

private theorem falling_ratio (r s j k : Nat) (hj : j ≤ r) (hk : k ≤ j) :
    ((r-s).descFactorial (j-k) : Real) * (j.descFactorial k : Real) ≤
      (r.descFactorial j : Real) * ((j : Real)/(r-j+1 : Nat))^k := by
  have hd : (0 : Real) < (r-j+1 : Nat) := by positivity
  have hlow : (r-j+1)^k ≤ (r-(j-k)).descFactorial k := by
    have h := Nat.pow_sub_le_descFactorial (r-(j-k)) k
    have he : r-(j-k)+1-k=r-j+1 := by omega
    simpa only [he] using h
  have ha := Nat.descFactorial_le (j-k) (Nat.sub_le r s)
  have hsplit := Nat.descFactorial_mul_descFactorial (n:=r) (m:=j) (k:=j-k)
    (Nat.sub_le j k)
  have he : j-(j-k)=k := by omega
  rw [he] at hsplit
  have hprod : (r-s).descFactorial (j-k) * (r-j+1)^k ≤ r.descFactorial j := by
    calc
      _ ≤ r.descFactorial (j-k) * (r-(j-k)).descFactorial k := Nat.mul_le_mul ha hlow
      _ = _ := by nlinarith only [hsplit]
  have hprod' : ((r-s).descFactorial (j-k) : Real) * (r-j+1 : Nat)^k ≤
      (r.descFactorial j : Real) := by exact_mod_cast hprod
  have hjpow : (j.descFactorial k : Real) ≤ (j : Real)^k := by
    exact_mod_cast Nat.descFactorial_le_pow j k
  rw [div_pow, ← mul_div_assoc]
  apply (le_div_iff₀ (pow_pos hd k)).2
  calc
    _ = (((r-s).descFactorial (j-k) : Real) * (r-j+1 : Nat)^k) *
        (j.descFactorial k : Real) := by ring
    _ ≤ (r.descFactorial j : Real) * (j : Real)^k :=
      mul_le_mul hprod' hjpow (by positivity) (by positivity)

/-- The denominator is positive because j≤r; no term is omitted. -/
theorem coefficient_bound (r s j : Nat) (h : Real) (hh : 0 ≤ h) (hj : j ≤ r) :
    coefficient r s j h ≤
      (r.descFactorial j : Real) * (h+(j : Real)/(r-j+1 : Nat))^s := by
  unfold coefficient
  calc
    _ ≤ ∑ k ∈ Finset.range (s+1), (s.choose k : Real) *
        ((r.descFactorial j : Real) * ((j : Real)/(r-j+1 : Nat))^k) * h^(s-k) := by
      apply Finset.sum_le_sum
      intro k hk
      by_cases hkj : k ≤ j
      · have hr := falling_ratio r s j k hj hkj
        have he := mul_le_mul_of_nonneg_left hr (show (0 : Real) ≤ s.choose k by positivity)
        have hf := mul_le_mul_of_nonneg_right he (pow_nonneg hh (s-k))
        convert hf using 1 <;> ring
      · rw [Nat.descFactorial_of_lt (by omega : j < k)]
        simp only [Nat.cast_zero, mul_zero, zero_mul]
        positivity
    _ = _ := by
      rw [add_comm h, add_pow, Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro k hk
      ring

/-- All orders, over any commutative ring; these are ordinary derivatives. -/
theorem linear_power_derivative {A : Type*} [CommRing A] (w b : A) (s j : Nat) :
    (derivative^[j]) ((X*C w-C b)^s) =
      C ((s.descFactorial j : A)*w^j) * (X*C w-C b)^(s-j) := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [Function.iterate_succ_apply', ih, derivative_C_mul, derivative_pow]
    simp only [derivative_sub, derivative_mul, derivative_X, derivative_C,
      one_mul, mul_zero, sub_zero]
    rw [Nat.descFactorial_succ, Nat.cast_mul, pow_succ]
    have he : s-(j+1)=s-j-1 := by omega
    rw [he]
    simp only [map_mul]
    ring

/-- Exact Leibniz expansion with every column retained, even beyond the degree. -/
theorem leibniz_jet {A : Type*} [CommRing A] (a : Int) (r s j : Nat)
    (hrs : s ≤ r) (w z : A) :
    ((derivative^[j]) (RadialOperator.polynomial a w r s)).eval z =
      ∑ k ∈ Finset.range (s+1),
        ((s.choose k * j.descFactorial k * (r-s).descFactorial (j-k) : Nat) : A) *
          z^(r-s-(j-k)) * w^k * (z*w-(a : A))^(s-k) := by
  rw [RadialOperator.polynomial, min_eq_right hrs]
  simp only [Nat.sub_self, pow_zero, mul_one]
  rw [iterate_derivative_mul]
  simp only [eval_finset_sum, eval_smul, iterate_derivative_X_pow_eq_C_mul,
    linear_power_derivative, eval_mul, eval_pow, eval_C, eval_X, eval_sub]
  have hf (k : Nat) :
      j.choose k • (((((r-s).descFactorial (j-k) : A)*z^(r-s-(j-k))) *
        (((s.descFactorial k : A)*w^k)*(z*w-(a : A))^(s-k)))) =
        ((s.choose k * j.descFactorial k * (r-s).descFactorial (j-k) : Nat) : A) *
          z^(r-s-(j-k)) * w^k * (z*w-(a : A))^(s-k) := by
    rw [nsmul_eq_mul]
    have hc : (j.choose k : A)*(s.descFactorial k : A)=
        (s.choose k : A)*(j.descFactorial k : A) := by
      simpa only [Nat.cast_mul] using
        congrArg (fun n : Nat => (n : A)) (choose_falling j s k)
    push_cast
    calc
      _ = ((j.choose k : A)*(s.descFactorial k : A))*
          ((r-s).descFactorial (j-k) : A)*z^(r-s-(j-k))*w^k*(z*w-(a : A))^(s-k) := by ring
      _ = _ := by rw [hc]
  simp_rw [hf]
  apply sum_same_support
  · intro k hk
    simp [Nat.descFactorial_of_lt hk]
  · intro k hk
    simp [Nat.choose_eq_zero_of_lt hk]

theorem opposite_jet {A : Type*} [CommRing A] (a : Int) (r s j : Nat)
    (hrs : r ≤ s) (w z : A) :
    ((derivative^[j]) (RadialOperator.polynomial a w r s)).eval z =
      (r.descFactorial j : A)*w^(s-r+j)*(z*w-(a : A))^(r-j) := by
  rw [RadialOperator.polynomial, min_eq_left hrs]
  simp only [Nat.sub_self, pow_zero, one_mul]
  rw [← map_pow, iterate_derivative_C_mul, linear_power_derivative]
  simp only [eval_mul, eval_C, eval_pow, eval_sub, eval_X]
  rw [pow_add]
  ring

theorem coefficient_one (r s j : Nat) (hrs : s ≤ r) :
    coefficient r s j 1=(r.descFactorial j : Real) := by
  have h := leibniz_jet (A:=Real) 0 r s j hrs 1 1
  have hp : RadialOperator.polynomial 0 (1 : Real) r s=X^r := by
    simp [RadialOperator.polynomial, min_eq_right hrs, ← pow_add, Nat.sub_add_cancel hrs]
  rw [hp, iterate_derivative_X_pow_eq_C_mul] at h
  simpa [coefficient, Nat.cast_mul] using h.symm

theorem coefficient_no_loss (r s j : Nat) (h : Real) (hrs : s ≤ r)
    (hh : 0 ≤ h) (h1 : h ≤ 1) : coefficient r s j h ≤ (r.descFactorial j : Real) := by
  rw [← coefficient_one r s j hrs]
  unfold coefficient
  apply Finset.sum_le_sum
  intro k hk
  exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hh h1 (s-k)) (by positivity)

private theorem power_accounting (r s j k : Nat) (hrs : s ≤ r) (hj : j ≤ r)
    (hk : k ≤ s) (hkj : k ≤ j) (hrem : j-k ≤ r-s) (rho h : Real) :
    rho^(r-s-(j-k))*rho^k*(h*rho^2)^(s-k) = h^(s-k)*rho^(r+s-j) := by
  rw [mul_pow, ← pow_mul]
  calc
    _ = h^(s-k)*(rho^(r-s-(j-k))*rho^k*rho^(2*(s-k))) := by ring
    _ = _ := by
      rw [← pow_add, ← pow_add]
      congr 2
      omega

private theorem norm_le_coefficient (a : Int) (r s j : Nat) (hrs : s ≤ r)
    (hj : j ≤ r) (rho h : Real) (hrho : 0 ≤ rho) (hh : 0 ≤ h)
    (z : Complex) (hz : ‖z‖ ≤ rho)
    (hc : ‖z*conj z-(a : Complex)‖ ≤ h*rho^2) :
    ‖jet a r s j z‖ ≤ coefficient r s j h * rho^(r+s-j) := by
  unfold jet
  rw [leibniz_jet a r s j hrs, coefficient, Finset.sum_mul]
  apply (norm_sum_le _ _).trans
  apply Finset.sum_le_sum
  intro k hk
  have hks : k ≤ s := by have := Finset.mem_range.mp hk; omega
  by_cases hkj : k ≤ j
  · by_cases hrem : j-k ≤ r-s
    · simp only [norm_mul, norm_pow, RCLike.norm_natCast, Complex.norm_conj,
        Nat.cast_mul]
      have hp := power_accounting r s j k hrs hj hks hkj hrem rho h
      calc
        _ = ((s.choose k : Real)*(j.descFactorial k : Real)*
            ((r-s).descFactorial (j-k) : Real))*
            (‖z‖^(r-s-(j-k))*‖z‖^k*‖z*conj z-(a : Complex)‖^(s-k)) := by ring
        _ ≤ ((s.choose k : Real)*(j.descFactorial k : Real)*
            ((r-s).descFactorial (j-k) : Real))*
            (rho^(r-s-(j-k))*rho^k*(h*rho^2)^(s-k)) := by
          apply mul_le_mul_of_nonneg_left _ (by positivity)
          have hza := pow_le_pow_left₀ (norm_nonneg z) hz (r-s-(j-k))
          have hzk := pow_le_pow_left₀ (norm_nonneg z) hz k
          have hqc := pow_le_pow_left₀ (norm_nonneg (z*conj z-(a : Complex))) hc (s-k)
          have hzz := mul_le_mul hza hzk (by positivity) (by positivity)
          exact mul_le_mul hzz hqc (by positivity) (by positivity)
        _ = _ := by rw [hp]; ring
    · rw [Nat.descFactorial_of_lt (by omega : r-s < j-k)]
      simp
  · rw [Nat.descFactorial_of_lt (by omega : j < k)]
    simp

/-- Integer rounding is included; radius5 already prevents an exact-half claim. -/
theorem centered_disc (rho : Nat) (hrho : 5 ≤ rho) (z : Complex) (hz : ‖z‖ ≤ rho) :
    ‖z*conj z-((rho^2/2 : Nat) : Complex)‖ ≤ (13/25 : Real)*(rho : Real)^2 := by
  have hmod := Nat.mod_lt (rho^2) (by decide : 0 < 2)
  have hdiv := Nat.mod_add_div (rho^2) 2
  have hlo : 2*(rho^2/2) ≤ rho^2 := by omega
  have hhi : rho^2 ≤ 2*(rho^2/2)+1 := by omega
  have hlo' : 2*((rho^2/2 : Nat) : Real) ≤ (rho : Real)^2 := by exact_mod_cast hlo
  have hhi' : (rho : Real)^2 ≤ 2*((rho^2/2 : Nat) : Real)+1 := by exact_mod_cast hhi
  have hrho' : (5 : Real) ≤ rho := by exact_mod_cast hrho
  have hn0 : 0 ≤ ‖z‖^2 := sq_nonneg ‖z‖
  have hn1 : ‖z‖^2 ≤ (rho : Real)^2 := by nlinarith [norm_nonneg z]
  have he : z*conj z-((rho^2/2 : Nat) : Complex) =
      ((‖z‖^2-((rho^2/2 : Nat) : Real) : Real) : Complex) := by
    rw [Complex.mul_conj']
    push_cast
    rfl
  rw [he, Complex.norm_real, Real.norm_eq_abs]
  apply abs_le.mpr
  constructor <;> nlinarith [sq_nonneg ((rho : Real)-5)]

private theorem center_int (rho : Nat) (hrho : 5 ≤ rho) (z : Complex) (hz : ‖z‖ ≤ rho) :
    ‖z*conj z-(((rho^2/2 : Nat) : Int) : Complex)‖ ≤ (13/25 : Real)*(rho : Real)^2 := by
  simpa using centered_disc rho hrho z hz

/-- The old uniform envelope is retained, also for r<s and at the origin. -/
theorem ordinary_jet_no_loss (rho : Nat) (hrho : 5 ≤ rho) (r s j : Nat) (hj : j ≤ r)
    (z : Complex) (hz : ‖z‖ ≤ rho) :
    ‖jet (rho^2/2 : Nat) r s j z‖ ≤ (r.descFactorial j : Real)*(rho : Real)^(r+s-j) := by
  by_cases hrs : s ≤ r
  · exact (norm_le_coefficient _ r s j hrs hj rho (13/25) (by positivity)
      (by norm_num) z hz (center_int rho hrho z hz)).trans
      (mul_le_mul_of_nonneg_right (coefficient_no_loss r s j (13/25) hrs
        (by norm_num) (by norm_num)) (by positivity))
  · have hsr : r ≤ s := by omega
    unfold jet
    rw [opposite_jet _ r s j hsr]
    simp only [norm_mul, norm_pow, RCLike.norm_natCast, Complex.norm_conj]
    have hc := center_int rho hrho z hz
    have hpow : (13/25 : Real)^(r-j) ≤ 1 := by
      simpa using pow_le_pow_left₀ (by norm_num : (0 : Real) ≤ 13/25)
        (by norm_num : (13/25 : Real) ≤ 1) (r-j)
    calc
      _ ≤ (r.descFactorial j : Real)*(rho : Real)^(s-r+j)*
          ((13/25 : Real)*(rho : Real)^2)^(r-j) := by gcongr
      _ = (r.descFactorial j : Real)*(13/25 : Real)^(r-j)*
          (rho : Real)^(r+s-j) := by
        rw [mul_pow, ← pow_mul]
        have he : s-r+j+2*(r-j)=r+s-j := by omega
        calc
          _ = (r.descFactorial j : Real)*(13/25 : Real)^(r-j)*
              ((rho : Real)^(s-r+j)*(rho : Real)^(2*(r-j))) := by ring
          _ = _ := by rw [← pow_add, he]
      _ ≤ _ := by
        have h := mul_le_mul_of_nonneg_left hpow
          (show (0 : Real) ≤ r.descFactorial j by positivity)
        have h' := mul_le_mul_of_nonneg_right h
          (show (0 : Real) ≤ (rho : Real)^(r+s-j) by positivity)
        simpa only [mul_one] using h'

/-- High derivatives vanish for the actual polynomial, without any radius guard. -/
theorem high_jet_zero (a : Int) (r s j : Nat) (hj : r < j) (z : Complex) :
    jet a r s j z=0 := by
  unfold jet
  rw [RadialOperator.polynomial_expansion]
  simp only [iterate_derivative_sum, iterate_derivative_smul, eval_finset_sum, eval_smul]
  apply Finset.sum_eq_zero
  intro t ht
  have hd : r-t < j := by omega
  have he : (X^(r-t)*C (conj z)^(s-t) : Complex[X]) =
      C ((conj z)^(s-t))*X^(r-t) := by simp [mul_comm]
  rw [he, iterate_derivative_C_mul, iterate_derivative_X_pow_eq_C_mul,
    Nat.descFactorial_of_lt hd]
  simp

/-- All derivative columns in the eligible rows obtain the same radial saving. -/
theorem ordinary_jet_gain (rho : Nat) (hrho : 5 ≤ rho) (S r s j : Nat)
    (hS : 1 ≤ S) (hs : s < S) (hj : j < S) (hr : 9*S ≤ r)
    (z : Complex) (hz : ‖z‖ ≤ rho) :
    ‖jet (rho^2/2 : Nat) r s j z‖ ≤
      (13/20 : Real)^s*(r.descFactorial j : Real)*(rho : Real)^(r+s-j) := by
  have hrs : s ≤ r := by omega
  have hjr : j ≤ r := by omega
  have hd : (0 : Real) < (r-j+1 : Nat) := by positivity
  have hratio : (j : Real)/(r-j+1 : Nat) ≤ 1/8 := by
    apply (div_le_iff₀ hd).2
    have h : 8*j ≤ r-j+1 := by omega
    have h' : (8 : Real)*j ≤ (r-j+1 : Nat) := by exact_mod_cast h
    nlinarith
  have hbase : (13/25 : Real)+(j : Real)/(r-j+1 : Nat) ≤ 13/20 := by linarith
  have hp : ((13/25 : Real)+(j : Real)/(r-j+1 : Nat))^s ≤ (13/20 : Real)^s :=
    pow_le_pow_left₀ (by positivity) hbase s
  calc
    _ ≤ coefficient r s j (13/25)*(rho : Real)^(r+s-j) :=
      norm_le_coefficient _ r s j hrs hjr rho (13/25) (by positivity) (by norm_num)
        z hz (center_int rho hrho z hz)
    _ ≤ ((r.descFactorial j : Real)*
        ((13/25 : Real)+(j : Real)/(r-j+1 : Nat))^s)*(rho : Real)^(r+s-j) :=
      mul_le_mul_of_nonneg_right (coefficient_bound r s j (13/25) (by norm_num) hjr)
        (by positivity)
    _ ≤ _ := by
      have h := mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hp (show (0 : Real) ≤ r.descFactorial j by positivity))
        (show (0 : Real) ≤ (rho : Real)^(r+s-j) by positivity)
      convert h using 1 <;> ring

theorem logarithm_gain : (43/100 : Real) ≤ Real.log (20/13 : Real) := by
  have hc : checkPositiveLogBounds 2 (20/13) 0 (43/100) (44/100)=true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
      oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]
  have h := (checkPositiveLogBounds_sound 2 (20/13) 0 (43/100) (44/100) hc).1
  push_cast at h
  exact h

/-- Exact rectangular row savings, before division by the positive scale R²S. -/
theorem scale_gain (R S : Nat) (hS : 100 ≤ S) (hlo : 25*S ≤ R) (hhi : R ≤ 26*S) :
    (R^2*S : Nat)/ (100 : Real) ≤
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
  have hS' : (100 : Real) ≤ S := by exact_mod_cast hS
  have hlo' : (25 : Real)*S ≤ R := by exact_mod_cast hlo
  have hhi' : (R : Real) ≤ 26*S := by exact_mod_cast hhi
  have h9 : 9*S ≤ R := by omega
  have h1 : 1 ≤ S := by omega
  rw [Nat.cast_sub h9, Nat.cast_sub h1]
  push_cast
  have hR0 : (0 : Real) ≤ (R : Real)-9*S := by nlinarith
  have hSm1 : (0 : Real) ≤ (S : Real)-1 := by linarith
  have hpart : (16*(S : Real))*(S : Real)*(99/100*(S : Real)) ≤
      ((R : Real)-9*S)*S*((S : Real)-1) := by
    apply mul_le_mul
    · exact mul_le_mul_of_nonneg_right (by nlinarith : 16*(S : Real) ≤ (R : Real)-9*S)
        (by positivity)
    · nlinarith
    · positivity
    · positivity
  have hprod := mul_le_mul hpart logarithm_gain (by norm_num : (0 : Real) ≤ 43/100)
    (by positivity : 0 ≤ ((R : Real)-9*S)*S*((S : Real)-1))
  have hR2 : (R : Real)^2 ≤ 676*(S : Real)^2 := by
    have h := mul_le_mul hhi' hhi' (show (0 : Real) ≤ R by positivity)
      (show (0 : Real) ≤ 26*(S : Real) by positivity)
    nlinarith only [h]
  have hup := mul_le_mul_of_nonneg_right hR2 (show (0 : Real) ≤ S by positivity)
  nlinarith [pow_nonneg (show (0 : Real) ≤ S by positivity) 3]

theorem endpoint_separation (u : Real) (hu : 245813/10000 ≤ u) :
    (4/5*u-823/1000)+1862561/10000000000 ≤ 999997/1000000*u-5739/1000 := by
  linarith

theorem coefficient_controls : coefficient 1 1 1 (13/25)=1 ∧
    ¬(coefficient 1 1 1 (13/25) ≤ (13/25 : Real)) := by
  norm_num [coefficient, Finset.sum_range_succ, Nat.descFactorial]

theorem zero_s_control (r j : Nat) : coefficient r 0 j (13/25)=(r.descFactorial j : Real) := by
  simp [coefficient]

theorem ordinary_controls :
    (RadialOperator.polynomial 3 (1 : Int) 1 1).eval 0 = -3 ∧
    ((derivative^[1]) (RadialOperator.polynomial 3 (1 : Int) 1 1)).eval 1=1 ∧
    ((derivative^[2]) (RadialOperator.polynomial 3 (1 : Int) 2 1)).eval 1=2 := by
  norm_num [RadialOperator.polynomial, Function.iterate_succ_apply, derivative_sub,
    derivative_mul, derivative_pow, eval_mul, eval_sub]

theorem rounding_control : (5^2/2 : Nat)=12 ∧
    ((5^2 : Nat)-(5^2/2 : Nat) : Real)/25=13/25 ∧ (1/2 : Real)<13/25 := by norm_num

theorem single_column_control (R : Nat) :
    (R-9*1 : Nat)*(1 : Real)*(1-1 : Nat)*Real.log (20/13 : Real)=0 := by norm_num

theorem negative_endpoint_control :
    ¬(4/5*(2458/100 : Real)-823/1000 < 999997/1000000*(2458/100)-5739/1000) := by
  norm_num

end
end TenthDiscriminant.RadialJetMajorant

/-! Phase119: the actual integral determinant at the unchanged production radius.
The preceding Phase118 namespace is an exact local dependency, not a new model. -/
namespace TenthDiscriminant.RadialDetBound
open Polynomial FirstCertificate
open scoped BigOperators ComplexConjugate Classical
set_option autoImplicit false
noncomputable section

/-- Additive coordinate chart only; no complex-to-residue-field map is used. -/
def chart (D : Nat) : Zsqrtd (-(D : Int)) →+ Complex where
  toFun v := pairEval D (v.re,v.im)
  map_zero' := by simp [pairEval,latticePoint]
  map_add' v w := by
    apply Complex.ext <;> simp [pairEval,latticePoint,add_mul]

theorem chart_pair (D : Nat) (q : Int × Int) :
    chart D (pairZsqrtdEquiv D q)=pairEval D q := by rfl

theorem actual_jet_value (D R S : Nat) (a : Int) (i : Fin (R*S))
    (q : Int × Int) (j : Nat) :
    chart D (RadialOperator.integerJet D R S a i q j)=
      RadialJetMajorant.jet a (i.val/S) (i.val%S) j (pairEval D q) := by
  calc
    _ = chart D (zsqrtdJetTransform (RadialOperator.matrix R S a)
        (rectangularCanonicalJet D R S) i q j) :=
      congrArg (chart D) (RadialOperator.integer_jet_action D R S a i q j).symm
    _ = ∑ h : Fin (R*S), RadialOperator.matrix R S a i h •
        derivativeRow (h.val/S) (h.val%S) j (pairEval D q) := by
      rw [zsqrtdJetTransform,map_sum]
      apply Finset.sum_congr rfl
      intro h hh
      rw [map_zsmul]
      congr 1
      change pairEval D (integerDerivativeRow D (h.val/S) (h.val%S) j q)=_
      exact integerDerivativeRow_eval D (h.val/S) (h.val%S) j q
    _ = _ := RadialOperator.complex_jet_action R S a i (pairEval D q) j

theorem trace_square (D : Nat) (v : Zsqrtd (-(D : Int))) :
    (zsqrtdTrace D v v : Real)=2*‖chart D v‖^2 := by
  have h := integerPairTrace_cast D (v.re,v.im) (v.re,v.im)
  change (zsqrtdTrace D v v : Real)=2*‖pairEval D (v.re,v.im)‖^2
  simpa only [integerPairTrace,zsqrtdTrace,Complex.mul_conj',← Complex.ofReal_pow,
    Complex.ofReal_re] using h

/-- The original factor2 and original sample/derivative indexing, entrywise. -/
theorem actual_diagonal (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int)
    (i : Fin (R*S)) :
    ((RadialOperator.gram Q D J R S a).map (Int.castRingHom Real)) i i =
      2*∑ j ∈ Finset.range J, ∑ q ∈ Q,
        ‖RadialJetMajorant.jet a (i.val/S) (i.val%S) j (pairEval D q)‖^2 := by
  change ((∑ j ∈ Finset.range J, ∑ q ∈ Q,
    zsqrtdTrace D (RadialOperator.integerJet D R S a i q j)
      (RadialOperator.integerJet D R S a i q j) : Int) : Real)=_
  push_cast
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro q hq
  rw [trace_square,actual_jet_value]

def rowFactor (S r s : Nat) : Real :=
  if 9*S ≤ r then (13/20 : Real)^(2*s) else 1

def rowPenalty (S r s : Nat) : Real :=
  if 9*S ≤ r then (2*s : Nat)*Real.log (20/13 : Real) else 0

def rowLog (S rho : Nat) (n : Real) (r s : Nat) : Real :=
  Real.log (2*n*S)+(2*(r+s) : Nat)*Real.log (rho : Real)+
    (2*(S-1) : Nat)*max 0 (Real.log ((r : Real)/rho))

theorem rowFactor_pos (S r s : Nat) : 0 < rowFactor S r s := by
  unfold rowFactor
  split_ifs <;> positivity

theorem rowFactor_log (S r s : Nat) :
    Real.log (rowFactor S r s) = -rowPenalty S r s := by
  unfold rowFactor rowPenalty
  split_ifs with h
  · rw [Real.log_pow]
    have he : (13/20 : Real)=(20/13 : Real)⁻¹ := by norm_num
    rw [he,Real.log_inv]
    ring
  · simp

/-- Actual squared jets, with both the old radius and derivative correction. -/
theorem actual_jet_square (rho S r s j : Nat) (hrho : 5 ≤ rho) (hS : 1 ≤ S)
    (hs : s < S) (hj : j < S) (z : Complex) (hz : ‖z‖ ≤ rho) :
    ‖RadialJetMajorant.jet (rho^2/2 : Nat) r s j z‖^2 ≤
      rowFactor S r s * ((rho : Real)^(2*(r+s))*
        (max 1 ((r : Real)/rho))^(2*(S-1))) := by
  have hf := (rowFactor_pos S r s).le
  by_cases hjr : j ≤ r
  · have hsq : ‖RadialJetMajorant.jet (rho^2/2 : Nat) r s j z‖^2 ≤
        rowFactor S r s*((r.descFactorial j : Real)^2*(rho : Real)^(2*(r+s-j))) := by
      by_cases he : 9*S ≤ r
      · have h := RadialJetMajorant.ordinary_jet_gain rho hrho S r s j hS hs hj he z hz
        have hp := pow_le_pow_left₀ (norm_nonneg _) h 2
        rw [rowFactor,if_pos he]
        convert hp using 1
        simp only [mul_pow,← pow_mul,Nat.mul_comm s 2,Nat.mul_comm (r+s-j) 2]
        ring
      · have h := RadialJetMajorant.ordinary_jet_no_loss rho hrho r s j hjr z hz
        have hp := pow_le_pow_left₀ (norm_nonneg _) h 2
        rw [rowFactor,if_neg he,one_mul]
        convert hp using 1
        simp only [mul_pow,← pow_mul,Nat.mul_comm (r+s-j) 2]
    exact hsq.trans (mul_le_mul_of_nonneg_left
      (radial_derivative_term_le rho r s S j (by omega) hjr hj) hf)
  · rw [RadialJetMajorant.high_jet_zero _ r s j (by omega) z]
    simp only [norm_zero,zero_pow (by decide : 2 ≠ 0)]
    positivity

theorem actual_diagonal_uniform (Q : Finset (Int × Int)) (D R S rho : Nat)
    (hrho : 5 ≤ rho) (hS : 1 ≤ S)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) (i : Fin (R*S)) :
    ((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map (Int.castRingHom Real)) i i ≤
      rowFactor S (i.val/S) (i.val%S)*
        (2*(Q.card : Real)*S*(rho : Real)^(2*(i.val/S+i.val%S))*
          (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1))) := by
  let B := rowFactor S (i.val/S) (i.val%S)*
    ((rho : Real)^(2*(i.val/S+i.val%S))*
      (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1)))
  rw [actual_diagonal]
  calc
    _ ≤ 2*∑ j ∈ Finset.range S, ∑ q ∈ Q, B := by
      apply mul_le_mul_of_nonneg_left _ (by norm_num)
      apply Finset.sum_le_sum
      intro j hj
      apply Finset.sum_le_sum
      intro q hq
      exact actual_jet_square rho S (i.val/S) (i.val%S) j hrho hS
        (Nat.mod_lt _ (by omega)) (Finset.mem_range.mp hj) (pairEval D q) (hbound q hq)
    _ = _ := by
      simp only [Finset.sum_const,Finset.card_range,nsmul_eq_mul]
      dsimp only [B]
      ring

theorem actual_log_diagonal (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hrho : 5 ≤ rho) (hS : 1 ≤ S) (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) (i : Fin (R*S))
    (hpos : 0 < ((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map
      (Int.castRingHom Real)) i i) :
    Real.log (((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map
      (Int.castRingHom Real)) i i) ≤
      rowLog S rho n (i.val/S) (i.val%S)-rowPenalty S (i.val/S) (i.val%S) := by
  have hf := rowFactor_pos S (i.val/S) (i.val%S)
  have hn' : rowFactor S (i.val/S) (i.val%S)*
      (2*(Q.card : Real)*S*(rho : Real)^(2*(i.val/S+i.val%S))*
        (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1))) ≤
      rowFactor S (i.val/S) (i.val%S)*
      (2*n*S*(rho : Real)^(2*(i.val/S+i.val%S))*
        (max 1 (((i.val/S : Nat) : Real)/rho))^(2*(S-1))) := by gcongr
  have hl := Real.log_le_log hpos ((actual_diagonal_uniform Q D R S rho hrho hS hbound i).trans hn')
  rw [Real.log_mul hf.ne' (by positivity),rowFactor_log,
    Real.log_mul (by positivity) (by positivity),Real.log_mul (by positivity) (by positivity),
    Real.log_pow,Real.log_pow,log_max_one_ratio rho (i.val/S) (by omega)] at hl
  unfold rowLog
  linarith

private theorem tail_sum (K R : Nat) (c : Real) :
    (∑ r ∈ Finset.range R, if K ≤ r then c else 0)=(R-K : Nat)*c := by
  induction R with
  | zero => simp
  | succ R ih =>
    rw [Finset.sum_range_succ,ih]
    by_cases h : K ≤ R
    · rw [if_pos h]
      have he : R+1-K=R-K+1 := by omega
      rw [he]
      push_cast
      ring
    · have h0 : R-K=0 := by omega
      have h1 : R+1-K=0 := by omega
      simp [h,h0,h1]

/-- Natural subtraction gives zero when the eligible rectangle is empty. -/
theorem penalty_sum (R S : Nat) (hS : 1 ≤ S) :
    (∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S, rowPenalty S r s)=
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
  have inner (r : Nat) : (∑ s ∈ Finset.range S,rowPenalty S r s)=
      if 9*S ≤ r then (S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) else 0 := by
    by_cases h : 9*S ≤ r
    · simp only [rowPenalty,if_pos h,Nat.cast_mul,Nat.cast_ofNat]
      rw [← Finset.sum_mul,← Finset.mul_sum,sum_cast_range,Nat.cast_sub hS,Nat.cast_one]
      ring
    · simp [rowPenalty,h]
  simp_rw [inner]
  rw [tail_sum]
  ring

theorem baseline_sum (R S rho : Nat) (n : Real) (hrho : 0 < rho) (hRrho : rho < R) :
    (∑ r ∈ Finset.range R, ∑ s ∈ Finset.range S,rowLog S rho n r s) ≤
      enderUpperB R S S rho n := by
  unfold rowLog
  rw [rectangular_log_row_sum]
  have hcorr := log_derivative_correction_le_upperB rho R hrho hRrho
  have hscaled := mul_le_mul_of_nonneg_left hcorr
    (by positivity : (0 : Real) ≤ 2*S*((S-1 : Nat) : Real))
  unfold enderUpperB
  exact add_le_add_left hscaled _

/-- The logarithm is of the SAME original integer determinant. -/
theorem integer_log_upper (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S) (hrho : 5 ≤ rho) (hRrho : rho < R)
    (hcard : 2*(R-1)+(S-1) < Q.card) (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) :
    Real.log ((integerRectangularTraceGram Q D S R S).det : Real) ≤
      enderUpperB R S S rho n-
        (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
  let H := (RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map (Int.castRingHom Real)
  have hp : H.PosDef := RadialOperator.real_posDef Q D S R S _ hD hR hS le_rfl hcard
  have hd (i : Fin (R*S)) : 0 < H i i := real_posDef_diagonal_pos _ H hp i
  have hh := real_psd_det_le_diag (R*S) H hp.posSemidef
  have hl := Real.log_le_log hp.det_pos hh
  rw [Real.log_prod Finset.univ _ (fun i hi => (hd i).ne')] at hl
  have hrows : (∑ i : Fin (R*S),Real.log (H i i)) ≤
      ∑ i : Fin (R*S), (rowLog S rho n (i.val/S) (i.val%S)-
        rowPenalty S (i.val/S) (i.val%S)) := by
    apply Finset.sum_le_sum
    intro i hi
    exact actual_log_diagonal Q D R S rho n hrho hS hnpos hn hbound i (hd i)
  rw [Finset.sum_sub_distrib,rectangular_row_sum R S (rowLog S rho n),
    rectangular_row_sum R S (rowPenalty S),penalty_sum R S hS] at hrows
  have hb := baseline_sum R S rho n (by omega) hRrho
  have he : H.det=((integerRectangularTraceGram Q D S R S).det : Real) := by
    dsimp only [H]
    simpa only [RadialOperator.gram_det] using
      ((Int.castRingHom Real).map_det (RadialOperator.gram Q D S R S (rho^2/2 : Nat))).symm
  rw [he] at hl
  linarith

theorem normalized_integer_upper (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hD : 0 < D) (hS : 100 ≤ S) (h25 : 25*S ≤ R) (h26 : R ≤ 26*S)
    (hrho : 5 ≤ rho) (hRrho : rho < R) (hcard : 2*(R-1)+(S-1) < Q.card)
    (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho) :
    Real.log ((integerRectangularTraceGram Q D S R S).det : Real)/comparisonScale R S ≤
      enderUpperB R S S rho n/comparisonScale R S-1/100 := by
  have hu := integer_log_upper Q D R S rho n hD (by omega) (by omega) hrho
    hRrho hcard hnpos hn hbound
  have ht := comparisonScale_pos R S (by omega) (by omega)
  have hg : comparisonScale R S/100 ≤
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
    simpa only [comparisonScale,Nat.cast_mul,Nat.cast_pow] using RadialJetMajorant.scale_gain R S hS h25 h26
  have hgn : (1/100 : Real) ≤
      ((R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real))/comparisonScale R S := by
    apply (le_div_iff₀ ht).2
    simpa only [div_eq_mul_inv,mul_comm,one_mul] using hg
  calc
    _ ≤ (enderUpperB R S S rho n-
        (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real))/comparisonScale R S :=
      div_le_div_of_nonneg_right hu ht.le
    _ = _ := sub_div _ _ _
    _ ≤ _ := sub_le_sub_left hgn _

theorem production_guards (D : Nat) (hD : 41006250000 ≤ D) :
    100 ≤ Tuned.S D ∧ 25*Tuned.S D ≤ Tuned.R D ∧ Tuned.R D ≤ 26*Tuned.S D ∧
      5 ≤ Tuned.rho D := by
  have hd := Tuned.dimensions D hD
  have h25 : 25*Tuned.S D ≤ Tuned.R D := by unfold Tuned.S; omega
  have h26 : Tuned.R D ≤ 26*Tuned.S D := by unfold Tuned.S; omega
  refine ⟨by omega,h25,h26,?_⟩
  have hlo := (Tuned.radius_bounds D hD).1
  have hroot := Tuned.root_large D hD
  have hcube := pow_le_pow_left₀ (by norm_num : (0 : Real) ≤ 450) hroot 3
  have h5 : (5 : Real) ≤ Tuned.rho D := by nlinarith only [hlo,hcube]
  exact_mod_cast h5

/-- Actual determinant, actual chosen radius, all geometric-domain D; no class premise. -/
theorem production_normalized_upper (D : Nat) (hD : 41006250000 ≤ D) :
    Real.log ((integerRectangularTraceGram (ellipsePairs D (Tuned.rho D)) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real)/
      comparisonScale (Tuned.R D) (Tuned.S D) ≤ (4/5 : Real)*Real.log D-823/1000 := by
  obtain ⟨hS,h25,h26,h5⟩ := production_guards D hD
  have hd := Tuned.dimensions D hD
  have hD0 : 0 < D := by omega
  have hc := ellipsePairs_card_gt_of_ender_radius D (Tuned.rho D)
    (3*Tuned.R D+Tuned.S D) hD0 (by omega) (Tuned.chosen_radius D hD)
  have hcard : 2*(Tuned.R D-1)+(Tuned.S D-1) < (ellipsePairs D (Tuned.rho D)).card := by omega
  have hn := ellipsePairs_card_le_padded_upper_count D D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D)) hD0 le_rfl le_rfl
  have hnpos : 0 < ellipsePaddedUpperCount D (Tuned.rho D)
      (ellipseVerticalBound D (Tuned.rho D)) :=
    lt_of_lt_of_le (by exact_mod_cast (show 0 < (ellipsePairs D (Tuned.rho D)).card by omega)) hn
  have hbound (q : Int × Int) (hq : q ∈ ellipsePairs D (Tuned.rho D)) :
      ‖pairEval D q‖ ≤ Tuned.rho D := by
    apply ellipsePoint_norm_le D (Tuned.rho D) hD0
    exact Finset.mem_image.mpr ⟨q,hq,rfl⟩
  have hu := normalized_integer_upper (ellipsePairs D (Tuned.rho D)) D (Tuned.R D)
    (Tuned.S D) (Tuned.rho D) (ellipsePaddedUpperCount D (Tuned.rho D)
      (ellipseVerticalBound D (Tuned.rho D))) hD0 hS h25 h26 h5
      (Tuned.radius_lt_R D hD) hcard hnpos hn hbound
  linarith [Tuned.normalized_upper D hD]

theorem constant_trace_control : integerPairTrace 3 (1,0) (1,0)=2 := by
  norm_num [integerPairTrace]

theorem empty_rows_control (Q : Finset (Int × Int)) (D S rho : Nat) :
    (integerRectangularTraceGram Q D S 0 S).det=1 := by
  haveI : IsEmpty (Fin (0*S)) := by
    simpa only [Nat.zero_mul] using (inferInstance : IsEmpty (Fin 0))
  exact Matrix.det_isEmpty

theorem singleton_control :
    (integerRectangularTraceGram {(0,0)} 3 1 1 1).det=2 := by
  rw [Matrix.det_fin_one]
  norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,
    integerPairTrace,integerDerivativeRow,pairScale,pairMul,pairPow,Finset.sum_range_succ,
    Nat.descFactorial,Matrix.det_fin_one]

theorem singular_control :
    (integerRectangularTraceGram ∅ 3 1 1 1).det=0 := by
  rw [Matrix.det_fin_one]
  norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,Matrix.det_fin_one]

theorem origin_control :
    ‖RadialJetMajorant.jet 12 1 1 0 0‖^2=(144 : Real) ∧ derivativeRow 1 1 0 0=0 := by
  norm_num [RadialJetMajorant.jet,RadialOperator.polynomial,derivativeRow]

theorem single_column_control (R : Nat) :
    (∑ r ∈ Finset.range R,∑ s ∈ Finset.range 1,rowPenalty 1 r s)=0 := by
  rw [penalty_sum R 1 (by decide)]
  norm_num

theorem empty_eligible_control (R S : Nat) (hS : 1 ≤ S) (hR : R ≤ 9*S) :
    (∑ r ∈ Finset.range R,∑ s ∈ Finset.range S,rowPenalty S r s)=0 := by
  rw [penalty_sum R S hS,Nat.sub_eq_zero_of_le hR]
  simp

end
end TenthDiscriminant.RadialDetBound

/-! Phase120: arithmetic lower bound on the same integer and actual field cutoff.
The preceding118+119 bodies are exact accepted local dependencies. -/
namespace TenthDiscriminant.RadialCutoff
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

theorem integer_det_positive (Q : Finset (Int × Int)) (D R S : Nat)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hcard : 2*(R-1)+(S-1) < Q.card) :
    0 < (integerRectangularTraceGram Q D S R S).det := by
  have hcount : 2*(R-1)+(S-1) < (Q.image (pairEval D)).card := by
    rw [Finset.card_image_of_injective _ (show Function.Injective (pairEval D) from
      latticePoint_injective D hD)]
    exact hcard
  have hp : (0 : Real) < ((integerRectangularTraceGram Q D S R S).det : Real) := by
    rw [integerRectangularTraceGram_det_cast Q D S R S hD]
    exact (rectangularTraceGram_posDef_of_point_count (Q.image (pairEval D)) S R S
      hR hS le_rfl hcount).det_pos
  exact_mod_cast hp

/-- Each distinct prime contributes to the SAME positive original integer. -/
theorem prime_mass_log_lower (Q : Finset (Int × Int)) (D R S : Nat)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hcard : 2*(R-1)+(S-1) < Q.card) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    exactOddPrimeMass R S ≤ Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  let P := oddPrimesBelow R
  let z := (integerRectangularTraceGram Q D S R S).det
  have hz : 0 < z := integer_det_positive Q D R S hD hR hS hcard
  have hprime (p : Nat) (hp : p ∈ P) : p.Prime := (Finset.mem_filter.mp hp).2.1
  have hlocal (p : Nat) (hp : p ∈ P) : (p : Int)^(2*valuationWeight R S p) ∣ z := by
    letI : Fact p.Prime := ⟨hprime p hp⟩
    have hodd : p ≠ 2 := (Finset.mem_filter.mp hp).2.2
    have hpr : p < R := Finset.mem_range.mp (Finset.mem_filter.mp hp).1
    have hpri : (p : Int) < R := by exact_mod_cast hpr
    exact rectangularTraceGram_valuation_of_classNumber_one Q D S R S p hsq hodd
      (hpri.trans hRcut) hclass
  have hnat := primePowerProduct_le_det P (fun p => 2*valuationWeight R S p) z hz hprime hlocal
  have hint : ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Int) ≤ z := by
    have h : ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Int) ≤ (z.natAbs : Int) := by
      exact_mod_cast hnat
    simpa only [Int.natCast_natAbs,abs_of_pos hz] using h
  have hreal : ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Real) ≤ (z : Real) := by
    exact_mod_cast hint
  have hppos (p : Nat) (hp : p ∈ P) : (0 : Real) < p := by exact_mod_cast (hprime p hp).pos
  have hprodpos : (0 : Real) < ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Real) := by
    exact_mod_cast Finset.prod_pos (fun p hp => pow_pos (hprime p hp).pos (2*valuationWeight R S p))
  have hlog := Real.log_le_log hprodpos hreal
  have he : Real.log ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Real)=
      exactOddPrimeMass R S := by
    simp only [Nat.cast_prod,Nat.cast_pow]
    rw [Real.log_prod]
    · simp only [Real.log_pow,exactOddPrimeMass,P]
    · intro p hp
      exact (pow_pos (hppos p hp) _).ne'
  rw [he] at hlog
  exact hlog

theorem recovered_normalized_lower (D : Nat) (hD : 41006250000 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5739/1000 ≤
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) FirstEnderInterval.tailBudget /
        comparisonScale (Tuned.R D) (Tuned.S D) := by
  obtain ⟨hS,h25,h26,h5⟩ := RadialDetBound.production_guards D hD
  have hh := strong_raw_normalized_add_gain_le_recovered (Tuned.R D) (Tuned.S D)
    FirstEnderInterval.tailBudget hS h25 h26
  linarith [Tuned.normalized_lower D hD]

theorem recovered_mass_le_actual_log (D : Nat) (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1) :
    recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram (ellipsePairs D (Tuned.rho D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) := by
  have hd := Tuned.dimensions D hD
  have hs : 1 ≤ Tuned.S D := by omega
  have htail := certifiedPrimeMassLower_antitone_tail (Tuned.R D) (Tuned.S D) hs
    FirstEnderInterval.tail_le_budget
  have hrec : recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith
  have hprod := recoveredPrimeMassLower_le_production (Tuned.R D) (Tuned.S D)
    (enderTailIntegral 10000) (by omega) hs
  have hmass := enderPrimeMassLower_le_exact_production (Tuned.R D) (Tuned.S D) 10000
    (by omega) hs (by decide) hd.2.2.2.1
  have hc := ellipsePairs_card_gt_of_ender_radius D (Tuned.rho D)
    (3*Tuned.R D+Tuned.S D) (by omega) (by omega) (Tuned.chosen_radius D hD)
  have hcard : 2*(Tuned.R D-1)+(Tuned.S D-1) < (ellipsePairs D (Tuned.rho D)).card := by omega
  exact hrec.trans (hprod.trans (hmass.trans (prime_mass_log_lower (ellipsePairs D (Tuned.rho D))
    D (Tuned.R D) (Tuned.S D) (by omega) (by omega) hs hcard hsq hclass (Tuned.strict_inertness D))))

theorem endpoint_log_controls : (6931/10000 : Real) ≤ Real.log 2 ∧
    (1609/1000 : Real) ≤ Real.log 5 := by
  have h2c : checkPositiveLogBounds 4 2 1 (6931/10000) (6932/10000)=true := by
    norm_num [checkPositiveLogBounds,binaryLogLowerRat,binaryLogUpperRat,
      oddLogPrefixRat,oddLogRemainderRat,Finset.sum_range_succ]
  have h5c : checkPositiveLogBounds 4 5 2 (1609/1000) (161/100)=true := by
    norm_num [checkPositiveLogBounds,binaryLogLowerRat,binaryLogUpperRat,
      oddLogPrefixRat,oddLogRemainderRat,Finset.sum_range_succ]
  have h2 := (checkPositiveLogBounds_sound 4 2 1 (6931/10000) (6932/10000) h2c).1
  have h5 := (checkPositiveLogBounds_sound 4 5 2 (1609/1000) (161/100) h5c).1
  norm_num at h2 h5
  exact ⟨h2,h5⟩

theorem endpoint_log_lower (D : Nat) (hD : 48000000000 ≤ D) :
    (245813/10000 : Real) ≤ Real.log D := by
  have hb : (48000000000 : Real) ≤ D := by exact_mod_cast hD
  have hl := Real.log_le_log (by norm_num : (0 : Real) < 48000000000) hb
  have he : (48000000000 : Real)=2^13*3*5^9 := by norm_num
  rw [he,Real.log_mul (by norm_num : (2 : Real)^13*3 ≠ 0) (by norm_num : (5 : Real)^9 ≠ 0),
    Real.log_mul (by norm_num : (2 : Real)^13 ≠ 0) (by norm_num : (3 : Real) ≠ 0),
    Real.log_pow,Real.log_pow] at hl
  norm_num only [Nat.cast_ofNat] at hl
  linarith [endpoint_log_controls.1,endpoint_log_controls.2,recovery_log_controls.1]

/-- The new actual determinant upper and arithmetic lower are incompatible. -/
theorem odd_large_classNumber_ne_one_48b (D : Nat) (hD : 48000000000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≠1 := by
  intro hc
  have hgeom : 41006250000 ≤ D := by omega
  have hd := Tuned.dimensions D hgeom
  have hp := comparisonScale_pos (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hupper := RadialDetBound.production_normalized_upper D hgeom
  have hactual := div_le_div_of_nonneg_right (recovered_mass_le_actual_log D hgeom hsq hc) hp.le
  have hlower := recovered_normalized_lower D hgeom
  have hsep := RadialJetMajorant.endpoint_separation (Real.log D) (endpoint_log_lower D hD)
  linarith

theorem imaginaryQuadratic_large_classNumber_ne_one_48b (d : Nat)
    [Fact (0<d)] (hsq : Squarefree d) (hd : 48000000000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_48b d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

theorem imaginaryQuadratic_classNumber_one_discriminant_bound_48b
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs < 48000000000 := by
  have hrad : d < 48000000000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_48b d hsq (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter,ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter,if_neg hnot]
    omega

/-- No caller-supplied generator: actual absolute discriminant of ANY such field. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_48b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 48000000000 := by
  obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_48b d hsq hcan

theorem endpoint_identity : (2 : Nat)^13*3*5^9=48000000000 := by norm_num

theorem negative_endpoint_control :
    ¬(4/5*(2458/100 : Real)-823/1000 < 999997/1000000*(2458/100)-5739/1000) := by
  exact RadialJetMajorant.negative_endpoint_control

theorem empty_prime_product_control (e : Nat → Nat) :
    (∏ p ∈ (∅ : Finset Nat),p^e p)=1 := by simp

theorem duplicate_prime_control : ¬ (3 : Int)^2 ∣ (3 : Int) := by norm_num

theorem actual_even_discriminant_control (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hd : d=1 ∨ d=2) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs ≤ 8 := by
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases hd with rfl | rfl <;> norm_num [absoluteDiscriminantParameter]

end
end TenthDiscriminant.RadialCutoff

#audit_namespace TenthDiscriminant.RadialCutoff
#check TenthDiscriminant.RadialCutoff.integer_det_positive
#check TenthDiscriminant.RadialCutoff.prime_mass_log_lower
#check TenthDiscriminant.RadialCutoff.recovered_normalized_lower
#check TenthDiscriminant.RadialCutoff.recovered_mass_le_actual_log
#check TenthDiscriminant.RadialCutoff.endpoint_log_controls
#check TenthDiscriminant.RadialCutoff.endpoint_log_lower
#check TenthDiscriminant.RadialCutoff.odd_large_classNumber_ne_one_48b
#check TenthDiscriminant.RadialCutoff.imaginaryQuadratic_large_classNumber_ne_one_48b
#check TenthDiscriminant.RadialCutoff.imaginaryQuadratic_classNumber_one_discriminant_bound_48b
#check TenthDiscriminant.RadialCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_48b
#check TenthDiscriminant.RadialCutoff.endpoint_identity
#check TenthDiscriminant.RadialCutoff.negative_endpoint_control
#check TenthDiscriminant.RadialCutoff.empty_prime_product_control
#check TenthDiscriminant.RadialCutoff.duplicate_prime_control
#check TenthDiscriminant.RadialCutoff.actual_even_discriminant_control

open Lean Elab Command
elab "#phase120_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE120_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.FirstCertificate.Tuned.fifty_normalized_lower,
    ``TenthDiscriminant.FirstCertificate.Tuned.fifty_dimensions,
    ``TenthDiscriminant.ellipse_enderPrimeMassLower_le_counted_upperB,
    ``TenthDiscriminant.ellipse_enderPrimeMassLower_le_upperB,
    ``TenthDiscriminant.ellipse_primeMass_log_le_upperB,
    ``TenthDiscriminant.ellipse_primeMass_product_dvd,
    ``TenthDiscriminant.ellipse_primeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_log_le_hadamard,
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
    ``TenthDiscriminant.FirstCertificate.rawPrimeMassLower_uniform,
    ``TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two,
    ``TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound,
    ``TenthDiscriminant.ControlledClassCount.controlled_class_form_and_count,
    ``TenthDiscriminant.PrincipalBasis.principal_form_of_class,
    ``TenthDiscriminant.PrincipalBasis.principal_class_form_and_prime_count,
    ``TenthDiscriminant.ActualPrimeAxis.actual_axis_card_le_two,
    ``TenthDiscriminant.ActualPrimeAxis.controlled_class_prime_count,
    ``TenthDiscriminant.ControlledPrimeFamily.controlled_family,
    ``TenthDiscriminant.ControlledPrimeFamily.fixed_family_odd_four,
    ``TenthDiscriminant.ControlledPrimeFamily.fixed_family_finite,
    ``TenthDiscriminant.ResidueMultiplicity.actualResidueMap,
    ``TenthDiscriminant.ResidueMultiplicity.actual_residue_pair_ne,
    ``TenthDiscriminant.ClassAggregation.prime_prefix_bound,
    ``TenthDiscriminant.ClassAggregation.uniform_two_class_bound,
    ``TenthDiscriminant.SplitPrimeBudget.countBound,
    ``TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound,
    ``TenthDiscriminant.SplitPrimeBudget.actual_gram_budget,
    ``TenthDiscriminant.ClosedKernel.actual_majorant,
    ``TenthDiscriminant.ClosedKernel.closed_count_kernel,
    ``TenthDiscriminant.ClosedKernel.closed_actual_gram_budget,
    ``TenthDiscriminant.OddMinkowski.actual_minkowski,
    ``TenthDiscriminant.OddMinkowski.normalized_count_kernel,
    ``TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget,
    ``TenthDiscriminant.EvenTwoClass.even_classNumber_gt_two,
    ``TenthDiscriminant.EvenTwoClass.even_radicand_bound,
    ``TenthDiscriminant.EvenTwoClass.even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.parity_refined_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant,
    ``TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_cast,
    ``TenthDiscriminant.CoordinateTranslation.shifted_posDef,
    ``TenthDiscriminant.CoordinateTranslation.shifted_valuation,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE120_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE120_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE120_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE120_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE120_INPUTS_OK {target}: {count} reached;73forbidden roots excluded;axioms {state.axioms}"





#phase120_inputs TenthDiscriminant.RadialCutoff.prime_mass_log_lower
#phase120_inputs TenthDiscriminant.RadialCutoff.odd_large_classNumber_ne_one_48b
#phase120_inputs TenthDiscriminant.RadialCutoff.totallyComplex_degree_two_classNumber_one_discriminant_bound_48b
