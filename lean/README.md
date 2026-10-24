# Lean: the proof you can inspect

Phase 31 proves the necessary nine-element list for actual class number one
below one million. The wheel's no-loss invariant and complete interval
enumeration are proved, and the finite survivor identity is kernel checked.
The range from one million to the effective cutoff remains open, as do the
nine positive class-number equalities.
[Read the wheel proof](../research/ender_radius_bridge/WHEEL_COVERAGE_GUIDE.md).

Phase 30 now derives the finite sieve's modulo-eight prefilter from actual
class number one, proves guarded prime tests necessary, and checks the
small candidate list below 92. The middle-range certificate and positive
class-number proofs remain open. Start with the
[finite-sieve guide](../research/ender_radius_bridge/FINITE_SIEVE_GUIDE.md).

**A checked interpolation and determinant apparatus, not yet a formalized
class-number-one classification.**

**Current frontier (Phase 29):** for every positive squarefree radicand d,
actual class number one of `Q(sqrt(-d))` implies d<700000000000. The even
maximal order, prime-two obstruction and explicit odd-chart field equivalence
are supplied. This is an effective bound, not the finite classification.
[Read the short proof](../research/ender_radius_bridge/FULL_CUTOFF_GUIDE.md).
Earlier bounded-interval/arithmetic descriptions below are historical checkpoints.

The first saved interval is now closed: for squarefree `D≡3 (mod 4)` in
`[700000000000,875000000000]`, the constructed quadratic field has class
number not one. Coverage, both total budgets and exact guards are proved;
`FirstIntervalChecked.lean` has no remaining numerical hypothesis. See the
[numerical bridge guide](../research/ender_radius_bridge/NUMERICAL_BRIDGE_GUIDE.md).

[The uniform arithmetic guide](../research/ender_radius_bridge/UNIFORM_PRIME_MASS_GUIDE.md)
explains Phase 27: four certified prime-log constants now give bounds for
arbitrary admissible R,S. The first interval is recovered without new per-R
prime-power certificates. Other interval comparisons and the global cutoff
are still open.

Start with the short [mathematical spine](MATHEMATICAL_SPINE.md): one
integer determinant, its real positivity, and its fixed modular relation.
Then read the [detailed human proof guide](HUMAN_GUIDE.md). Use the
[current claim map](FORMALIZATION.md) to distinguish proved components,
conditional helpers, finite calculations and open links.

The arithmetic foundation includes the
[maximal-order equivalence](TenthDiscriminant/QuadraticFieldChart.lean):
Phase 14's rational trace/norm criterion identifies every algebraic
integer in the constructed quadratic field with the explicit
half-integral order. The [class-number bridge](TenthDiscriminant/ClassNumberInertBridge.lean)
now turns this into the strict-small-prime local valuation for the
actual integer Gram; see [§21 of the guide](HUMAN_GUIDE.md#21-the-global-hypothesis-reaches-the-local-determinant).

The current bridge reaches the finite prime mass and production `upper_B`
on that same chosen-radius matrix. [EnderUpperB.lean](TenthDiscriminant/EnderUpperB.lean)
checks the full upper expression for the campaign's integer radii.
[EllipseUpperCount.lean](TenthDiscriminant/EllipseUpperCount.lean) now supplies
its upper sample count and interval transfer, with safe floor padding explicit.
The [short upper-bound proof](../research/ender_radius_bridge/UPPER_BOUND_GUIDE.md)
explains the row estimate, integral and inward-cell count. The
[factorial proof](../research/ender_radius_bridge/FACTORIAL_LOWER_GUIDE.md)
now checks the finite Legendre identity and scalar `factorial_lower`.
The [staircase proof](../research/ender_radius_bridge/PRIME_MASS_LOWER_GUIDE.md)
now converts to the determinant's odd-prime weights, bounds both finite
losses and justifies clipping. [PrimeTail.lean](TenthDiscriminant/PrimeTail.lean)
now proves the reciprocal-prime bound by finite potential drops and
connects the unchanged lower/upper expressions under the documented guards.
Numerical enclosure/guard interpretation for the remaining intervals, universal closure and
classification remain open.

## The result to start with

For a finite set P of distinct complex points and the original R-by-S monomial
row grid, positive R,S and

$$
J\ge S,\qquad |P|>2(R-1)+(S-1)
$$

imply positive definiteness of the actual real derivative trace-Gram matrix G,
and

$$
0<\det G\le\prod_iG_{ii}.
$$

No independence, irreducibility, nonzero resultant or positive determinant is
assumed in this public criterion. The derivatives are ordinary Z-derivatives
with W held fixed; the trace normalization is unchanged. The criterion is
sufficient, not claimed necessary or sharp.

The direct API is in [`Interpolation.lean`](TenthDiscriminant/Interpolation.lean):

```lean
open TenthDiscriminant

example (P : Finset Complex) (J R S : Nat)
    (hR : 1 <= R) (hS : 1 <= S) (hJ : S <= J)
    (hc : 2*(R-1)+(S-1) < P.card) :
    (rectangularTraceGram P J R S).PosDef :=
  rectangularTraceGram_posDef_of_point_count P J R S hR hS hJ hc
```

`rectangularTraceGram_det_bounds` supplies positivity and the diagonal-product
upper bound together. It proves the row-major index bookkeeping internally;
callers need not supply injectivity of the canonical labels. The more general
arbitrary-label theorem remains in
[`JetCountGram.lean`](TenthDiscriminant/JetCountGram.lean).

For a concrete positive-D integer-radius ellipse, see
[`LatticeEllipse.lean`](TenthDiscriminant/LatticeEllipse.lean). Its theorem
`ellipseTraceGram_det_bounds` requires the actual integer-pair count; it does
not prove Ender's analytic estimate for the chosen radius. The explanation is
in [guide §9](HUMAN_GUIDE.md#9-the-concrete-ellipse-bridge).
The [separate cell-covering proof](../research/ender_radius_bridge/PROOF.md)
explains the count in ordinary mathematics.
[`EllipseCellArea.lean`](TenthDiscriminant/EllipseCellArea.lean) now checks the
disk-covering inequality, exact chosen-radius count, interval transfer and
actual-Gram positivity without a point-count or area premise.

[`IntegerTraceGram.lean`](TenthDiscriminant/IntegerTraceGram.lean) gives the
next bridge: for a supplied finite set of distinct integer pairs and positive
D, its exact integer derivative trace-Gram matrix casts entrywise to this
same real matrix. The integer-radius ellipse is a specialization. The
determinant casts accordingly. The later rectangular valuation theorem
proves the exact determinant power under an explicit universal Frobenius
congruence. [InertFrobenius.lean](TenthDiscriminant/InertFrobenius.lean)
derives that congruence from odd-prime nonsquareness of `-D : ZMod p`.
For squarefree `D≡3 (mod 4)`, the
[class-number bridge](TenthDiscriminant/ClassNumberInertBridge.lean)
now supplies that local guard at strict small odd primes.
The [guide's coordinate explanation](HUMAN_GUIDE.md#10-the-same-gram-matrix-in-integer-and-complex-coordinates)
includes an asymmetric control that a determinant-only comparison misses.

[`QuadraticCoordinates.lean`](TenthDiscriminant/QuadraticCoordinates.lean)
identifies those pairs for `D>0` with the selected order `ℤ[√(-D)]`, not
necessarily the full ring of integers.
[`ResidueTraceGram.lean`](TenthDiscriminant/ResidueTraceGram.lean)
then defines the corresponding local matrix over `ZMod m` and proves that its
determinant vanishes exactly when `m>0` divides the integer determinant.
Distinct global points can share a residue; the original sample indexing is
kept. See [guide §11](HUMAN_GUIDE.md#11-local-and-global-arithmetic-views-of-one-gram-matrix).
This detects divisibility but supplies no general inert-prime exponent.
The [row-action](TenthDiscriminant/RectangularRowAction.lean) and
[Gram-factor](TenthDiscriminant/RectangularGramFactor.lean) theorems now
construct that exponent for the original integer matrix **under the
universal coordinatewise Frobenius premise**, discharged under the precise
local nonsquare guard in [guide §14](HUMAN_GUIDE.md#14-one-local-generator-controls-every-lattice-point).
[`InertPilot.lean`](TenthDiscriminant/InertPilot.lean) uses a matching
row/column shear and the integral two-sided factor lemma in
[`GramDivisibility.lean`](TenthDiscriminant/GramDivisibility.lean) to prove
`9 | det G` for the canonical `D=19`, `R=4`, `S=2` grid and arbitrary finite
samples and derivative depth. The positive `ellipsePairs 19 5` control makes
this nonvacuous. It is a fixed pilot, not Ender's general valuation theorem.

## Read in mathematical order

1. [Human guide](HUMAN_GUIDE.md): statement, definitions, proof and examples.
2. [JetCountGram](TenthDiscriminant/JetCountGram.lean): the actual observations and matrix.
3. [FactorJetBudget](TenthDiscriminant/FactorJetBudget.lean): the short exceptional-set product rule.
4. [IrreducibleContact](TenthDiscriminant/IrreducibleContact.lean): the algebraic contact bound it uses.

Lower-level files implement the fixed coefficient matrix, local multiplicity,
field-level nonvanishing and degree accounting. The
[claim map](FORMALIZATION.md) also covers the arithmetic, moment, interval,
envelope, transport and experimental modules. Optional research contracts are
not extra premises of the interpolation theorem.

## Reproduce the checks

Pinned environment: **Lean 4.19.0**, **Mathlib
c44e0c8ee63ca166450922a373c7409c5d26b00b**. From the repository root:

```sh
cd lean
lake update
lake exe cache get
python3 verify_sources.py
lake build
python3 audit.py
python3 negative_controls.py
```

`verify_sources.py` matches the saved interval endpoints; it does not certify
Arb inequalities. `lake build` checks the imported formal statements.
`audit.py` checks that all project modules are imported, audits transitive
axiom dependencies of every logical constant in the project namespace, and runs matched tests
of that audit and the public API. `negative_controls.py` retains the inherited
mathematical controls. Invalid probes are generated in temporary files, not
imported into the proof library.

Only `propext`, `Classical.choice` and `Quot.sound` are allowed by the dependency
gate. An unreferenced safe definition or opaque declaration is checked too.
Unsafe compiler-generated runtime auxiliaries are reported separately using
Lean safety metadata, not trusted as proof objects. Source-level unsafe
declarations remain forbidden.
Import coverage and source scanning are structural safeguards, not substitutes
for the compiled audit or a semantic review.

## Revision and evidence discipline

PRs #15 and #16 are merged into `main`; the interpolation source head
`d6c4876a316814aa0ac4ef1a719a13ea2822e620` was checked by workflow
`39863039414`. The later apparatus review was checked at its own source head.
Those runs do not certify this ellipse bridge or the end-to-end classification;
verification must be reported against the bridge's exact commit.

Earlier stage notes preserve their local derivations and dated evidence:
[JET_NONVANISHING](JET_NONVANISHING.md),
[SYLVESTER_MULTIPLICITY](SYLVESTER_MULTIPLICITY.md),
[SYLVESTER_NONZERO](SYLVESTER_NONZERO.md),
[DEGREE_CONTACT_BUDGET](DEGREE_CONTACT_BUDGET.md), and
[JET_FACTOR_ASSEMBLY](JET_FACTOR_ASSEMBLY.md).
Their old descriptions of what was still open are historical, not the current
status. The current status is [FORMALIZATION.md](FORMALIZATION.md).

## The remaining boundary

The chosen-radius cell-area count is Lean-checked. Determinant divisibility
is checked under an odd-prime nonsquare condition, which Phase 16 derives
from class number one in the squarefree `D≡3 (mod 4)` strict small-prime
range. The abstract class-number-one quotient-to-principal-norm step is checked;
the explicit order is now identified with the maximal integer ring,
including its principal norm coordinates, and the class-number-one
ideal step is composed with the strict local valuation. The finite
mathematical lower/upper comparison is now connected, including the tail.
Phase 26 closes the first bounded numerical exclusion with all guards.
The other 249 intervals, universal closure, even cases and finite
classification remain open. The candidate cutoff and saved numerical evidence are
unchanged. No human or blind independent semantic review is claimed.
