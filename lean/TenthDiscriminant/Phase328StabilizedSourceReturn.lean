import TenthDiscriminant.IntegerTraceGram

/-!
# Phase328 — stabilized source entry and exact return to original Gram

This module formalizes the entrywise integral source/auxiliary split,
without replacing the original ordinary-Z derivative convention. It
does NOT yet formalize the full Q8 moving-frame determinant covariance;
the explicit finite matrix harness is in research/phase328/.

For any integer matrix B, we place B in the scalar block and use
the identity matrix on each of three auxiliary quaternionic blocks.
The original block is recovered exactly, with no scalar or norm-shift.
This is a source-preservation theorem only, NOT a new determinant
divisor or a class-number-one field bound.
-/
namespace TenthDiscriminant.Phase328
set_option autoImplicit false

/-- Scalar block B together with three auxiliary identity blocks,
on the same original row-label type Fin n. -/
def stabilizedEntry {n : Nat}
    (B : Matrix (Fin n) (Fin n) Int) :
    Matrix (Fin 4 × Fin n) (Fin 4 × Fin n) Int :=
  fun a b =>
    if a.1 = b.1 then
      if a.1 = 0 then B a.2 b.2
      else if a.2 = b.2 then 1 else 0
    else 0

/-- The old integral Gram is the exact scalar-block restriction. -/
theorem stabilized_source_return {n : Nat}
    (B : Matrix (Fin n) (Fin n) Int) (i j : Fin n) :
    stabilizedEntry B ((0 : Fin 4), i) ((0 : Fin 4), j) = B i j := by
  simp [stabilizedEntry]

/-- Every non-scalar diagonal block is the identity. -/
theorem stabilized_aux_identity {n : Nat}
    (B : Matrix (Fin n) (Fin n) Int)
    (k : Fin 4) (hk : k ≠ 0) (i j : Fin n) :
    stabilizedEntry B (k, i) (k, j) =
      if i = j then 1 else 0 := by
  simp [stabilizedEntry, hk]

/-- The four blocks are orthogonal at the entrywise integral level. -/
theorem stabilized_cross_zero {n : Nat}
    (B : Matrix (Fin n) (Fin n) Int)
    (k l : Fin 4) (hkl : k ≠ l)
    (i j : Fin n) :
    stabilizedEntry B (k, i) (l, j) = 0 := by
  simp [stabilizedEntry, hkl]

/-- Matrix-valued return, not just a scalar pilot row. -/
theorem stabilized_source_matrix {n : Nat}
    (B : Matrix (Fin n) (Fin n) Int) :
    (fun i j : Fin n =>
       stabilizedEntry B ((0 : Fin 4), i) ((0 : Fin 4), j)) = B := by
  ext i j
  exact stabilized_source_return B i j

/-- Apply the generic source-return identity to the exact original
integer rectangular trace Gram with its unchanged ordinary-Z jets. -/
theorem stabilized_original_integer_traceGram_return
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (i j : Fin (R*S)) :
    stabilizedEntry (TenthDiscriminant.integerRectangularTraceGram Q D J R S)
      ((0 : Fin 4), i) ((0 : Fin 4), j) =
      TenthDiscriminant.integerRectangularTraceGram Q D J R S i j := by
  exact stabilized_source_return _ i j

/-- The exact original rectangular source Gram is recovered as
a full matrix from its scalar block, with all source rows preserved. -/
theorem stabilized_original_integer_traceGram_matrix
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    (fun i j : Fin (R*S) =>
      stabilizedEntry (TenthDiscriminant.integerRectangularTraceGram Q D J R S)
        ((0 : Fin 4), i) ((0 : Fin 4), j)) =
      TenthDiscriminant.integerRectangularTraceGram Q D J R S := by
  exact stabilized_source_matrix _

end TenthDiscriminant.Phase328

#print axioms TenthDiscriminant.Phase328.stabilized_source_matrix
#print axioms TenthDiscriminant.Phase328.stabilized_original_integer_traceGram_return

#print axioms TenthDiscriminant.Phase328.stabilized_original_integer_traceGram_matrix
