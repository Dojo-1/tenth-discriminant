import TenthDiscriminant.MaximalOrderCoordinates

/-! Integer coordinates for the trace-zero chart. The congruence guard is
essential: d=3 has half-integral integers and is not covered here. -/
namespace TenthDiscriminant
set_option autoImplicit false

private theorem evenChart_square_mod_four (m : Int) : m^2%4=m%2 := by
  rcases Int.even_or_odd' m with ⟨u, rfl | rfl⟩
  · have h : (2*u)^2=4*u^2 := by ring
    rw [h]
    omega
  · have h : (2*u+1)^2=4*(u^2+u)+1 := by ring
    rw [h]
    omega

theorem evenChart_parity (d m n : Int) (hd : d%4=1 ∨ d%4=2)
    (h : 4 ∣ m^2+d*n^2) : 2 ∣ m ∧ 2 ∣ n := by
  have hm := evenChart_square_mod_four m
  have hn := evenChart_square_mod_four n
  have h4 := Int.emod_eq_zero_of_dvd h
  rw [Int.add_emod, Int.mul_emod, hm, hn] at h4
  rcases hd with hd | hd <;> rw [hd] at h4 <;> omega

theorem evenChart_integral_coordinates (d : Nat) (hsq : Squarefree d)
    (hmod : (d : Int)%4=1 ∨ (d : Int)%4=2) (a b : Rat)
    (ht : ∃ m : Int, 2*a=(m : Rat))
    (hn : ∃ k : Int, a^2+(d : Rat)*b^2=(k : Rat)) :
    ∃ x y : Int, a=(x : Rat) ∧ b=(y : Rat) := by
  obtain ⟨m, hm⟩ := ht
  obtain ⟨k, hk⟩ := hn
  have hm2 : (2*a)^2=(m : Rat)^2 := congrArg (·^2) hm
  have hb2 : (d : Rat)*(2*b)^2=((4*k-m^2 : Int) : Rat) := by
    push_cast
    nlinarith
  obtain ⟨n, hn⟩ := squarefree_rational_coefficient_integral d hsq (2*b) ⟨_, hb2⟩
  have hq : ((m^2+(d : Int)*n^2 : Int) : Rat)=((4*k : Int) : Rat) := by
    calc
      _ = (m : Rat)^2+(d : Rat)*(n : Rat)^2 := by push_cast; ring
      _ = (2*a)^2+(d : Rat)*(2*b)^2 := by rw [hm, hn]
      _ = 4*(a^2+(d : Rat)*b^2) := by ring
      _ = ((4*k : Int) : Rat) := by rw [hk]; push_cast; ring
  have hi : m^2+(d : Int)*n^2=4*k := by exact_mod_cast hq
  obtain ⟨hmEven, hnEven⟩ := evenChart_parity d m n hmod
    (by rw [hi]; exact dvd_mul_right 4 k)
  obtain ⟨x, hx⟩ := hmEven
  obtain ⟨y, hy⟩ := hnEven
  have hxq : (m : Rat)=2*(x : Rat) := by exact_mod_cast hx
  have hyq : (n : Rat)=2*(y : Rat) := by exact_mod_cast hy
  exact ⟨x, y, by linarith, by linarith⟩

theorem evenChart_norm_nonneg (d : Nat) (x y : Int) :
    0 ≤ x^2+(d : Int)*y^2 := by positivity

theorem evenChart_no_norm_two (d : Nat) (hd : 2 < d) (x y : Int) :
    x^2+(d : Int)*y^2 ≠ 2 := by
  intro h
  by_cases hy : y=0
  · subst y
    have hm := evenChart_square_mod_four x
    norm_num at h
    rw [h] at hm
    omega
  · have hy1 : 1 ≤ y^2 := by
      have hp : 0 < y^2 := sq_pos_of_ne_zero hy
      omega
    have hdi : (2 : Int) < d := by exact_mod_cast hd
    have hm := mul_le_mul_of_nonneg_left hy1 (show (0 : Int) ≤ d by omega)
    nlinarith [sq_nonneg x]

theorem evenChart_exceptional_norm_two :
    (1 : Int)^2+1*1^2=2 ∧ (0 : Int)^2+2*1^2=2 := by norm_num

theorem evenChart_mod_guard_counterexample :
    2*(1/2 : Rat)=1 ∧ (1/2 : Rat)^2+3*(1/2 : Rat)^2=1 ∧
      ¬ ∃ n : Int, (1/2 : Rat)=(n : Rat) := by
  refine ⟨by norm_num, by norm_num, ?_⟩
  rintro ⟨n, hn⟩
  have hden := congrArg Rat.den hn
  norm_num at hden

end TenthDiscriminant
