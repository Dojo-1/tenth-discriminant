import TenthDiscriminant.Coverage

/-!
# Exact coverage of the recorded Ender endpoint chain
The 250 pairs in ledger/coverage_ender.txt are exactly this recurrence,
checked against the source bytes by verify_sources.py. No decimal margin
is turned into an axiom or interpreted as a Lean certificate.
-/
namespace TenthDiscriminant

def makeIntervals : ℕ → ℕ → ℕ → List (ℕ × ℕ)
  | 0, _, _ => []
  | n+1, lo, hi =>
      let next := min hi (5*lo/4)
      (lo,next) :: makeIntervals n next hi

def enderIntervals : List (ℕ × ℕ) := makeIntervals 250 700000000000 (10^36)

set_option maxRecDepth 20000 in
set_option maxHeartbeats 2000000 in
theorem ender_chain_checked : checkChain 700000000000 (10^36) enderIntervals = true := by decide

set_option maxRecDepth 20000 in
theorem ender_interval_count : enderIntervals.length = 250 := by decide

/-- Coverage only: no positivity or class-number conclusion is assumed or derived. -/
theorem ender_integer_coverage (D : ℕ) (hlo : 700000000000 ≤ D) (hhi : D < 10^36) :
    ∃ a b, (a,b) ∈ enderIntervals ∧ a ≤ D ∧ D ≤ b :=
  checkChain_sound enderIntervals 700000000000 (10^36) D ender_chain_checked hlo hhi

end TenthDiscriminant
