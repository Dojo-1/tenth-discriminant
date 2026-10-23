# Registered attempt — global Gram data and residue coordinates

Registered on 23 October 2026 before any new Lean proof edit or control run.
Base: draft PR #20 at `f12085372078a7958f4a1fc7995853fed49efb00`;
merged `main` remains `c77049288e0eac33f72739b255d8254ff3e6aca1`.
This extends the integer-coordinate bridge, not `flow/PREREG_ENDER.txt`,
the recorded certificates, the cutoff, or the class-number claim.

## Exact two-way target

**Global coordinates.** Compare the current pair `(a,b) : Int × Int` with
`Zsqrtd (-(D : Int))`, the selected order `Z[sqrt(-D)]`. Prove that the
coordinate map is bijective and transports multiplication, conjugation and
norm/trace pairing. Do not assert that this order is the full quadratic
integer ring. Preserve the already-checked map to complex numbers and the
existing derivative trace-Gram matrix; do not replace it with a new Gram.

**Global to residue.** For a modulus `m > 0`, reduce both coordinates to
`ZMod m`. Define the corresponding pair multiplication, conjugation,
ordinary derivative row, factor-of-two trace pairing and Gram matrix there.
Prove that reducing the *existing integer matrix* entrywise equals that
residue matrix with the same derivative cutoff and row-major labels.
The residue sum remains indexed by the original finite set `Q` of integer
pairs: reduction need not be injective, so `Q.image` as a set would lose
sample multiplicity.

**Residue to global.** Use determinant naturality to prove that the reduced
determinant is the image of the integer determinant. Aim to prove, for
`m > 0`, that the residue determinant is zero if and only if `m` divides
the integer determinant. A conditional `m = p^k` reformulation may be
included. This criterion alone is not a valuation lower bound.

**Nontrivial inert-prime pilot.** For `D=19`, `p=3`, `R=4`, `S=2`, isolate the
row `Z^3-W` as the difference of two canonical monomial rows. Prove that
its evaluated ordinary `Z`-derivatives are multiples of `3` in both
integer coordinates for every pair and every derivative order. If the
pinned matrix library permits a small proof, transport this through the
unitriangular row change and prove a two-sided Gram factorization with
one `3` on each side, hence `9 ∣ det G` for the full canonical `8 × 8`
integer Gram matrix for arbitrary finite `Q` and `J`. Mere row-and-column
divisibility is not enough without the `9`-divisible diagonal. This is
the `F(3)=1` toy case only, not Ender's universal inert-prime bound.

This is a commuting calculation in two directions, not a local-to-global
principle for arbitrary fields or a Cayley–Dickson tower beyond the first
quadratic doubling. No inert-prime or class-number hypothesis is imported.

## Controls, falsifiers and stop rule

Use exact controls. For `D=3`, `Q={(0,1)}`, `J=2`, rows `1, ZW`, the global
matrix is already checked as `[[2,6],[6,24]]` with determinant `12`.
Its determinant must reduce to zero modulo `3` and to `2` modulo `5`;
these are arithmetic controls, **not** inert-prime evidence.

Test the tempting but false set-image rule: with `m=3`,
`Q={(0,0),(3,0)}`, `J=1` and the constant row, the global entry is `4`
and reduces to `1`, while summing once over the reduced image set gives
`2`. Record the mismatch even if an attempted Lean encoding is difficult.
For the inert pilot, `Q=ellipsePairs 19 5`, `J=2` has 21 distinct points
and the existing strict count criterion makes its determinant positive;
this rules out explaining the claimed `9` divisibility by a zero determinant.
As a falsifier, `D=2`, `p=3`, `z=sqrt(-2)` gives `z^3-conj(z)=-z`, not
`3`-divisible; no inertness-free Frobenius claim is allowed. Singular
reduction modulo `p` alone also does not imply `p^2` divisibility.
Also retain zero high derivatives, conjugate `W`, factor two, origin,
negative coordinates and arbitrary finite `Q` in the universal theorem.

Use pinned Lean 4.19.0 and Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`. Run a targeted Lean
check, full build, source-correspondence check, compiled dependency audit
and inherited negative controls; report any local timeout as a failure of
that run, not a pass. Seek pinned CI for the final exact commit. If the
bidirectional determinant criterion, Zsqrtd transport, or inert pilot
cannot be proved within this bounded slice, keep the strongest checked
lemma and report the unsolved obligation; do not weaken the theorem
silently or widen the task to a class-number classification. Keep the
diff small and the explanation readable by a mathematician not following
every Lean declaration.

## Result ledger (appended after registration)

The preregistration was committed alone at `e8bb4d389c95bc24624d7b94174245314594dfba`;
its pinned Linux workflow `39944972558` passed. The following proof edits
were made only afterward.

- `QuadraticCoordinates.lean` proves a coordinate bijection with
  `Zsqrtd (-(D : Int))` and compatibility with multiplication, conjugation,
  powers, norm and the existing trace pairing. It is not a packaged ring
  equivalence or an assertion that this order is the full ring of integers.
- `ResidueTraceGram.lean` builds the local operations independently, retains
  original `Q` indexing, proves the integer-matrix reduction and determinant
  naturality, and proves `det G_m = 0 ↔ m | det G_Z` for `m>0`.
- Both preregistered arithmetic controls are Lean-checked: determinant `12`
  maps to `0` modulo `3` and `2` modulo `5`; the two colliding global
  samples give `4 ≡ 1` modulo `3`, while incorrect image-set deduplication
  gives `2`.
- `InertPilot.lean` proves every ordinary derivative of `Z³-W` at `D=19`
  has both integer coordinates divisible by `3`, for every point and every
  derivative order. Its actual canonical eight-row Gram is related to an
  integral normalized Gram by a determinant-preserving matching shear and a
  two-sided diagonal factor. Hence Lean proves `9 | det G` for every finite
  `Q` and every `J`; this is the registered `F(3)=1` pilot, not an all-prime
  theorem. The `ellipsePairs 19 5`, `J=2` determinant is strictly positive,
  using the existing 21-point control. The `D=2,p=3,z=(0,1)` noninert
  falsifier is also Lean-checked.
- The feared shortcut remains false: a divisible row and column alone do not
  supply a square factor, as `[3]` shows. The proof instead exhibits an
  *integer* middle matrix. Neither the general inert-prime filtration, the
  cell-area count in Lean, Ender's global valuation bound, nor the
  class-number classification is established by this pilot.

Verification on this proof head, before its final commit:

- `python verify_sources.py`: exit 0; saved source digest and all 250
  interval endpoints match the Lean recurrence. This does not certify Arb
  inequalities.
- `lake env lean TenthDiscriminant/InertPilot.lean`: exit 0, including the
  fixed-grid theorem and controls. `lake build`: exit 0, all 6690 build steps;
  existing linter warnings in older modules and one tactic suggestion in the
  pilot do not affect proof checking.
- `python audit.py`: exit 1 locally on Windows. Before its 240-second
  `apparatus_controls.py` subprocess timeout, it reported all 36 project
  modules reachable, `AUDIT_OK` for 526 logical declarations (435 theorems;
  only the three permitted axioms), and several matched apparatus controls.
  This partial output is **not** a full audit pass.
- `python negative_controls.py`: exit 1 after this local run was intentionally
  stopped following four passing matched controls to avoid a prolonged
  Windows replay; its full suite was **not** completed locally. The exact
  stopped run is not presented as a pass.

The pinned Linux workflow on the final proof commit is the required complete
check. Proof-head commit `d5945cf7fc5b891b54ef85986c40a55bec35843c`
passed workflow `39954106722` (job `120415525126`): source correspondence,
full Lean build, compiled dependency audit and inherited negative controls.
The preregistration's earlier green run did not certify those proof edits;
nor does this result certify any later documentation-only follow-up until its
own exact-head workflow passes.
