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
