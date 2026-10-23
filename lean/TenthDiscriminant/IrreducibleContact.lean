import TenthDiscriminant.SylvesterIrreducible
import TenthDiscriminant.ContactBudget

/-! The actual nonzero and nonzero-fiber obligations are now discharged. -/
namespace TenthDiscriminant
open Polynomial Matrix
noncomputable section
variable {K : Type*} [Field K] [CharZero K]

/-- Irreducibility supplies both nonzero premises of the contact budget. -/
theorem irreducible_fixedDerivativeSylvester_contact_sum
    (F : Polynomial (Polynomial K)) (a b : Nat) (ha : 1 <= a)
    (hZ : F.natDegree = a) (hi : Irreducible F)
    (hW : forall i, (F.coeff i).natDegree <= b)
    (s : Finset K) (z : K -> K) (m : K -> Nat)
    (hroot : forall w, w ∈ s ->
      (Polynomial.X - Polynomial.C (z w))^(m w) ∣ F.map (Polynomial.evalRingHom w)) :
    s.sum (fun w => m w - 1) <= (2*a-1)*b := by
  have he : a+(a-1) = 2*a-1 := by omega
  have hh := fixedDerivativeSylvester_contact_sum F a b hZ.le hW
    (fixedDerivativeSylvester_ne_zero_of_irreducible F a ha hZ hi) s z m
    (fun w hw => irreducible_positive_specialization_ne_zero F a ha hZ hi w) hroot
  simpa only [he] using hh

/-- An irreducible positive-Z-degree factor has at most 2a-1 excessive contacts. -/
theorem irreducible_fixedDerivativeSylvester_excessive_contact_card
    (F : Polynomial (Polynomial K)) (a b : Nat) (ha : 1 <= a) (hb : 0 < b)
    (hZ : F.natDegree = a) (hi : Irreducible F)
    (hW : forall i, (F.coeff i).natDegree <= b)
    (s : Finset K) (z : K -> K) (m : K -> Nat)
    (hroot : forall w, w ∈ s ->
      (Polynomial.X - Polynomial.C (z w))^(m w) ∣ F.map (Polynomial.evalRingHom w))
    (hcontact : forall w, w ∈ s -> b < m w) :
    s.card <= 2*a-1 := by
  exact fixedDerivativeSylvester_excessive_contact_card F a b ha hb hZ.le hW
    (fixedDerivativeSylvester_ne_zero_of_irreducible F a ha hZ hi) s z m
    (fun w hw => irreducible_positive_specialization_ne_zero F a ha hZ hi w)
    hroot hcontact

end
end TenthDiscriminant
