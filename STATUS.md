# Status — 2026-10-25

## Phase 33: all nine positive fields, bounded iff below one million

Actual class number one is now proved for all nine radicands
1,2,3,7,11,19,43,67,163. `classNumber_one_iff_below_million` proves both
directions for positive squarefree d<1000000, using the previously checked
complete finite interval for necessity and the new positive proofs for sufficiency.

An ideal of prime norm gives a residue map. Finite polynomial root absence
rules out norm two for 11,19, and norms 2,3,5,7 for 43,67,163. Minkowski's
representatives have norm below three or nine respectively. In the latter
tier the only nonunit small ideal is the legitimate principal ideal (2),
of norm four. Unique factorization used is of ideals, not an assumed PID
property of the integer ring. No class-number-one hypothesis is used in
the positive bridge. Controls retain (2), the root at d=11 modulo three,
and the actual d=23 counterexample to omitting local hypotheses.

The entire interval [1000000,700000000000), full classification and other
challenge shortfalls remain open. No cutoff/pin/gate/campaign changes.
[Human proof](research/ender_radius_bridge/NINE_POSITIVE_GUIDE.md) ·
[Protocol](research/ender_radius_bridge/PHASE33_PROTOCOL.md) ·
[Verification checkpoint](research/ender_radius_bridge/PHASE33_RESULTS.json).
Local root build/audit/signatures passed; full exact-head CI must accompany publication.
Older positive-case gap descriptions below are historical.

## Phase 32: actual discriminant and four positive class-number equalities

`imaginaryQuadratic_discr` proves the signed actual field discriminant is
-d in the odd chart and -4*d otherwise, for positive squarefree d. The
absolute value equals `absoluteDiscriminantParameter d`, not merely by
definition. The existing cutoff therefore gives an actual Mathlib field-
discriminant bound below 700000000000 under class number one.

The two-dimensional trace-pairing lemma uses maximal integral bases.
Its control distinguishes the order discriminant -12 from the actual field
discriminant -3 at d=3. The pinned small-discriminant Minkowski criterion
then proves actual class number one for d=1,2,3,7. At d=11 it no longer
applies; no negative class-number conclusion is drawn.

Still open: positive proofs for 11,19,43,67,163; the complete interval
[1000000,700000000000); full classification and other challenge shortfalls.
The cutoff, production campaign, pins and gates are unchanged.
[Human proof](research/ender_radius_bridge/DISCRIMINANT_POSITIVE_GUIDE.md) ·
[Protocol](research/ender_radius_bridge/PHASE32_PROTOCOL.md) ·
[Verification checkpoint](research/ender_radius_bridge/PHASE32_RESULTS.json).
Exact published-head CI must accompany the local build/audit checkpoint.
Older phase descriptions below are historical where these gaps are now closed.

## Phase 31: necessary nine-candidate list below one million

`classNumber_one_middle_below_million` compiles: for positive squarefree d
with actual class number one and 92<=d<1000000, d=163.
`classNumber_one_candidates_below_million` joins the small end to give the
necessary nine-element list below one million. Universal wheel-lift and
quotient/remainder interval coverage are proved, not inferred from output.
The fixed 9240 wheel has 30 residues and 3245 interval candidates; exact
kernel evaluation leaves [163]. Extra primes and strict guards are checked.
The independent exact control agrees but is not used as a proof input.

The remaining interval is [1000000,700000000000), not silently discarded.
The positive class-number equalities, full classification and other open
challenge objectives remain open. No cutoff or production-campaign change.
[Human guide](research/ender_radius_bridge/WHEEL_COVERAGE_GUIDE.md) ·
[Protocol](research/ender_radius_bridge/PHASE31_PROTOCOL.md) ·
[Verification checkpoint](research/ender_radius_bridge/PHASE31_RESULTS.json).
Whole-library and exact-head CI terminal status must accompany publication.

## Phase 30: checked finite-sieve preconditions, not classification

`imaginaryQuadratic_classNumber_one_mod_eight` proves d=3 mod 8 for
positive squarefree d>7 with actual class number one. The F2 quotient is
constructed without dividing by two. Norm-two at 7 and exclusion of the
actual field at 23 are checked controls. Guarded odd-prime tests are proved
necessary; their primality/oddness checks and strict endpoint are explicit.
Kernel evaluation on [0,92) gives the necessary list 1,2,3,7,11,19,43,67.
The conditional nine-candidate theorem still requires a complete survivor
certificate on [92,700000000000). No positive class-number classification,
new numerical run, changed threshold or optimization is claimed.
[Human guide](research/ender_radius_bridge/FINITE_SIEVE_GUIDE.md) ·
[Protocol](research/ender_radius_bridge/PHASE30_PROTOCOL.md) ·
[Verification checkpoint](research/ender_radius_bridge/PHASE30_RESULTS.json).
Exact published-head CI must accompany this checkpoint.

## Phase 29: effective radicand bound, with both parity cases supplied

`imaginaryQuadratic_classNumber_one_radicand_bound` compiles for every
positive squarefree d: actual-field class number one implies d<700000000000.
`ImaginaryQuadraticField d` is the actual quotient `Q[X]/(X^2+d)`, not a
piecewise proxy. The even maximal-order theorem and prime-two obstruction
force d=1 or 2 when d=1,2 mod 4. An explicit theta=2*omega-1 field equivalence
and integer-ring/PID transport connect the d=3 mod 4 branch to Phase28.
The new public cutoff has no mod-4, numerical, maximal-order or equivalence
premise. It assumes only positivity, squarefreeness and actual class number one.

The supplementary conventional absolute-discriminant parameter is also
bounded; its equality with Mathlib's NumberField.discr is not asserted.
The finite odd classification, independent human semantic review,
optimization, systematic writeup comparison and submission remain open.
All exact controls and development failures are retained. Full root
build/audit and exact-head CI status must accompany publication.
[Human proof](research/ender_radius_bridge/FULL_CUTOFF_GUIDE.md)
· [Preregistration](research/ender_radius_bridge/PHASE29_PROTOCOL.md).

The Phase28 and earlier frontier descriptions below are historical.

## Phase 28: universal odd-discriminant cutoff, not full classification

`FirstCertificate.odd_large_classNumber_ne_one` compiles for every squarefree
`D≡3 (mod 4)` with `D≥700000000000`. There is no numerical premise.
The new fixed auxiliary radius family, all floor/ceiling/inertness/count
guards, the exact normalized production formula, and both affine envelopes
are proved. The same actual Gram connects both sides. The envelopes separate
by at least `0.013919` after division by positive `R^2*S`.

This bypasses the remaining interval comparisons and unbounded envelope for
the **odd** statement; it does not validate those frozen records or cover
even fundamental discriminants. The finite sieve/classification, independent
human review, optimization and upstream review remain open. The one fixed
256-bit Arb pilot passed separately; it is not the universal proof.
Development failures and proof-search limits are retained. Full pinned
root build/audit/controls and exact-tree CI must accompany publication.
[Human proof](research/ender_radius_bridge/ODD_CUTOFF_GUIDE.md)
· [Preregistration](research/ender_radius_bridge/PHASE28_PROTOCOL.md).

Earlier phase sections below are historical checkpoints, not the current frontier.

## Phase 27: arithmetic now separates dimensions from fixed primes

`UniformPrimeMass` proves floor, factorial/geometric and retained-weight
estimates for arbitrary admissible R,S,Q,P, including the floor error,
quadratic loss and clipping. `PrimeLogConstants` certifies four fixed bounds
for P=10000/Q=7 using exact paired row checks and chunk totals.
`UniformPrimeMassCertified` turns these into bounds valid for every R>=2,
S>=1, composed with the original actual-Gram comparison and its explicit
range/radius/class-number guards. The fixed tail budget is reused with a
proved monotonicity direction.

The unchanged first-interval pilot meets the old budgets, now proved in Lean.
No new interval or global cutoff is claimed. The gain is a reusable arithmetic
engine instead of duplicated prime-power tables. Four omission controls,
missing-row and wrong-rounding controls compile. Development failures and
the single exact-rational observational pilot are preserved separately.
Full root audit and exact-head CI status must accompany publication.
[Human explanation](research/ender_radius_bridge/UNIFORM_PRIME_MASS_GUIDE.md)
· [Preregistration](research/ender_radius_bridge/PHASE27_PROTOCOL.md).

## Phase 26: first bounded class-number exclusion closes end to end

`FirstCertificate.first_interval_classNumber_ne_one` compiles with no
numerical premise. For squarefree `D≡3 (mod 4)` and
`700000000000≤D≤875000000000`, the actual constructed quadratic field's
class number is not one. Exact log enclosures, all 1,229 row checks,
complete prime coverage, both aggregate budgets and radius/padding guards
are supplied. The conservative contradiction is `581×10^31>572×10^31`.

Coverage is proved on integer windows of at most 16, then joined by exact
range identities. Both totals are proved on the existing 32-row chunks,
then joined symbolically. No production tool, parameter, saved certificate
or dependency pin changed. Failed pilots and prior resource limits remain
preserved. Local bounded-module build passes; full audit/CI status belongs
to the exact published head, not to a proof-attempt label.

This excludes one bounded interval in the stated arithmetic class, not the
global cutoff. The remaining 249 intervals, unbounded range, even cases and
finite classification are still open. No novelty, optimization or human
peer-review claim. [Human proof](research/ender_radius_bridge/NUMERICAL_BRIDGE_GUIDE.md)
· [Theorem](lean/TenthDiscriminant/FirstIntervalChecked.lean)
· [Preregistration](research/ender_radius_bridge/PHASE26_PROTOCOL.md).

## Historical Phase 25 checkpoint: sound bridge, table verification then pending

The fixed first interval is `[700000000000,875000000000]`, for squarefree
`D≡3 (mod 4)`. Local pinned builds accept the eight-term log enclosure and
integer checker, exact radius/padding guards, globally valid staircase lower
bound, quotient-witness soundness, scalar budget reductions and conditional
class-number conclusion. `FirstIntervalRows` additionally checks all 1,229
individual rows. The unchanged Arb replay and exact rational
candidate have a positive gap, but neither proves the missing completeness
and total-budget obligations in Lean.
Full-table attempts encountered stack/memory failures; all records are
preserved in `research/ender_radius_bridge/PHASE25_PROOF_FAILURES.json`.
No concrete interval exclusion, new cutoff or classification is claimed.
[Human explanation](research/ender_radius_bridge/NUMERICAL_BRIDGE_GUIDE.md).

For a concise mathematical overview of the checked result and the open
bridge, read [one determinant, two kinds of information](lean/MATHEMATICAL_SPINE.md).
For a comparison with Tao's challenge and a separate accounting of useful
side results, see [the current objective ledger](TAO_OBJECTIVES_CURRENT.md).

## 2026-10-24: the analytic tail is discharged; the finite comparison connects

[Phase 24](research/ender_radius_bridge/PHASE24_PROTOCOL.md) proves
`J≤I(P)` for every natural `R` and `P≥2`. A positive potential
`K(x)=log(x+1)/x+log(x+1)−log(x)` pays for each integer summand; its finite
drops telescope. Prime indices form a subset of that integer interval.
No infinite-series interchange or prime-distribution estimate is used.

`ellipse_enderPrimeMassLower_le_counted_upperB` now connects both unchanged
mathematical production expressions on the same actual Gram without a tail
hypothesis. Arithmetic, class-number, strict range, radius and floor-padding
guards remain explicit. `classNumber_ne_one_of_ender_comparison` gives an
exclusion criterion conditional on a strict real numerical comparison.
It does not assume that the saved Arb output supplies that comparison.
Eight controls and full local Lean build (6714 steps) pass.

Numerical enclosure/guard interpretation, universal closure, even cases and
finite classification remain open. No checked cutoff, new numerical run
or change to a production formula/certificate is claimed.
[Human proof](research/ender_radius_bridge/PRIME_MASS_LOWER_GUIDE.md) ·
[Lean source](lean/TenthDiscriminant/PrimeTail.lean).

## 2026-10-24: finite weight conversion and clipping reach the same Gram

[Phase 23](research/ender_radius_bridge/PHASE23_PROTOCOL.md) checks
`F(p)=(S−1/2)A(p)−Q(p)/2` under the production quotient guard, the exact
small-prime split, both integer loss coefficients, padded enumeration and
clipping. Finite geometric and floor-square bounds reduce both losses to
`J=∑_{P<p<R,prime} log(p)/(p(p−1))`. The clipped lower expression reaches
the actual counted `upper_B` **assuming `J≤I`**. Eight controls include
counterexamples to dropping the quadratic loss or quotient guard.

The remaining analytic target is `J≤log(P+1)/P+log(1+1/P)`; it has not
been discharged in Lean. Numerical interpretation, universal closure,
even cases and classification remain open. No production tool, formula,
cutoff or certificate changed.
[Short staircase proof](research/ender_radius_bridge/PRIME_MASS_LOWER_GUIDE.md) ·
[Lean source](lean/TenthDiscriminant/PrimeMassLower.lean).

## 2026-10-24: the factorial identity and scalar lower bound are checked

[Phase 22](research/ender_radius_bridge/PHASE22_PROTOCOL.md) proves
`H(R)=log(product_{r<R} r!)` equals its exact finite Legendre prime-power
sum, including prime `2`. For `R≥2`, an increasing integral envelope
proves the unchanged production `factorial_lower(R)≤H(R)`. Ten controls
include equality at `R=2`, `288=2^5*3^2`, strict power endpoints and rejection
of omitting prime `2`. Full local Lean build passes (6712 steps).

This factorial prime-power sum is **not** the determinant's odd-prime
valuation mass. Small-prime subtraction, weight conversion, higher-power
tail control and clipping still need a connected `prime_mass` theorem.
Numerical certificate interpretation, universal closure and classification
remain open. No production formula, certificate or cutoff changed.
[Short human proof](research/ender_radius_bridge/FACTORIAL_LOWER_GUIDE.md) ·
[Lean source](lean/TenthDiscriminant/FactorialPrimeMass.lean).

## 2026-10-24: the upper ellipse count reaches production `upper_B`

[Phase 21](research/ender_radius_bridge/PHASE21_PROTOCOL.md) proves
`|E(D,rho)| ≤ pi*rho²/sqrt(D)+2rho+(2Y+1)` for `D>0`, integer `rho≥0`,
and `Y=floor(rho/sqrt(D))`. Off-axis points own disjoint open inward cells
of area `sqrt(D)` inside the same disk. The horizontal axis excluding the
origin contributes `2rho` possible points; the vertical axis contributes
`2Y+1`. The theorem handles radius zero exactly and rejects counting axis
points as full inward cells. Endpoint antitonicity supplies the upper count
throughout an interval. Safe upward line-count padding is explicit.

`ellipse_primeMass_log_le_counted_upperB` now joins both geometric counts,
class number one, the actual integer Gram, finite prime mass and unchanged
production upper formula. The factorial lower estimate, Arb certificate
interpretation, universal closure and classification remain open.
[Lean source](lean/TenthDiscriminant/EllipseUpperCount.lean) ·
[human proof](research/ender_radius_bridge/UPPER_BOUND_GUIDE.md).

## 2026-10-24: production `upper_B` is connected to the actual Gram

[Phase 20](research/ender_radius_bridge/PHASE20_PROTOCOL.md) checks the
unchanged `R>rho` upper expression for positive **integer** radii, including
the falling factorials, row-major rectangle, logarithmic integral correction
and Python's exact integer coefficients. Chosen-radius positivity and the
class-number/local-factor chain compose to `∑ 2F(p) log p ≤ upper_B`,
under the explicit premise that its real input `n` bounds the actual ellipse
count. Seven boundary/false-strengthening controls compile. The geometric
`n_up` estimate, factorial lower bound, numerical certificates, universal
closure and classification still require their own proofs.
[Lean source](lean/TenthDiscriminant/EnderUpperB.lean) ·
[short human proof](research/ender_radius_bridge/UPPER_BOUND_GUIDE.md).

## 2026-10-24: the finite local-to-global determinant sandwich is Lean-checked

[Phase 19](research/ender_radius_bridge/PHASE19_PROTOCOL.md) now assembles
the exact factors `p^(2F(p))` for **all distinct odd primes `p<R`** on the
same positive integer ellipse Gram, under squarefree `D≡3 (mod 4)`, class
number one, strict `R<(D+1)/4`, and Ender's chosen-radius guard. Lean proves
the product divides the determinant and its finite logarithmic prime mass
is at most the logarithm of the Hadamard diagonal product. Empty, singleton
and duplicate-prime controls compile. This connects local arithmetic to
real geometry; it does **not** prove the factorial lower estimate, the
recorded Arb interval margins, the universal envelope, or classification.
[Lean source](lean/TenthDiscriminant/PrimeMassAssembly.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#22-the-finite-prime-mass-sandwich).

## 2026-10-24: the chosen-radius cell-area count is Lean-checked

[Phase 18](research/ender_radius_bridge/PHASE18_PROTOCOL.md) proves the
previously paper-only cell-area inequality for the **actual finite ellipse**.
Closed width-one, height-`√D` cells cover the plane by integer floors;
each point in the smaller disk lies in a cell whose center meets the
ellipse inequality. Complex disk volume and finite-union subadditivity
give `π(ρ−δ)²≤|E(D,ρ)|√D`, where `δ=(1+√D)/2` and `ρ≥δ`.
Composing with Phase 17 checks Ender's exact radius gives
`|E(D,ρ)|>3R+S` and positivity/Hadamard of the actual trace-Gram
throughout a certified interval once its upper-endpoint radius guard
is supplied. This does **not** formalize the analytic determinant
comparison, certify Arb inequalities, or classify class-number-one fields.
[Lean source](lean/TenthDiscriminant/EllipseCellArea.lean) ·
[human proof](lean/HUMAN_GUIDE.md#9-the-concrete-ellipse-bridge).

## 2026-10-24: Phase 17 radius algebra, before the area proof

[Phase 17](research/ender_radius_bridge/PHASE17_PROTOCOL.md) proves in Lean
that Ender's exact `1.001` radius guard and the explicit cell-area inequality
force the **strict** `3R+S` point count, including the finite-interval
upper-endpoint transfer to the actual Gram determinant. The cell-covering
area inequality was a stated hypothesis; Phase 18 now proves it. Phase 17
alone was an algebraic/geometric interface, not a checked analytic cutoff or a
classification. [Lean source](lean/TenthDiscriminant/LatticeEllipse.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#9-the-concrete-ellipse-bridge).

## 2026-10-24: class number one now supplies the local Gram valuation

[Phase 16](research/uniform_inert_valuation/PHASE16_PROTOCOL.md) proves
in Lean that, for squarefree `D ≡ 3 (mod 4)`, class number one of the
actual quadratic field implies Ender's exact
`p^(2·valuationWeight R S p)` divisor of the original integer Gram
determinant at every odd prime `p < (D+1)/4`. The proof composes the
residue quotient, maximal-order equivalence, principal-kernel norm,
nonnegative imaginary quadratic norm, and the existing valuation
theorem. `D=15,p=3` yields a checked `classNumber ≠ 1` control.
This closes the previously open *class-number-to-local-valuation*
arrow, **not** the chosen-radius area formalization, analytic cutoff,
or class-number classification. [Lean source](lean/TenthDiscriminant/ClassNumberInertBridge.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#21-the-global-hypothesis-reaches-the-local-determinant).

## 2026-10-24: explicit order equals the maximal integer ring

[Phase 15](research/uniform_inert_valuation/PHASE15_PROTOCOL.md) now
constructs the genuine quadratic number field for squarefree
`D ≡ 3 (mod 4)` and proves in Lean that its maximal integer ring is
isomorphic to `ℤ[T]/(T²-T+(D+1)/4)`. The proof uses the actual field
trace and norm, Phase 14's denominator/parity argument, and an
injective order-to-field map; the norm on the maximal ring agrees
with the repository's `principalNorm`. This closes the previously
open *order-identification* arrow. Phase 16 now checks the next
class-number-to-lifting arrow. Neither the analytic
cutoff nor classification is established. [Lean source](lean/TenthDiscriminant/QuadraticFieldChart.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#20-why-this-is-the-whole-integer-ring).

## 2026-10-24: prospective maximal-order coordinates checked

[Phase 14](research/uniform_inert_valuation/PHASE14_PROTOCOL.md) proves
in Lean that, for squarefree `D ≡ 3 (mod 4)`, rational `a,b` with
integer `2a` and `a²+Db²` have unique coordinates
`a=x+y/2, b=y/2` with `x,y∈ℤ`; the converse is checked too.
`D=15` is a positive control, while `D=9,q=1/3` shows why
squarefreeness matters. This is the arithmetic heart of the
maximal-order argument, **not by itself** the field-to-order equivalence.
Phase 15 now proves that equivalence; the cutoff and classification
remain open.
[Lean source](lean/TenthDiscriminant/MaximalOrderCoordinates.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#19-why-the-half-integral-coordinates-are-forced).

## 2026-10-24: the explicit order's algebraic norm is checked

[Phase 13](research/uniform_inert_valuation/PHASE13_PROTOCOL.md) proves
in Lean that `ℤ[T]/(T²-T+c)` has the power basis `(1,T)` and that
Mathlib's actual `Algebra.norm ℤ (x+yT)` equals `x²+xy+cy²` for every
integer `c,x,y`. Specializing `c=(D+1)/4` makes this *exactly* the
repository's `principalNorm D x y`; `D=15,T` has norm `4`, and
scalars have norm `x²`. This closes Phase 12's formal norm transport.
Phase 13 alone did **not** identify this explicit order with the maximal ring of
integers of the intended quadratic field (Phase 15 now does), so Phase 9's lifting premise,
the cutoff and the classification remain open. [Lean source](lean/TenthDiscriminant/HalfOrderAlgebraicNorm.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#18-the-two-dimensional-norm-chart).

## 2026-10-24: the order's two-dimensional norm chart

[Phase 12](research/uniform_inert_valuation/PHASE12_PROTOCOL.md) checks
`T²=T-c` inside the actual quotient order and the second column of
multiplication by `x+yT`. The determinant of the resulting `2×2`
matrix is exactly `x²+xy+cy²`; `D=15,c=4` is a concrete control.
Phase 13 identifies that matrix determinant with `Algebra.norm`
in the power basis, and Phase 15 identifies the order with the
maximal integer ring. The Phase 9 lifting premise and
the end-to-end classification remain open. [Lean source](lean/TenthDiscriminant/HalfOrderNorm.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#18-the-two-dimensional-norm-chart).

## 2026-10-24: a residue root gives an explicit order quotient

[Phase 11](research/uniform_inert_valuation/PHASE11_PROTOCOL.md) now
checks that for `D ≡ 3 (mod 4)` and odd prime `p`, a root `z²=-D`
modulo `p` yields a surjective ring map from
`ℤ[T]/(T²-T+(D+1)/4)` to `ZMod p`, sending `T` to `(1+z)/2`.
The `D=15,p=3` ramified control has this map although Phase 9's
principal norm lifting fails. Phase 15 now transports this map to
Mathlib's maximal integer ring; composing it with Phase 10 and a
sign-safe norm identity is the remaining arithmetic arrow before
Phase 9's lifting premise. Geometric and analytic links
remain open. [Lean source](lean/TenthDiscriminant/HalfOrderResidue.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#17-from-a-residue-root-to-an-actual-quotient-map).

## 2026-10-23: the abstract class-number-one ideal step is checked

[Phase 10](research/uniform_inert_valuation/PHASE10_PROTOCOL.md) proves in
Lean that a ring map from a number field's integer ring to `ZMod n`
has kernel of ideal norm `n`, and class number one makes that kernel
principal. Its generator has algebraic norm of magnitude `n`; the
`K=ℚ,n=3` control compiles. This does **not** yet turn a root of
`X²+D` into a map from the specific maximal quadratic order, nor
identify the generator's norm with `principalNorm D x y`. Those
specific-field arrows were open at this historical checkpoint; Phases
16 and 18 now close those arithmetic and area links. The analytic cutoff
and classification remain open. [Lean source](lean/TenthDiscriminant/PrincipalIdealBridge.lean) ·
[human proof](lean/HUMAN_GUIDE.md#16-what-class-number-one-actually-buys).

## 2026-10-23: a conditional small-prime norm gate

[Phase 9](research/uniform_inert_valuation/PHASE9_PROTOCOL.md) adds a
conditional global-to-local interface. Lean proves that if every root
of `X²+D` modulo an odd prime `p<(D+1)/4` lifts to a principal norm-`p`
representation, then no root exists and the Phase 8 valuation applies.
It also equates the exact nonsquare guard with quadratic irreducibility.
The norm-lifting premise is **not derived from class number one**;
identifying the maximal order, prime ideals and principality is the
remaining arithmetic bridge. `D=15,p=3` falsifies an unconditional
lifting statement. [Proof](lean/TenthDiscriminant/SmallPrimeBridge.lean) ·
[human explanation](lean/HUMAN_GUIDE.md#15-the-small-prime-gate-without-hiding-the-class-group).

## 2026-10-23: odd-prime nonsquare condition now yields exact valuation

[Phase 8](research/uniform_inert_valuation/PHASE8_PROTOCOL.md) formalizes
the precise local arithmetic premise. In the **same** two residue
coordinates, `t²=-D`; for an odd prime `p`, nonsquareness of `-D` modulo
`p` and Euler's criterion give `t^p=-t`. Freshman's dream then gives
`(x+yt)^p=x-yt` for every pair. Lean transports this back to both integer
coordinates and applies Phase 7's actual Gram theorem, proving
`p^(2*valuationWeight R S p) | det G` for every finite sample set,
rectangle and derivative cutoff. The `D=19,p=3` guard passes and
`D=2,p=3` is a square falsifier. This is a checked **local-nonsquare
valuation theorem**, not by itself a class-number-one theorem. At this
historical checkpoint the global guard and cell-area count were open;
Phases 16 and 18 now check those separate links. The analytic cutoff
and classification remain open.
[Lean theorem](lean/TenthDiscriminant/InertFrobenius.lean).

## 2026-10-23: actual rectangular row-to-Gram bridge

The [preregistered Phase 7](research/uniform_inert_valuation/PHASE7_PROTOCOL.md)
identifies the integer binomial matrix's action on every original
ordinary-derivative row with the jet of `Z^(r-pk) W^s (Z^p-W)^k`.
The original samples, derivative cutoff, row order and factor-two trace
are retained. Bilinearity constructs the previously assumed **integral
two-sided Gram factor**. Lean then proves
`p^(2*valuationWeight R S p) | det G` for every rectangular grid and
finite sample set, **provided** `a^p-conjugate(a)` is coordinatewise
divisible by `p` for every integer pair `a`. Phase 8 above now derives
that premise from an odd-prime nonsquare guard. The Lean geometric area step, analytic cutoff and class-number
classification remain open. [Row identity](lean/TenthDiscriminant/RectangularRowAction.lean) ·
[Gram factor](lean/TenthDiscriminant/RectangularGramFactor.lean).

## 2026-10-23: local conjugation closes a valid sample orbit

The next bounded operator test is preregistered in
[Phase 6](research/uniform_inert_valuation/PHASE6_PROTOCOL.md).
Lean proves conjugation takes any sample satisfying the explicit
coordinatewise `a^p ≡ conjugate(a) (mod p)` premise to another such
sample, and composes this symmetry with the existing ordinary-jet
theorem. Its square is the identity; the non-real `D=19,p=3` control
checks this is not just a real-point tautology. This local orbit does
not prove the premise for all samples or a
global class-number statement. [Lean source](lean/TenthDiscriminant/LocalOperators.lean).

## 2026-10-23: the rectangular integer basis matrix is explicit

Lean now defines the sample-independent binomial coefficient matrix for
`Z^(r-pk)W^s(Z^p-W)^k` in the existing row-major indexing. For `p>0`,
every active term remains in the rectangle, every non-leading term has
an earlier column, the matrix is lower triangular with diagonal `1`,
and its determinant is `1`, including empty rectangles. The full
`4×2,p=3` pilot row is checked. The action on the actual integer Gram
is proved in Phase 7 above; this matrix theorem alone proves no cutoff.
[Lean theorem](lean/TenthDiscriminant/RectangularBasisMatrix.lean) ·
[preregistration](research/uniform_inert_valuation/PHASE5_PROTOCOL.md).

## 2026-10-23: the full ordinary-jet power is checked locally

Lean proves that if all ordinary jets of `H` at a point are divisible
by `p`, then all jets of `B*H^k` are divisible by `p^k`. Applied to
`H=Z^p-W` in the repository's selected quadratic order, this gives
both integer-coordinate factors for every proposed transformed row
under its explicit order-zero Frobenius congruence. A checked Hasse
derivative counterexample guards the derivative convention. At this
Phase 4 checkpoint the uniform premise and analytic/class-number chain
were open; Phases 7–16 now supply the Gram and strict-small-prime links.
[Theorem](lean/TenthDiscriminant/JetPower.lean) ·
[preregistration](research/uniform_inert_valuation/PHASE4_PROTOCOL.md).

## 2026-10-23: exact Ender exponent, conditional on the missing basis

Lean now proves that the proposed row-major exponents
`min(⌊r/p⌋,S-1-s)` sum to the existing `valuationWeight R S p` and
that a specified **integral unimodular two-sided factorization** of the
actual integer rectangular Gram implies
`p^(2*valuationWeight R S p) | det G`. This is checked for all natural
`R,S,p`, including empty grids, but the factorization is an explicit
unproved hypothesis in this earlier theorem. Phase 7 constructs it
under an explicit universal Frobenius premise, without deriving that
premise from inertness. Analytic inequalities and class-number argument
remain open in Lean. [Exact declaration](lean/TenthDiscriminant/RectangularValuation.lean) ·
[preregistration](research/uniform_inert_valuation/PHASE3_PROTOCOL.md).

## 2026-10-23: uniform valuation reconstructed on paper

The [preregistered argument](research/uniform_inert_valuation/PROOF.md)
uses `Z^p-W` and a unitriangular change of the rectangular monomial
basis to derive Ender's full `p^(2F(p)) | det G` for the *same* integer
matrix, under the explicit condition that `X²+D` is irreducible modulo
the odd prime `p`. Lean checks the general unimodular two-sided matrix
factor and, in a follow-up, [all ordinary jets of the single factor
`Z^p-W`](lean/TenthDiscriminant/FrobeniusJet.lean), conditional on its
order-zero congruence. At that checkpoint, the `H^k` product-rule/basis
construction and inertness-to-irreducibility link were not yet in Lean;
the newer power-jet result above closes the product-rule part only. This is a paper proof of an inherited
valuation input, not a new cutoff or a full classification theorem.

## 2026-10-23: local–global determinant bridge (bounded pilot)

For `D>0`, Lean identifies the integer-pair coordinates with the selected
quadratic order `ℤ[√(-D)]`; this does not identify the full ring of integers
for every D.
It also computes the derivative trace-Gram matrix independently in residue
coordinates. For any modulus `m>0`, the local determinant equals the reduction
of the existing integer determinant, and vanishes exactly when `m` divides
that determinant. Samples remain indexed by the original integer-point set:
colliding residues retain their multiplicities. Registered controls check both
this collision issue and the asymmetric `D=3` determinant `12` modulo `3` and
`5`. Separately, a checked fixed-grid theorem proves `9 | det G` for the
canonical `D=19`, `R=4`, `S=2` integer Gram for every finite sample set and
derivative cutoff. For `ellipsePairs 19 5`, `J=2`, its determinant is also
strictly positive. A `D=2`, `p=3` control refutes dropping inertness. This
one-prime toy theorem does not imply Ender's uniform prime-adic lower bound.
The proof and limitations are reported in the
[guide](lean/HUMAN_GUIDE.md#11-local-and-global-arithmetic-views-of-one-gram-matrix)
and [protocol](research/local_global_gram/PROTOCOL.md). At this pilot
checkpoint the general valuation was open; Phase 16 now supplies its
strict-small-prime form, while the classification remains open.

## 2026-10-23: integer-coordinate trace-Gram bridge

For any finite set of distinct integer pairs and positive D, Lean now proves
that the integer-pair derivative trace-Gram matrix, cast entrywise to Real, is
the existing complex `traceGramMatrix` on the image points. Its row-major
rectangular specialization and determinant cast equality follow. On the
integer-radius ellipse this identifies the same determinant whose positivity
the interpolation theorem controls. The proof preserves conjugate W,
ordinary Z-derivatives, zero high-order columns and factor two.

This is **matrix identification**, not inert-prime divisibility. It does not
equate the integer-radius `ellipsePairs` generator with the verifier's
half-integer-radius historical generator, or turn AI review/CI into a full
classification proof. [Proof guide](lean/HUMAN_GUIDE.md#10-the-same-gram-matrix-in-integer-and-complex-coordinates) ·
[protocol](research/integer_gram_bridge/PROTOCOL.md).

## 2026-10-23: geometric count for Ender's chosen radius

The registered [radius proof](research/ender_radius_bridge/PROOF.md) uses
unit-by-√D lattice cells to establish the inherited lower count for every
integer D≥1 and radius rho≥0. For the exact radius chosen by Ender it yields
`card(ellipsePairs D rho) > 3R+S`; at finite intervals the count transfers
from D2 to every D≤D2 by exact set inclusion. Phase 17 additionally checks
that the exact radius plus the explicit area premise give this strict count;
Lean also checks the cardinality transfer and Gram application, plus a D=19,
rho=5 exact control with 21 points. **At this checkpoint** the cell-area
estimate was unformalized; Phase 18 now checks it. The geometric count alone
does not establish the analytic contradiction or class-number classification.
The earlier numerical records are unchanged.

## 2026-10-23: bounded formal ellipse bridge

The registered attempt in `research/lattice_bridge_r1/PROTOCOL.md` adds
`LatticeEllipse.lean`. For positive natural D and integer radius rho, Lean
proves that its bounded finite construction is the full set of integer pairs
with x²+D y²≤rho², that distinct pairs give distinct complex points, and
that the image has the same cardinality. The original rectangular trace-Gram
determinant is positive and satisfies Hadamard **conditional on** the explicit
count `2*(R-1)+(S-1) < card(ellipsePairs D rho)`, R,S≥1 and J≥S. A D=rho=1
control checks all five boundary/axis points. This earlier result was a proof
bridge, not a point-count estimate. The chosen-radius count and integer-matrix
identification were advanced later, as described above; valuation and
classification remain open.

Verification of this exact revision is reported in the associated PR; no
earlier green CI run is evidence for it. The 22 October numerical claims below
are unchanged.

## 2026-10-23: Tao-objective audit and bounded radial replay

`TAO_OBJECTIVE_AUDIT.md` now compares the project's twelve-item status table
with Tao's 20 October challenge and the frozen repository evidence. The main
correction is operational: PR #15 and PR #16 are no longer drafts; they landed
on current `main` at `47ec647` and `4c034f9`. Their checked interpolation
theorem and apparatus audit do not close the arithmetic-to-classification
bridge.

The fixed radial-control suite from `flow/PREREG_RADIAL.txt` was rerun with
Python 3.13.16, python-flint 0.9.0, and SymPy 1.14.0: 9 tests passed in
1.525 seconds. This is a bounded reproducibility check, not a rerun of the
18-case campaign or new numerical evidence. Its registered $O(1/R)$ ceiling
still rules out a cutoff-improvement claim from this bound alone.

The audit labels the Ender route and its $7\times10^{11}$ cutoff as a
**candidate** rather than an achieved classification, keeps the $h\le2$ track
unreviewed, and records that no repository-supported evidence of a Tao-comment
submission was found. See `TAO_OBJECTIVE_AUDIT.md` for the full table and
precise evidence boundaries.

## 2026-10-22: analytic radial correlation follow-up

Derived a moment-only formula and a uniform annulus correlation lemma:
eligible disjoint row pairs contribute a block/diagonal ratio at most
9/25, with sufficient independence checked on the actual point set.
The 18-case campaign certifies 16 cases; 8 have strict savings and 2
fail the sufficient rank guard. The guaranteed normalized saving is
O(1/R), so this bound alone does not improve Ender's leading slope.
No global cutoff or Ender certificate was changed.
Derivation, failures and commands: `ledger/radial_bounds.txt`;
raw output: `ledger/radial_bounds.jsonl`.

## 2026-10-22: determinant structure / prime-power lifts

A separate preregistered finite experiment now varies matrix size,
derivative order and sampling geometry, and measures nested Smith
prime-power layers and disjoint-block Fischer bounds. Of 108 cases,
101 are nonsingular and all 101 improve on ordinary Hadamard.
A genuine h=1 control with strict cutoff and sufficient independence
has v_3(det G)=2F(3), ruling out a uniform extra two units of valuation.
These are finite observations, not an all-dimensional improvement or
a change to Ender's proof. Details, commands and limitations:
`ledger/determinant_lifts.txt`; raw results: `ledger/determinant_lifts.jsonl`.

## Latest: ENDER / FORMIC

Ender's computational campaign is complete: factorials and Legendre's identity replace Dusart, without any prime-distribution estimate.
There are 250 certified intervals on [7e11,1e36], a floor-safe all-D envelope above 1e36 (slope 15/64, initial margin 7.84016),
and a fresh CRT run on [92,7e11) returning only 163. Formic rechecks local arithmetic, geometry, mutations and interval stitching.
Proof, commands and limitations: `ledger/ender.txt`; outputs: `ledger/coverage_ender.txt`, `ledger/asymptotic_ender.txt`,
`ledger/sieve_ender.txt`, `ledger/formic.txt`.
The separate BEAN audit returned GAPS ONLY (`review/BEAN_AUDIT.txt`); the old point-based asymptotic claim is not thereby validated.
Ender's analytic re-audit found no mathematical defect in the new factorial and universal-envelope derivations (`review/ENDER_AUDIT.txt`).
This remains a candidate mathematical argument, not a formalized or human-reviewed theorem. Historical entries below are not the latest status.

## Track GREEN-H1: an L-function-free route to class number one (HYPOTHESIS → under test)

**Idea.** Green's determinant argument (hexagon:2610.00311v2) needs one input: inert primes carry
almost all of the prime mass sum log p / p up to X. Usually that comes from a Siegel zero.
For h(-D)=1 it has an elementary source: every split prime is x^2+xy+((D+1)/4)y^2 with y != 0,
so a lattice-point count bounds split primes up to t by (2t+sqrt t)/sqrt D. No L-functions needed.

**Calculator:** `tools/green_h1.py` (Arb ball arithmetic). Point checks certify a contradiction
(h(-D)=1 impossible) at sample D = 1e6, 1e8, 1e10, 1e14 with R = D*1e14, S = J = R/80.

**Controls passed** (all FAILURES = 0):
- `control_heegner.py`: no contradiction for D = 19, 43, 67, 163 (weak: lower bound is vacuous there).
- `bruteforce_green.py`: exact Gram determinants (PARI) satisfy det>0, det <= Hadamard, v_p(det) >= 2F(p), 21 instances.
- `control_bounds.py`: my aggregated upper bound >= exact log prod G_ii (16 instances); split-count bound and
  min split prime >= (D+1)/4 hold for all genuine h=1 fields up to 1e6 (bound is ~2x loose).
- Tail inequality Gl(p) <= F(p) checked at 7 primes.

**NOT yet established:**
1. Coverage of *every* D >= D0 (only sample points so far) — needs interval version + asymptotic argument.
2. [P1] Rosser–Schoenfeld theta(x) > x(1-1/(2 log x)), x >= 563: quoted from memory, must be checked against the paper.
3. Independent review of each derivation (fresh model / human), then Lean.
4. Below D0: sieve endgame (`tools/sieve_h1.py`, verified to 1e10).
Nothing here may be reported externally until 1–3 close.

## 2026-10-21 (later): ellipse variant GREEN-H1-E (suggested by J. Vilela)
Replace Green's N x N grid by lattice points inside the norm ellipse x^2 + D y^2 <= rho^2 (a disc in C).
Max point size drops by ~D^{1/4}; zero bound via horizontal lines (J >= points/line + #lines).
Point checks (`tools/green_h1_ellipse.py`), certified margins L/U:
square grid: 1.09-1.21 (D=1e6..1e14)  ->  ellipse: 1.26 (1e6), 1.49 (1e8), 1.50 (1e10), 1.47 (1e14), 1.44 (1e20).
Crossover now between D=1e5 (0.91) and 1e6. Same open items 1-4 apply; new ingredients E1-E3 need review + brute-force control.

## 2026-10-21 (evening): self-audit + exact verification
- Rule-0 audit table of the chain recorded in conversation; new ledger nodes needed: genus-theory lemma
  (h=1, |disc|>8 => disc=-D, D prime = 3 mod 4), and the line-slicing zero bound for general point sets.
- `tools/verify_exact.py`: one exact verifier for any point set; checks hypothesis, det>0, Hadamard,
  my aggregated bound, v_p(det)>=2F(p), ellipse point count. 46 cases (ellipse + square, D=7..67): 0 failures.
- `tools/mutation_test.py`: verifier rejects a too-strong valuation claim (M1) and shows det=0 when the
  independence hypothesis is dropped (M3) — the hypothesis is not decorative.
- M2 (Hadamard x1e-6 stronger) NOT caught => Hadamard is loose. Measured slack log(prod G_ii)/log det:
  square ~18-20%, ellipse ~6-10%. The round point set also makes rows closer to orthogonal.
  Open lever: replace Hadamard by a sharper determinant bound.

## Parked
- Track F (function-field calibration over F_q[T]): RH known there (Weil); use to test the method against
  ground truth. Needs Hasse derivatives (char p). Start after integer coverage. MacRae 1971 citation unverified.

## 2026-10-21 18:40: deeper probe
- `tools/verify_exact_large.gp`: exact checks (det>0, Hadamard, v_p >= 2F) on ellipse sets with general rho,
  matrices up to 160 rows, up to 9 inert primes, valuations up to 380: 9 cases, 0 failures (4.5 min).
  Hadamard loss at this scale: log(prod G_ii)/log det = 1.03-1.06.
- Bottleneck at D=1e5 is the split-prime subtraction (7.3 of 24.7 normalized units); N3 bound is ~2x loose
  (2t/sqrt D vs area pi t/(2 sqrt D)). Tightening N3 is the next lever for D0.

## 2026-10-21 22:20 — class number <= 2, elementary route (pre-registered, flow/PREREG_H2.md)
Result (unreviewed): every imaginary quadratic field with |disc| >= 7e4 has h > 2, with no L-functions; below 7e4 PARI
returns exactly the 9 + 18 known fields. Not found in the thread snapshot (higher h there only via QRH or Siegel-zero routes).
Next: independent review of cover_h / asymptotic_h / N3' before any external statement.
