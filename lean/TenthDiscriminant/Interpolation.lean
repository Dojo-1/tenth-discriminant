import TenthDiscriminant.JetCountGram

/-!
# Rectangular interpolation: the public entry point

For the original R-by-S monomial grid, callers provide only the distinct point
set, derivative depth, and numerical count conditions. The quotient/remainder
row enumeration and its injectivity are proved here, not delegated to callers.

Read HUMAN_GUIDE.md for the mathematical proof. This file does not construct an
ellipse, identify an integer matrix, or prove a class-number statement.
-/
namespace TenthDiscriminant
open Matrix
noncomputable section

/-- Quotient and remainder recover the index of the existing row-major grid. -/
theorem rectangularRowLabels_injective (R S : Nat) :
    Function.Injective (fun i : Fin (R*S) => (i.val / S, i.val % S)) := by
  intro i j h
  apply Fin.ext
  have hq : i.val / S = j.val / S := congrArg Prod.fst h
  have hr : i.val % S = j.val % S := congrArg Prod.snd h
  calc
    i.val = i.val % S + S * (i.val / S) := (Nat.mod_add_div i.val S).symm
    _ = j.val % S + S * (j.val / S) := by rw [hq, hr]
    _ = j.val := Nat.mod_add_div j.val S

/-- A finite point-count condition makes the actual rectangular trace Gram PD. -/
theorem rectangularTraceGram_posDef_of_point_count
    (P : Finset Complex) (J R S : Nat) (hR : 1 <= R) (hS : 1 <= S)
    (hJ : S <= J) (hcard : 2*(R-1)+(S-1) < P.card) :
    (rectangularTraceGram P J R S).PosDef := by
  apply JetAssembly.traceGramMatrix_posDef_of_point_count P J R S hR hS
    (fun i : Fin (R*S) => (i.val / S, i.val % S))
    (rectangularRowLabels_injective R S)
  · intro i
    exact (Nat.div_lt_iff_lt_mul (by omega)).mpr i.isLt
  · intro i
    exact Nat.mod_lt _ (by omega)
  · exact hJ
  · exact hcard

/-- Positivity and Hadamard concern one unchanged matrix. No PD premise is assumed. -/
theorem rectangularTraceGram_det_bounds
    (P : Finset Complex) (J R S : Nat) (hR : 1 <= R) (hS : 1 <= S)
    (hJ : S <= J) (hcard : 2*(R-1)+(S-1) < P.card) :
    0 < (rectangularTraceGram P J R S).det /\
      (rectangularTraceGram P J R S).det <=
        Finset.univ.prod (fun i => rectangularTraceGram P J R S i i) := by
  constructor
  · exact (rectangularTraceGram_posDef_of_point_count P J R S hR hS hJ hcard).det_pos
  · exact traceGramMatrix_det_le_diag P J _

end
end TenthDiscriminant
